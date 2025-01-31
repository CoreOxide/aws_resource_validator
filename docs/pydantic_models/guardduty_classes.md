# guardduty_classes

# AcceptAdministratorInvitationRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AdministratorId
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptInvitationRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MasterId
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# AccessControlListTypeDef

### AllowsPublicReadAccess
- **Type**: typing.Optional[bool]

### AllowsPublicWriteAccess
- **Type**: typing.Optional[bool]


# AccessKeyDetailsTypeDef

### AccessKeyId
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[str]


# AccountDetailTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes


# AccountFreeTrialInfoTypeDef

### AccountId
- **Type**: typing.Optional[str]

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourcesFreeTrialTypeDef]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.FreeTrialFeatureConfigurationResultTypeDef]]


# AccountLevelPermissionsTypeDef

### BlockPublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.BlockPublicAccessTypeDef]


# ActionTypeDef

### ActionType
- **Type**: typing.Optional[str]

### AwsApiCallAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.AwsApiCallActionTypeDef]

### DnsRequestAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DnsRequestActionTypeDef]

### NetworkConnectionAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.NetworkConnectionActionTypeDef]

### PortProbeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PortProbeActionTypeDef]

### KubernetesApiCallAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesApiCallActionTypeDef]

### RdsLoginAttemptAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RdsLoginAttemptActionTypeDef]

### KubernetesPermissionCheckedDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesPermissionCheckedDetailsTypeDef]

### KubernetesRoleBindingDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesRoleBindingDetailsTypeDef]

### KubernetesRoleDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesRoleDetailsTypeDef]


# AddonDetailsTypeDef

### AddonVersion
- **Type**: typing.Optional[str]

### AddonStatus
- **Type**: typing.Optional[str]


# AdminAccountTypeDef

### AdminAccountId
- **Type**: typing.Optional[str]

### AdminStatus
- **Type**: typing.Optional[typing.Literal['DISABLE_IN_PROGRESS', 'ENABLED']]


# AdministratorTypeDef

### AccountId
- **Type**: typing.Optional[str]

### InvitationId
- **Type**: typing.Optional[str]

### RelationshipStatus
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[str]


# AgentDetailsTypeDef

### Version
- **Type**: typing.Optional[str]


# AnomalyObjectTypeDef

### ProfileType
- **Type**: typing.Optional[typing.Literal['FREQUENCY']]

### ProfileSubtype
- **Type**: typing.Optional[typing.Literal['FREQUENT', 'INFREQUENT', 'RARE', 'UNSEEN']]

### Observations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ObservationsTypeDef]


# AnomalyTypeDef

### Profiles
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.guardduty_classes.AnomalyObjectTypeDef]]]]

### Unusual
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.AnomalyUnusualTypeDef]


# AnomalyUnusualTypeDef

### Behavior
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.guardduty_classes.AnomalyObjectTypeDef]]]


# ArchiveFindingsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AwsApiCallActionTypeDef

### Api
- **Type**: typing.Optional[str]

### CallerType
- **Type**: typing.Optional[str]

### DomainDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DomainDetailsTypeDef]

### ErrorCode
- **Type**: typing.Optional[str]

### UserAgent
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RemoteIpDetailsTypeDef]

### ServiceName
- **Type**: typing.Optional[str]

### RemoteAccountDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RemoteAccountDetailsTypeDef]

### AffectedResources
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockPublicAccessTypeDef

### IgnorePublicAcls
- **Type**: typing.Optional[bool]

### RestrictPublicBuckets
- **Type**: typing.Optional[bool]

### BlockPublicAcls
- **Type**: typing.Optional[bool]

### BlockPublicPolicy
- **Type**: typing.Optional[bool]


# BucketLevelPermissionsTypeDef

### AccessControlList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.AccessControlListTypeDef]

### BucketPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.BucketPolicyTypeDef]

### BlockPublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.BlockPublicAccessTypeDef]


# BucketPolicyTypeDef

### AllowsPublicReadAccess
- **Type**: typing.Optional[bool]

### AllowsPublicWriteAccess
- **Type**: typing.Optional[bool]


# CityTypeDef

### CityName
- **Type**: typing.Optional[str]


# CloudTrailConfigurationResultTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# ConditionOutputTypeDef

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


# ConditionTypeDef

### Eq
- **Type**: typing.Optional[typing.Sequence[str]]

### Neq
- **Type**: typing.Optional[typing.Sequence[str]]

### Gt
- **Type**: typing.Optional[int]

### Gte
- **Type**: typing.Optional[int]

### Lt
- **Type**: typing.Optional[int]

### Lte
- **Type**: typing.Optional[int]

### Equals
- **Type**: typing.Optional[typing.Sequence[str]]

### NotEquals
- **Type**: typing.Optional[typing.Sequence[str]]

### GreaterThan
- **Type**: typing.Optional[int]

### GreaterThanOrEqual
- **Type**: typing.Optional[int]

### LessThan
- **Type**: typing.Optional[int]

### LessThanOrEqual
- **Type**: typing.Optional[int]


# ContainerInstanceDetailsTypeDef

### CoveredContainerInstances
- **Type**: typing.Optional[int]

### CompatibleContainerInstances
- **Type**: typing.Optional[int]


# ContainerTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.VolumeMountTypeDef]]

### SecurityContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.SecurityContextTypeDef]


# CountryTypeDef

### CountryCode
- **Type**: typing.Optional[str]

### CountryName
- **Type**: typing.Optional[str]


