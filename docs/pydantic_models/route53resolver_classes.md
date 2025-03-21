# Route53Resolver Classes

# AssociateFirewallRuleGroupRequestTypeDef

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MutationProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]]


# AssociateFirewallRuleGroupResponseTypeDef

### FirewallRuleGroupAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateResolverEndpointIpAddressRequestTypeDef

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.IpAddressUpdateTypeDef'>
- **Required**: Yes


# AssociateResolverEndpointIpAddressResponseTypeDef

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateResolverQueryLogConfigRequestTypeDef

### ResolverQueryLogConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateResolverQueryLogConfigResponseTypeDef

### ResolverQueryLogConfigAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverQueryLogConfigAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateResolverRuleRequestTypeDef

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssociateResolverRuleResponseTypeDef

### ResolverRuleAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateFirewallDomainListRequestTypeDef

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]]


# CreateFirewallDomainListResponseTypeDef

### FirewallDomainList
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallDomainListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFirewallRuleGroupRequestTypeDef

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]]


# CreateFirewallRuleGroupResponseTypeDef

### FirewallRuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFirewallRuleRequestTypeDef

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['ALERT', 'ALLOW', 'BLOCK']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallDomainListId
- **Type**: typing.Optional[str]

### BlockResponse
- **Type**: typing.Optional[typing.Literal['NODATA', 'NXDOMAIN', 'OVERRIDE']]

### BlockOverrideDomain
- **Type**: typing.Optional[str]

### BlockOverrideDnsType
- **Type**: typing.Optional[typing.Literal['CNAME']]

### BlockOverrideTtl
- **Type**: typing.Optional[int]

### FirewallDomainRedirectionAction
- **Type**: typing.Optional[typing.Literal['INSPECT_REDIRECTION_DOMAIN', 'TRUST_REDIRECTION_DOMAIN']]

### Qtype
- **Type**: typing.Optional[str]

### DnsThreatProtection
- **Type**: typing.Optional[typing.Literal['DGA', 'DNS_TUNNELING']]

### ConfidenceThreshold
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# CreateFirewallRuleResponseTypeDef

### FirewallRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOutpostResolverRequestTypeDef

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PreferredInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]]


# CreateOutpostResolverResponseTypeDef

### OutpostResolver
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.OutpostResolverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResolverEndpointRequestTypeDef

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Direction
- **Type**: typing.Literal['INBOUND', 'OUTBOUND']
- **Required**: Yes

### IpAddresses
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.IpAddressRequestTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]

### PreferredInstanceType
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]]

### ResolverEndpointType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]

### Protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Do53', 'DoH', 'DoH-FIPS']]]


# CreateResolverEndpointResponseTypeDef

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResolverQueryLogConfigRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]]


# CreateResolverQueryLogConfigResponseTypeDef

### ResolverQueryLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverQueryLogConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResolverRuleRequestTypeDef

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleType
- **Type**: typing.Literal['FORWARD', 'RECURSIVE', 'SYSTEM']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### TargetIps
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TargetAddressTypeDef]]

### ResolverEndpointId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]]


# CreateResolverRuleResponseTypeDef

### ResolverRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFirewallDomainListRequestTypeDef

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFirewallDomainListResponseTypeDef

### FirewallDomainList
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallDomainListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFirewallRuleGroupRequestTypeDef

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFirewallRuleGroupResponseTypeDef

### FirewallRuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFirewallRuleRequestTypeDef

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallDomainListId
- **Type**: typing.Optional[str]

### FirewallThreatProtectionId
- **Type**: typing.Optional[str]

### Qtype
- **Type**: typing.Optional[str]


# DeleteFirewallRuleResponseTypeDef

### FirewallRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteOutpostResolverRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutpostResolverResponseTypeDef

### OutpostResolver
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.OutpostResolverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResolverEndpointRequestTypeDef

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverEndpointResponseTypeDef

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResolverQueryLogConfigRequestTypeDef

### ResolverQueryLogConfigId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverQueryLogConfigResponseTypeDef

### ResolverQueryLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverQueryLogConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResolverRuleRequestTypeDef

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverRuleResponseTypeDef

### ResolverRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateFirewallRuleGroupRequestTypeDef

### FirewallRuleGroupAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFirewallRuleGroupResponseTypeDef

### FirewallRuleGroupAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateResolverEndpointIpAddressRequestTypeDef

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.IpAddressUpdateTypeDef'>
- **Required**: Yes


# DisassociateResolverEndpointIpAddressResponseTypeDef

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateResolverQueryLogConfigRequestTypeDef

### ResolverQueryLogConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateResolverQueryLogConfigResponseTypeDef

### ResolverQueryLogConfigAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverQueryLogConfigAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateResolverRuleRequestTypeDef

