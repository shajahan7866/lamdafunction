import json

def lambda_handler(event, context):
    # TODO implement
    print("welcome to Tahaan world")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

