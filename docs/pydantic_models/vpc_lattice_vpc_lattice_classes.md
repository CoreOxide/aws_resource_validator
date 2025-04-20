# Vpc Lattice Vpc Lattice Classes

# AccessLogSubscriptionSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkLogType
- **Type**: typing.Optional[typing.Literal['RESOURCE', 'SERVICE']]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleUpdate]
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# BatchUpdateRuleResponse

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleUpdateSuccess]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleUpdateFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAccessLogSubscriptionResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkLogType
- **Type**: typing.Literal['RESOURCE', 'SERVICE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateListenerRequest

### defaultAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleAction, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateListenerResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['HTTP', 'HTTPS', 'TLS_PASSTHROUGH']
- **Required**: Yes

### serviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceConfigurationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ARN', 'CHILD', 'GROUP', 'SINGLE']
- **Required**: Yes

### allowAssociationToShareableServiceNetwork
- **Type**: typing.Optional[bool]

### clientToken
- **Type**: typing.Optional[str]

### portRanges
- **Type**: typing.Optional[typing.List[str]]

### protocol
- **Type**: typing.Optional[typing.Literal['TCP']]

### resourceConfigurationDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResourceConfigurationDefinition]

### resourceConfigurationGroupIdentifier
- **Type**: typing.Optional[str]

### resourceGatewayIdentifier
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateResourceConfigurationResponse

### allowAssociationToShareableServiceNetwork
- **Type**: <class 'bool'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### portRanges
- **Type**: typing.List[str]
- **Required**: Yes

### protocol
- **Type**: typing.Literal['TCP']
- **Required**: Yes

### resourceConfigurationDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResourceConfigurationDefinition'>
- **Required**: Yes

### resourceConfigurationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['ARN', 'CHILD', 'GROUP', 'SINGLE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceGatewayRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateResourceGatewayResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ipAddressType
- **Type**: typing.Literal['DUALSTACK', 'IPV4', 'IPV6']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleRequest

### action
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleAction, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput]
- **Required**: Yes

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### match
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatch, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatchOutput]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRuleResponse

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatchOutput'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceNetworkRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### clientToken
- **Type**: typing.Optional[str]

### sharingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.SharingConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateServiceNetworkResourceAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'PARTIAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceNetworkResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sharingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.SharingConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateServiceNetworkServiceAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### dnsEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateServiceNetworkVpcAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateServiceResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### dnsEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTargetGroupRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.TargetGroupConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateTargetGroupResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### config
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.TargetGroupConfig'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


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


# DeleteResourceEndpointAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### vpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourceGatewayRequest

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceGatewayResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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


# DeleteServiceNetworkResourceAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'PARTIAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceNetworkServiceAssociationRequest

### serviceNetworkServiceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkServiceAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceNetworkVpcAssociationRequest

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkVpcAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceRequest

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTargetGroupRequest

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetGroupResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterTargetsRequest

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.Target]
- **Required**: Yes


# DeregisterTargetsResponse

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.Target]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.TargetFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.WeightedTargetGroup]
- **Required**: Yes


# ForwardActionOutput

### targetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.WeightedTargetGroup]
- **Required**: Yes


