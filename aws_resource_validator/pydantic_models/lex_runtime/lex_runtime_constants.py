from typing import Literal
from datetime import datetime


ConfirmationStatusType = Literal['Confirmed', 'Denied', 'None']
ContentTypeType = Literal['application/vnd.amazonaws.card.generic']
DialogActionTypeType = Literal['Close', 'ConfirmIntent', 'Delegate', 'ElicitIntent', 'ElicitSlot']
DialogStateType = Literal['ConfirmIntent', 'ElicitIntent', 'ElicitSlot', 'Failed', 'Fulfilled', 'ReadyForFulfillment']
FulfillmentStateType = Literal['Failed', 'Fulfilled', 'ReadyForFulfillment']
LexRuntimeServiceServiceName = Literal['lex-runtime']
MessageFormatTypeType = Literal['Composite', 'CustomPayload', 'PlainText', 'SSML']
RegionName = Literal['ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'us-east-1', 'us-west-2']
ResourceServiceName = Literal['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
