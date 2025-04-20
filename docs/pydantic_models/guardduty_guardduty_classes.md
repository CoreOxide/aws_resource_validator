# Guardduty Guardduty Classes

# AcceptAdministratorInvitationRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AdministratorId
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptInvitationRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MasterId
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# AccessControlList

### AllowsPublicReadAccess
- **Type**: typing.Optional[bool]

### AllowsPublicWriteAccess
- **Type**: typing.Optional[bool]


# AccessKey

### PrincipalId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[str]


# AccessKeyDetails

### AccessKeyId
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[str]


# Account

### Uid
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AccountDetail

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes


# AccountFreeTrialInfo

### AccountId
- **Type**: typing.Optional[str]

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourcesFreeTrial]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FreeTrialFeatureConfigurationResult]]


# AccountLevelPermissions

### BlockPublicAccess
- **Type**: <class 'NoneType'>


# AccountStatistics

### AccountId
- **Type**: typing.Optional[str]

### LastGeneratedAt
- **Type**: typing.Optional[datetime.datetime]

### TotalFindings
- **Type**: typing.Optional[int]


# Action

### ActionType
- **Type**: typing.Optional[str]

### AwsApiCallAction
- **Type**: <class 'NoneType'>

### DnsRequestAction
- **Type**: <class 'NoneType'>

### NetworkConnectionAction
- **Type**: <class 'NoneType'>

### PortProbeAction
- **Type**: <class 'NoneType'>

### KubernetesApiCallAction
- **Type**: <class 'NoneType'>

### RdsLoginAttemptAction
- **Type**: <class 'NoneType'>

### KubernetesPermissionCheckedDetails
- **Type**: <class 'NoneType'>

### KubernetesRoleBindingDetails
- **Type**: <class 'NoneType'>

### KubernetesRoleDetails
- **Type**: <class 'NoneType'>


# Actor

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'NoneType'>

### Session
- **Type**: <class 'NoneType'>


# AddonDetails

### AddonVersion
- **Type**: typing.Optional[str]

### AddonStatus
- **Type**: typing.Optional[str]


# AdminAccount

### AdminAccountId
- **Type**: typing.Optional[str]

### AdminStatus
- **Type**: typing.Optional[typing.Literal['DISABLE_IN_PROGRESS', 'ENABLED']]


# Administrator

### AccountId
- **Type**: typing.Optional[str]

### InvitationId
- **Type**: typing.Optional[str]

### RelationshipStatus
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[str]


# AgentDetails

### Version
- **Type**: typing.Optional[str]


# Anomaly

### Profiles
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.AnomalyObject]]]]

### Unusual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.AnomalyUnusual]


# AnomalyObject

### ProfileType
- **Type**: typing.Optional[typing.Literal['FREQUENCY']]

### ProfileSubtype
- **Type**: typing.Optional[typing.Literal['FREQUENT', 'INFREQUENT', 'RARE', 'UNSEEN']]

### Observations
- **Type**: <class 'NoneType'>


# AnomalyUnusual

### Behavior
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.AnomalyObject]]]


# ArchiveFindingsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingIds
- **Type**: typing.List[str]
- **Required**: Yes


# AutonomousSystem

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Number
- **Type**: <class 'int'>
- **Required**: Yes


# AwsApiCallAction

### Api
- **Type**: typing.Optional[str]

### CallerType
- **Type**: typing.Optional[str]

### DomainDetails
- **Type**: <class 'NoneType'>

### ErrorCode
- **Type**: typing.Optional[str]

### UserAgent
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: <class 'NoneType'>

### ServiceName
- **Type**: typing.Optional[str]

### RemoteAccountDetails
- **Type**: <class 'NoneType'>

### AffectedResources
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockPublicAccess

### IgnorePublicAcls
- **Type**: typing.Optional[bool]

### RestrictPublicBuckets
- **Type**: typing.Optional[bool]

### BlockPublicAcls
- **Type**: typing.Optional[bool]

### BlockPublicPolicy
- **Type**: typing.Optional[bool]


# BucketLevelPermissions

### AccessControlList
- **Type**: <class 'NoneType'>

### BucketPolicy
- **Type**: <class 'NoneType'>

### BlockPublicAccess
- **Type**: <class 'NoneType'>


# BucketPolicy

### AllowsPublicReadAccess
- **Type**: typing.Optional[bool]

### AllowsPublicWriteAccess
- **Type**: typing.Optional[bool]


# City

### CityName
- **Type**: typing.Optional[str]


# CloudTrailConfigurationResult

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# Condition

### Eq
- **Type**: typing.Optional[typing.List[str]]

### Neq
- **Type**: typing.Optional[typing.List[str]]

### Gt
- **Type**: typing.Optional[int]

### Gte
- **Type**: typing.Optional[int]

### Lt
- **Type**: typing.Optional[int]

### Lte
- **Type**: typing.Optional[int]

### Equals
- **Type**: typing.Optional[typing.List[str]]

### NotEquals
- **Type**: typing.Optional[typing.List[str]]

### GreaterThan
- **Type**: typing.Optional[int]

### GreaterThanOrEqual
- **Type**: typing.Optional[int]

### LessThan
- **Type**: typing.Optional[int]

### LessThanOrEqual
- **Type**: typing.Optional[int]


# ConditionOutput

### Eq
- **Type**: typing.Optional[typing.List[str]]

### Neq
- **Type**: typing.Optional[typing.List[str]]

### Gt
- **Type**: typing.Optional[int]

### Gte
- **Type**: typing.Optional[int]

### Lt
- **Type**: typing.Optional[int]

### Lte
- **Type**: typing.Optional[int]

### Equals
- **Type**: typing.Optional[typing.List[str]]

### NotEquals
- **Type**: typing.Optional[typing.List[str]]

### GreaterThan
- **Type**: typing.Optional[int]

### GreaterThanOrEqual
- **Type**: typing.Optional[int]

### LessThan
- **Type**: typing.Optional[int]

### LessThanOrEqual
- **Type**: typing.Optional[int]


# Container

### ContainerRuntime
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### ImagePrefix
- **Type**: typing.Optional[str]

### VolumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.VolumeMount]]

### SecurityContext
- **Type**: <class 'NoneType'>


# ContainerInstanceDetails

### CoveredContainerInstances
- **Type**: typing.Optional[int]

### CompatibleContainerInstances
- **Type**: typing.Optional[int]


# Country

### CountryCode
- **Type**: typing.Optional[str]

### CountryName
- **Type**: typing.Optional[str]


# CoverageEc2InstanceDetails

### InstanceId
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### AgentDetails
- **Type**: <class 'NoneType'>