# GetAccessLogSubscriptionRequest

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessLogSubscriptionResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkLogType
- **Type**: typing.Literal['RESOURCE', 'SERVICE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetListenerRequest

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetListenerResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['HTTP', 'HTTPS', 'TLS_PASSTHROUGH']
- **Required**: Yes

### serviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceConfigurationRequest

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceConfigurationResponse

### allowAssociationToShareableServiceNetwork
- **Type**: <class 'bool'>
- **Required**: Yes

### amazonManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### portRanges
- **Type**: typing.List[str]
- **Required**: Yes

### protocol
- **Type**: typing.Literal['TCP']
- **Required**: Yes

### resourceConfigurationDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResourceConfigurationDefinition'>
- **Required**: Yes

### resourceConfigurationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['ARN', 'CHILD', 'GROUP', 'SINGLE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceGatewayRequest

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceGatewayResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ipAddressType
- **Type**: typing.Literal['DUALSTACK', 'IPV4', 'IPV6']
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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


# GetRuleResponse

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### isDefault
- **Type**: <class 'bool'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatchOutput'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceNetworkRequest

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkResourceAssociationRequest

### serviceNetworkResourceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkResourceAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### dnsEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry'>
- **Required**: Yes

### failureCode
- **Type**: <class 'str'>
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### isManagedAssociation
- **Type**: <class 'bool'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### privateDnsEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry'>
- **Required**: Yes

### resourceConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'PARTIAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceNetworkResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### numberOfAssociatedServices
- **Type**: <class 'int'>
- **Required**: Yes

### numberOfAssociatedVPCs
- **Type**: <class 'int'>
- **Required**: Yes

### sharingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.SharingConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceNetworkServiceAssociationRequest

### serviceNetworkServiceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkServiceAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### dnsEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry'>
- **Required**: Yes

### failureCode
- **Type**: <class 'str'>
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### serviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceNetworkVpcAssociationRequest

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkVpcAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### failureCode
- **Type**: <class 'str'>
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### serviceNetworkArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceNetworkName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceRequest

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### dnsEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry'>
- **Required**: Yes

### failureCode
- **Type**: <class 'str'>
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# GetTargetGroupRequest

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetGroupResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### config
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.TargetGroupConfig'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureCode
- **Type**: <class 'str'>
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### serviceArns
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# HeaderMatch

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.HeaderMatchType'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.Matcher]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.HeaderMatch]]

### method
- **Type**: typing.Optional[str]

### pathMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PathMatch]


# HttpMatchOutput

### headerMatches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.HeaderMatch]]

### method
- **Type**: typing.Optional[str]

### pathMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PathMatch]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListAccessLogSubscriptionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.AccessLogSubscriptionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListListenersResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ListenerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListResourceConfigurationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResourceConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListResourceEndpointAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResourceEndpointAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListResourceGatewaysResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResourceGatewaySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListRulesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworkResourceAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ServiceNetworkResourceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworkServiceAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ServiceNetworkServiceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworkVpcAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ServiceNetworkVpcAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworkVpcEndpointAssociationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ServiceNetworkEndpointAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListServiceNetworksResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ServiceNetworkSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListServicesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ServiceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListTargetGroupsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.TargetGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.Target]]


# ListTargetsRequestPaginate

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.Target]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PaginatorConfig]


# ListTargetsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.TargetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListenerSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS', 'TLS_PASSTHROUGH']]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.PathMatchType'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.Target]
- **Required**: Yes


# RegisterTargetsResponse

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.Target]
- **Required**: Yes

### unsuccessful
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.TargetFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceConfigurationDefinition

### arnResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ArnResource]

### dnsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsResource]

### ipResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.IpResource]


# ResourceConfigurationSummary

### amazonManaged
- **Type**: typing.Optional[bool]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### resourceConfigurationGroupId
- **Type**: typing.Optional[str]

### resourceGatewayId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### type
- **Type**: typing.Optional[typing.Literal['ARN', 'CHILD', 'GROUP', 'SINGLE']]


# ResourceEndpointAssociationSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### resourceConfigurationArn
- **Type**: typing.Optional[str]

### resourceConfigurationId
- **Type**: typing.Optional[str]

### resourceConfigurationName
- **Type**: typing.Optional[str]

### vpcEndpointId
- **Type**: typing.Optional[str]

### vpcEndpointOwner
- **Type**: typing.Optional[str]


# ResourceGatewaySummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### vpcIdentifier
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.FixedResponseAction]

### forward
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ForwardAction, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ForwardActionOutput, NoneType]


# RuleActionOutput

### fixedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.FixedResponseAction]

### forward
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ForwardActionOutput]


# RuleMatch

### httpMatch
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.HttpMatch, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.HttpMatchOutput, NoneType]


# RuleMatchOutput

### httpMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.HttpMatchOutput]


# RuleSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### isDefault
- **Type**: typing.Optional[bool]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]


# RuleUpdate

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleAction, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput, NoneType]

### match
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatch, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatchOutput, NoneType]

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

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput]

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### isDefault
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatchOutput]

### name
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]


# ServiceNetworkEndpointAssociation

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### serviceNetworkArn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]

### vpcEndpointId
- **Type**: typing.Optional[str]

### vpcEndpointOwnerId
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]


# ServiceNetworkResourceAssociationSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### dnsEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry]

