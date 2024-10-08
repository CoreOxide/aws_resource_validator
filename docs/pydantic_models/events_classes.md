# Pydantic Models in events_classes

# ActivateEventSourceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ApiDestinationTypeDef

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


# AppSyncParametersTypeDef

### GraphQLOperation
- **Type**: typing.Optional[str]


# ArchiveTypeDef

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


# AwsVpcConfigurationExtraOutputTypeDef

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationOutputTypeDef

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationTypeDef

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchArrayPropertiesTypeDef

### Size
- **Type**: typing.Optional[int]


# BatchParametersTypeDef

### JobDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ArrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.BatchArrayPropertiesTypeDef]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.BatchRetryStrategyTypeDef]


# BatchRetryStrategyTypeDef

### Attempts
- **Type**: typing.Optional[int]


# CancelReplayRequestRequestTypeDef

### ReplayName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelReplayResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CapacityProviderStrategyItemTypeDef

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### base
- **Type**: typing.Optional[int]


# ConditionTypeDef

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ConnectionApiKeyAuthResponseParametersTypeDef

### ApiKeyName
- **Type**: typing.Optional[str]


# ConnectionAuthResponseParametersTypeDef

### BasicAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionBasicAuthResponseParametersTypeDef]

### OAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionOAuthResponseParametersTypeDef]

### ApiKeyAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionApiKeyAuthResponseParametersTypeDef]

### InvocationHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersOutputTypeDef]


# ConnectionBasicAuthResponseParametersTypeDef

### Username
- **Type**: typing.Optional[str]


# ConnectionBodyParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### IsValueSecret
- **Type**: typing.Optional[bool]


# ConnectionHeaderParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### IsValueSecret
- **Type**: typing.Optional[bool]


# ConnectionHttpParametersOutputTypeDef

### HeaderParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.ConnectionHeaderParameterTypeDef]]

### QueryStringParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.ConnectionQueryStringParameterTypeDef]]

### BodyParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.ConnectionBodyParameterTypeDef]]


# ConnectionHttpParametersTypeDef

### HeaderParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.ConnectionHeaderParameterTypeDef]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.ConnectionQueryStringParameterTypeDef]]

### BodyParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.ConnectionBodyParameterTypeDef]]


# ConnectionOAuthClientResponseParametersTypeDef

### ClientID
- **Type**: typing.Optional[str]


# ConnectionOAuthResponseParametersTypeDef

### ClientParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionOAuthClientResponseParametersTypeDef]

### AuthorizationEndpoint
- **Type**: typing.Optional[str]

### HttpMethod
- **Type**: typing.Optional[typing.Literal['GET', 'POST', 'PUT']]

### OAuthHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersOutputTypeDef]


# ConnectionQueryStringParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### IsValueSecret
- **Type**: typing.Optional[bool]


# ConnectionTypeDef

### ConnectionArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'UPDATING']]

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


# CreateApiDestinationRequestRequestTypeDef

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


# CreateApiDestinationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateArchiveRequestRequestTypeDef

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


# CreateArchiveResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectionApiKeyAuthRequestParametersTypeDef

### ApiKeyName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeyValue
- **Type**: <class 'str'>
- **Required**: Yes


# CreateConnectionAuthRequestParametersTypeDef

### BasicAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.CreateConnectionBasicAuthRequestParametersTypeDef]

### OAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.CreateConnectionOAuthRequestParametersTypeDef]

### ApiKeyAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.CreateConnectionApiKeyAuthRequestParametersTypeDef]

### InvocationHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersTypeDef]


# CreateConnectionBasicAuthRequestParametersTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# CreateConnectionOAuthClientRequestParametersTypeDef

### ClientID
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: <class 'str'>
- **Required**: Yes


# CreateConnectionOAuthRequestParametersTypeDef

### ClientParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.CreateConnectionOAuthClientRequestParametersTypeDef'>
- **Required**: Yes

### AuthorizationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### HttpMethod
- **Type**: typing.Literal['GET', 'POST', 'PUT']
- **Required**: Yes

### OAuthHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersTypeDef]


# CreateConnectionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationType
- **Type**: typing.Literal['API_KEY', 'BASIC', 'OAUTH_CLIENT_CREDENTIALS']
- **Required**: Yes

### AuthParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.CreateConnectionAuthRequestParametersTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateConnectionResponseTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEndpointRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.RoutingConfigTypeDef'>
- **Required**: Yes

### EventBuses
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.EndpointEventBusTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ReplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ReplicationConfigTypeDef]

### RoleArn
- **Type**: typing.Optional[str]


# CreateEndpointResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.RoutingConfigTypeDef'>
- **Required**: Yes

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplicationConfigTypeDef'>
- **Required**: Yes

### EventBuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointEventBusTypeDef]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventBusRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.DeadLetterConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.TagTypeDef]]


# CreateEventBusResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.DeadLetterConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePartnerEventSourceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePartnerEventSourceResponseTypeDef

### EventSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeactivateEventSourceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeadLetterConfigTypeDef

### Arn
- **Type**: typing.Optional[str]


# DeauthorizeConnectionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeauthorizeConnectionResponseTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'UPDATING']
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApiDestinationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteArchiveRequestRequestTypeDef

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionResponseTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'UPDATING']
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEndpointRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventBusRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePartnerEventSourceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### Force
- **Type**: typing.Optional[bool]


# DescribeApiDestinationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApiDestinationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeArchiveRequestRequestTypeDef

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeArchiveResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectionResponseTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'UPDATING']
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ConnectionAuthResponseParametersTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HomeRegion
- **Type**: typing.Optional[str]


# DescribeEndpointResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.RoutingConfigTypeDef'>
- **Required**: Yes

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplicationConfigTypeDef'>
- **Required**: Yes

### EventBuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointEventBusTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventBusRequestRequestTypeDef

### Name
- **Type**: typing.Optional[str]


# DescribeEventBusResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.DeadLetterConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventSourceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEventSourceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePartnerEventSourceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePartnerEventSourceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplayRequestRequestTypeDef

### ReplayName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReplayResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplayDestinationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRuleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]


# DescribeRuleResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableRuleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]


# EcsParametersExtraOutputTypeDef

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.NetworkConfigurationExtraOutputTypeDef]

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.CapacityProviderStrategyItemTypeDef]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.PlacementConstraintTypeDef]]

### PlacementStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.PlacementStrategyTypeDef]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.TagTypeDef]]


# EcsParametersOutputTypeDef

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.NetworkConfigurationOutputTypeDef]

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.CapacityProviderStrategyItemTypeDef]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.PlacementConstraintTypeDef]]

### PlacementStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.PlacementStrategyTypeDef]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.TagTypeDef]]


# EcsParametersTypeDef

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.NetworkConfigurationTypeDef]

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.CapacityProviderStrategyItemTypeDef]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.PlacementConstraintTypeDef]]

### PlacementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.PlacementStrategyTypeDef]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.TagTypeDef]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableRuleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]


# EndpointEventBusTypeDef

### EventBusArn
- **Type**: <class 'str'>
- **Required**: Yes


# EndpointTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RoutingConfigTypeDef]

### ReplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ReplicationConfigTypeDef]

### EventBuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointEventBusTypeDef]]

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


# EventBusTypeDef

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


# EventSourceTypeDef

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


# FailoverConfigTypeDef

### Primary
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.PrimaryTypeDef'>
- **Required**: Yes

### Secondary
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.SecondaryTypeDef'>
- **Required**: Yes


# HttpParametersExtraOutputTypeDef

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# HttpParametersOutputTypeDef

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# HttpParametersTypeDef

