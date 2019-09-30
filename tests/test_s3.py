import boto3
import unittest

from divvy_x import settings


class S3Tests(unittest.TestCase):

    def test_list_all_s3_keys(self):
        print(f"\nBoto3Tests.test_list_all_s3_keys()")
        bucket_name = settings.S3_BUCKET_NAME
        for key in list(self.get_all_s3_keys(bucket_name)):
            print(f"s3://{bucket_name}/{key}")

    def get_all_s3_keys(self, bucket_name):
        """
        Generate the keys in an S3 bucket.
        :param bucket_name: Name of the S3 bucket.
        """
        s3 = boto3.client('s3')
        kwargs = {'Bucket': bucket_name}
        while True:

            # The S3 API response is a large blob of metadata.
            # 'Contents' contains information about the listed objects.
            resp = s3.list_objects_v2(**kwargs)
            try:
                contents = resp['Contents']
            except KeyError:
                return

            for obj in contents:
                yield obj['Key']

            # The S3 API is paginated, returning up to 1000 keys at a time.
            # Pass the continuation token into the next response, until we
            # reach the final page (when this field is missing).
            try:
                kwargs['ContinuationToken'] = resp['NextContinuationToken']
            except KeyError:
                break


if __name__ == '__main__':
    unittest.main()
