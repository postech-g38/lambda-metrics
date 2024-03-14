import pytest

from src.helpers.lambda_event import CognitoEvent


def test_cognito_event():
    # arrange
    event = {
        "triggerSource": "testTrigger",
        "userPoolId": "testPool",
        "userName": "testName",
        "callerContext": {
            "clientId": "12345"
        },
        "response": {}
     }
    # act
    obj = CognitoEvent(**event)
    # assert
    obj.triggerSource == event["triggerSource"]
    obj.userPoolId == event["userPoolId"]
    obj.callerContext['clientId'] == event["callerContext"]['clientId']
    obj.response == {}
    