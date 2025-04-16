# Fms Classes

# AccountScope

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### AllAccountsEnabled
- **Type**: typing.Optional[bool]

### ExcludeSpecifiedAccounts
- **Type**: typing.Optional[bool]


# AccountScopeOutput

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### AllAccountsEnabled
- **Type**: typing.Optional[bool]

### ExcludeSpecifiedAccounts
- **Type**: typing.Optional[bool]


# ActionTarget

### ResourceId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AdminAccountSummary

### AdminAccount
- **Type**: typing.Optional[str]

### DefaultAdmin
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['OFFBOARDING', 'OFFBOARDING_COMPLETE', 'ONBOARDING', 'ONBOARDING_COMPLETE']]


# AdminScope

### AccountScope
- **Type**: <class 'NoneType'>

### OrganizationalUnitScope
- **Type**: <class 'NoneType'>

### RegionScope
- **Type**: <class 'NoneType'>

### PolicyTypeScope
- **Type**: <class 'NoneType'>


# AdminScopeOutput

### AccountScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.AccountScopeOutput]

### OrganizationalUnitScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.OrganizationalUnitScopeOutput]

### RegionScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.RegionScopeOutput]

### PolicyTypeScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PolicyTypeScopeOutput]


# AdminScopeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# App

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppsListData

### ListName
- **Type**: <class 'str'>
- **Required**: Yes

### AppsList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.App]
- **Required**: Yes

### ListId
- **Type**: typing.Optional[str]

### ListUpdateToken
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.Timestamp]

### LastUpdateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.Timestamp]

### PreviousAppsList
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.App]]]


# AppsListDataOutput

### ListName
- **Type**: <class 'str'>
- **Required**: Yes

### AppsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.App]
- **Required**: Yes

### ListId
- **Type**: typing.Optional[str]

### ListUpdateToken
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### PreviousAppsList
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.fms_classes.App]]]


# AppsListDataSummary

### ListArn
- **Type**: typing.Optional[str]

### ListId
- **Type**: typing.Optional[str]

### ListName
- **Type**: typing.Optional[str]

### AppsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.App]]


# AppsListDataUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateAdminAccountRequest

### AdminAccount
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateThirdPartyFirewallRequest

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes


# AssociateThirdPartyFirewallResponse

### ThirdPartyFirewallStatus
- **Type**: typing.Literal['NOT_EXIST', 'OFFBOARDING', 'OFFBOARD_COMPLETE', 'ONBOARDING', 'ONBOARD_COMPLETE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# AwsEc2InstanceViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### AwsEc2NetworkInterfaceViolations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.AwsEc2NetworkInterfaceViolation]]


# AwsEc2NetworkInterfaceViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolatingSecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# AwsVPCSecurityGroupViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolationTargetDescription
- **Type**: typing.Optional[str]

### PartialMatches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.PartialMatch]]

### PossibleSecurityGroupRemediationActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.SecurityGroupRemediationAction]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateResourceRequest

### ResourceSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchAssociateResourceResponse

### ResourceSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### FailedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.FailedItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateResourceRequest

### ResourceSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDisassociateResourceResponse

### ResourceSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### FailedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.FailedItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# ComplianceViolator

### ResourceId
- **Type**: typing.Optional[str]

### ViolationReason
- **Type**: typing.Optional[typing.Literal['BLACK_HOLE_ROUTE_DETECTED', 'BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET', 'FIREWALL_SUBNET_IS_OUT_OF_SCOPE', 'FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE', 'FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT', 'FMS_CREATED_SECURITY_GROUP_EDITED', 'INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE', 'INTERNET_TRAFFIC_NOT_INSPECTED', 'INVALID_NETWORK_ACL_ENTRY', 'INVALID_ROUTE_CONFIGURATION', 'MISSING_EXPECTED_ROUTE_TABLE', 'MISSING_FIREWALL', 'MISSING_FIREWALL_SUBNET_IN_AZ', 'MISSING_TARGET_GATEWAY', 'NETWORK_FIREWALL_POLICY_MODIFIED', 'RESOURCE_INCORRECT_WEB_ACL', 'RESOURCE_MISSING_DNS_FIREWALL', 'RESOURCE_MISSING_SECURITY_GROUP', 'RESOURCE_MISSING_SHIELD_PROTECTION', 'RESOURCE_MISSING_WEB_ACL', 'RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION', 'RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP', 'ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT', 'SECURITY_GROUP_REDUNDANT', 'SECURITY_GROUP_UNUSED', 'TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY', 'UNEXPECTED_FIREWALL_ROUTES', 'UNEXPECTED_TARGET_GATEWAY_ROUTES', 'WEB_ACL_CONFIGURATION_OR_SCOPE_OF_USE', 'WEB_ACL_MISSING_RULE_GROUP']]

### ResourceType
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNetworkAclAction

### Description
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]

