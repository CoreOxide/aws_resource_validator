# Pydantic Models in personalize_events_classes

# ActionInteractionTypeDef

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]

### recommendationId
- **Type**: typing.Optional[str]

### impression
- **Type**: typing.Optional[typing.Sequence[str]]

### properties
- **Type**: typing.Optional[str]


# ActionTypeDef

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventTypeDef

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### sentAt
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### eventId
- **Type**: typing.Optional[str]

### eventValue
- **Type**: typing.Optional[float]

### itemId
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[str]

### recommendationId
- **Type**: typing.Optional[str]

### impression
- **Type**: typing.Optional[typing.Sequence[str]]

### metricAttribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_events_classes.MetricAttributionTypeDef]


# ItemTypeDef

### itemId
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[str]


# MetricAttributionTypeDef

### eventAttributionSource
- **Type**: <class 'str'>
- **Required**: Yes


# PutActionInteractionsRequestRequestTypeDef

### trackingId
- **Type**: <class 'str'>
- **Required**: Yes

### actionInteractions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.ActionInteractionTypeDef]
- **Required**: Yes


# PutActionsRequestRequestTypeDef

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.ActionTypeDef]
- **Required**: Yes


# PutEventsRequestRequestTypeDef

### trackingId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### eventList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.EventTypeDef]
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]


# PutItemsRequestRequestTypeDef

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.ItemTypeDef]
- **Required**: Yes


# PutUsersRequestRequestTypeDef

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### users
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.UserTypeDef]
- **Required**: Yes


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


# UserTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[str]


