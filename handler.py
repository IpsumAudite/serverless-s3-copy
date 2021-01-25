import json
import boto3
import datetime
import os

s3_client = boto3.client("s3")

def s3Copy(event, context):
    #Names of the buckets taken from the serverless.yml file
    upload_bucket = os.environ['uploadBucket']
    receiving_bucket = os.environ['receivingBucket']
    
    #Show the information about the object that was uploaded and will be subsequently copied
    print("Uploaded object :", event)
    
    #Extract the name of the file that was uploaded from the event payload
    file_name = event['Records'][0]['s3']['object']['key']

    #List out the items in the bucket to validate that the .tar and .sig are both there
    file_list = s3_client.list_objects(Bucket=upload_bucket)
    
    #Object to be copied
    source_object = {'Bucket': upload_bucket, 'Key': file_name}

    #Copy command
    s3_client.copy_object(
        CopySource=source_object, 
        Bucket=receiving_bucket, 
        Key=file_name
    )
    
    #Delete file from source bucket after copy
    s3_client.delete_object(
        Bucket=upload_bucket,
        Key=file_name
    )

    body = {
        "message": "Your function executed - check cloud watch to ensure there are no errors",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
