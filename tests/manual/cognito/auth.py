
BOTO_COGNITO_INIT_AUTH = {
    'ChallengeName': 'DEVICE_PASSWORD_VERIFIER',
    'Session': 'string',
    'ChallengeParameters': {
        'string': 'string'
    },
    'AuthenticationResult': {
        'AccessToken': 'string',
        'ExpiresIn': 123,
        'TokenType': 'string',
        'RefreshToken': 'string',
        'IdToken': 'string',
        'NewDeviceMetadata': {
            'DeviceKey': 'string',
            'DeviceGroupKey': 'string'
        }
    }
}
