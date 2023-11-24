#!/usr/bin/env python3
import aws_cdk as cdk
from stack.t2p_pipeline_stack import T2pPipelineStack

app = cdk.App()
T2pPipelineStack(app, "T2pPipelineStack",
    env=cdk.Environment(account="802697717686", region="us-east-1")
)

app.synth()