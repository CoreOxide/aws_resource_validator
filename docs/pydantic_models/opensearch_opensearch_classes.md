# Opensearch Opensearch Classes

# AIMLOptionsInput

### NaturalLanguageQueryGenerationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.NaturalLanguageQueryGenerationOptionsInput]


# AIMLOptionsOutput

### NaturalLanguageQueryGenerationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.NaturalLanguageQueryGenerationOptionsOutput]


# AIMLOptionsStatus

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AIMLOptionsOutput]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus]


# AWSDomainInformation

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# AcceptInboundConnectionRequest

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptInboundConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.InboundConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# AccessPoliciesStatus

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# AddDataSourceRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSourceType'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# AddDataSourceResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# AddDirectQueryDataSourceRequest

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DirectQueryDataSourceType'>
- **Required**: Yes

### OpenSearchArns
- **Type**: typing.List[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Tag]]


# AddDirectQueryDataSourceResponse

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsRequest

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Tag]
- **Required**: Yes


# AdditionalLimit

### LimitName
- **Type**: typing.Optional[str]

### LimitValues
- **Type**: typing.Optional[typing.List[str]]


# AdvancedOptionsStatus

### Options
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# AdvancedSecurityOptions

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### SAMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SAMLOptionsOutput]

### JWTOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.JWTOptionsOutput]

### AnonymousAuthDisableDate
- **Type**: typing.Optional[datetime.datetime]

### AnonymousAuthEnabled
- **Type**: typing.Optional[bool]


# AdvancedSecurityOptionsInput

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### MasterUserOptions
- **Type**: <class 'NoneType'>

### SAMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SAMLOptionsInput]

### JWTOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.JWTOptionsInput]

### AnonymousAuthEnabled
- **Type**: typing.Optional[bool]


# AdvancedSecurityOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AdvancedSecurityOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# AppConfig

### key
- **Type**: typing.Optional[typing.Literal['opensearchDashboards.dashboardAdmin.groups', 'opensearchDashboards.dashboardAdmin.users']]

### value
- **Type**: typing.Optional[str]


# ApplicationSummary

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### endpoint
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# AssociatePackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PrerequisitePackageIDList
- **Type**: typing.Optional[typing.List[str]]

### AssociationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageAssociationConfiguration]


# AssociatePackageResponse

### DomainPackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainPackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatePackagesRequest

### PackageList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageDetailsForAssociation]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatePackagesResponse

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainPackageDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# AuthorizeVpcEndpointAccessRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[typing.Literal['application.opensearchservice.amazonaws.com']]


# AuthorizeVpcEndpointAccessResponse

### AuthorizedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AuthorizedPrincipal'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# AuthorizedPrincipal

### PrincipalType
- **Type**: typing.Optional[typing.Literal['AWS_ACCOUNT', 'AWS_SERVICE']]

### Principal
- **Type**: typing.Optional[str]


# AutoTune

### AutoTuneType
- **Type**: typing.Optional[typing.Literal['SCHEDULED_ACTION']]

### AutoTuneDetails
- **Type**: <class 'NoneType'>


# AutoTuneDetails

### ScheduledAutoTuneDetails
- **Type**: <class 'NoneType'>


# AutoTuneMaintenanceSchedule

### StartAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: <class 'NoneType'>

### CronExpressionForRecurrence
- **Type**: typing.Optional[str]


# AutoTuneMaintenanceScheduleOutput

### StartAt
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: <class 'NoneType'>

### CronExpressionForRecurrence
- **Type**: typing.Optional[str]


# AutoTuneOptions

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RollbackOnDisable
- **Type**: typing.Optional[typing.Literal['DEFAULT_ROLLBACK', 'NO_ROLLBACK']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneMaintenanceSchedule]]

### UseOffPeakWindow
- **Type**: typing.Optional[bool]


# AutoTuneOptionsExtra

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RollbackOnDisable
- **Type**: typing.Optional[typing.Literal['DEFAULT_ROLLBACK', 'NO_ROLLBACK']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneMaintenanceScheduleOutput]]

### UseOffPeakWindow
- **Type**: typing.Optional[bool]


# AutoTuneOptionsInput

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneMaintenanceSchedule, aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneMaintenanceScheduleOutput]]]

### UseOffPeakWindow
- **Type**: typing.Optional[bool]


# AutoTuneOptionsOutput

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLED_AND_ROLLBACK_COMPLETE', 'DISABLED_AND_ROLLBACK_ERROR', 'DISABLED_AND_ROLLBACK_IN_PROGRESS', 'DISABLED_AND_ROLLBACK_SCHEDULED', 'DISABLE_IN_PROGRESS', 'ENABLED', 'ENABLE_IN_PROGRESS', 'ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]

