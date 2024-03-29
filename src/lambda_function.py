from typing import Dict, Any
import os

from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext
import boto3

client = boto3.client('cognito-idp', region_name='us-west-2')


def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:

    username = event['username']
    password = event['password']

    response = client.initiate_auth(
        ClientId=os.getenv('COGNITO_POOL_CLIENT_ID'),
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        },
        ClientMetadata={
            'username': username,
            'password': password
        }
    )

    refresh_token = response['AuthenticationResult']['RefreshToken']
    access_token = response['AuthenticationResult']['AccessToken']
    expires_in = response['AuthenticationResult']['ExpiresIn']

    return {
        'statusCode': 200,
        'body': {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expires_in': expires_in
        }
    }
