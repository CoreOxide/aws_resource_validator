# Network Firewall Classes

# ActionDefinition

### PublishMetricAction
- **Type**: <class 'NoneType'>


# ActionDefinitionOutput

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PublishMetricActionOutput]


# Address

### AddressDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# AnalysisReport

### AnalysisReportId
- **Type**: typing.Optional[str]

### AnalysisType
- **Type**: typing.Optional[typing.Literal['HTTP_HOST', 'TLS_SNI']]

### ReportTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]


# AnalysisResult

### IdentifiedRuleIds
- **Type**: typing.Optional[typing.List[str]]

### IdentifiedType
- **Type**: typing.Optional[typing.Literal['STATELESS_RULE_CONTAINS_TCP_FLAGS', 'STATELESS_RULE_FORWARDING_ASYMMETRICALLY']]

### AnalysisDetail
- **Type**: typing.Optional[str]


# AnalysisTypeReportResult

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateFirewallPolicyRequest

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# AssociateFirewallPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateSubnetsRequest

### SubnetMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMapping]
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# AssociateSubnetsResponse

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMapping]
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# Attachment

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

# CIDRSummary

### AvailableCIDRCount
- **Type**: typing.Optional[int]

### UtilizedCIDRCount
- **Type**: typing.Optional[int]

### IPSetReferences
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetMetadata]]


# CapacityUsageSummary

### CIDRs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.CIDRSummary]


# CheckCertificateRevocationStatusActions

### RevokedStatusAction
- **Type**: typing.Optional[typing.Literal['DROP', 'PASS', 'REJECT']]

### UnknownStatusAction
- **Type**: typing.Optional[typing.Literal['DROP', 'PASS', 'REJECT']]


# CreateFirewallPolicyRequest

### FirewallPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyUnion'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Tag]]

### DryRun
- **Type**: typing.Optional[bool]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>


# CreateFirewallPolicyResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFirewallRequest

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: typing.Optional[str]

### SubnetMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMapping]]

### DeleteProtection
- **Type**: typing.Optional[bool]

### SubnetChangeProtection
- **Type**: typing.Optional[bool]

### FirewallPolicyChangeProtection
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Tag]]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### EnabledAnalysisTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HTTP_HOST', 'TLS_SNI']]]


# CreateFirewallResponse

### Firewall
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.Firewall'>
- **Required**: Yes

### FirewallStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleGroupResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTLSInspectionConfigurationRequest

### TLSInspectionConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationUnion'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Tag]]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>


# CreateTLSInspectionConfigurationResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# CustomAction

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ActionDefinition'>
- **Required**: Yes


# CustomActionOutput

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ActionDefinitionOutput'>
- **Required**: Yes


# DeleteFirewallPolicyRequest

### FirewallPolicyName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]


# DeleteFirewallPolicyResponse

### FirewallPolicyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFirewallRequest

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]


# DeleteFirewallResponse

### Firewall
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.Firewall'>
- **Required**: Yes

### FirewallStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleGroupResponse

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTLSInspectionConfigurationRequest

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### TLSInspectionConfigurationName
- **Type**: typing.Optional[str]


# DeleteTLSInspectionConfigurationResponse

### TLSInspectionConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFirewallPolicyRequest

### FirewallPolicyName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]


# DescribeFirewallPolicyResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyResponse'>
- **Required**: Yes

### FirewallPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFirewallRequest

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]


# DescribeFirewallResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### Firewall
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.Firewall'>
- **Required**: Yes

### FirewallStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoggingConfigurationRequest

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# DescribeLoggingConfigurationResponse

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourcePolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRuleGroupResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupOutput'>
- **Required**: Yes

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTLSInspectionConfigurationRequest

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### TLSInspectionConfigurationName
- **Type**: typing.Optional[str]


# DescribeTLSInspectionConfigurationResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationOutput'>
- **Required**: Yes

### TLSInspectionConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# Dimension

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateSubnetsRequest

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# DisassociateSubnetsResponse

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMapping]
- **Required**: Yes

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Firewall

### FirewallPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.SubnetMapping]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Tag]]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### EnabledAnalysisTypes
- **Type**: typing.Optional[typing.List[typing.Literal['HTTP_HOST', 'TLS_SNI']]]


# FirewallMetadata

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]


# FirewallPolicy

### StatelessDefaultActions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StatelessFragmentDefaultActions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRuleGroupReference]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.CustomAction]]

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleGroupReference]]

### StatefulDefaultActions
- **Type**: typing.Optional[typing.Sequence[str]]

