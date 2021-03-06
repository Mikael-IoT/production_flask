import os

import boto3
import time

def get_resource():
    return boto3.resource('dynamodb',
                          # These can NOT leak, if push to git, replace with nonsense
                          aws_access_key_id=os.environ['AWS_KEY'],
                          aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
                          region_name='eu-north-1')


def get_all_readings():
    client = get_resource()
    table = client.Table('temp_readings')
    response = table.scan()
    return response['Items']