### UseOffPeakWindow
- **Type**: typing.Optional[bool]


# AutoTuneOptionsStatus

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneOptionsExtra]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneStatus]


# AutoTuneStatus

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


# AvailabilityZoneInfo

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

# CancelDomainConfigChangeRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# CancelDomainConfigChangeResponse

### CancelledChangeIds
- **Type**: typing.List[str]
- **Required**: Yes

### CancelledChangeProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.CancelledChangeProperty]
- **Required**: Yes

### DryRun
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# CancelServiceSoftwareUpdateRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelServiceSoftwareUpdateResponse

### ServiceSoftwareOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ServiceSoftwareOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# CancelledChangeProperty

### PropertyName
- **Type**: typing.Optional[str]

### CancelledValue
- **Type**: typing.Optional[str]

### ActiveValue
- **Type**: typing.Optional[str]


# ChangeProgressDetails

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


# ChangeProgressStage

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]


# ChangeProgressStatusDetails

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ChangeProgressStage]]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ConfigChangeStatus
- **Type**: typing.Optional[typing.Literal['ApplyingChanges', 'Cancelled', 'Completed', 'Initializing', 'Pending', 'PendingUserInput', 'Validating', 'ValidationFailed']]

### InitiatedBy
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


# CloudWatchDirectQueryDataSource

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterConfig

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### InstanceCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessConfig
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

### MultiAZWithStandbyEnabled
- **Type**: typing.Optional[bool]

### NodeOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.NodeOption]]


# ClusterConfigOutput

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### InstanceCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessConfig
- **Type**: <class 'NoneType'>

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
- **Type**: <class 'NoneType'>

### MultiAZWithStandbyEnabled
- **Type**: typing.Optional[bool]

### NodeOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.NodeOption]]


# ClusterConfigStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ClusterConfigOutput'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# CognitoOptions

### Enabled
- **Type**: typing.Optional[bool]

### UserPoolId
- **Type**: typing.Optional[str]

### IdentityPoolId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# CognitoOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.CognitoOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# ColdStorageOptions

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# CompatibleVersionsMap

### SourceVersion
- **Type**: typing.Optional[str]

### TargetVersions
- **Type**: typing.Optional[typing.List[str]]


# ConnectionProperties

### Endpoint
- **Type**: typing.Optional[str]

### CrossClusterSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.CrossClusterSearchConnectionProperties]


# CreateApplicationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### dataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSource]]

### iamIdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IamIdentityCenterOptionsInput]

### appConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AppConfig]]

### tagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Tag]]


# CreateApplicationResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSource]
- **Required**: Yes

### iamIdentityCenterOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IamIdentityCenterOptions'>
- **Required**: Yes

### appConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AppConfig]
- **Required**: Yes

### tagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Tag]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineVersion
- **Type**: typing.Optional[str]

### ClusterConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ClusterConfig, aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ClusterConfigOutput, NoneType]

### EBSOptions
- **Type**: <class 'NoneType'>

### AccessPolicies
- **Type**: typing.Optional[str]

### IPAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4']]

### SnapshotOptions
- **Type**: <class 'NoneType'>

### VPCOptions
- **Type**: <class 'NoneType'>

### CognitoOptions
- **Type**: <class 'NoneType'>

### EncryptionAtRestOptions
- **Type**: <class 'NoneType'>

### NodeToNodeEncryptionOptions
- **Type**: <class 'NoneType'>

### AdvancedOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.opensearch.opensearch_classes.LogPublishingOption]]

### DomainEndpointOptions
- **Type**: <class 'NoneType'>

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AdvancedSecurityOptionsInput]

### IdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IdentityCenterOptionsInput]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Tag]]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneOptionsInput]

### OffPeakWindowOptions
- **Type**: <class 'NoneType'>

### SoftwareUpdateOptions
- **Type**: <class 'NoneType'>

### AIMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AIMLOptionsInput]


# CreateDomainResponse

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOutboundConnectionRequest

### LocalDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInformationContainer'>
- **Required**: Yes

### RemoteDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInformationContainer'>
- **Required**: Yes

### ConnectionAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionMode
- **Type**: typing.Optional[typing.Literal['DIRECT', 'VPC_ENDPOINT']]

### ConnectionProperties
- **Type**: <class 'NoneType'>


# CreateOutboundConnectionResponse

### LocalDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInformationContainer'>
- **Required**: Yes

### RemoteDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInformationContainer'>
- **Required**: Yes

### ConnectionAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OutboundConnectionStatus'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionMode
- **Type**: typing.Literal['DIRECT', 'VPC_ENDPOINT']
- **Required**: Yes

### ConnectionProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ConnectionProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackageRequest

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageType
- **Type**: typing.Literal['PACKAGE-CONFIG', 'PACKAGE-LICENSE', 'TXT-DICTIONARY', 'ZIP-PLUGIN']
- **Required**: Yes

### PackageSource
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageSource'>
- **Required**: Yes

### PackageDescription
- **Type**: typing.Optional[str]

### PackageConfiguration
- **Type**: <class 'NoneType'>

### EngineVersion
- **Type**: typing.Optional[str]

### PackageVendingOptions
- **Type**: <class 'NoneType'>

### PackageEncryptionOptions
- **Type**: <class 'NoneType'>


# CreatePackageResponse

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcEndpointRequest

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VPCOptions'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateVpcEndpointResponse

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VpcEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# CrossClusterSearchConnectionProperties

### SkipUnavailable
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DataSource

### dataSourceArn
- **Type**: typing.Optional[str]

### dataSourceDescription
- **Type**: typing.Optional[str]


# DataSourceDetails

### DataSourceType
- **Type**: <class 'NoneType'>

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DISABLED']]


# DataSourceType

### S3GlueDataCatalog
- **Type**: <class 'NoneType'>


# DeleteApplicationRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDirectQueryDataSourceRequest

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResponse

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInboundConnectionRequest

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInboundConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.InboundConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteOutboundConnectionRequest

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutboundConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OutboundConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePackageResponse

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVpcEndpointRequest

### VpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcEndpointResponse

### VpcEndpointSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VpcEndpointSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainAutoTunesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainAutoTunesResponse

### AutoTunes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTune]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainChangeProgressRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeId
- **Type**: typing.Optional[str]


# DescribeDomainChangeProgressResponse

### ChangeProgressStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ChangeProgressStatusDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainConfigRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainConfigResponse

### DomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainHealthRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainHealthResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.EnvironmentInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainNodesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainNodesResponse

### DomainNodesStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainNodesStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainResponse

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainsRequest

### DomainNames
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeDomainsResponse

### DomainStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDryRunProgressRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRunId
- **Type**: typing.Optional[str]

### LoadDryRunConfig
- **Type**: typing.Optional[bool]


# DescribeDryRunProgressResponse

### DryRunProgressStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DryRunProgressStatus'>
- **Required**: Yes

### DryRunConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainStatus'>
- **Required**: Yes

### DryRunResults
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DryRunResults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInboundConnectionsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInboundConnectionsResponse

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.InboundConnection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceTypeLimitsRequest

### InstanceType
- **Type**: typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]


# DescribeInstanceTypeLimitsResponse

### LimitsByRole
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Limits]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOutboundConnectionsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOutboundConnectionsResponse

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OutboundConnection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePackagesFilter

### Name
- **Type**: typing.Optional[typing.Literal['EngineVersion', 'PackageID', 'PackageName', 'PackageOwner', 'PackageStatus', 'PackageType']]

### Value
- **Type**: typing.Optional[typing.List[str]]


# DescribePackagesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DescribePackagesFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePackagesResponse

### PackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedInstanceOfferingsRequest

### ReservedInstanceOfferingId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedInstanceOfferingsResponse

### ReservedInstanceOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ReservedInstanceOffering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedInstancesRequest

### ReservedInstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedInstancesResponse

### ReservedInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ReservedInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVpcEndpointsRequest

### VpcEndpointIds
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeVpcEndpointsResponse

### VpcEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VpcEndpoint]
- **Required**: Yes

### VpcEndpointErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VpcEndpointError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DirectQueryDataSource

### DataSourceName
- **Type**: typing.Optional[str]

### DataSourceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DirectQueryDataSourceType]

### Description
- **Type**: typing.Optional[str]

### OpenSearchArns
- **Type**: typing.Optional[typing.List[str]]

### DataSourceArn
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Tag]]


# DirectQueryDataSourceType

### CloudWatchLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.CloudWatchDirectQueryDataSource]

### SecurityLake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SecurityLakeDirectQueryDataSource]


# DissociatePackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DissociatePackageResponse

### DomainPackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainPackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DissociatePackagesRequest

### PackageList
- **Type**: typing.List[str]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DissociatePackagesResponse

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainPackageDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# DomainConfig

### EngineVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VersionStatus]

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ClusterConfigStatus]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.EBSOptionsStatus]

### AccessPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AccessPoliciesStatus]

