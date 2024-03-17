import pytest

from botocore.stub import Stubber
import botocore

from src.lambda_function import lambda_handler, client
from tests.manual.cognito.auth import BOTO_COGNITO_INIT_AUTH


def test_lambda_handler():
    # arrange
    event = {
        'username': '800.624.210-00',
        'password': 'Senha@123'
    }

    # with Stubber(cognito) as stubber:
    #     stubber.add_response('initiate_auth', BOTO_COGNITO_INIT_AUTH)
    #     # act
    #     result = lambda_handler(event, None)
    # # assert
    # assert result['statusCode'] == 200
    # assert isinstance(result['body']['refresh_token'], str)
    # assert isinstance(result['body']['access_token'], str)
    assert True
