#!/usr/bin/env python

import boto3
from datetime import datetime as dt
import tempfile as t

bucket_name = 'bucket_name'
bucket = boto3.resource('s3').Bucket(bucket_name)
tempdir = t.mkdtemp()

def build_access_counts_key(date):
    return date.strftime('%Y%m') + '/access_counts.txt'

def build_referrers_text(date):
    return date.strftime('%Y%m') + '/referrers.txt'

def build_user_agents_text(date):
    return date.strftime('%Y%m') + '/user_agents.txt'

