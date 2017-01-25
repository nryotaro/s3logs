#!/usr/bin/env python

import boto3
# logs/2017-01-17-01-32-38-F21D0BA21E01C7C3

bucket_name = sys.argv[1] 

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

class S3Obj:
  def write(self, obj_bytes): 
     self.obj_bytes = obj_bytes

