import boto3
import json
import uuid

dynamodb = boto3.resource('dynamodb')
def create(event, context):
       
    table = dynamodb.Table("Gautamm")
    userid = str(uuid.uuid4())

    
    item = {
        
        "id" : userid,
       "name":event['name'],
       "lastname" : event["lastname"]
       
    }

    # write the item to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item),
        "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": "true"
        }
    }

    return response