### failureCode
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### isManagedAssociation
- **Type**: typing.Optional[bool]

### privateDnsEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry]

### resourceConfigurationArn
- **Type**: typing.Optional[str]

### resourceConfigurationId
- **Type**: typing.Optional[str]

### resourceConfigurationName
- **Type**: typing.Optional[str]

### serviceNetworkArn
- **Type**: typing.Optional[str]

### serviceNetworkId
- **Type**: typing.Optional[str]

### serviceNetworkName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'PARTIAL']]


# ServiceNetworkServiceAssociationSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### customDomainName
- **Type**: typing.Optional[str]

### dnsEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry]

### id
- **Type**: typing.Optional[str]

### serviceArn
- **Type**: typing.Optional[str]

### serviceId
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### serviceNetworkArn
- **Type**: typing.Optional[str]

### serviceNetworkId
- **Type**: typing.Optional[str]

### serviceNetworkName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]


# ServiceNetworkSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### numberOfAssociatedResourceConfigurations
- **Type**: typing.Optional[int]

### numberOfAssociatedServices
- **Type**: typing.Optional[int]

### numberOfAssociatedVPCs
- **Type**: typing.Optional[int]


# ServiceNetworkVpcAssociationSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### serviceNetworkArn
- **Type**: typing.Optional[str]

### serviceNetworkId
- **Type**: typing.Optional[str]

### serviceNetworkName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### vpcId
- **Type**: typing.Optional[str]


# ServiceSummary

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### customDomainName
- **Type**: typing.Optional[str]

### dnsEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.DnsEntry]

### id
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]


# SharingConfig

### enabled
- **Type**: typing.Optional[bool]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Target

### id
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: typing.Optional[int]


# TargetFailure

### failureCode
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]


# TargetGroupConfig

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.HealthCheckConfig]

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

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['IPV4', 'IPV6']]

### lambdaEventStructureVersion
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS', 'TCP']]

### serviceArns
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### type
- **Type**: typing.Optional[typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']]

### vpcIdentifier
- **Type**: typing.Optional[str]


# TargetSummary

### id
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### reasonCode
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DRAINING', 'HEALTHY', 'INITIAL', 'UNAVAILABLE', 'UNHEALTHY', 'UNUSED']]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccessLogSubscriptionRequest

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAccessLogSubscriptionResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateListenerRequest

### defaultAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleAction, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput]
- **Required**: Yes

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateListenerResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['HTTP', 'HTTPS', 'TLS_PASSTHROUGH']
- **Required**: Yes

### serviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResourceConfigurationRequest

### resourceConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### allowAssociationToShareableServiceNetwork
- **Type**: typing.Optional[bool]

### portRanges
- **Type**: typing.Optional[typing.List[str]]

### resourceConfigurationDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResourceConfigurationDefinition]


# UpdateResourceConfigurationResponse

### allowAssociationToShareableServiceNetwork
- **Type**: <class 'bool'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### portRanges
- **Type**: typing.List[str]
- **Required**: Yes

### protocol
- **Type**: typing.Literal['TCP']
- **Required**: Yes

### resourceConfigurationDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResourceConfigurationDefinition'>
- **Required**: Yes

### resourceConfigurationGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceGatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['ARN', 'CHILD', 'GROUP', 'SINGLE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResourceGatewayRequest

### resourceGatewayIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# UpdateResourceGatewayResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ipAddressType
- **Type**: typing.Literal['IPV4', 'IPV6']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleAction, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput, NoneType]

### match
- **Type**: typing.Union[aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatch, aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatchOutput, NoneType]

### priority
- **Type**: typing.Optional[int]


# UpdateRuleResponse

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleActionOutput'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### isDefault
- **Type**: <class 'bool'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.RuleMatchOutput'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceNetworkRequest

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceNetworkResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceNetworkVpcAssociationRequest

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceNetworkVpcAssociationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceRequest

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### certificateArn
- **Type**: typing.Optional[str]


# UpdateServiceResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTargetGroupRequest

### healthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.HealthCheckConfig'>
- **Required**: Yes

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTargetGroupResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### config
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.TargetGroupConfig'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_classes.ResponseMetadata'>
- **Required**: Yes


# WeightedTargetGroup

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]


