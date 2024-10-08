# Pydantic Models in network_firewall_classes

# ActionDefinitionTypeDef

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PublishMetricActionTypeDef]


# AddressTypeDef

### AddressDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# AnalysisResultTypeDef

### IdentifiedRuleIds
- **Type**: typing.Optional[typing.List[str]]

### IdentifiedType
- **Type**: typing.Optional[typing.Literal['STATELESS_RULE_CONTAINS_TCP_FLAGS', 'STATELESS_RULE_FORWARDING_ASYMMETRICALLY']]

### AnalysisDetail
- **Type**: typing.Optional[str]


# AssociateFirewallPolicyRequestRequestTypeDef

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# AssociateFirewallPolicyResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateSubnetsRequestRequestTypeDef

### SubnetMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMappingTypeDef]
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# AssociateSubnetsResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMappingTypeDef]
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachmentTypeDef

### SubnetId
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'ERROR', 'FAILED', 'READY', 'SCALING']]

### StatusMessage
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CIDRSummaryTypeDef

### AvailableCIDRCount
- **Type**: typing.Optional[int]

### UtilizedCIDRCount
- **Type**: typing.Optional[int]

### IPSetReferences
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetMetadataTypeDef]]


# CapacityUsageSummaryTypeDef

### CIDRs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.CIDRSummaryTypeDef]


# CheckCertificateRevocationStatusActionsTypeDef

### RevokedStatusAction
- **Type**: typing.Optional[typing.Literal['DROP', 'PASS', 'REJECT']]

### UnknownStatusAction
- **Type**: typing.Optional[typing.Literal['DROP', 'PASS', 'REJECT']]


# CreateFirewallPolicyRequestRequestTypeDef

### FirewallPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]]

### DryRun
- **Type**: typing.Optional[bool]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]


# CreateFirewallPolicyResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFirewallRequestRequestTypeDef

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMappingTypeDef]
- **Required**: Yes

### DeleteProtection
- **Type**: typing.Optional[bool]

### SubnetChangeProtection
- **Type**: typing.Optional[bool]

### FirewallPolicyChangeProtection
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]


# CreateFirewallResponseTypeDef

### Firewall
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallTypeDef'>
- **Required**: Yes

### FirewallStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleGroupRequestRequestTypeDef

### RuleGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['STATEFUL', 'STATELESS']
- **Required**: Yes

### Capacity
- **Type**: <class 'int'>
- **Required**: Yes

### RuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupTypeDef]

### Rules
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]]

### DryRun
- **Type**: typing.Optional[bool]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]

### SourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.SourceMetadataTypeDef]

### AnalyzeRuleGroup
- **Type**: typing.Optional[bool]


# CreateRuleGroupResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTLSInspectionConfigurationRequestRequestTypeDef

### TLSInspectionConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]


# CreateTLSInspectionConfigurationResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomActionTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ActionDefinitionTypeDef'>
- **Required**: Yes


# DeleteFirewallPolicyRequestRequestTypeDef

### FirewallPolicyName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]


# DeleteFirewallPolicyResponseTypeDef

### FirewallPolicyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFirewallRequestRequestTypeDef

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]


# DeleteFirewallResponseTypeDef

### Firewall
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallTypeDef'>
- **Required**: Yes

### FirewallStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleGroupRequestRequestTypeDef

### RuleGroupName
- **Type**: typing.Optional[str]

### RuleGroupArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['STATEFUL', 'STATELESS']]


# DeleteRuleGroupResponseTypeDef

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTLSInspectionConfigurationRequestRequestTypeDef

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### TLSInspectionConfigurationName
- **Type**: typing.Optional[str]


# DeleteTLSInspectionConfigurationResponseTypeDef

### TLSInspectionConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFirewallPolicyRequestRequestTypeDef

### FirewallPolicyName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]


# DescribeFirewallPolicyResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyResponseTypeDef'>
- **Required**: Yes

### FirewallPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFirewallRequestRequestTypeDef

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]


# DescribeFirewallResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### Firewall
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallTypeDef'>
- **Required**: Yes

### FirewallStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoggingConfigurationRequestRequestTypeDef

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# DescribeLoggingConfigurationResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourcePolicyRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourcePolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRuleGroupMetadataRequestRequestTypeDef

