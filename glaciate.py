#!/usr/local/lib/python2.7

import boto3
import json
import hasher
from pprint import pprint

# load options from config file
with open('config.json') as data_file:
    data = json.load(data_file)
pprint(data)

# check local file system for changes (new files or update files)
# keep human readible log of files sent to glacier
# if fileisnew then:


# hash files to be transferred keep
# hasher(file)

# upload new files to AWS glacier

# upload and replace files
