import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_lambda import Code, Runtime, Function
from aws_cdk.aws_s3 import Bucket
from constants import MODEL_FILE_NAME

class T2pAppStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, env_name: str, **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        bucket = Bucket(self, "T2pBucket", bucket_name=f"{env_name}-t2p-ml-model")

        Function(self, "LambdaFunction",
            function_name=f"{env_name}-t2p-ml-predict",
            handler="index.handler",
            code=Code.from_asset("src/functions"),
            runtime=Runtime.PYTHON_3_8,
            environment={
                "BUCKET_NAME": bucket.bucket_name,
                "MODEL_FILE_NAME": f"{env_name}-MODEL_FILE_NAME"
            }
        )
        
        from aws_cdk import aws_lambda_python as _lambda_python
