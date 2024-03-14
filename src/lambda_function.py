from typing import Dict, Any

from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext

from src.helpers.lambda_event import CognitoEvent


def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:
    cognito = CognitoEvent(**event)
    print(cognito)
    return event