### IPAddressType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IPAddressTypeStatus]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SnapshotOptionsStatus]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VPCDerivedInfoStatus]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.CognitoOptionsStatus]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.EncryptionAtRestOptionsStatus]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.NodeToNodeEncryptionOptionsStatus]

### AdvancedOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AdvancedOptionsStatus]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.LogPublishingOptionsStatus]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainEndpointOptionsStatus]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AdvancedSecurityOptionsStatus]

### IdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IdentityCenterOptionsStatus]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneOptionsStatus]

### ChangeProgressDetails
- **Type**: <class 'NoneType'>

### OffPeakWindowOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OffPeakWindowOptionsStatus]

### SoftwareUpdateOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SoftwareUpdateOptionsStatus]

### ModifyingProperties
- **Type**: typing.Optional[typing.List[NoneType]]

### AIMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AIMLOptionsStatus]


# DomainEndpointOptions

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


# DomainEndpointOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainEndpointOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# DomainInfo

### DomainName
- **Type**: typing.Optional[str]

### EngineType
- **Type**: typing.Optional[typing.Literal['Elasticsearch', 'OpenSearch']]


# DomainInformationContainer

### AWSDomainInformation
- **Type**: <class 'NoneType'>


# DomainMaintenanceDetails

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


# DomainNodesStatus

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


# DomainPackageDetails

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
- **Type**: <class 'NoneType'>

### AssociationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageAssociationConfiguration]


# DomainStatus

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
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ClusterConfigOutput'>
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
- **Type**: <class 'NoneType'>

### AccessPolicies
- **Type**: typing.Optional[str]

### IPAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4']]

### SnapshotOptions
- **Type**: <class 'NoneType'>

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VPCDerivedInfo]

### CognitoOptions
- **Type**: <class 'NoneType'>

### EncryptionAtRestOptions
- **Type**: <class 'NoneType'>

### NodeToNodeEncryptionOptions
- **Type**: <class 'NoneType'>

### AdvancedOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.opensearch.opensearch_classes.LogPublishingOption]]

### ServiceSoftwareOptions
- **Type**: <class 'NoneType'>

### DomainEndpointOptions
- **Type**: <class 'NoneType'>

### AdvancedSecurityOptions
- **Type**: <class 'NoneType'>

### IdentityCenterOptions
- **Type**: <class 'NoneType'>

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneOptionsOutput]

### ChangeProgressDetails
- **Type**: <class 'NoneType'>

### OffPeakWindowOptions
- **Type**: <class 'NoneType'>

### SoftwareUpdateOptions
- **Type**: <class 'NoneType'>

### DomainProcessingStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Creating', 'Deleting', 'Isolated', 'Modifying', 'UpdatingServiceSoftware', 'UpgradingEngineVersion']]

### ModifyingProperties
- **Type**: typing.Optional[typing.List[NoneType]]

### AIMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AIMLOptionsOutput]


# DryRunProgressStatus

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ValidationFailure]]


# DryRunResults

### DeploymentType
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# Duration

### Value
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['HOURS']]


# EBSOptions

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


# EBSOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.EBSOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionAtRestOptions

### Enabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]


# EncryptionAtRestOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.EncryptionAtRestOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# EnvironmentInfo

### AvailabilityZoneInformation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AvailabilityZoneInfo]]


# ErrorDetails

### ErrorType
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# Filter

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# GetApplicationRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### iamIdentityCenterOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IamIdentityCenterOptions'>
- **Required**: Yes

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSource]
- **Required**: Yes

### appConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AppConfig]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# GetCompatibleVersionsRequest

### DomainName
- **Type**: typing.Optional[str]


# GetCompatibleVersionsResponse

### CompatibleVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.CompatibleVersionsMap]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSourceRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceResponse

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSourceType'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# GetDirectQueryDataSourceRequest

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDirectQueryDataSourceResponse

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DirectQueryDataSourceType'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainMaintenanceStatusRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaintenanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainMaintenanceStatusResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# GetPackageVersionHistoryRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetPackageVersionHistoryResponse

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersionHistoryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageVersionHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeHistoryRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeHistoryResponse

### UpgradeHistories
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.UpgradeHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeStatusRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetUpgradeStatusResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# IPAddressTypeStatus

### Options
- **Type**: typing.Literal['dualstack', 'ipv4']
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# IamIdentityCenterOptions

### enabled
- **Type**: typing.Optional[bool]

### iamIdentityCenterInstanceArn
- **Type**: typing.Optional[str]

### iamRoleForIdentityCenterApplicationArn
- **Type**: typing.Optional[str]

### iamIdentityCenterApplicationArn
- **Type**: typing.Optional[str]


