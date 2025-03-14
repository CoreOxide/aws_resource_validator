# Network Firewall Classes

# ActionDefinitionOutputTypeDef

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PublishMetricActionOutputTypeDef]


# ActionDefinitionTypeDef

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PublishMetricActionTypeDef]


# AddressTypeDef

### AddressDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# AnalysisReportTypeDef

### AnalysisReportId
- **Type**: typing.Optional[str]

### AnalysisType
- **Type**: typing.Optional[typing.Literal['HTTP_HOST', 'TLS_SNI']]

### ReportTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]


# AnalysisResultTypeDef

### IdentifiedRuleIds
- **Type**: typing.Optional[typing.List[str]]

### IdentifiedType
- **Type**: typing.Optional[typing.Literal['STATELESS_RULE_CONTAINS_TCP_FLAGS', 'STATELESS_RULE_FORWARDING_ASYMMETRICALLY']]

### AnalysisDetail
- **Type**: typing.Optional[str]


# AnalysisTypeReportResultTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateFirewallPolicyRequestTypeDef

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


# AssociateSubnetsRequestTypeDef

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


# CreateFirewallPolicyRequestTypeDef

### FirewallPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyUnionTypeDef'>
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


# CreateFirewallRequestTypeDef

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: typing.Optional[str]

### SubnetMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMappingTypeDef]]

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

### EnabledAnalysisTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HTTP_HOST', 'TLS_SNI']]]


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


# CreateTLSInspectionConfigurationRequestTypeDef

### TLSInspectionConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationUnionTypeDef'>
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


# CustomActionOutputTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ActionDefinitionOutputTypeDef'>
- **Required**: Yes


# CustomActionTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ActionDefinitionTypeDef'>
- **Required**: Yes


# DeleteFirewallPolicyRequestTypeDef

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


# DeleteFirewallRequestTypeDef

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


# DeleteResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleGroupResponseTypeDef

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTLSInspectionConfigurationRequestTypeDef

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


# DescribeFirewallPolicyRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFirewallRequestTypeDef

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


# DescribeLoggingConfigurationRequestTypeDef

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# DescribeLoggingConfigurationResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourcePolicyRequestTypeDef

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


# DescribeRuleGroupResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupOutputTypeDef'>
- **Required**: Yes

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTLSInspectionConfigurationRequestTypeDef

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### TLSInspectionConfigurationName
- **Type**: typing.Optional[str]


# DescribeTLSInspectionConfigurationResponseTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationOutputTypeDef'>
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


# DisassociateSubnetsRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# FirewallPolicyOutputTypeDef

### StatelessDefaultActions
- **Type**: typing.List[str]
- **Required**: Yes

### StatelessFragmentDefaultActions
- **Type**: typing.List[str]
- **Required**: Yes

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRuleGroupReferenceTypeDef]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.CustomActionOutputTypeDef]]

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleGroupReferenceTypeDef]]

### StatefulDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatefulEngineOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulEngineOptionsTypeDef]

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### PolicyVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PolicyVariablesOutputTypeDef]


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


# FirewallPolicyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### EnabledAnalysisTypes
- **Type**: typing.Optional[typing.List[typing.Literal['HTTP_HOST', 'TLS_SNI']]]


# FlowTimeoutsTypeDef

### TcpIdleTimeoutSeconds
- **Type**: typing.Optional[int]


# GetAnalysisReportResultsRequestPaginateTypeDef

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# GetAnalysisReportResultsRequestTypeDef

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetAnalysisReportResultsResponseTypeDef

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReportTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AnalysisType
- **Type**: typing.Literal['HTTP_HOST', 'TLS_SNI']
- **Required**: Yes

### AnalysisReportResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AnalysisTypeReportResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# HeaderTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HitsTypeDef

### Count
- **Type**: typing.Optional[int]


# IPSetMetadataTypeDef

### ResolvedCIDRCount
- **Type**: typing.Optional[int]


# IPSetOutputTypeDef

### Definition
- **Type**: typing.List[str]
- **Required**: Yes


# IPSetReferenceTypeDef

