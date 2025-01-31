# Lex Runtime Classes

# ActiveContextTimeToLiveTypeDef

### timeToLiveInSeconds
- **Type**: typing.Optional[int]

### turnsToLive
- **Type**: typing.Optional[int]


# ActiveContextTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextTimeToLiveTypeDef'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ButtonTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSessionRequestRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSessionResponseTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DialogActionTypeDef

### type
- **Type**: typing.Literal['Close', 'ConfirmIntent', 'Delegate', 'ElicitIntent', 'ElicitSlot']
- **Required**: Yes

### intentName
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.Dict[str, str]]

### slotToElicit
- **Type**: typing.Optional[str]

### fulfillmentState
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'ReadyForFulfillment']]

### message
- **Type**: typing.Optional[str]

### messageFormat
- **Type**: typing.Optional[typing.Literal['Composite', 'CustomPayload', 'PlainText', 'SSML']]


# GenericAttachmentTypeDef

### title
- **Type**: typing.Optional[str]

### subTitle
- **Type**: typing.Optional[str]

### attachmentLinkUrl
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.ButtonTypeDef]]


# GetSessionRequestRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### checkpointLabelFilter
- **Type**: typing.Optional[str]


# GetSessionResponseTypeDef

### recentIntentSummaryView
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.IntentSummaryTypeDef]
- **Required**: Yes

### sessionAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### dialogAction
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.DialogActionTypeDef'>
- **Required**: Yes

### activeContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IntentConfidenceTypeDef

### score
- **Type**: typing.Optional[float]


# IntentSummaryTypeDef

### dialogActionType
- **Type**: typing.Literal['Close', 'ConfirmIntent', 'Delegate', 'ElicitIntent', 'ElicitSlot']
- **Required**: Yes

### intentName
- **Type**: typing.Optional[str]

### checkpointLabel
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.Dict[str, str]]

### confirmationStatus
- **Type**: typing.Optional[typing.Literal['Confirmed', 'Denied', 'None']]

### fulfillmentState
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'ReadyForFulfillment']]

### slotToElicit
- **Type**: typing.Optional[str]


# PostContentRequestRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### inputStream
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### sessionAttributes
- **Type**: typing.Optional[str]

### requestAttributes
- **Type**: typing.Optional[str]

### accept
- **Type**: typing.Optional[str]

### activeContexts
- **Type**: typing.Optional[str]


# PostContentResponseTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidence
- **Type**: <class 'str'>
- **Required**: Yes

### alternativeIntents
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: <class 'str'>
- **Required**: Yes

### sessionAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### sentimentResponse
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### encodedMessage
- **Type**: <class 'str'>
- **Required**: Yes

### messageFormat
- **Type**: typing.Literal['Composite', 'CustomPayload', 'PlainText', 'SSML']
- **Required**: Yes

### dialogState
- **Type**: typing.Literal['ConfirmIntent', 'ElicitIntent', 'ElicitSlot', 'Failed', 'Fulfilled', 'ReadyForFulfillment']
- **Required**: Yes

### slotToElicit
- **Type**: <class 'str'>
- **Required**: Yes

### inputTranscript
- **Type**: <class 'str'>
- **Required**: Yes

### encodedInputTranscript
- **Type**: <class 'str'>
- **Required**: Yes

### audioStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### activeContexts
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PostTextRequestRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### inputText
- **Type**: <class 'str'>
- **Required**: Yes

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### activeContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextTypeDef]]


# PostTextResponseTypeDef

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidence
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.IntentConfidenceTypeDef'>
- **Required**: Yes

### alternativeIntents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.PredictedIntentTypeDef]
- **Required**: Yes

### slots
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### sessionAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### sentimentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.SentimentResponseTypeDef'>
- **Required**: Yes

### messageFormat
- **Type**: typing.Literal['Composite', 'CustomPayload', 'PlainText', 'SSML']
- **Required**: Yes

### dialogState
- **Type**: typing.Literal['ConfirmIntent', 'ElicitIntent', 'ElicitSlot', 'Failed', 'Fulfilled', 'ReadyForFulfillment']
- **Required**: Yes

### slotToElicit
- **Type**: <class 'str'>
- **Required**: Yes

### responseCard
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseCardTypeDef'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### activeContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PredictedIntentTypeDef

### intentName
- **Type**: typing.Optional[str]

### nluIntentConfidence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_runtime_classes.IntentConfidenceTypeDef]

### slots
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutSessionRequestRequestTypeDef

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_runtime_classes.DialogActionTypeDef]

### recentIntentSummaryView
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_runtime_classes.IntentSummaryTypeDef]]

### accept
- **Type**: typing.Optional[str]

### activeContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextTypeDef]]


# PutSessionResponseTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: <class 'str'>
- **Required**: Yes

### sessionAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### encodedMessage
- **Type**: <class 'str'>
- **Required**: Yes

### messageFormat
- **Type**: typing.Literal['Composite', 'CustomPayload', 'PlainText', 'SSML']
- **Required**: Yes

### dialogState
- **Type**: typing.Literal['ConfirmIntent', 'ElicitIntent', 'ElicitSlot', 'Failed', 'Fulfilled', 'ReadyForFulfillment']
- **Required**: Yes

### slotToElicit
- **Type**: <class 'str'>
- **Required**: Yes

### audioStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### activeContexts
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseCardTypeDef

### version
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[typing.Literal['application/vnd.amazonaws.card.generic']]

### genericAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.GenericAttachmentTypeDef]]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# SentimentResponseTypeDef

### sentimentLabel
- **Type**: typing.Optional[str]

### sentimentScore
- **Type**: typing.Optional[str]


