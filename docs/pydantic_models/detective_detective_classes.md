# Detective Detective Classes

# AcceptInvitationRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# Account

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# Administrator

### AccountId
- **Type**: typing.Optional[str]

### GraphArn
- **Type**: typing.Optional[str]

### DelegationTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetGraphMemberDatasourcesRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetGraphMemberDatasourcesResponse

### MemberDatasources
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.MembershipDatasources]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetMembershipDatasourcesRequest

### GraphArns
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetMembershipDatasourcesResponse

### MembershipDatasources
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.MembershipDatasources]
- **Required**: Yes

### UnprocessedGraphs
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.UnprocessedGraph]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGraphRequest

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateGraphResponse

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMembersRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.Account]
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]

### DisableEmailNotification
- **Type**: typing.Optional[bool]


# CreateMembersResponse

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.MemberDetail]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# DatasourcePackageIngestDetail

### DatasourcePackageIngestState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'STARTED', 'STOPPED']]

### LastIngestStateChange
- **Type**: typing.Optional[typing.Dict[typing.Literal['DISABLED', 'STARTED', 'STOPPED'], aws_resource_validator.pydantic_models.detective.detective_classes.TimestampForCollection]]


# DatasourcePackageUsageInfo

### VolumeUsageInBytes
- **Type**: typing.Optional[int]

### VolumeUsageUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# DateFilter

### StartInclusive
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndInclusive
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# DeleteGraphRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMembersRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteMembersResponse

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationConfigurationRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOrganizationConfigurationResponse

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateMembershipRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# EnableOrganizationAdminAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# FilterCriteria

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective.detective_classes.StringFilter]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective.detective_classes.StringFilter]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective.detective_classes.StringFilter]

### EntityArn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective.detective_classes.StringFilter]

### CreatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.detective.detective_classes.DateFilter]


# FlaggedIpAddressDetail

### IpAddress
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['AWS_THREAT_INTELLIGENCE']]


# GetInvestigationRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInvestigationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# GetMembersRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# GetMembersResponse

### MemberDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.MemberDetail]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# Graph

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# ImpossibleTravelDetail

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


# Indicator

### IndicatorType
- **Type**: typing.Optional[typing.Literal['FLAGGED_IP_ADDRESS', 'IMPOSSIBLE_TRAVEL', 'NEW_ASO', 'NEW_GEOLOCATION', 'NEW_USER_AGENT', 'RELATED_FINDING', 'RELATED_FINDING_GROUP', 'TTP_OBSERVED']]

### IndicatorDetail
- **Type**: <class 'NoneType'>


# IndicatorDetail

### TTPsObservedDetail
- **Type**: <class 'NoneType'>

### ImpossibleTravelDetail
- **Type**: <class 'NoneType'>

### FlaggedIpAddressDetail
- **Type**: <class 'NoneType'>

### NewGeolocationDetail
- **Type**: <class 'NoneType'>

### NewAsoDetail
- **Type**: <class 'NoneType'>

### NewUserAgentDetail
- **Type**: <class 'NoneType'>

### RelatedFindingDetail
- **Type**: <class 'NoneType'>

### RelatedFindingGroupDetail
- **Type**: <class 'NoneType'>


# InvestigationDetail

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


# ListDatasourcePackagesRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasourcePackagesResponse

### DatasourcePackages
- **Type**: typing.Dict[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT'], aws_resource_validator.pydantic_models.detective.detective_classes.DatasourcePackageIngestDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGraphsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGraphsResponse

### GraphList
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.Graph]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndicatorsRequest

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


# ListIndicatorsResponse

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes

### Indicators
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.Indicator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvestigationsRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### FilterCriteria
- **Type**: <class 'NoneType'>

### SortCriteria
- **Type**: <class 'NoneType'>


# ListInvestigationsResponse

### InvestigationDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.InvestigationDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInvitationsResponse

### Invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.MemberDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMembersResponse

### MemberDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.MemberDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOrganizationAdminAccountsResponse

### Administrators
- **Type**: typing.List[aws_resource_validator.pydantic_models.detective.detective_classes.Administrator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# MemberDetail

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT'], aws_resource_validator.pydantic_models.detective.detective_classes.DatasourcePackageUsageInfo]]

### DatasourcePackageIngestStates
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT'], typing.Literal['DISABLED', 'STARTED', 'STOPPED']]]


# MembershipDatasources

### AccountId
- **Type**: typing.Optional[str]

### GraphArn
- **Type**: typing.Optional[str]

### DatasourcePackageIngestHistory
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT'], typing.Dict[typing.Literal['DISABLED', 'STARTED', 'STOPPED'], aws_resource_validator.pydantic_models.detective.detective_classes.TimestampForCollection]]]


# NewAsoDetail

### Aso
- **Type**: typing.Optional[str]

### IsNewForEntireAccount
- **Type**: typing.Optional[bool]


# NewGeolocationDetail

### Location
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### IsNewForEntireAccount
- **Type**: typing.Optional[bool]


# NewUserAgentDetail

### UserAgent
- **Type**: typing.Optional[str]

### IsNewForEntireAccount
- **Type**: typing.Optional[bool]


# RejectInvitationRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes


# RelatedFindingDetail

### Arn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# RelatedFindingGroupDetail

### Id
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


# SortCriteria

### Field
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'SEVERITY', 'STATUS']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# StartInvestigationRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### EntityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ScopeStartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ScopeEndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# StartInvestigationResponse

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.detective.detective_classes.ResponseMetadata'>
- **Required**: Yes


# StartMonitoringMemberRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# StringFilter

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TTPsObservedDetail

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


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TimestampForCollection

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# UnprocessedAccount

### AccountId
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# UnprocessedGraph

### GraphArn
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDatasourcePackagesRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasourcePackages
- **Type**: typing.List[typing.Literal['ASFF_SECURITYHUB_FINDING', 'DETECTIVE_CORE', 'EKS_AUDIT']]
- **Required**: Yes


# UpdateInvestigationStateRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvestigationId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED']
- **Required**: Yes


# UpdateOrganizationConfigurationRequest

### GraphArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoEnable
- **Type**: typing.Optional[bool]


