#!/usr/bin/env python3
import aws_cdk as cdk
from stack.t2p_pipeline_stack import T2pPipelineStack
from constants import AWS_ACCOUNT_NUMBER, AWS_REGION

app = cdk.App()
T2pPipelineStack(app, "T2pPipelineStack",
    env=cdk.Environment(account=AWS_ACCOUNT_NUMBER, region=AWS_REGION)
)

app.synth()