import uuid

import boto3

ACCESS_KEY = 'AKIAVZNZLSPNWFPJ7EMX'
SECRET_KEY = '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'
bucket = 'vertuhouse-dev'


def upload_image(image):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    object_name = f'{uuid.uuid1()}.jpg'
    try:
        s3.put_object(Body=image, Bucket=bucket, Key=object_name)
        return f'http://{bucket}.s3.amazonaws.com/{object_name}'
    except FileNotFoundError:
        print("The file was not found")
        return False