### ReferenceArn
- **Type**: typing.Optional[str]


# IPSetTypeDef

### Definition
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ListAnalysisReportsRequestPaginateTypeDef

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListAnalysisReportsRequestTypeDef

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAnalysisReportsResponseTypeDef

### AnalysisReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AnalysisReportTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallPoliciesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListFirewallPoliciesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFirewallPoliciesResponseTypeDef

### FirewallPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallsRequestPaginateTypeDef

### VpcIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListFirewallsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### VpcIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]


# ListFirewallsResponseTypeDef

### Firewalls
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.FirewallMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRuleGroupsResponseTypeDef

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTLSInspectionConfigurationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListTLSInspectionConfigurationsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTLSInspectionConfigurationsResponseTypeDef

### TLSInspectionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogDestinationConfigOutputTypeDef

### LogType
- **Type**: typing.Literal['ALERT', 'FLOW', 'TLS']
- **Required**: Yes

### LogDestinationType
- **Type**: typing.Literal['CloudWatchLogs', 'KinesisDataFirehose', 'S3']
- **Required**: Yes

### LogDestination
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# LogDestinationConfigTypeDef

### LogType
- **Type**: typing.Literal['ALERT', 'FLOW', 'TLS']
- **Required**: Yes

### LogDestinationType
- **Type**: typing.Literal['CloudWatchLogs', 'KinesisDataFirehose', 'S3']
- **Required**: Yes

### LogDestination
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# LoggingConfigurationOutputTypeDef

### LogDestinationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.LogDestinationConfigOutputTypeDef]
- **Required**: Yes


# LoggingConfigurationTypeDef

### LogDestinationConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.LogDestinationConfigTypeDef]
- **Required**: Yes


# LoggingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MatchAttributesOutputTypeDef

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AddressTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AddressTypeDef]]

### SourcePorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.PortRangeTypeDef]]

### DestinationPorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.PortRangeTypeDef]]

### Protocols
- **Type**: typing.Optional[typing.List[int]]

### TCPFlags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TCPFlagFieldOutputTypeDef]]


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


# PolicyVariablesOutputTypeDef

### RuleVariables
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetOutputTypeDef]]


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


# PortSetOutputTypeDef

### Definition
- **Type**: typing.Optional[typing.List[str]]


# PortSetTypeDef

### Definition
- **Type**: typing.Optional[typing.Sequence[str]]


# PublishMetricActionOutputTypeDef

### Dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.DimensionTypeDef]
- **Required**: Yes


# PublishMetricActionTypeDef

### Dimensions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.DimensionTypeDef]
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# ReferenceSetsOutputTypeDef

### IPSetReferences
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetReferenceTypeDef]]


# ReferenceSetsTypeDef

### IPSetReferences
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetReferenceTypeDef]]


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


# RuleDefinitionOutputTypeDef

### MatchAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.MatchAttributesOutputTypeDef'>
- **Required**: Yes

### Actions
- **Type**: typing.List[str]
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


# RuleGroupOutputTypeDef

### RulesSource
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RulesSourceOutputTypeDef'>
- **Required**: Yes

### RuleVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RuleVariablesOutputTypeDef]

### ReferenceSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.ReferenceSetsOutputTypeDef]

### StatefulRuleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleOptionsTypeDef]


# RuleGroupResponseTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RuleOptionOutputTypeDef

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Optional[typing.List[str]]


# RuleOptionTypeDef

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleVariablesOutputTypeDef

### IPSets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetOutputTypeDef]]

### PortSets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.PortSetOutputTypeDef]]


# RuleVariablesTypeDef

### IPSets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetTypeDef]]

### PortSets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.PortSetTypeDef]]


# RulesSourceListOutputTypeDef

### Targets
- **Type**: typing.List[str]
- **Required**: Yes

### TargetTypes
- **Type**: typing.List[typing.Literal['HTTP_HOST', 'TLS_SNI']]
- **Required**: Yes

### GeneratedRulesType
- **Type**: typing.Literal['ALLOWLIST', 'DENYLIST']
- **Required**: Yes


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


# RulesSourceOutputTypeDef