### FMSCanRemediate
- **Type**: typing.Optional[bool]


# CreateNetworkAclEntriesAction

### Description
- **Type**: typing.Optional[str]

### NetworkAclId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]

### NetworkAclEntriesToBeCreated
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EntryDescription]]

### FMSCanRemediate
- **Type**: typing.Optional[bool]


# DeleteAppsListRequest

### ListId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkAclEntriesAction

### Description
- **Type**: typing.Optional[str]

### NetworkAclId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]

### NetworkAclEntriesToBeDeleted
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EntryDescription]]

### FMSCanRemediate
- **Type**: typing.Optional[bool]


# DeletePolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteAllPolicyResources
- **Type**: typing.Optional[bool]


# DeleteProtocolsListRequest

### ListId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceSetRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateThirdPartyFirewallRequest

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes


# DisassociateThirdPartyFirewallResponse

### ThirdPartyFirewallStatus
- **Type**: typing.Literal['NOT_EXIST', 'OFFBOARDING', 'OFFBOARD_COMPLETE', 'ONBOARDING', 'ONBOARD_COMPLETE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# DiscoveredResource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DnsDuplicateRuleGroupViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolationTargetDescription
- **Type**: typing.Optional[str]


# DnsRuleGroupLimitExceededViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolationTargetDescription
- **Type**: typing.Optional[str]

### NumberOfRuleGroupsAlreadyAssociated
- **Type**: typing.Optional[int]


# DnsRuleGroupPriorityConflictViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolationTargetDescription
- **Type**: typing.Optional[str]

### ConflictingPriority
- **Type**: typing.Optional[int]

### ConflictingPolicyId
- **Type**: typing.Optional[str]

### UnavailablePriorities
- **Type**: typing.Optional[typing.List[int]]


# EC2AssociateRouteTableAction

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]

### GatewayId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]


# EC2CopyRouteTableAction

### VpcId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# EC2CreateRouteAction

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### DestinationPrefixListId
- **Type**: typing.Optional[str]

### DestinationIpv6CidrBlock
- **Type**: typing.Optional[str]

### VpcEndpointId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]

### GatewayId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]


# EC2CreateRouteTableAction

### VpcId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# EC2DeleteRouteAction

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### DestinationPrefixListId
- **Type**: typing.Optional[str]

### DestinationIpv6CidrBlock
- **Type**: typing.Optional[str]


# EC2ReplaceRouteAction

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### DestinationPrefixListId
- **Type**: typing.Optional[str]

### DestinationIpv6CidrBlock
- **Type**: typing.Optional[str]

### GatewayId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]


# EC2ReplaceRouteTableAssociationAction

### AssociationId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTarget'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# EntryDescription

### EntryDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntry]

### EntryRuleNumber
- **Type**: typing.Optional[int]

### EntryType
- **Type**: typing.Optional[typing.Literal['CUSTOM_ENTRY', 'FMS_MANAGED_FIRST_ENTRY', 'FMS_MANAGED_LAST_ENTRY']]


# EntryViolation

### ExpectedEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EntryDescription]

### ExpectedEvaluationOrder
- **Type**: typing.Optional[str]

### ActualEvaluationOrder
- **Type**: typing.Optional[str]

### EntryAtExpectedEvaluationOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EntryDescription]

### EntriesWithConflicts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EntryDescription]]

### EntryViolationReasons
- **Type**: typing.Optional[typing.List[typing.Literal['ENTRY_CONFLICT', 'INCORRECT_ENTRY_ORDER', 'MISSING_EXPECTED_ENTRY']]]


# EvaluationResult

### ComplianceStatus
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'NON_COMPLIANT']]

### ViolatorCount
- **Type**: typing.Optional[int]

### EvaluationLimitExceeded
- **Type**: typing.Optional[bool]


# ExpectedRoute

