FROM apache/airflow:2.2.5
RUN pip3 install Faker numpy boto3 botocore