### ManagementType
- **Type**: typing.Optional[typing.Literal['AUTO_MANAGED', 'DISABLED', 'MANUAL']]


# CoverageEcsClusterDetails

### ClusterName
- **Type**: typing.Optional[str]

### FargateDetails
- **Type**: <class 'NoneType'>

### ContainerInstanceDetails
- **Type**: <class 'NoneType'>


# CoverageEksClusterDetails

### ClusterName
- **Type**: typing.Optional[str]

### CoveredNodes
- **Type**: typing.Optional[int]

### CompatibleNodes
- **Type**: typing.Optional[int]

### AddonDetails
- **Type**: <class 'NoneType'>

### ManagementType
- **Type**: typing.Optional[typing.Literal['AUTO_MANAGED', 'DISABLED', 'MANUAL']]


# CoverageFilterCondition

### Equals
- **Type**: typing.Optional[typing.List[str]]

### NotEquals
- **Type**: typing.Optional[typing.List[str]]


# CoverageFilterCriteria

### FilterCriterion
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageFilterCriterion]]


# CoverageFilterCriterion

### CriterionKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ADDON_VERSION', 'AGENT_VERSION', 'CLUSTER_ARN', 'CLUSTER_NAME', 'COVERAGE_STATUS', 'ECS_CLUSTER_NAME', 'EKS_CLUSTER_NAME', 'INSTANCE_ID', 'MANAGEMENT_TYPE', 'RESOURCE_TYPE']]

### FilterCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageFilterCondition]


# CoverageResource

### ResourceId
- **Type**: typing.Optional[str]

### DetectorId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageResourceDetails]

### CoverageStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### Issue
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# CoverageResourceDetails

### EksClusterDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageEksClusterDetails]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2', 'ECS', 'EKS']]

### EcsClusterDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageEcsClusterDetails]

### Ec2InstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageEc2InstanceDetails]


# CoverageSortCriteria

### AttributeName
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ADDON_VERSION', 'CLUSTER_NAME', 'COVERAGE_STATUS', 'ECS_CLUSTER_NAME', 'EKS_CLUSTER_NAME', 'INSTANCE_ID', 'ISSUE', 'UPDATED_AT']]

### OrderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# CoverageStatistics

### CountByResourceType
- **Type**: typing.Optional[typing.Dict[typing.Literal['EC2', 'ECS', 'EKS'], int]]

### CountByCoverageStatus
- **Type**: typing.Optional[typing.Dict[typing.Literal['HEALTHY', 'UNHEALTHY'], int]]


# CreateDetectorRequest

### Enable
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### FindingPublishingFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']]

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceConfigurations]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DetectorFeatureConfiguration]]


# CreateDetectorResponse

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### UnprocessedDataSources
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedDataSourcesResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFilterRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FindingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteria, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteriaOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'NOOP']]

### Rank
- **Type**: typing.Optional[int]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateFilterResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIPSetRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['ALIEN_VAULT', 'FIRE_EYE', 'OTX_CSV', 'PROOF_POINT', 'STIX', 'TXT']
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### Activate
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateIPSetResponse

### IpSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMalwareProtectionPlanRequest

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedResource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CreateProtectedResource, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CreateProtectedResourceOutput]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionPlanActions]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMalwareProtectionPlanResponse

### MalwareProtectionPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMembersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.AccountDetail]
- **Required**: Yes


# CreateMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProtectedResource

### S3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CreateS3BucketResource]


# CreateProtectedResourceOutput

### S3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CreateS3BucketResourceOutput]


# CreatePublishingDestinationRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationType
- **Type**: typing.Literal['S3']
- **Required**: Yes

### DestinationProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DestinationProperties'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreatePublishingDestinationResponse

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# CreateS3BucketResource

### BucketName
- **Type**: typing.Optional[str]

### ObjectPrefixes
- **Type**: typing.Optional[typing.List[str]]


# CreateS3BucketResourceOutput

### BucketName
- **Type**: typing.Optional[str]

### ObjectPrefixes
- **Type**: typing.Optional[typing.List[str]]


# CreateSampleFindingsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingTypes
- **Type**: typing.Optional[typing.List[str]]


# CreateThreatIntelSetRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['ALIEN_VAULT', 'FIRE_EYE', 'OTX_CSV', 'PROOF_POINT', 'STIX', 'TXT']
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### Activate
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateThreatIntelSetResponse

### ThreatIntelSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# DNSLogsConfigurationResult

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# DataSourceConfigurations

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.S3LogsConfiguration]

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.KubernetesConfiguration]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionConfiguration]


# DataSourceConfigurationsResult

### CloudTrail
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CloudTrailConfigurationResult'>
- **Required**: Yes

### DNSLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DNSLogsConfigurationResult'>
- **Required**: Yes

### FlowLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FlowLogsConfigurationResult'>
- **Required**: Yes

### S3Logs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.S3LogsConfigurationResult'>
- **Required**: Yes

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.KubernetesConfigurationResult]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionConfigurationResult]


# DataSourceFreeTrial

### FreeTrialDaysRemaining
- **Type**: typing.Optional[int]


# DataSourcesFreeTrial

### CloudTrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceFreeTrial]

### DnsLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceFreeTrial]

### FlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceFreeTrial]

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceFreeTrial]

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.KubernetesDataSourceFreeTrial]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionDataSourceFreeTrial]


# DateStatistics

### Date
- **Type**: typing.Optional[datetime.datetime]

### LastGeneratedAt
- **Type**: typing.Optional[datetime.datetime]

### Severity
- **Type**: typing.Optional[float]

### TotalFindings
- **Type**: typing.Optional[int]


# DeclineInvitationsRequest

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# DeclineInvitationsResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# DefaultServerSideEncryption

### EncryptionType
- **Type**: typing.Optional[str]

### KmsMasterKeyArn
- **Type**: typing.Optional[str]


# DeleteDetectorRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFilterRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIPSetRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### IpSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInvitationsRequest

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteInvitationsResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMalwareProtectionPlanRequest

### MalwareProtectionPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMembersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePublishingDestinationRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThreatIntelSetRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ThreatIntelSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMalwareScansRequest

### DetectorId
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


# DescribeMalwareScansRequestPaginate

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterCriteria
- **Type**: <class 'NoneType'>

### SortCriteria
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# DescribeMalwareScansResponse

### Scans
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Scan]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigurationRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigurationResponse

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### MemberAccountLimitReached
- **Type**: <class 'bool'>
- **Required**: Yes

### DataSources
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationDataSourceConfigurationsResult'>
- **Required**: Yes

### Features
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationFeatureConfigurationResult]
- **Required**: Yes