# IamIdentityCenterOptionsInput

### enabled
- **Type**: typing.Optional[bool]

### iamIdentityCenterInstanceArn
- **Type**: typing.Optional[str]

### iamRoleForIdentityCenterApplicationArn
- **Type**: typing.Optional[str]


# IdentityCenterOptions

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


# IdentityCenterOptionsInput

### EnabledAPIAccess
- **Type**: typing.Optional[bool]

### IdentityCenterInstanceARN
- **Type**: typing.Optional[str]

### SubjectKey
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### RolesKey
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# IdentityCenterOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IdentityCenterOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# InboundConnection

### LocalDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInformationContainer]

### RemoteDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInformationContainer]

### ConnectionId
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.InboundConnectionStatus]

### ConnectionMode
- **Type**: typing.Optional[typing.Literal['DIRECT', 'VPC_ENDPOINT']]


# InboundConnectionStatus

### StatusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'APPROVED', 'DELETED', 'DELETING', 'PENDING_ACCEPTANCE', 'PROVISIONING', 'REJECTED', 'REJECTING']]

### Message
- **Type**: typing.Optional[str]


# InstanceCountLimits

### MinimumInstanceCount
- **Type**: typing.Optional[int]

### MaximumInstanceCount
- **Type**: typing.Optional[int]


# InstanceLimits

### InstanceCountLimits
- **Type**: <class 'NoneType'>


# InstanceTypeDetails

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


# JWTOptionsInput

### Enabled
- **Type**: typing.Optional[bool]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### PublicKey
- **Type**: typing.Optional[str]


# JWTOptionsOutput

### Enabled
- **Type**: typing.Optional[bool]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### PublicKey
- **Type**: typing.Optional[str]


# KeyStoreAccessOption

### KeyStoreAccessEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### KeyAccessRoleArn
- **Type**: typing.Optional[str]


# Limits

### StorageTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.StorageType]]

### InstanceLimits
- **Type**: <class 'NoneType'>

### AdditionalLimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AdditionalLimit]]


# ListApplicationsRequest

### nextToken
- **Type**: typing.Optional[str]

### statuses
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]]

### maxResults
- **Type**: typing.Optional[int]


# ListApplicationsRequestPaginate

### statuses
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PaginatorConfig]


# ListApplicationsResponse

### ApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# ListDataSourcesResponse

### DataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSourceDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# ListDirectQueryDataSourcesRequest

### NextToken
- **Type**: typing.Optional[str]


# ListDirectQueryDataSourcesResponse

### DirectQueryDataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DirectQueryDataSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainMaintenancesRequest

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


# ListDomainMaintenancesResponse

### DomainMaintenances
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainMaintenanceDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainNamesRequest

### EngineType
- **Type**: typing.Optional[typing.Literal['Elasticsearch', 'OpenSearch']]


# ListDomainNamesResponse

### DomainNames
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# ListDomainsForPackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsForPackageResponse

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainPackageDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstanceTypeDetailsRequest

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


# ListInstanceTypeDetailsResponse

### InstanceTypeDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.InstanceTypeDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesForDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesForDomainResponse

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainPackageDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsResponse

### ScheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ScheduledAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequest

### ARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# ListVersionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVersionsResponse

### Versions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointAccessRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointAccessResponse

### AuthorizedPrincipalList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AuthorizedPrincipal]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcEndpointsForDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointsForDomainResponse

### VpcEndpointSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VpcEndpointSummary]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcEndpointsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointsResponse

### VpcEndpointSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VpcEndpointSummary]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# LogPublishingOption

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# LogPublishingOptionsStatus

### Options
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.opensearch.opensearch_classes.LogPublishingOption]]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus]


# MasterUserOptions

### MasterUserARN
- **Type**: typing.Optional[str]

### MasterUserName
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]


# ModifyingProperties

### Name
- **Type**: typing.Optional[str]

### ActiveValue
- **Type**: typing.Optional[str]

### PendingValue
- **Type**: typing.Optional[str]

### ValueType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT', 'STRINGIFIED_JSON']]


# NaturalLanguageQueryGenerationOptionsInput

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# NaturalLanguageQueryGenerationOptionsOutput

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CurrentState
- **Type**: typing.Optional[typing.Literal['DISABLE_COMPLETE', 'DISABLE_FAILED', 'DISABLE_IN_PROGRESS', 'ENABLE_COMPLETE', 'ENABLE_FAILED', 'ENABLE_IN_PROGRESS', 'NOT_ENABLED']]


# NodeConfig

### Enabled
- **Type**: typing.Optional[bool]

