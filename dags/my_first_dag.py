# [START import_module]

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Pendulum is a Python package to ease datetimes manipulation
import pendulum

# Operators; we need this to operate!
from airflow.operators.python import PythonOperator

# Python module for data weblog generation 
from weblog_gen import generate_log

# Other packages for AWS connection and data processing
import os
import boto3
from botocore.exceptions import ClientError
import logging

# [END import_module]

# [START instantiate_dag]
with DAG(
    'my_first_dag',
    # [START default_args]
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={'retries': 2},
    # [END default_args]
    description='ETL DAG tutorial',
    schedule_interval=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=['example'],
) as dag:
    # [END instantiate_dag]

    # [START weblog_function]
    def f_generate_log(*op_args, **kwargs):
        ti = kwargs['ti']
        lines = op_args[0]
        logFile = generate_log(lines)
        ti.xcom_push(key='logFileName', value=logFile)
    # [END weblog_function]

    # [START s3_upload_file function]
    def s3_upload_file(**kwargs):
        ti = kwargs['ti']
        bucketName = kwargs['bucketName']
        fileName = ti.xcom_pull(task_ids='weblog', key='logFileName')
        objectName = os.path.basename(fileName)

        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(fileName, bucketName, objectName)
        except ClientError as e:
            return False
        return True
    # [END s3_upload_file function]
            
    ### Tasks ###

    create_weblog_task = PythonOperator(
        task_id='weblog',
        python_callable=f_generate_log,
        op_args = [30],
    )
        
    s3_upload_log_file_task = PythonOperator(
        task_id = 's3_upload_log_file',
        python_callable=s3_upload_file,
        op_kwargs = {'bucketName': 'baalti123'},
    )

    create_weblog_task >> s3_upload_log_file_task

