import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.aws_s3 import Bucket

class T2pAppStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = Bucket(self, "T2pBucket")

        Function(self, "LambdaFunction",
            runtime=Runtime.PYTHON_3_8,
            handler="predict.handler",
            code=Code.from_asset("src/functions"),
            environment={
                "BUCKET_NAME": bucket.bucket_name
            }
        )