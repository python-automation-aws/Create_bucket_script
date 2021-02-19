import boto3
aws_mg_con=boto3.session.Session(profile_name='username')
s3_client=aws_mg_con.client(service_name='s3',region_name='us-west-2')

#here whatever you have mentioned the region in config file there bucket will create.

session_region=aws_mg_con.region_name

def create_bucket_name(buketprefix):
    bucket_join="".join([buketprefix,"-"])
    bucket_name=  "".join([bucket_join,datetime.datetime.now().strftime('%Y-%d-%m')])
    return bucket_name

get_bucket=create_bucket_name(input("please enter the bucket name"))

def bucket():
    s3_bucket=s3_client.create_bucket(Bucket=get_bucket,
                                          CreateBucketConfiguration={
                                              'LocationConstraint':session_region
                                          })
    return bucket
print(bucket())
