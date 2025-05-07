# Pinpoint Email Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlacklistEntry

### RblName
- **Type**: typing.Optional[str]

### ListingTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]


# Body

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Content]

### Html
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Content]


# CloudWatchDestination

### DimensionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.CloudWatchDimensionConfiguration]
- **Required**: Yes


# CloudWatchDestinationOutput

### DimensionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.CloudWatchDimensionConfiguration]
- **Required**: Yes


# CloudWatchDimensionConfiguration

### DimensionName
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueSource
- **Type**: typing.Literal['EMAIL_HEADER', 'LINK_TAG', 'MESSAGE_TAG']
- **Required**: Yes

### DefaultDimensionValue
- **Type**: <class 'str'>
- **Required**: Yes


# Content

### Data
- **Type**: <class 'str'>
- **Required**: Yes

### Charset
- **Type**: typing.Optional[str]


# CreateConfigurationSetEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.EventDestinationDefinition'>
- **Required**: Yes


# CreateConfigurationSetRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'NoneType'>

### DeliveryOptions
- **Type**: <class 'NoneType'>

### ReputationOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ReputationOptions, aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ReputationOptionsOutput, NoneType]

### SendingOptions
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]]


# CreateDedicatedIpPoolRequest

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]]


# CreateDeliverabilityTestReportRequest

### FromEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.EmailContent'>
- **Required**: Yes

### ReportName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]]


# CreateDeliverabilityTestReportResponse

### ReportId
- **Type**: <class 'str'>
- **Required**: Yes

### DeliverabilityTestStatus
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEmailIdentityRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]]


# CreateEmailIdentityResponse

### IdentityType
- **Type**: typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']
- **Required**: Yes

### VerifiedForSendingStatus
- **Type**: <class 'bool'>
- **Required**: Yes

### DkimAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DkimAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# DailyVolume

### StartDate
- **Type**: typing.Optional[datetime.datetime]

### VolumeStatistics
- **Type**: <class 'NoneType'>

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DomainIspPlacement]]


# DedicatedIp

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


# DeleteConfigurationSetEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationSetRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDedicatedIpPoolRequest

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailIdentityRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverabilityTestReport

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


# DeliveryOptions

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE']]

### SendingPoolName
- **Type**: typing.Optional[str]


# Destination

### ToAddresses
- **Type**: typing.Optional[typing.List[str]]

### CcAddresses
- **Type**: typing.Optional[typing.List[str]]

### BccAddresses
- **Type**: typing.Optional[typing.List[str]]


# DkimAttributes

### SigningEnabled
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']]

### Tokens
- **Type**: typing.Optional[typing.List[str]]


# DomainDeliverabilityCampaign

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


# DomainDeliverabilityTrackingOption

### Domain
- **Type**: typing.Optional[str]

### SubscriptionStartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### InboxPlacementTrackingOption
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.InboxPlacementTrackingOption, aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.InboxPlacementTrackingOptionOutput, NoneType]


# DomainDeliverabilityTrackingOptionOutput

### Domain
- **Type**: typing.Optional[str]

### SubscriptionStartDate
- **Type**: typing.Optional[datetime.datetime]

### InboxPlacementTrackingOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.InboxPlacementTrackingOptionOutput]


# DomainIspPlacement

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


# EmailContent

### Simple
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Message]

### Raw
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.RawMessage]

### Template
- **Type**: <class 'NoneType'>


# EventDestination

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.List[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND']]
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.CloudWatchDestinationOutput]

### SnsDestination
- **Type**: <class 'NoneType'>

### PinpointDestination
- **Type**: <class 'NoneType'>


# EventDestinationDefinition

### Enabled
- **Type**: typing.Optional[bool]

### MatchingEventTypes
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND']]]

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### CloudWatchDestination
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.CloudWatchDestination, aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.CloudWatchDestinationOutput, NoneType]

### SnsDestination
- **Type**: <class 'NoneType'>

### PinpointDestination
- **Type**: <class 'NoneType'>


# GetAccountResponse

### SendQuota
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.SendQuota'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetBlacklistReportsRequest

### BlacklistItemNames
- **Type**: typing.List[str]
- **Required**: Yes


# GetBlacklistReportsResponse

### BlacklistReport
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.BlacklistEntry]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsResponse

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.EventDestination]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigurationSetRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetResponse

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.TrackingOptions'>
- **Required**: Yes

### DeliveryOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DeliveryOptions'>
- **Required**: Yes

### ReputationOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ReputationOptionsOutput'>
- **Required**: Yes

### SendingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.SendingOptions'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetDedicatedIpRequest

### Ip
- **Type**: <class 'str'>
- **Required**: Yes


# GetDedicatedIpResponse

### DedicatedIp
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DedicatedIp'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetDedicatedIpsRequest

### PoolName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# GetDedicatedIpsRequestPaginate

### PoolName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.PaginatorConfig]


# GetDedicatedIpsResponse

### DedicatedIps
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DedicatedIp]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDeliverabilityDashboardOptionsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DomainDeliverabilityTrackingOptionOutput]
- **Required**: Yes

### PendingExpirationSubscribedDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DomainDeliverabilityTrackingOptionOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeliverabilityTestReportRequest

### ReportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliverabilityTestReportResponse

### DeliverabilityTestReport
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DeliverabilityTestReport'>
- **Required**: Yes

### OverallPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.PlacementStatistics'>
- **Required**: Yes

### IspPlacements
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.IspPlacement]
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainDeliverabilityCampaignRequest

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainDeliverabilityCampaignResponse

### DomainDeliverabilityCampaign
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DomainDeliverabilityCampaign'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainStatisticsReportRequest

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# GetDomainStatisticsReportResponse

### OverallVolume
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.OverallVolume'>
- **Required**: Yes

### DailyVolumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DailyVolume]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# GetEmailIdentityRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailIdentityResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DkimAttributes'>
- **Required**: Yes

### MailFromAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.MailFromAttributes'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# IdentityInfo

### IdentityType
- **Type**: typing.Optional[typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']]

### IdentityName
- **Type**: typing.Optional[str]

### SendingEnabled
- **Type**: typing.Optional[bool]


# InboxPlacementTrackingOption

### Global
- **Type**: typing.Optional[bool]

### TrackedIsps
- **Type**: typing.Optional[typing.List[str]]


# InboxPlacementTrackingOptionOutput

### Global
- **Type**: typing.Optional[bool]

### TrackedIsps
- **Type**: typing.Optional[typing.List[str]]


# IspPlacement

### IspName
- **Type**: typing.Optional[str]

### PlacementStatistics
- **Type**: <class 'NoneType'>


# KinesisFirehoseDestination

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListConfigurationSetsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListConfigurationSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.PaginatorConfig]


# ListConfigurationSetsResponse

### ConfigurationSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDedicatedIpPoolsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDedicatedIpPoolsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.PaginatorConfig]


# ListDedicatedIpPoolsResponse

### DedicatedIpPools
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeliverabilityTestReportsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDeliverabilityTestReportsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.PaginatorConfig]


# ListDeliverabilityTestReportsResponse

### DeliverabilityTestReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DeliverabilityTestReport]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainDeliverabilityCampaignsRequest

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


# ListDomainDeliverabilityCampaignsResponse

### DomainDeliverabilityCampaigns
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DomainDeliverabilityCampaign]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEmailIdentitiesRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListEmailIdentitiesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.PaginatorConfig]


# ListEmailIdentitiesResponse

### EmailIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.IdentityInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# MailFromAttributes

### MailFromDomain
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomainStatus
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']
- **Required**: Yes

### BehaviorOnMxFailure
- **Type**: typing.Literal['REJECT_MESSAGE', 'USE_DEFAULT_VALUE']
- **Required**: Yes


# Message

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Content'>
- **Required**: Yes

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Body'>
- **Required**: Yes


# MessageTag

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# OverallVolume

### VolumeStatistics
- **Type**: <class 'NoneType'>

### ReadRatePercent
- **Type**: typing.Optional[float]

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DomainIspPlacement]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PinpointDestination

### ApplicationArn
- **Type**: typing.Optional[str]


# PlacementStatistics

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


# PutAccountDedicatedIpWarmupAttributesRequest

### AutoWarmupEnabled
- **Type**: typing.Optional[bool]


# PutAccountSendingAttributesRequest

### SendingEnabled
- **Type**: typing.Optional[bool]


# PutConfigurationSetDeliveryOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE']]

### SendingPoolName
- **Type**: typing.Optional[str]


# PutConfigurationSetReputationOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]


# PutConfigurationSetSendingOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SendingEnabled
- **Type**: typing.Optional[bool]


# PutConfigurationSetTrackingOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomRedirectDomain
- **Type**: typing.Optional[str]


# PutDedicatedIpInPoolRequest

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPoolName
- **Type**: <class 'str'>
- **Required**: Yes


# PutDedicatedIpWarmupAttributesRequest

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### WarmupPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# PutDeliverabilityDashboardOptionRequest

### DashboardEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SubscribedDomains
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DomainDeliverabilityTrackingOption, aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.DomainDeliverabilityTrackingOptionOutput]]]


# PutEmailIdentityDkimAttributesRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### SigningEnabled
- **Type**: typing.Optional[bool]


# PutEmailIdentityFeedbackAttributesRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### EmailForwardingEnabled
- **Type**: typing.Optional[bool]


# PutEmailIdentityMailFromAttributesRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomain
- **Type**: typing.Optional[str]

### BehaviorOnMxFailure
- **Type**: typing.Optional[typing.Literal['REJECT_MESSAGE', 'USE_DEFAULT_VALUE']]


# RawMessage

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# ReputationOptions

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]

### LastFreshStart
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ReputationOptionsOutput

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]

### LastFreshStart
- **Type**: typing.Optional[datetime.datetime]


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


# SendEmailRequest

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Destination'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.EmailContent'>
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[str]

### ReplyToAddresses
- **Type**: typing.Optional[typing.List[str]]

### FeedbackForwardingEmailAddress
- **Type**: typing.Optional[str]

### EmailTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.MessageTag]]

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendEmailResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.ResponseMetadata'>
- **Required**: Yes


# SendQuota

### Max24HourSend
- **Type**: typing.Optional[float]

### MaxSendRate
- **Type**: typing.Optional[float]

### SentLast24Hours
- **Type**: typing.Optional[float]


# SendingOptions

### SendingEnabled
- **Type**: typing.Optional[bool]


# SnsDestination

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.Tag]
- **Required**: Yes


# Template

### TemplateArn
- **Type**: typing.Optional[str]

### TemplateData
- **Type**: typing.Optional[str]


# TrackingOptions

### CustomRedirectDomain
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateConfigurationSetEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_email.pinpoint_email_classes.EventDestinationDefinition'>
- **Required**: Yes


# VolumeStatistics

### InboxRawCount
- **Type**: typing.Optional[int]

### SpamRawCount
- **Type**: typing.Optional[int]

### ProjectedInbox
- **Type**: typing.Optional[int]

### ProjectedSpam
- **Type**: typing.Optional[int]


