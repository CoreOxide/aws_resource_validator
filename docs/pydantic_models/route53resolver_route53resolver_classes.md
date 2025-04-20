# Route53Resolver Route53Resolver Classes

# AssociateFirewallRuleGroupRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]]


# AssociateFirewallRuleGroupResponse

### FirewallRuleGroupAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroupAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateResolverEndpointIpAddressRequest

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.IpAddressUpdate'>
- **Required**: Yes


# AssociateResolverEndpointIpAddressResponse

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateResolverQueryLogConfigRequest

### ResolverQueryLogConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateResolverQueryLogConfigResponse

### ResolverQueryLogConfigAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverQueryLogConfigAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateResolverRuleRequest

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AssociateResolverRuleResponse

### ResolverRuleAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRuleAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateFirewallDomainListRequest

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]]


# CreateFirewallDomainListResponse

### FirewallDomainList
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallDomainList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFirewallRuleGroupRequest

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]]


# CreateFirewallRuleGroupResponse

### FirewallRuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFirewallRuleRequest

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


# CreateFirewallRuleResponse

### FirewallRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOutpostResolverRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]]


# CreateOutpostResolverResponse

### OutpostResolver
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.OutpostResolver'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResolverEndpointRequest

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Direction
- **Type**: typing.Literal['INBOUND', 'OUTBOUND']
- **Required**: Yes

### IpAddresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.IpAddressRequest]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]

### PreferredInstanceType
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]]

### ResolverEndpointType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['Do53', 'DoH', 'DoH-FIPS']]]


# CreateResolverEndpointResponse

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResolverQueryLogConfigRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]]


# CreateResolverQueryLogConfigResponse

### ResolverQueryLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverQueryLogConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResolverRuleRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.TargetAddress]]

### ResolverEndpointId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]]


# CreateResolverRuleResponse

### ResolverRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFirewallDomainListRequest

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFirewallDomainListResponse

### FirewallDomainList
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallDomainList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFirewallRuleGroupRequest

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFirewallRuleGroupResponse

### FirewallRuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFirewallRuleRequest

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallDomainListId
- **Type**: typing.Optional[str]

### FirewallThreatProtectionId
- **Type**: typing.Optional[str]

### Qtype
- **Type**: typing.Optional[str]


# DeleteFirewallRuleResponse

### FirewallRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteOutpostResolverRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutpostResolverResponse

### OutpostResolver
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.OutpostResolver'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResolverEndpointRequest

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverEndpointResponse

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResolverQueryLogConfigRequest

### ResolverQueryLogConfigId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverQueryLogConfigResponse

### ResolverQueryLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverQueryLogConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResolverRuleRequest

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverRuleResponse

### ResolverRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateFirewallRuleGroupRequest

### FirewallRuleGroupAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFirewallRuleGroupResponse

### FirewallRuleGroupAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroupAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateResolverEndpointIpAddressRequest

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.IpAddressUpdate'>
- **Required**: Yes


# DisassociateResolverEndpointIpAddressResponse

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateResolverQueryLogConfigRequest

### ResolverQueryLogConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateResolverQueryLogConfigResponse

### ResolverQueryLogConfigAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverQueryLogConfigAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateResolverRuleRequest

### VPCId
- **Type**: <class 'str'>
- **Required**: Yes

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateResolverRuleResponse

### ResolverRuleAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRuleAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# Filter

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# FirewallConfig

### Id
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### FirewallFailOpen
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'USE_LOCAL_RESOURCE_SETTING']]


# FirewallDomainList

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


# FirewallDomainListMetadata

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


# FirewallRule

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


# FirewallRuleGroup

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


# FirewallRuleGroupAssociation

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


# FirewallRuleGroupMetadata

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


# GetFirewallConfigRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallConfigResponse

### FirewallConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetFirewallDomainListRequest

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallDomainListResponse

### FirewallDomainList
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallDomainList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetFirewallRuleGroupAssociationRequest

### FirewallRuleGroupAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallRuleGroupAssociationResponse

### FirewallRuleGroupAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroupAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetFirewallRuleGroupPolicyRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallRuleGroupPolicyResponse

### FirewallRuleGroupPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetFirewallRuleGroupRequest

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFirewallRuleGroupResponse

### FirewallRuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetOutpostResolverRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOutpostResolverResponse

### OutpostResolver
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.OutpostResolver'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverConfigRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverConfigResponse

### ResolverConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverDnssecConfigRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverDnssecConfigResponse

### ResolverDNSSECConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverDnssecConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverEndpointRequest

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverEndpointResponse

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverQueryLogConfigAssociationRequest

### ResolverQueryLogConfigAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverQueryLogConfigAssociationResponse

### ResolverQueryLogConfigAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverQueryLogConfigAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverQueryLogConfigPolicyRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverQueryLogConfigPolicyResponse

### ResolverQueryLogConfigPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverQueryLogConfigRequest

### ResolverQueryLogConfigId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverQueryLogConfigResponse

### ResolverQueryLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverQueryLogConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverRuleAssociationRequest

### ResolverRuleAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverRuleAssociationResponse

### ResolverRuleAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRuleAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverRulePolicyRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverRulePolicyResponse

### ResolverRulePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverRuleRequest

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverRuleResponse

### ResolverRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# ImportFirewallDomainsRequest

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['REPLACE']
- **Required**: Yes

### DomainFileUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ImportFirewallDomainsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# IpAddressRequest

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### Ip
- **Type**: typing.Optional[str]

### Ipv6
- **Type**: typing.Optional[str]


# IpAddressResponse

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


# IpAddressUpdate

### IpId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### Ip
- **Type**: typing.Optional[str]

### Ipv6
- **Type**: typing.Optional[str]


# ListFirewallConfigsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallConfigsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListFirewallConfigsResponse

### FirewallConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallDomainListsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallDomainListsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListFirewallDomainListsResponse

### FirewallDomainLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallDomainListMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallDomainsRequest

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallDomainsRequestPaginate

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListFirewallDomainsResponse

### Domains
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRuleGroupAssociationsRequest

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


# ListFirewallRuleGroupAssociationsRequestPaginate

### FirewallRuleGroupId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'DELETING', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListFirewallRuleGroupAssociationsResponse

### FirewallRuleGroupAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroupAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRuleGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRuleGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListFirewallRuleGroupsResponse

### FirewallRuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroupMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallRulesRequest

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


# ListFirewallRulesRequestPaginate

### FirewallRuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: typing.Optional[int]

### Action
- **Type**: typing.Optional[typing.Literal['ALERT', 'ALLOW', 'BLOCK']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListFirewallRulesResponse

### FirewallRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOutpostResolversRequest

### OutpostArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOutpostResolversRequestPaginate

### OutpostArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListOutpostResolversResponse

### OutpostResolvers
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.OutpostResolver]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverConfigsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResolverConfigsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListResolverConfigsResponse

### ResolverConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverDnssecConfigsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]


# ListResolverDnssecConfigsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListResolverDnssecConfigsResponse

### ResolverDnssecConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverDnssecConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverEndpointIpAddressesRequest

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResolverEndpointIpAddressesRequestPaginate

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListResolverEndpointIpAddressesResponse

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### IpAddresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.IpAddressResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverEndpointsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]


# ListResolverEndpointsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListResolverEndpointsResponse

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverEndpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverQueryLogConfigAssociationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListResolverQueryLogConfigAssociationsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListResolverQueryLogConfigAssociationsResponse

### TotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalFilteredCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverQueryLogConfigAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverQueryLogConfigAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverQueryLogConfigsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListResolverQueryLogConfigsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListResolverQueryLogConfigsResponse

### TotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalFilteredCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverQueryLogConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverQueryLogConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverRuleAssociationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]


# ListResolverRuleAssociationsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListResolverRuleAssociationsResponse

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverRuleAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRuleAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResolverRulesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]


# ListResolverRulesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListResolverRulesResponse

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResolverRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OutpostResolver

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutFirewallRuleGroupPolicyRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallRuleGroupPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutFirewallRuleGroupPolicyResponse

### ReturnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# PutResolverQueryLogConfigPolicyRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResolverQueryLogConfigPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResolverQueryLogConfigPolicyResponse

### ReturnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# PutResolverRulePolicyRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResolverRulePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResolverRulePolicyResponse

### ReturnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# ResolverConfig

### Id
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### AutodefinedReverse
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'UPDATING_TO_USE_LOCAL_RESOURCE_SETTING', 'USE_LOCAL_RESOURCE_SETTING']]


# ResolverDnssecConfig

### Id
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ValidationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING', 'UPDATING_TO_USE_LOCAL_RESOURCE_SETTING', 'USE_LOCAL_RESOURCE_SETTING']]


# ResolverEndpoint

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


# ResolverQueryLogConfig

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


# ResolverQueryLogConfigAssociation

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


# ResolverRule

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.TargetAddress]]

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


# ResolverRuleAssociation

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


# ResolverRuleConfig

### Name
- **Type**: typing.Optional[str]

### TargetIps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.TargetAddress]]

### ResolverEndpointId
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


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.Tag]
- **Required**: Yes


# TargetAddress

### Ip
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Ipv6
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[typing.Literal['Do53', 'DoH', 'DoH-FIPS']]

### ServerNameIndication
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateFirewallConfigRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallFailOpen
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'USE_LOCAL_RESOURCE_SETTING']
- **Required**: Yes


# UpdateFirewallConfigResponse

### FirewallConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFirewallDomainsRequest

### FirewallDomainListId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['ADD', 'REMOVE', 'REPLACE']
- **Required**: Yes

### Domains
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateFirewallDomainsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFirewallRuleGroupAssociationRequest

### FirewallRuleGroupAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: typing.Optional[int]

### MutationProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Name
- **Type**: typing.Optional[str]


# UpdateFirewallRuleGroupAssociationResponse

### FirewallRuleGroupAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRuleGroupAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFirewallRuleRequest

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


# UpdateFirewallRuleResponse

### FirewallRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.FirewallRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIpAddress

### IpId
- **Type**: <class 'str'>
- **Required**: Yes

### Ipv6
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateOutpostResolverRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### PreferredInstanceType
- **Type**: typing.Optional[str]


# UpdateOutpostResolverResponse

### OutpostResolver
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.OutpostResolver'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResolverConfigRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AutodefinedReverseFlag
- **Type**: typing.Literal['DISABLE', 'ENABLE', 'USE_LOCAL_RESOURCE_SETTING']
- **Required**: Yes


# UpdateResolverConfigResponse

### ResolverConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResolverDnssecConfigRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Validation
- **Type**: typing.Literal['DISABLE', 'ENABLE', 'USE_LOCAL_RESOURCE_SETTING']
- **Required**: Yes


# UpdateResolverDnssecConfigResponse

### ResolverDNSSECConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverDnssecConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResolverEndpointRequest

### ResolverEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### ResolverEndpointType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]

### UpdateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.UpdateIpAddress]]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['Do53', 'DoH', 'DoH-FIPS']]]


# UpdateResolverEndpointResponse

### ResolverEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResolverRuleRequest

### ResolverRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Config
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRuleConfig'>
- **Default**: <class 'aws_resource_validator.pydantic_models.base_validator_model.BaseValidatorModel.Config'>


# UpdateResolverRuleResponse

### ResolverRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResolverRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53resolver.route53resolver_classes.ResponseMetadata'>
- **Required**: Yes


