# Detective Classes

# AcceptInvitationRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# AccountTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# AdministratorTypeDef

### AccountId
- **Type**: typing.Optional[str]

### GraphArn
- **Type**: typing.Optional[str]

### DelegationTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetGraphMemberDatasourcesRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetGraphMemberDatasourcesResponseTypeDef

### MemberDatasources
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.MembershipDatasourcesTypeDef]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetMembershipDatasourcesRequestTypeDef

### GraphArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetMembershipDatasourcesResponseTypeDef

### MembershipDatasources
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.MembershipDatasourcesTypeDef]
- **Required**: Yes

### UnprocessedGraphs
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.UnprocessedGraphTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGraphRequestTypeDef

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateGraphResponseTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMembersRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### Accounts
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.detective_classes.AccountTypeDef]
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]

### DisableEmailNotification
- **Type**: typing.Optional[bool]


# CreateMembersResponseTypeDef

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.MemberDetailTypeDef]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DatasourcePackageIngestDetailTypeDef

### DatasourcePackageIngestState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'STARTED', 'STOPPED']]

### LastIngestStateChange
- **Type**: typing.Optional[typing.Dict[typing.Literal['DISABLED', 'STARTED', 'STOPPED'], aws_resource_validator.pydantic_models.detective_classes.TimestampForCollectionTypeDef]]


# DatasourcePackageUsageInfoTypeDef

### VolumeUsageInBytes
- **Type**: typing.Optional[int]

### VolumeUsageUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# DateFilterTypeDef

### StartInclusive
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.TimestampTypeDef'>
- **Required**: Yes

### EndInclusive
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.TimestampTypeDef'>
- **Required**: Yes


# DeleteGraphRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMembersRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteMembersResponseTypeDef

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationConfigurationRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOrganizationConfigurationResponseTypeDef

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateMembershipRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableOrganizationAdminAccountRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# FilterCriteriaTypeDef

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.StringFilterTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.StringFilterTypeDef]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.StringFilterTypeDef]

### EntityArn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.StringFilterTypeDef]

### CreatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.DateFilterTypeDef]


# FlaggedIpAddressDetailTypeDef

### IpAddress
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['AWS_THREAT_INTELLIGENCE']]


# GetInvestigationRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInvestigationResponseTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityArn
- **Type**: <class 'str'>
- **Required**: Yes

### EntityType
- **Type**: typing.Literal['IAM_ROLE', 'IAM_USER']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ScopeStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ScopeEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'SUCCESSFUL']
- **Required**: Yes

### Severity
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMembersRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetMembersResponseTypeDef

### MemberDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.MemberDetailTypeDef]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GraphTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# ImpossibleTravelDetailTypeDef

### StartingIpAddress
- **Type**: typing.Optional[str]

### EndingIpAddress
- **Type**: typing.Optional[str]

### StartingLocation
- **Type**: typing.Optional[str]

### EndingLocation
- **Type**: typing.Optional[str]

### HourlyTimeDelta
- **Type**: typing.Optional[int]


# IndicatorDetailTypeDef

### TTPsObservedDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.TTPsObservedDetailTypeDef]

### ImpossibleTravelDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.ImpossibleTravelDetailTypeDef]

### FlaggedIpAddressDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.FlaggedIpAddressDetailTypeDef]

### NewGeolocationDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.NewGeolocationDetailTypeDef]

### NewAsoDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.NewAsoDetailTypeDef]

### NewUserAgentDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.NewUserAgentDetailTypeDef]

### RelatedFindingDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.RelatedFindingDetailTypeDef]

### RelatedFindingGroupDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.RelatedFindingGroupDetailTypeDef]


# IndicatorTypeDef

### IndicatorType
- **Type**: typing.Optional[typing.Literal['FLAGGED_IP_ADDRESS', 'IMPOSSIBLE_TRAVEL', 'NEW_ASO', 'NEW_GEOLOCATION', 'NEW_USER_AGENT', 'RELATED_FINDING', 'RELATED_FINDING_GROUP', 'TTP_OBSERVED']]

### IndicatorDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.IndicatorDetailTypeDef]


# InvestigationDetailTypeDef

### InvestigationId
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'SUCCESSFUL']]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### EntityArn
- **Type**: typing.Optional[str]

### EntityType
- **Type**: typing.Optional[typing.Literal['IAM_ROLE', 'IAM_USER']]


# ListDatasourcePackagesRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasourcePackagesResponseTypeDef

### DatasourcePackages
- **Type**: typing.Dict[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT'], aws_resource_validator.pydantic_models.detective_classes.DatasourcePackageIngestDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGraphsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGraphsResponseTypeDef

### GraphList
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.GraphTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndicatorsRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes

### IndicatorType
- **Type**: typing.Optional[typing.Literal['FLAGGED_IP_ADDRESS', 'IMPOSSIBLE_TRAVEL', 'NEW_ASO', 'NEW_GEOLOCATION', 'NEW_USER_AGENT', 'RELATED_FINDING', 'RELATED_FINDING_GROUP', 'TTP_OBSERVED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIndicatorsResponseTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes

### Indicators
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.IndicatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvestigationsRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.FilterCriteriaTypeDef]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective_classes.SortCriteriaTypeDef]


# ListInvestigationsResponseTypeDef

### InvestigationDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.InvestigationDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInvitationsResponseTypeDef

### Invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.MemberDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMembersResponseTypeDef

### MemberDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.MemberDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOrganizationAdminAccountsResponseTypeDef

### Administrators
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective_classes.AdministratorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MemberDetailTypeDef

### AccountId
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### GraphArn
- **Type**: typing.Optional[str]

### MasterId
- **Type**: typing.Optional[str]

### AdministratorId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED_BUT_DISABLED', 'ENABLED', 'INVITED', 'VERIFICATION_FAILED', 'VERIFICATION_IN_PROGRESS']]

### DisabledReason
- **Type**: typing.Optional[typing.Literal['VOLUME_TOO_HIGH', 'VOLUME_UNKNOWN']]

### InvitedTime
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### VolumeUsageInBytes
- **Type**: typing.Optional[int]

### VolumeUsageUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### PercentOfGraphUtilization
- **Type**: typing.Optional[float]

### PercentOfGraphUtilizationUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### InvitationType
- **Type**: typing.Optional[typing.Literal['INVITATION', 'ORGANIZATION']]

### VolumeUsageByDatasourcePackage
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT'], aws_resource_validator.pydantic_models.detective_classes.DatasourcePackageUsageInfoTypeDef]]

### DatasourcePackageIngestStates
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT'], typing.Literal['DISABLED', 'STARTED', 'STOPPED']]]


# MembershipDatasourcesTypeDef

### AccountId
- **Type**: typing.Optional[str]

### GraphArn
- **Type**: typing.Optional[str]

### DatasourcePackageIngestHistory
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT'], typing.Dict[typing.Literal['DISABLED', 'STARTED', 'STOPPED'], aws_resource_validator.pydantic_models.detective_classes.TimestampForCollectionTypeDef]]]


# NewAsoDetailTypeDef

### Aso
- **Type**: typing.Optional[str]

### IsNewForEntireAccount
- **Type**: typing.Optional[bool]


# NewGeolocationDetailTypeDef

### Location
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### IsNewForEntireAccount
- **Type**: typing.Optional[bool]


# NewUserAgentDetailTypeDef

### UserAgent
- **Type**: typing.Optional[str]

### IsNewForEntireAccount
- **Type**: typing.Optional[bool]


# RejectInvitationRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# RelatedFindingDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RelatedFindingGroupDetailTypeDef

### Id
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


# SortCriteriaTypeDef

### Field
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'SEVERITY', 'STATUS']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# StartInvestigationRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### EntityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ScopeStartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.TimestampTypeDef'>
- **Required**: Yes

### ScopeEndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.TimestampTypeDef'>
- **Required**: Yes


# StartInvestigationResponseTypeDef

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMonitoringMemberRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# StringFilterTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TTPsObservedDetailTypeDef

### Tactic
- **Type**: typing.Optional[str]

### Technique
- **Type**: typing.Optional[str]

### Procedure
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### APIName
- **Type**: typing.Optional[str]

### APISuccessCount
- **Type**: typing.Optional[int]

### APIFailureCount
- **Type**: typing.Optional[int]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampForCollectionTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnprocessedAccountTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# UnprocessedGraphTypeDef

### GraphArn
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasourcePackagesRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasourcePackages
- **Type**: typing.Sequence[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT']]
- **Required**: Yes


# UpdateInvestigationStateRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED']
- **Required**: Yes


# UpdateOrganizationConfigurationRequestTypeDef

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoEnable
- **Type**: typing.Optional[bool]


