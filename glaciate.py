#!/usr/local/lib/python2.7

import base64
import boto3
import json
import os
from to_s3 import to_s3
from time import gmtime, strftime
from hasher import hashing
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

def dump2json(jsonfile):
    with open('files.txt', 'w') as outfile:
        json.dump(jsonfile, outfile)

def get_s3():
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.download_file('12345supertestbucket', 'tmp_payload.json', '/tmp/test.json')
    except:
        continue


# AccessKey = data["AWS_Access_Key_ID"]
# SecretKey = data["AWS_Secret_Access_Key"]

# Test to see if you can authenticate to AWS

# check local file system for changes (new files or update files)

filedict = dict()

for file in os.listdir(os.getcwd()):
    try:
        if os.path.isfile(file):
            filedict[file] = hashing(file)
        else:
            continue
    except KeyError:
        payload = "File %s already exists in system" % (file)
        logger(payload)

# take filenames from json document

dump2json(filedict)

# compare filedict to json dump from S3.

get_s3()
f = open('/tmp/tmp_payload.json') as data_file:
    data = json.load(

to_s3(filedict)

# check to see if files exist in AWS

# filename = os.path.basename("bigfile.avi")

#payload = "%s %s" % (filename, hashing(filename))
#logger(payload)

# hash files to be transferred keep
# hasher(file)

# upload new files to AWS glacier
# testing with s3 for now

# s3 = boto3.resource('s3')

# upload and replace files

# make log of transfers to and from glacier 