### VPCId
- **Type**: <class 'str'>
- **Required**: Yes

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateResolverRuleResponseTypeDef

### ResolverRuleAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# FirewallConfigTypeDef

### Id
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### FirewallFailOpen
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'USE_LOCAL_RESOURCE_SETTING']]


# FirewallDomainListMetadataTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### ManagedOwnerName
- **Type**: typing.Optional[str]


# FirewallDomainListTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### DomainCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'COMPLETE_IMPORT_FAILED', 'DELETING', 'IMPORTING', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]

### ManagedOwnerName
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[str]


# FirewallRuleGroupAssociationTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### FirewallRuleGroupId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### MutationProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ManagedOwnerName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'DELETING', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[str]


# FirewallRuleGroupMetadataTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['NOT_SHARED', 'SHARED_BY_ME', 'SHARED_WITH_ME']]


# FirewallRuleGroupTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'DELETING', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['NOT_SHARED', 'SHARED_BY_ME', 'SHARED_WITH_ME']]

### CreationTime
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[str]


# FirewallRuleTypeDef

### FirewallRuleGroupId
- **Type**: typing.Optional[str]

### FirewallDomainListId
- **Type**: typing.Optional[str]

### FirewallThreatProtectionId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Action
- **Type**: typing.Optional[typing.Literal['ALERT', 'ALLOW', 'BLOCK']]

### BlockResponse
- **Type**: typing.Optional[typing.Literal['NODATA', 'NXDOMAIN', 'OVERRIDE']]

### BlockOverrideDomain
- **Type**: typing.Optional[str]

### BlockOverrideDnsType
- **Type**: typing.Optional[typing.Literal['CNAME']]

### BlockOverrideTtl
- **Type**: typing.Optional[int]

### CreatorRequestId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[str]

### FirewallDomainRedirectionAction
- **Type**: typing.Optional[typing.Literal['INSPECT_REDIRECTION_DOMAIN', 'TRUST_REDIRECTION_DOMAIN']]

### Qtype
- **Type**: typing.Optional[str]

### DnsThreatProtection
- **Type**: typing.Optional[typing.Literal['DGA', 'DNS_TUNNELING']]

### ConfidenceThreshold
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# GetFirewallConfigRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallConfigResponseTypeDef

### FirewallConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFirewallDomainListRequestTypeDef

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallDomainListResponseTypeDef

### FirewallDomainList
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallDomainListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFirewallRuleGroupAssociationRequestTypeDef

### FirewallRuleGroupAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallRuleGroupAssociationResponseTypeDef

### FirewallRuleGroupAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFirewallRuleGroupPolicyRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallRuleGroupPolicyResponseTypeDef

### FirewallRuleGroupPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFirewallRuleGroupRequestTypeDef

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallRuleGroupResponseTypeDef

### FirewallRuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOutpostResolverRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOutpostResolverResponseTypeDef

### OutpostResolver
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.OutpostResolverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverConfigRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverConfigResponseTypeDef

### ResolverConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverDnssecConfigRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverDnssecConfigResponseTypeDef

### ResolverDNSSECConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverDnssecConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverEndpointRequestTypeDef

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverEndpointResponseTypeDef

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverQueryLogConfigAssociationRequestTypeDef

### ResolverQueryLogConfigAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverQueryLogConfigAssociationResponseTypeDef

### ResolverQueryLogConfigAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverQueryLogConfigAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverQueryLogConfigPolicyRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverQueryLogConfigPolicyResponseTypeDef

### ResolverQueryLogConfigPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverQueryLogConfigRequestTypeDef

### ResolverQueryLogConfigId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverQueryLogConfigResponseTypeDef

### ResolverQueryLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverQueryLogConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverRuleAssociationRequestTypeDef

### ResolverRuleAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverRuleAssociationResponseTypeDef

### ResolverRuleAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverRulePolicyRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverRulePolicyResponseTypeDef

### ResolverRulePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverRuleRequestTypeDef

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverRuleResponseTypeDef

### ResolverRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportFirewallDomainsRequestTypeDef

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['REPLACE']
- **Required**: Yes

### DomainFileUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ImportFirewallDomainsResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'COMPLETE_IMPORT_FAILED', 'DELETING', 'IMPORTING', 'UPDATING']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IpAddressRequestTypeDef

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### Ip
- **Type**: typing.Optional[str]

### Ipv6
- **Type**: typing.Optional[str]


# IpAddressResponseTypeDef

### IpId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### Ip
- **Type**: typing.Optional[str]

### Ipv6
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ATTACHED', 'ATTACHING', 'CREATING', 'DELETE_FAILED_FAS_EXPIRED', 'DELETING', 'DETACHING', 'FAILED_CREATION', 'FAILED_RESOURCE_GONE', 'REMAP_ATTACHING', 'REMAP_DETACHING', 'UPDATE_FAILED', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[str]


