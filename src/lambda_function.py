from typing import Dict, Any
import os

from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext
import boto3

client = boto3.client('cognito-idp', region_name='us-west-2')


def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:

    response = client.initiate_auth(
        ClientId=os.getenv('COGNITO_POOL_CLIENT_ID'),
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': event['username'],
            'PASSWORD': event['password']
        },
    )

    access_token = response['AuthenticationResult']['AccessToken']
    expires_in = response['AuthenticationResult']['ExpiresIn']
    refresh_token = response['AuthenticationResult']['RefreshToken']

    return {
        'statusCode': 200,
        'body': {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expires_in': expires_in
        }
    }
