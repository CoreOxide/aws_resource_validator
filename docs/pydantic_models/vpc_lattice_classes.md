# Vpc Lattice Classes

# AccessLogSubscriptionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ArnResourceTypeDef

### arn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateRuleRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleUpdateTypeDef]
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# BatchUpdateRuleResponseTypeDef

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleUpdateSuccessTypeDef]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleUpdateFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccessLogSubscriptionRequestTypeDef

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


# CreateListenerRequestTypeDef

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnionTypeDef'>
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


# CreateResourceGatewayRequestTypeDef

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


# CreateRuleRequestTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnionTypeDef'>
- **Required**: Yes

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchUnionTypeDef'>
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


# CreateServiceNetworkRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### clientToken
- **Type**: typing.Optional[str]

### sharingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.SharingConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateServiceNetworkResourceAssociationRequestTypeDef

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


# CreateServiceNetworkServiceAssociationRequestTypeDef

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


# CreateServiceNetworkVpcAssociationRequestTypeDef

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


# CreateServiceRequestTypeDef

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


# DeleteAccessLogSubscriptionRequestTypeDef

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthPolicyRequestTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListenerRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceConfigurationRequestTypeDef

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceEndpointAssociationRequestTypeDef

### resourceEndpointAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceGatewayRequestTypeDef

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkRequestTypeDef

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkResourceAssociationRequestTypeDef

### serviceNetworkResourceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkServiceAssociationRequestTypeDef

### serviceNetworkServiceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkVpcAssociationRequestTypeDef

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceRequestTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetGroupRequestTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTargetsRequestTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetTypeDef]
- **Required**: Yes


# DeregisterTargetsResponseTypeDef

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetTypeDef]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DnsEntryTypeDef

### domainName
- **Type**: typing.Optional[str]

### hostedZoneId
- **Type**: typing.Optional[str]


# DnsResourceTypeDef

### domainName
- **Type**: typing.Optional[str]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]


# FixedResponseActionTypeDef

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes


# ForwardActionOutputTypeDef

### targetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.WeightedTargetGroupTypeDef]
- **Required**: Yes


# ForwardActionTypeDef

### targetGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.WeightedTargetGroupTypeDef]
- **Required**: Yes


# ForwardActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAccessLogSubscriptionRequestTypeDef

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthPolicyRequestTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthPolicyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetListenerRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceConfigurationRequestTypeDef

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceGatewayRequestTypeDef

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRuleRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkRequestTypeDef

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkResourceAssociationRequestTypeDef

### serviceNetworkResourceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkServiceAssociationRequestTypeDef

### serviceNetworkServiceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkVpcAssociationRequestTypeDef

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceRequestTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetGroupRequestTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# HeaderMatchTypeDef

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.HeaderMatchTypeTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### caseSensitive
- **Type**: typing.Optional[bool]


# HeaderMatchTypeTypeDef

### contains
- **Type**: typing.Optional[str]

### exact
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# HealthCheckConfigTypeDef

### enabled
- **Type**: typing.Optional[bool]

### healthCheckIntervalSeconds
- **Type**: typing.Optional[int]

### healthCheckTimeoutSeconds
- **Type**: typing.Optional[int]

### healthyThresholdCount
- **Type**: typing.Optional[int]

### matcher
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.MatcherTypeDef]

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


# HttpMatchOutputTypeDef

### headerMatches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.HeaderMatchTypeDef]]

### method
- **Type**: typing.Optional[str]

### pathMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PathMatchTypeDef]


# HttpMatchTypeDef

### headerMatches
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.HeaderMatchTypeDef]]

### method
- **Type**: typing.Optional[str]

### pathMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PathMatchTypeDef]


# HttpMatchUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IpResourceTypeDef

### ipAddress
- **Type**: typing.Optional[str]


# ListAccessLogSubscriptionsRequestPaginateTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListAccessLogSubscriptionsRequestTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessLogSubscriptionsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.AccessLogSubscriptionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListListenersRequestPaginateTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListListenersRequestTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListListenersResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ListenerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceConfigurationsRequestPaginateTypeDef

### resourceConfigurationGroupIdentifier
- **Type**: typing.Optional[str]

### resourceGatewayIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListResourceConfigurationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceConfigurationGroupIdentifier
- **Type**: typing.Optional[str]

### resourceGatewayIdentifier
- **Type**: typing.Optional[str]


# ListResourceConfigurationsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ResourceConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceEndpointAssociationsRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListResourceEndpointAssociationsRequestTypeDef

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


# ListResourceEndpointAssociationsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ResourceEndpointAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceGatewaysRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListResourceGatewaysRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListResourceGatewaysResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ResourceGatewaySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRulesRequestPaginateTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListRulesRequestTypeDef

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


# ListRulesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkResourceAssociationsRequestPaginateTypeDef

### resourceConfigurationIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServiceNetworkResourceAssociationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceConfigurationIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]


# ListServiceNetworkResourceAssociationsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkResourceAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkServiceAssociationsRequestPaginateTypeDef

### serviceIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServiceNetworkServiceAssociationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serviceIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]


# ListServiceNetworkServiceAssociationsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkServiceAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkVpcAssociationsRequestPaginateTypeDef

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### vpcIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServiceNetworkVpcAssociationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### vpcIdentifier
- **Type**: typing.Optional[str]


# ListServiceNetworkVpcAssociationsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkVpcAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkVpcEndpointAssociationsRequestPaginateTypeDef

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServiceNetworkVpcEndpointAssociationsRequestTypeDef

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworkVpcEndpointAssociationsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkEndpointAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworksRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServiceNetworksRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworksResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServicesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServicesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetGroupsRequestPaginateTypeDef

### targetGroupType
- **Type**: typing.Optional[typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']]

### vpcIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListTargetGroupsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### targetGroupType
- **Type**: typing.Optional[typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']]

### vpcIdentifier
- **Type**: typing.Optional[str]


# ListTargetGroupsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTargetsRequestPaginateTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListTargetsRequestTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetTypeDef]]


# ListTargetsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListenerSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MatcherTypeDef

### httpCode
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathMatchTypeDef

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.PathMatchTypeTypeDef'>
- **Required**: Yes

### caseSensitive
- **Type**: typing.Optional[bool]


# PathMatchTypeTypeDef

### exact
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# PutAuthPolicyRequestTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PutAuthPolicyResponseTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterTargetsRequestTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetTypeDef]
- **Required**: Yes


# RegisterTargetsResponseTypeDef

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetTypeDef]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceConfigurationDefinitionTypeDef

### arnResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ArnResourceTypeDef]

### dnsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.DnsResourceTypeDef]

### ipResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.IpResourceTypeDef]


# ResourceConfigurationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceEndpointAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceGatewaySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RuleActionOutputTypeDef

### fixedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.FixedResponseActionTypeDef]

### forward
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ForwardActionOutputTypeDef]


# RuleActionTypeDef

### fixedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.FixedResponseActionTypeDef]

### forward
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ForwardActionUnionTypeDef]


# RuleActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleMatchOutputTypeDef

### httpMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.HttpMatchOutputTypeDef]


# RuleMatchTypeDef

### httpMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.HttpMatchUnionTypeDef]


# RuleMatchUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleUpdateFailureTypeDef

### failureCode
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]

### ruleIdentifier
- **Type**: typing.Optional[str]


# RuleUpdateSuccessTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleUpdateTypeDef

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnionTypeDef]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchUnionTypeDef]

### priority
- **Type**: typing.Optional[int]


# ServiceNetworkEndpointAssociationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkResourceAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkServiceAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNetworkVpcAssociationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SharingConfigTypeDef

### enabled
- **Type**: typing.Optional[bool]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetFailureTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetGroupConfigTypeDef

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.HealthCheckConfigTypeDef]

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


# TargetGroupSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessLogSubscriptionRequestTypeDef

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateListenerRequestTypeDef

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnionTypeDef'>
- **Required**: Yes

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateResourceConfigurationRequestTypeDef

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### allowAssociationToShareableServiceNetwork
- **Type**: typing.Optional[bool]

### portRanges
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceConfigurationDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ResourceConfigurationDefinitionTypeDef]


# UpdateResourceGatewayRequestTypeDef

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateRuleRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionUnionTypeDef]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchUnionTypeDef]

### priority
- **Type**: typing.Optional[int]


# UpdateServiceNetworkRequestTypeDef

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceNetworkVpcAssociationRequestTypeDef

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceRequestTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### certificateArn
- **Type**: typing.Optional[str]


# UpdateTargetGroupRequestTypeDef

### healthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.HealthCheckConfigTypeDef'>
- **Required**: Yes

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# WeightedTargetGroupTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]