### AutoEnableOrganizationMembers
- **Type**: typing.Literal['ALL', 'NEW', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePublishingDestinationRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePublishingDestinationResponse

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationType
- **Type**: typing.Literal['S3']
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING_VERIFICATION', 'PUBLISHING', 'STOPPED', 'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY']
- **Required**: Yes

### PublishingFailureStartTimestamp
- **Type**: <class 'int'>
- **Required**: Yes

### DestinationProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DestinationProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationType
- **Type**: typing.Literal['S3']
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING_VERIFICATION', 'PUBLISHING', 'STOPPED', 'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY']
- **Required**: Yes


# DestinationProperties

### DestinationArn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# Detection

### Anomaly
- **Type**: <class 'NoneType'>

### Sequence
- **Type**: <class 'NoneType'>


# DetectorAdditionalConfiguration

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DetectorAdditionalConfigurationResult

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# DetectorFeatureConfiguration

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DetectorAdditionalConfiguration]]


# DetectorFeatureConfigurationResult

### Name
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DetectorAdditionalConfigurationResult]]


# DisableOrganizationAdminAccountRequest

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFromAdministratorAccountRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFromMasterAccountRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMembersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# DisassociateMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# DnsRequestAction

### Domain
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]

### Blocked
- **Type**: typing.Optional[bool]

### DomainWithSuffix
- **Type**: typing.Optional[str]


# DomainDetails

### Domain
- **Type**: typing.Optional[str]


# EbsVolumeDetails

### ScannedVolumeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.VolumeDetail]]

### SkippedVolumeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.VolumeDetail]]


# EbsVolumeScanDetails

### ScanId
- **Type**: typing.Optional[str]

### ScanStartedAt
- **Type**: typing.Optional[datetime.datetime]

### ScanCompletedAt
- **Type**: typing.Optional[datetime.datetime]

### TriggerFindingId
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[str]]

### ScanDetections
- **Type**: <class 'NoneType'>

### ScanType
- **Type**: typing.Optional[typing.Literal['GUARDDUTY_INITIATED', 'ON_DEMAND']]


# EbsVolumesResult

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Reason
- **Type**: typing.Optional[str]


# Ec2Instance

### AvailabilityZone
- **Type**: typing.Optional[str]

### ImageDescription
- **Type**: typing.Optional[str]

### InstanceState
- **Type**: typing.Optional[str]

### IamInstanceProfile
- **Type**: <class 'NoneType'>

### InstanceType
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[str]

### ProductCodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ProductCode]]

### Ec2NetworkInterfaceUids
- **Type**: typing.Optional[typing.List[str]]


# Ec2NetworkInterface

### Ipv6Addresses
- **Type**: typing.Optional[typing.List[str]]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PrivateIpAddressDetails]]

### PublicIp
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.SecurityGroup]]

### SubNetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# EcsClusterDetails

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### ActiveServicesCount
- **Type**: typing.Optional[int]

### RegisteredContainerInstancesCount
- **Type**: typing.Optional[int]

### RunningTasksCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]

### TaskDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.EcsTaskDetails]


# EcsTaskDetails

### Arn
- **Type**: typing.Optional[str]

### DefinitionArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### TaskCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]

### StartedBy
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Volume]]

### Containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Container]]

### Group
- **Type**: typing.Optional[str]

### LaunchType
- **Type**: typing.Optional[str]


# EksClusterDetails

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# EnableOrganizationAdminAccountRequest

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# Evidence

### ThreatIntelligenceDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ThreatIntelligenceDetail]]


# FargateDetails

### Issues
- **Type**: typing.Optional[typing.List[str]]

### ManagementType
- **Type**: typing.Optional[typing.Literal['AUTO_MANAGED', 'DISABLED', 'MANUAL']]


# FilterCondition

### EqualsValue
- **Type**: typing.Optional[str]

### GreaterThan
- **Type**: typing.Optional[int]

### LessThan
- **Type**: typing.Optional[int]


# FilterCriteria

### FilterCriterion
- **Type**: typing.Optional[typing.List[NoneType]]


# FilterCriterion

### CriterionKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'EC2_INSTANCE_ARN', 'GUARDDUTY_FINDING_ID', 'SCAN_ID', 'SCAN_START_TIME', 'SCAN_STATUS', 'SCAN_TYPE']]

### FilterCondition
- **Type**: <class 'NoneType'>


# Finding

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Resource'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Severity
- **Type**: <class 'float'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Confidence
- **Type**: typing.Optional[float]

### Description
- **Type**: typing.Optional[str]

### Partition
- **Type**: typing.Optional[str]

### Service
- **Type**: <class 'NoneType'>

### Title
- **Type**: typing.Optional[str]

### AssociatedAttackSequenceArn
- **Type**: typing.Optional[str]


# FindingCriteria

### Criterion
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Condition]]


# FindingCriteriaOutput

### Criterion
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ConditionOutput]]


# FindingStatistics

### CountBySeverity
- **Type**: typing.Optional[typing.Dict[str, int]]

### GroupedByAccount
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.AccountStatistics]]

### GroupedByDate
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DateStatistics]]

### GroupedByFindingType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingTypeStatistics]]

### GroupedByResource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResourceStatistics]]

### GroupedBySeverity
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.SeverityStatistics]]


# FindingTypeStatistics

### FindingType
- **Type**: typing.Optional[str]

### LastGeneratedAt
- **Type**: typing.Optional[datetime.datetime]

### TotalFindings
- **Type**: typing.Optional[int]


# FlowLogsConfigurationResult

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# FreeTrialFeatureConfigurationResult

### Name
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EC2_RUNTIME_MONITORING', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FARGATE_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'S3_DATA_EVENTS']]

### FreeTrialDaysRemaining
- **Type**: typing.Optional[int]


# GeoLocation

### Lat
- **Type**: typing.Optional[float]

### Lon
- **Type**: typing.Optional[float]


# GetAdministratorAccountRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdministratorAccountResponse

### Administrator
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Administrator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetCoverageStatisticsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### StatisticsType
- **Type**: typing.List[typing.Literal['COUNT_BY_COVERAGE_STATUS', 'COUNT_BY_RESOURCE_TYPE']]
- **Required**: Yes

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageFilterCriteria]


# GetCoverageStatisticsResponse

### CoverageStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetDetectorRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDetectorResponse

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### FindingPublishingFrequency
- **Type**: typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']
- **Required**: Yes

### ServiceRole
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DataSources
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceConfigurationsResult'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Features
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DetectorFeatureConfigurationResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetFilterRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes


# GetFilterResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['ARCHIVE', 'NOOP']
- **Required**: Yes

### Rank
- **Type**: <class 'int'>
- **Required**: Yes

### FindingCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteriaOutput'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingIds
- **Type**: typing.List[str]
- **Required**: Yes

### SortCriteria
- **Type**: <class 'NoneType'>


# GetFindingsResponse

### Findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Finding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingsStatisticsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingStatisticTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COUNT_BY_SEVERITY']]]

### FindingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteria, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteriaOutput, NoneType]

### GroupBy
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'DATE', 'FINDING_TYPE', 'RESOURCE', 'SEVERITY']]

### OrderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### MaxResults
- **Type**: typing.Optional[int]


# GetFindingsStatisticsResponse

### FindingStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetIPSetRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### IpSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIPSetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['ALIEN_VAULT', 'FIRE_EYE', 'OTX_CSV', 'PROOF_POINT', 'STIX', 'TXT']
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'DEACTIVATING', 'DELETED', 'DELETE_PENDING', 'ERROR', 'INACTIVE']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetInvitationsCountResponse

### InvitationsCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetMalwareProtectionPlanRequest

### MalwareProtectionPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMalwareProtectionPlanResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedResource
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CreateProtectedResourceOutput'>
- **Required**: Yes

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionPlanActions'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR', 'WARNING']
- **Required**: Yes

### StatusReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionPlanStatusReason]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetMalwareScanSettingsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMalwareScanSettingsResponse

### ScanResourceCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanResourceCriteriaOutput'>
- **Required**: Yes

### EbsSnapshotPreservation
- **Type**: typing.Literal['NO_RETENTION', 'RETENTION_WITH_FINDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetMasterAccountRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMasterAccountResponse

### Master
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Master'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetMemberDetectorsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# GetMemberDetectorsResponse

### MemberDataSourceConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MemberDataSourceConfiguration]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetMembersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# GetMembersResponse

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Member]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetOrganizationStatisticsResponse

### OrganizationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetRemainingFreeTrialDaysRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.List[str]]


# GetRemainingFreeTrialDaysResponse

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.AccountFreeTrialInfo]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetThreatIntelSetRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ThreatIntelSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetThreatIntelSetResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['ALIEN_VAULT', 'FIRE_EYE', 'OTX_CSV', 'PROOF_POINT', 'STIX', 'TXT']
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'DEACTIVATING', 'DELETED', 'DELETE_PENDING', 'ERROR', 'INACTIVE']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# GetUsageStatisticsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### UsageStatisticType
- **Type**: typing.Literal['SUM_BY_ACCOUNT', 'SUM_BY_DATA_SOURCE', 'SUM_BY_FEATURES', 'SUM_BY_RESOURCE', 'TOP_ACCOUNTS_BY_FEATURE', 'TOP_RESOURCES']
- **Required**: Yes

### UsageCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageCriteria'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetUsageStatisticsResponse

### UsageStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# HighestSeverityThreatDetails

### Severity
- **Type**: typing.Optional[str]

### ThreatName
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]


# HostPath

### Path
- **Type**: typing.Optional[str]


# IamInstanceProfile

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# ImpersonatedUser

### Username
- **Type**: typing.Optional[str]

### Groups
- **Type**: typing.Optional[typing.List[str]]


# Indicator

### Key
- **Type**: typing.Literal['ATTACK_TACTIC', 'ATTACK_TECHNIQUE', 'HIGH_RISK_API', 'MALICIOUS_IP', 'SUSPICIOUS_NETWORK', 'SUSPICIOUS_USER_AGENT', 'TOR_IP', 'UNUSUAL_API_FOR_ACCOUNT', 'UNUSUAL_ASN_FOR_ACCOUNT', 'UNUSUAL_ASN_FOR_USER']
- **Required**: Yes

### Values
- **Type**: typing.Optional[typing.List[str]]

### Title
- **Type**: typing.Optional[str]


# InstanceDetails

### AvailabilityZone
- **Type**: typing.Optional[str]

### IamInstanceProfile
- **Type**: <class 'NoneType'>

### ImageDescription
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceState
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]

### LaunchTime
- **Type**: typing.Optional[str]

### NetworkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.NetworkInterface]]

### Platform
- **Type**: typing.Optional[str]

### ProductCodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ProductCode]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]


# Invitation

### AccountId
- **Type**: typing.Optional[str]

### InvitationId
- **Type**: typing.Optional[str]

### RelationshipStatus
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[str]


# InviteMembersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### DisableEmailNotification
- **Type**: typing.Optional[bool]

### Message
- **Type**: typing.Optional[str]


# InviteMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# ItemPath

### NestedItemPath
- **Type**: typing.Optional[str]

### Hash
- **Type**: typing.Optional[str]


# KubernetesApiCallAction

### RequestUri
- **Type**: typing.Optional[str]

### Verb
- **Type**: typing.Optional[str]

### SourceIps
- **Type**: typing.Optional[typing.List[str]]

### UserAgent
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: <class 'NoneType'>

### StatusCode
- **Type**: typing.Optional[int]

### Parameters
- **Type**: typing.Optional[str]

### Resource
- **Type**: typing.Optional[str]

### Subresource
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### ResourceName
- **Type**: typing.Optional[str]


# KubernetesAuditLogsConfiguration

### Enable
- **Type**: <class 'bool'>
- **Required**: Yes


# KubernetesAuditLogsConfigurationResult

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# KubernetesConfiguration

### AuditLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.KubernetesAuditLogsConfiguration'>
- **Required**: Yes


# KubernetesConfigurationResult

### AuditLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.KubernetesAuditLogsConfigurationResult'>
- **Required**: Yes


# KubernetesDataSourceFreeTrial

### AuditLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceFreeTrial]


# KubernetesDetails

### KubernetesUserDetails
- **Type**: <class 'NoneType'>

### KubernetesWorkloadDetails
- **Type**: <class 'NoneType'>


# KubernetesPermissionCheckedDetails

### Verb
- **Type**: typing.Optional[str]

### Resource
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Allowed
- **Type**: typing.Optional[bool]


# KubernetesRoleBindingDetails

### Kind
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Uid
- **Type**: typing.Optional[str]

### RoleRefName
- **Type**: typing.Optional[str]

### RoleRefKind
- **Type**: typing.Optional[str]


# KubernetesRoleDetails

### Kind
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Uid
- **Type**: typing.Optional[str]


# KubernetesUserDetails

### Username
- **Type**: typing.Optional[str]

### Uid
- **Type**: typing.Optional[str]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### SessionName
- **Type**: typing.Optional[typing.List[str]]

### ImpersonatedUser
- **Type**: <class 'NoneType'>


# KubernetesWorkloadDetails

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Uid
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### HostNetwork
- **Type**: typing.Optional[bool]

### Containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Container]]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Volume]]

### ServiceAccountName
- **Type**: typing.Optional[str]

### HostIPC
- **Type**: typing.Optional[bool]

### HostPID
- **Type**: typing.Optional[bool]


# LambdaDetails

### FunctionArn
- **Type**: typing.Optional[str]

### FunctionName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LastModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### RevisionId
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]


# LineageObject

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### NamespacePid
- **Type**: typing.Optional[int]

### UserId
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### Pid
- **Type**: typing.Optional[int]

### Uuid
- **Type**: typing.Optional[str]

### ExecutablePath
- **Type**: typing.Optional[str]

### Euid
- **Type**: typing.Optional[int]

### ParentUuid
- **Type**: typing.Optional[str]


# ListCoverageRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageFilterCriteria]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageSortCriteria]


# ListCoverageRequestPaginate

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageFilterCriteria]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageSortCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListCoverageResponse

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.CoverageResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDetectorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDetectorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListDetectorsResponse

### DetectorIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFiltersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFiltersRequestPaginate

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListFiltersResponse

### FilterNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFindingsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteria, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteriaOutput, NoneType]

### SortCriteria
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFindingsRequestPaginate

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteria, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteriaOutput, NoneType]

### SortCriteria
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListFindingsResponse

### FindingIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIPSetsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIPSetsRequestPaginate

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListIPSetsResponse

### IpSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListInvitationsResponse

### Invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Invitation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMalwareProtectionPlansRequest

### NextToken
- **Type**: typing.Optional[str]


# ListMalwareProtectionPlansResponse

### MalwareProtectionPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionPlanSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### OnlyAssociated
- **Type**: typing.Optional[str]


# ListMembersRequestPaginate

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### OnlyAssociated
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListMembersResponse

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Member]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListOrganizationAdminAccountsResponse

### AdminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.AdminAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPublishingDestinationsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPublishingDestinationsResponse

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Destination]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# ListThreatIntelSetsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListThreatIntelSetsRequestPaginate

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PaginatorConfig]


# ListThreatIntelSetsResponse

### ThreatIntelSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocalIpDetails

### IpAddressV4
- **Type**: typing.Optional[str]

### IpAddressV6
- **Type**: typing.Optional[str]


# LocalPortDetails

### Port
- **Type**: typing.Optional[int]

### PortName
- **Type**: typing.Optional[str]


# LoginAttribute

### User
- **Type**: typing.Optional[str]

### Application
- **Type**: typing.Optional[str]

### FailedLoginAttempts
- **Type**: typing.Optional[int]

### SuccessfulLoginAttempts
- **Type**: typing.Optional[int]


# MalwareProtectionConfiguration

### ScanEc2InstanceWithFindings
- **Type**: <class 'NoneType'>


# MalwareProtectionConfigurationResult

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanEc2InstanceWithFindingsResult]

### ServiceRole
- **Type**: typing.Optional[str]


# MalwareProtectionDataSourceFreeTrial

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceFreeTrial]


# MalwareProtectionPlanActions

### Tagging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionPlanTaggingAction]


# MalwareProtectionPlanStatusReason

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# MalwareProtectionPlanSummary

### MalwareProtectionPlanId
- **Type**: typing.Optional[str]


# MalwareProtectionPlanTaggingAction

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MalwareScanDetails

### Threats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Threat]]


# Master

### AccountId
- **Type**: typing.Optional[str]

### InvitationId
- **Type**: typing.Optional[str]

### RelationshipStatus
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[str]


# Member

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MasterId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### RelationshipStatus
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DetectorId
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[str]

### AdministratorId
- **Type**: typing.Optional[str]


# MemberAdditionalConfiguration

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MemberAdditionalConfigurationResult

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# MemberDataSourceConfiguration

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceConfigurationsResult]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MemberFeaturesConfigurationResult]]


# MemberFeaturesConfiguration

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MemberAdditionalConfiguration]]


# MemberFeaturesConfigurationResult

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MemberAdditionalConfigurationResult]]


# NetworkConnection

### Direction
- **Type**: typing.Literal['INBOUND', 'OUTBOUND']
- **Required**: Yes


# NetworkConnectionAction

### Blocked
- **Type**: typing.Optional[bool]

### ConnectionDirection
- **Type**: typing.Optional[str]

### LocalPortDetails
- **Type**: <class 'NoneType'>

### Protocol
- **Type**: typing.Optional[str]

### LocalIpDetails
- **Type**: <class 'NoneType'>

### LocalNetworkInterface
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: <class 'NoneType'>

### RemotePortDetails
- **Type**: <class 'NoneType'>


# NetworkEndpoint

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Ip
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.NetworkGeoLocation]

### AutonomousSystem
- **Type**: <class 'NoneType'>

### Connection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.NetworkConnection]


# NetworkGeoLocation

### City
- **Type**: <class 'str'>
- **Required**: Yes

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### Latitude
- **Type**: <class 'float'>
- **Required**: Yes

### Longitude
- **Type**: <class 'float'>
- **Required**: Yes


# NetworkInterface

### Ipv6Addresses
- **Type**: typing.Optional[typing.List[str]]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### PrivateDnsName
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PrivateIpAddressDetails]]

### PublicDnsName
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.SecurityGroup]]

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# Observations

### Text
- **Type**: typing.Optional[typing.List[str]]


# Organization

### Asn
- **Type**: typing.Optional[str]

### AsnOrg
- **Type**: typing.Optional[str]

### Isp
- **Type**: typing.Optional[str]

### Org
- **Type**: typing.Optional[str]


# OrganizationAdditionalConfiguration

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### AutoEnable
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]


# OrganizationAdditionalConfigurationResult

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### AutoEnable
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]


# OrganizationDataSourceConfigurations

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationS3LogsConfiguration]

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationKubernetesConfiguration]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationMalwareProtectionConfiguration]


# OrganizationDataSourceConfigurationsResult

### S3Logs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationS3LogsConfigurationResult'>
- **Required**: Yes

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationKubernetesConfigurationResult]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationMalwareProtectionConfigurationResult]


# OrganizationDetails

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### OrganizationStatistics
- **Type**: <class 'NoneType'>


# OrganizationEbsVolumes

### AutoEnable
- **Type**: typing.Optional[bool]


# OrganizationEbsVolumesResult

### AutoEnable
- **Type**: typing.Optional[bool]


# OrganizationFeatureConfiguration

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### AutoEnable
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationAdditionalConfiguration]]


# OrganizationFeatureConfigurationResult

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### AutoEnable
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationAdditionalConfigurationResult]]


# OrganizationFeatureStatistics

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### EnabledAccountsCount
- **Type**: typing.Optional[int]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationFeatureStatisticsAdditionalConfiguration]]


# OrganizationFeatureStatisticsAdditionalConfiguration

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### EnabledAccountsCount
- **Type**: typing.Optional[int]


# OrganizationKubernetesAuditLogsConfiguration

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# OrganizationKubernetesAuditLogsConfigurationResult

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# OrganizationKubernetesConfiguration

### AuditLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationKubernetesAuditLogsConfiguration'>
- **Required**: Yes


# OrganizationKubernetesConfigurationResult

### AuditLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationKubernetesAuditLogsConfigurationResult'>
- **Required**: Yes


# OrganizationMalwareProtectionConfiguration

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationScanEc2InstanceWithFindings]


# OrganizationMalwareProtectionConfigurationResult

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationScanEc2InstanceWithFindingsResult]


# OrganizationS3LogsConfiguration

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# OrganizationS3LogsConfigurationResult

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# OrganizationScanEc2InstanceWithFindings

### EbsVolumes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationEbsVolumes]


# OrganizationScanEc2InstanceWithFindingsResult

### EbsVolumes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationEbsVolumesResult]


# OrganizationStatistics

### TotalAccountsCount
- **Type**: typing.Optional[int]

### MemberAccountsCount
- **Type**: typing.Optional[int]

### ActiveAccountsCount
- **Type**: typing.Optional[int]

### EnabledAccountsCount
- **Type**: typing.Optional[int]

### CountByFeature
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationFeatureStatistics]]


# Owner

### Id
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionConfiguration

### BucketLevelPermissions
- **Type**: <class 'NoneType'>

### AccountLevelPermissions
- **Type**: <class 'NoneType'>


# PortProbeAction

### Blocked
- **Type**: typing.Optional[bool]

### PortProbeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PortProbeDetail]]


# PortProbeDetail

### LocalPortDetails
- **Type**: <class 'NoneType'>

### LocalIpDetails
- **Type**: <class 'NoneType'>

### RemoteIpDetails
- **Type**: <class 'NoneType'>


# PrivateIpAddressDetails

### PrivateDnsName
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]


# ProcessDetails

### Name
- **Type**: typing.Optional[str]

### ExecutablePath
- **Type**: typing.Optional[str]

### ExecutableSha256
- **Type**: typing.Optional[str]

### NamespacePid
- **Type**: typing.Optional[int]

### Pwd
- **Type**: typing.Optional[str]

### Pid
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Uuid
- **Type**: typing.Optional[str]

### ParentUuid
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[int]

### Euid
- **Type**: typing.Optional[int]

### Lineage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.LineageObject]]


# ProductCode

### Code
- **Type**: typing.Optional[str]

### ProductType
- **Type**: typing.Optional[str]


# PublicAccess

### PermissionConfiguration
- **Type**: <class 'NoneType'>

### EffectivePermission
- **Type**: typing.Optional[str]


# PublicAccessConfiguration

### PublicAclAccess
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'BLOCKED']]

### PublicPolicyAccess
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'BLOCKED']]

### PublicAclIgnoreBehavior
- **Type**: typing.Optional[typing.Literal['IGNORED', 'NOT_IGNORED']]

### PublicBucketRestrictBehavior
- **Type**: typing.Optional[typing.Literal['NOT_RESTRICTED', 'RESTRICTED']]


# RdsDbInstanceDetails

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbInstanceArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]


# RdsDbUserDetails

### User
- **Type**: typing.Optional[str]

### Application
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### Ssl
- **Type**: typing.Optional[str]

### AuthMethod
- **Type**: typing.Optional[str]


# RdsLimitlessDbDetails

### DbShardGroupIdentifier
- **Type**: typing.Optional[str]

### DbShardGroupResourceId
- **Type**: typing.Optional[str]

### DbShardGroupArn
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]


# RdsLoginAttemptAction

### RemoteIpDetails
- **Type**: <class 'NoneType'>

### LoginAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.LoginAttribute]]


# RemoteAccountDetails

### AccountId
- **Type**: typing.Optional[str]

### Affiliated
- **Type**: typing.Optional[bool]


# RemoteIpDetails

### City
- **Type**: <class 'NoneType'>

### Country
- **Type**: <class 'NoneType'>

### GeoLocation
- **Type**: <class 'NoneType'>

### IpAddressV4
- **Type**: typing.Optional[str]

### IpAddressV6
- **Type**: typing.Optional[str]

### Organization
- **Type**: <class 'NoneType'>


# RemotePortDetails

### Port
- **Type**: typing.Optional[int]

### PortName
- **Type**: typing.Optional[str]


# Resource

### AccessKeyDetails
- **Type**: <class 'NoneType'>

### S3BucketDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.S3BucketDetail]]

### InstanceDetails
- **Type**: <class 'NoneType'>

### EksClusterDetails
- **Type**: <class 'NoneType'>

### KubernetesDetails
- **Type**: <class 'NoneType'>

### ResourceType
- **Type**: typing.Optional[str]

### EbsVolumeDetails
- **Type**: <class 'NoneType'>

### EcsClusterDetails
- **Type**: <class 'NoneType'>

### ContainerDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Container]

### RdsDbInstanceDetails
- **Type**: <class 'NoneType'>

### RdsLimitlessDbDetails
- **Type**: <class 'NoneType'>

### RdsDbUserDetails
- **Type**: <class 'NoneType'>

### LambdaDetails
- **Type**: <class 'NoneType'>


# ResourceData

### S3Bucket
- **Type**: <class 'NoneType'>

### Ec2Instance
- **Type**: <class 'NoneType'>

### AccessKey
- **Type**: <class 'NoneType'>

### Ec2NetworkInterface
- **Type**: <class 'NoneType'>

### S3Object
- **Type**: <class 'NoneType'>


# ResourceDetails

### InstanceArn
- **Type**: typing.Optional[str]


# ResourceStatistics

### AccountId
- **Type**: typing.Optional[str]

### LastGeneratedAt
- **Type**: typing.Optional[datetime.datetime]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### TotalFindings
- **Type**: typing.Optional[int]


# ResourceV2

### Uid
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['ACCESS_KEY', 'EC2_INSTANCE', 'EC2_NETWORK_INTERFACE', 'S3_BUCKET', 'S3_OBJECT']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[str]

### CloudPartition
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]

### Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResourceData]


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


# RuntimeContext

### ModifyingProcess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ProcessDetails]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### ScriptPath
- **Type**: typing.Optional[str]

### LibraryPath
- **Type**: typing.Optional[str]

### LdPreloadValue
- **Type**: typing.Optional[str]

### SocketPath
- **Type**: typing.Optional[str]

