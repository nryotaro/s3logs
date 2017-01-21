#!/usr/bin/env python

import boto3
import tempfile as t
import re

"""
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

return [tempdir + '/' + k['filename'] for k in log_file_key_name_tuples]
"""

files = ["2017-01-14-15-17-49-A87702DEE4890EC6", "2017-01-15-00-26-01-D6E9D8DFD6946B9B"]

def parse_log_line(line):
    line_regex='^[^ ]+ [^ ]+ \[(.+)\] [^ ]+ [^ ]+ [^ ]+ ([^ ]+) ([^ ]+) \"([^\"]*)\" (\d{3}) [^ ]+ [^ ]+ [^ ]+ [^ ]+ [^ ]+ \"([^\"]*)\" \"([^\"]*)\" .+\r?\n$'
    r = re.search(line_regex, line)
    return {"time": r.group(1), "operation": r.group(2), "key": r.group(3), "request_url": r.group(4), "http_status": r.group(5), "referrer": r.group(6), "user_agent": r.group(7)}

for a in files:
    with open("logs/" + a, "r") as f:
        for b in f.readlines():
            print(parse_log_line(b))
