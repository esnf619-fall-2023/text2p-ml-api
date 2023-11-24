import aws_cdk as core
import aws_cdk.assertions as assertions

from pipeline.text2p_ml_api_stack import Text2PMlApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in text2p_ml_api/text2p_ml_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Text2PMlApiStack(app, "text2p-ml-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