### RuncBinaryPath
- **Type**: typing.Optional[str]

### ReleaseAgentPath
- **Type**: typing.Optional[str]

### MountSource
- **Type**: typing.Optional[str]

### MountTarget
- **Type**: typing.Optional[str]

### FileSystemType
- **Type**: typing.Optional[str]

### Flags
- **Type**: typing.Optional[typing.List[str]]

### ModuleName
- **Type**: typing.Optional[str]

### ModuleFilePath
- **Type**: typing.Optional[str]

### ModuleSha256
- **Type**: typing.Optional[str]

### ShellHistoryFilePath
- **Type**: typing.Optional[str]

### TargetProcess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ProcessDetails]

### AddressFamily
- **Type**: typing.Optional[str]

### IanaProtocolNumber
- **Type**: typing.Optional[int]

### MemoryRegions
- **Type**: typing.Optional[typing.List[str]]

### ToolName
- **Type**: typing.Optional[str]

### ToolCategory
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### CommandLineExample
- **Type**: typing.Optional[str]

### ThreatFilePath
- **Type**: typing.Optional[str]


# RuntimeDetails

### Process
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ProcessDetails]

### Context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.RuntimeContext]


# S3Bucket

### OwnerId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### EncryptionType
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### EffectivePermission
- **Type**: typing.Optional[str]

### PublicReadAccess
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'BLOCKED']]

### PublicWriteAccess
- **Type**: typing.Optional[typing.Literal['ALLOWED', 'BLOCKED']]

### AccountPublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PublicAccessConfiguration]

### BucketPublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.PublicAccessConfiguration]

### S3ObjectUids
- **Type**: typing.Optional[typing.List[str]]


# S3BucketDetail

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Owner
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Tag]]

### DefaultServerSideEncryption
- **Type**: <class 'NoneType'>

### PublicAccess
- **Type**: <class 'NoneType'>

### S3ObjectDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.S3ObjectDetail]]


# S3LogsConfiguration

### Enable
- **Type**: <class 'bool'>
- **Required**: Yes


# S3LogsConfigurationResult

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# S3Object

### ETag
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# S3ObjectDetail

### ObjectArn
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### Hash
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# Scan

### DetectorId
- **Type**: typing.Optional[str]

### AdminDetectorId
- **Type**: typing.Optional[str]

### ScanId
- **Type**: typing.Optional[str]

### ScanStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'SKIPPED']]

### FailureReason
- **Type**: typing.Optional[str]

### ScanStartTime
- **Type**: typing.Optional[datetime.datetime]

### ScanEndTime
- **Type**: typing.Optional[datetime.datetime]

### TriggerDetails
- **Type**: <class 'NoneType'>

### ResourceDetails
- **Type**: <class 'NoneType'>

### ScanResultDetails
- **Type**: <class 'NoneType'>

### AccountId
- **Type**: typing.Optional[str]

### TotalBytes
- **Type**: typing.Optional[int]

### FileCount
- **Type**: typing.Optional[int]

### AttachedVolumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.VolumeDetail]]

### ScanType
- **Type**: typing.Optional[typing.Literal['GUARDDUTY_INITIATED', 'ON_DEMAND']]


# ScanCondition

### MapEquals
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanConditionPair]
- **Required**: Yes


# ScanConditionOutput

### MapEquals
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanConditionPair]
- **Required**: Yes


# ScanConditionPair

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# ScanDetections

### ScannedItemCount
- **Type**: <class 'NoneType'>

### ThreatsDetectedItemCount
- **Type**: <class 'NoneType'>

### HighestSeverityThreatDetails
- **Type**: <class 'NoneType'>

### ThreatDetectedByName
- **Type**: <class 'NoneType'>


# ScanEc2InstanceWithFindings

### EbsVolumes
- **Type**: typing.Optional[bool]


# ScanEc2InstanceWithFindingsResult

### EbsVolumes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.EbsVolumesResult]


# ScanFilePath

### FilePath
- **Type**: typing.Optional[str]

### VolumeArn
- **Type**: typing.Optional[str]

### Hash
- **Type**: typing.Optional[str]

### FileName
- **Type**: typing.Optional[str]


# ScanResourceCriteria

### Include
- **Type**: typing.Optional[typing.Dict[typing.Literal['EC2_INSTANCE_TAG'], aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanCondition]]

### Exclude
- **Type**: typing.Optional[typing.Dict[typing.Literal['EC2_INSTANCE_TAG'], aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanCondition]]


# ScanResourceCriteriaOutput

### Include
- **Type**: typing.Optional[typing.Dict[typing.Literal['EC2_INSTANCE_TAG'], aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanConditionOutput]]

### Exclude
- **Type**: typing.Optional[typing.Dict[typing.Literal['EC2_INSTANCE_TAG'], aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanConditionOutput]]


# ScanResultDetails

### ScanResult
- **Type**: typing.Optional[typing.Literal['CLEAN', 'INFECTED']]


# ScanThreatName

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### FilePaths
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanFilePath]]


# ScannedItemCount

### TotalGb
- **Type**: typing.Optional[int]

### Files
- **Type**: typing.Optional[int]

### Volumes
- **Type**: typing.Optional[int]


# SecurityContext

### Privileged
- **Type**: typing.Optional[bool]

### AllowPrivilegeEscalation
- **Type**: typing.Optional[bool]


# SecurityGroup

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# Sequence

### Uid
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Signals
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Signal]
- **Required**: Yes

### Actors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Actor]]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResourceV2]]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.NetworkEndpoint]]

### SequenceIndicators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Indicator]]


# Service

### Action
- **Type**: <class 'NoneType'>

### Evidence
- **Type**: <class 'NoneType'>

### Archived
- **Type**: typing.Optional[bool]

### Count
- **Type**: typing.Optional[int]

### DetectorId
- **Type**: typing.Optional[str]

### EventFirstSeen
- **Type**: typing.Optional[str]

### EventLastSeen
- **Type**: typing.Optional[str]

### ResourceRole
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### UserFeedback
- **Type**: typing.Optional[str]

### AdditionalInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ServiceAdditionalInfo]

### FeatureName
- **Type**: typing.Optional[str]

### EbsVolumeScanDetails
- **Type**: <class 'NoneType'>

### RuntimeDetails
- **Type**: <class 'NoneType'>

### Detection
- **Type**: <class 'NoneType'>

### MalwareScanDetails
- **Type**: <class 'NoneType'>


# ServiceAdditionalInfo

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# Session

### Uid
- **Type**: typing.Optional[str]

### MfaStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Issuer
- **Type**: typing.Optional[str]


# SeverityStatistics

