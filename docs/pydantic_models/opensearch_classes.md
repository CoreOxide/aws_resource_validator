# Opensearch Classes

# AIMLOptionsInputTypeDef

### NaturalLanguageQueryGenerationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.NaturalLanguageQueryGenerationOptionsInputTypeDef]


# AIMLOptionsOutputTypeDef

### NaturalLanguageQueryGenerationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.NaturalLanguageQueryGenerationOptionsOutputTypeDef]


# AIMLOptionsStatusTypeDef

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AIMLOptionsOutputTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef]


# AWSDomainInformationTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# AcceptInboundConnectionRequestTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptInboundConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.InboundConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccessPoliciesStatusTypeDef

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# AddDataSourceRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DataSourceTypeTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# AddDataSourceResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddDirectQueryDataSourceRequestTypeDef

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DirectQueryDataSourceTypeTypeDef'>
- **Required**: Yes

### OpenSearchArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.TagTypeDef]]


# AddDirectQueryDataSourceResponseTypeDef

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddTagsRequestTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.TagTypeDef]
- **Required**: Yes


# AdditionalLimitTypeDef

### LimitName
- **Type**: typing.Optional[str]

### LimitValues
- **Type**: typing.Optional[typing.List[str]]


# AdvancedOptionsStatusTypeDef

### Options
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# AdvancedSecurityOptionsInputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### MasterUserOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.MasterUserOptionsTypeDef]

### SAMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SAMLOptionsInputTypeDef]

### JWTOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.JWTOptionsInputTypeDef]

### AnonymousAuthEnabled
- **Type**: typing.Optional[bool]


# AdvancedSecurityOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.AdvancedSecurityOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# AdvancedSecurityOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### SAMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SAMLOptionsOutputTypeDef]

### JWTOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.JWTOptionsOutputTypeDef]

### AnonymousAuthDisableDate
- **Type**: typing.Optional[datetime.datetime]

### AnonymousAuthEnabled
- **Type**: typing.Optional[bool]


# AppConfigTypeDef

### key
- **Type**: typing.Optional[typing.Literal['opensearchDashboards.dashboardAdmin.groups', 'opensearchDashboards.dashboardAdmin.users']]

### value
- **Type**: typing.Optional[str]


# ApplicationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociatePackageRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PrerequisitePackageIDList
- **Type**: typing.Optional[typing.Sequence[str]]

### AssociationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageAssociationConfigurationTypeDef]


# AssociatePackageResponseTypeDef

### DomainPackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainPackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatePackagesRequestTypeDef

### PackageList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.PackageDetailsForAssociationTypeDef]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatePackagesResponseTypeDef

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DomainPackageDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizeVpcEndpointAccessRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[typing.Literal['application.opensearchservice.amazonaws.com']]


# AuthorizeVpcEndpointAccessResponseTypeDef

### AuthorizedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.AuthorizedPrincipalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizedPrincipalTypeDef

### PrincipalType
- **Type**: typing.Optional[typing.Literal['AWS_ACCOUNT', 'AWS_SERVICE']]

### Principal
- **Type**: typing.Optional[str]


# AutoTuneDetailsTypeDef

### ScheduledAutoTuneDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ScheduledAutoTuneDetailsTypeDef]


# AutoTuneMaintenanceScheduleOutputTypeDef

### StartAt
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DurationTypeDef]

### CronExpressionForRecurrence
- **Type**: typing.Optional[str]


# AutoTuneMaintenanceScheduleTypeDef

### StartAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DurationTypeDef]

### CronExpressionForRecurrence
- **Type**: typing.Optional[str]


# AutoTuneMaintenanceScheduleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoTuneOptionsExtraTypeDef

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RollbackOnDisable
- **Type**: typing.Optional[typing.Literal['DEFAULT_ROLLBACK', 'NO_ROLLBACK']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneMaintenanceScheduleOutputTypeDef]]

### UseOffPeakWindow
- **Type**: typing.Optional[bool]


# AutoTuneOptionsInputTypeDef

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneMaintenanceScheduleUnionTypeDef]]

### UseOffPeakWindow
- **Type**: typing.Optional[bool]


# AutoTuneOptionsOutputTypeDef

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLED_AND_ROLLBACK_COMPLETE', 'DISABLED_AND_ROLLBACK_ERROR', 'DISABLED_AND_ROLLBACK_IN_PROGRESS', 'DISABLED_AND_ROLLBACK_SCHEDULED', 'DISABLE_IN_PROGRESS', 'ENABLED', 'ENABLE_IN_PROGRESS', 'ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]

### UseOffPeakWindow
- **Type**: typing.Optional[bool]


# AutoTuneOptionsStatusTypeDef

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneOptionsExtraTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneStatusTypeDef]


# AutoTuneOptionsTypeDef

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RollbackOnDisable
- **Type**: typing.Optional[typing.Literal['DEFAULT_ROLLBACK', 'NO_ROLLBACK']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneMaintenanceScheduleTypeDef]]

### UseOffPeakWindow
- **Type**: typing.Optional[bool]


# AutoTuneOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoTuneStatusTypeDef

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'DISABLED_AND_ROLLBACK_COMPLETE', 'DISABLED_AND_ROLLBACK_ERROR', 'DISABLED_AND_ROLLBACK_IN_PROGRESS', 'DISABLED_AND_ROLLBACK_SCHEDULED', 'DISABLE_IN_PROGRESS', 'ENABLED', 'ENABLE_IN_PROGRESS', 'ERROR']
- **Required**: Yes

### UpdateVersion
- **Type**: typing.Optional[int]

### ErrorMessage
- **Type**: typing.Optional[str]