### RulesString
- **Type**: typing.Optional[str]

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RulesSourceListOutputTypeDef]

### StatefulRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleOutputTypeDef]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRulesAndCustomActionsOutputTypeDef]


# RulesSourceTypeDef

### RulesString
- **Type**: typing.Optional[str]

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RulesSourceListTypeDef]

### StatefulRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleTypeDef]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRulesAndCustomActionsTypeDef]


# ServerCertificateConfigurationOutputTypeDef

### ServerCertificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateTypeDef]]

### Scopes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateScopeOutputTypeDef]]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CheckCertificateRevocationStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.CheckCertificateRevocationStatusActionsTypeDef]


# ServerCertificateConfigurationTypeDef

### ServerCertificates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateTypeDef]]

### Scopes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateScopeTypeDef]]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CheckCertificateRevocationStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.CheckCertificateRevocationStatusActionsTypeDef]


# ServerCertificateScopeOutputTypeDef

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AddressTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AddressTypeDef]]

### SourcePorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.PortRangeTypeDef]]

### DestinationPorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.PortRangeTypeDef]]

### Protocols
- **Type**: typing.Optional[typing.List[int]]


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


# StartAnalysisReportRequestTypeDef

### AnalysisType
- **Type**: typing.Literal['HTTP_HOST', 'TLS_SNI']
- **Required**: Yes

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]


# StartAnalysisReportResponseTypeDef

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatefulEngineOptionsTypeDef

### RuleOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT_ACTION_ORDER', 'STRICT_ORDER']]

### StreamExceptionPolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP', 'REJECT']]

### FlowTimeouts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.FlowTimeoutsTypeDef]


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


# StatefulRuleOutputTypeDef

### Action
- **Type**: typing.Literal['ALERT', 'DROP', 'PASS', 'REJECT']
- **Required**: Yes

### Header
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.HeaderTypeDef'>
- **Required**: Yes

### RuleOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.RuleOptionOutputTypeDef]
- **Required**: Yes


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


# StatelessRuleOutputTypeDef

### RuleDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleDefinitionOutputTypeDef'>
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


# StatelessRulesAndCustomActionsOutputTypeDef

### StatelessRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRuleOutputTypeDef]
- **Required**: Yes

### CustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.CustomActionOutputTypeDef]]


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


# TCPFlagFieldOutputTypeDef

### Flags
- **Type**: typing.List[typing.Literal['ACK', 'CWR', 'ECE', 'FIN', 'PSH', 'RST', 'SYN', 'URG']]
- **Required**: Yes

### Masks
- **Type**: typing.Optional[typing.List[typing.Literal['ACK', 'CWR', 'ECE', 'FIN', 'PSH', 'RST', 'SYN', 'URG']]]


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


# TLSInspectionConfigurationOutputTypeDef

### ServerCertificateConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateConfigurationOutputTypeDef]]


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


# TLSInspectionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

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


# UniqueSourcesTypeDef

### Count
- **Type**: typing.Optional[int]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFirewallAnalysisSettingsRequestTypeDef

### EnabledAnalysisTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HTTP_HOST', 'TLS_SNI']]]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### UpdateToken
- **Type**: typing.Optional[str]


# UpdateFirewallAnalysisSettingsResponseTypeDef

### EnabledAnalysisTypes
- **Type**: typing.List[typing.Literal['HTTP_HOST', 'TLS_SNI']]
- **Required**: Yes

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFirewallDeleteProtectionRequestTypeDef

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


# UpdateFirewallDescriptionRequestTypeDef

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


# UpdateFirewallEncryptionConfigurationRequestTypeDef

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


# UpdateFirewallPolicyChangeProtectionRequestTypeDef

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


# UpdateFirewallPolicyRequestTypeDef

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyUnionTypeDef'>
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


# UpdateLoggingConfigurationRequestTypeDef

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationUnionTypeDef]


# UpdateLoggingConfigurationResponseTypeDef

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# UpdateSubnetChangeProtectionRequestTypeDef

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


# UpdateTLSInspectionConfigurationRequestTypeDef

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationUnionTypeDef'>
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


