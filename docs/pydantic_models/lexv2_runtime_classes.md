# Pydantic Models in lexv2_runtime_classes

# ActiveContextTimeToLiveTypeDef

### timeToLiveInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### turnsToLive
- **Type**: <class 'int'>
- **Required**: Yes


# ActiveContextTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timeToLive
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextTimeToLiveTypeDef'>
- **Required**: Yes

### contextAttributes
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


# ConfidenceScoreTypeDef

### score
- **Type**: typing.Optional[float]


# DeleteSessionRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSessionResponseTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DialogActionTypeDef

### type
- **Type**: typing.Literal['Close', 'ConfirmIntent', 'Delegate', 'ElicitIntent', 'ElicitSlot', 'None']
- **Required**: Yes

### slotToElicit
- **Type**: typing.Optional[str]

### slotElicitationStyle
- **Type**: typing.Optional[typing.Literal['Default', 'SpellByLetter', 'SpellByWord']]

### subSlotToElicit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ElicitSubSlotTypeDef]


# ElicitSubSlotTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subSlotToElicit
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# GetSessionRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponseTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageTypeDef]
- **Required**: Yes

### interpretations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.InterpretationTypeDef]
- **Required**: Yes

### sessionState
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImageResponseCardTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### subtitle
- **Type**: typing.Optional[str]

### imageUrl
- **Type**: typing.Optional[str]

### buttons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ButtonTypeDef]]


# IntentTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### slots
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.SlotTypeDef]]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Fulfilled', 'FulfillmentInProgress', 'InProgress', 'ReadyForFulfillment', 'Waiting']]

### confirmationState
- **Type**: typing.Optional[typing.Literal['Confirmed', 'Denied', 'None']]


# InterpretationTypeDef

### nluConfidence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ConfidenceScoreTypeDef]

### sentimentResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SentimentResponseTypeDef]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentTypeDef]

### interpretationSource
- **Type**: typing.Optional[typing.Literal['Bedrock', 'Lex']]


# MessageTypeDef

### contentType
- **Type**: typing.Literal['CustomPayload', 'ImageResponseCard', 'PlainText', 'SSML']
- **Required**: Yes

### content
- **Type**: typing.Optional[str]

### imageResponseCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ImageResponseCardTypeDef]


# PutSessionRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateTypeDef'>
- **Required**: Yes

### messages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageTypeDef]]

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### responseContentType
- **Type**: typing.Optional[str]


# PutSessionResponseTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: <class 'str'>
- **Required**: Yes

### requestAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### audioStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecognizeTextRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### text
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateTypeDef]

### requestAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RecognizeTextResponseTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.MessageTypeDef]
- **Required**: Yes

### sessionState
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.SessionStateTypeDef'>
- **Required**: Yes

### interpretations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.InterpretationTypeDef]
- **Required**: Yes

### requestAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### recognizedBotMember
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.RecognizedBotMemberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecognizeUtteranceRequestRequestTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### requestContentType
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: typing.Optional[str]

### requestAttributes
- **Type**: typing.Optional[str]

### responseContentType
- **Type**: typing.Optional[str]

### inputStream
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# RecognizeUtteranceResponseTypeDef

### inputMode
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: <class 'str'>
- **Required**: Yes

### interpretations
- **Type**: <class 'str'>
- **Required**: Yes

### sessionState
- **Type**: <class 'str'>
- **Required**: Yes

### requestAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### inputTranscript
- **Type**: <class 'str'>
- **Required**: Yes

### audioStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### recognizedBotMember
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lexv2_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecognizedBotMemberTypeDef

### botId
- **Type**: <class 'str'>
- **Required**: Yes

### botName
- **Type**: typing.Optional[str]


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


# RuntimeHintDetailsTypeDef

### runtimeHintValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintValueTypeDef]]

### subSlotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# RuntimeHintValueTypeDef

### phrase
- **Type**: <class 'str'>
- **Required**: Yes


# RuntimeHintsTypeDef

### slotHints
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintDetailsTypeDef]]]


# SentimentResponseTypeDef

### sentiment
- **Type**: typing.Optional[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]

### sentimentScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.SentimentScoreTypeDef]


# SentimentScoreTypeDef

### positive
- **Type**: typing.Optional[float]

### negative
- **Type**: typing.Optional[float]

### neutral
- **Type**: typing.Optional[float]

### mixed
- **Type**: typing.Optional[float]


# SessionStateTypeDef

### dialogAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.DialogActionTypeDef]

### intent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.IntentTypeDef]

### activeContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ActiveContextTypeDef]]

### sessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### originatingRequestId
- **Type**: typing.Optional[str]

### runtimeHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.RuntimeHintsTypeDef]


# SlotTypeDef

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lexv2_runtime_classes.ValueTypeDef]

### shape
- **Type**: typing.Optional[typing.Literal['Composite', 'List', 'Scalar']]

### values
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### subSlots
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# ValueTypeDef

### interpretedValue
- **Type**: <class 'str'>
- **Required**: Yes

### originalValue
- **Type**: typing.Optional[str]

### resolvedValues
- **Type**: typing.Optional[typing.List[str]]