### PendingDeletion
- **Type**: typing.Optional[bool]


# AutoTuneTypeDef

### AutoTuneType
- **Type**: typing.Optional[typing.Literal['SCHEDULED_ACTION']]

### AutoTuneDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneDetailsTypeDef]


# AvailabilityZoneInfoTypeDef

### AvailabilityZoneName
- **Type**: typing.Optional[str]

### ZoneStatus
- **Type**: typing.Optional[typing.Literal['Active', 'NotAvailable', 'StandBy']]

### ConfiguredDataNodeCount
- **Type**: typing.Optional[str]

### AvailableDataNodeCount
- **Type**: typing.Optional[str]

### TotalShards
- **Type**: typing.Optional[str]

### TotalUnAssignedShards
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelDomainConfigChangeRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# CancelDomainConfigChangeResponseTypeDef

### CancelledChangeIds
- **Type**: typing.List[str]
- **Required**: Yes

### CancelledChangeProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.CancelledChangePropertyTypeDef]
- **Required**: Yes

### DryRun
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelServiceSoftwareUpdateRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelServiceSoftwareUpdateResponseTypeDef

### ServiceSoftwareOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ServiceSoftwareOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelledChangePropertyTypeDef

### PropertyName
- **Type**: typing.Optional[str]

### CancelledValue
- **Type**: typing.Optional[str]

### ActiveValue
- **Type**: typing.Optional[str]


# ChangeProgressDetailsTypeDef

### ChangeId
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### ConfigChangeStatus
- **Type**: typing.Optional[typing.Literal['ApplyingChanges', 'Cancelled', 'Completed', 'Initializing', 'Pending', 'PendingUserInput', 'Validating', 'ValidationFailed']]

### InitiatedBy
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# ChangeProgressStageTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]


# ChangeProgressStatusDetailsTypeDef

### ChangeId
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'PENDING', 'PROCESSING']]

### PendingProperties
- **Type**: typing.Optional[typing.List[str]]

### CompletedProperties
- **Type**: typing.Optional[typing.List[str]]

### TotalNumberOfStages
- **Type**: typing.Optional[int]

### ChangeProgressStages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.ChangeProgressStageTypeDef]]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ConfigChangeStatus
- **Type**: typing.Optional[typing.Literal['ApplyingChanges', 'Cancelled', 'Completed', 'Initializing', 'Pending', 'PendingUserInput', 'Validating', 'ValidationFailed']]

### InitiatedBy
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


# CloudWatchDirectQueryDataSourceTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterConfigOutputTypeDef

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### InstanceCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ZoneAwarenessConfigTypeDef]

### DedicatedMasterType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### DedicatedMasterCount
- **Type**: typing.Optional[int]

### WarmEnabled
- **Type**: typing.Optional[bool]

### WarmType
- **Type**: typing.Optional[typing.Literal['ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### WarmCount
- **Type**: typing.Optional[int]

### ColdStorageOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ColdStorageOptionsTypeDef]

### MultiAZWithStandbyEnabled
- **Type**: typing.Optional[bool]

### NodeOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.NodeOptionTypeDef]]


# ClusterConfigStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ClusterConfigOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# ClusterConfigTypeDef

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### InstanceCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ZoneAwarenessConfigTypeDef]

### DedicatedMasterType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### DedicatedMasterCount
- **Type**: typing.Optional[int]

### WarmEnabled
- **Type**: typing.Optional[bool]

### WarmType
- **Type**: typing.Optional[typing.Literal['ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### WarmCount
- **Type**: typing.Optional[int]

### ColdStorageOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ColdStorageOptionsTypeDef]

### MultiAZWithStandbyEnabled
- **Type**: typing.Optional[bool]

### NodeOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.NodeOptionTypeDef]]


# ClusterConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CognitoOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.CognitoOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# CognitoOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### UserPoolId
- **Type**: typing.Optional[str]

### IdentityPoolId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# ColdStorageOptionsTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# CompatibleVersionsMapTypeDef

### SourceVersion
- **Type**: typing.Optional[str]

### TargetVersions
- **Type**: typing.Optional[typing.List[str]]


# ConnectionPropertiesTypeDef

### Endpoint
- **Type**: typing.Optional[str]

### CrossClusterSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.CrossClusterSearchConnectionPropertiesTypeDef]


# CreateApplicationRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### dataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.DataSourceTypeDef]]

### iamIdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.IamIdentityCenterOptionsInputTypeDef]

### appConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.AppConfigTypeDef]]

### tagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.TagTypeDef]]


# CreateDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: typing.Optional[str]

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ClusterConfigUnionTypeDef]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.EBSOptionsTypeDef]

### AccessPolicies
- **Type**: typing.Optional[str]

### IPAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4']]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SnapshotOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.VPCOptionsTypeDef]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.CognitoOptionsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.EncryptionAtRestOptionsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.NodeToNodeEncryptionOptionsTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.opensearch_classes.LogPublishingOptionTypeDef]]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DomainEndpointOptionsTypeDef]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AdvancedSecurityOptionsInputTypeDef]

### IdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.IdentityCenterOptionsInputTypeDef]

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.TagTypeDef]]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneOptionsInputTypeDef]

### OffPeakWindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OffPeakWindowOptionsTypeDef]

### SoftwareUpdateOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SoftwareUpdateOptionsTypeDef]

### AIMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AIMLOptionsInputTypeDef]


# CreateDomainResponseTypeDef

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOutboundConnectionRequestTypeDef

### LocalDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainInformationContainerTypeDef'>
- **Required**: Yes

### RemoteDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainInformationContainerTypeDef'>
- **Required**: Yes

### ConnectionAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionMode
- **Type**: typing.Optional[typing.Literal['DIRECT', 'VPC_ENDPOINT']]

### ConnectionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ConnectionPropertiesTypeDef]


# CreateOutboundConnectionResponseTypeDef

### LocalDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainInformationContainerTypeDef'>
- **Required**: Yes

### RemoteDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainInformationContainerTypeDef'>
- **Required**: Yes

### ConnectionAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OutboundConnectionStatusTypeDef'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionMode
- **Type**: typing.Literal['DIRECT', 'VPC_ENDPOINT']
- **Required**: Yes

### ConnectionProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ConnectionPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackageRequestTypeDef

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageType
- **Type**: typing.Literal['PACKAGE-CONFIG', 'PACKAGE-LICENSE', 'TXT-DICTIONARY', 'ZIP-PLUGIN']
- **Required**: Yes

### PackageSource
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.PackageSourceTypeDef'>
- **Required**: Yes

### PackageDescription
- **Type**: typing.Optional[str]

### PackageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageConfigurationTypeDef]

### EngineVersion
- **Type**: typing.Optional[str]

### PackageVendingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageVendingOptionsTypeDef]

### PackageEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageEncryptionOptionsTypeDef]


# CreatePackageResponseTypeDef

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.PackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcEndpointRequestTypeDef

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.VPCOptionsTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateVpcEndpointResponseTypeDef

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.VpcEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CrossClusterSearchConnectionPropertiesTypeDef

### SkipUnavailable
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DataSourceDetailsTypeDef

### DataSourceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DataSourceTypeTypeDef]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DISABLED']]


# DataSourceTypeDef

### dataSourceArn
- **Type**: typing.Optional[str]

### dataSourceDescription
- **Type**: typing.Optional[str]


# DataSourceTypeTypeDef

### S3GlueDataCatalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.S3GlueDataCatalogTypeDef]


# DeleteDataSourceRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDirectQueryDataSourceRequestTypeDef

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResponseTypeDef

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInboundConnectionRequestTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInboundConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.InboundConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteOutboundConnectionRequestTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutboundConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OutboundConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePackageRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePackageResponseTypeDef

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.PackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVpcEndpointRequestTypeDef

### VpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcEndpointResponseTypeDef

### VpcEndpointSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.VpcEndpointSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainAutoTunesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainAutoTunesResponseTypeDef

### AutoTunes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainChangeProgressRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeId
- **Type**: typing.Optional[str]


# DescribeDomainChangeProgressResponseTypeDef

### ChangeProgressStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ChangeProgressStatusDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainConfigRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainConfigResponseTypeDef

### DomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainHealthRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainHealthResponseTypeDef

### DomainState
- **Type**: typing.Literal['Active', 'NotAvailable', 'Processing']
- **Required**: Yes

### AvailabilityZoneCount
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveAvailabilityZoneCount
- **Type**: <class 'str'>
- **Required**: Yes

### StandByAvailabilityZoneCount
- **Type**: <class 'str'>
- **Required**: Yes

### DataNodeCount
- **Type**: <class 'str'>
- **Required**: Yes

### DedicatedMaster
- **Type**: <class 'bool'>
- **Required**: Yes

### MasterEligibleNodeCount
- **Type**: <class 'str'>
- **Required**: Yes

### WarmNodeCount
- **Type**: <class 'str'>
- **Required**: Yes

### MasterNode
- **Type**: typing.Literal['Available', 'UnAvailable']
- **Required**: Yes

### ClusterHealth
- **Type**: typing.Literal['Green', 'NotAvailable', 'Red', 'Yellow']
- **Required**: Yes

### TotalShards
- **Type**: <class 'str'>
- **Required**: Yes

### TotalUnAssignedShards
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentInformation
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.EnvironmentInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainNodesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainNodesResponseTypeDef

### DomainNodesStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DomainNodesStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainResponseTypeDef

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainsRequestTypeDef

### DomainNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeDomainsResponseTypeDef

### DomainStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DomainStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDryRunProgressRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRunId
- **Type**: typing.Optional[str]

### LoadDryRunConfig
- **Type**: typing.Optional[bool]


# DescribeDryRunProgressResponseTypeDef

### DryRunProgressStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DryRunProgressStatusTypeDef'>
- **Required**: Yes

### DryRunConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainStatusTypeDef'>
- **Required**: Yes

### DryRunResults
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DryRunResultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInboundConnectionsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInboundConnectionsResponseTypeDef

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.InboundConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceTypeLimitsRequestTypeDef

### InstanceType
- **Type**: typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]


# DescribeInstanceTypeLimitsResponseTypeDef

### LimitsByRole
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.opensearch_classes.LimitsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOutboundConnectionsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOutboundConnectionsResponseTypeDef

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.OutboundConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePackagesFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EngineVersion', 'PackageID', 'PackageName', 'PackageOwner', 'PackageStatus', 'PackageType']]

### Value
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribePackagesRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearch_classes.DescribePackagesFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePackagesResponseTypeDef

### PackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.PackageDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedInstanceOfferingsRequestTypeDef

### ReservedInstanceOfferingId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedInstanceOfferingsResponseTypeDef

### ReservedInstanceOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.ReservedInstanceOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedInstancesRequestTypeDef

### ReservedInstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedInstancesResponseTypeDef

### ReservedInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.ReservedInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVpcEndpointsRequestTypeDef

### VpcEndpointIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeVpcEndpointsResponseTypeDef

### VpcEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.VpcEndpointTypeDef]
- **Required**: Yes

### VpcEndpointErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.VpcEndpointErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DirectQueryDataSourceTypeDef

### DataSourceName
- **Type**: typing.Optional[str]

### DataSourceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DirectQueryDataSourceTypeTypeDef]

### Description
- **Type**: typing.Optional[str]

### OpenSearchArns
- **Type**: typing.Optional[typing.List[str]]

### DataSourceArn
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.TagTypeDef]]


# DirectQueryDataSourceTypeTypeDef

### CloudWatchLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.CloudWatchDirectQueryDataSourceTypeDef]

### SecurityLake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SecurityLakeDirectQueryDataSourceTypeDef]


# DissociatePackageRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DissociatePackageResponseTypeDef

### DomainPackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainPackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DissociatePackagesRequestTypeDef

### PackageList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DissociatePackagesResponseTypeDef

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DomainPackageDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainConfigTypeDef

### EngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.VersionStatusTypeDef]

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ClusterConfigStatusTypeDef]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.EBSOptionsStatusTypeDef]

### AccessPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AccessPoliciesStatusTypeDef]

### IPAddressType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.IPAddressTypeStatusTypeDef]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SnapshotOptionsStatusTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.VPCDerivedInfoStatusTypeDef]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.CognitoOptionsStatusTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.EncryptionAtRestOptionsStatusTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.NodeToNodeEncryptionOptionsStatusTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AdvancedOptionsStatusTypeDef]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.LogPublishingOptionsStatusTypeDef]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DomainEndpointOptionsStatusTypeDef]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AdvancedSecurityOptionsStatusTypeDef]

### IdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.IdentityCenterOptionsStatusTypeDef]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneOptionsStatusTypeDef]

### ChangeProgressDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ChangeProgressDetailsTypeDef]

### OffPeakWindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OffPeakWindowOptionsStatusTypeDef]

### SoftwareUpdateOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SoftwareUpdateOptionsStatusTypeDef]

### ModifyingProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.ModifyingPropertiesTypeDef]]

### AIMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AIMLOptionsStatusTypeDef]


# DomainEndpointOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainEndpointOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# DomainEndpointOptionsTypeDef

### EnforceHTTPS
- **Type**: typing.Optional[bool]

### TLSSecurityPolicy
- **Type**: typing.Optional[typing.Literal['Policy-Min-TLS-1-0-2019-07', 'Policy-Min-TLS-1-2-2019-07', 'Policy-Min-TLS-1-2-PFS-2023-10']]

### CustomEndpointEnabled
- **Type**: typing.Optional[bool]

### CustomEndpoint
- **Type**: typing.Optional[str]

### CustomEndpointCertificateArn
- **Type**: typing.Optional[str]


# DomainInfoTypeDef

### DomainName
- **Type**: typing.Optional[str]

### EngineType
- **Type**: typing.Optional[typing.Literal['Elasticsearch', 'OpenSearch']]


# DomainInformationContainerTypeDef

### AWSDomainInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AWSDomainInformationTypeDef]


# DomainMaintenanceDetailsTypeDef

### MaintenanceId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['REBOOT_NODE', 'RESTART_DASHBOARD', 'RESTART_SEARCH_PROCESS']]

### NodeId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'TIMED_OUT']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# DomainNodesStatusTypeDef

### NodeId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[typing.Literal['Data', 'Master', 'Ultrawarm']]

### AvailabilityZone
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### NodeStatus
- **Type**: typing.Optional[typing.Literal['Active', 'NotAvailable', 'StandBy']]

### StorageType
- **Type**: typing.Optional[str]

### StorageVolumeType
- **Type**: typing.Optional[typing.Literal['gp2', 'gp3', 'io1', 'standard']]

### StorageSize
- **Type**: typing.Optional[str]


# DomainPackageDetailsTypeDef

### PackageID
- **Type**: typing.Optional[str]

### PackageName
- **Type**: typing.Optional[str]

### PackageType
- **Type**: typing.Optional[typing.Literal['PACKAGE-CONFIG', 'PACKAGE-LICENSE', 'TXT-DICTIONARY', 'ZIP-PLUGIN']]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### DomainName
- **Type**: typing.Optional[str]

### DomainPackageStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ASSOCIATING', 'ASSOCIATION_FAILED', 'DISSOCIATING', 'DISSOCIATION_FAILED']]

### PackageVersion
- **Type**: typing.Optional[str]

### PrerequisitePackageIDList
- **Type**: typing.Optional[typing.List[str]]

### ReferencePath
- **Type**: typing.Optional[str]

### ErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ErrorDetailsTypeDef]

### AssociationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageAssociationConfigurationTypeDef]


# DomainStatusTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ClusterConfigOutputTypeDef'>
- **Required**: Yes

### Created
- **Type**: typing.Optional[bool]

### Deleted
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[str]

### EndpointV2
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Dict[str, str]]

### DomainEndpointV2HostedZoneId
- **Type**: typing.Optional[str]

### Processing
- **Type**: typing.Optional[bool]

### UpgradeProcessing
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.EBSOptionsTypeDef]

### AccessPolicies
- **Type**: typing.Optional[str]

### IPAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4']]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SnapshotOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.VPCDerivedInfoTypeDef]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.CognitoOptionsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.EncryptionAtRestOptionsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.NodeToNodeEncryptionOptionsTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.opensearch_classes.LogPublishingOptionTypeDef]]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ServiceSoftwareOptionsTypeDef]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DomainEndpointOptionsTypeDef]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AdvancedSecurityOptionsTypeDef]

### IdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.IdentityCenterOptionsTypeDef]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneOptionsOutputTypeDef]

### ChangeProgressDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ChangeProgressDetailsTypeDef]

### OffPeakWindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OffPeakWindowOptionsTypeDef]

### SoftwareUpdateOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SoftwareUpdateOptionsTypeDef]

### DomainProcessingStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Creating', 'Deleting', 'Isolated', 'Modifying', 'UpdatingServiceSoftware', 'UpgradingEngineVersion']]

### ModifyingProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.ModifyingPropertiesTypeDef]]

### AIMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AIMLOptionsOutputTypeDef]


# DryRunProgressStatusTypeDef

### DryRunId
- **Type**: <class 'str'>
- **Required**: Yes

### DryRunStatus
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateDate
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationFailures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.ValidationFailureTypeDef]]


# DryRunResultsTypeDef

### DeploymentType
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# DurationTypeDef

### Value
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['HOURS']]


# EBSOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.EBSOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# EBSOptionsTypeDef

### EBSEnabled
- **Type**: typing.Optional[bool]

### VolumeType
- **Type**: typing.Optional[typing.Literal['gp2', 'gp3', 'io1', 'standard']]

### VolumeSize
- **Type**: typing.Optional[int]

### Iops
- **Type**: typing.Optional[int]

### Throughput
- **Type**: typing.Optional[int]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionAtRestOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.EncryptionAtRestOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# EncryptionAtRestOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]


# EnvironmentInfoTypeDef

### AvailabilityZoneInformation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.AvailabilityZoneInfoTypeDef]]


# ErrorDetailsTypeDef

### ErrorType
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FilterTypeDef

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetCompatibleVersionsRequestTypeDef

### DomainName
- **Type**: typing.Optional[str]


# GetCompatibleVersionsResponseTypeDef

### CompatibleVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.CompatibleVersionsMapTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSourceRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceResponseTypeDef

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DataSourceTypeTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DISABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDirectQueryDataSourceRequestTypeDef

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDirectQueryDataSourceResponseTypeDef

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DirectQueryDataSourceTypeTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### OpenSearchArns
- **Type**: typing.List[str]
- **Required**: Yes

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainMaintenanceStatusRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaintenanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainMaintenanceStatusResponseTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'TIMED_OUT']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['REBOOT_NODE', 'RESTART_DASHBOARD', 'RESTART_SEARCH_PROCESS']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPackageVersionHistoryRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetPackageVersionHistoryResponseTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersionHistoryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.PackageVersionHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeHistoryRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeHistoryResponseTypeDef

### UpgradeHistories
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.UpgradeHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeStatusRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetUpgradeStatusResponseTypeDef

### UpgradeStep
- **Type**: typing.Literal['PRE_UPGRADE_CHECK', 'SNAPSHOT', 'UPGRADE']
- **Required**: Yes

### StepStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED', 'SUCCEEDED_WITH_ISSUES']
- **Required**: Yes

### UpgradeName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IPAddressTypeStatusTypeDef

### Options
- **Type**: typing.Literal['dualstack', 'ipv4']
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# IamIdentityCenterOptionsInputTypeDef

### enabled
- **Type**: typing.Optional[bool]

### iamIdentityCenterInstanceArn
- **Type**: typing.Optional[str]

### iamRoleForIdentityCenterApplicationArn
- **Type**: typing.Optional[str]


# IamIdentityCenterOptionsTypeDef

### enabled
- **Type**: typing.Optional[bool]

### iamIdentityCenterInstanceArn
- **Type**: typing.Optional[str]

### iamRoleForIdentityCenterApplicationArn
- **Type**: typing.Optional[str]

### iamIdentityCenterApplicationArn
- **Type**: typing.Optional[str]


# IdentityCenterOptionsInputTypeDef

### EnabledAPIAccess
- **Type**: typing.Optional[bool]

### IdentityCenterInstanceARN
- **Type**: typing.Optional[str]

### SubjectKey
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### RolesKey
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# IdentityCenterOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.IdentityCenterOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# IdentityCenterOptionsTypeDef

### EnabledAPIAccess
- **Type**: typing.Optional[bool]

### IdentityCenterInstanceARN
- **Type**: typing.Optional[str]

### SubjectKey
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### RolesKey
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]

### IdentityCenterApplicationARN
- **Type**: typing.Optional[str]

### IdentityStoreId
- **Type**: typing.Optional[str]


# InboundConnectionStatusTypeDef

### StatusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'APPROVED', 'DELETED', 'DELETING', 'PENDING_ACCEPTANCE', 'PROVISIONING', 'REJECTED', 'REJECTING']]

### Message
- **Type**: typing.Optional[str]


# InboundConnectionTypeDef

### LocalDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DomainInformationContainerTypeDef]

### RemoteDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DomainInformationContainerTypeDef]

### ConnectionId
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.InboundConnectionStatusTypeDef]

### ConnectionMode
- **Type**: typing.Optional[typing.Literal['DIRECT', 'VPC_ENDPOINT']]


# InstanceCountLimitsTypeDef

### MinimumInstanceCount
- **Type**: typing.Optional[int]

### MaximumInstanceCount
- **Type**: typing.Optional[int]


# InstanceLimitsTypeDef

### InstanceCountLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.InstanceCountLimitsTypeDef]


# InstanceTypeDetailsTypeDef

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### EncryptionEnabled
- **Type**: typing.Optional[bool]

### CognitoEnabled
- **Type**: typing.Optional[bool]

### AppLogsEnabled
- **Type**: typing.Optional[bool]

### AdvancedSecurityEnabled
- **Type**: typing.Optional[bool]