### RuleGroupName
- **Type**: typing.Optional[str]

### RuleGroupArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['STATEFUL', 'STATELESS']]


# DescribeRuleGroupMetadataResponseTypeDef

### RuleGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['STATEFUL', 'STATELESS']
- **Required**: Yes

### Capacity
- **Type**: <class 'int'>
- **Required**: Yes

### StatefulRuleOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleOptionsTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRuleGroupRequestRequestTypeDef

### RuleGroupName
- **Type**: typing.Optional[str]

### RuleGroupArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['STATEFUL', 'STATELESS']]

### AnalyzeRuleGroup
- **Type**: typing.Optional[bool]


# DescribeRuleGroupResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupTypeDef'>
- **Required**: Yes

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTLSInspectionConfigurationRequestRequestTypeDef

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### TLSInspectionConfigurationName
- **Type**: typing.Optional[str]


# DescribeTLSInspectionConfigurationResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationTypeDef'>
- **Required**: Yes

### TLSInspectionConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DimensionTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateSubnetsRequestRequestTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# DisassociateSubnetsResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMappingTypeDef]
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionConfigurationTypeDef

### Type
- **Type**: typing.Literal['AWS_OWNED_KMS_KEY', 'CUSTOMER_KMS']
- **Required**: Yes

### KeyId
- **Type**: typing.Optional[str]


# FirewallMetadataTypeDef

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]


# FirewallPolicyMetadataTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# FirewallPolicyResponseTypeDef

### FirewallPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### FirewallPolicyStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'ERROR']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]]

### ConsumedStatelessRuleCapacity
- **Type**: typing.Optional[int]

### ConsumedStatefulRuleCapacity
- **Type**: typing.Optional[int]

### NumberOfAssociations
- **Type**: typing.Optional[int]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# FirewallPolicyTypeDef

### StatelessDefaultActions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StatelessFragmentDefaultActions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRuleGroupReferenceTypeDef]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.CustomActionTypeDef]]

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleGroupReferenceTypeDef]]

### StatefulDefaultActions
- **Type**: typing.Optional[typing.Sequence[str]]

### StatefulEngineOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulEngineOptionsTypeDef]

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### PolicyVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PolicyVariablesTypeDef]


# FirewallStatusTypeDef

### Status
- **Type**: typing.Literal['DELETING', 'PROVISIONING', 'READY']
- **Required**: Yes

### ConfigurationSyncStateSummary
- **Type**: typing.Literal['CAPACITY_CONSTRAINED', 'IN_SYNC', 'PENDING']
- **Required**: Yes

### SyncStates
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.SyncStateTypeDef]]

### CapacityUsageSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.CapacityUsageSummaryTypeDef]


# FirewallTypeDef

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMappingTypeDef]
- **Required**: Yes

### FirewallId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### DeleteProtection
- **Type**: typing.Optional[bool]

### SubnetChangeProtection
- **Type**: typing.Optional[bool]

### FirewallPolicyChangeProtection
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]


# HeaderTypeDef

### Protocol
- **Type**: typing.Literal['DCERPC', 'DHCP', 'DNS', 'FTP', 'HTTP', 'ICMP', 'IKEV2', 'IMAP', 'IP', 'KRB5', 'MSN', 'NTP', 'SMB', 'SMTP', 'SSH', 'TCP', 'TFTP', 'TLS', 'UDP']
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### SourcePort
- **Type**: <class 'str'>
- **Required**: Yes

### Direction
- **Type**: typing.Literal['ANY', 'FORWARD']
- **Required**: Yes

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPort
- **Type**: <class 'str'>
- **Required**: Yes


# IPSetMetadataTypeDef

### ResolvedCIDRCount
- **Type**: typing.Optional[int]


# IPSetReferenceTypeDef

### ReferenceArn
- **Type**: typing.Optional[str]


# IPSetTypeDef

### Definition
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ListFirewallPoliciesRequestListFirewallPoliciesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListFirewallPoliciesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFirewallPoliciesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFirewallsRequestListFirewallsPaginateTypeDef

### VpcIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListFirewallsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### VpcIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]


# ListFirewallsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Firewalls
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.FirewallMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRuleGroupsRequestListRuleGroupsPaginateTypeDef

