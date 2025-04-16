# Vpc Lattice Classes

# AccessLogSubscriptionSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ArnResource

### arn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateRuleRequest

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleUpdate]
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# BatchUpdateRuleResponse

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleUpdateSuccess]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleUpdateFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccessLogSubscriptionRequest

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### serviceNetworkLogType
- **Type**: typing.Optional[typing.Literal['RESOURCE', 'SERVICE']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateListenerRequest

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnion'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['HTTP', 'HTTPS', 'TLS_PASSTHROUGH']
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateResourceGatewayRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRuleRequest

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnion'>
- **Required**: Yes

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchUnion'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateServiceNetworkRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### clientToken
- **Type**: typing.Optional[str]

### sharingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.SharingConfig]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateServiceNetworkResourceAssociationRequest

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateServiceNetworkServiceAssociationRequest

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateServiceNetworkVpcAssociationRequest

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateServiceRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### certificateArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### customDomainName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeleteAccessLogSubscriptionRequest

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthPolicyRequest

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListenerRequest

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceConfigurationRequest

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceEndpointAssociationRequest

### resourceEndpointAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceGatewayRequest

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequest

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkRequest

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkResourceAssociationRequest

### serviceNetworkResourceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkServiceAssociationRequest

### serviceNetworkServiceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkVpcAssociationRequest

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceRequest

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetGroupRequest

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTargetsRequest

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.Target]
- **Required**: Yes


# DeregisterTargetsResponse

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.Target]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# DnsEntry

### domainName
- **Type**: typing.Optional[str]

### hostedZoneId
- **Type**: typing.Optional[str]


# DnsResource

### domainName
- **Type**: typing.Optional[str]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]


# FixedResponseAction

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes


# ForwardAction

### targetGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.WeightedTargetGroup]
- **Required**: Yes


# ForwardActionOutput

### targetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.WeightedTargetGroup]
- **Required**: Yes


# ForwardActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAccessLogSubscriptionRequest

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthPolicyRequest

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthPolicyResponse

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetListenerRequest

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceConfigurationRequest

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceGatewayRequest

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetRuleRequest

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkRequest

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkResourceAssociationRequest

### serviceNetworkResourceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkServiceAssociationRequest

### serviceNetworkServiceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkVpcAssociationRequest

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceRequest

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetGroupRequest

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# HeaderMatch

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.HeaderMatchType'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### caseSensitive
- **Type**: typing.Optional[bool]


# HeaderMatchType

### contains
- **Type**: typing.Optional[str]

### exact
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# HealthCheckConfig

### enabled
- **Type**: typing.Optional[bool]

### healthCheckIntervalSeconds
- **Type**: typing.Optional[int]

### healthCheckTimeoutSeconds
- **Type**: typing.Optional[int]

### healthyThresholdCount
- **Type**: typing.Optional[int]

### matcher
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.Matcher]

### path
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS', 'TCP']]

### protocolVersion
- **Type**: typing.Optional[typing.Literal['HTTP1', 'HTTP2']]

### unhealthyThresholdCount
- **Type**: typing.Optional[int]


# HttpMatch

### headerMatches
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.HeaderMatch]]

### method
- **Type**: typing.Optional[str]

### pathMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PathMatch]


# HttpMatchOutput

### headerMatches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.HeaderMatch]]

### method
- **Type**: typing.Optional[str]

### pathMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PathMatch]


# HttpMatchUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IpResource

### ipAddress
- **Type**: typing.Optional[str]


# ListAccessLogSubscriptionsRequest

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessLogSubscriptionsRequestPaginate

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListAccessLogSubscriptionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.AccessLogSubscriptionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListListenersRequest

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListListenersRequestPaginate

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListListenersResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ListenerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceConfigurationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceConfigurationGroupIdentifier
- **Type**: typing.Optional[str]

### resourceGatewayIdentifier
- **Type**: typing.Optional[str]


# ListResourceConfigurationsRequestPaginate

### resourceConfigurationGroupIdentifier
- **Type**: typing.Optional[str]

### resourceGatewayIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListResourceConfigurationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ResourceConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceEndpointAssociationsRequest

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceEndpointAssociationIdentifier
- **Type**: typing.Optional[str]

