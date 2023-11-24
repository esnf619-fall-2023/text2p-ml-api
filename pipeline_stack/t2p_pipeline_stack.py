import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from pipeline_stack.t2p_pipeline_app_stage import T2pPipelineAppStage


class T2pPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(self, "T2pPipeline",
                                pipeline_name="T2pPipeline",
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.git_hub("esnf619-fall-2023/text2p-ml-api", "main", authentication=cdk.SecretValue.secrets_manager("dev/text2p/github-token")),
                                                commands=["npm install -g aws-cdk",
                                                          "python -m pip install -r requirements.txt",
                                                          "cdk synth"]
                                                )
                                )

        wave = pipeline.add_wave("wave")
        wave.add_stage(T2pPipelineAppStage(self, "qa",
                                          env=cdk.Environment(account="802697717686", region="us-east-1")))
        wave.add_stage(T2pPipelineAppStage(self, "prod",
                                          env=cdk.Environment(account="802697717686", region="us-east-1")))
