import boto3
client = boto3.client('cognito-idp')
def forgot_password(event, context):
	response = client.forgot_password(
    ClientId='4i6rhs3ssfjfa3leg3ievnjuuq',
    Username=event['Username'],
	)
	return response