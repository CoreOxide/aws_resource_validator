# Vpc Lattice Classes

# AccessLogSubscriptionSummaryTypeDef

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateRuleRequestRequestTypeDef

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


# CreateAccessLogSubscriptionRequestRequestTypeDef

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAccessLogSubscriptionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateListenerRequestRequestTypeDef

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionTypeDef'>
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


# CreateListenerResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleRequestRequestTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionTypeDef'>
- **Required**: Yes

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchTypeDef'>
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


# CreateRuleResponseTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionOutputTypeDef'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchOutputTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceNetworkRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateServiceNetworkResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceNetworkServiceAssociationRequestRequestTypeDef

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


# CreateServiceNetworkServiceAssociationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.DnsEntryTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceNetworkVpcAssociationRequestRequestTypeDef

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


# CreateServiceNetworkVpcAssociationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceRequestRequestTypeDef

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


# CreateServiceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.DnsEntryTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTargetGroupRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetGroupConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTargetGroupResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### config
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetGroupConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAccessLogSubscriptionRequestRequestTypeDef

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthPolicyRequestRequestTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListenerRequestRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequestRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkRequestRequestTypeDef

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkServiceAssociationRequestRequestTypeDef

### serviceNetworkServiceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkServiceAssociationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceNetworkVpcAssociationRequestRequestTypeDef

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceNetworkVpcAssociationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceRequestRequestTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTargetGroupRequestRequestTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetGroupResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterTargetsRequestRequestTypeDef

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


# GetAccessLogSubscriptionRequestRequestTypeDef

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessLogSubscriptionResponseTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAuthPolicyRequestRequestTypeDef

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


# GetListenerRequestRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetListenerResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyRequestRequestTypeDef

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


# GetRuleRequestRequestTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleResponseTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchOutputTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceNetworkRequestRequestTypeDef

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkResponseTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceNetworkServiceAssociationRequestRequestTypeDef

### serviceNetworkServiceAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkServiceAssociationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.DnsEntryTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceNetworkVpcAssociationRequestRequestTypeDef

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceNetworkVpcAssociationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceRequestRequestTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.DnsEntryTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTargetGroupRequestRequestTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetGroupResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### config
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetGroupConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
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


# ListAccessLogSubscriptionsRequestListAccessLogSubscriptionsPaginateTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListAccessLogSubscriptionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListListenersRequestListListenersPaginateTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListListenersRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRulesRequestListRulesPaginateTypeDef

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListRulesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceNetworkServiceAssociationsRequestListServiceNetworkServiceAssociationsPaginateTypeDef

### serviceIdentifier
- **Type**: typing.Optional[str]

### serviceNetworkIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServiceNetworkServiceAssociationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceNetworkVpcAssociationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceNetworksRequestListServiceNetworksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServiceNetworksRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServiceNetworksResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceNetworkSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicesRequestListServicesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListServicesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServicesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.vpc_lattice_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListTargetGroupsRequestListTargetGroupsPaginateTypeDef

### targetGroupType
- **Type**: typing.Optional[typing.Literal['ALB', 'INSTANCE', 'IP', 'LAMBDA']]

### vpcIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListTargetGroupsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetsRequestListTargetsPaginateTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.PaginatorConfigTypeDef]


# ListTargetsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListenerSummaryTypeDef

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


# PutAuthPolicyRequestRequestTypeDef

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


# PutResourcePolicyRequestRequestTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterTargetsRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.ForwardActionTypeDef]


# RuleMatchOutputTypeDef

### httpMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.HttpMatchOutputTypeDef]


# RuleMatchTypeDef

### httpMatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.HttpMatchTypeDef]


# RuleSummaryTypeDef

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


# RuleUpdateFailureTypeDef

### failureCode
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]

### ruleIdentifier
- **Type**: typing.Optional[str]


# RuleUpdateSuccessTypeDef

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionOutputTypeDef]

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### isDefault
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchOutputTypeDef]

### name
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]


# RuleUpdateTypeDef

### ruleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionTypeDef]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchTypeDef]

### priority
- **Type**: typing.Optional[int]


# ServiceNetworkServiceAssociationSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### customDomainName
- **Type**: typing.Optional[str]

### dnsEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.DnsEntryTypeDef]

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


# ServiceNetworkSummaryTypeDef

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

### numberOfAssociatedServices
- **Type**: typing.Optional[int]

### numberOfAssociatedVPCs
- **Type**: typing.Optional[int]


# ServiceNetworkVpcAssociationSummaryTypeDef

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


# ServiceSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### customDomainName
- **Type**: typing.Optional[str]

### dnsEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.DnsEntryTypeDef]

### id
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetFailureTypeDef

### failureCode
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]


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


# TargetSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### reasonCode
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DRAINING', 'HEALTHY', 'INITIAL', 'UNAVAILABLE', 'UNHEALTHY', 'UNUSED']]


# TargetTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: typing.Optional[int]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessLogSubscriptionRequestRequestTypeDef

### accessLogSubscriptionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAccessLogSubscriptionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateListenerRequestRequestTypeDef

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionTypeDef'>
- **Required**: Yes

### listenerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateListenerResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRuleRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionTypeDef]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchTypeDef]

### priority
- **Type**: typing.Optional[int]


# UpdateRuleResponseTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleActionOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.RuleMatchOutputTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceNetworkRequestRequestTypeDef

### authType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### serviceNetworkIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceNetworkResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceNetworkVpcAssociationRequestRequestTypeDef

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### serviceNetworkVpcAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceNetworkVpcAssociationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceRequestRequestTypeDef

### serviceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### certificateArn
- **Type**: typing.Optional[str]


# UpdateServiceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTargetGroupRequestRequestTypeDef

### healthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.HealthCheckConfigTypeDef'>
- **Required**: Yes

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTargetGroupResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### config
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.TargetGroupConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.vpc_lattice_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WeightedTargetGroupTypeDef

### targetGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]


