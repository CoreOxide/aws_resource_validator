# Events Classes

# ActivateEventSourceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ApiDestination

### ApiDestinationArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ApiDestinationState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### ConnectionArn
- **Type**: typing.Optional[str]

### InvocationEndpoint
- **Type**: typing.Optional[str]

### HttpMethod
- **Type**: typing.Optional[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]

### InvocationRateLimitPerSecond
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# AppSyncParameters

### GraphQLOperation
- **Type**: typing.Optional[str]


# Archive

### ArchiveName
- **Type**: typing.Optional[str]

### EventSourceArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DISABLED', 'ENABLED', 'UPDATE_FAILED', 'UPDATING']]

### StateReason
- **Type**: typing.Optional[str]

### RetentionDays
- **Type**: typing.Optional[int]

### SizeBytes
- **Type**: typing.Optional[int]

### EventCount
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# AwsVpcConfiguration

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationOutput

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchArrayProperties

### Size
- **Type**: typing.Optional[int]


# BatchParameters

### JobDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ArrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.BatchArrayProperties]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.BatchRetryStrategy]


# BatchRetryStrategy

### Attempts
- **Type**: typing.Optional[int]


# CancelReplayRequest

### ReplayName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelReplayResponse

### ReplayArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'RUNNING', 'STARTING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# CapacityProviderStrategyItem

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### base
- **Type**: typing.Optional[int]


# Condition

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Connection

### ConnectionArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'FAILED_CONNECTIVITY', 'UPDATING']]

### StateReason
- **Type**: typing.Optional[str]

