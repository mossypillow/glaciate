#!/bin/python

import boto3, botocore

def to_s3(payload):
    ''' description: Upload a file to s3.
    '''
# Module that sends information from hash file (payload) to s3
    try:
        s3 = boto3.resource('s3')
        data = open('tmp/tmp_payload.json', 'rb')
        s3.Bucket('12345supertestbucket').put_object(Key='tmp_payload.json', Body=data)
        print(data)

    except botocore.exceptions.ClientError, fault:
        raise
    except Exception, fault:
        raise

def from_s3():
# Module that receives information from s3 resources
    ''' description: Downloads payload from s3.
    '''
    try:
        s3 = boto3.resource('s3')
        data = open('tmp/cur_s3.json', 'w')
        s3.meta.client.download_fileobj('12345supertestbucket', 'tmp_payload.json', data)
    except botocore.exceptions.ClientError, fault:
        raise
    except Exception, fault:
        raise