### IpV4Cidr
- **Type**: typing.Optional[str]

### PrefixListId
- **Type**: typing.Optional[str]

### IpV6Cidr
- **Type**: typing.Optional[str]

### ContributingSubnets
- **Type**: typing.Optional[typing.List[str]]

### AllowedTargets
- **Type**: typing.Optional[typing.List[str]]

### RouteTableId
- **Type**: typing.Optional[str]


# FMSPolicyUpdateFirewallCreationConfigAction

### Description
- **Type**: typing.Optional[str]

### FirewallCreationConfig
- **Type**: typing.Optional[str]


# FailedItem

### URI
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['NOT_VALID_ACCOUNT_ID', 'NOT_VALID_ARN', 'NOT_VALID_PARTITION', 'NOT_VALID_REGION', 'NOT_VALID_RESOURCE_TYPE', 'NOT_VALID_SERVICE']]


# FirewallSubnetIsOutOfScopeViolation

### FirewallSubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### SubnetAvailabilityZoneId
- **Type**: typing.Optional[str]

### VpcEndpointId
- **Type**: typing.Optional[str]


# FirewallSubnetMissingVPCEndpointViolation

### FirewallSubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### SubnetAvailabilityZoneId
- **Type**: typing.Optional[str]


# GetAdminAccountResponse

### AdminAccount
- **Type**: <class 'str'>
- **Required**: Yes

### RoleStatus
- **Type**: typing.Literal['CREATING', 'DELETED', 'DELETING', 'PENDING_DELETION', 'READY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetAdminScopeRequest

### AdminAccount
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdminScopeResponse

### AdminScope
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.AdminScopeOutput'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['OFFBOARDING', 'OFFBOARDING_COMPLETE', 'ONBOARDING', 'ONBOARDING_COMPLETE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppsListRequest

### ListId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultList
- **Type**: typing.Optional[bool]


# GetAppsListResponse

### AppsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.AppsListDataOutput'>
- **Required**: Yes

### AppsListArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetComplianceDetailRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberAccount
- **Type**: <class 'str'>
- **Required**: Yes


# GetComplianceDetailResponse

### PolicyComplianceDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.PolicyComplianceDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetNotificationChannelResponse

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsRoleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.PolicyOutput'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetProtectionStatusRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberAccountId
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.Timestamp]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetProtectionStatusResponse

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceType
- **Type**: typing.Literal['DNS_FIREWALL', 'IMPORT_NETWORK_FIREWALL', 'NETWORK_ACL_COMMON', 'NETWORK_FIREWALL', 'SECURITY_GROUPS_COMMON', 'SECURITY_GROUPS_CONTENT_AUDIT', 'SECURITY_GROUPS_USAGE_AUDIT', 'SHIELD_ADVANCED', 'THIRD_PARTY_FIREWALL', 'WAF', 'WAFV2']
- **Required**: Yes

### Data
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetProtocolsListRequest

### ListId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultList
- **Type**: typing.Optional[bool]


# GetProtocolsListResponse

### ProtocolsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ProtocolsListDataOutput'>
- **Required**: Yes

### ProtocolsListArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceSetRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceSetResponse

### ResourceSet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResourceSetOutput'>
- **Required**: Yes

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetThirdPartyFirewallAssociationStatusRequest

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes


# GetThirdPartyFirewallAssociationStatusResponse

### ThirdPartyFirewallStatus
- **Type**: typing.Literal['NOT_EXIST', 'OFFBOARDING', 'OFFBOARD_COMPLETE', 'ONBOARDING', 'ONBOARD_COMPLETE']
- **Required**: Yes

### MarketplaceOnboardingStatus
- **Type**: typing.Literal['COMPLETE', 'NOT_COMPLETE', 'NO_SUBSCRIPTION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# GetViolationDetailsRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberAccount
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes


# GetViolationDetailsResponse

### ViolationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ViolationDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# InvalidNetworkAclEntriesViolation

### Vpc
- **Type**: typing.Optional[str]

### Subnet
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### CurrentAssociatedNetworkAcl
- **Type**: typing.Optional[str]

### EntryViolations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EntryViolation]]


# ListAdminAccountsForOrganizationRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAdminAccountsForOrganizationRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfig]


# ListAdminAccountsForOrganizationResponse

### AdminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.AdminAccountSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAdminsManagingAccountRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAdminsManagingAccountRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfig]


# ListAdminsManagingAccountResponse

### AdminAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppsListsRequest

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultLists
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]


