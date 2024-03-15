from typing import Dict, Any

from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext


def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:
    print(f"PoolID: {event['userPoolId']} | ClientID: {event['callerContext']['clientId']} | UserName: {event['userName'][:15]}")
    return event
