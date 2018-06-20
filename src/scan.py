import json
import  boto3
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    table = dynamodb.Table('Gautamm')
    result = table.scan()
    """
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items']),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true"
        }
    }
    """
    response =  json.dumps(result['Items'])

    return response

    
