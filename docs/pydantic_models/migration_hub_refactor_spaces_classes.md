# Pydantic Models in migration_hub_refactor_spaces_classes

# ApiGatewayProxyConfigTypeDef

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


# ApiGatewayProxyInputTypeDef

### EndpointType
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'REGIONAL']]

### StageName
- **Type**: typing.Optional[str]


# ApiGatewayProxySummaryTypeDef

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


# ApplicationSummaryTypeDef

### ApiGatewayProxy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ApiGatewayProxySummaryTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ErrorResponseTypeDef]

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

# CreateApplicationRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ApiGatewayProxyInputTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateApplicationResponseTypeDef

### ApiGatewayProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ApiGatewayProxyInputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEnvironmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRouteRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.DefaultRouteInputTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UriPathRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.UriPathRouteInputTypeDef]


# CreateRouteResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.UriPathRouteInputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.LambdaEndpointInputTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UrlEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.UrlEndpointInputTypeDef]

### VpcId
- **Type**: typing.Optional[str]


# CreateServiceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.LambdaEndpointInputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.UrlEndpointInputTypeDef'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefaultRouteInputTypeDef

### ActivationState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# DeleteApplicationRequestRequestTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentRequestRequestTypeDef

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteRequestRequestTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RouteIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceRequestRequestTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ErrorResponseTypeDef]

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


# EnvironmentVpcTypeDef

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


# ErrorResponseTypeDef

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


# GetApplicationRequestRequestTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponseTypeDef

### ApiGatewayProxy
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ApiGatewayProxyConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ErrorResponseTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnvironmentRequestRequestTypeDef

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ErrorResponseTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRouteRequestRequestTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RouteIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ErrorResponseTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceRequestRequestTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ErrorResponseTypeDef'>
- **Required**: Yes

### LambdaEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.LambdaEndpointConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.UrlEndpointConfigTypeDef'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LambdaEndpointConfigTypeDef

### Arn
- **Type**: typing.Optional[str]


# LambdaEndpointInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaEndpointSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]


# ListApplicationsRequestListApplicationsPaginateTypeDef

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### ApplicationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentVpcsRequestListEnvironmentVpcsPaginateTypeDef

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.PaginatorConfigTypeDef]


# ListEnvironmentVpcsRequestRequestTypeDef

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEnvironmentVpcsResponseTypeDef

### EnvironmentVpcList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.EnvironmentVpcTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEnvironmentsRequestListEnvironmentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsResponseTypeDef

### EnvironmentSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.EnvironmentSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoutesRequestListRoutesPaginateTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.PaginatorConfigTypeDef]


# ListRoutesRequestRequestTypeDef

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


# ListRoutesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RouteSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.RouteSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicesRequestListServicesPaginateTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.PaginatorConfigTypeDef]


# ListServicesRequestRequestTypeDef

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


# ListServicesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequestRequestTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
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


# RouteSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ErrorResponseTypeDef]

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


# ServiceSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ErrorResponseTypeDef]

### LambdaEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.LambdaEndpointSummaryTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.UrlEndpointSummaryTypeDef]

### VpcId
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateRouteRequestRequestTypeDef

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


# UpdateRouteResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UriPathRouteInputTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]]


# UrlEndpointConfigTypeDef

### HealthUrl
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# UrlEndpointInputTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### HealthUrl
- **Type**: typing.Optional[str]


# UrlEndpointSummaryTypeDef

### HealthUrl
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


