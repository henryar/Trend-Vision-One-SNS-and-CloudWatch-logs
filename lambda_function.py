import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Lambda function invoked with event: %s", json.dumps(event))
    
    try:
        # Extract SNS message
        for record in event.get("Records", []):
            if record.get("EventSource") == "aws:sns":
                sns_message = record.get("Sns", {}).get("Message", "No message")
                logger.info("Received SNS message: %s", sns_message)
                
        response_message = "SNS message processed successfully."
        
        logger.info("Processing completed successfully.")
        return {
            'statusCode': 200,
            'body': json.dumps(response_message)
        }
    except Exception as e:
        logger.error("Error processing SNS event: %s", str(e), exc_info=True)
        return {
            'statusCode': 500,
            'body': json.dumps("Internal Server Error")
        }
