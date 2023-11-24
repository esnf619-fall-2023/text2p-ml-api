import aws_cdk as cdk
from constructs import Construct
from stack.t2p_app_stack import T2pAppStack


class T2pPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        appStack = T2pAppStack(self, "T2pAppStack")
