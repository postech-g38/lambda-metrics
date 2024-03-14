import pytest

from src.lambda_function import lambda_handler
from tests.manual.lambda_event.cognito import LAMBDA_EVENT_COGNITO


def test_lambda_handler():
    # arrange
    # act
    result = lambda_handler(LAMBDA_EVENT_COGNITO, None)
    # assert
    assert result == LAMBDA_EVENT_COGNITO