### StatefulEngineOptions
- **Type**: <class 'NoneType'>

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### PolicyVariables
- **Type**: <class 'NoneType'>


# FirewallPolicyMetadata

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# FirewallPolicyOutput

### StatelessDefaultActions
- **Type**: typing.List[str]
- **Required**: Yes

### StatelessFragmentDefaultActions
- **Type**: typing.List[str]
- **Required**: Yes

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRuleGroupReference]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.CustomActionOutput]]

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleGroupReference]]

### StatefulDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatefulEngineOptions
- **Type**: <class 'NoneType'>

### TLSInspectionConfigurationArn
- **Type**: typing.Optional[str]

### PolicyVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PolicyVariablesOutput]


# FirewallPolicyResponse

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Tag]]

### ConsumedStatelessRuleCapacity
- **Type**: typing.Optional[int]

### ConsumedStatefulRuleCapacity
- **Type**: typing.Optional[int]

### NumberOfAssociations
- **Type**: typing.Optional[int]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# FirewallPolicyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FirewallStatus

### Status
- **Type**: typing.Literal['DELETING', 'PROVISIONING', 'READY']
- **Required**: Yes

### ConfigurationSyncStateSummary
- **Type**: typing.Literal['CAPACITY_CONSTRAINED', 'IN_SYNC', 'PENDING']
- **Required**: Yes

### SyncStates
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.SyncState]]

### CapacityUsageSummary
- **Type**: <class 'NoneType'>


# FlowTimeouts

### TcpIdleTimeoutSeconds
- **Type**: typing.Optional[int]


# GetAnalysisReportResultsRequest

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


# GetAnalysisReportResultsRequestPaginate

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfig]


# GetAnalysisReportResultsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AnalysisTypeReportResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Header

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Hits

### Count
- **Type**: typing.Optional[int]


# IPSet

### Definition
- **Type**: typing.Sequence[str]
- **Required**: Yes


# IPSetMetadata

### ResolvedCIDRCount
- **Type**: typing.Optional[int]


# IPSetOutput

### Definition
- **Type**: typing.List[str]
- **Required**: Yes


# IPSetReference

### ReferenceArn
- **Type**: typing.Optional[str]


# ListAnalysisReportsRequest

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAnalysisReportsRequestPaginate

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfig]


# ListAnalysisReportsResponse

### AnalysisReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.AnalysisReport]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallPoliciesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFirewallPoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfig]


# ListFirewallPoliciesResponse

### FirewallPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFirewallsRequest

### NextToken
- **Type**: typing.Optional[str]

### VpcIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]


# ListFirewallsRequestPaginate

### VpcIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfig]


# ListFirewallsResponse

### Firewalls
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.FirewallMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRuleGroupsResponse

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTLSInspectionConfigurationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTLSInspectionConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfig]


# ListTLSInspectionConfigurationsResponse

### TLSInspectionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogDestinationConfig

### LogType
- **Type**: typing.Literal['ALERT', 'FLOW', 'TLS']
- **Required**: Yes

### LogDestinationType
- **Type**: typing.Literal['CloudWatchLogs', 'KinesisDataFirehose', 'S3']
- **Required**: Yes

### LogDestination
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# LogDestinationConfigOutput

### LogType
- **Type**: typing.Literal['ALERT', 'FLOW', 'TLS']
- **Required**: Yes

### LogDestinationType
- **Type**: typing.Literal['CloudWatchLogs', 'KinesisDataFirehose', 'S3']
- **Required**: Yes

### LogDestination
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# LoggingConfiguration

### LogDestinationConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.LogDestinationConfig]
- **Required**: Yes


# LoggingConfigurationOutput

### LogDestinationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.LogDestinationConfigOutput]
- **Required**: Yes


# LoggingConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MatchAttributes

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Address]]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Address]]

### SourcePorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.PortRange]]

### DestinationPorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.PortRange]]

### Protocols
- **Type**: typing.Optional[typing.Sequence[int]]

### TCPFlags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.TCPFlagField]]


# MatchAttributesOutput

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Address]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Address]]

### SourcePorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.PortRange]]

### DestinationPorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.PortRange]]

### Protocols
- **Type**: typing.Optional[typing.List[int]]

### TCPFlags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TCPFlagFieldOutput]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerObjectStatus

### SyncStatus
- **Type**: typing.Optional[typing.Literal['CAPACITY_CONSTRAINED', 'IN_SYNC', 'PENDING']]

### UpdateToken
- **Type**: typing.Optional[str]


# PolicyVariables

### RuleVariables
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSet]]


# PolicyVariablesOutput

### RuleVariables
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetOutput]]


# PortRange

