import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, ManualApprovalStep
from stack.t2p_pipeline_app_stage import T2pPipelineAppStage
from constants import AWS_ACCOUNT_NUMBER, AWS_REGION


class T2pPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(self, "T2pPipeline",
                                pipeline_name="T2pPipeline",
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.git_hub("esnf619-fall-2023/text2p-ml-api", "main", authentication=cdk.SecretValue.secrets_manager("github-access-token-secret")),
                                                commands=["npm install -g aws-cdk",
                                                          "python -m pip install -r requirements.txt",
                                                          "cdk synth"]
                                                )
                                )
        
        # add qa envoironment stage
        staging_wave = pipeline.add_wave("staging-wave")
        staging = T2pPipelineAppStage(self, "staging", env=cdk.Environment(account=AWS_ACCOUNT_NUMBER, region=AWS_REGION))
        staging_wave.add_stage(staging)
        
        # add prod envoironment stage with a mnual approval step
        prod_wave = pipeline.add_wave("prod-wave")
        prod = T2pPipelineAppStage(self, "prod", env=cdk.Environment(account=AWS_ACCOUNT_NUMBER, region=AWS_REGION))
        prod_wave.add_stage(prod, pre=[ManualApprovalStep('ManualApproval', comment="Approve to deploy to prod")])
