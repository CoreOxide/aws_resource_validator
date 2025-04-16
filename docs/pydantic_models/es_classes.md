# Es Classes

# AcceptInboundCrossClusterSearchConnectionRequest

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptInboundCrossClusterSearchConnectionResponse

### CrossClusterSearchConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# AccessPoliciesStatus

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# AddTagsRequest

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.es_classes.Tag]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# AdvancedSecurityOptions

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### SAMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SAMLOptionsOutput]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SAMLOptionsInput]

### AnonymousAuthEnabled
- **Type**: typing.Optional[bool]


# AdvancedSecurityOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# AssociatePackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatePackageResponse

### DomainPackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainPackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# AuthorizeVpcEndpointAccessRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: <class 'str'>
- **Required**: Yes


# AuthorizeVpcEndpointAccessResponse

### AuthorizedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.AuthorizedPrincipal'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.Timestamp]

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


# AutoTuneMaintenanceScheduleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoTuneOptions

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RollbackOnDisable
- **Type**: typing.Optional[typing.Literal['DEFAULT_ROLLBACK', 'NO_ROLLBACK']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.AutoTuneMaintenanceSchedule]]


# AutoTuneOptionsExtra

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RollbackOnDisable
- **Type**: typing.Optional[typing.Literal['DEFAULT_ROLLBACK', 'NO_ROLLBACK']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.AutoTuneMaintenanceScheduleOutput]]


# AutoTuneOptionsInput

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.AutoTuneMaintenanceScheduleUnion]]


# AutoTuneOptionsOutput

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLED_AND_ROLLBACK_COMPLETE', 'DISABLED_AND_ROLLBACK_ERROR', 'DISABLED_AND_ROLLBACK_IN_PROGRESS', 'DISABLED_AND_ROLLBACK_SCHEDULED', 'DISABLE_IN_PROGRESS', 'ENABLED', 'ENABLE_IN_PROGRESS', 'ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]


# AutoTuneOptionsStatus

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsExtra]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneStatus]


# AutoTuneOptionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### DryRun
- **Type**: <class 'bool'>
- **Required**: Yes

### CancelledChangeIds
- **Type**: typing.List[str]
- **Required**: Yes

### CancelledChangeProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.CancelledChangeProperty]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# CancelElasticsearchServiceSoftwareUpdateRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelElasticsearchServiceSoftwareUpdateResponse

### ServiceSoftwareOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ServiceSoftwareOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### InitiatedBy
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.ChangeProgressStage]]

### ConfigChangeStatus
- **Type**: typing.Optional[typing.Literal['ApplyingChanges', 'Cancelled', 'Completed', 'Initializing', 'Pending', 'PendingUserInput', 'Validating', 'ValidationFailed']]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### InitiatedBy
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.CognitoOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
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


# CreateElasticsearchDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ElasticsearchVersion
- **Type**: typing.Optional[str]

### ElasticsearchClusterConfig
- **Type**: <class 'NoneType'>

### EBSOptions
- **Type**: <class 'NoneType'>

### AccessPolicies
- **Type**: typing.Optional[str]

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.es_classes.LogPublishingOption]]

### DomainEndpointOptions
- **Type**: <class 'NoneType'>

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptionsInput]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsInput]

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.Tag]]


# CreateElasticsearchDomainResponse

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOutboundCrossClusterSearchConnectionRequest

### SourceDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainInformation'>
- **Required**: Yes

### DestinationDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainInformation'>
- **Required**: Yes

### ConnectionAlias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateOutboundCrossClusterSearchConnectionResponse

### SourceDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainInformation'>
- **Required**: Yes

### DestinationDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainInformation'>
- **Required**: Yes

### ConnectionAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OutboundCrossClusterSearchConnectionStatus'>
- **Required**: Yes

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackageRequest

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageType
- **Type**: typing.Literal['TXT-DICTIONARY']
- **Required**: Yes

### PackageSource
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageSource'>
- **Required**: Yes

### PackageDescription
- **Type**: typing.Optional[str]


# CreatePackageResponse

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcEndpointRequest

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VPCOptions'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateVpcEndpointResponse

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VpcEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteElasticsearchDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteElasticsearchDomainResponse

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInboundCrossClusterSearchConnectionRequest

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInboundCrossClusterSearchConnectionResponse

### CrossClusterSearchConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteOutboundCrossClusterSearchConnectionRequest

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutboundCrossClusterSearchConnectionResponse

### CrossClusterSearchConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OutboundCrossClusterSearchConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePackageResponse

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVpcEndpointRequest

### VpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcEndpointResponse

### VpcEndpointSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VpcEndpointSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.AutoTune]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ChangeProgressStatusDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeElasticsearchDomainConfigRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeElasticsearchDomainConfigResponse

### DomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeElasticsearchDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeElasticsearchDomainResponse

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeElasticsearchDomainsRequest

### DomainNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeElasticsearchDomainsResponse

### DomainStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeElasticsearchInstanceTypeLimitsRequest

### InstanceType
- **Type**: typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']
- **Required**: Yes

### ElasticsearchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]


# DescribeElasticsearchInstanceTypeLimitsResponse

### LimitsByRole
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.es_classes.Limits]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInboundCrossClusterSearchConnectionsRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInboundCrossClusterSearchConnectionsResponse

### CrossClusterSearchConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOutboundCrossClusterSearchConnectionsRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOutboundCrossClusterSearchConnectionsResponse

### CrossClusterSearchConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.OutboundCrossClusterSearchConnection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePackagesFilter

### Name
- **Type**: typing.Optional[typing.Literal['PackageID', 'PackageName', 'PackageStatus']]

### Value
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribePackagesRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.DescribePackagesFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePackagesResponse

### PackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.PackageDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedElasticsearchInstanceOfferingsRequest

### ReservedElasticsearchInstanceOfferingId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedElasticsearchInstanceOfferingsRequestPaginate

### ReservedElasticsearchInstanceOfferingId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfig]


# DescribeReservedElasticsearchInstanceOfferingsResponse

### ReservedElasticsearchInstanceOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.ReservedElasticsearchInstanceOffering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedElasticsearchInstancesRequest

### ReservedElasticsearchInstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedElasticsearchInstancesRequestPaginate

### ReservedElasticsearchInstanceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfig]


# DescribeReservedElasticsearchInstancesResponse

### ReservedElasticsearchInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.ReservedElasticsearchInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVpcEndpointsRequest

### VpcEndpointIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeVpcEndpointsResponse

### VpcEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.VpcEndpoint]
- **Required**: Yes

### VpcEndpointErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.VpcEndpointError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# DissociatePackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DissociatePackageResponse

### DomainPackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainPackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainEndpointOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# DomainInfo

### DomainName
- **Type**: typing.Optional[str]

### EngineType
- **Type**: typing.Optional[typing.Literal['Elasticsearch', 'OpenSearch']]


# DomainInformation

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# DomainPackageDetails

### PackageID
- **Type**: typing.Optional[str]

### PackageName
- **Type**: typing.Optional[str]

### PackageType
- **Type**: typing.Optional[typing.Literal['TXT-DICTIONARY']]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### DomainName
- **Type**: typing.Optional[str]

### DomainPackageStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ASSOCIATING', 'ASSOCIATION_FAILED', 'DISSOCIATING', 'DISSOCIATION_FAILED']]

### PackageVersion
- **Type**: typing.Optional[str]

### ReferencePath
- **Type**: typing.Optional[str]

### ErrorDetails
- **Type**: <class 'NoneType'>


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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.EBSOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# ElasticsearchClusterConfig

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']]

### InstanceCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessConfig
- **Type**: <class 'NoneType'>

### DedicatedMasterType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']]

### DedicatedMasterCount
- **Type**: typing.Optional[int]

### WarmEnabled
- **Type**: typing.Optional[bool]

### WarmType
- **Type**: typing.Optional[typing.Literal['ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']]

### WarmCount
- **Type**: typing.Optional[int]

### ColdStorageOptions
- **Type**: <class 'NoneType'>


# ElasticsearchClusterConfigStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchClusterConfig'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# ElasticsearchDomainConfig

### ElasticsearchVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ElasticsearchVersionStatus]

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ElasticsearchClusterConfigStatus]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EBSOptionsStatus]

### AccessPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AccessPoliciesStatus]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SnapshotOptionsStatus]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.VPCDerivedInfoStatus]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.CognitoOptionsStatus]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EncryptionAtRestOptionsStatus]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.NodeToNodeEncryptionOptionsStatus]

### AdvancedOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedOptionsStatus]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.LogPublishingOptionsStatus]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainEndpointOptionsStatus]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptionsStatus]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsStatus]

### ChangeProgressDetails
- **Type**: <class 'NoneType'>

### ModifyingProperties
- **Type**: typing.Optional[typing.List[NoneType]]


