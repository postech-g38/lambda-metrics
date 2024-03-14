from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class CognitoEvent:
    triggerSource: str
    userPoolId: str
    userName: str
    callerContext: Dict[str, str]
    response: Dict[str, Any]

    def __str__(self) -> str:
        return f"PoolID: {self.userPoolId} | ClientID: {self.callerContext['clientId']} | UserName: {self.userName[:15]}"
