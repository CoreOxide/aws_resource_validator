# Pydantic Models in pinpoint_email_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlacklistEntryTypeDef

### RblName
- **Type**: typing.Optional[str]

### ListingTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]


# BodyTypeDef

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.ContentTypeDef]

### Html
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.ContentTypeDef]


# CloudWatchDestinationTypeDef

### DimensionConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_email_classes.CloudWatchDimensionConfigurationTypeDef]
- **Required**: Yes


# CloudWatchDimensionConfigurationTypeDef

### DimensionName
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueSource
- **Type**: typing.Literal['EMAIL_HEADER', 'LINK_TAG', 'MESSAGE_TAG']
- **Required**: Yes

### DefaultDimensionValue
- **Type**: <class 'str'>
- **Required**: Yes


# ContentTypeDef

### Data
- **Type**: <class 'str'>
- **Required**: Yes

### Charset
- **Type**: typing.Optional[str]


# CreateConfigurationSetEventDestinationRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.EventDestinationDefinitionTypeDef'>
- **Required**: Yes


# CreateConfigurationSetRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.TrackingOptionsTypeDef]

### DeliveryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.DeliveryOptionsTypeDef]

### ReputationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.ReputationOptionsTypeDef]

### SendingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.SendingOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]]


# CreateDedicatedIpPoolRequestRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]]


# CreateDeliverabilityTestReportRequestRequestTypeDef

### FromEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.EmailContentTypeDef'>
- **Required**: Yes

### ReportName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]]


# CreateDeliverabilityTestReportResponseTypeDef

### ReportId
- **Type**: <class 'str'>
- **Required**: Yes

### DeliverabilityTestStatus
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEmailIdentityRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]]


# CreateEmailIdentityResponseTypeDef

### IdentityType
- **Type**: typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']
- **Required**: Yes

### VerifiedForSendingStatus
- **Type**: <class 'bool'>
- **Required**: Yes

### DkimAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.DkimAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DailyVolumeTypeDef

### StartDate
- **Type**: typing.Optional[datetime.datetime]

### VolumeStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.VolumeStatisticsTypeDef]

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.DomainIspPlacementTypeDef]]


# DedicatedIpTypeDef

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### WarmupStatus
- **Type**: typing.Literal['DONE', 'IN_PROGRESS']
- **Required**: Yes

### WarmupPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### PoolName
- **Type**: typing.Optional[str]


# DeleteConfigurationSetEventDestinationRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationSetRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDedicatedIpPoolRequestRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailIdentityRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverabilityTestReportTypeDef

### ReportId
- **Type**: typing.Optional[str]

### ReportName
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### FromEmailAddress
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### DeliverabilityTestStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS']]


# DeliveryOptionsTypeDef

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE']]

### SendingPoolName
- **Type**: typing.Optional[str]


# DestinationTypeDef

### ToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### CcAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### BccAddresses
- **Type**: typing.Optional[typing.Sequence[str]]


# DkimAttributesTypeDef

### SigningEnabled
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']]

### Tokens
- **Type**: typing.Optional[typing.List[str]]


# DomainDeliverabilityCampaignTypeDef

### CampaignId
- **Type**: typing.Optional[str]

### ImageUrl
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### FromAddress
- **Type**: typing.Optional[str]

### SendingIps
- **Type**: typing.Optional[typing.List[str]]

### FirstSeenDateTime
- **Type**: typing.Optional[datetime.datetime]

### LastSeenDateTime
- **Type**: typing.Optional[datetime.datetime]

### InboxCount
- **Type**: typing.Optional[int]

### SpamCount
- **Type**: typing.Optional[int]

### ReadRate
- **Type**: typing.Optional[float]

### DeleteRate
- **Type**: typing.Optional[float]

### ReadDeleteRate
- **Type**: typing.Optional[float]

### ProjectedVolume
- **Type**: typing.Optional[int]

### Esps
- **Type**: typing.Optional[typing.List[str]]


# DomainDeliverabilityTrackingOptionTypeDef

### Domain
- **Type**: typing.Optional[str]

### SubscriptionStartDate
- **Type**: typing.Optional[datetime.datetime]

### InboxPlacementTrackingOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.InboxPlacementTrackingOptionTypeDef]


# DomainIspPlacementTypeDef

### IspName
- **Type**: typing.Optional[str]

### InboxRawCount
- **Type**: typing.Optional[int]

### SpamRawCount
- **Type**: typing.Optional[int]

### InboxPercentage
- **Type**: typing.Optional[float]

### SpamPercentage
- **Type**: typing.Optional[float]


# EmailContentTypeDef

### Simple
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.MessageTypeDef]