### AuthorizationType
- **Type**: typing.Optional[typing.Literal['API_KEY', 'BASIC', 'OAUTH_CLIENT_CREDENTIALS']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastAuthorizedTime
- **Type**: typing.Optional[datetime.datetime]


# ConnectionApiKeyAuthResponseParameters

### ApiKeyName
- **Type**: typing.Optional[str]


# ConnectionAuthResponseParameters

### BasicAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionBasicAuthResponseParameters]

### OAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionOAuthResponseParameters]

### ApiKeyAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionApiKeyAuthResponseParameters]

### InvocationHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersOutput]

### ConnectivityParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.DescribeConnectionConnectivityParameters]


# ConnectionBasicAuthResponseParameters

### Username
- **Type**: typing.Optional[str]


# ConnectionBodyParameter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### IsValueSecret
- **Type**: typing.Optional[bool]


# ConnectionHeaderParameter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### IsValueSecret
- **Type**: typing.Optional[bool]


# ConnectionHttpParameters

### HeaderParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.ConnectionHeaderParameter]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.ConnectionQueryStringParameter]]

### BodyParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.ConnectionBodyParameter]]


# ConnectionHttpParametersOutput

### HeaderParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.ConnectionHeaderParameter]]

### QueryStringParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.ConnectionQueryStringParameter]]

### BodyParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.ConnectionBodyParameter]]


# ConnectionHttpParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectionOAuthClientResponseParameters

### ClientID
- **Type**: typing.Optional[str]


# ConnectionOAuthResponseParameters

### ClientParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionOAuthClientResponseParameters]

### AuthorizationEndpoint
- **Type**: typing.Optional[str]

### HttpMethod
- **Type**: typing.Optional[typing.Literal['GET', 'POST', 'PUT']]

### OAuthHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersOutput]


# ConnectionQueryStringParameter

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### IsValueSecret
- **Type**: typing.Optional[bool]


# ConnectivityResourceConfigurationArn

### ResourceConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConnectivityResourceParameters

### ResourceParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ConnectivityResourceConfigurationArn'>
- **Required**: Yes


# CreateApiDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### HttpMethod
- **Type**: typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### InvocationRateLimitPerSecond
- **Type**: typing.Optional[int]


# CreateApiDestinationResponse

### ApiDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApiDestinationState
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# CreateArchiveRequest

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EventPattern
- **Type**: typing.Optional[str]

### RetentionDays
- **Type**: typing.Optional[int]


# CreateArchiveResponse

### ArchiveArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DISABLED', 'ENABLED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectionApiKeyAuthRequestParameters

### ApiKeyName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeyValue
- **Type**: <class 'str'>
- **Required**: Yes


# CreateConnectionAuthRequestParameters

### BasicAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.CreateConnectionBasicAuthRequestParameters]

### OAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.CreateConnectionOAuthRequestParameters]

### ApiKeyAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.CreateConnectionApiKeyAuthRequestParameters]

### InvocationHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersUnion]

### ConnectivityParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectivityResourceParameters]


# CreateConnectionBasicAuthRequestParameters

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# CreateConnectionOAuthClientRequestParameters

### ClientID
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: <class 'str'>
- **Required**: Yes


# CreateConnectionOAuthRequestParameters

### ClientParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.CreateConnectionOAuthClientRequestParameters'>
- **Required**: Yes

### AuthorizationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### HttpMethod
- **Type**: typing.Literal['GET', 'POST', 'PUT']
- **Required**: Yes

### OAuthHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersUnion]


# CreateConnectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationType
- **Type**: typing.Literal['API_KEY', 'BASIC', 'OAUTH_CLIENT_CREDENTIALS']
- **Required**: Yes

### AuthParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.CreateConnectionAuthRequestParameters'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### InvocationConnectivityParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectivityResourceParameters]


# CreateConnectionResponse

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['ACTIVE', 'AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'FAILED_CONNECTIVITY', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEndpointRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.RoutingConfig'>
- **Required**: Yes

### EventBuses
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.EndpointEventBus]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ReplicationConfig
- **Type**: <class 'NoneType'>

### RoleArn
- **Type**: typing.Optional[str]


# CreateEndpointResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.RoutingConfig'>
- **Required**: Yes

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplicationConfig'>
- **Required**: Yes

### EventBuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointEventBus]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventBusRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.Tag]]


# CreateEventBusResponse

### EventBusArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.DeadLetterConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePartnerEventSourceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePartnerEventSourceResponse

### EventSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DeactivateEventSourceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeadLetterConfig

### Arn
- **Type**: typing.Optional[str]


# DeauthorizeConnectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeauthorizeConnectionResponse

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['ACTIVE', 'AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'FAILED_CONNECTIVITY', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastAuthorizedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApiDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteArchiveRequest

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionResponse

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['ACTIVE', 'AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'FAILED_CONNECTIVITY', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastAuthorizedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEndpointRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventBusRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePartnerEventSourceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### Force
- **Type**: typing.Optional[bool]


# DescribeApiDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApiDestinationResponse

### ApiDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ApiDestinationState
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### HttpMethod
- **Type**: typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']
- **Required**: Yes

### InvocationRateLimitPerSecond
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeArchiveRequest

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeArchiveResponse

### ArchiveArn
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EventPattern
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DISABLED', 'ENABLED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionDays
- **Type**: <class 'int'>
- **Required**: Yes

### SizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### EventCount
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectionConnectivityParameters

### ResourceParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.DescribeConnectionResourceParameters'>
- **Required**: Yes


# DescribeConnectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectionResourceParameters

### ResourceConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectionResponse

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationConnectivityParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.DescribeConnectionConnectivityParameters'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['ACTIVE', 'AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'FAILED_CONNECTIVITY', 'UPDATING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationType
- **Type**: typing.Literal['API_KEY', 'BASIC', 'OAUTH_CLIENT_CREDENTIALS']
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ConnectionAuthResponseParameters'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastAuthorizedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HomeRegion
- **Type**: typing.Optional[str]


# DescribeEndpointResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.RoutingConfig'>
- **Required**: Yes

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplicationConfig'>
- **Required**: Yes

### EventBuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointEventBus]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointUrl
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventBusRequest

### Name
- **Type**: typing.Optional[str]


# DescribeEventBusResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.DeadLetterConfig'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventSourceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEventSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePartnerEventSourceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePartnerEventSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplayRequest

### ReplayName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReplayResponse

### ReplayName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplayArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'RUNNING', 'STARTING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplayDestinationOutput'>
- **Required**: Yes

### EventStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EventEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EventLastReplayedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReplayStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReplayEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]


# DescribeRuleResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### EventPattern
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedBy
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# DisableRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]


# EcsParameters

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.NetworkConfigurationUnion]

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.CapacityProviderStrategyItem]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.PlacementConstraint]]

### PlacementStrategy
- **Type**: typing.Optional[typing.Sequence[NoneType]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.Tag]]


