import boto3
client =  boto3.client('cognito-idp')
def handler(event, context):
	response = client.sign_up(
    ClientId='4i6rhs3ssfjfa3leg3ievnjuuq',
    Username=event['Username'],
    Password=event['Password'],
    UserAttributes = [
            {
                'Name' : "nickname",
                'Value' : event['nickname']
            },
            {
                'Name' : "phone_number",
                'Value' : event['phone_number']
            },
            {
                'Name' : "email",
                'Value' : event['Username']
            }
        ]
        
	)
	return response