### Scope
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'MANAGED']]

### ManagedType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED_DOMAIN_LISTS', 'AWS_MANAGED_THREAT_SIGNATURES']]

### Type
- **Type**: typing.Optional[typing.Literal['STATEFUL', 'STATELESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListRuleGroupsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Scope
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'MANAGED']]

### ManagedType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED_DOMAIN_LISTS', 'AWS_MANAGED_THREAT_SIGNATURES']]

### Type
- **Type**: typing.Optional[typing.Literal['STATEFUL', 'STATELESS']]


# ListRuleGroupsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTLSInspectionConfigurationsRequestListTLSInspectionConfigurationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListTLSInspectionConfigurationsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTLSInspectionConfigurationsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogDestinationConfigTypeDef

### LogType
- **Type**: typing.Literal['ALERT', 'FLOW']
- **Required**: Yes

### LogDestinationType
- **Type**: typing.Literal['CloudWatchLogs', 'KinesisDataFirehose', 'S3']
- **Required**: Yes

### LogDestination
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# LoggingConfigurationTypeDef

### LogDestinationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.LogDestinationConfigTypeDef]
- **Required**: Yes


# MatchAttributesTypeDef

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.AddressTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.AddressTypeDef]]

### SourcePorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.PortRangeTypeDef]]

### DestinationPorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.PortRangeTypeDef]]

### Protocols
- **Type**: typing.Optional[typing.Sequence[int]]

### TCPFlags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.TCPFlagFieldTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerObjectStatusTypeDef

### SyncStatus
- **Type**: typing.Optional[typing.Literal['CAPACITY_CONSTRAINED', 'IN_SYNC', 'PENDING']]

### UpdateToken
- **Type**: typing.Optional[str]


# PolicyVariablesTypeDef

### RuleVariables
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetTypeDef]]


# PortRangeTypeDef

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes


# PortSetTypeDef

### Definition
- **Type**: typing.Optional[typing.Sequence[str]]


# PublishMetricActionTypeDef

### Dimensions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.DimensionTypeDef]
- **Required**: Yes


# PutResourcePolicyRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# ReferenceSetsTypeDef

### IPSetReferences
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetReferenceTypeDef]]


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


# RuleDefinitionTypeDef

### MatchAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.MatchAttributesTypeDef'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RuleGroupMetadataTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# RuleGroupResponseTypeDef

### RuleGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['STATEFUL', 'STATELESS']]

### Capacity
- **Type**: typing.Optional[int]

### RuleGroupStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'ERROR']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]]

### ConsumedCapacity
- **Type**: typing.Optional[int]

### NumberOfAssociations
- **Type**: typing.Optional[int]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]

### SourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.SourceMetadataTypeDef]

### SnsTopic
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### AnalysisResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AnalysisResultTypeDef]]


# RuleGroupTypeDef

### RulesSource
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RulesSourceTypeDef'>
- **Required**: Yes

### RuleVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RuleVariablesTypeDef]

### ReferenceSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.ReferenceSetsTypeDef]

### StatefulRuleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleOptionsTypeDef]


# RuleOptionTypeDef

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleVariablesTypeDef

### IPSets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetTypeDef]]

### PortSets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.PortSetTypeDef]]


# RulesSourceListTypeDef

### Targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TargetTypes
- **Type**: typing.Sequence[typing.Literal['HTTP_HOST', 'TLS_SNI']]
- **Required**: Yes

### GeneratedRulesType
- **Type**: typing.Literal['ALLOWLIST', 'DENYLIST']
- **Required**: Yes


# RulesSourceTypeDef

### RulesString
- **Type**: typing.Optional[str]

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RulesSourceListTypeDef]

### StatefulRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleTypeDef]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRulesAndCustomActionsTypeDef]


# ServerCertificateConfigurationTypeDef

### ServerCertificates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateTypeDef]]

### Scopes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateScopeTypeDef]]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CheckCertificateRevocationStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.CheckCertificateRevocationStatusActionsTypeDef]


# ServerCertificateScopeTypeDef

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.AddressTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.AddressTypeDef]]

### SourcePorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.PortRangeTypeDef]]

### DestinationPorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.PortRangeTypeDef]]