# IpAddressUpdateTypeDef

### IpId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### Ip
- **Type**: typing.Optional[str]

### Ipv6
- **Type**: typing.Optional[str]


# ListFirewallConfigsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListFirewallConfigsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallConfigsResponseTypeDef

### FirewallConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.FirewallConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallDomainListsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListFirewallDomainListsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallDomainListsResponseTypeDef

### FirewallDomainLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.FirewallDomainListMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallDomainsRequestPaginateTypeDef

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListFirewallDomainsRequestTypeDef

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallDomainsResponseTypeDef

### Domains
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRuleGroupAssociationsRequestPaginateTypeDef

### FirewallRuleGroupId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'DELETING', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListFirewallRuleGroupAssociationsRequestTypeDef

### FirewallRuleGroupId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'DELETING', 'UPDATING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRuleGroupAssociationsResponseTypeDef

### FirewallRuleGroupAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRuleGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListFirewallRuleGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRuleGroupsResponseTypeDef

### FirewallRuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRulesRequestPaginateTypeDef

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: typing.Optional[int]

### Action
- **Type**: typing.Optional[typing.Literal['ALERT', 'ALLOW', 'BLOCK']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListFirewallRulesRequestTypeDef

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: typing.Optional[int]

### Action
- **Type**: typing.Optional[typing.Literal['ALERT', 'ALLOW', 'BLOCK']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRulesResponseTypeDef

### FirewallRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOutpostResolversRequestPaginateTypeDef

### OutpostArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListOutpostResolversRequestTypeDef

### OutpostArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOutpostResolversResponseTypeDef

### OutpostResolvers
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.OutpostResolverTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverConfigsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListResolverConfigsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResolverConfigsResponseTypeDef

### ResolverConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.ResolverConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverDnssecConfigsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListResolverDnssecConfigsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]


# ListResolverDnssecConfigsResponseTypeDef

### ResolverDnssecConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.ResolverDnssecConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverEndpointIpAddressesRequestPaginateTypeDef

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListResolverEndpointIpAddressesRequestTypeDef

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResolverEndpointIpAddressesResponseTypeDef

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### IpAddresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.IpAddressResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverEndpointsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListResolverEndpointsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]


# ListResolverEndpointsResponseTypeDef

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.ResolverEndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverQueryLogConfigAssociationsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListResolverQueryLogConfigAssociationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListResolverQueryLogConfigAssociationsResponseTypeDef

### TotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalFilteredCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverQueryLogConfigAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.ResolverQueryLogConfigAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverQueryLogConfigsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListResolverQueryLogConfigsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListResolverQueryLogConfigsResponseTypeDef

### TotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalFilteredCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverQueryLogConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.ResolverQueryLogConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverRuleAssociationsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListResolverRuleAssociationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]


# ListResolverRuleAssociationsResponseTypeDef

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverRuleAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverRulesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListResolverRulesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.FilterTypeDef]]


# ListResolverRulesResponseTypeDef

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OutpostResolverTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### PreferredInstanceType
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTION_NEEDED', 'CREATING', 'DELETING', 'FAILED_CREATION', 'FAILED_DELETION', 'OPERATIONAL', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutFirewallRuleGroupPolicyRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallRuleGroupPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutFirewallRuleGroupPolicyResponseTypeDef

### ReturnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResolverQueryLogConfigPolicyRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResolverQueryLogConfigPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResolverQueryLogConfigPolicyResponseTypeDef

### ReturnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResolverRulePolicyRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResolverRulePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResolverRulePolicyResponseTypeDef

### ReturnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResolverConfigTypeDef

### Id
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### AutodefinedReverse
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'UPDATING_TO_USE_LOCAL_RESOURCE_SETTING', 'USE_LOCAL_RESOURCE_SETTING']]


# ResolverDnssecConfigTypeDef

### Id
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ValidationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'UPDATING_TO_USE_LOCAL_RESOURCE_SETTING', 'USE_LOCAL_RESOURCE_SETTING']]


# ResolverEndpointTypeDef

### Id
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Direction
- **Type**: typing.Optional[typing.Literal['INBOUND', 'OUTBOUND']]

### IpAddressCount
- **Type**: typing.Optional[int]

### HostVPCId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTION_NEEDED', 'AUTO_RECOVERING', 'CREATING', 'DELETING', 'OPERATIONAL', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]

### PreferredInstanceType
- **Type**: typing.Optional[str]

### ResolverEndpointType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['Do53', 'DoH', 'DoH-FIPS']]]


# ResolverQueryLogConfigAssociationTypeDef

### Id
- **Type**: typing.Optional[str]

