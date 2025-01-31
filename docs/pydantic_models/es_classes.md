# Es Classes

# AcceptInboundCrossClusterSearchConnectionRequestRequestTypeDef

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptInboundCrossClusterSearchConnectionResponseTypeDef

### CrossClusterSearchConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccessPoliciesStatusTypeDef

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
- **Required**: Yes


# AddTagsRequestRequestTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.es_classes.TagTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
- **Required**: Yes


# AdvancedSecurityOptionsInputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### MasterUserOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.MasterUserOptionsTypeDef]

### SAMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SAMLOptionsInputTypeDef]

### AnonymousAuthEnabled
- **Type**: typing.Optional[bool]


# AdvancedSecurityOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
- **Required**: Yes


# AdvancedSecurityOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### SAMLOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SAMLOptionsOutputTypeDef]

### AnonymousAuthDisableDate
- **Type**: typing.Optional[datetime.datetime]

### AnonymousAuthEnabled
- **Type**: typing.Optional[bool]


# AssociatePackageRequestRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatePackageResponseTypeDef

### DomainPackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainPackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizeVpcEndpointAccessRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: <class 'str'>
- **Required**: Yes


# AuthorizeVpcEndpointAccessResponseTypeDef

### AuthorizedPrincipal
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.AuthorizedPrincipalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizedPrincipalTypeDef

### PrincipalType
- **Type**: typing.Optional[typing.Literal['AWS_ACCOUNT', 'AWS_SERVICE']]

### Principal
- **Type**: typing.Optional[str]


# AutoTuneDetailsTypeDef

### ScheduledAutoTuneDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ScheduledAutoTuneDetailsTypeDef]


# AutoTuneMaintenanceScheduleOutputTypeDef

### StartAt
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DurationTypeDef]

### CronExpressionForRecurrence
- **Type**: typing.Optional[str]


# AutoTuneMaintenanceScheduleTypeDef

### StartAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DurationTypeDef]

### CronExpressionForRecurrence
- **Type**: typing.Optional[str]


# AutoTuneOptionsExtraOutputTypeDef

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RollbackOnDisable
- **Type**: typing.Optional[typing.Literal['DEFAULT_ROLLBACK', 'NO_ROLLBACK']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.AutoTuneMaintenanceScheduleOutputTypeDef]]


# AutoTuneOptionsInputTypeDef

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.AutoTuneMaintenanceScheduleTypeDef]]


# AutoTuneOptionsOutputTypeDef

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLED_AND_ROLLBACK_COMPLETE', 'DISABLED_AND_ROLLBACK_ERROR', 'DISABLED_AND_ROLLBACK_IN_PROGRESS', 'DISABLED_AND_ROLLBACK_SCHEDULED', 'DISABLE_IN_PROGRESS', 'ENABLED', 'ENABLE_IN_PROGRESS', 'ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]


# AutoTuneOptionsStatusTypeDef

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsExtraOutputTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneStatusTypeDef]


# AutoTuneOptionsTypeDef

### DesiredState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RollbackOnDisable
- **Type**: typing.Optional[typing.Literal['DEFAULT_ROLLBACK', 'NO_ROLLBACK']]

### MaintenanceSchedules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.AutoTuneMaintenanceScheduleTypeDef]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneDetailsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelDomainConfigChangeRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# CancelDomainConfigChangeResponseTypeDef

### DryRun
- **Type**: <class 'bool'>
- **Required**: Yes

### CancelledChangeIds
- **Type**: typing.List[str]
- **Required**: Yes

### CancelledChangeProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.CancelledChangePropertyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelElasticsearchServiceSoftwareUpdateRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# CancelElasticsearchServiceSoftwareUpdateResponseTypeDef

### ServiceSoftwareOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ServiceSoftwareOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
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

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### InitiatedBy
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.ChangeProgressStageTypeDef]]

### ConfigChangeStatus
- **Type**: typing.Optional[typing.Literal['ApplyingChanges', 'Cancelled', 'Completed', 'Initializing', 'Pending', 'PendingUserInput', 'Validating', 'ValidationFailed']]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### InitiatedBy
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]


# CognitoOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.CognitoOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
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


# CreateElasticsearchDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ElasticsearchVersion
- **Type**: typing.Optional[str]

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ElasticsearchClusterConfigTypeDef]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EBSOptionsTypeDef]