# ListAppsListsRequestPaginate

### DefaultLists
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfig]


# ListAppsListsResponse

### AppsLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.AppsListDataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComplianceStatusRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComplianceStatusRequestPaginate

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfig]


# ListComplianceStatusResponse

### PolicyComplianceStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.PolicyComplianceStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesRequest

### MemberAccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.DiscoveredResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMemberAccountsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMemberAccountsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfig]


# ListMemberAccountsResponse

### MemberAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPoliciesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfig]


# ListPoliciesResponse

### PolicyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.PolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtocolsListsRequest

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultLists
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]


# ListProtocolsListsRequestPaginate

### DefaultLists
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfig]


# ListProtocolsListsResponse

### ProtocolsLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ProtocolsListDataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetResourcesRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetResourcesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.Resource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceSetsResponse

### ResourceSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ResourceSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# ListThirdPartyFirewallFirewallPoliciesRequest

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListThirdPartyFirewallFirewallPoliciesRequestPaginate

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfig]


# ListThirdPartyFirewallFirewallPoliciesResponse

### ThirdPartyFirewallFirewallPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ThirdPartyFirewallFirewallPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NetworkAclCommonPolicy

### NetworkAclEntrySet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntrySet'>
- **Required**: Yes


# NetworkAclCommonPolicyOutput

### NetworkAclEntrySet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntrySetOutput'>
- **Required**: Yes


# NetworkAclEntry

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkAclEntrySet

### ForceRemediateForFirstEntries
- **Type**: <class 'bool'>
- **Required**: Yes

### ForceRemediateForLastEntries
- **Type**: <class 'bool'>
- **Required**: Yes

### FirstEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntry]]

### LastEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntry]]


# NetworkAclEntrySetOutput

### ForceRemediateForFirstEntries
- **Type**: <class 'bool'>
- **Required**: Yes

### ForceRemediateForLastEntries
- **Type**: <class 'bool'>
- **Required**: Yes

### FirstEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntry]]

### LastEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntry]]


# NetworkAclPortRange

### From
- **Type**: typing.Optional[int]

### To
- **Type**: typing.Optional[int]


# NetworkFirewallBlackHoleRouteDetectedViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### RouteTableId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]


# NetworkFirewallInternetTrafficNotInspectedViolation

### SubnetId
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### RouteTableId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### IsRouteTableUsedInDifferentAZ
- **Type**: typing.Optional[bool]

### CurrentFirewallSubnetRouteTable
- **Type**: typing.Optional[str]

### ExpectedFirewallEndpoint
- **Type**: typing.Optional[str]

### FirewallSubnetId
- **Type**: typing.Optional[str]

### ExpectedFirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRoute]]

### ActualFirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### InternetGatewayId
- **Type**: typing.Optional[str]

### CurrentInternetGatewayRouteTable
- **Type**: typing.Optional[str]

### ExpectedInternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRoute]]

### ActualInternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### VpcId
- **Type**: typing.Optional[str]


# NetworkFirewallInvalidRouteConfigurationViolation

### AffectedSubnets
- **Type**: typing.Optional[typing.List[str]]

### RouteTableId
- **Type**: typing.Optional[str]

### IsRouteTableUsedInDifferentAZ
- **Type**: typing.Optional[bool]

### ViolatingRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.Route]

### CurrentFirewallSubnetRouteTable
- **Type**: typing.Optional[str]

### ExpectedFirewallEndpoint
- **Type**: typing.Optional[str]

### ActualFirewallEndpoint
- **Type**: typing.Optional[str]

### ExpectedFirewallSubnetId
- **Type**: typing.Optional[str]

### ActualFirewallSubnetId
- **Type**: typing.Optional[str]

### ExpectedFirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRoute]]

### ActualFirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### InternetGatewayId
- **Type**: typing.Optional[str]

### CurrentInternetGatewayRouteTable
- **Type**: typing.Optional[str]

### ExpectedInternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRoute]]

### ActualInternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### VpcId
- **Type**: typing.Optional[str]


# NetworkFirewallMissingExpectedRTViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### CurrentRouteTable
- **Type**: typing.Optional[str]

### ExpectedRouteTable
- **Type**: typing.Optional[str]


# NetworkFirewallMissingExpectedRoutesViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### ExpectedRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRoute]]

### VpcId
- **Type**: typing.Optional[str]


# NetworkFirewallMissingFirewallViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### TargetViolationReason
- **Type**: typing.Optional[str]


# NetworkFirewallMissingSubnetViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### TargetViolationReason
- **Type**: typing.Optional[str]


# NetworkFirewallPolicy

### FirewallDeploymentModel
- **Type**: typing.Optional[typing.Literal['CENTRALIZED', 'DISTRIBUTED']]


# NetworkFirewallPolicyDescription

### StatelessRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.StatelessRuleGroup]]

### StatelessDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessFragmentDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.List[str]]

### StatefulRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.StatefulRuleGroup]]

### StatefulDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatefulEngineOptions
- **Type**: <class 'NoneType'>


# NetworkFirewallPolicyModifiedViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### CurrentPolicyDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallPolicyDescription]

### ExpectedPolicyDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallPolicyDescription]


# NetworkFirewallStatefulRuleGroupOverride

### Action
- **Type**: typing.Optional[typing.Literal['DROP_TO_ALERT']]


# NetworkFirewallUnexpectedFirewallRoutesViolation

### FirewallSubnetId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### RouteTableId
- **Type**: typing.Optional[str]

### FirewallEndpoint
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# NetworkFirewallUnexpectedGatewayRoutesViolation

### GatewayId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### RouteTableId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# OrganizationalUnitScope

### OrganizationalUnits
- **Type**: typing.Optional[typing.Sequence[str]]

### AllOrganizationalUnitsEnabled
- **Type**: typing.Optional[bool]

### ExcludeSpecifiedOrganizationalUnits
- **Type**: typing.Optional[bool]


# OrganizationalUnitScopeOutput

### OrganizationalUnits
- **Type**: typing.Optional[typing.List[str]]

### AllOrganizationalUnitsEnabled
- **Type**: typing.Optional[bool]

### ExcludeSpecifiedOrganizationalUnits
- **Type**: typing.Optional[bool]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartialMatch

### Reference
- **Type**: typing.Optional[str]

### TargetViolationReasons
- **Type**: typing.Optional[typing.List[str]]


# Policy

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityServicePolicyData
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.SecurityServicePolicyData'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: <class 'bool'>
- **Required**: Yes

### RemediationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### PolicyId
- **Type**: typing.Optional[str]

### PolicyUpdateToken
- **Type**: typing.Optional[str]

### ResourceTypeList
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.ResourceTag]]

### DeleteUnusedFMManagedResources
- **Type**: typing.Optional[bool]

### IncludeMap
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ACCOUNT', 'ORG_UNIT'], typing.Sequence[str]]]

### ExcludeMap
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ACCOUNT', 'ORG_UNIT'], typing.Sequence[str]]]

### ResourceSetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PolicyDescription
- **Type**: typing.Optional[str]

### PolicyStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'OUT_OF_ADMIN_SCOPE']]

### ResourceTagLogicalOperator
- **Type**: typing.Optional[typing.Literal['AND', 'OR']]


# PolicyComplianceDetail

### PolicyOwner
- **Type**: typing.Optional[str]

### PolicyId
- **Type**: typing.Optional[str]

### MemberAccount
- **Type**: typing.Optional[str]

### Violators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ComplianceViolator]]

### EvaluationLimitExceeded
- **Type**: typing.Optional[bool]

### ExpiredAt
- **Type**: typing.Optional[datetime.datetime]

### IssueInfoMap
- **Type**: typing.Optional[typing.Dict[typing.Literal['AWSCONFIG', 'AWSSHIELD_ADVANCED', 'AWSVPC', 'AWSWAF'], str]]


# PolicyComplianceStatus

### PolicyOwner
- **Type**: typing.Optional[str]

### PolicyId
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### MemberAccount
- **Type**: typing.Optional[str]

### EvaluationResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EvaluationResult]]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### IssueInfoMap
- **Type**: typing.Optional[typing.Dict[typing.Literal['AWSCONFIG', 'AWSSHIELD_ADVANCED', 'AWSVPC', 'AWSWAF'], str]]


# PolicyOption

### NetworkFirewallPolicy
- **Type**: <class 'NoneType'>

### ThirdPartyFirewallPolicy
- **Type**: <class 'NoneType'>