### WarmEnabled
- **Type**: typing.Optional[bool]

### InstanceRole
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]


# JWTOptionsInputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### PublicKey
- **Type**: typing.Optional[str]


# JWTOptionsOutputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### PublicKey
- **Type**: typing.Optional[str]


# KeyStoreAccessOptionTypeDef

### KeyStoreAccessEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### KeyAccessRoleArn
- **Type**: typing.Optional[str]


# LimitsTypeDef

### StorageTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.StorageTypeTypeDef]]

### InstanceLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.InstanceLimitsTypeDef]

### AdditionalLimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.AdditionalLimitTypeDef]]


# ListApplicationsRequestPaginateTypeDef

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]]

### maxResults
- **Type**: typing.Optional[int]


# ListApplicationsResponseTypeDef

### ApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# ListDataSourcesResponseTypeDef

### DataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DataSourceDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDirectQueryDataSourcesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListDirectQueryDataSourcesResponseTypeDef

### DirectQueryDataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DirectQueryDataSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainMaintenancesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[typing.Literal['REBOOT_NODE', 'RESTART_DASHBOARD', 'RESTART_SEARCH_PROCESS']]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'TIMED_OUT']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainMaintenancesResponseTypeDef

### DomainMaintenances
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DomainMaintenanceDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainNamesRequestTypeDef

### EngineType
- **Type**: typing.Optional[typing.Literal['Elasticsearch', 'OpenSearch']]


# ListDomainNamesResponseTypeDef

### DomainNames
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DomainInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainsForPackageRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsForPackageResponseTypeDef

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DomainPackageDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstanceTypeDetailsRequestTypeDef

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RetrieveAZs
- **Type**: typing.Optional[bool]

### InstanceType
- **Type**: typing.Optional[str]


# ListInstanceTypeDetailsResponseTypeDef

### InstanceTypeDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.InstanceTypeDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesForDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesForDomainResponseTypeDef

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.DomainPackageDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsResponseTypeDef

### ScheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.ScheduledActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequestTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVersionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVersionsResponseTypeDef

### Versions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointAccessRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointAccessResponseTypeDef

### AuthorizedPrincipalList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.AuthorizedPrincipalTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcEndpointsForDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointsForDomainResponseTypeDef

### VpcEndpointSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.VpcEndpointSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcEndpointsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointsResponseTypeDef

### VpcEndpointSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch_classes.VpcEndpointSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogPublishingOptionTypeDef

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# LogPublishingOptionsStatusTypeDef

### Options
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.opensearch_classes.LogPublishingOptionTypeDef]]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef]


# MasterUserOptionsTypeDef

### MasterUserARN
- **Type**: typing.Optional[str]

### MasterUserName
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]


# ModifyingPropertiesTypeDef

### Name
- **Type**: typing.Optional[str]

### ActiveValue
- **Type**: typing.Optional[str]

### PendingValue
- **Type**: typing.Optional[str]

### ValueType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT', 'STRINGIFIED_JSON']]


# NaturalLanguageQueryGenerationOptionsInputTypeDef

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# NaturalLanguageQueryGenerationOptionsOutputTypeDef

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CurrentState
- **Type**: typing.Optional[typing.Literal['DISABLE_COMPLETE', 'DISABLE_FAILED', 'DISABLE_IN_PROGRESS', 'ENABLE_COMPLETE', 'ENABLE_FAILED', 'ENABLE_IN_PROGRESS', 'NOT_ENABLED']]


# NodeConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeOptionTypeDef

### NodeType
- **Type**: typing.Optional[typing.Literal['coordinator']]

### NodeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.NodeConfigTypeDef]


# NodeToNodeEncryptionOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.NodeToNodeEncryptionOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# NodeToNodeEncryptionOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# OffPeakWindowOptionsStatusTypeDef

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OffPeakWindowOptionsTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef]


# OffPeakWindowOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### OffPeakWindow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OffPeakWindowTypeDef]


# OffPeakWindowTypeDef

### WindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.WindowStartTimeTypeDef]


# OptionStatusTypeDef

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['Active', 'Processing', 'RequiresIndexDocuments']
- **Required**: Yes

### UpdateVersion
- **Type**: typing.Optional[int]

### PendingDeletion
- **Type**: typing.Optional[bool]


# OutboundConnectionStatusTypeDef

### StatusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'APPROVED', 'DELETED', 'DELETING', 'PENDING_ACCEPTANCE', 'PROVISIONING', 'REJECTED', 'REJECTING', 'VALIDATING', 'VALIDATION_FAILED']]

### Message
- **Type**: typing.Optional[str]


# OutboundConnectionTypeDef

### LocalDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DomainInformationContainerTypeDef]

### RemoteDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DomainInformationContainerTypeDef]

### ConnectionId
- **Type**: typing.Optional[str]

### ConnectionAlias
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OutboundConnectionStatusTypeDef]

### ConnectionMode
- **Type**: typing.Optional[typing.Literal['DIRECT', 'VPC_ENDPOINT']]

### ConnectionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ConnectionPropertiesTypeDef]


# PackageAssociationConfigurationTypeDef

### KeyStoreAccessOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.KeyStoreAccessOptionTypeDef]


# PackageConfigurationTypeDef

### LicenseRequirement
- **Type**: typing.Literal['NONE', 'OPTIONAL', 'REQUIRED']
- **Required**: Yes

### ConfigurationRequirement
- **Type**: typing.Literal['NONE', 'OPTIONAL', 'REQUIRED']
- **Required**: Yes

### LicenseFilepath
- **Type**: typing.Optional[str]

