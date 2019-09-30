import os

if os.getenv('AWS_ACCESS_KEY_ID') is None:
    raise ValueError("environment variable AWS_ACCESS_KEY_ID is undefined")
else:
    print("environment variable AWS_ACCESS_KEY_ID is defined")
if os.getenv('AWS_SECRET_ACCESS_KEY') is None:
    raise ValueError("environment variable AWS_SECRET_ACCESS_KEY is undefined")
else:
    print("environment variable AWS_SECRET_ACCESS_KEY is defined")
if os.getenv('AWS_DEFAULT_REGION') is None:
    raise ValueError("environment variable AWS_DEFAULT_REGION is undefined")
else:
    print("environment variable AWS_DEFAULT_REGION is defined")

S3_BUCKET_NAME = 'sbecker-11-divvy'