### LastGeneratedAt
- **Type**: typing.Optional[datetime.datetime]

### Severity
- **Type**: typing.Optional[float]

### TotalFindings
- **Type**: typing.Optional[int]


# Signal

### Uid
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['CLOUD_TRAIL', 'FINDING', 'S3_DATA_EVENTS']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FirstSeenAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastSeenAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[float]

### ResourceUids
- **Type**: typing.Optional[typing.List[str]]

### ActorIds
- **Type**: typing.Optional[typing.List[str]]

### EndpointIds
- **Type**: typing.Optional[typing.List[str]]

### SignalIndicators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.Indicator]]


# SortCriteria

### AttributeName
- **Type**: typing.Optional[str]

### OrderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# StartMalwareScanRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartMalwareScanResponse

### ScanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# StartMonitoringMembersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# StartMonitoringMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# StopMonitoringMembersRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# StopMonitoringMembersResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Threat

### Name
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### ItemPaths
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ItemPath]]


# ThreatDetectedByName

### ItemCount
- **Type**: typing.Optional[int]

### UniqueThreatNameCount
- **Type**: typing.Optional[int]

### Shortened
- **Type**: typing.Optional[bool]

### ThreatNames
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanThreatName]]


# ThreatIntelligenceDetail

### ThreatListName
- **Type**: typing.Optional[str]

### ThreatNames
- **Type**: typing.Optional[typing.List[str]]

### ThreatFileSha256
- **Type**: typing.Optional[str]


# ThreatsDetectedItemCount

### Files
- **Type**: typing.Optional[int]


# Total

### Amount
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# TriggerDetails

### GuardDutyFindingId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UnarchiveFindingsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingIds
- **Type**: typing.List[str]
- **Required**: Yes


# UnprocessedAccount

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Result
- **Type**: <class 'str'>
- **Required**: Yes


# UnprocessedDataSourcesResult

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionConfigurationResult]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDetectorRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Enable
- **Type**: typing.Optional[bool]

### FindingPublishingFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']]

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceConfigurations]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DetectorFeatureConfiguration]]


# UpdateFilterRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'NOOP']]

### Rank
- **Type**: typing.Optional[int]

### FindingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteria, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.FindingCriteriaOutput, NoneType]


# UpdateFilterResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFindingsFeedbackRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingIds
- **Type**: typing.List[str]
- **Required**: Yes

### Feedback
- **Type**: typing.Literal['NOT_USEFUL', 'USEFUL']
- **Required**: Yes

### Comments
- **Type**: typing.Optional[str]


# UpdateIPSetRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### IpSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### Activate
- **Type**: typing.Optional[bool]


# UpdateMalwareProtectionPlanRequest

### MalwareProtectionPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MalwareProtectionPlanActions]

### ProtectedResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UpdateProtectedResource]


# UpdateMalwareScanSettingsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ScanResourceCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanResourceCriteria, aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ScanResourceCriteriaOutput, NoneType]

### EbsSnapshotPreservation
- **Type**: typing.Optional[typing.Literal['NO_RETENTION', 'RETENTION_WITH_FINDING']]


# UpdateMemberDetectorsRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.DataSourceConfigurations]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.MemberFeaturesConfiguration]]


# UpdateMemberDetectorsResponse

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty.guardduty_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateOrganizationConfigurationRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoEnable
- **Type**: typing.Optional[bool]

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationDataSourceConfigurations]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.OrganizationFeatureConfiguration]]

### AutoEnableOrganizationMembers
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]


# UpdateProtectedResource

### S3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UpdateS3BucketResource]


# UpdatePublishingDestinationRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationProperties
- **Type**: <class 'NoneType'>


# UpdateS3BucketResource

### ObjectPrefixes
- **Type**: typing.Optional[typing.List[str]]


# UpdateThreatIntelSetRequest

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ThreatIntelSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### Activate
- **Type**: typing.Optional[bool]


# UsageAccountResult

### AccountId
- **Type**: typing.Optional[str]

### Total
- **Type**: <class 'NoneType'>


# UsageCriteria

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### DataSources
- **Type**: typing.Optional[typing.List[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EC2_MALWARE_SCAN', 'FLOW_LOGS', 'KUBERNETES_AUDIT_LOGS', 'S3_LOGS']]]

### Resources
- **Type**: typing.Optional[typing.List[str]]

### Features
- **Type**: typing.Optional[typing.List[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EC2_RUNTIME_MONITORING', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FARGATE_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_DBI_PROTECTION_PROVISIONED', 'RDS_DBI_PROTECTION_SERVERLESS', 'RDS_LOGIN_EVENTS', 'S3_DATA_EVENTS']]]


# UsageDataSourceResult

### DataSource
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EC2_MALWARE_SCAN', 'FLOW_LOGS', 'KUBERNETES_AUDIT_LOGS', 'S3_LOGS']]

### Total
- **Type**: <class 'NoneType'>


# UsageFeatureResult

### Feature
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EC2_RUNTIME_MONITORING', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FARGATE_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_DBI_PROTECTION_PROVISIONED', 'RDS_DBI_PROTECTION_SERVERLESS', 'RDS_LOGIN_EVENTS', 'S3_DATA_EVENTS']]

### Total
- **Type**: <class 'NoneType'>


# UsageResourceResult

### Resource
- **Type**: typing.Optional[str]

### Total
- **Type**: <class 'NoneType'>


# UsageStatistics

### SumByAccount
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageAccountResult]]

### TopAccountsByFeature
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageTopAccountsResult]]

### SumByDataSource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageDataSourceResult]]

### SumByResource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageResourceResult]]

### TopResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageResourceResult]]

### SumByFeature
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageFeatureResult]]


# UsageTopAccountResult

### AccountId
- **Type**: typing.Optional[str]

### Total
- **Type**: <class 'NoneType'>


# UsageTopAccountsResult

### Feature
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EC2_RUNTIME_MONITORING', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FARGATE_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_DBI_PROTECTION_PROVISIONED', 'RDS_DBI_PROTECTION_SERVERLESS', 'RDS_LOGIN_EVENTS', 'S3_DATA_EVENTS']]

### Accounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.UsageTopAccountResult]]


# User

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Uid
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### CredentialUid
- **Type**: typing.Optional[str]

### Account
- **Type**: <class 'NoneType'>


# Volume

### Name
- **Type**: typing.Optional[str]

### HostPath
- **Type**: <class 'NoneType'>


# VolumeDetail

### VolumeArn
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### EncryptionType
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# VolumeMount

### Name
- **Type**: typing.Optional[str]

### MountPath
- **Type**: typing.Optional[str]


# VpcConfig

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty.guardduty_classes.SecurityGroup]]