### RequiresRestartForConfigurationUpdate
- **Type**: typing.Optional[bool]


# PackageDetailsForAssociationTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### PrerequisitePackageIDList
- **Type**: typing.Optional[typing.Sequence[str]]

### AssociationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageAssociationConfigurationTypeDef]


# PackageDetailsTypeDef

### PackageID
- **Type**: typing.Optional[str]

### PackageName
- **Type**: typing.Optional[str]

### PackageType
- **Type**: typing.Optional[typing.Literal['PACKAGE-CONFIG', 'PACKAGE-LICENSE', 'TXT-DICTIONARY', 'ZIP-PLUGIN']]

### PackageDescription
- **Type**: typing.Optional[str]

### PackageStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'COPYING', 'COPY_FAILED', 'DELETED', 'DELETE_FAILED', 'DELETING', 'VALIDATING', 'VALIDATION_FAILED']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### AvailablePackageVersion
- **Type**: typing.Optional[str]

### ErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ErrorDetailsTypeDef]

### EngineVersion
- **Type**: typing.Optional[str]

### AvailablePluginProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PluginPropertiesTypeDef]

### AvailablePackageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageConfigurationTypeDef]

### AllowListedUserList
- **Type**: typing.Optional[typing.List[str]]

### PackageOwner
- **Type**: typing.Optional[str]

### PackageVendingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageVendingOptionsTypeDef]

### PackageEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageEncryptionOptionsTypeDef]


# PackageEncryptionOptionsTypeDef

### EncryptionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### KmsKeyIdentifier
- **Type**: typing.Optional[str]


# PackageSourceTypeDef

### S3BucketName
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]


# PackageVendingOptionsTypeDef

### VendingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# PackageVersionHistoryTypeDef

### PackageVersion
- **Type**: typing.Optional[str]

### CommitMessage
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### PluginProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PluginPropertiesTypeDef]

### PackageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageConfigurationTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PluginPropertiesTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### ClassName
- **Type**: typing.Optional[str]

### UncompressedSizeInBytes
- **Type**: typing.Optional[int]


# PurchaseReservedInstanceOfferingRequestTypeDef

### ReservedInstanceOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: typing.Optional[int]


# PurchaseReservedInstanceOfferingResponseTypeDef

### ReservedInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecurringChargeTypeDef

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RejectInboundConnectionRequestTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# RejectInboundConnectionResponseTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.InboundConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsRequestTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReservedInstanceOfferingTypeDef

### ReservedInstanceOfferingId
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### UsagePrice
- **Type**: typing.Optional[float]

### CurrencyCode
- **Type**: typing.Optional[str]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.RecurringChargeTypeDef]]


# ReservedInstanceTypeDef

### ReservationName
- **Type**: typing.Optional[str]

### ReservedInstanceId
- **Type**: typing.Optional[str]

### BillingSubscriptionId
- **Type**: typing.Optional[int]

### ReservedInstanceOfferingId
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### UsagePrice
- **Type**: typing.Optional[float]

### CurrencyCode
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[str]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.RecurringChargeTypeDef]]


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


# RevokeVpcEndpointAccessRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[typing.Literal['application.opensearchservice.amazonaws.com']]


# S3GlueDataCatalogTypeDef

### RoleArn
- **Type**: typing.Optional[str]


# SAMLIdpTypeDef

### MetadataContent
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# SAMLOptionsInputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### Idp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SAMLIdpTypeDef]

### MasterUserName
- **Type**: typing.Optional[str]

### MasterBackendRole
- **Type**: typing.Optional[str]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### SessionTimeoutMinutes
- **Type**: typing.Optional[int]


# SAMLOptionsOutputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### Idp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SAMLIdpTypeDef]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### SessionTimeoutMinutes
- **Type**: typing.Optional[int]


# ScheduledActionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduledAutoTuneDetailsTypeDef

### Date
- **Type**: typing.Optional[datetime.datetime]

### ActionType
- **Type**: typing.Optional[typing.Literal['JVM_HEAP_SIZE_TUNING', 'JVM_YOUNG_GEN_TUNING']]

### Action
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# SecurityLakeDirectQueryDataSourceTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceSoftwareOptionsTypeDef

### CurrentVersion
- **Type**: typing.Optional[str]

### NewVersion
- **Type**: typing.Optional[str]

### UpdateAvailable
- **Type**: typing.Optional[bool]

### Cancellable
- **Type**: typing.Optional[bool]

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'ELIGIBLE', 'IN_PROGRESS', 'NOT_ELIGIBLE', 'PENDING_UPDATE']]

### Description
- **Type**: typing.Optional[str]

### AutomatedUpdateDate
- **Type**: typing.Optional[datetime.datetime]

### OptionalDeployment
- **Type**: typing.Optional[bool]


# SnapshotOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.SnapshotOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# SnapshotOptionsTypeDef

### AutomatedSnapshotStartHour
- **Type**: typing.Optional[int]


# SoftwareUpdateOptionsStatusTypeDef

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SoftwareUpdateOptionsTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef]


# SoftwareUpdateOptionsTypeDef

### AutoSoftwareUpdateEnabled
- **Type**: typing.Optional[bool]


# StartDomainMaintenanceRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['REBOOT_NODE', 'RESTART_DASHBOARD', 'RESTART_SEARCH_PROCESS']
- **Required**: Yes

### NodeId
- **Type**: typing.Optional[str]


# StartDomainMaintenanceResponseTypeDef

### MaintenanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartServiceSoftwareUpdateRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleAt
- **Type**: typing.Optional[typing.Literal['NOW', 'OFF_PEAK_WINDOW', 'TIMESTAMP']]

