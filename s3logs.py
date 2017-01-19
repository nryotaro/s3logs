#!/usr/bin/env python

import s3

bucket_name = 'foobar'

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

objs = bucket.objects.all() # all objects


