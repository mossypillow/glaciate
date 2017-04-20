#!/usr/local/lib/python2.7

import base64
import boto3
import json
import os
from time import gmtime, strftime
from hasher import hashing
import paramiko
from pprint import pprint

def timestamp():
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return time

def logger(payload):
    if not os.path.isfile("logfile.txt"):
        f = open("logfile.txt","w+")
        cur_time = timestamp()
        print(cur_time)
        f.write("%s %s \n" % (payload, cur_time))
        f.close()
    else:
        f = open("logfile.txt","a")
        cur_time = timestamp()
        print(cur_time)
        f.write("%s %s \n" % (payload, cur_time))
        f.close()

# load options from config file
# with open('config.json') as data_file:
#     data = json.load(data_file)
# pprint(data)

# AccessKey = data["AWS_Access_Key_ID"]
# SecretKey = data["AWS_Secret_Access_Key"]

# Test to see if you can authenticate to AWS

# key = paramiko.RSAKey(data=base64.b64decode(b'rsakey'))

# check local file system for changes (new files or update files)


# keep human readible log of files sent to glacier
# if fileisnew then:

for file in os.listdir(os.getcwd()):
    print(file)

filename = os.path.basename("bigfile.avi")

payload = "%s %s" % (filename, hashing(filename))

logger(payload)

# hash files to be transferred keep
# hasher(file)

# upload new files to AWS glacier
# testing with s3 for now

# s3 = boto3.resource('s3')

# upload and replace files

# make log of transfers to and from glacier 


