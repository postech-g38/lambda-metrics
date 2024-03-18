from typing import Dict, Any
import json
import os

from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext
import boto3

client = boto3.client('cognito-idp', region_name='us-west-2')


def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:
    body = json.loads(event['body'])
    username = body['username']
    password = body['password']

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
        'statusCode': 201,
        'body': json.dumps({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expires_in': expires_in
        })
    }