# CoverageEc2InstanceDetailsTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### AgentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.AgentDetailsTypeDef]

### ManagementType
- **Type**: typing.Optional[typing.Literal['AUTO_MANAGED', 'DISABLED', 'MANUAL']]


# CoverageEcsClusterDetailsTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### FargateDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.FargateDetailsTypeDef]

### ContainerInstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ContainerInstanceDetailsTypeDef]


# CoverageEksClusterDetailsTypeDef

### ClusterName
- **Type**: typing.Optional[str]

### CoveredNodes
- **Type**: typing.Optional[int]

### CompatibleNodes
- **Type**: typing.Optional[int]

### AddonDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.AddonDetailsTypeDef]

### ManagementType
- **Type**: typing.Optional[typing.Literal['AUTO_MANAGED', 'DISABLED', 'MANUAL']]


# CoverageFilterConditionTypeDef

### Equals
- **Type**: typing.Optional[typing.Sequence[str]]

### NotEquals
- **Type**: typing.Optional[typing.Sequence[str]]


# CoverageFilterCriteriaTypeDef

### FilterCriterion
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.CoverageFilterCriterionTypeDef]]


# CoverageFilterCriterionTypeDef

### CriterionKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ADDON_VERSION', 'AGENT_VERSION', 'CLUSTER_ARN', 'CLUSTER_NAME', 'COVERAGE_STATUS', 'ECS_CLUSTER_NAME', 'EKS_CLUSTER_NAME', 'INSTANCE_ID', 'MANAGEMENT_TYPE', 'RESOURCE_TYPE']]

### FilterCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageFilterConditionTypeDef]


# CoverageResourceDetailsTypeDef

### EksClusterDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageEksClusterDetailsTypeDef]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2', 'ECS', 'EKS']]

### EcsClusterDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageEcsClusterDetailsTypeDef]

### Ec2InstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageEc2InstanceDetailsTypeDef]


# CoverageResourceTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### DetectorId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### ResourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageResourceDetailsTypeDef]

### CoverageStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### Issue
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# CoverageSortCriteriaTypeDef

### AttributeName
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'ADDON_VERSION', 'CLUSTER_NAME', 'COVERAGE_STATUS', 'ECS_CLUSTER_NAME', 'EKS_CLUSTER_NAME', 'INSTANCE_ID', 'ISSUE', 'UPDATED_AT']]

### OrderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# CoverageStatisticsTypeDef

### CountByResourceType
- **Type**: typing.Optional[typing.Dict[typing.Literal['EC2', 'ECS', 'EKS'], int]]

### CountByCoverageStatus
- **Type**: typing.Optional[typing.Dict[typing.Literal['HEALTHY', 'UNHEALTHY'], int]]


# CreateDetectorRequestRequestTypeDef

### Enable
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### FindingPublishingFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']]

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceConfigurationsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Features
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.DetectorFeatureConfigurationTypeDef]]


# CreateDetectorResponseTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### UnprocessedDataSources
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedDataSourcesResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFilterRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FindingCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.FindingCriteriaTypeDef'>
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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFilterResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIPSetRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateIPSetResponseTypeDef

### IpSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMalwareProtectionPlanRequestRequestTypeDef

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedResource
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.CreateProtectedResourceTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionPlanActionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMalwareProtectionPlanResponseTypeDef

### MalwareProtectionPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMembersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountDetails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.AccountDetailTypeDef]
- **Required**: Yes


# CreateMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProtectedResourceOutputTypeDef

### S3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CreateS3BucketResourceOutputTypeDef]


# CreateProtectedResourceTypeDef

### S3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CreateS3BucketResourceTypeDef]


# CreatePublishingDestinationRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationType
- **Type**: typing.Literal['S3']
- **Required**: Yes

### DestinationProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.DestinationPropertiesTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreatePublishingDestinationResponseTypeDef

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateS3BucketResourceOutputTypeDef

### BucketName
- **Type**: typing.Optional[str]

### ObjectPrefixes
- **Type**: typing.Optional[typing.List[str]]


# CreateS3BucketResourceTypeDef

### BucketName
- **Type**: typing.Optional[str]

### ObjectPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateSampleFindingsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateThreatIntelSetRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateThreatIntelSetResponseTypeDef

### ThreatIntelSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DNSLogsConfigurationResultTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# DataSourceConfigurationsResultTypeDef

### CloudTrail
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.CloudTrailConfigurationResultTypeDef'>
- **Required**: Yes

### DNSLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.DNSLogsConfigurationResultTypeDef'>
- **Required**: Yes

### FlowLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.FlowLogsConfigurationResultTypeDef'>
- **Required**: Yes

### S3Logs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.S3LogsConfigurationResultTypeDef'>
- **Required**: Yes

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesConfigurationResultTypeDef]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionConfigurationResultTypeDef]


# DataSourceConfigurationsTypeDef

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.S3LogsConfigurationTypeDef]

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesConfigurationTypeDef]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionConfigurationTypeDef]


# DataSourceFreeTrialTypeDef

### FreeTrialDaysRemaining
- **Type**: typing.Optional[int]


# DataSourcesFreeTrialTypeDef

### CloudTrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceFreeTrialTypeDef]

### DnsLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceFreeTrialTypeDef]

### FlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceFreeTrialTypeDef]

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceFreeTrialTypeDef]

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesDataSourceFreeTrialTypeDef]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionDataSourceFreeTrialTypeDef]


# DeclineInvitationsRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeclineInvitationsResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefaultServerSideEncryptionTypeDef

### EncryptionType
- **Type**: typing.Optional[str]

### KmsMasterKeyArn
- **Type**: typing.Optional[str]


# DeleteDetectorRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFilterRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIPSetRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### IpSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInvitationsRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteInvitationsResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMalwareProtectionPlanRequestRequestTypeDef

### MalwareProtectionPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMembersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePublishingDestinationRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThreatIntelSetRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ThreatIntelSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMalwareScansRequestDescribeMalwareScansPaginateTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.FilterCriteriaTypeDef]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.SortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# DescribeMalwareScansRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.FilterCriteriaTypeDef]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.SortCriteriaTypeDef]


# DescribeMalwareScansResponseTypeDef

### Scans
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ScanTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigurationRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigurationResponseTypeDef

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### MemberAccountLimitReached
- **Type**: <class 'bool'>
- **Required**: Yes

### DataSources
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.OrganizationDataSourceConfigurationsResultTypeDef'>
- **Required**: Yes

### Features
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationFeatureConfigurationResultTypeDef]
- **Required**: Yes

### AutoEnableOrganizationMembers
- **Type**: typing.Literal['ALL', 'NEW', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePublishingDestinationRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePublishingDestinationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.DestinationPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationPropertiesTypeDef

### DestinationArn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# DestinationTypeDef

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationType
- **Type**: typing.Literal['S3']
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING_VERIFICATION', 'PUBLISHING', 'STOPPED', 'UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY']
- **Required**: Yes


# DetectionTypeDef

### Anomaly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.AnomalyTypeDef]


# DetectorAdditionalConfigurationResultTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# DetectorAdditionalConfigurationTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DetectorFeatureConfigurationResultTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.DetectorAdditionalConfigurationResultTypeDef]]


# DetectorFeatureConfigurationTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.DetectorAdditionalConfigurationTypeDef]]


# DisableOrganizationAdminAccountRequestRequestTypeDef

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFromAdministratorAccountRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFromMasterAccountRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMembersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociateMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DnsRequestActionTypeDef

### Domain
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]

### Blocked
- **Type**: typing.Optional[bool]

### DomainWithSuffix
- **Type**: typing.Optional[str]


# DomainDetailsTypeDef

### Domain
- **Type**: typing.Optional[str]


# EbsVolumeDetailsTypeDef

### ScannedVolumeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.VolumeDetailTypeDef]]

### SkippedVolumeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.VolumeDetailTypeDef]]


# EbsVolumeScanDetailsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ScanDetectionsTypeDef]

### ScanType
- **Type**: typing.Optional[typing.Literal['GUARDDUTY_INITIATED', 'ON_DEMAND']]


# EbsVolumesResultTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Reason
- **Type**: typing.Optional[str]


# EcsClusterDetailsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.TagTypeDef]]

### TaskDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.EcsTaskDetailsTypeDef]


# EcsTaskDetailsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.TagTypeDef]]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.VolumeTypeDef]]

### Containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ContainerTypeDef]]

### Group
- **Type**: typing.Optional[str]


# EksClusterDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.TagTypeDef]]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableOrganizationAdminAccountRequestRequestTypeDef

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# EvidenceTypeDef

### ThreatIntelligenceDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ThreatIntelligenceDetailTypeDef]]


# FargateDetailsTypeDef

### Issues
- **Type**: typing.Optional[typing.List[str]]

### ManagementType
- **Type**: typing.Optional[typing.Literal['AUTO_MANAGED', 'DISABLED', 'MANUAL']]


# FilterConditionTypeDef

### EqualsValue
- **Type**: typing.Optional[str]

### GreaterThan
- **Type**: typing.Optional[int]

### LessThan
- **Type**: typing.Optional[int]


# FilterCriteriaTypeDef

### FilterCriterion
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.FilterCriterionTypeDef]]


# FilterCriterionTypeDef

### CriterionKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'EC2_INSTANCE_ARN', 'GUARDDUTY_FINDING_ID', 'SCAN_ID', 'SCAN_START_TIME', 'SCAN_STATUS', 'SCAN_TYPE']]

### FilterCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.FilterConditionTypeDef]


# FindingCriteriaOutputTypeDef

### Criterion
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.guardduty_classes.ConditionOutputTypeDef]]


# FindingCriteriaTypeDef

### Criterion
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.guardduty_classes.ConditionTypeDef]]


# FindingStatisticsTypeDef

### CountBySeverity
- **Type**: typing.Optional[typing.Dict[str, int]]


# FindingTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResourceTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ServiceTypeDef]

### Title
- **Type**: typing.Optional[str]


# FlowLogsConfigurationResultTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# FreeTrialFeatureConfigurationResultTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EC2_RUNTIME_MONITORING', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FARGATE_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'S3_DATA_EVENTS']]

### FreeTrialDaysRemaining
- **Type**: typing.Optional[int]


# GeoLocationTypeDef

### Lat
- **Type**: typing.Optional[float]

### Lon
- **Type**: typing.Optional[float]


# GetAdministratorAccountRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdministratorAccountResponseTypeDef

### Administrator
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.AdministratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCoverageStatisticsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### StatisticsType
- **Type**: typing.Sequence[typing.Literal['COUNT_BY_COVERAGE_STATUS', 'COUNT_BY_RESOURCE_TYPE']]
- **Required**: Yes

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageFilterCriteriaTypeDef]


# GetCoverageStatisticsResponseTypeDef

### CoverageStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.CoverageStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDetectorRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDetectorResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.DataSourceConfigurationsResultTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Features
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.DetectorFeatureConfigurationResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFilterRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes


# GetFilterResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.FindingCriteriaOutputTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.SortCriteriaTypeDef]


# GetFindingsResponseTypeDef

### Findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.FindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingsStatisticsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingStatisticTypes
- **Type**: typing.Sequence[typing.Literal['COUNT_BY_SEVERITY']]
- **Required**: Yes

### FindingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.FindingCriteriaTypeDef]


# GetFindingsStatisticsResponseTypeDef

### FindingStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.FindingStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIPSetRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### IpSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIPSetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInvitationsCountResponseTypeDef

### InvitationsCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMalwareProtectionPlanRequestRequestTypeDef

### MalwareProtectionPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMalwareProtectionPlanResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedResource
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.CreateProtectedResourceOutputTypeDef'>
- **Required**: Yes

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionPlanActionsTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR', 'WARNING']
- **Required**: Yes

### StatusReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionPlanStatusReasonTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMalwareScanSettingsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMalwareScanSettingsResponseTypeDef

### ScanResourceCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ScanResourceCriteriaOutputTypeDef'>
- **Required**: Yes

### EbsSnapshotPreservation
- **Type**: typing.Literal['NO_RETENTION', 'RETENTION_WITH_FINDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMasterAccountRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMasterAccountResponseTypeDef

### Master
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.MasterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMemberDetectorsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetMemberDetectorsResponseTypeDef

### MemberDataSourceConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.MemberDataSourceConfigurationTypeDef]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMembersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetMembersResponseTypeDef

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.MemberTypeDef]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOrganizationStatisticsResponseTypeDef

### OrganizationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.OrganizationDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRemainingFreeTrialDaysRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# GetRemainingFreeTrialDaysResponseTypeDef

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.AccountFreeTrialInfoTypeDef]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetThreatIntelSetRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ThreatIntelSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetThreatIntelSetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUsageStatisticsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### UsageStatisticType
- **Type**: typing.Literal['SUM_BY_ACCOUNT', 'SUM_BY_DATA_SOURCE', 'SUM_BY_FEATURES', 'SUM_BY_RESOURCE', 'TOP_ACCOUNTS_BY_FEATURE', 'TOP_RESOURCES']
- **Required**: Yes

### UsageCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.UsageCriteriaTypeDef'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetUsageStatisticsResponseTypeDef

### UsageStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.UsageStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# HighestSeverityThreatDetailsTypeDef

### Severity
- **Type**: typing.Optional[str]

### ThreatName
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]


# HostPathTypeDef

### Path
- **Type**: typing.Optional[str]


# IamInstanceProfileTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# ImpersonatedUserTypeDef

### Username
- **Type**: typing.Optional[str]

### Groups
- **Type**: typing.Optional[typing.List[str]]


# InstanceDetailsTypeDef

### AvailabilityZone
- **Type**: typing.Optional[str]

### IamInstanceProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.IamInstanceProfileTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.NetworkInterfaceTypeDef]]

### Platform
- **Type**: typing.Optional[str]

### ProductCodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ProductCodeTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.TagTypeDef]]


# InvitationTypeDef

### AccountId
- **Type**: typing.Optional[str]

### InvitationId
- **Type**: typing.Optional[str]

### RelationshipStatus
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[str]


# InviteMembersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DisableEmailNotification
- **Type**: typing.Optional[bool]

### Message
- **Type**: typing.Optional[str]


# InviteMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ItemPathTypeDef

### NestedItemPath
- **Type**: typing.Optional[str]

### Hash
- **Type**: typing.Optional[str]


# KubernetesApiCallActionTypeDef

### RequestUri
- **Type**: typing.Optional[str]

### Verb
- **Type**: typing.Optional[str]

### SourceIps
- **Type**: typing.Optional[typing.List[str]]

### UserAgent
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RemoteIpDetailsTypeDef]

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


# KubernetesAuditLogsConfigurationResultTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# KubernetesAuditLogsConfigurationTypeDef

### Enable
- **Type**: <class 'bool'>
- **Required**: Yes


# KubernetesConfigurationResultTypeDef

### AuditLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.KubernetesAuditLogsConfigurationResultTypeDef'>
- **Required**: Yes


# KubernetesConfigurationTypeDef

### AuditLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.KubernetesAuditLogsConfigurationTypeDef'>
- **Required**: Yes


# KubernetesDataSourceFreeTrialTypeDef

### AuditLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceFreeTrialTypeDef]


# KubernetesDetailsTypeDef

### KubernetesUserDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesUserDetailsTypeDef]

### KubernetesWorkloadDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesWorkloadDetailsTypeDef]


# KubernetesPermissionCheckedDetailsTypeDef

### Verb
- **Type**: typing.Optional[str]

### Resource
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Allowed
- **Type**: typing.Optional[bool]


# KubernetesRoleBindingDetailsTypeDef

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


# KubernetesRoleDetailsTypeDef

### Kind
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Uid
- **Type**: typing.Optional[str]


# KubernetesUserDetailsTypeDef

### Username
- **Type**: typing.Optional[str]

### Uid
- **Type**: typing.Optional[str]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### SessionName
- **Type**: typing.Optional[typing.List[str]]

### ImpersonatedUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ImpersonatedUserTypeDef]


# KubernetesWorkloadDetailsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ContainerTypeDef]]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.VolumeTypeDef]]

### ServiceAccountName
- **Type**: typing.Optional[str]

### HostIPC
- **Type**: typing.Optional[bool]

### HostPID
- **Type**: typing.Optional[bool]


# LambdaDetailsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.VpcConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.TagTypeDef]]


# LineageObjectTypeDef

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


# ListCoverageRequestListCoveragePaginateTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageFilterCriteriaTypeDef]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageSortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListCoverageRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageFilterCriteriaTypeDef]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CoverageSortCriteriaTypeDef]


# ListCoverageResponseTypeDef

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.CoverageResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDetectorsRequestListDetectorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListDetectorsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDetectorsResponseTypeDef

### DetectorIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFiltersRequestListFiltersPaginateTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListFiltersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFiltersResponseTypeDef

### FilterNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFindingsRequestListFindingsPaginateTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.FindingCriteriaTypeDef]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.SortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListFindingsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.FindingCriteriaTypeDef]

### SortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.SortCriteriaTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFindingsResponseTypeDef

### FindingIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIPSetsRequestListIPSetsPaginateTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListIPSetsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIPSetsResponseTypeDef

### IpSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequestListInvitationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListInvitationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsResponseTypeDef

### Invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.InvitationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMalwareProtectionPlansRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListMalwareProtectionPlansResponseTypeDef

### MalwareProtectionPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionPlanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersRequestListMembersPaginateTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### OnlyAssociated
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListMembersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### OnlyAssociated
- **Type**: typing.Optional[str]


# ListMembersResponseTypeDef

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.MemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListOrganizationAdminAccountsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsResponseTypeDef

### AdminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.AdminAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPublishingDestinationsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPublishingDestinationsResponseTypeDef

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.DestinationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThreatIntelSetsRequestListThreatIntelSetsPaginateTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PaginatorConfigTypeDef]


# ListThreatIntelSetsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListThreatIntelSetsResponseTypeDef

### ThreatIntelSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocalIpDetailsTypeDef

### IpAddressV4
- **Type**: typing.Optional[str]

### IpAddressV6
- **Type**: typing.Optional[str]


# LocalPortDetailsTypeDef

### Port
- **Type**: typing.Optional[int]

### PortName
- **Type**: typing.Optional[str]


# LoginAttributeTypeDef

### User
- **Type**: typing.Optional[str]

### Application
- **Type**: typing.Optional[str]

### FailedLoginAttempts
- **Type**: typing.Optional[int]

### SuccessfulLoginAttempts
- **Type**: typing.Optional[int]


# MalwareProtectionConfigurationResultTypeDef

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ScanEc2InstanceWithFindingsResultTypeDef]

### ServiceRole
- **Type**: typing.Optional[str]


# MalwareProtectionConfigurationTypeDef

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ScanEc2InstanceWithFindingsTypeDef]


# MalwareProtectionDataSourceFreeTrialTypeDef

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceFreeTrialTypeDef]


# MalwareProtectionPlanActionsTypeDef

### Tagging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionPlanTaggingActionTypeDef]


# MalwareProtectionPlanStatusReasonTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# MalwareProtectionPlanSummaryTypeDef

### MalwareProtectionPlanId
- **Type**: typing.Optional[str]


# MalwareProtectionPlanTaggingActionTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MalwareScanDetailsTypeDef

### Threats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ThreatTypeDef]]


# MasterTypeDef

### AccountId
- **Type**: typing.Optional[str]

### InvitationId
- **Type**: typing.Optional[str]

### RelationshipStatus
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[str]


# MemberAdditionalConfigurationResultTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# MemberAdditionalConfigurationTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MemberDataSourceConfigurationTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceConfigurationsResultTypeDef]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.MemberFeaturesConfigurationResultTypeDef]]


# MemberFeaturesConfigurationResultTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.MemberAdditionalConfigurationResultTypeDef]]


# MemberFeaturesConfigurationTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.MemberAdditionalConfigurationTypeDef]]


# MemberTypeDef

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


# NetworkConnectionActionTypeDef

### Blocked
- **Type**: typing.Optional[bool]

### ConnectionDirection
- **Type**: typing.Optional[str]

### LocalPortDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.LocalPortDetailsTypeDef]

### Protocol
- **Type**: typing.Optional[str]

### LocalIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.LocalIpDetailsTypeDef]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RemoteIpDetailsTypeDef]

### RemotePortDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RemotePortDetailsTypeDef]


# NetworkInterfaceTypeDef

### Ipv6Addresses
- **Type**: typing.Optional[typing.List[str]]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### PrivateDnsName
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.PrivateIpAddressDetailsTypeDef]]

### PublicDnsName
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.SecurityGroupTypeDef]]

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# ObservationsTypeDef

### Text
- **Type**: typing.Optional[typing.List[str]]


# OrganizationAdditionalConfigurationResultTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### AutoEnable
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]


# OrganizationAdditionalConfigurationTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### AutoEnable
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]


# OrganizationDataSourceConfigurationsResultTypeDef

### S3Logs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.OrganizationS3LogsConfigurationResultTypeDef'>
- **Required**: Yes

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationKubernetesConfigurationResultTypeDef]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationMalwareProtectionConfigurationResultTypeDef]


# OrganizationDataSourceConfigurationsTypeDef

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationS3LogsConfigurationTypeDef]

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationKubernetesConfigurationTypeDef]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationMalwareProtectionConfigurationTypeDef]


# OrganizationDetailsTypeDef

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### OrganizationStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationStatisticsTypeDef]


# OrganizationEbsVolumesResultTypeDef

### AutoEnable
- **Type**: typing.Optional[bool]


# OrganizationEbsVolumesTypeDef

### AutoEnable
- **Type**: typing.Optional[bool]


# OrganizationFeatureConfigurationResultTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### AutoEnable
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationAdditionalConfigurationResultTypeDef]]


# OrganizationFeatureConfigurationTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### AutoEnable
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationAdditionalConfigurationTypeDef]]


# OrganizationFeatureStatisticsAdditionalConfigurationTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EC2_AGENT_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EKS_ADDON_MANAGEMENT']]

### EnabledAccountsCount
- **Type**: typing.Optional[int]


# OrganizationFeatureStatisticsTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EBS_MALWARE_PROTECTION', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'LAMBDA_NETWORK_LOGS', 'RDS_LOGIN_EVENTS', 'RUNTIME_MONITORING', 'S3_DATA_EVENTS']]

### EnabledAccountsCount
- **Type**: typing.Optional[int]

### AdditionalConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationFeatureStatisticsAdditionalConfigurationTypeDef]]


# OrganizationKubernetesAuditLogsConfigurationResultTypeDef

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# OrganizationKubernetesAuditLogsConfigurationTypeDef

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# OrganizationKubernetesConfigurationResultTypeDef

### AuditLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.OrganizationKubernetesAuditLogsConfigurationResultTypeDef'>
- **Required**: Yes


# OrganizationKubernetesConfigurationTypeDef

### AuditLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.OrganizationKubernetesAuditLogsConfigurationTypeDef'>
- **Required**: Yes


# OrganizationMalwareProtectionConfigurationResultTypeDef

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationScanEc2InstanceWithFindingsResultTypeDef]


# OrganizationMalwareProtectionConfigurationTypeDef

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationScanEc2InstanceWithFindingsTypeDef]


# OrganizationS3LogsConfigurationResultTypeDef

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# OrganizationS3LogsConfigurationTypeDef

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# OrganizationScanEc2InstanceWithFindingsResultTypeDef

### EbsVolumes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationEbsVolumesResultTypeDef]


# OrganizationScanEc2InstanceWithFindingsTypeDef

### EbsVolumes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationEbsVolumesTypeDef]


# OrganizationStatisticsTypeDef

### TotalAccountsCount
- **Type**: typing.Optional[int]

### MemberAccountsCount
- **Type**: typing.Optional[int]

### ActiveAccountsCount
- **Type**: typing.Optional[int]

### EnabledAccountsCount
- **Type**: typing.Optional[int]

### CountByFeature
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationFeatureStatisticsTypeDef]]


# OrganizationTypeDef

### Asn
- **Type**: typing.Optional[str]

### AsnOrg
- **Type**: typing.Optional[str]

### Isp
- **Type**: typing.Optional[str]

### Org
- **Type**: typing.Optional[str]


# OwnerTypeDef

### Id
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionConfigurationTypeDef

### BucketLevelPermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.BucketLevelPermissionsTypeDef]

### AccountLevelPermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.AccountLevelPermissionsTypeDef]


# PortProbeActionTypeDef

### Blocked
- **Type**: typing.Optional[bool]

### PortProbeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.PortProbeDetailTypeDef]]


# PortProbeDetailTypeDef

### LocalPortDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.LocalPortDetailsTypeDef]

### LocalIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.LocalIpDetailsTypeDef]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RemoteIpDetailsTypeDef]


# PrivateIpAddressDetailsTypeDef

### PrivateDnsName
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]


# ProcessDetailsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.LineageObjectTypeDef]]


# ProductCodeTypeDef

### Code
- **Type**: typing.Optional[str]

### ProductType
- **Type**: typing.Optional[str]


# PublicAccessTypeDef

### PermissionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PermissionConfigurationTypeDef]

### EffectivePermission
- **Type**: typing.Optional[str]


# RdsDbInstanceDetailsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.TagTypeDef]]


# RdsDbUserDetailsTypeDef

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


# RdsLoginAttemptActionTypeDef

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RemoteIpDetailsTypeDef]

### LoginAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.LoginAttributeTypeDef]]


# RemoteAccountDetailsTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Affiliated
- **Type**: typing.Optional[bool]


# RemoteIpDetailsTypeDef

### City
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CityTypeDef]

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.CountryTypeDef]

### GeoLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.GeoLocationTypeDef]

### IpAddressV4
- **Type**: typing.Optional[str]

### IpAddressV6
- **Type**: typing.Optional[str]

### Organization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationTypeDef]


# RemotePortDetailsTypeDef

### Port
- **Type**: typing.Optional[int]

### PortName
- **Type**: typing.Optional[str]


# ResourceDetailsTypeDef

### InstanceArn
- **Type**: typing.Optional[str]


# ResourceTypeDef

### AccessKeyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.AccessKeyDetailsTypeDef]

### S3BucketDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.S3BucketDetailTypeDef]]

### InstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.InstanceDetailsTypeDef]

### EksClusterDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.EksClusterDetailsTypeDef]

### KubernetesDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.KubernetesDetailsTypeDef]

### ResourceType
- **Type**: typing.Optional[str]

### EbsVolumeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.EbsVolumeDetailsTypeDef]

### EcsClusterDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.EcsClusterDetailsTypeDef]

### ContainerDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ContainerTypeDef]

### RdsDbInstanceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RdsDbInstanceDetailsTypeDef]

### RdsDbUserDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RdsDbUserDetailsTypeDef]

### LambdaDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.LambdaDetailsTypeDef]


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


# RuntimeContextTypeDef

### ModifyingProcess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ProcessDetailsTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ProcessDetailsTypeDef]

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


# RuntimeDetailsTypeDef

### Process
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ProcessDetailsTypeDef]

### Context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RuntimeContextTypeDef]


# S3BucketDetailTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Owner
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OwnerTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.TagTypeDef]]

### DefaultServerSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DefaultServerSideEncryptionTypeDef]

### PublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.PublicAccessTypeDef]

### S3ObjectDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.S3ObjectDetailTypeDef]]


# S3LogsConfigurationResultTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# S3LogsConfigurationTypeDef

### Enable
- **Type**: <class 'bool'>
- **Required**: Yes


# S3ObjectDetailTypeDef

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


# ScanConditionOutputTypeDef

### MapEquals
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ScanConditionPairTypeDef]
- **Required**: Yes


# ScanConditionPairTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# ScanConditionTypeDef

### MapEquals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.ScanConditionPairTypeDef]
- **Required**: Yes


# ScanDetectionsTypeDef

### ScannedItemCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ScannedItemCountTypeDef]

### ThreatsDetectedItemCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ThreatsDetectedItemCountTypeDef]

### HighestSeverityThreatDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.HighestSeverityThreatDetailsTypeDef]

### ThreatDetectedByName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ThreatDetectedByNameTypeDef]


# ScanEc2InstanceWithFindingsResultTypeDef

### EbsVolumes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.EbsVolumesResultTypeDef]


# ScanEc2InstanceWithFindingsTypeDef

### EbsVolumes
- **Type**: typing.Optional[bool]


# ScanFilePathTypeDef

### FilePath
- **Type**: typing.Optional[str]

### VolumeArn
- **Type**: typing.Optional[str]

### Hash
- **Type**: typing.Optional[str]

### FileName
- **Type**: typing.Optional[str]


# ScanResourceCriteriaOutputTypeDef

### Include
- **Type**: typing.Optional[typing.Dict[typing.Literal['EC2_INSTANCE_TAG'], aws_resource_validator.pydantic_models.guardduty_classes.ScanConditionOutputTypeDef]]

### Exclude
- **Type**: typing.Optional[typing.Dict[typing.Literal['EC2_INSTANCE_TAG'], aws_resource_validator.pydantic_models.guardduty_classes.ScanConditionOutputTypeDef]]


# ScanResourceCriteriaTypeDef

### Include
- **Type**: typing.Optional[typing.Mapping[typing.Literal['EC2_INSTANCE_TAG'], aws_resource_validator.pydantic_models.guardduty_classes.ScanConditionTypeDef]]

### Exclude
- **Type**: typing.Optional[typing.Mapping[typing.Literal['EC2_INSTANCE_TAG'], aws_resource_validator.pydantic_models.guardduty_classes.ScanConditionTypeDef]]


# ScanResultDetailsTypeDef

### ScanResult
- **Type**: typing.Optional[typing.Literal['CLEAN', 'INFECTED']]


# ScanThreatNameTypeDef

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### FilePaths
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ScanFilePathTypeDef]]


# ScanTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.TriggerDetailsTypeDef]

### ResourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ResourceDetailsTypeDef]

### ScanResultDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ScanResultDetailsTypeDef]

### AccountId
- **Type**: typing.Optional[str]

### TotalBytes
- **Type**: typing.Optional[int]

### FileCount
- **Type**: typing.Optional[int]

### AttachedVolumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.VolumeDetailTypeDef]]

### ScanType
- **Type**: typing.Optional[typing.Literal['GUARDDUTY_INITIATED', 'ON_DEMAND']]


# ScannedItemCountTypeDef

### TotalGb
- **Type**: typing.Optional[int]

### Files
- **Type**: typing.Optional[int]

### Volumes
- **Type**: typing.Optional[int]


# SecurityContextTypeDef

### Privileged
- **Type**: typing.Optional[bool]

### AllowPrivilegeEscalation
- **Type**: typing.Optional[bool]


# SecurityGroupTypeDef

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# ServiceAdditionalInfoTypeDef

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# ServiceTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ActionTypeDef]

### Evidence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.EvidenceTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ServiceAdditionalInfoTypeDef]

### FeatureName
- **Type**: typing.Optional[str]

### EbsVolumeScanDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.EbsVolumeScanDetailsTypeDef]

### RuntimeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.RuntimeDetailsTypeDef]

### Detection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DetectionTypeDef]

### MalwareScanDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.MalwareScanDetailsTypeDef]


# SortCriteriaTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### OrderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# StartMalwareScanRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartMalwareScanResponseTypeDef

### ScanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMonitoringMembersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StartMonitoringMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopMonitoringMembersRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StopMonitoringMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ThreatDetectedByNameTypeDef

### ItemCount
- **Type**: typing.Optional[int]

### UniqueThreatNameCount
- **Type**: typing.Optional[int]

### Shortened
- **Type**: typing.Optional[bool]

### ThreatNames
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ScanThreatNameTypeDef]]


# ThreatIntelligenceDetailTypeDef

### ThreatListName
- **Type**: typing.Optional[str]