### AccessPolicies
- **Type**: typing.Optional[str]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SnapshotOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.VPCOptionsTypeDef]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.CognitoOptionsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EncryptionAtRestOptionsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.NodeToNodeEncryptionOptionsTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.es_classes.LogPublishingOptionTypeDef]]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainEndpointOptionsTypeDef]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptionsInputTypeDef]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsInputTypeDef]

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.TagTypeDef]]


# CreateElasticsearchDomainResponseTypeDef

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOutboundCrossClusterSearchConnectionRequestRequestTypeDef

### SourceDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainInformationTypeDef'>
- **Required**: Yes

### DestinationDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainInformationTypeDef'>
- **Required**: Yes

### ConnectionAlias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateOutboundCrossClusterSearchConnectionResponseTypeDef

### SourceDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainInformationTypeDef'>
- **Required**: Yes

### DestinationDomainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainInformationTypeDef'>
- **Required**: Yes

### ConnectionAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OutboundCrossClusterSearchConnectionStatusTypeDef'>
- **Required**: Yes

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackageRequestRequestTypeDef

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageType
- **Type**: typing.Literal['TXT-DICTIONARY']
- **Required**: Yes

### PackageSource
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageSourceTypeDef'>
- **Required**: Yes

### PackageDescription
- **Type**: typing.Optional[str]


# CreatePackageResponseTypeDef

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcEndpointRequestRequestTypeDef

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VPCOptionsTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateVpcEndpointResponseTypeDef

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VpcEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteElasticsearchDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteElasticsearchDomainResponseTypeDef

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInboundCrossClusterSearchConnectionRequestRequestTypeDef

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInboundCrossClusterSearchConnectionResponseTypeDef

### CrossClusterSearchConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteOutboundCrossClusterSearchConnectionRequestRequestTypeDef

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutboundCrossClusterSearchConnectionResponseTypeDef

### CrossClusterSearchConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OutboundCrossClusterSearchConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePackageRequestRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePackageResponseTypeDef

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVpcEndpointRequestRequestTypeDef

### VpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcEndpointResponseTypeDef

### VpcEndpointSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VpcEndpointSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainAutoTunesRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainAutoTunesResponseTypeDef

### AutoTunes
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.AutoTuneTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainChangeProgressRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeId
- **Type**: typing.Optional[str]


# DescribeDomainChangeProgressResponseTypeDef

### ChangeProgressStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ChangeProgressStatusDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeElasticsearchDomainConfigRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeElasticsearchDomainConfigResponseTypeDef

### DomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeElasticsearchDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeElasticsearchDomainResponseTypeDef

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeElasticsearchDomainsRequestRequestTypeDef

### DomainNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeElasticsearchDomainsResponseTypeDef

### DomainStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeElasticsearchInstanceTypeLimitsRequestRequestTypeDef

### InstanceType
- **Type**: typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']
- **Required**: Yes

### ElasticsearchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]


# DescribeElasticsearchInstanceTypeLimitsResponseTypeDef

### LimitsByRole
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.es_classes.LimitsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInboundCrossClusterSearchConnectionsRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInboundCrossClusterSearchConnectionsResponseTypeDef

### CrossClusterSearchConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOutboundCrossClusterSearchConnectionsRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef

### CrossClusterSearchConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.OutboundCrossClusterSearchConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePackagesFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['PackageID', 'PackageName', 'PackageStatus']]

### Value
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribePackagesRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.es_classes.DescribePackagesFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePackagesResponseTypeDef

### PackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.PackageDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedElasticsearchInstanceOfferingsRequestDescribeReservedElasticsearchInstanceOfferingsPaginateTypeDef

### ReservedElasticsearchInstanceOfferingId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfigTypeDef]


# DescribeReservedElasticsearchInstanceOfferingsRequestRequestTypeDef

### ReservedElasticsearchInstanceOfferingId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef

### ReservedElasticsearchInstanceOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.ReservedElasticsearchInstanceOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedElasticsearchInstancesRequestDescribeReservedElasticsearchInstancesPaginateTypeDef

### ReservedElasticsearchInstanceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfigTypeDef]


# DescribeReservedElasticsearchInstancesRequestRequestTypeDef

### ReservedElasticsearchInstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeReservedElasticsearchInstancesResponseTypeDef

### ReservedElasticsearchInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.ReservedElasticsearchInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVpcEndpointsRequestRequestTypeDef

### VpcEndpointIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeVpcEndpointsResponseTypeDef

### VpcEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.VpcEndpointTypeDef]
- **Required**: Yes

### VpcEndpointErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.VpcEndpointErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DissociatePackageRequestRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DissociatePackageResponseTypeDef

### DomainPackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainPackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainEndpointOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DomainEndpointOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
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


# DomainInformationTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# DomainPackageDetailsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ErrorDetailsTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.EBSOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
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


# ElasticsearchClusterConfigStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchClusterConfigTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
- **Required**: Yes


# ElasticsearchClusterConfigTypeDef

### InstanceType
- **Type**: typing.Optional[typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']]

### InstanceCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ZoneAwarenessConfigTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ColdStorageOptionsTypeDef]


# ElasticsearchDomainConfigTypeDef

### ElasticsearchVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ElasticsearchVersionStatusTypeDef]

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ElasticsearchClusterConfigStatusTypeDef]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EBSOptionsStatusTypeDef]

### AccessPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AccessPoliciesStatusTypeDef]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SnapshotOptionsStatusTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.VPCDerivedInfoStatusTypeDef]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.CognitoOptionsStatusTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EncryptionAtRestOptionsStatusTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.NodeToNodeEncryptionOptionsStatusTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedOptionsStatusTypeDef]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.LogPublishingOptionsStatusTypeDef]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainEndpointOptionsStatusTypeDef]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptionsStatusTypeDef]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsStatusTypeDef]

### ChangeProgressDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ChangeProgressDetailsTypeDef]

### ModifyingProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.ModifyingPropertiesTypeDef]]


# ElasticsearchDomainStatusTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchClusterConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EBSOptionsTypeDef]

### AccessPolicies
- **Type**: typing.Optional[str]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SnapshotOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.VPCDerivedInfoTypeDef]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.CognitoOptionsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EncryptionAtRestOptionsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.NodeToNodeEncryptionOptionsTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.es_classes.LogPublishingOptionTypeDef]]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ServiceSoftwareOptionsTypeDef]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainEndpointOptionsTypeDef]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptionsTypeDef]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsOutputTypeDef]

### ChangeProgressDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ChangeProgressDetailsTypeDef]

### DomainProcessingStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Creating', 'Deleting', 'Isolated', 'Modifying', 'UpdatingServiceSoftware', 'UpgradingEngineVersion']]

### ModifyingProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.ModifyingPropertiesTypeDef]]


# ElasticsearchVersionStatusTypeDef

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionAtRestOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.EncryptionAtRestOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
- **Required**: Yes


# EncryptionAtRestOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]


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


# GetCompatibleElasticsearchVersionsRequestRequestTypeDef

### DomainName
- **Type**: typing.Optional[str]


# GetCompatibleElasticsearchVersionsResponseTypeDef

### CompatibleElasticsearchVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.CompatibleVersionsMapTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPackageVersionHistoryRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.PackageVersionHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeHistoryRequestGetUpgradeHistoryPaginateTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfigTypeDef]


# GetUpgradeHistoryRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeHistoryResponseTypeDef

### UpgradeHistories
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.UpgradeHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetUpgradeStatusRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InboundCrossClusterSearchConnectionStatusTypeDef

### StatusCode
- **Type**: typing.Optional[typing.Literal['APPROVED', 'DELETED', 'DELETING', 'PENDING_ACCEPTANCE', 'REJECTED', 'REJECTING']]

### Message
- **Type**: typing.Optional[str]


# InboundCrossClusterSearchConnectionTypeDef

### SourceDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainInformationTypeDef]

### DestinationDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainInformationTypeDef]

### CrossClusterSearchConnectionId
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnectionStatusTypeDef]


# InstanceCountLimitsTypeDef

### MinimumInstanceCount
- **Type**: typing.Optional[int]

### MaximumInstanceCount
- **Type**: typing.Optional[int]


# InstanceLimitsTypeDef

### InstanceCountLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.InstanceCountLimitsTypeDef]


# LimitsTypeDef

### StorageTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.StorageTypeTypeDef]]

### InstanceLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.InstanceLimitsTypeDef]

### AdditionalLimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.AdditionalLimitTypeDef]]


# ListDomainNamesRequestRequestTypeDef

### EngineType
- **Type**: typing.Optional[typing.Literal['Elasticsearch', 'OpenSearch']]


# ListDomainNamesResponseTypeDef

### DomainNames
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.DomainInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainsForPackageRequestRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsForPackageResponseTypeDef

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.DomainPackageDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListElasticsearchInstanceTypesRequestListElasticsearchInstanceTypesPaginateTypeDef

### ElasticsearchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfigTypeDef]


# ListElasticsearchInstanceTypesRequestRequestTypeDef

### ElasticsearchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListElasticsearchInstanceTypesResponseTypeDef

### ElasticsearchInstanceTypes
- **Type**: typing.List[typing.Literal['c4.2xlarge.elasticsearch', 'c4.4xlarge.elasticsearch', 'c4.8xlarge.elasticsearch', 'c4.large.elasticsearch', 'c4.xlarge.elasticsearch', 'c5.18xlarge.elasticsearch', 'c5.2xlarge.elasticsearch', 'c5.4xlarge.elasticsearch', 'c5.9xlarge.elasticsearch', 'c5.large.elasticsearch', 'c5.xlarge.elasticsearch', 'd2.2xlarge.elasticsearch', 'd2.4xlarge.elasticsearch', 'd2.8xlarge.elasticsearch', 'd2.xlarge.elasticsearch', 'i2.2xlarge.elasticsearch', 'i2.xlarge.elasticsearch', 'i3.16xlarge.elasticsearch', 'i3.2xlarge.elasticsearch', 'i3.4xlarge.elasticsearch', 'i3.8xlarge.elasticsearch', 'i3.large.elasticsearch', 'i3.xlarge.elasticsearch', 'm3.2xlarge.elasticsearch', 'm3.large.elasticsearch', 'm3.medium.elasticsearch', 'm3.xlarge.elasticsearch', 'm4.10xlarge.elasticsearch', 'm4.2xlarge.elasticsearch', 'm4.4xlarge.elasticsearch', 'm4.large.elasticsearch', 'm4.xlarge.elasticsearch', 'm5.12xlarge.elasticsearch', 'm5.2xlarge.elasticsearch', 'm5.4xlarge.elasticsearch', 'm5.large.elasticsearch', 'm5.xlarge.elasticsearch', 'r3.2xlarge.elasticsearch', 'r3.4xlarge.elasticsearch', 'r3.8xlarge.elasticsearch', 'r3.large.elasticsearch', 'r3.xlarge.elasticsearch', 'r4.16xlarge.elasticsearch', 'r4.2xlarge.elasticsearch', 'r4.4xlarge.elasticsearch', 'r4.8xlarge.elasticsearch', 'r4.large.elasticsearch', 'r4.xlarge.elasticsearch', 'r5.12xlarge.elasticsearch', 'r5.2xlarge.elasticsearch', 'r5.4xlarge.elasticsearch', 'r5.large.elasticsearch', 'r5.xlarge.elasticsearch', 't2.medium.elasticsearch', 't2.micro.elasticsearch', 't2.small.elasticsearch', 'ultrawarm1.large.elasticsearch', 'ultrawarm1.medium.elasticsearch']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListElasticsearchVersionsRequestListElasticsearchVersionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.PaginatorConfigTypeDef]


# ListElasticsearchVersionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListElasticsearchVersionsResponseTypeDef

### ElasticsearchVersions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesForDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesForDomainResponseTypeDef

### DomainPackageDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.DomainPackageDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequestRequestTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcEndpointAccessRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointAccessResponseTypeDef

### AuthorizedPrincipalList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.AuthorizedPrincipalTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcEndpointsForDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointsForDomainResponseTypeDef

### VpcEndpointSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.VpcEndpointSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcEndpointsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListVpcEndpointsResponseTypeDef

### VpcEndpointSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.es_classes.VpcEndpointSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogPublishingOptionTypeDef

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# LogPublishingOptionsStatusTypeDef

### Options
- **Type**: typing.Optional[typing.Dict[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.es_classes.LogPublishingOptionTypeDef]]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef]


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


# NodeToNodeEncryptionOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.NodeToNodeEncryptionOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
- **Required**: Yes


# NodeToNodeEncryptionOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


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


# OutboundCrossClusterSearchConnectionStatusTypeDef

### StatusCode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'PENDING_ACCEPTANCE', 'PROVISIONING', 'REJECTED', 'VALIDATING', 'VALIDATION_FAILED']]

### Message
- **Type**: typing.Optional[str]


# OutboundCrossClusterSearchConnectionTypeDef

### SourceDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainInformationTypeDef]

### DestinationDomainInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainInformationTypeDef]

### CrossClusterSearchConnectionId
- **Type**: typing.Optional[str]

