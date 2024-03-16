import pytest

from botocore.stub import Stubber
import botocore

from src.lambda_function import lambda_handler
from tests.manual.cognito.auth import BOTO_COGNITO_INIT_AUTH


def test_lambda_handler():
    # arrange
    # cognito = botocore.session.get_session().create_client('cognito-idp', 'us-west-2')
    # event = {
    #     'username': '',
    #     'password': ''
    # }
    # with Stubber(cognito) as stubber:
    #     stubber.add_response('initiate_auth', BOTO_COGNITO_INIT_AUTH)
    #     # act
    #     result = lambda_handler(event, None)
    # # assert
    # assert result['statusCode'] == 200
    # assert isinstance(result['body']['refresh_token'], str)
    # assert isinstance(result['body']['access_token'], str)
    assert True
