# Migration Hub Refactor Spaces Migration Hub Refactor Spaces Classes

# ApiGatewayProxyConfig

### ApiGatewayId
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'REGIONAL']]

### NlbArn
- **Type**: typing.Optional[str]

### NlbName
- **Type**: typing.Optional[str]

### ProxyUrl
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]

### VpcLinkId
- **Type**: typing.Optional[str]


# ApiGatewayProxyInput

### EndpointType
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'REGIONAL']]

### StageName
- **Type**: typing.Optional[str]


# ApiGatewayProxySummary

### ApiGatewayId
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'REGIONAL']]

### NlbArn
- **Type**: typing.Optional[str]

### NlbName
- **Type**: typing.Optional[str]

### ProxyUrl
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]

### VpcLinkId
- **Type**: typing.Optional[str]


# ApplicationSummary

### ApiGatewayProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ApiGatewayProxySummary]

### ApplicationId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreatedByAccountId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### EnvironmentId
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ErrorResponse]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### ProxyType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY']]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### VpcId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationRequest

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProxyType
- **Type**: typing.Literal['API_GATEWAY']
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiGatewayProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ApiGatewayProxyInput]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateApplicationResponse

### ApiGatewayProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ApiGatewayProxyInput'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxyType
- **Type**: typing.Literal['API_GATEWAY']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkFabricType
- **Type**: typing.Literal['NONE', 'TRANSIT_GATEWAY']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateEnvironmentResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkFabricType
- **Type**: typing.Literal['NONE', 'TRANSIT_GATEWAY']
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRouteRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RouteType
- **Type**: typing.Literal['DEFAULT', 'URI_PATH']
- **Required**: Yes

### ServiceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### DefaultRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.DefaultRouteInput]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UriPathRoute
- **Type**: typing.Union[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.UriPathRouteInput, aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.UriPathRouteInputOutput, NoneType]


# CreateRouteResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteType
- **Type**: typing.Literal['DEFAULT', 'URI_PATH']
- **Required**: Yes

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UriPathRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.UriPathRouteInputOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: typing.Literal['LAMBDA', 'URL']
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LambdaEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.LambdaEndpointInput]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UrlEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.UrlEndpointInput]

### VpcId
- **Type**: typing.Optional[str]


# CreateServiceResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: typing.Literal['LAMBDA', 'URL']
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### LambdaEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.LambdaEndpointInput'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UrlEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.UrlEndpointInput'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# DefaultRouteInput

### ActivationState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# DeleteApplicationRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEnvironmentRequest

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RouteIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# EnvironmentSummary

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ErrorResponse]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### NetworkFabricType
- **Type**: typing.Optional[typing.Literal['NONE', 'TRANSIT_GATEWAY']]

### OwnerAccountId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TransitGatewayId
- **Type**: typing.Optional[str]


# EnvironmentVpc

### AccountId
- **Type**: typing.Optional[str]

### CidrBlocks
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### EnvironmentId
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### VpcId
- **Type**: typing.Optional[str]

### VpcName
- **Type**: typing.Optional[str]


# ErrorResponse

### AccountId
- **Type**: typing.Optional[str]

### AdditionalDetails
- **Type**: typing.Optional[typing.Dict[str, str]]

### Code
- **Type**: typing.Optional[typing.Literal['INVALID_RESOURCE_STATE', 'NOT_AUTHORIZED', 'REQUEST_LIMIT_EXCEEDED', 'RESOURCE_CREATION_FAILURE', 'RESOURCE_DELETION_FAILURE', 'RESOURCE_IN_USE', 'RESOURCE_LIMIT_EXCEEDED', 'RESOURCE_NOT_FOUND', 'RESOURCE_RETRIEVAL_FAILURE', 'RESOURCE_UPDATE_FAILURE', 'SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE', 'STATE_TRANSITION_FAILURE']]