### ConnectionAlias
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.OutboundCrossClusterSearchConnectionStatusTypeDef]


# PackageDetailsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ErrorDetailsTypeDef]


# PackageSourceTypeDef

### S3BucketName
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]


# PackageVersionHistoryTypeDef

### PackageVersion
- **Type**: typing.Optional[str]

### CommitMessage
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PurchaseReservedElasticsearchInstanceOfferingRequestRequestTypeDef

### ReservedElasticsearchInstanceOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: typing.Optional[int]


# PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef

### ReservedElasticsearchInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ReservationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecurringChargeTypeDef

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RejectInboundCrossClusterSearchConnectionRequestRequestTypeDef

### CrossClusterSearchConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# RejectInboundCrossClusterSearchConnectionResponseTypeDef

### CrossClusterSearchConnection
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.InboundCrossClusterSearchConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsRequestRequestTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReservedElasticsearchInstanceOfferingTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.RecurringChargeTypeDef]]


# ReservedElasticsearchInstanceTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.RecurringChargeTypeDef]]


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


# RevokeVpcEndpointAccessRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SAMLIdpTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SAMLIdpTypeDef]

### SubjectKey
- **Type**: typing.Optional[str]

### RolesKey
- **Type**: typing.Optional[str]

### SessionTimeoutMinutes
- **Type**: typing.Optional[int]


# ScheduledAutoTuneDetailsTypeDef

### Date
- **Type**: typing.Optional[datetime.datetime]

### ActionType
- **Type**: typing.Optional[typing.Literal['JVM_HEAP_SIZE_TUNING', 'JVM_YOUNG_GEN_TUNING']]

### Action
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.SnapshotOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
- **Required**: Yes


# SnapshotOptionsTypeDef

### AutomatedSnapshotStartHour
- **Type**: typing.Optional[int]


# StartElasticsearchServiceSoftwareUpdateRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# StartElasticsearchServiceSoftwareUpdateResponseTypeDef

### ServiceSoftwareOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ServiceSoftwareOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.StorageTypeLimitTypeDef]]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateElasticsearchDomainConfigRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.ElasticsearchClusterConfigTypeDef]

### EBSOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EBSOptionsTypeDef]

### SnapshotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.SnapshotOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.VPCOptionsTypeDef]

### CognitoOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.CognitoOptionsTypeDef]

### AdvancedOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessPolicies
- **Type**: typing.Optional[str]

### LogPublishingOptions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AUDIT_LOGS', 'ES_APPLICATION_LOGS', 'INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS'], aws_resource_validator.pydantic_models.es_classes.LogPublishingOptionTypeDef]]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.DomainEndpointOptionsTypeDef]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AdvancedSecurityOptionsInputTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.NodeToNodeEncryptionOptionsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.EncryptionAtRestOptionsTypeDef]

### AutoTuneOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.AutoTuneOptionsTypeDef]

### DryRun
- **Type**: typing.Optional[bool]


# UpdateElasticsearchDomainConfigResponseTypeDef

### DomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ElasticsearchDomainConfigTypeDef'>
- **Required**: Yes

### DryRunResults
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.DryRunResultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePackageRequestRequestTypeDef

### PackageID
- **Type**: <class 'str'>
- **Required**: Yes

### PackageSource
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageSourceTypeDef'>
- **Required**: Yes

### PackageDescription
- **Type**: typing.Optional[str]

### CommitMessage
- **Type**: typing.Optional[str]


# UpdatePackageResponseTypeDef

### PackageDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.PackageDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVpcEndpointRequestRequestTypeDef

### VpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VPCOptionsTypeDef'>
- **Required**: Yes


# UpdateVpcEndpointResponseTypeDef

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VpcEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpgradeElasticsearchDomainRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PerformCheckOnly
- **Type**: typing.Optional[bool]


# UpgradeElasticsearchDomainResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ChangeProgressDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpgradeHistoryTypeDef

### UpgradeName
- **Type**: typing.Optional[str]

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpgradeStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED', 'SUCCEEDED_WITH_ISSUES']]

### StepsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.es_classes.UpgradeStepItemTypeDef]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.VPCDerivedInfoTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.es_classes.OptionStatusTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.es_classes.VPCDerivedInfoTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### Endpoint
- **Type**: typing.Optional[str]


# ZoneAwarenessConfigTypeDef

### AvailabilityZoneCount
- **Type**: typing.Optional[int]


