import json
import urllib.request
from io import StringIO
import pandas as pd
import boto3
def main():
    aws_access_key_id = 'access key'
    aws_secret_access_key = 'secret key'
    aws_region = 'region'

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    res = urllib.request.urlopen(urllib.request.Request(
        url='https://swapi.dev/api/people/',
        headers={'Accept': 'application/json'},
        method='GET'))
    res_json = json.loads(res.read().decode())

    df = pd.DataFrame(res_json['results'])

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)


    bucket_name = 'bucket-name'
    s3.put_object(
        Bucket=bucket_name,
        Key='files/df.csv',
        Body=csv_buffer.getvalue()
    )

main()