# EcsParametersOutput

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.NetworkConfigurationOutput]

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.CapacityProviderStrategyItem]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.PlacementConstraint]]

### PlacementStrategy
- **Type**: typing.Optional[typing.List[NoneType]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.Tag]]


# EcsParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# EnableRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]


# Endpoint

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: <class 'NoneType'>

### ReplicationConfig
- **Type**: <class 'NoneType'>

### EventBuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointEventBus]]

### RoleArn
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### StateReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# EndpointEventBus

### EventBusArn
- **Type**: <class 'str'>
- **Required**: Yes


# EventBus

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# EventSource

### Arn
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'PENDING']]


# FailoverConfig

### Primary
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.Primary'>
- **Required**: Yes

### Secondary
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.Secondary'>
- **Required**: Yes


# HttpParameters

### PathParameterValues
- **Type**: typing.Optional[typing.Sequence[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# HttpParametersOutput

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# HttpParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputTransformer

### InputTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### InputPathsMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# InputTransformerOutput

### InputTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### InputPathsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# InputTransformerUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KinesisParameters

### PartitionKeyPath
- **Type**: <class 'str'>
- **Required**: Yes


# ListApiDestinationsRequest

### NamePrefix
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListApiDestinationsResponse

### ApiDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.ApiDestination]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArchivesRequest

### NamePrefix
- **Type**: typing.Optional[str]

### EventSourceArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATING', 'DISABLED', 'ENABLED', 'UPDATE_FAILED', 'UPDATING']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListArchivesResponse

### Archives
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.Archive]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionsRequest

### NamePrefix
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'FAILED_CONNECTIVITY', 'UPDATING']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListConnectionsResponse

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.Connection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointsRequest

### NamePrefix
- **Type**: typing.Optional[str]

### HomeRegion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEndpointsResponse

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventBusesRequest

### NamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListEventBusesResponse

### EventBuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EventBus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventSourcesRequest

### NamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListEventSourcesResponse

### EventSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EventSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerEventSourceAccountsRequest

### EventSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListPartnerEventSourceAccountsResponse

### PartnerEventSourceAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PartnerEventSourceAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerEventSourcesRequest

### NamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListPartnerEventSourcesResponse

### PartnerEventSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PartnerEventSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReplaysRequest

### NamePrefix
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'RUNNING', 'STARTING']]

### EventSourceArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListReplaysResponse

### Replays
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.Replay]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRuleNamesByTargetRequest

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRuleNamesByTargetRequestPaginate

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.PaginatorConfig]


# ListRuleNamesByTargetResponse

### RuleNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRulesRequest

### NamePrefix
- **Type**: typing.Optional[str]

### EventBusName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRulesRequestPaginate

### NamePrefix
- **Type**: typing.Optional[str]

### EventBusName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.PaginatorConfig]


# ListRulesResponse

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.Rule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# ListTargetsByRuleRequest

### Rule
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTargetsByRuleRequestPaginate

### Rule
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.PaginatorConfig]


# ListTargetsByRuleResponse

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.TargetOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NetworkConfiguration

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.AwsVpcConfigurationUnion]


# NetworkConfigurationOutput

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.AwsVpcConfigurationOutput]


# NetworkConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartnerEventSource

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# PartnerEventSourceAccount

### Account
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'PENDING']]


# PlacementConstraint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PlacementStrategy

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Primary

### HealthCheck
- **Type**: <class 'str'>
- **Required**: Yes


# PutEventsRequest

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.PutEventsRequestEntry]
- **Required**: Yes

### EndpointId
- **Type**: typing.Optional[str]


# PutEventsRequestEntry

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.Timestamp]

### Source
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.Sequence[str]]

### DetailType
- **Type**: typing.Optional[str]

### Detail
- **Type**: typing.Optional[str]

### EventBusName
- **Type**: typing.Optional[str]

### TraceHeader
- **Type**: typing.Optional[str]


# PutEventsResponse

### FailedEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PutEventsResultEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# PutEventsResultEntry

### EventId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# PutPartnerEventsRequest

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.PutPartnerEventsRequestEntry]
- **Required**: Yes


# PutPartnerEventsRequestEntry

### Time
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.Timestamp]

### Source
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.Sequence[str]]

