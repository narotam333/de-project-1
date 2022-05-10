import argparse
import time

# Importing libraries to generate fake or random data
from faker import Faker
import numpy

def generate_log(lines):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    outFileName = 'weblog_'+timestr+'.log'

    f = open(outFileName,'w')

    fake = Faker()

    resp = ["200", "404", "500"]

    ip = ["82.97.162.126", "222.47.188.202", "88.110.233.7", "139.237.45.178", "147.209.209.28", "217.103.241.164", "195.68.20.123", "213.213.63.6", "61.106.82.98", "205.207.199.182"]

    agent = ["Mozilla/5.0 (iPad; CPU iPad OS 9_3_5 like Mac OS X) AppleWebKit/533.0 (KHTML, like Gecko) CriOS/58.0.820.0 Mobile/53K104 Safari/533.0", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/532.1 (KHTML, like Gecko) CriOS/19.0.827.0 Mobile/62X374 Safari/532.1", "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_6_0 rv:5.0; crh-UA) AppleWebKit/532.8.6 (KHTML, like Gecko) Version/5.0.3 Safari/532.8.6", "Opera/8.74.(Windows 98; Win 9x 4.90; ast-ES) Presto/2.9.167 Version/12.00", "BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba", "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36"] 

    for i in range(lines):
    
        #clientIP = fake.ipv4_public()
        clientIP = numpy.random.choice(ip, p = [0.4, 0.1, 0.2, 0.01, 0.06, 0.03, 0.05, 0.05, 0.05, 0.05])
        ident = fake.user_name()
        user = fake.user_name()
        tm = time.strftime("%H:%M:%S")
        httpMethod = fake.http_method()
        uri = fake.uri()
        response = numpy.random.choice(resp, p = [0.8, 0.1, 0.1])
        size = numpy.random.randint(50, 5000)
        referer = uri
        #userAgent = fake.user_agent()
        userAgent = numpy.random.choice(agent, p = [0.3, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1])

        f.write('%s %s %s %s "%s %s HTTP/1.0" %s %s "%s" "%s"\n' % (clientIP, ident, user, tm, httpMethod, uri, response, size, referer, userAgent))
        f.flush()
    
    return outFileName

if __name__ == '__main__':
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Weblog generation')

    # Add the arguments
    my_parser.add_argument("-n",
                       dest = 'num_lines',
                       type = int,
                       default = 10,
                       help="Number of lines to generate")

    # Execute the parse_args() method
    args = my_parser.parse_args()

    # No. of lines to generate
    lines = args.num_lines
    generate_log(lines)

