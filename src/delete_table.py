import boto3
client = boto3.client('dynamodb')
def lambda_handler(event, context):
    response = client.delete_table(
    TableName='helloo'
    )
    return response
    