### Protocols
- **Type**: typing.Optional[typing.Sequence[int]]


# ServerCertificateTypeDef

### ResourceArn
- **Type**: typing.Optional[str]


# SourceMetadataTypeDef

### SourceArn
- **Type**: typing.Optional[str]

### SourceUpdateToken
- **Type**: typing.Optional[str]


# StatefulEngineOptionsTypeDef

### RuleOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT_ACTION_ORDER', 'STRICT_ORDER']]

### StreamExceptionPolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP', 'REJECT']]


# StatefulRuleGroupOverrideTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DROP_TO_ALERT']]


# StatefulRuleGroupReferenceTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: typing.Optional[int]

### Override
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleGroupOverrideTypeDef]


# StatefulRuleOptionsTypeDef

### RuleOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT_ACTION_ORDER', 'STRICT_ORDER']]


# StatefulRuleTypeDef

### Action
- **Type**: typing.Literal['ALERT', 'DROP', 'PASS', 'REJECT']
- **Required**: Yes

### Header
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.HeaderTypeDef'>
- **Required**: Yes

### RuleOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.RuleOptionTypeDef]
- **Required**: Yes


# StatelessRuleGroupReferenceTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# StatelessRuleTypeDef

### RuleDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleDefinitionTypeDef'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# StatelessRulesAndCustomActionsTypeDef

### StatelessRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRuleTypeDef]
- **Required**: Yes

### CustomActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.CustomActionTypeDef]]


# SubnetMappingTypeDef

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### IPAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]


# SyncStateTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.AttachmentTypeDef]

### Config
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.PerObjectStatusTypeDef]]


# TCPFlagFieldTypeDef

### Flags
- **Type**: typing.Sequence[typing.Literal['ACK', 'CWR', 'ECE', 'FIN', 'PSH', 'RST', 'SYN', 'URG']]
- **Required**: Yes

### Masks
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACK', 'CWR', 'ECE', 'FIN', 'PSH', 'RST', 'SYN', 'URG']]]


# TLSInspectionConfigurationMetadataTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# TLSInspectionConfigurationResponseTypeDef

### TLSInspectionConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurationStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'ERROR']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### NumberOfAssociations
- **Type**: typing.Optional[int]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]

### Certificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TlsCertificateDataTypeDef]]

### CertificateAuthority
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.TlsCertificateDataTypeDef]


# TLSInspectionConfigurationTypeDef

### ServerCertificateConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateConfigurationTypeDef]]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TlsCertificateDataTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### CertificateSerial
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFirewallDeleteProtectionRequestRequestTypeDef

### DeleteProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# UpdateFirewallDeleteProtectionResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFirewallDescriptionRequestRequestTypeDef

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateFirewallDescriptionResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFirewallEncryptionConfigurationRequestRequestTypeDef

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]


# UpdateFirewallEncryptionConfigurationResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFirewallPolicyChangeProtectionRequestRequestTypeDef

### FirewallPolicyChangeProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# UpdateFirewallPolicyChangeProtectionResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyChangeProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFirewallPolicyRequestRequestTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyTypeDef'>
- **Required**: Yes

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DryRun
- **Type**: typing.Optional[bool]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]


# UpdateFirewallPolicyResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLoggingConfigurationRequestRequestTypeDef

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationTypeDef]


# UpdateLoggingConfigurationResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRuleGroupRequestRequestTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupArn
- **Type**: typing.Optional[str]

### RuleGroupName
- **Type**: typing.Optional[str]

### RuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupTypeDef]

### Rules
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['STATEFUL', 'STATELESS']]

### Description
- **Type**: typing.Optional[str]

### DryRun
- **Type**: typing.Optional[bool]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]

### SourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.SourceMetadataTypeDef]

### AnalyzeRuleGroup
- **Type**: typing.Optional[bool]


# UpdateRuleGroupResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSubnetChangeProtectionRequestRequestTypeDef

### SubnetChangeProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# UpdateSubnetChangeProtectionResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetChangeProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTLSInspectionConfigurationRequestRequestTypeDef

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationTypeDef'>
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### TLSInspectionConfigurationName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfigurationTypeDef]


# UpdateTLSInspectionConfigurationResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


