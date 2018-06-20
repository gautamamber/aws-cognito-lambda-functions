import boto3
import json
client = boto3.client('cognito-idp')

def change_password(event, context):
    response = client.change_password( 
    PreviousPassword = event['PreviousPassword'],
    ProposedPassword = event['ProposedPassword'],
    AccessToken = event['AccessToken']
    )
   
    return response
    
    
    
    
    
