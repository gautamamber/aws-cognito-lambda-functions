import boto3
client = boto3.client('cognito-idp')
def forgot_password_confirm(event, context):
    response = client.confirm_forgot_password(
    ClientId='4i6rhs3ssfjfa3leg3ievnjuuq',
    
    Username=event['Username'],
    ConfirmationCode='050130',
    Password=event['Password'],
    
    )
    return response

