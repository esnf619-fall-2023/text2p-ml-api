import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    # Log the received event
    logger.info('Received event: ' + json.dumps(event))

    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }