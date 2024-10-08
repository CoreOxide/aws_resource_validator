# Pydantic Models in fms_classes

# AccountScopeOutputTypeDef

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### AllAccountsEnabled
- **Type**: typing.Optional[bool]

### ExcludeSpecifiedAccounts
- **Type**: typing.Optional[bool]


# AccountScopeTypeDef

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### AllAccountsEnabled
- **Type**: typing.Optional[bool]

### ExcludeSpecifiedAccounts
- **Type**: typing.Optional[bool]


# ActionTargetTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AdminAccountSummaryTypeDef

### AdminAccount
- **Type**: typing.Optional[str]

### DefaultAdmin
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['OFFBOARDING', 'OFFBOARDING_COMPLETE', 'ONBOARDING', 'ONBOARDING_COMPLETE']]


# AdminScopeOutputTypeDef

### AccountScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.AccountScopeOutputTypeDef]

### OrganizationalUnitScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.OrganizationalUnitScopeOutputTypeDef]

### RegionScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.RegionScopeOutputTypeDef]

### PolicyTypeScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PolicyTypeScopeOutputTypeDef]


# AdminScopeTypeDef

### AccountScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.AccountScopeTypeDef]

### OrganizationalUnitScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.OrganizationalUnitScopeTypeDef]

### RegionScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.RegionScopeTypeDef]

### PolicyTypeScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PolicyTypeScopeTypeDef]


# AppTypeDef

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes


# AppsListDataOutputTypeDef

### ListName
- **Type**: <class 'str'>
- **Required**: Yes

### AppsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.AppTypeDef]
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
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.fms_classes.AppTypeDef]]]


# AppsListDataSummaryTypeDef

### ListArn
- **Type**: typing.Optional[str]

### ListId
- **Type**: typing.Optional[str]

### ListName
- **Type**: typing.Optional[str]

### AppsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.AppTypeDef]]


# AppsListDataTypeDef

### ListName
- **Type**: <class 'str'>
- **Required**: Yes

### AppsList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.AppTypeDef]
- **Required**: Yes

### ListId
- **Type**: typing.Optional[str]

### ListUpdateToken
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastUpdateTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PreviousAppsList
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.AppTypeDef]]]


# AssociateAdminAccountRequestRequestTypeDef

### AdminAccount
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateThirdPartyFirewallRequestRequestTypeDef

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes


# AssociateThirdPartyFirewallResponseTypeDef

### ThirdPartyFirewallStatus
- **Type**: typing.Literal['NOT_EXIST', 'OFFBOARDING', 'OFFBOARD_COMPLETE', 'ONBOARDING', 'ONBOARD_COMPLETE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AwsEc2InstanceViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### AwsEc2NetworkInterfaceViolations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.AwsEc2NetworkInterfaceViolationTypeDef]]


# AwsEc2NetworkInterfaceViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolatingSecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# AwsVPCSecurityGroupViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolationTargetDescription
- **Type**: typing.Optional[str]

### PartialMatches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.PartialMatchTypeDef]]

### PossibleSecurityGroupRemediationActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.SecurityGroupRemediationActionTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateResourceRequestRequestTypeDef

### ResourceSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchAssociateResourceResponseTypeDef

### ResourceSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### FailedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.FailedItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateResourceRequestRequestTypeDef

### ResourceSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDisassociateResourceResponseTypeDef

### ResourceSetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### FailedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.FailedItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ComplianceViolatorTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### ViolationReason
- **Type**: typing.Optional[typing.Literal['BLACK_HOLE_ROUTE_DETECTED', 'BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET', 'FIREWALL_SUBNET_IS_OUT_OF_SCOPE', 'FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE', 'FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT', 'FMS_CREATED_SECURITY_GROUP_EDITED', 'INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE', 'INTERNET_TRAFFIC_NOT_INSPECTED', 'INVALID_NETWORK_ACL_ENTRY', 'INVALID_ROUTE_CONFIGURATION', 'MISSING_EXPECTED_ROUTE_TABLE', 'MISSING_FIREWALL', 'MISSING_FIREWALL_SUBNET_IN_AZ', 'MISSING_TARGET_GATEWAY', 'NETWORK_FIREWALL_POLICY_MODIFIED', 'RESOURCE_INCORRECT_WEB_ACL', 'RESOURCE_MISSING_DNS_FIREWALL', 'RESOURCE_MISSING_SECURITY_GROUP', 'RESOURCE_MISSING_SHIELD_PROTECTION', 'RESOURCE_MISSING_WEB_ACL', 'RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION', 'RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP', 'ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT', 'SECURITY_GROUP_REDUNDANT', 'SECURITY_GROUP_UNUSED', 'TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY', 'UNEXPECTED_FIREWALL_ROUTES', 'UNEXPECTED_TARGET_GATEWAY_ROUTES', 'WEB_ACL_MISSING_RULE_GROUP']]

### ResourceType
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNetworkAclActionTypeDef

### Description
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]

### FMSCanRemediate
- **Type**: typing.Optional[bool]


# CreateNetworkAclEntriesActionTypeDef

### Description
- **Type**: typing.Optional[str]

### NetworkAclId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]

### NetworkAclEntriesToBeCreated
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EntryDescriptionTypeDef]]

### FMSCanRemediate
- **Type**: typing.Optional[bool]


# DeleteAppsListRequestRequestTypeDef

### ListId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkAclEntriesActionTypeDef

### Description
- **Type**: typing.Optional[str]

### NetworkAclId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]

### NetworkAclEntriesToBeDeleted
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EntryDescriptionTypeDef]]

### FMSCanRemediate
- **Type**: typing.Optional[bool]


# DeletePolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteAllPolicyResources
- **Type**: typing.Optional[bool]


# DeleteProtocolsListRequestRequestTypeDef

### ListId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceSetRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateThirdPartyFirewallRequestRequestTypeDef

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes


# DisassociateThirdPartyFirewallResponseTypeDef

### ThirdPartyFirewallStatus
- **Type**: typing.Literal['NOT_EXIST', 'OFFBOARDING', 'OFFBOARD_COMPLETE', 'ONBOARDING', 'ONBOARD_COMPLETE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DiscoveredResourceTypeDef

### URI
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DnsDuplicateRuleGroupViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolationTargetDescription
- **Type**: typing.Optional[str]


# DnsRuleGroupLimitExceededViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### ViolationTargetDescription
- **Type**: typing.Optional[str]

### NumberOfRuleGroupsAlreadyAssociated
- **Type**: typing.Optional[int]


# DnsRuleGroupPriorityConflictViolationTypeDef

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


# EC2AssociateRouteTableActionTypeDef

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]

### GatewayId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]


# EC2CopyRouteTableActionTypeDef

### VpcId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
- **Required**: Yes

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# EC2CreateRouteActionTypeDef

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]

### GatewayId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]


# EC2CreateRouteTableActionTypeDef

### VpcId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# EC2DeleteRouteActionTypeDef

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### DestinationPrefixListId
- **Type**: typing.Optional[str]

### DestinationIpv6CidrBlock
- **Type**: typing.Optional[str]


# EC2ReplaceRouteActionTypeDef

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]


# EC2ReplaceRouteTableAssociationActionTypeDef

### AssociationId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
- **Required**: Yes

### RouteTableId
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EntryDescriptionTypeDef

### EntryDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntryTypeDef]

### EntryRuleNumber
- **Type**: typing.Optional[int]

### EntryType
- **Type**: typing.Optional[typing.Literal['CUSTOM_ENTRY', 'FMS_MANAGED_FIRST_ENTRY', 'FMS_MANAGED_LAST_ENTRY']]


# EntryViolationTypeDef

### ExpectedEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EntryDescriptionTypeDef]

### ExpectedEvaluationOrder
- **Type**: typing.Optional[str]

### ActualEvaluationOrder
- **Type**: typing.Optional[str]

### EntryAtExpectedEvaluationOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EntryDescriptionTypeDef]

### EntriesWithConflicts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EntryDescriptionTypeDef]]

### EntryViolationReasons
- **Type**: typing.Optional[typing.List[typing.Literal['ENTRY_CONFLICT', 'INCORRECT_ENTRY_ORDER', 'MISSING_EXPECTED_ENTRY']]]


# EvaluationResultTypeDef

### ComplianceStatus
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'NON_COMPLIANT']]

### ViolatorCount
- **Type**: typing.Optional[int]

### EvaluationLimitExceeded
- **Type**: typing.Optional[bool]


# ExpectedRouteTypeDef

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


# FMSPolicyUpdateFirewallCreationConfigActionTypeDef

### Description
- **Type**: typing.Optional[str]

### FirewallCreationConfig
- **Type**: typing.Optional[str]


# FailedItemTypeDef

### URI
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['NOT_VALID_ACCOUNT_ID', 'NOT_VALID_ARN', 'NOT_VALID_PARTITION', 'NOT_VALID_REGION', 'NOT_VALID_RESOURCE_TYPE', 'NOT_VALID_SERVICE']]


# FirewallSubnetIsOutOfScopeViolationTypeDef

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


# FirewallSubnetMissingVPCEndpointViolationTypeDef

### FirewallSubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### SubnetAvailabilityZoneId
- **Type**: typing.Optional[str]


# GetAdminAccountResponseTypeDef

### AdminAccount
- **Type**: <class 'str'>
- **Required**: Yes

### RoleStatus
- **Type**: typing.Literal['CREATING', 'DELETED', 'DELETING', 'PENDING_DELETION', 'READY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAdminScopeRequestRequestTypeDef

### AdminAccount
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdminScopeResponseTypeDef

### AdminScope
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.AdminScopeOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['OFFBOARDING', 'OFFBOARDING_COMPLETE', 'ONBOARDING', 'ONBOARDING_COMPLETE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppsListRequestRequestTypeDef

### ListId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultList
- **Type**: typing.Optional[bool]


# GetAppsListResponseTypeDef

### AppsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.AppsListDataOutputTypeDef'>
- **Required**: Yes

### AppsListArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComplianceDetailRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberAccount
- **Type**: <class 'str'>
- **Required**: Yes


# GetComplianceDetailResponseTypeDef

### PolicyComplianceDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.PolicyComplianceDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNotificationChannelResponseTypeDef

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsRoleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.PolicyOutputTypeDef'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProtectionStatusRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberAccountId
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetProtectionStatusResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetProtocolsListRequestRequestTypeDef

### ListId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultList
- **Type**: typing.Optional[bool]


# GetProtocolsListResponseTypeDef

### ProtocolsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ProtocolsListDataOutputTypeDef'>
- **Required**: Yes

### ProtocolsListArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceSetRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceSetResponseTypeDef

### ResourceSet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResourceSetOutputTypeDef'>
- **Required**: Yes

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes


# GetThirdPartyFirewallAssociationStatusResponseTypeDef

### ThirdPartyFirewallStatus
- **Type**: typing.Literal['NOT_EXIST', 'OFFBOARDING', 'OFFBOARD_COMPLETE', 'ONBOARDING', 'ONBOARD_COMPLETE']
- **Required**: Yes

### MarketplaceOnboardingStatus
- **Type**: typing.Literal['COMPLETE', 'NOT_COMPLETE', 'NO_SUBSCRIPTION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetViolationDetailsRequestRequestTypeDef

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


# GetViolationDetailsResponseTypeDef

### ViolationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ViolationDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvalidNetworkAclEntriesViolationTypeDef

### Vpc
- **Type**: typing.Optional[str]

### Subnet
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### CurrentAssociatedNetworkAcl
- **Type**: typing.Optional[str]

### EntryViolations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EntryViolationTypeDef]]


# ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfigTypeDef]


# ListAdminAccountsForOrganizationRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAdminAccountsForOrganizationResponseTypeDef

### AdminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.AdminAccountSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfigTypeDef]


# ListAdminsManagingAccountRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAdminsManagingAccountResponseTypeDef

### AdminAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppsListsRequestListAppsListsPaginateTypeDef

### DefaultLists
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfigTypeDef]


# ListAppsListsRequestRequestTypeDef

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultLists
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]


# ListAppsListsResponseTypeDef

### AppsLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.AppsListDataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComplianceStatusRequestListComplianceStatusPaginateTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfigTypeDef]


# ListComplianceStatusRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComplianceStatusResponseTypeDef

### PolicyComplianceStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.PolicyComplianceStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesRequestRequestTypeDef

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


# ListDiscoveredResourcesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.DiscoveredResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMemberAccountsRequestListMemberAccountsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfigTypeDef]


# ListMemberAccountsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMemberAccountsResponseTypeDef

### MemberAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPoliciesRequestListPoliciesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfigTypeDef]


# ListPoliciesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPoliciesResponseTypeDef

### PolicyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.PolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtocolsListsRequestListProtocolsListsPaginateTypeDef

### DefaultLists
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfigTypeDef]


# ListProtocolsListsRequestRequestTypeDef

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultLists
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]


# ListProtocolsListsResponseTypeDef

### ProtocolsLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ProtocolsListDataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetResourcesRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetResourcesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceSetsResponseTypeDef

### ResourceSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ResourceSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PaginatorConfigTypeDef]


# ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef

### ThirdPartyFirewall
- **Type**: typing.Literal['FORTIGATE_CLOUD_NATIVE_FIREWALL', 'PALO_ALTO_NETWORKS_CLOUD_NGFW']
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListThirdPartyFirewallFirewallPoliciesResponseTypeDef

### ThirdPartyFirewallFirewallPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ThirdPartyFirewallFirewallPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NetworkAclCommonPolicyOutputTypeDef

### NetworkAclEntrySet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntrySetOutputTypeDef'>
- **Required**: Yes


# NetworkAclCommonPolicyTypeDef

### NetworkAclEntrySet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntrySetTypeDef'>
- **Required**: Yes


# NetworkAclEntrySetOutputTypeDef

### ForceRemediateForFirstEntries
- **Type**: <class 'bool'>
- **Required**: Yes

### ForceRemediateForLastEntries
- **Type**: <class 'bool'>
- **Required**: Yes

### FirstEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntryTypeDef]]

### LastEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntryTypeDef]]


# NetworkAclEntrySetTypeDef

### ForceRemediateForFirstEntries
- **Type**: <class 'bool'>
- **Required**: Yes

### ForceRemediateForLastEntries
- **Type**: <class 'bool'>
- **Required**: Yes

### FirstEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntryTypeDef]]

### LastEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.NetworkAclEntryTypeDef]]


# NetworkAclEntryTypeDef

### Protocol
- **Type**: <class 'str'>
- **Required**: Yes

### RuleAction
- **Type**: typing.Literal['allow', 'deny']
- **Required**: Yes

### Egress
- **Type**: <class 'bool'>
- **Required**: Yes

### IcmpTypeCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkAclIcmpTypeCodeTypeDef]

### PortRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkAclPortRangeTypeDef]

### CidrBlock
- **Type**: typing.Optional[str]

### Ipv6CidrBlock
- **Type**: typing.Optional[str]


# NetworkAclIcmpTypeCodeTypeDef

### Code
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[int]


# NetworkAclPortRangeTypeDef

### From
- **Type**: typing.Optional[int]

### To
- **Type**: typing.Optional[int]


# NetworkFirewallBlackHoleRouteDetectedViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### RouteTableId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]


# NetworkFirewallInternetTrafficNotInspectedViolationTypeDef

### SubnetId
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### RouteTableId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### IsRouteTableUsedInDifferentAZ
- **Type**: typing.Optional[bool]

### CurrentFirewallSubnetRouteTable
- **Type**: typing.Optional[str]

### ExpectedFirewallEndpoint
- **Type**: typing.Optional[str]

### FirewallSubnetId
- **Type**: typing.Optional[str]

### ExpectedFirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRouteTypeDef]]

### ActualFirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### InternetGatewayId
- **Type**: typing.Optional[str]

### CurrentInternetGatewayRouteTable
- **Type**: typing.Optional[str]

### ExpectedInternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRouteTypeDef]]

### ActualInternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# NetworkFirewallInvalidRouteConfigurationViolationTypeDef

### AffectedSubnets
- **Type**: typing.Optional[typing.List[str]]

### RouteTableId
- **Type**: typing.Optional[str]

### IsRouteTableUsedInDifferentAZ
- **Type**: typing.Optional[bool]

### ViolatingRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRouteTypeDef]]

### ActualFirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### InternetGatewayId
- **Type**: typing.Optional[str]

### CurrentInternetGatewayRouteTable
- **Type**: typing.Optional[str]

### ExpectedInternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRouteTypeDef]]

### ActualInternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# NetworkFirewallMissingExpectedRTViolationTypeDef

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


# NetworkFirewallMissingExpectedRoutesViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### ExpectedRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ExpectedRouteTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# NetworkFirewallMissingFirewallViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### TargetViolationReason
- **Type**: typing.Optional[str]


# NetworkFirewallMissingSubnetViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### TargetViolationReason
- **Type**: typing.Optional[str]


# NetworkFirewallPolicyDescriptionTypeDef

### StatelessRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.StatelessRuleGroupTypeDef]]

### StatelessDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessFragmentDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.List[str]]

### StatefulRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.StatefulRuleGroupTypeDef]]

### StatefulDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatefulEngineOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.StatefulEngineOptionsTypeDef]


# NetworkFirewallPolicyModifiedViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### CurrentPolicyDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallPolicyDescriptionTypeDef]

### ExpectedPolicyDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallPolicyDescriptionTypeDef]


# NetworkFirewallPolicyTypeDef

### FirewallDeploymentModel
- **Type**: typing.Optional[typing.Literal['CENTRALIZED', 'DISTRIBUTED']]


# NetworkFirewallStatefulRuleGroupOverrideTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DROP_TO_ALERT']]


# NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef

### FirewallSubnetId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### RouteTableId
- **Type**: typing.Optional[str]

### FirewallEndpoint
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef

### GatewayId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### RouteTableId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# OrganizationalUnitScopeOutputTypeDef

### OrganizationalUnits
- **Type**: typing.Optional[typing.List[str]]

### AllOrganizationalUnitsEnabled
- **Type**: typing.Optional[bool]

### ExcludeSpecifiedOrganizationalUnits
- **Type**: typing.Optional[bool]


# OrganizationalUnitScopeTypeDef

### OrganizationalUnits
- **Type**: typing.Optional[typing.Sequence[str]]

### AllOrganizationalUnitsEnabled
- **Type**: typing.Optional[bool]

### ExcludeSpecifiedOrganizationalUnits
- **Type**: typing.Optional[bool]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartialMatchTypeDef

### Reference
- **Type**: typing.Optional[str]

### TargetViolationReasons
- **Type**: typing.Optional[typing.List[str]]


# PolicyComplianceDetailTypeDef

### PolicyOwner
- **Type**: typing.Optional[str]

### PolicyId
- **Type**: typing.Optional[str]

### MemberAccount
- **Type**: typing.Optional[str]

### Violators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ComplianceViolatorTypeDef]]

### EvaluationLimitExceeded
- **Type**: typing.Optional[bool]

### ExpiredAt
- **Type**: typing.Optional[datetime.datetime]

### IssueInfoMap
- **Type**: typing.Optional[typing.Dict[typing.Literal['AWSCONFIG', 'AWSSHIELD_ADVANCED', 'AWSVPC', 'AWSWAF'], str]]


# PolicyComplianceStatusTypeDef

### PolicyOwner
- **Type**: typing.Optional[str]

### PolicyId
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### MemberAccount
- **Type**: typing.Optional[str]

### EvaluationResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.EvaluationResultTypeDef]]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### IssueInfoMap
- **Type**: typing.Optional[typing.Dict[typing.Literal['AWSCONFIG', 'AWSSHIELD_ADVANCED', 'AWSVPC', 'AWSWAF'], str]]


# PolicyOptionOutputTypeDef

### NetworkFirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallPolicyTypeDef]

### ThirdPartyFirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ThirdPartyFirewallPolicyTypeDef]

### NetworkAclCommonPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkAclCommonPolicyOutputTypeDef]


# PolicyOptionTypeDef

### NetworkFirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallPolicyTypeDef]

### ThirdPartyFirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ThirdPartyFirewallPolicyTypeDef]

### NetworkAclCommonPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkAclCommonPolicyTypeDef]


# PolicyOutputTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityServicePolicyData
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.SecurityServicePolicyDataOutputTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.ResourceTagTypeDef]]

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


# PolicySummaryTypeDef

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


# PolicyTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityServicePolicyData
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.SecurityServicePolicyDataTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.ResourceTagTypeDef]]

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


# PolicyTypeScopeOutputTypeDef

### PolicyTypes
- **Type**: typing.Optional[typing.List[typing.Literal['DNS_FIREWALL', 'IMPORT_NETWORK_FIREWALL', 'NETWORK_ACL_COMMON', 'NETWORK_FIREWALL', 'SECURITY_GROUPS_COMMON', 'SECURITY_GROUPS_CONTENT_AUDIT', 'SECURITY_GROUPS_USAGE_AUDIT', 'SHIELD_ADVANCED', 'THIRD_PARTY_FIREWALL', 'WAF', 'WAFV2']]]

### AllPolicyTypesEnabled
- **Type**: typing.Optional[bool]


# PolicyTypeScopeTypeDef

### PolicyTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DNS_FIREWALL', 'IMPORT_NETWORK_FIREWALL', 'NETWORK_ACL_COMMON', 'NETWORK_FIREWALL', 'SECURITY_GROUPS_COMMON', 'SECURITY_GROUPS_CONTENT_AUDIT', 'SECURITY_GROUPS_USAGE_AUDIT', 'SHIELD_ADVANCED', 'THIRD_PARTY_FIREWALL', 'WAF', 'WAFV2']]]

### AllPolicyTypesEnabled
- **Type**: typing.Optional[bool]


# PossibleRemediationActionTypeDef

### OrderedRemediationActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.RemediationActionWithOrderTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IsDefaultAction
- **Type**: typing.Optional[bool]


# PossibleRemediationActionsTypeDef

### Description
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.PossibleRemediationActionTypeDef]]


# ProtocolsListDataOutputTypeDef

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


# ProtocolsListDataSummaryTypeDef

### ListArn
- **Type**: typing.Optional[str]

### ListId
- **Type**: typing.Optional[str]

### ListName
- **Type**: typing.Optional[str]

### ProtocolsList
- **Type**: typing.Optional[typing.List[str]]


# ProtocolsListDataTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastUpdateTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PreviousProtocolsList
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# PutAdminAccountRequestRequestTypeDef

### AdminAccount
- **Type**: <class 'str'>
- **Required**: Yes

### AdminScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.AdminScopeTypeDef]


# PutAppsListRequestRequestTypeDef

### AppsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.AppsListDataTypeDef'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.TagTypeDef]]


# PutAppsListResponseTypeDef

### AppsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.AppsListDataOutputTypeDef'>
- **Required**: Yes

### AppsListArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutNotificationChannelRequestRequestTypeDef

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsRoleName
- **Type**: <class 'str'>
- **Required**: Yes


# PutPolicyRequestRequestTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.PolicyTypeDef'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.TagTypeDef]]


# PutPolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.PolicyOutputTypeDef'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutProtocolsListRequestRequestTypeDef

### ProtocolsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ProtocolsListDataTypeDef'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.TagTypeDef]]


# PutProtocolsListResponseTypeDef

### ProtocolsList
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ProtocolsListDataOutputTypeDef'>
- **Required**: Yes

### ProtocolsListArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourceSetRequestRequestTypeDef

### ResourceSet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResourceSetTypeDef'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.TagTypeDef]]


# PutResourceSetResponseTypeDef

### ResourceSet
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResourceSetOutputTypeDef'>
- **Required**: Yes

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegionScopeOutputTypeDef

### Regions
- **Type**: typing.Optional[typing.List[str]]

### AllRegionsEnabled
- **Type**: typing.Optional[bool]


# RegionScopeTypeDef

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]

### AllRegionsEnabled
- **Type**: typing.Optional[bool]


# RemediationActionTypeDef

### Description
- **Type**: typing.Optional[str]

### EC2CreateRouteAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EC2CreateRouteActionTypeDef]

### EC2ReplaceRouteAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EC2ReplaceRouteActionTypeDef]

### EC2DeleteRouteAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EC2DeleteRouteActionTypeDef]

### EC2CopyRouteTableAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EC2CopyRouteTableActionTypeDef]

### EC2ReplaceRouteTableAssociationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EC2ReplaceRouteTableAssociationActionTypeDef]

### EC2AssociateRouteTableAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EC2AssociateRouteTableActionTypeDef]

### EC2CreateRouteTableAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.EC2CreateRouteTableActionTypeDef]

### FMSPolicyUpdateFirewallCreationConfigAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.FMSPolicyUpdateFirewallCreationConfigActionTypeDef]

### CreateNetworkAclAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.CreateNetworkAclActionTypeDef]

### ReplaceNetworkAclAssociationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ReplaceNetworkAclAssociationActionTypeDef]

### CreateNetworkAclEntriesAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.CreateNetworkAclEntriesActionTypeDef]

### DeleteNetworkAclEntriesAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.DeleteNetworkAclEntriesActionTypeDef]


# RemediationActionWithOrderTypeDef

### RemediationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.RemediationActionTypeDef]

### Order
- **Type**: typing.Optional[int]


# ReplaceNetworkAclAssociationActionTypeDef

### Description
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]

### NetworkAclId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ActionTargetTypeDef]

### FMSCanRemediate
- **Type**: typing.Optional[bool]


# ResourceSetOutputTypeDef

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


# ResourceSetSummaryTypeDef

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


# ResourceSetTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ResourceSetStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'OUT_OF_ADMIN_SCOPE']]


# ResourceTagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# ResourceTypeDef

### URI
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# ResourceViolationTypeDef

### AwsVPCSecurityGroupViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.AwsVPCSecurityGroupViolationTypeDef]

### AwsEc2NetworkInterfaceViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.AwsEc2NetworkInterfaceViolationTypeDef]

### AwsEc2InstanceViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.AwsEc2InstanceViolationTypeDef]

### NetworkFirewallMissingFirewallViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallMissingFirewallViolationTypeDef]

### NetworkFirewallMissingSubnetViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallMissingSubnetViolationTypeDef]

### NetworkFirewallMissingExpectedRTViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallMissingExpectedRTViolationTypeDef]

### NetworkFirewallPolicyModifiedViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallPolicyModifiedViolationTypeDef]

### NetworkFirewallInternetTrafficNotInspectedViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallInternetTrafficNotInspectedViolationTypeDef]

### NetworkFirewallInvalidRouteConfigurationViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallInvalidRouteConfigurationViolationTypeDef]

### NetworkFirewallBlackHoleRouteDetectedViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallBlackHoleRouteDetectedViolationTypeDef]

### NetworkFirewallUnexpectedFirewallRoutesViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef]

### NetworkFirewallUnexpectedGatewayRoutesViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef]

### NetworkFirewallMissingExpectedRoutesViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallMissingExpectedRoutesViolationTypeDef]

### DnsRuleGroupPriorityConflictViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.DnsRuleGroupPriorityConflictViolationTypeDef]

### DnsDuplicateRuleGroupViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.DnsDuplicateRuleGroupViolationTypeDef]

### DnsRuleGroupLimitExceededViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.DnsRuleGroupLimitExceededViolationTypeDef]

### FirewallSubnetIsOutOfScopeViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.FirewallSubnetIsOutOfScopeViolationTypeDef]

### RouteHasOutOfScopeEndpointViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.RouteHasOutOfScopeEndpointViolationTypeDef]

### ThirdPartyFirewallMissingFirewallViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ThirdPartyFirewallMissingFirewallViolationTypeDef]

### ThirdPartyFirewallMissingSubnetViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ThirdPartyFirewallMissingSubnetViolationTypeDef]

### ThirdPartyFirewallMissingExpectedRouteTableViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef]

### FirewallSubnetMissingVPCEndpointViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.FirewallSubnetMissingVPCEndpointViolationTypeDef]

### InvalidNetworkAclEntriesViolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.InvalidNetworkAclEntriesViolationTypeDef]

### PossibleRemediationActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PossibleRemediationActionsTypeDef]


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


# RouteHasOutOfScopeEndpointViolationTypeDef

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### RouteTableId
- **Type**: typing.Optional[str]

### ViolatingRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### SubnetAvailabilityZone
- **Type**: typing.Optional[str]

### SubnetAvailabilityZoneId
- **Type**: typing.Optional[str]

### CurrentFirewallSubnetRouteTable
- **Type**: typing.Optional[str]

### FirewallSubnetId
- **Type**: typing.Optional[str]

### FirewallSubnetRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]

### InternetGatewayId
- **Type**: typing.Optional[str]

### CurrentInternetGatewayRouteTable
- **Type**: typing.Optional[str]

### InternetGatewayRoutes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.RouteTypeDef]]


# RouteTypeDef

### DestinationType
- **Type**: typing.Optional[typing.Literal['IPV4', 'IPV6', 'PREFIX_LIST']]

### TargetType
- **Type**: typing.Optional[typing.Literal['CARRIER_GATEWAY', 'EGRESS_ONLY_INTERNET_GATEWAY', 'GATEWAY', 'INSTANCE', 'LOCAL_GATEWAY', 'NAT_GATEWAY', 'NETWORK_INTERFACE', 'TRANSIT_GATEWAY', 'VPC_ENDPOINT', 'VPC_PEERING_CONNECTION']]

### Destination
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# SecurityGroupRemediationActionTypeDef

### RemediationActionType
- **Type**: typing.Optional[typing.Literal['MODIFY', 'REMOVE']]

### Description
- **Type**: typing.Optional[str]

### RemediationResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.SecurityGroupRuleDescriptionTypeDef]

### IsDefaultAction
- **Type**: typing.Optional[bool]


# SecurityGroupRuleDescriptionTypeDef

### IPV4Range
- **Type**: typing.Optional[str]

### IPV6Range
- **Type**: typing.Optional[str]

### PrefixListId
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]


# SecurityServicePolicyDataOutputTypeDef

### Type
- **Type**: typing.Literal['DNS_FIREWALL', 'IMPORT_NETWORK_FIREWALL', 'NETWORK_ACL_COMMON', 'NETWORK_FIREWALL', 'SECURITY_GROUPS_COMMON', 'SECURITY_GROUPS_CONTENT_AUDIT', 'SECURITY_GROUPS_USAGE_AUDIT', 'SHIELD_ADVANCED', 'THIRD_PARTY_FIREWALL', 'WAF', 'WAFV2']
- **Required**: Yes

### ManagedServiceData
- **Type**: typing.Optional[str]

### PolicyOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PolicyOptionOutputTypeDef]


# SecurityServicePolicyDataTypeDef

### Type
- **Type**: typing.Literal['DNS_FIREWALL', 'IMPORT_NETWORK_FIREWALL', 'NETWORK_ACL_COMMON', 'NETWORK_FIREWALL', 'SECURITY_GROUPS_COMMON', 'SECURITY_GROUPS_CONTENT_AUDIT', 'SECURITY_GROUPS_USAGE_AUDIT', 'SHIELD_ADVANCED', 'THIRD_PARTY_FIREWALL', 'WAF', 'WAFV2']
- **Required**: Yes

### ManagedServiceData
- **Type**: typing.Optional[str]

### PolicyOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.PolicyOptionTypeDef]


# StatefulEngineOptionsTypeDef

### RuleOrder
- **Type**: typing.Optional[typing.Literal['DEFAULT_ACTION_ORDER', 'STRICT_ORDER']]

### StreamExceptionPolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP', 'FMS_IGNORE', 'REJECT']]


# StatefulRuleGroupTypeDef

### RuleGroupName
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Override
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fms_classes.NetworkFirewallStatefulRuleGroupOverrideTypeDef]


# StatelessRuleGroupTypeDef

### RuleGroupName
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.fms_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ThirdPartyFirewallFirewallPolicyTypeDef

### FirewallPolicyId
- **Type**: typing.Optional[str]

### FirewallPolicyName
- **Type**: typing.Optional[str]


# ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef

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


# ThirdPartyFirewallMissingFirewallViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### TargetViolationReason
- **Type**: typing.Optional[str]


# ThirdPartyFirewallMissingSubnetViolationTypeDef

### ViolationTarget
- **Type**: typing.Optional[str]

### VPC
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### TargetViolationReason
- **Type**: typing.Optional[str]


# ThirdPartyFirewallPolicyTypeDef

### FirewallDeploymentModel
- **Type**: typing.Optional[typing.Literal['CENTRALIZED', 'DISTRIBUTED']]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ViolationDetailTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.fms_classes.ResourceViolationTypeDef]
- **Required**: Yes

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fms_classes.TagTypeDef]]

### ResourceDescription
- **Type**: typing.Optional[str]


