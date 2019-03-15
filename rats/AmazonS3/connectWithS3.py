import boto3
import os
#from boto3.s3.connection import S3Connection




def connectWithS3():
    print (os.environ['AWS_SECRET_ACCESS_KEY'])
    # Create an S3 client
    #s3 = boto3.client('s3', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    #aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
    #s3 = S3Connection(os.environ['AWS_ACCESS_KEY_ID'], os.environ['AWS_SECRET_ACCESS_KEY'])

    s3 = boto3.client('s3')

    # Call S3 to list current buckets
    response = s3.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list
    print("Bucket List: %s" % buckets)
    return "Bucket List: %s" % buckets;