### DetailType
- **Type**: typing.Optional[str]

### Detail
- **Type**: typing.Optional[str]


# PutPartnerEventsResponse

### FailedEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PutPartnerEventsResultEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# PutPartnerEventsResultEntry

### EventId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# PutPermissionRequest

### EventBusName
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[str]

### Principal
- **Type**: typing.Optional[str]

### StatementId
- **Type**: typing.Optional[str]

### Condition
- **Type**: <class 'NoneType'>

### Policy
- **Type**: typing.Optional[str]


# PutRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: typing.Optional[str]

### EventPattern
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS']]

### Description
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.Tag]]

### EventBusName
- **Type**: typing.Optional[str]


# PutRuleResponse

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# PutTargetsRequest

### Rule
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.TargetUnion]
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]


# PutTargetsResponse

### FailedEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### FailedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PutTargetsResultEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# PutTargetsResultEntry

### TargetId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# RedshiftDataParameters

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### SecretManagerArn
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### Sql
- **Type**: typing.Optional[str]

### StatementName
- **Type**: typing.Optional[str]

### WithEvent
- **Type**: typing.Optional[bool]

### Sqls
- **Type**: typing.Optional[typing.Sequence[str]]


# RedshiftDataParametersOutput

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### SecretManagerArn
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### Sql
- **Type**: typing.Optional[str]

### StatementName
- **Type**: typing.Optional[str]

### WithEvent
- **Type**: typing.Optional[bool]

### Sqls
- **Type**: typing.Optional[typing.List[str]]


# RedshiftDataParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemovePermissionRequest

### StatementId
- **Type**: typing.Optional[str]

### RemoveAllPermissions
- **Type**: typing.Optional[bool]

### EventBusName
- **Type**: typing.Optional[str]


# RemoveTargetsRequest

### Rule
- **Type**: <class 'str'>
- **Required**: Yes

### Ids
- **Type**: typing.Sequence[str]
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### Force
- **Type**: typing.Optional[bool]


# RemoveTargetsResponse

### FailedEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### FailedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.RemoveTargetsResultEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTargetsResultEntry

### TargetId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# Replay

### ReplayName
- **Type**: typing.Optional[str]

### EventSourceArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'RUNNING', 'STARTING']]

### StateReason
- **Type**: typing.Optional[str]

### EventStartTime
- **Type**: typing.Optional[datetime.datetime]

### EventEndTime
- **Type**: typing.Optional[datetime.datetime]

### EventLastReplayedTime
- **Type**: typing.Optional[datetime.datetime]

### ReplayStartTime
- **Type**: typing.Optional[datetime.datetime]

### ReplayEndTime
- **Type**: typing.Optional[datetime.datetime]


# ReplayDestination

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FilterArns
- **Type**: typing.Optional[typing.Sequence[str]]


# ReplayDestinationOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FilterArns
- **Type**: typing.Optional[typing.List[str]]


# ReplayDestinationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReplicationConfig

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


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


# RetryPolicy

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### MaximumEventAgeInSeconds
- **Type**: typing.Optional[int]


# RoutingConfig

### FailoverConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.FailoverConfig'>
- **Required**: Yes


# Rule

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### EventPattern
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS']]

### Description
- **Type**: typing.Optional[str]

### ScheduleExpression
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ManagedBy
- **Type**: typing.Optional[str]

### EventBusName
- **Type**: typing.Optional[str]


# RunCommandParameters

### RunCommandTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.RunCommandTargetUnion]
- **Required**: Yes


# RunCommandParametersOutput

### RunCommandTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.RunCommandTargetOutput]
- **Required**: Yes


# RunCommandParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RunCommandTarget

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RunCommandTargetOutput

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RunCommandTargetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SageMakerPipelineParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SageMakerPipelineParameters

### PipelineParameterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParameter]]


# SageMakerPipelineParametersOutput

### PipelineParameterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParameter]]


# SageMakerPipelineParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Secondary

### Route
- **Type**: <class 'str'>
- **Required**: Yes


# SqsParameters

### MessageGroupId
- **Type**: typing.Optional[str]


# StartReplayRequest

### ReplayName
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventStartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.Timestamp'>
- **Required**: Yes

### EventEndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.Timestamp'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplayDestinationUnion'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# StartReplayResponse

### ReplayArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'RUNNING', 'STARTING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### ReplayStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.Tag]
- **Required**: Yes


# Target

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Input
- **Type**: typing.Optional[str]

### InputPath
- **Type**: typing.Optional[str]

### InputTransformer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.InputTransformerUnion]

### KinesisParameters
- **Type**: <class 'NoneType'>

### RunCommandParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RunCommandParametersUnion]

### EcsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.EcsParametersUnion]

### BatchParameters
- **Type**: <class 'NoneType'>

### SqsParameters
- **Type**: <class 'NoneType'>

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.HttpParametersUnion]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RedshiftDataParametersUnion]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParametersUnion]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

### RetryPolicy
- **Type**: <class 'NoneType'>

### AppSyncParameters
- **Type**: <class 'NoneType'>


# TargetOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Input
- **Type**: typing.Optional[str]

### InputPath
- **Type**: typing.Optional[str]

### InputTransformer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.InputTransformerOutput]

### KinesisParameters
- **Type**: <class 'NoneType'>

### RunCommandParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RunCommandParametersOutput]

### EcsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.EcsParametersOutput]

### BatchParameters
- **Type**: <class 'NoneType'>

### SqsParameters
- **Type**: <class 'NoneType'>

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.HttpParametersOutput]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RedshiftDataParametersOutput]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParametersOutput]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

### RetryPolicy
- **Type**: <class 'NoneType'>

### AppSyncParameters
- **Type**: <class 'NoneType'>


# TargetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TestEventPatternRequest

### EventPattern
- **Type**: <class 'str'>
- **Required**: Yes

### Event
- **Type**: <class 'str'>
- **Required**: Yes


# TestEventPatternResponse

### Result
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApiDestinationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### InvocationEndpoint
- **Type**: typing.Optional[str]

### HttpMethod
- **Type**: typing.Optional[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]

### InvocationRateLimitPerSecond
- **Type**: typing.Optional[int]


# UpdateApiDestinationResponse

### ApiDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApiDestinationState
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateArchiveRequest

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EventPattern
- **Type**: typing.Optional[str]

### RetentionDays
- **Type**: typing.Optional[int]


# UpdateArchiveResponse

### ArchiveArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATE_FAILED', 'CREATING', 'DISABLED', 'ENABLED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConnectionApiKeyAuthRequestParameters

### ApiKeyName
- **Type**: typing.Optional[str]

### ApiKeyValue
- **Type**: typing.Optional[str]


# UpdateConnectionAuthRequestParameters

### BasicAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionBasicAuthRequestParameters]

### OAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionOAuthRequestParameters]

### ApiKeyAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionApiKeyAuthRequestParameters]

### InvocationHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersUnion]

### ConnectivityParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectivityResourceParameters]


# UpdateConnectionBasicAuthRequestParameters

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# UpdateConnectionOAuthClientRequestParameters

### ClientID
- **Type**: typing.Optional[str]

### ClientSecret
- **Type**: typing.Optional[str]


# UpdateConnectionOAuthRequestParameters

### ClientParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionOAuthClientRequestParameters]

### AuthorizationEndpoint
- **Type**: typing.Optional[str]

### HttpMethod
- **Type**: typing.Optional[typing.Literal['GET', 'POST', 'PUT']]

### OAuthHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersUnion]


# UpdateConnectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AuthorizationType
- **Type**: typing.Optional[typing.Literal['API_KEY', 'BASIC', 'OAUTH_CLIENT_CREDENTIALS']]

### AuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionAuthRequestParameters]

### InvocationConnectivityParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectivityResourceParameters]


# UpdateConnectionResponse

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['ACTIVE', 'AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'FAILED_CONNECTIVITY', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastAuthorizedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEndpointRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: <class 'NoneType'>

### ReplicationConfig
- **Type**: <class 'NoneType'>

### EventBuses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.EndpointEventBus]]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateEndpointResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.RoutingConfig'>
- **Required**: Yes

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplicationConfig'>
- **Required**: Yes

### EventBuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointEventBus]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointUrl
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEventBusRequest

### Name
- **Type**: typing.Optional[str]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DeadLetterConfig
- **Type**: <class 'NoneType'>


# UpdateEventBusResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.DeadLetterConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadata'>
- **Required**: Yes