### Raw
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.RawMessageTypeDef]

### Template
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.TemplateTypeDef]


# EventDestinationDefinitionTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### MatchingEventTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND']]]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.KinesisFirehoseDestinationTypeDef]

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.CloudWatchDestinationTypeDef]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.SnsDestinationTypeDef]

### PinpointDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.PinpointDestinationTypeDef]


# EventDestinationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.List[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND']]
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.KinesisFirehoseDestinationTypeDef]

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.CloudWatchDestinationTypeDef]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.SnsDestinationTypeDef]

### PinpointDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.PinpointDestinationTypeDef]


# GetAccountResponseTypeDef

### SendQuota
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.SendQuotaTypeDef'>
- **Required**: Yes

### SendingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### DedicatedIpAutoWarmupEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### EnforcementStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionAccessEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBlacklistReportsRequestRequestTypeDef

### BlacklistItemNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetBlacklistReportsResponseTypeDef

### BlacklistReport
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.BlacklistEntryTypeDef]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsResponseTypeDef

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.EventDestinationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigurationSetRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetResponseTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.TrackingOptionsTypeDef'>
- **Required**: Yes

### DeliveryOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.DeliveryOptionsTypeDef'>
- **Required**: Yes

### ReputationOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ReputationOptionsTypeDef'>
- **Required**: Yes

### SendingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.SendingOptionsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDedicatedIpRequestRequestTypeDef

### Ip
- **Type**: <class 'str'>
- **Required**: Yes


# GetDedicatedIpResponseTypeDef

### DedicatedIp
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.DedicatedIpTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDedicatedIpsRequestGetDedicatedIpsPaginateTypeDef

### PoolName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.PaginatorConfigTypeDef]


# GetDedicatedIpsRequestRequestTypeDef

### PoolName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# GetDedicatedIpsResponseTypeDef

### DedicatedIps
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.DedicatedIpTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeliverabilityDashboardOptionsResponseTypeDef

### DashboardEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SubscriptionExpiryDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccountStatus
- **Type**: typing.Literal['ACTIVE', 'DISABLED', 'PENDING_EXPIRATION']
- **Required**: Yes

### ActiveSubscribedDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.DomainDeliverabilityTrackingOptionTypeDef]
- **Required**: Yes

### PendingExpirationSubscribedDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.DomainDeliverabilityTrackingOptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeliverabilityTestReportRequestRequestTypeDef

### ReportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliverabilityTestReportResponseTypeDef

### DeliverabilityTestReport
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.DeliverabilityTestReportTypeDef'>
- **Required**: Yes

### OverallPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.PlacementStatisticsTypeDef'>
- **Required**: Yes

### IspPlacements
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.IspPlacementTypeDef]
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainDeliverabilityCampaignRequestRequestTypeDef

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainDeliverabilityCampaignResponseTypeDef

### DomainDeliverabilityCampaign
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.DomainDeliverabilityCampaignTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainStatisticsReportRequestRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# GetDomainStatisticsReportResponseTypeDef

### OverallVolume
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.OverallVolumeTypeDef'>
- **Required**: Yes

### DailyVolumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.DailyVolumeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEmailIdentityRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailIdentityResponseTypeDef

### IdentityType
- **Type**: typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']
- **Required**: Yes

### FeedbackForwardingStatus
- **Type**: <class 'bool'>
- **Required**: Yes

### VerifiedForSendingStatus
- **Type**: <class 'bool'>
- **Required**: Yes

### DkimAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.DkimAttributesTypeDef'>
- **Required**: Yes

### MailFromAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.MailFromAttributesTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityInfoTypeDef

### IdentityType
- **Type**: typing.Optional[typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']]

### IdentityName
- **Type**: typing.Optional[str]

### SendingEnabled
- **Type**: typing.Optional[bool]


# InboxPlacementTrackingOptionTypeDef

### Global
- **Type**: typing.Optional[bool]

### TrackedIsps
- **Type**: typing.Optional[typing.List[str]]


# IspPlacementTypeDef

### IspName
- **Type**: typing.Optional[str]

### PlacementStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.PlacementStatisticsTypeDef]


# KinesisFirehoseDestinationTypeDef

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.PaginatorConfigTypeDef]


# ListConfigurationSetsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListConfigurationSetsResponseTypeDef

### ConfigurationSets
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDedicatedIpPoolsRequestListDedicatedIpPoolsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.PaginatorConfigTypeDef]


# ListDedicatedIpPoolsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDedicatedIpPoolsResponseTypeDef

### DedicatedIpPools
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeliverabilityTestReportsRequestListDeliverabilityTestReportsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.PaginatorConfigTypeDef]


# ListDeliverabilityTestReportsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDeliverabilityTestReportsResponseTypeDef

### DeliverabilityTestReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.DeliverabilityTestReportTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainDeliverabilityCampaignsRequestRequestTypeDef

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### SubscribedDomain
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDomainDeliverabilityCampaignsResponseTypeDef

### DomainDeliverabilityCampaigns
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.DomainDeliverabilityCampaignTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEmailIdentitiesRequestListEmailIdentitiesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.PaginatorConfigTypeDef]


# ListEmailIdentitiesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListEmailIdentitiesResponseTypeDef

### EmailIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.IdentityInfoTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MailFromAttributesTypeDef

### MailFromDomain
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomainStatus
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']
- **Required**: Yes

### BehaviorOnMxFailure
- **Type**: typing.Literal['REJECT_MESSAGE', 'USE_DEFAULT_VALUE']
- **Required**: Yes


# MessageTagTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# MessageTypeDef

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ContentTypeDef'>
- **Required**: Yes

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.BodyTypeDef'>
- **Required**: Yes


# OverallVolumeTypeDef

### VolumeStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email_classes.VolumeStatisticsTypeDef]

### ReadRatePercent
- **Type**: typing.Optional[float]

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email_classes.DomainIspPlacementTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PinpointDestinationTypeDef

### ApplicationArn
- **Type**: typing.Optional[str]


# PlacementStatisticsTypeDef

### InboxPercentage
- **Type**: typing.Optional[float]

### SpamPercentage
- **Type**: typing.Optional[float]

### MissingPercentage
- **Type**: typing.Optional[float]

### SpfPercentage
- **Type**: typing.Optional[float]

### DkimPercentage
- **Type**: typing.Optional[float]


# PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef

### AutoWarmupEnabled
- **Type**: typing.Optional[bool]


# PutAccountSendingAttributesRequestRequestTypeDef

### SendingEnabled
- **Type**: typing.Optional[bool]


# PutConfigurationSetDeliveryOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE']]

### SendingPoolName
- **Type**: typing.Optional[str]


# PutConfigurationSetReputationOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]


# PutConfigurationSetSendingOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SendingEnabled
- **Type**: typing.Optional[bool]


# PutConfigurationSetTrackingOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomRedirectDomain
- **Type**: typing.Optional[str]


# PutDedicatedIpInPoolRequestRequestTypeDef

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPoolName
- **Type**: <class 'str'>
- **Required**: Yes


# PutDedicatedIpWarmupAttributesRequestRequestTypeDef

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### WarmupPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# PutDeliverabilityDashboardOptionRequestRequestTypeDef

### DashboardEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SubscribedDomains
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_email_classes.DomainDeliverabilityTrackingOptionTypeDef]]


# PutEmailIdentityDkimAttributesRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### SigningEnabled
- **Type**: typing.Optional[bool]


# PutEmailIdentityFeedbackAttributesRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### EmailForwardingEnabled
- **Type**: typing.Optional[bool]


# PutEmailIdentityMailFromAttributesRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomain
- **Type**: typing.Optional[str]

### BehaviorOnMxFailure
- **Type**: typing.Optional[typing.Literal['REJECT_MESSAGE', 'USE_DEFAULT_VALUE']]


# RawMessageTypeDef

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# ReputationOptionsTypeDef

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]

### LastFreshStart
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# SendEmailRequestRequestTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.DestinationTypeDef'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.EmailContentTypeDef'>
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[str]

### ReplyToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### FeedbackForwardingEmailAddress
- **Type**: typing.Optional[str]

### EmailTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_email_classes.MessageTagTypeDef]]

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendEmailResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendQuotaTypeDef

### Max24HourSend
- **Type**: typing.Optional[float]

### MaxSendRate
- **Type**: typing.Optional[float]

### SentLast24Hours
- **Type**: typing.Optional[float]


# SendingOptionsTypeDef

### SendingEnabled
- **Type**: typing.Optional[bool]


# SnsDestinationTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_email_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateTypeDef

### TemplateArn
- **Type**: typing.Optional[str]

### TemplateData
- **Type**: typing.Optional[str]


# TrackingOptionsTypeDef

### CustomRedirectDomain
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConfigurationSetEventDestinationRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email_classes.EventDestinationDefinitionTypeDef'>
- **Required**: Yes


# VolumeStatisticsTypeDef

### InboxRawCount
- **Type**: typing.Optional[int]

### SpamRawCount
- **Type**: typing.Optional[int]

### ProjectedInbox
- **Type**: typing.Optional[int]

### ProjectedSpam
- **Type**: typing.Optional[int]