### FromPort
- **Type**: <class 'int'>
- **Required**: Yes

### ToPort
- **Type**: <class 'int'>
- **Required**: Yes


# PortSet

### Definition
- **Type**: typing.Optional[typing.Sequence[str]]


# PortSetOutput

### Definition
- **Type**: typing.Optional[typing.List[str]]


# PublishMetricAction

### Dimensions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Dimension]
- **Required**: Yes


# PublishMetricActionOutput

### Dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Dimension]
- **Required**: Yes


# PutResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# ReferenceSets

### IPSetReferences
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetReference]]


# ReferenceSetsOutput

### IPSetReferences
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetReference]]


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


# RuleDefinition

### MatchAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.MatchAttributes'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RuleDefinitionOutput

### MatchAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.MatchAttributesOutput'>
- **Required**: Yes

### Actions
- **Type**: typing.List[str]
- **Required**: Yes


# RuleGroup

### RulesSource
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RulesSource'>
- **Required**: Yes

### RuleVariables
- **Type**: <class 'NoneType'>

### ReferenceSets
- **Type**: <class 'NoneType'>

### StatefulRuleOptions
- **Type**: <class 'NoneType'>


# RuleGroupMetadata

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# RuleGroupOutput

### RulesSource
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RulesSourceOutput'>
- **Required**: Yes

### RuleVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RuleVariablesOutput]

### ReferenceSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.ReferenceSetsOutput]

### StatefulRuleOptions
- **Type**: <class 'NoneType'>


# RuleGroupResponse

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleOption

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleOptionOutput

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Optional[typing.List[str]]


# RuleVariables

### IPSets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSet]]

### PortSets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.network_firewall_classes.PortSet]]


# RuleVariablesOutput

### IPSets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.IPSetOutput]]

### PortSets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.PortSetOutput]]


# RulesSource

### RulesString
- **Type**: typing.Optional[str]

### RulesSourceList
- **Type**: <class 'NoneType'>

### StatefulRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRule]]

### StatelessRulesAndCustomActions
- **Type**: <class 'NoneType'>


# RulesSourceList

### Targets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TargetTypes
- **Type**: typing.Sequence[typing.Literal['HTTP_HOST', 'TLS_SNI']]
- **Required**: Yes

### GeneratedRulesType
- **Type**: typing.Literal['ALLOWLIST', 'DENYLIST']
- **Required**: Yes


# RulesSourceListOutput

### Targets
- **Type**: typing.List[str]
- **Required**: Yes

### TargetTypes
- **Type**: typing.List[typing.Literal['HTTP_HOST', 'TLS_SNI']]
- **Required**: Yes

### GeneratedRulesType
- **Type**: typing.Literal['ALLOWLIST', 'DENYLIST']
- **Required**: Yes


# RulesSourceOutput

### RulesString
- **Type**: typing.Optional[str]

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.RulesSourceListOutput]

### StatefulRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleOutput]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRulesAndCustomActionsOutput]


# ServerCertificate

### ResourceArn
- **Type**: typing.Optional[str]


# ServerCertificateConfiguration

### ServerCertificates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificate]]

### Scopes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateScope]]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CheckCertificateRevocationStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.CheckCertificateRevocationStatusActions]


# ServerCertificateConfigurationOutput

### ServerCertificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificate]]

### Scopes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateScopeOutput]]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CheckCertificateRevocationStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.CheckCertificateRevocationStatusActions]


# ServerCertificateScope

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Address]]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Address]]

### SourcePorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.PortRange]]

### DestinationPorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.PortRange]]

### Protocols
- **Type**: typing.Optional[typing.Sequence[int]]


# ServerCertificateScopeOutput

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Address]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Address]]

### SourcePorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.PortRange]]

### DestinationPorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.PortRange]]

### Protocols
- **Type**: typing.Optional[typing.List[int]]


# SourceMetadata

### SourceArn
- **Type**: typing.Optional[str]

### SourceUpdateToken
- **Type**: typing.Optional[str]


# StartAnalysisReportRequest

### AnalysisType
- **Type**: typing.Literal['HTTP_HOST', 'TLS_SNI']
- **Required**: Yes

### FirewallName
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]


# StartAnalysisReportResponse

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# StatefulEngineOptions

### RuleOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT_ACTION_ORDER', 'STRICT_ORDER']]

### StreamExceptionPolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP', 'REJECT']]

### FlowTimeouts
- **Type**: <class 'NoneType'>


# StatefulRule

### Action
- **Type**: typing.Literal['ALERT', 'DROP', 'PASS', 'REJECT']
- **Required**: Yes

### Header
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.Header'>
- **Required**: Yes

### RuleOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.RuleOption]
- **Required**: Yes


# StatefulRuleGroupOverride

### Action
- **Type**: typing.Optional[typing.Literal['DROP_TO_ALERT']]


# StatefulRuleGroupReference

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: typing.Optional[int]

### Override
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.StatefulRuleGroupOverride]


# StatefulRuleOptions

### RuleOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT_ACTION_ORDER', 'STRICT_ORDER']]


# StatefulRuleOutput

### Action
- **Type**: typing.Literal['ALERT', 'DROP', 'PASS', 'REJECT']
- **Required**: Yes

### Header
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.Header'>
- **Required**: Yes

### RuleOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.RuleOptionOutput]
- **Required**: Yes


# StatelessRule

### RuleDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleDefinition'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# StatelessRuleGroupReference

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# StatelessRuleOutput

### RuleDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleDefinitionOutput'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# StatelessRulesAndCustomActions

### StatelessRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRule]
- **Required**: Yes

### CustomActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.CustomAction]]


# StatelessRulesAndCustomActionsOutput

### StatelessRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.StatelessRuleOutput]
- **Required**: Yes

### CustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.CustomActionOutput]]


# SubnetMapping

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### IPAddressType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4', 'IPV6']]


# SyncState

### Attachment
- **Type**: <class 'NoneType'>

### Config
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.network_firewall_classes.PerObjectStatus]]


# TCPFlagField

### Flags
- **Type**: typing.Sequence[typing.Literal['ACK', 'CWR', 'ECE', 'FIN', 'PSH', 'RST', 'SYN', 'URG']]
- **Required**: Yes

### Masks
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACK', 'CWR', 'ECE', 'FIN', 'PSH', 'RST', 'SYN', 'URG']]]


# TCPFlagFieldOutput

### Flags
- **Type**: typing.List[typing.Literal['ACK', 'CWR', 'ECE', 'FIN', 'PSH', 'RST', 'SYN', 'URG']]
- **Required**: Yes

### Masks
- **Type**: typing.Optional[typing.List[typing.Literal['ACK', 'CWR', 'ECE', 'FIN', 'PSH', 'RST', 'SYN', 'URG']]]


# TLSInspectionConfiguration

### ServerCertificateConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateConfiguration]]


# TLSInspectionConfigurationMetadata

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# TLSInspectionConfigurationOutput

### ServerCertificateConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.ServerCertificateConfigurationOutput]]


# TLSInspectionConfigurationResponse

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.Tag]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### NumberOfAssociations
- **Type**: typing.Optional[int]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>

### Certificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.network_firewall_classes.TlsCertificateData]]

### CertificateAuthority
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.TlsCertificateData]


# TLSInspectionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.network_firewall_classes.Tag]
- **Required**: Yes


# TlsCertificateData

### CertificateArn
- **Type**: typing.Optional[str]

### CertificateSerial
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# UniqueSources

### Count
- **Type**: typing.Optional[int]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFirewallAnalysisSettingsRequest

### EnabledAnalysisTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HTTP_HOST', 'TLS_SNI']]]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### UpdateToken
- **Type**: typing.Optional[str]


# UpdateFirewallAnalysisSettingsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFirewallDeleteProtectionRequest

### DeleteProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# UpdateFirewallDeleteProtectionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFirewallDescriptionRequest

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateFirewallDescriptionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFirewallEncryptionConfigurationRequest

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### EncryptionConfiguration
- **Type**: <class 'NoneType'>


# UpdateFirewallEncryptionConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.EncryptionConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFirewallPolicyChangeProtectionRequest

### FirewallPolicyChangeProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# UpdateFirewallPolicyChangeProtectionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFirewallPolicyRequest

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyUnion'>
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
- **Type**: <class 'NoneType'>


# UpdateFirewallPolicyResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallPolicyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.FirewallPolicyResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLoggingConfigurationRequest

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationUnion]


# UpdateLoggingConfigurationResponse

### FirewallArn
- **Type**: <class 'str'>
- **Required**: Yes

### FirewallName
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRuleGroupResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.RuleGroupResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSubnetChangeProtectionRequest

### SubnetChangeProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### UpdateToken
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]


# UpdateSubnetChangeProtectionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTLSInspectionConfigurationRequest

### TLSInspectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationUnion'>
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
- **Type**: <class 'NoneType'>


# UpdateTLSInspectionConfigurationResponse

### UpdateToken
- **Type**: <class 'str'>
- **Required**: Yes

### TLSInspectionConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.TLSInspectionConfigurationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.network_firewall_classes.ResponseMetadata'>
- **Required**: Yes