### DesiredStartTime
- **Type**: typing.Optional[int]


# StartServiceSoftwareUpdateResponseTypeDef

### ServiceSoftwareOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ServiceSoftwareOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StorageTypeLimitTypeDef

### LimitName
- **Type**: typing.Optional[str]

### LimitValues
- **Type**: typing.Optional[typing.List[str]]


# StorageTypeTypeDef

### StorageTypeName
- **Type**: typing.Optional[str]

### StorageSubTypeName
- **Type**: typing.Optional[str]

### StorageTypeLimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.StorageTypeLimitTypeDef]]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateDataSourceRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DataSourceTypeTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DISABLED']]


# UpdateDataSourceResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDirectQueryDataSourceRequestTypeDef

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DirectQueryDataSourceTypeTypeDef'>
- **Required**: Yes

### OpenSearchArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateDirectQueryDataSourceResponseTypeDef

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainConfigRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.ClusterConfigUnionTypeDef]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.EBSOptionsTypeDef]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SnapshotOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.VPCOptionsTypeDef]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.CognitoOptionsTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessPolicies
- **Type**: typing.Optional[str]

### IPAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4']]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.opensearch_classes.LogPublishingOptionTypeDef]]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.EncryptionAtRestOptionsTypeDef]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.DomainEndpointOptionsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.NodeToNodeEncryptionOptionsTypeDef]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AdvancedSecurityOptionsInputTypeDef]

### IdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.IdentityCenterOptionsInputTypeDef]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AutoTuneOptionsUnionTypeDef]

### DryRun
- **Type**: typing.Optional[bool]

### DryRunMode
- **Type**: typing.Optional[typing.Literal['Basic', 'Verbose']]

### OffPeakWindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.OffPeakWindowOptionsTypeDef]

### SoftwareUpdateOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.SoftwareUpdateOptionsTypeDef]

### AIMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.AIMLOptionsInputTypeDef]


# UpdateDomainConfigResponseTypeDef

### DomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DomainConfigTypeDef'>
- **Required**: Yes

### DryRunResults
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DryRunResultsTypeDef'>
- **Required**: Yes

### DryRunProgressStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.DryRunProgressStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePackageRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### PackageSource
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.PackageSourceTypeDef'>
- **Required**: Yes

### PackageDescription
- **Type**: typing.Optional[str]

### CommitMessage
- **Type**: typing.Optional[str]

### PackageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageConfigurationTypeDef]

### PackageEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.PackageEncryptionOptionsTypeDef]


# UpdatePackageResponseTypeDef

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.PackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePackageScopeRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['ADD', 'OVERRIDE', 'REMOVE']
- **Required**: Yes

### PackageUserList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdatePackageScopeResponseTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['ADD', 'OVERRIDE', 'REMOVE']
- **Required**: Yes

### PackageUserList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScheduledActionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionID
- **Type**: <class 'str'>
- **Required**: Yes

### ActionType
- **Type**: typing.Literal['JVM_HEAP_SIZE_TUNING', 'JVM_YOUNG_GEN_TUNING', 'SERVICE_SOFTWARE_UPDATE']
- **Required**: Yes

### ScheduleAt
- **Type**: typing.Literal['NOW', 'OFF_PEAK_WINDOW', 'TIMESTAMP']
- **Required**: Yes

### DesiredStartTime
- **Type**: typing.Optional[int]


# UpdateScheduledActionResponseTypeDef

### ScheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ScheduledActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVpcEndpointRequestTypeDef

### VpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.VPCOptionsTypeDef'>
- **Required**: Yes


# UpdateVpcEndpointResponseTypeDef

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.VpcEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpgradeDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PerformCheckOnly
- **Type**: typing.Optional[bool]

### AdvancedOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpgradeDomainResponseTypeDef

### UpgradeId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PerformCheckOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### AdvancedOptions
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ChangeProgressDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ChangeProgressDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpgradeHistoryTypeDef

### UpgradeName
- **Type**: typing.Optional[str]

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpgradeStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED', 'SUCCEEDED_WITH_ISSUES']]

### StepsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch_classes.UpgradeStepItemTypeDef]]


# UpgradeStepItemTypeDef

### UpgradeStep
- **Type**: typing.Optional[typing.Literal['PRE_UPGRADE_CHECK', 'SNAPSHOT', 'UPGRADE']]

### UpgradeStepStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED', 'SUCCEEDED_WITH_ISSUES']]

### Issues
- **Type**: typing.Optional[typing.List[str]]

### ProgressPercent
- **Type**: typing.Optional[float]


# VPCDerivedInfoStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.VPCDerivedInfoTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# VPCDerivedInfoTypeDef

### VPCId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VPCOptionsTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ValidationFailureTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# VersionStatusTypeDef

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# VpcEndpointErrorTypeDef

### VpcEndpointId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['ENDPOINT_NOT_FOUND', 'SERVER_ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]


# VpcEndpointSummaryTypeDef

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcEndpointOwner
- **Type**: typing.Optional[str]

### DomainArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]


# VpcEndpointTypeDef

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcEndpointOwner
- **Type**: typing.Optional[str]

### DomainArn
- **Type**: typing.Optional[str]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch_classes.VPCDerivedInfoTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### Endpoint
- **Type**: typing.Optional[str]


# WindowStartTimeTypeDef

### Hours
- **Type**: <class 'int'>
- **Required**: Yes

### Minutes
- **Type**: <class 'int'>
- **Required**: Yes


# ZoneAwarenessConfigTypeDef

### AvailabilityZoneCount
- **Type**: typing.Optional[int]


