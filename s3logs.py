#!/usr/bin/env python

import boto3
import tempfile as t
import re

bucket_name = 'bucket_name'

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

obj_keys = [o.key for o in bucket.objects.all()] # all objects
log_file_keys = filter(lambda obj_key: re.search('^logs/\d{4}', obj_key), obj_keys)

tempdir = t.mkdtemp()

log_file_key_name_tuples = map(lambda k: {'key': k, 'filename': re.search('^logs/(.+)',k).group(1)}, log_file_keys)


print(tempdir)

for k in log_file_key_name_tuples: 
    bucket.download_file(k['key'], tempdir + '/' + k['filename'])