### PathParameterValues
- **Type**: typing.Optional[typing.Sequence[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# InputTransformerExtraOutputTypeDef

### InputTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### InputPathsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# InputTransformerOutputTypeDef

### InputTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### InputPathsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# InputTransformerTypeDef

### InputTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### InputPathsMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# KinesisParametersTypeDef

### PartitionKeyPath
- **Type**: <class 'str'>
- **Required**: Yes


# ListApiDestinationsRequestRequestTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListApiDestinationsResponseTypeDef

### ApiDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.ApiDestinationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArchivesRequestRequestTypeDef

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


# ListArchivesResponseTypeDef

### Archives
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.ArchiveTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionsRequestRequestTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'UPDATING']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListConnectionsResponseTypeDef

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.ConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointsRequestRequestTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### HomeRegion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEndpointsResponseTypeDef

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventBusesRequestRequestTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListEventBusesResponseTypeDef

### EventBuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EventBusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventSourcesRequestRequestTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListEventSourcesResponseTypeDef

### EventSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EventSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerEventSourceAccountsRequestRequestTypeDef

### EventSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListPartnerEventSourceAccountsResponseTypeDef

### PartnerEventSourceAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PartnerEventSourceAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerEventSourcesRequestRequestTypeDef

### NamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListPartnerEventSourcesResponseTypeDef

### PartnerEventSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PartnerEventSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReplaysRequestRequestTypeDef

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


# ListReplaysResponseTypeDef

### Replays
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.ReplayTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRuleNamesByTargetRequestListRuleNamesByTargetPaginateTypeDef

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.PaginatorConfigTypeDef]


# ListRuleNamesByTargetRequestRequestTypeDef

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRuleNamesByTargetResponseTypeDef

### RuleNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRulesRequestListRulesPaginateTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### EventBusName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.PaginatorConfigTypeDef]


# ListRulesRequestRequestTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### EventBusName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRulesResponseTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.RuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetsByRuleRequestListTargetsByRulePaginateTypeDef

### Rule
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.PaginatorConfigTypeDef]


# ListTargetsByRuleRequestRequestTypeDef

### Rule
- **Type**: <class 'str'>
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTargetsByRuleResponseTypeDef

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.TargetOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NetworkConfigurationExtraOutputTypeDef

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.AwsVpcConfigurationExtraOutputTypeDef]


# NetworkConfigurationOutputTypeDef

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.AwsVpcConfigurationOutputTypeDef]


# NetworkConfigurationTypeDef

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.AwsVpcConfigurationTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartnerEventSourceAccountTypeDef

### Account
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'PENDING']]


# PartnerEventSourceTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# PlacementConstraintTypeDef

### type
- **Type**: typing.Optional[typing.Literal['distinctInstance', 'memberOf']]

### expression
- **Type**: typing.Optional[str]


# PlacementStrategyTypeDef

### type
- **Type**: typing.Optional[typing.Literal['binpack', 'random', 'spread']]

### field
- **Type**: typing.Optional[str]


# PrimaryTypeDef

### HealthCheck
- **Type**: <class 'str'>
- **Required**: Yes


# PutEventsRequestEntryTypeDef

### Time
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# PutEventsRequestRequestTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.PutEventsRequestEntryTypeDef]
- **Required**: Yes

### EndpointId
- **Type**: typing.Optional[str]


# PutEventsResponseTypeDef

### FailedEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PutEventsResultEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutEventsResultEntryTypeDef

### EventId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# PutPartnerEventsRequestEntryTypeDef

### Time
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Source
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.Sequence[str]]

### DetailType
- **Type**: typing.Optional[str]

### Detail
- **Type**: typing.Optional[str]


# PutPartnerEventsRequestRequestTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.PutPartnerEventsRequestEntryTypeDef]
- **Required**: Yes


# PutPartnerEventsResponseTypeDef

### FailedEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PutPartnerEventsResultEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutPartnerEventsResultEntryTypeDef

### EventId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# PutPermissionRequestRequestTypeDef