### vpcEndpointId
- **Type**: typing.Optional[str]

### vpcEndpointOwner
- **Type**: typing.Optional[str]


# ListResourceEndpointAssociationsRequestPaginate

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### resourceEndpointAssociationIdentifier
- **Type**: typing.Optional[str]

### vpcEndpointId
- **Type**: typing.Optional[str]

### vpcEndpointOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListResourceEndpointAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ResourceEndpointAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceGatewaysRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListResourceGatewaysRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListResourceGatewaysResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ResourceGatewaySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRulesRequest

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRulesRequestPaginate

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListRulesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkResourceAssociationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceConfigurationIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]


# ListServiceNetworkResourceAssociationsRequestPaginate

### resourceConfigurationIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworkResourceAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkResourceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkServiceAssociationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serviceIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]


# ListServiceNetworkServiceAssociationsRequestPaginate

### serviceIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworkServiceAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkServiceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkVpcAssociationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### vpcIdentifier
- **Type**: typing.Optional[str]


# ListServiceNetworkVpcAssociationsRequestPaginate

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### vpcIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworkVpcAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkVpcAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkVpcEndpointAssociationsRequest

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkVpcEndpointAssociationsRequestPaginate

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworkVpcEndpointAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkEndpointAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworksRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworksResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServicesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListServicesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# ListTargetGroupsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### targetGroupType
- **Type**: typing.Optional[typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']]

### vpcIdentifier
- **Type**: typing.Optional[str]


# ListTargetGroupsRequestPaginate

### targetGroupType
- **Type**: typing.Optional[typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']]

### vpcIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListTargetGroupsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTargetsRequest

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.Target]]


# ListTargetsRequestPaginate

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.Target]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfig]


# ListTargetsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListenerSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Matcher

### httpCode
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathMatch

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.PathMatchType'>
- **Required**: Yes

### caseSensitive
- **Type**: typing.Optional[bool]


# PathMatchType

### exact
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# PutAuthPolicyRequest

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PutAuthPolicyResponse

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyRequest

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterTargetsRequest

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.Target]
- **Required**: Yes


# RegisterTargetsResponse

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.Target]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceConfigurationDefinition

### arnResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ArnResource]

### dnsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.DnsResource]

### ipResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.IpResource]


# ResourceConfigurationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceEndpointAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceGatewaySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RuleAction

### fixedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.FixedResponseAction]

### forward
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ForwardActionUnion]


# RuleActionOutput

### fixedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.FixedResponseAction]

### forward
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ForwardActionOutput]


# RuleActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleMatch

### httpMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.HttpMatchUnion]


# RuleMatchOutput

### httpMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.HttpMatchOutput]


# RuleMatchUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleUpdate

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnion]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchUnion]

### priority
- **Type**: typing.Optional[int]


# RuleUpdateFailure

### failureCode
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]

### ruleIdentifier
- **Type**: typing.Optional[str]


# RuleUpdateSuccess

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkEndpointAssociation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkResourceAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkServiceAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkVpcAssociationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SharingConfig

### enabled
- **Type**: typing.Optional[bool]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Target

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetFailure

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetGroupConfig

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.HealthCheckConfig]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['IPV4', 'IPV6']]

### lambdaEventStructureVersion
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### port
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS', 'TCP']]

### protocolVersion
- **Type**: typing.Optional[typing.Literal['GRPC', 'HTTP1', 'HTTP2']]

### vpcIdentifier
- **Type**: typing.Optional[str]


# TargetGroupSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessLogSubscriptionRequest

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateListenerRequest

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnion'>
- **Required**: Yes

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateResourceConfigurationRequest

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### allowAssociationToShareableServiceNetwork
- **Type**: typing.Optional[bool]

### portRanges
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceConfigurationDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ResourceConfigurationDefinition]


# UpdateResourceGatewayRequest

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateRuleRequest

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnion]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchUnion]

### priority
- **Type**: typing.Optional[int]


# UpdateServiceNetworkRequest

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceNetworkVpcAssociationRequest

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceRequest

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### certificateArn
- **Type**: typing.Optional[str]


# UpdateTargetGroupRequest

### healthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.HealthCheckConfig'>
- **Required**: Yes

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# WeightedTargetGroup

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]