### ResolverQueryLogConfigId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTION_NEEDED', 'ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### Error
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'DESTINATION_NOT_FOUND', 'INTERNAL_SERVICE_ERROR', 'NONE']]

### ErrorMessage
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[str]


# ResolverQueryLogConfigTypeDef

### Id
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'DELETING', 'FAILED']]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['NOT_SHARED', 'SHARED_BY_ME', 'SHARED_WITH_ME']]

### AssociationCount
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[str]


# ResolverRuleAssociationTypeDef

### Id
- **Type**: typing.Optional[str]

### ResolverRuleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VPCId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'CREATING', 'DELETING', 'FAILED', 'OVERRIDDEN']]

### StatusMessage
- **Type**: typing.Optional[str]


# ResolverRuleConfigTypeDef

### Name
- **Type**: typing.Optional[str]

### TargetIps
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TargetAddressTypeDef]]

### ResolverEndpointId
- **Type**: typing.Optional[str]


# ResolverRuleTypeDef

### Id
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'DELETING', 'FAILED', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]

### RuleType
- **Type**: typing.Optional[typing.Literal['FORWARD', 'RECURSIVE', 'SYSTEM']]

### Name
- **Type**: typing.Optional[str]

### TargetIps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver_classes.TargetAddressTypeDef]]

### ResolverEndpointId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['NOT_SHARED', 'SHARED_BY_ME', 'SHARED_WITH_ME']]

### CreationTime
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[str]


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


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetAddressTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFirewallConfigRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallFailOpen
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'USE_LOCAL_RESOURCE_SETTING']
- **Required**: Yes


# UpdateFirewallConfigResponseTypeDef

### FirewallConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFirewallDomainsRequestTypeDef

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['ADD', 'REMOVE', 'REPLACE']
- **Required**: Yes

### Domains
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFirewallDomainsResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'COMPLETE_IMPORT_FAILED', 'DELETING', 'IMPORTING', 'UPDATING']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFirewallRuleGroupAssociationRequestTypeDef

### FirewallRuleGroupAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: typing.Optional[int]

### MutationProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Name
- **Type**: typing.Optional[str]


# UpdateFirewallRuleGroupAssociationResponseTypeDef

### FirewallRuleGroupAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleGroupAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFirewallRuleRequestTypeDef

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallDomainListId
- **Type**: typing.Optional[str]

### FirewallThreatProtectionId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Action
- **Type**: typing.Optional[typing.Literal['ALERT', 'ALLOW', 'BLOCK']]

### BlockResponse
- **Type**: typing.Optional[typing.Literal['NODATA', 'NXDOMAIN', 'OVERRIDE']]

### BlockOverrideDomain
- **Type**: typing.Optional[str]

### BlockOverrideDnsType
- **Type**: typing.Optional[typing.Literal['CNAME']]

### BlockOverrideTtl
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### FirewallDomainRedirectionAction
- **Type**: typing.Optional[typing.Literal['INSPECT_REDIRECTION_DOMAIN', 'TRUST_REDIRECTION_DOMAIN']]

### Qtype
- **Type**: typing.Optional[str]

### DnsThreatProtection
- **Type**: typing.Optional[typing.Literal['DGA', 'DNS_TUNNELING']]

### ConfidenceThreshold
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# UpdateFirewallRuleResponseTypeDef

### FirewallRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.FirewallRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIpAddressTypeDef

### IpId
- **Type**: <class 'str'>
- **Required**: Yes

### Ipv6
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateOutpostResolverRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### PreferredInstanceType
- **Type**: typing.Optional[str]


# UpdateOutpostResolverResponseTypeDef

### OutpostResolver
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.OutpostResolverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResolverConfigRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AutodefinedReverseFlag
- **Type**: typing.Literal['DISABLE', 'ENABLE', 'USE_LOCAL_RESOURCE_SETTING']
- **Required**: Yes


# UpdateResolverConfigResponseTypeDef

### ResolverConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResolverDnssecConfigRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Validation
- **Type**: typing.Literal['DISABLE', 'ENABLE', 'USE_LOCAL_RESOURCE_SETTING']
- **Required**: Yes


# UpdateResolverDnssecConfigResponseTypeDef

### ResolverDNSSECConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverDnssecConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResolverEndpointRequestTypeDef

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### ResolverEndpointType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]

### UpdateIpAddresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53resolver_classes.UpdateIpAddressTypeDef]]

### Protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Do53', 'DoH', 'DoH-FIPS']]]


# UpdateResolverEndpointResponseTypeDef

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResolverRuleRequestTypeDef

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Config
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleConfigTypeDef'>
- **Default**: <class 'aws_resource_validator.pydantic_models.base_validator_model.BaseValidatorModel.Config'>


# UpdateResolverRuleResponseTypeDef

### ResolverRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResolverRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


