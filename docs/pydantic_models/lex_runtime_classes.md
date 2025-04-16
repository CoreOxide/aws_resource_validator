# Lex Runtime Classes

# ActiveContext

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextTimeToLive'>
- **Required**: Yes

### parameters
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ActiveContextOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextTimeToLive'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# ActiveContextTimeToLive

### timeToLiveInSeconds
- **Type**: typing.Optional[int]

### turnsToLive
- **Type**: typing.Optional[int]


# ActiveContextUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Button

### text
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSessionRequest

### botName
- **Type**: <class 'str'>
- **Required**: Yes

### botAlias
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# DialogActionOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DialogActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GenericAttachment

### title
- **Type**: typing.Optional[str]

### subTitle
- **Type**: typing.Optional[str]

### attachmentLinkUrl
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.Button]]


# GetSessionRequest

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


# GetSessionResponse

### recentIntentSummaryView
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.IntentSummaryOutput]
- **Required**: Yes

### sessionAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### dialogAction
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.DialogActionOutput'>
- **Required**: Yes

### activeContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# IntentConfidence

### score
- **Type**: typing.Optional[float]


# IntentSummary

### dialogActionType
- **Type**: typing.Literal['Close', 'ConfirmIntent', 'Delegate', 'ElicitIntent', 'ElicitSlot']
- **Required**: Yes

### intentName
- **Type**: typing.Optional[str]

### checkpointLabel
- **Type**: typing.Optional[str]

### slots
- **Type**: typing.Optional[typing.Mapping[str, str]]

### confirmationStatus
- **Type**: typing.Optional[typing.Literal['Confirmed', 'Denied', 'None']]

### fulfillmentState
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'ReadyForFulfillment']]

### slotToElicit
- **Type**: typing.Optional[str]


# IntentSummaryOutput

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


# IntentSummaryUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PostContentRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.Blob'>
- **Required**: Yes

### sessionAttributes
- **Type**: typing.Optional[str]

### requestAttributes
- **Type**: typing.Optional[str]

### accept
- **Type**: typing.Optional[str]

### activeContexts
- **Type**: typing.Optional[str]


# PostContentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# PostTextRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextUnion]]


# PostTextResponse

### intentName
- **Type**: <class 'str'>
- **Required**: Yes

### nluIntentConfidence
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.IntentConfidence'>
- **Required**: Yes

### alternativeIntents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.PredictedIntent]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.SentimentResponse'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseCard'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### botVersion
- **Type**: <class 'str'>
- **Required**: Yes

### activeContexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# PredictedIntent

### intentName
- **Type**: typing.Optional[str]

### nluIntentConfidence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_runtime_classes.IntentConfidence]

### slots
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutSessionRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lex_runtime_classes.DialogActionUnion]

### recentIntentSummaryView
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_runtime_classes.IntentSummaryUnion]]

### accept
- **Type**: typing.Optional[str]

### activeContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lex_runtime_classes.ActiveContextUnion]]


# PutSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lex_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# ResponseCard

### version
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[typing.Literal['application/vnd.amazonaws.card.generic']]

### genericAttachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lex_runtime_classes.GenericAttachment]]


# ResponseMetadata

### RequestId
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

### HostId
- **Type**: typing.Optional[str]


# SentimentResponse

### sentimentLabel
- **Type**: typing.Optional[str]

### sentimentScore
- **Type**: typing.Optional[str]


