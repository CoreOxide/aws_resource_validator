# Personalize Events Classes

# Action

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[str]


# ActionInteraction

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_events_classes.Timestamp'>
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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_events_classes.ResponseMetadata'>
- **Required**: Yes


# Event

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### sentAt
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_events_classes.Timestamp'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_events_classes.MetricAttribution]


# Item

### itemId
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[str]


# MetricAttribution

### eventAttributionSource
- **Type**: <class 'str'>
- **Required**: Yes


# PutActionInteractionsRequest

### trackingId
- **Type**: <class 'str'>
- **Required**: Yes

### actionInteractions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.ActionInteraction]
- **Required**: Yes


# PutActionsRequest

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.Action]
- **Required**: Yes


# PutEventsRequest

### trackingId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### eventList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.Event]
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]


# PutItemsRequest

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.Item]
- **Required**: Yes


# PutUsersRequest

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### users
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_events_classes.User]
- **Required**: Yes


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


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# User

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[str]


