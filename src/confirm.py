import boto3
client =  boto3.client('cognito-idp')
def confirm(event, context):
    response = client.confirm_sign_up(
        ClientId='4i6rhs3ssfjfa3leg3ievnjuuq',
        
        Username=event['Username'],
        ConfirmationCode='547467'
    )
    return response