# ElasticsearchDomainStatus

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ElasticsearchClusterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchClusterConfig'>
- **Required**: Yes

### Created
- **Type**: typing.Optional[bool]

### Deleted
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Dict[str, str]]

### Processing
- **Type**: typing.Optional[bool]

### UpgradeProcessing
- **Type**: typing.Optional[bool]

### ElasticsearchVersion
- **Type**: typing.Optional[str]

### EBSOptions
- **Type**: <class 'NoneType'>

### AccessPolicies
- **Type**: typing.Optional[str]

### SnapshotOptions
- **Type**: <class 'NoneType'>

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.VPCDerivedInfo]

### CognitoOptions
- **Type**: <class 'NoneType'>

### EncryptionAtRestOptions
- **Type**: <class 'NoneType'>

### NodeToNodeEncryptionOptions
- **Type**: <class 'NoneType'>

### AdvancedOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.es_classes.LogPublishingOption]]

### ServiceSoftwareOptions
- **Type**: <class 'NoneType'>

### DomainEndpointOptions
- **Type**: <class 'NoneType'>

### AdvancedSecurityOptions
- **Type**: <class 'NoneType'>

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsOutput]

### ChangeProgressDetails
- **Type**: <class 'NoneType'>

### DomainProcessingStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Creating', 'Deleting', 'Isolated', 'Modifying', 'UpdatingServiceSoftware', 'UpgradingEngineVersion']]

### ModifyingProperties
- **Type**: typing.Optional[typing.List[NoneType]]


# ElasticsearchVersionStatus

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionAtRestOptions

### Enabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]


# EncryptionAtRestOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.EncryptionAtRestOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# ErrorDetails

### ErrorType
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# Filter

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetCompatibleElasticsearchVersionsRequest

### DomainName
- **Type**: typing.Optional[str]


# GetCompatibleElasticsearchVersionsResponse

### CompatibleElasticsearchVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.CompatibleVersionsMap]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.PackageVersionHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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


# GetUpgradeHistoryRequestPaginate

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfig]


# GetUpgradeHistoryResponse

### UpgradeHistories
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.UpgradeHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# InboundCrossClusterSearchConnection

### SourceDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainInformation]

### DestinationDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainInformation]

### CrossClusterSearchConnectionId
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnectionStatus]


# InboundCrossClusterSearchConnectionStatus

### StatusCode
- **Type**: typing.Optional[typing.Literal['APPROVED', 'DELETED', 'DELETING', 'PENDING_ACCEPTANCE', 'REJECTED', 'REJECTING']]

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


# Limits

### StorageTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.StorageType]]

### InstanceLimits
- **Type**: <class 'NoneType'>

### AdditionalLimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.AdditionalLimit]]


# ListDomainNamesRequest

### EngineType
- **Type**: typing.Optional[typing.Literal['Elasticsearch', 'OpenSearch']]


# ListDomainNamesResponse

### DomainNames
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.DomainInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.DomainPackageDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListElasticsearchInstanceTypesRequest

### ElasticsearchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListElasticsearchInstanceTypesRequestPaginate

### ElasticsearchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfig]


# ListElasticsearchInstanceTypesResponse

### ElasticsearchInstanceTypes
- **Type**: typing.List[typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListElasticsearchVersionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListElasticsearchVersionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfig]


# ListElasticsearchVersionsResponse

### ElasticsearchVersions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.DomainPackageDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequest

### ARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcEndpointAccessRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointAccessResponse

### AuthorizedPrincipalList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.AuthorizedPrincipal]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcEndpointsForDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointsForDomainResponse

### VpcEndpointSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.VpcEndpointSummary]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcEndpointsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointsResponse

### VpcEndpointSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.VpcEndpointSummary]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# LogPublishingOption

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# LogPublishingOptionsStatus

### Options
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.es_classes.LogPublishingOption]]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.OptionStatus]


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


# NodeToNodeEncryptionOptions

### Enabled
- **Type**: typing.Optional[bool]


# NodeToNodeEncryptionOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.NodeToNodeEncryptionOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


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


# OutboundCrossClusterSearchConnection

### SourceDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainInformation]

### DestinationDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainInformation]

### CrossClusterSearchConnectionId
- **Type**: typing.Optional[str]

### ConnectionAlias
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.OutboundCrossClusterSearchConnectionStatus]


# OutboundCrossClusterSearchConnectionStatus

### StatusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'PENDING_ACCEPTANCE', 'PROVISIONING', 'REJECTED', 'VALIDATING', 'VALIDATION_FAILED']]

