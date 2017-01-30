#!/usr/bin/env python

import boto3
import tempfile as t
import re
import os
import sys



bucket_name = sys.argv[1]
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

def log_object_keys(bucket_name, s3):
    objects = s3.meta.client.list_objects_v2(Bucket=bucket_name, Prefix='logs/2')
    return [o['Key'] for o in objects['Contents']]

"""
obj_keys = [o.key for o in bucket.objects.all()] # all objects
log_file_keys = filter(lambda obj_key: re.search('^logs/\d{4}', obj_key), obj_keys)

tempdir = t.mkdtemp()

log_file_key_name_tuples = map(lambda k: {'key': k, 'filename': re.search('^logs/(.+)',k).group(1)}, log_file_keys)


print(tempdir)

for k in log_file_key_name_tuples: 
    bucket.download_file(k['key'], tempdir + '/' + k['filename'])

return [tempdir + '/' + k['filename'] for k in log_file_key_name_tuples]
"""


"""
files = os.listdir('logs') 

def parse_log_line(line):
    line_regex='^[^ ]+ [^ ]+ \[(.+)\] ([^ ]+) [^ ]+ [^ ]+ ([^ ]+) ([^ ]+) \"([^\"]*)\" (\d{3}) [^ ]+ [^ ]+ [^ ]+ [^ ]+ [^ ]+ \"([^\"]*)\" \"([^\"]*)\" .+\r?\n$'
    r = re.search(line_regex, line)
    return {"time": r.group(1), \
            "remote_ip": r.group(2), \
            "operation": r.group(3), \
            "key": r.group(4), \
            "request_url": r.group(5), \
            "http_status": r.group(6), \
            "referrer": r.group(7), 
            "user_agent": r.group(8)}

def access_logs(log_file_paths):
    access=[]
    for path in log_file_paths:
        with open('logs/' + path, 'r') as f:
            def filter_code(log_map): 
                return log_map['key'].endswith('.html') and \
                       log_map['operation'] == 'WEBSITE.GET.OBJECT' and \
                       (not 'Googlebot' in log_map['user_agent'] and \
                        not 'Baiduspider' in log_map['user_agent'] and \
                        not 'bingbot' in log_map['user_agent']) and \
                       log_map['http_status'] == "200"
            access = access + filter(lambda e: filter_code(e), [parse_log_line(l) for l in f.readlines()])
    return access

def cnt(d, e):
    d[e] = d[e] + 1 if d.has_key(e) else 1
    return d
a = access_logs(files)

result = {"keys": reduce(lambda acc, c: cnt(acc,c), [e['key']for e in a], {}), \
          "referrers": reduce(lambda a, b: cnt(a,b), [e['referrer'] for e in a], {}), \
          "user_agents": set([e['user_agent'] for e in a])}
"""
