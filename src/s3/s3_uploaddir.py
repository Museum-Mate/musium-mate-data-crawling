import os
import json

import boto3

# Load secrets.json
with open('../secrets.json') as f:

    json_data = json.load(f)

#####################################################
BUCKET_NAME = json_data['BUCKET_NAME']
REGION_NAME = json_data['BUCKET_REGION']
ACCESS_KEY = json_data['AWS_ACCESS_KEY']
SECRET_KEY = json_data['AWS_SECRET_KEY']
#####################################################

PATH = '/Users/geun/Documents/dev/python/mume/musium-mate-data-crawling/data'
 
def upload_files(path):
    session = boto3.Session(
        region_name=REGION_NAME,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
 
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
 
if __name__ == "__main__":
    upload_files(PATH)