### Message
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'APPLICATION', 'ENVIRONMENT', 'IAM_ROLE', 'LAMBDA', 'LOAD_BALANCER_LISTENER', 'NLB', 'RESOURCE_SHARE', 'ROUTE', 'ROUTE_TABLE', 'SECURITY_GROUP', 'SERVICE', 'SUBNET', 'TARGET_GROUP', 'TRANSIT_GATEWAY', 'TRANSIT_GATEWAY_ATTACHMENT', 'VPC', 'VPC_ENDPOINT_SERVICE_CONFIGURATION', 'VPC_LINK']]


# GetApplicationRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponse

### ApiGatewayProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ApiGatewayProxyConfig'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ErrorResponse'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxyType
- **Type**: typing.Literal['API_GATEWAY']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnvironmentRequest

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ErrorResponse'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkFabricType
- **Type**: typing.Literal['NONE', 'TRANSIT_GATEWAY']
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TransitGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# GetRouteRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RouteIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteResponse

### AppendSourcePath
- **Type**: <class 'bool'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ErrorResponse'>
- **Required**: Yes

### IncludeChildPaths
- **Type**: <class 'bool'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Methods
- **Type**: typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PathResourceToId
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteType
- **Type**: typing.Literal['DEFAULT', 'URI_PATH']
- **Required**: Yes

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### SourcePath
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedByAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointType
- **Type**: typing.Literal['LAMBDA', 'URL']
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ErrorResponse'>
- **Required**: Yes

### LambdaEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.LambdaEndpointConfig'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UrlEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.UrlEndpointConfig'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# LambdaEndpointConfig

### Arn
- **Type**: typing.Optional[str]


# LambdaEndpointInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaEndpointSummary

### Arn
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginate

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.PaginatorConfig]


# ListApplicationsResponse

### ApplicationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEnvironmentVpcsRequest

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEnvironmentVpcsRequestPaginate

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.PaginatorConfig]


# ListEnvironmentVpcsResponse

### EnvironmentVpcList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.EnvironmentVpc]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.PaginatorConfig]


# ListEnvironmentsResponse

### EnvironmentSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.EnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoutesRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRoutesRequestPaginate

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.PaginatorConfig]


# ListRoutesResponse

### RouteSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.RouteSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesRequest

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServicesRequestPaginate

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.PaginatorConfig]


# ListServicesResponse

### ServiceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ServiceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequest

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
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


# RouteSummary

### AppendSourcePath
- **Type**: typing.Optional[bool]

### ApplicationId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreatedByAccountId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### EnvironmentId
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ErrorResponse]

### IncludeChildPaths
- **Type**: typing.Optional[bool]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Methods
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]]

### OwnerAccountId
- **Type**: typing.Optional[str]

### PathResourceToId
- **Type**: typing.Optional[typing.Dict[str, str]]

### RouteId
- **Type**: typing.Optional[str]

### RouteType
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'URI_PATH']]

### ServiceId
- **Type**: typing.Optional[str]

### SourcePath
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ServiceSummary

### ApplicationId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreatedByAccountId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[typing.Literal['LAMBDA', 'URL']]

### EnvironmentId
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ErrorResponse]

### LambdaEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.LambdaEndpointSummary]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### ServiceId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UrlEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.UrlEndpointSummary]

### VpcId
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateRouteRequest

### ActivationState
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RouteIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRouteResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'INACTIVE', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_classes.ResponseMetadata'>
- **Required**: Yes


# UriPathRouteInput

### ActivationState
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### SourcePath
- **Type**: <class 'str'>
- **Required**: Yes

### AppendSourcePath
- **Type**: typing.Optional[bool]

### IncludeChildPaths
- **Type**: typing.Optional[bool]

### Methods
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]]


# UriPathRouteInputOutput

### ActivationState
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### SourcePath
- **Type**: <class 'str'>
- **Required**: Yes

### AppendSourcePath
- **Type**: typing.Optional[bool]

### IncludeChildPaths
- **Type**: typing.Optional[bool]

### Methods
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]]


# UrlEndpointConfig

### HealthUrl
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# UrlEndpointInput

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### HealthUrl
- **Type**: typing.Optional[str]


# UrlEndpointSummary

### HealthUrl
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