### NetworkAclCommonPolicy
- **Type**: <class 'NoneType'>


# PolicyOptionOutput

### NetworkFirewallPolicy
- **Type**: <class 'NoneType'>

### ThirdPartyFirewallPolicy
- **Type**: <class 'NoneType'>

### NetworkAclCommonPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkAclCommonPolicyOutput]


# PolicyOutput

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityServicePolicyData
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.SecurityServicePolicyDataOutput'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeResourceTags
- **Type**: <class 'bool'>
- **Required**: Yes

### RemediationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### PolicyId
- **Type**: typing.Optional[str]

### PolicyUpdateToken
- **Type**: typing.Optional[str]

### ResourceTypeList
- **Type**: typing.Optional[typing.List[str]]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ResourceTag]]

### DeleteUnusedFMManagedResources
- **Type**: typing.Optional[bool]

### IncludeMap
- **Type**: typing.Optional[typing.Dict[typing.Literal['ACCOUNT', 'ORG_UNIT'], typing.List[str]]]

### ExcludeMap
- **Type**: typing.Optional[typing.Dict[typing.Literal['ACCOUNT', 'ORG_UNIT'], typing.List[str]]]

### ResourceSetIds
- **Type**: typing.Optional[typing.List[str]]

### PolicyDescription
- **Type**: typing.Optional[str]

### PolicyStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'OUT_OF_ADMIN_SCOPE']]

### ResourceTagLogicalOperator
- **Type**: typing.Optional[typing.Literal['AND', 'OR']]


# PolicySummary

### PolicyArn
- **Type**: typing.Optional[str]

### PolicyId
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### SecurityServiceType
- **Type**: typing.Optional[typing.Literal['DNS_FIREWALL', 'IMPORT_NETWORK_FIREWALL', 'NETWORK_ACL_COMMON', 'NETWORK_FIREWALL', 'SECURITY_GROUPS_COMMON', 'SECURITY_GROUPS_CONTENT_AUDIT', 'SECURITY_GROUPS_USAGE_AUDIT', 'SHIELD_ADVANCED', 'THIRD_PARTY_FIREWALL', 'WAF', 'WAFV2']]

### RemediationEnabled
- **Type**: typing.Optional[bool]

### DeleteUnusedFMManagedResources
- **Type**: typing.Optional[bool]

### PolicyStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'OUT_OF_ADMIN_SCOPE']]


# PolicyTypeScope

### PolicyTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DNS_FIREWALL', 'IMPORT_NETWORK_FIREWALL', 'NETWORK_ACL_COMMON', 'NETWORK_FIREWALL', 'SECURITY_GROUPS_COMMON', 'SECURITY_GROUPS_CONTENT_AUDIT', 'SECURITY_GROUPS_USAGE_AUDIT', 'SHIELD_ADVANCED', 'THIRD_PARTY_FIREWALL', 'WAF', 'WAFV2']]]

### AllPolicyTypesEnabled
- **Type**: typing.Optional[bool]


# PolicyTypeScopeOutput

### PolicyTypes
- **Type**: typing.Optional[typing.List[typing.Literal['DNS_FIREWALL', 'IMPORT_NETWORK_FIREWALL', 'NETWORK_ACL_COMMON', 'NETWORK_FIREWALL', 'SECURITY_GROUPS_COMMON', 'SECURITY_GROUPS_CONTENT_AUDIT', 'SECURITY_GROUPS_USAGE_AUDIT', 'SHIELD_ADVANCED', 'THIRD_PARTY_FIREWALL', 'WAF', 'WAFV2']]]

### AllPolicyTypesEnabled
- **Type**: typing.Optional[bool]


# PolicyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PossibleRemediationAction

### OrderedRemediationActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.RemediationActionWithOrder]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IsDefaultAction
- **Type**: typing.Optional[bool]


# PossibleRemediationActions

### Description
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.PossibleRemediationAction]]


# ProtocolsListData

### ListName
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolsList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ListId
- **Type**: typing.Optional[str]

### ListUpdateToken
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.Timestamp]

### LastUpdateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.Timestamp]

### PreviousProtocolsList
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# ProtocolsListDataOutput

### ListName
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolsList
- **Type**: typing.List[str]
- **Required**: Yes

### ListId
- **Type**: typing.Optional[str]

### ListUpdateToken
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### PreviousProtocolsList
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# ProtocolsListDataSummary

### ListArn
- **Type**: typing.Optional[str]

### ListId
- **Type**: typing.Optional[str]

### ListName
- **Type**: typing.Optional[str]

### ProtocolsList
- **Type**: typing.Optional[typing.List[str]]


# ProtocolsListDataUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutAdminAccountRequest

### AdminAccount
- **Type**: <class 'str'>
- **Required**: Yes

### AdminScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.AdminScopeUnion]


# PutAppsListRequest

### AppsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.AppsListDataUnion'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.Tag]]


# PutAppsListResponse

### AppsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.AppsListDataOutput'>
- **Required**: Yes

### AppsListArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# PutNotificationChannelRequest

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsRoleName
- **Type**: <class 'str'>
- **Required**: Yes


# PutPolicyRequest

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.PolicyUnion'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.Tag]]


# PutPolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.PolicyOutput'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# PutProtocolsListRequest

### ProtocolsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ProtocolsListDataUnion'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.Tag]]


# PutProtocolsListResponse

### ProtocolsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ProtocolsListDataOutput'>
- **Required**: Yes

### ProtocolsListArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourceSetRequest

### ResourceSet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResourceSetUnion'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.Tag]]


# PutResourceSetResponse

### ResourceSet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResourceSetOutput'>
- **Required**: Yes

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadata'>
- **Required**: Yes


# RegionScope

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]

### AllRegionsEnabled
- **Type**: typing.Optional[bool]


# RegionScopeOutput

### Regions
- **Type**: typing.Optional[typing.List[str]]

### AllRegionsEnabled
- **Type**: typing.Optional[bool]


# RemediationAction

### Description
- **Type**: typing.Optional[str]

### EC2CreateRouteAction
- **Type**: <class 'NoneType'>

### EC2ReplaceRouteAction
- **Type**: <class 'NoneType'>

### EC2DeleteRouteAction
- **Type**: <class 'NoneType'>

### EC2CopyRouteTableAction
- **Type**: <class 'NoneType'>

### EC2ReplaceRouteTableAssociationAction
- **Type**: <class 'NoneType'>

### EC2AssociateRouteTableAction
- **Type**: <class 'NoneType'>

### EC2CreateRouteTableAction
- **Type**: <class 'NoneType'>

### FMSPolicyUpdateFirewallCreationConfigAction
- **Type**: <class 'NoneType'>

### CreateNetworkAclAction
- **Type**: <class 'NoneType'>

### ReplaceNetworkAclAssociationAction
- **Type**: <class 'NoneType'>

### CreateNetworkAclEntriesAction
- **Type**: <class 'NoneType'>

### DeleteNetworkAclEntriesAction
- **Type**: <class 'NoneType'>


# RemediationActionWithOrder

### RemediationAction
- **Type**: <class 'NoneType'>

### Order
- **Type**: typing.Optional[int]


# ReplaceNetworkAclAssociationAction

### Description
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]

### NetworkAclId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTarget]

### FMSCanRemediate
- **Type**: typing.Optional[bool]


# Resource

### URI
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# ResourceSet

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypeList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UpdateToken
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.Timestamp]

### ResourceSetStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'OUT_OF_ADMIN_SCOPE']]


# ResourceSetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypeList
- **Type**: typing.List[str]
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UpdateToken
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceSetStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'OUT_OF_ADMIN_SCOPE']]


# ResourceSetSummary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceSetStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'OUT_OF_ADMIN_SCOPE']]


# ResourceSetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceTag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# ResourceViolation

### AwsVPCSecurityGroupViolation
- **Type**: <class 'NoneType'>

### AwsEc2NetworkInterfaceViolation
- **Type**: <class 'NoneType'>

### AwsEc2InstanceViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallMissingFirewallViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallMissingSubnetViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallMissingExpectedRTViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallPolicyModifiedViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallInternetTrafficNotInspectedViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallInvalidRouteConfigurationViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallBlackHoleRouteDetectedViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallUnexpectedFirewallRoutesViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallUnexpectedGatewayRoutesViolation
- **Type**: <class 'NoneType'>

### NetworkFirewallMissingExpectedRoutesViolation
- **Type**: <class 'NoneType'>

### DnsRuleGroupPriorityConflictViolation
- **Type**: <class 'NoneType'>

### DnsDuplicateRuleGroupViolation
- **Type**: <class 'NoneType'>

### DnsRuleGroupLimitExceededViolation
- **Type**: <class 'NoneType'>

### FirewallSubnetIsOutOfScopeViolation
- **Type**: <class 'NoneType'>

### RouteHasOutOfScopeEndpointViolation
- **Type**: <class 'NoneType'>

### ThirdPartyFirewallMissingFirewallViolation
- **Type**: <class 'NoneType'>

### ThirdPartyFirewallMissingSubnetViolation
- **Type**: <class 'NoneType'>

### ThirdPartyFirewallMissingExpectedRouteTableViolation
- **Type**: <class 'NoneType'>

### FirewallSubnetMissingVPCEndpointViolation
- **Type**: <class 'NoneType'>

### InvalidNetworkAclEntriesViolation
- **Type**: <class 'NoneType'>

### PossibleRemediationActions
- **Type**: <class 'NoneType'>

### WebACLHasIncompatibleConfigurationViolation
- **Type**: <class 'NoneType'>

### WebACLHasOutOfScopeResourcesViolation
- **Type**: <class 'NoneType'>


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


# Route

### DestinationType
- **Type**: typing.Optional[typing.Literal['IPV4', 'IPV6', 'PREFIX_LIST']]

### TargetType
- **Type**: typing.Optional[typing.Literal['CARRIER_GATEWAY', 'EGRESS_ONLY_INTERNET_GATEWAY', 'GATEWAY', 'INSTANCE', 'LOCAL_GATEWAY', 'NAT_GATEWAY', 'NETWORK_INTERFACE', 'TRANSIT_GATEWAY', 'VPC_ENDPOINT', 'VPC_PEERING_CONNECTION']]

### Destination
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# RouteHasOutOfScopeEndpointViolation

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### RouteTableId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### SubnetAvailabilityZoneId
- **Type**: typing.Optional[str]

### CurrentFirewallSubnetRouteTable
- **Type**: typing.Optional[str]

### FirewallSubnetId
- **Type**: typing.Optional[str]

### FirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]

### InternetGatewayId
- **Type**: typing.Optional[str]

### CurrentInternetGatewayRouteTable
- **Type**: typing.Optional[str]

### InternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Route]]


# SecurityGroupRemediationAction

### RemediationActionType
- **Type**: typing.Optional[typing.Literal['MODIFY', 'REMOVE']]

### Description
- **Type**: typing.Optional[str]

### RemediationResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.SecurityGroupRuleDescription]

### IsDefaultAction
- **Type**: typing.Optional[bool]


# SecurityGroupRuleDescription

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityServicePolicyData

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityServicePolicyDataOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StatefulEngineOptions

### RuleOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT_ACTION_ORDER', 'STRICT_ORDER']]

### StreamExceptionPolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP', 'FMS_IGNORE', 'REJECT']]


# StatefulRuleGroup

### RuleGroupName
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Override
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallStatefulRuleGroupOverride]


# StatelessRuleGroup

### RuleGroupName
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]


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

### TagList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.Tag]
- **Required**: Yes


# ThirdPartyFirewallFirewallPolicy

### FirewallPolicyId
- **Type**: typing.Optional[str]

### FirewallPolicyName
- **Type**: typing.Optional[str]


# ThirdPartyFirewallMissingExpectedRouteTableViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### CurrentRouteTable
- **Type**: typing.Optional[str]

### ExpectedRouteTable
- **Type**: typing.Optional[str]


# ThirdPartyFirewallMissingFirewallViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### TargetViolationReason
- **Type**: typing.Optional[str]


# ThirdPartyFirewallMissingSubnetViolation

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### TargetViolationReason
- **Type**: typing.Optional[str]


# ThirdPartyFirewallPolicy

### FirewallDeploymentModel
- **Type**: typing.Optional[typing.Literal['CENTRALIZED', 'DISTRIBUTED']]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ViolationDetail

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberAccount
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceViolations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ResourceViolation]
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.Tag]]

### ResourceDescription
- **Type**: typing.Optional[str]


# WebACLHasIncompatibleConfigurationViolation

### WebACLArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# WebACLHasOutOfScopeResourcesViolation

### WebACLArn
- **Type**: typing.Optional[str]

### OutOfScopeResourceList
- **Type**: typing.Optional[typing.List[str]]


