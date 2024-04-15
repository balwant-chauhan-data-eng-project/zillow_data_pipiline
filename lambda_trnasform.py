import json
import pandas as pd
import tempfile
import boto3
from io import StringIO

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Extracting bucket and object key information from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Defining the target bucket and file name
    target_bucket = 'cleaned-data-zone-csv-bucket-from-lambda'

    # Extracting the date part from the object key
    data_parts = object_key.split('/')
    file_name_parts = data_parts[-1].split('_')[:3]
    file_name = '_'.join(file_name_parts)
    file_key = f'transformed_data/{file_name}.csv'

    # Waiting for the object to exist in the source bucket
    waiter = s3_client.get_waiter('object_exists')
    waiter.wait(Bucket=source_bucket, Key=object_key)

    # Fetching the new data from the source bucket
    response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
    data = response['Body'].read().decode('utf-8')

    # Convert new data to DataFrame
    df = pd.read_json(data, orient='records')

    try:
        # Read existing data from S3
        response = s3_client.get_object(Bucket=target_bucket, Key=file_key)
        existing_data = pd.read_csv(response['Body'])
    except s3_client.exceptions.NoSuchKey:
        # If the file does not exist, create a new DataFrame
        existing_data = pd.DataFrame()

    # Concatenate new data with existing data
    updated_data = pd.concat([df, existing_data], ignore_index=True)

    # Convert updated data to CSV string
    csv_data = updated_data.to_csv(index=False)

    # Upload the updated data to S3
    s3_client.put_object(Bucket=target_bucket, Key=file_key, Body=csv_data)

    return {
        'statusCode': 200,
        'body': json.dumps('Data appended and updated in S3.')
    }