### Type
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.search', 'c4.4xlarge.search', 'c4.8xlarge.search', 'c4.large.search', 'c4.xlarge.search', 'c5.18xlarge.search', 'c5.2xlarge.search', 'c5.4xlarge.search', 'c5.9xlarge.search', 'c5.large.search', 'c5.xlarge.search', 'c6g.12xlarge.search', 'c6g.2xlarge.search', 'c6g.4xlarge.search', 'c6g.8xlarge.search', 'c6g.large.search', 'c6g.xlarge.search', 'd2.2xlarge.search', 'd2.4xlarge.search', 'd2.8xlarge.search', 'd2.xlarge.search', 'i2.2xlarge.search', 'i2.xlarge.search', 'i3.16xlarge.search', 'i3.2xlarge.search', 'i3.4xlarge.search', 'i3.8xlarge.search', 'i3.large.search', 'i3.xlarge.search', 'm3.2xlarge.search', 'm3.large.search', 'm3.medium.search', 'm3.xlarge.search', 'm4.10xlarge.search', 'm4.2xlarge.search', 'm4.4xlarge.search', 'm4.large.search', 'm4.xlarge.search', 'm5.12xlarge.search', 'm5.24xlarge.search', 'm5.2xlarge.search', 'm5.4xlarge.search', 'm5.large.search', 'm5.xlarge.search', 'm6g.12xlarge.search', 'm6g.2xlarge.search', 'm6g.4xlarge.search', 'm6g.8xlarge.search', 'm6g.large.search', 'm6g.xlarge.search', 'or1.12xlarge.search', 'or1.16xlarge.search', 'or1.2xlarge.search', 'or1.4xlarge.search', 'or1.8xlarge.search', 'or1.large.search', 'or1.medium.search', 'or1.xlarge.search', 'r3.2xlarge.search', 'r3.4xlarge.search', 'r3.8xlarge.search', 'r3.large.search', 'r3.xlarge.search', 'r4.16xlarge.search', 'r4.2xlarge.search', 'r4.4xlarge.search', 'r4.8xlarge.search', 'r4.large.search', 'r4.xlarge.search', 'r5.12xlarge.search', 'r5.24xlarge.search', 'r5.2xlarge.search', 'r5.4xlarge.search', 'r5.large.search', 'r5.xlarge.search', 'r6g.12xlarge.search', 'r6g.2xlarge.search', 'r6g.4xlarge.search', 'r6g.8xlarge.search', 'r6g.large.search', 'r6g.xlarge.search', 'r6gd.12xlarge.search', 'r6gd.16xlarge.search', 'r6gd.2xlarge.search', 'r6gd.4xlarge.search', 'r6gd.8xlarge.search', 'r6gd.large.search', 'r6gd.xlarge.search', 't2.medium.search', 't2.micro.search', 't2.small.search', 't3.2xlarge.search', 't3.large.search', 't3.medium.search', 't3.micro.search', 't3.nano.search', 't3.small.search', 't3.xlarge.search', 't4g.medium.search', 't4g.small.search', 'ultrawarm1.large.search', 'ultrawarm1.medium.search', 'ultrawarm1.xlarge.search']]

### Count
- **Type**: typing.Optional[int]


# NodeOption

### NodeType
- **Type**: typing.Optional[typing.Literal['coordinator']]

### NodeConfig
- **Type**: <class 'NoneType'>


# NodeToNodeEncryptionOptions

### Enabled
- **Type**: typing.Optional[bool]


# NodeToNodeEncryptionOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.NodeToNodeEncryptionOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# OffPeakWindow

### WindowStartTime
- **Type**: <class 'NoneType'>


# OffPeakWindowOptions

### Enabled
- **Type**: typing.Optional[bool]

### OffPeakWindow
- **Type**: <class 'NoneType'>


# OffPeakWindowOptionsStatus

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OffPeakWindowOptions]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus]


# OptionStatus

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


# OutboundConnection

### LocalDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInformationContainer]

### RemoteDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainInformationContainer]

### ConnectionId
- **Type**: typing.Optional[str]

### ConnectionAlias
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OutboundConnectionStatus]

### ConnectionMode
- **Type**: typing.Optional[typing.Literal['DIRECT', 'VPC_ENDPOINT']]

### ConnectionProperties
- **Type**: <class 'NoneType'>


# OutboundConnectionStatus

### StatusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'APPROVED', 'DELETED', 'DELETING', 'PENDING_ACCEPTANCE', 'PROVISIONING', 'REJECTED', 'REJECTING', 'VALIDATING', 'VALIDATION_FAILED']]

### Message
- **Type**: typing.Optional[str]


# PackageAssociationConfiguration

