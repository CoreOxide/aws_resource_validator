from typing import Literal
from datetime import datetime


EventTypeType = Literal['ANSWERED', 'BUSY', 'COMPLETED_CALL', 'FAILED', 'INITIATED_CALL', 'NO_ANSWER', 'RINGING']
PinpointSMSVoiceServiceName = Literal['pinpoint-sms-voice']
ResourceServiceName = Literal['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
