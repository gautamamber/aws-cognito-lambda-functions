import boto3
client = boto3.client('cognito-idp')

def login(event, context):
    response = client.initiate_auth(
    AuthFlow='USER_PASSWORD_AUTH',
     AuthParameters={
       "USERNAME" : event['Username'],
       "PASSWORD" : event['Password'],
    },
    
    ClientId='4i6rhs3ssfjfa3leg3ievnjuuq',
   
    )
    return response