### KeyStoreAccessOption
- **Type**: <class 'NoneType'>


# PackageConfiguration

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


# PackageDetails

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
- **Type**: <class 'NoneType'>

### EngineVersion
- **Type**: typing.Optional[str]

### AvailablePluginProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PluginProperties]

### AvailablePackageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageConfiguration]

### AllowListedUserList
- **Type**: typing.Optional[typing.List[str]]

### PackageOwner
- **Type**: typing.Optional[str]

### PackageVendingOptions
- **Type**: <class 'NoneType'>

### PackageEncryptionOptions
- **Type**: <class 'NoneType'>


# PackageDetailsForAssociation

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### PrerequisitePackageIDList
- **Type**: typing.Optional[typing.List[str]]

### AssociationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageAssociationConfiguration]


# PackageEncryptionOptions

### EncryptionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### KmsKeyIdentifier
- **Type**: typing.Optional[str]


# PackageSource

### S3BucketName
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]


# PackageVendingOptions

### VendingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# PackageVersionHistory

### PackageVersion
- **Type**: typing.Optional[str]

### CommitMessage
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### PluginProperties
- **Type**: <class 'NoneType'>

### PackageConfiguration
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PluginProperties

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


# PurchaseReservedInstanceOfferingRequest

### ReservedInstanceOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: typing.Optional[int]


# PurchaseReservedInstanceOfferingResponse

### ReservedInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# RecurringCharge

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RejectInboundConnectionRequest

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# RejectInboundConnectionResponse

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.InboundConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsRequest

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# ReservedInstance

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.RecurringCharge]]


# ReservedInstanceOffering

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.RecurringCharge]]


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


# RevokeVpcEndpointAccessRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[typing.Literal['application.opensearchservice.amazonaws.com']]


# S3GlueDataCatalog

### RoleArn
- **Type**: typing.Optional[str]


# SAMLIdp

### MetadataContent
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# SAMLOptionsInput

### Enabled
- **Type**: typing.Optional[bool]

### Idp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SAMLIdp]

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


# SAMLOptionsOutput

### Enabled
- **Type**: typing.Optional[bool]

### Idp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SAMLIdp]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### SessionTimeoutMinutes
- **Type**: typing.Optional[int]


# ScheduledAction

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['JVM_HEAP_SIZE_TUNING', 'JVM_YOUNG_GEN_TUNING', 'SERVICE_SOFTWARE_UPDATE']
- **Required**: Yes

### Severity
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes

### ScheduledTime
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ScheduledBy
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'ELIGIBLE', 'FAILED', 'IN_PROGRESS', 'NOT_ELIGIBLE', 'PENDING_UPDATE']]

### Mandatory
- **Type**: typing.Optional[bool]

### Cancellable
- **Type**: typing.Optional[bool]


# ScheduledAutoTuneDetails

### Date
- **Type**: typing.Optional[datetime.datetime]

### ActionType
- **Type**: typing.Optional[typing.Literal['JVM_HEAP_SIZE_TUNING', 'JVM_YOUNG_GEN_TUNING']]

### Action
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# SecurityLakeDirectQueryDataSource

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceSoftwareOptions

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


# SnapshotOptions

### AutomatedSnapshotStartHour
- **Type**: typing.Optional[int]


# SnapshotOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SnapshotOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# SoftwareUpdateOptions

### AutoSoftwareUpdateEnabled
- **Type**: typing.Optional[bool]


# SoftwareUpdateOptionsStatus

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.SoftwareUpdateOptions]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus]


# StartDomainMaintenanceRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['REBOOT_NODE', 'RESTART_DASHBOARD', 'RESTART_SEARCH_PROCESS']
- **Required**: Yes

### NodeId
- **Type**: typing.Optional[str]


# StartDomainMaintenanceResponse

### MaintenanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# StartServiceSoftwareUpdateRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleAt
- **Type**: typing.Optional[typing.Literal['NOW', 'OFF_PEAK_WINDOW', 'TIMESTAMP']]

### DesiredStartTime
- **Type**: typing.Optional[int]


# StartServiceSoftwareUpdateResponse

### ServiceSoftwareOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ServiceSoftwareOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# StorageType

### StorageTypeName
- **Type**: typing.Optional[str]

### StorageSubTypeName
- **Type**: typing.Optional[str]

### StorageTypeLimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.StorageTypeLimit]]


# StorageTypeLimit

### LimitName
- **Type**: typing.Optional[str]

### LimitValues
- **Type**: typing.Optional[typing.List[str]]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApplicationRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### dataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSource]]

### appConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AppConfig]]


# UpdateApplicationResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSource]
- **Required**: Yes

### iamIdentityCenterOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IamIdentityCenterOptions'>
- **Required**: Yes

### appConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AppConfig]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSourceRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DataSourceType'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DISABLED']]


# UpdateDataSourceResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDirectQueryDataSourceRequest

### DataSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DirectQueryDataSourceType'>
- **Required**: Yes

### OpenSearchArns
- **Type**: typing.List[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateDirectQueryDataSourceResponse

### DataSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainConfigRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ClusterConfig, aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ClusterConfigOutput, NoneType]

### EBSOptions
- **Type**: <class 'NoneType'>

### SnapshotOptions
- **Type**: <class 'NoneType'>

### VPCOptions
- **Type**: <class 'NoneType'>

### CognitoOptions
- **Type**: <class 'NoneType'>

### AdvancedOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### AccessPolicies
- **Type**: typing.Optional[str]

### IPAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4']]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.opensearch.opensearch_classes.LogPublishingOption]]

### EncryptionAtRestOptions
- **Type**: <class 'NoneType'>

### DomainEndpointOptions
- **Type**: <class 'NoneType'>

### NodeToNodeEncryptionOptions
- **Type**: <class 'NoneType'>

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AdvancedSecurityOptionsInput]

### IdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.IdentityCenterOptionsInput]

### AutoTuneOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneOptions, aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AutoTuneOptionsExtra, NoneType]

### DryRun
- **Type**: typing.Optional[bool]

### DryRunMode
- **Type**: typing.Optional[typing.Literal['Basic', 'Verbose']]

### OffPeakWindowOptions
- **Type**: <class 'NoneType'>

### SoftwareUpdateOptions
- **Type**: <class 'NoneType'>

### AIMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.AIMLOptionsInput]


# UpdateDomainConfigResponse

### DomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DomainConfig'>
- **Required**: Yes

### DryRunResults
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DryRunResults'>
- **Required**: Yes

### DryRunProgressStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.DryRunProgressStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### PackageSource
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageSource'>
- **Required**: Yes

### PackageDescription
- **Type**: typing.Optional[str]

### CommitMessage
- **Type**: typing.Optional[str]

### PackageConfiguration
- **Type**: <class 'NoneType'>

### PackageEncryptionOptions
- **Type**: <class 'NoneType'>


# UpdatePackageResponse

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.PackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePackageScopeRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['ADD', 'OVERRIDE', 'REMOVE']
- **Required**: Yes

### PackageUserList
- **Type**: typing.List[str]
- **Required**: Yes


# UpdatePackageScopeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScheduledActionRequest

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


# UpdateScheduledActionResponse

### ScheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ScheduledAction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVpcEndpointRequest

### VpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VPCOptions'>
- **Required**: Yes


# UpdateVpcEndpointResponse

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VpcEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpgradeDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PerformCheckOnly
- **Type**: typing.Optional[bool]

### AdvancedOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpgradeDomainResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ChangeProgressDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpgradeHistory

### UpgradeName
- **Type**: typing.Optional[str]

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpgradeStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED', 'SUCCEEDED_WITH_ISSUES']]

### StepsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.UpgradeStepItem]]


# UpgradeStepItem

### UpgradeStep
- **Type**: typing.Optional[typing.Literal['PRE_UPGRADE_CHECK', 'SNAPSHOT', 'UPGRADE']]

### UpgradeStepStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED', 'SUCCEEDED_WITH_ISSUES']]

### Issues
- **Type**: typing.Optional[typing.List[str]]

### ProgressPercent
- **Type**: typing.Optional[float]


# VPCDerivedInfo

### VPCId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VPCDerivedInfoStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VPCDerivedInfo'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# VPCOptions

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# ValidationFailure

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# VersionStatus

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearch.opensearch_classes.OptionStatus'>
- **Required**: Yes


# VpcEndpoint

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcEndpointOwner
- **Type**: typing.Optional[str]

### DomainArn
- **Type**: typing.Optional[str]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearch.opensearch_classes.VPCDerivedInfo]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### Endpoint
- **Type**: typing.Optional[str]


# VpcEndpointError

### VpcEndpointId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['ENDPOINT_NOT_FOUND', 'SERVER_ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]


# VpcEndpointSummary

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcEndpointOwner
- **Type**: typing.Optional[str]

### DomainArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]


# WindowStartTime

### Hours
- **Type**: <class 'int'>
- **Required**: Yes

### Minutes
- **Type**: <class 'int'>
- **Required**: Yes


# ZoneAwarenessConfig

### AvailabilityZoneCount
- **Type**: typing.Optional[int]