### Message
- **Type**: typing.Optional[str]


# PackageDetails

### PackageID
- **Type**: typing.Optional[str]

### PackageName
- **Type**: typing.Optional[str]

### PackageType
- **Type**: typing.Optional[typing.Literal['TXT-DICTIONARY']]

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


# PackageSource

### S3BucketName
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]


# PackageVersionHistory

### PackageVersion
- **Type**: typing.Optional[str]

### CommitMessage
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PurchaseReservedElasticsearchInstanceOfferingRequest

### ReservedElasticsearchInstanceOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: typing.Optional[int]


# PurchaseReservedElasticsearchInstanceOfferingResponse

### ReservedElasticsearchInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# RecurringCharge

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RejectInboundCrossClusterSearchConnectionRequest

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# RejectInboundCrossClusterSearchConnectionResponse

### CrossClusterSearchConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsRequest

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReservedElasticsearchInstance

### ReservationName
- **Type**: typing.Optional[str]

### ReservedElasticsearchInstanceId
- **Type**: typing.Optional[str]

### ReservedElasticsearchInstanceOfferingId
- **Type**: typing.Optional[str]

### ElasticsearchInstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']]

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

### ElasticsearchInstanceCount
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[str]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.RecurringCharge]]


# ReservedElasticsearchInstanceOffering

### ReservedElasticsearchInstanceOfferingId
- **Type**: typing.Optional[str]

### ElasticsearchInstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.RecurringCharge]]


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
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SAMLIdp]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SAMLIdp]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### SessionTimeoutMinutes
- **Type**: typing.Optional[int]


# ScheduledAutoTuneDetails

### Date
- **Type**: typing.Optional[datetime.datetime]

### ActionType
- **Type**: typing.Optional[typing.Literal['JVM_HEAP_SIZE_TUNING', 'JVM_YOUNG_GEN_TUNING']]

### Action
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.SnapshotOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# StartElasticsearchServiceSoftwareUpdateRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# StartElasticsearchServiceSoftwareUpdateResponse

### ServiceSoftwareOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ServiceSoftwareOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# StorageType

### StorageTypeName
- **Type**: typing.Optional[str]

### StorageSubTypeName
- **Type**: typing.Optional[str]

### StorageTypeLimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.StorageTypeLimit]]


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


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateElasticsearchDomainConfigRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ElasticsearchClusterConfig
- **Type**: <class 'NoneType'>

### EBSOptions
- **Type**: <class 'NoneType'>

### SnapshotOptions
- **Type**: <class 'NoneType'>

### VPCOptions
- **Type**: <class 'NoneType'>

### CognitoOptions
- **Type**: <class 'NoneType'>

### AdvancedOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessPolicies
- **Type**: typing.Optional[str]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.es_classes.LogPublishingOption]]

### DomainEndpointOptions
- **Type**: <class 'NoneType'>

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptionsInput]

### NodeToNodeEncryptionOptions
- **Type**: <class 'NoneType'>

### EncryptionAtRestOptions
- **Type**: <class 'NoneType'>

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsUnion]

### DryRun
- **Type**: typing.Optional[bool]


# UpdateElasticsearchDomainConfigResponse

### DomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainConfig'>
- **Required**: Yes

### DryRunResults
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DryRunResults'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePackageRequest

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### PackageSource
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageSource'>
- **Required**: Yes

### PackageDescription
- **Type**: typing.Optional[str]

### CommitMessage
- **Type**: typing.Optional[str]


# UpdatePackageResponse

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVpcEndpointRequest

### VpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VPCOptions'>
- **Required**: Yes


# UpdateVpcEndpointResponse

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VpcEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# UpgradeElasticsearchDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PerformCheckOnly
- **Type**: typing.Optional[bool]


# UpgradeElasticsearchDomainResponse

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PerformCheckOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### ChangeProgressDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ChangeProgressDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadata'>
- **Required**: Yes


# UpgradeHistory

### UpgradeName
- **Type**: typing.Optional[str]

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpgradeStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED', 'SUCCEEDED_WITH_ISSUES']]

### StepsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.UpgradeStepItem]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VPCDerivedInfo'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatus'>
- **Required**: Yes


# VPCOptions

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# VpcEndpoint

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcEndpointOwner
- **Type**: typing.Optional[str]

### DomainArn
- **Type**: typing.Optional[str]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.VPCDerivedInfo]

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


# ZoneAwarenessConfig

### AvailabilityZoneCount
- **Type**: typing.Optional[int]


