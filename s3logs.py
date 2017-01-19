#!/usr/bin/env python

import s3
import tempfile as t
import re

bucket_name = 'foobar'

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

objs = bucket.objects.all() # all objects

tempdir = t.mkdtemp() # dir
# c = filter(lambda n: re.search('^logs/\d{4}', n), aa)
#  aa = [c.key for c in a]

# map(lambda e: re.search('^logs/(.+)',e).group(1), filter(lambda n: re.search('^logs/\d{4}', n), aa))