### ThreatNames
- **Type**: typing.Optional[typing.List[str]]

### ThreatFileSha256
- **Type**: typing.Optional[str]


# ThreatTypeDef

### Name
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### ItemPaths
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.ItemPathTypeDef]]


# ThreatsDetectedItemCountTypeDef

### Files
- **Type**: typing.Optional[int]


# TotalTypeDef

### Amount
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# TriggerDetailsTypeDef

### GuardDutyFindingId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UnarchiveFindingsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UnprocessedAccountTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Result
- **Type**: <class 'str'>
- **Required**: Yes


# UnprocessedDataSourcesResultTypeDef

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionConfigurationResultTypeDef]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDetectorRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Enable
- **Type**: typing.Optional[bool]

### FindingPublishingFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']]

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceConfigurationsTypeDef]

### Features
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.DetectorFeatureConfigurationTypeDef]]


# UpdateFilterRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.FindingCriteriaTypeDef]


# UpdateFilterResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFindingsFeedbackRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### FindingIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Feedback
- **Type**: typing.Literal['NOT_USEFUL', 'USEFUL']
- **Required**: Yes

### Comments
- **Type**: typing.Optional[str]


# UpdateIPSetRequestRequestTypeDef

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


# UpdateMalwareProtectionPlanRequestRequestTypeDef

### MalwareProtectionPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.MalwareProtectionPlanActionsTypeDef]

### ProtectedResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.UpdateProtectedResourceTypeDef]


# UpdateMalwareScanSettingsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ScanResourceCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.ScanResourceCriteriaTypeDef]

### EbsSnapshotPreservation
- **Type**: typing.Optional[typing.Literal['NO_RETENTION', 'RETENTION_WITH_FINDING']]


# UpdateMemberDetectorsRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DataSourceConfigurationsTypeDef]

### Features
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.MemberFeaturesConfigurationTypeDef]]


# UpdateMemberDetectorsResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.guardduty_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateOrganizationConfigurationRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoEnable
- **Type**: typing.Optional[bool]

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationDataSourceConfigurationsTypeDef]

### Features
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.guardduty_classes.OrganizationFeatureConfigurationTypeDef]]

### AutoEnableOrganizationMembers
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]


# UpdateProtectedResourceTypeDef

### S3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.UpdateS3BucketResourceTypeDef]


# UpdatePublishingDestinationRequestRequestTypeDef

### DetectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.DestinationPropertiesTypeDef]


# UpdateS3BucketResourceTypeDef

### ObjectPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateThreatIntelSetRequestRequestTypeDef

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


# UsageAccountResultTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.TotalTypeDef]


# UsageCriteriaTypeDef

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DataSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EC2_MALWARE_SCAN', 'FLOW_LOGS', 'KUBERNETES_AUDIT_LOGS', 'S3_LOGS']]]

### Resources
- **Type**: typing.Optional[typing.Sequence[str]]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EC2_RUNTIME_MONITORING', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FARGATE_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_DBI_PROTECTION_PROVISIONED', 'RDS_DBI_PROTECTION_SERVERLESS', 'RDS_LOGIN_EVENTS', 'S3_DATA_EVENTS']]]


# UsageDataSourceResultTypeDef

### DataSource
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EC2_MALWARE_SCAN', 'FLOW_LOGS', 'KUBERNETES_AUDIT_LOGS', 'S3_LOGS']]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.TotalTypeDef]


# UsageFeatureResultTypeDef

### Feature
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EC2_RUNTIME_MONITORING', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FARGATE_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_DBI_PROTECTION_PROVISIONED', 'RDS_DBI_PROTECTION_SERVERLESS', 'RDS_LOGIN_EVENTS', 'S3_DATA_EVENTS']]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.TotalTypeDef]


# UsageResourceResultTypeDef

### Resource
- **Type**: typing.Optional[str]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.TotalTypeDef]


# UsageStatisticsTypeDef

### SumByAccount
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UsageAccountResultTypeDef]]

### TopAccountsByFeature
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UsageTopAccountsResultTypeDef]]

### SumByDataSource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UsageDataSourceResultTypeDef]]

### SumByResource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UsageResourceResultTypeDef]]

### TopResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UsageResourceResultTypeDef]]

### SumByFeature
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UsageFeatureResultTypeDef]]


# UsageTopAccountResultTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.TotalTypeDef]


# UsageTopAccountsResultTypeDef

### Feature
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL', 'DNS_LOGS', 'EBS_MALWARE_PROTECTION', 'EC2_RUNTIME_MONITORING', 'EKS_AUDIT_LOGS', 'EKS_RUNTIME_MONITORING', 'FARGATE_RUNTIME_MONITORING', 'FLOW_LOGS', 'LAMBDA_NETWORK_LOGS', 'RDS_DBI_PROTECTION_PROVISIONED', 'RDS_DBI_PROTECTION_SERVERLESS', 'RDS_LOGIN_EVENTS', 'S3_DATA_EVENTS']]

### Accounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.UsageTopAccountResultTypeDef]]


# VolumeDetailTypeDef

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


# VolumeMountTypeDef

### Name
- **Type**: typing.Optional[str]

### MountPath
- **Type**: typing.Optional[str]


# VolumeTypeDef

### Name
- **Type**: typing.Optional[str]

### HostPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.guardduty_classes.HostPathTypeDef]


# VpcConfigTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.guardduty_classes.SecurityGroupTypeDef]]