### EventBusName
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[str]

### Principal
- **Type**: typing.Optional[str]

### StatementId
- **Type**: typing.Optional[str]

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConditionTypeDef]

### Policy
- **Type**: typing.Optional[str]


# PutRuleRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.TagTypeDef]]

### EventBusName
- **Type**: typing.Optional[str]


# PutRuleResponseTypeDef

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutTargetsRequestRequestTypeDef

### Rule
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.events_classes.TargetTypeDef, aws_resource_validator.pydantic_models.events_classes.TargetExtraOutputTypeDef]]
- **Required**: Yes

### EventBusName
- **Type**: typing.Optional[str]


# PutTargetsResponseTypeDef

### FailedEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### FailedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.PutTargetsResultEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutTargetsResultEntryTypeDef

### TargetId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# RedshiftDataParametersExtraOutputTypeDef

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


# RedshiftDataParametersOutputTypeDef

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


# RedshiftDataParametersTypeDef

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


# RemovePermissionRequestRequestTypeDef

### StatementId
- **Type**: typing.Optional[str]

### RemoveAllPermissions
- **Type**: typing.Optional[bool]

### EventBusName
- **Type**: typing.Optional[str]


# RemoveTargetsRequestRequestTypeDef

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


# RemoveTargetsResponseTypeDef

### FailedEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### FailedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.RemoveTargetsResultEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTargetsResultEntryTypeDef

### TargetId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# ReplayDestinationOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FilterArns
- **Type**: typing.Optional[typing.List[str]]


# ReplayDestinationTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FilterArns
- **Type**: typing.Optional[typing.Sequence[str]]


# ReplayTypeDef

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


# ReplicationConfigTypeDef

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ResponseMetadataTypeDef

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


# RetryPolicyTypeDef

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### MaximumEventAgeInSeconds
- **Type**: typing.Optional[int]


# RoutingConfigTypeDef

### FailoverConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.FailoverConfigTypeDef'>
- **Required**: Yes


# RuleTypeDef

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


# RunCommandParametersExtraOutputTypeDef

### RunCommandTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.RunCommandTargetExtraOutputTypeDef]
- **Required**: Yes


# RunCommandParametersOutputTypeDef

### RunCommandTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.RunCommandTargetOutputTypeDef]
- **Required**: Yes


# RunCommandParametersTypeDef

### RunCommandTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.RunCommandTargetTypeDef]
- **Required**: Yes


# RunCommandTargetExtraOutputTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RunCommandTargetOutputTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RunCommandTargetTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SageMakerPipelineParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SageMakerPipelineParametersExtraOutputTypeDef

### PipelineParameterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParameterTypeDef]]


# SageMakerPipelineParametersOutputTypeDef

### PipelineParameterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParameterTypeDef]]


# SageMakerPipelineParametersTypeDef

### PipelineParameterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParameterTypeDef]]


# SecondaryTypeDef

### Route
- **Type**: <class 'str'>
- **Required**: Yes


# SqsParametersTypeDef

### MessageGroupId
- **Type**: typing.Optional[str]


# StartReplayRequestRequestTypeDef

### ReplayName
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventStartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EventEndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplayDestinationTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# StartReplayResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.events_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetExtraOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.InputTransformerExtraOutputTypeDef]

### KinesisParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.KinesisParametersTypeDef]

### RunCommandParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RunCommandParametersExtraOutputTypeDef]

### EcsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.EcsParametersExtraOutputTypeDef]

### BatchParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.BatchParametersTypeDef]

### SqsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.SqsParametersTypeDef]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.HttpParametersExtraOutputTypeDef]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RedshiftDataParametersExtraOutputTypeDef]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParametersExtraOutputTypeDef]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.DeadLetterConfigTypeDef]

### RetryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RetryPolicyTypeDef]

### AppSyncParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.AppSyncParametersTypeDef]


# TargetOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.InputTransformerOutputTypeDef]

### KinesisParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.KinesisParametersTypeDef]

### RunCommandParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RunCommandParametersOutputTypeDef]

### EcsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.EcsParametersOutputTypeDef]

### BatchParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.BatchParametersTypeDef]

### SqsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.SqsParametersTypeDef]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.HttpParametersOutputTypeDef]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RedshiftDataParametersOutputTypeDef]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParametersOutputTypeDef]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.DeadLetterConfigTypeDef]

### RetryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RetryPolicyTypeDef]

### AppSyncParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.AppSyncParametersTypeDef]


# TargetTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.InputTransformerTypeDef]

### KinesisParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.KinesisParametersTypeDef]

### RunCommandParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RunCommandParametersTypeDef]

### EcsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.EcsParametersTypeDef]

### BatchParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.BatchParametersTypeDef]

### SqsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.SqsParametersTypeDef]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.HttpParametersTypeDef]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RedshiftDataParametersTypeDef]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.SageMakerPipelineParametersTypeDef]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.DeadLetterConfigTypeDef]

### RetryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RetryPolicyTypeDef]

### AppSyncParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.AppSyncParametersTypeDef]


# TestEventPatternRequestRequestTypeDef

### EventPattern
- **Type**: <class 'str'>
- **Required**: Yes

### Event
- **Type**: <class 'str'>
- **Required**: Yes


# TestEventPatternResponseTypeDef

### Result
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApiDestinationRequestRequestTypeDef

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


# UpdateApiDestinationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateArchiveRequestRequestTypeDef

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### EventPattern
- **Type**: typing.Optional[str]

### RetentionDays
- **Type**: typing.Optional[int]


# UpdateArchiveResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConnectionApiKeyAuthRequestParametersTypeDef

### ApiKeyName
- **Type**: typing.Optional[str]

### ApiKeyValue
- **Type**: typing.Optional[str]


# UpdateConnectionAuthRequestParametersTypeDef

### BasicAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionBasicAuthRequestParametersTypeDef]

### OAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionOAuthRequestParametersTypeDef]

### ApiKeyAuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionApiKeyAuthRequestParametersTypeDef]

### InvocationHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersTypeDef]


# UpdateConnectionBasicAuthRequestParametersTypeDef

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# UpdateConnectionOAuthClientRequestParametersTypeDef

### ClientID
- **Type**: typing.Optional[str]

### ClientSecret
- **Type**: typing.Optional[str]


# UpdateConnectionOAuthRequestParametersTypeDef

### ClientParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionOAuthClientRequestParametersTypeDef]

### AuthorizationEndpoint
- **Type**: typing.Optional[str]

### HttpMethod
- **Type**: typing.Optional[typing.Literal['GET', 'POST', 'PUT']]

### OAuthHttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ConnectionHttpParametersTypeDef]


# UpdateConnectionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AuthorizationType
- **Type**: typing.Optional[typing.Literal['API_KEY', 'BASIC', 'OAUTH_CLIENT_CREDENTIALS']]

### AuthParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.UpdateConnectionAuthRequestParametersTypeDef]


# UpdateConnectionResponseTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionState
- **Type**: typing.Literal['AUTHORIZED', 'AUTHORIZING', 'CREATING', 'DEAUTHORIZED', 'DEAUTHORIZING', 'DELETING', 'UPDATING']
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEndpointRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.RoutingConfigTypeDef]

### ReplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.ReplicationConfigTypeDef]

### EventBuses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.events_classes.EndpointEventBusTypeDef]]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateEndpointResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.RoutingConfigTypeDef'>
- **Required**: Yes

### ReplicationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ReplicationConfigTypeDef'>
- **Required**: Yes

### EventBuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.events_classes.EndpointEventBusTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEventBusRequestRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.events_classes.DeadLetterConfigTypeDef]


# UpdateEventBusResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.DeadLetterConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.events_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


