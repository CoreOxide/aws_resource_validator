# sesv2_classes

# AccountDetailsTypeDef

### MailType
- **Type**: typing.Optional[typing.Literal['MARKETING', 'TRANSACTIONAL']]

### WebsiteURL
- **Type**: typing.Optional[str]

### ContactLanguage
- **Type**: typing.Optional[typing.Literal['EN', 'JA']]

### UseCaseDescription
- **Type**: typing.Optional[str]

### AdditionalContactEmailAddresses
- **Type**: typing.Optional[typing.List[str]]

### ReviewDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ReviewDetailsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetMetricDataQueryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: typing.Literal['VDM']
- **Required**: Yes

### Metric
- **Type**: typing.Literal['CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_CLICK', 'DELIVERY_COMPLAINT', 'DELIVERY_OPEN', 'OPEN', 'PERMANENT_BOUNCE', 'SEND', 'TRANSIENT_BOUNCE']
- **Required**: Yes

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CONFIGURATION_SET', 'EMAIL_IDENTITY', 'ISP'], str]]


# BatchGetMetricDataRequestRequestTypeDef

### Queries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.BatchGetMetricDataQueryTypeDef]
- **Required**: Yes


# BatchGetMetricDataResponseTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.MetricDataResultTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.MetricDataErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlacklistEntryTypeDef

### RblName
- **Type**: typing.Optional[str]

### ListingTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]


# BodyTypeDef

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ContentTypeDef]

### Html
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ContentTypeDef]


# BounceTypeDef

### BounceType
- **Type**: typing.Optional[typing.Literal['PERMANENT', 'TRANSIENT', 'UNDETERMINED']]

### BounceSubType
- **Type**: typing.Optional[str]

### DiagnosticCode
- **Type**: typing.Optional[str]


# BulkEmailContentTypeDef

### Template
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TemplateTypeDef]


# BulkEmailEntryResultTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['ACCOUNT_DAILY_QUOTA_EXCEEDED', 'ACCOUNT_SENDING_PAUSED', 'ACCOUNT_SUSPENDED', 'ACCOUNT_THROTTLED', 'CONFIGURATION_SET_NOT_FOUND', 'CONFIGURATION_SET_SENDING_PAUSED', 'FAILED', 'INVALID_PARAMETER', 'INVALID_SENDING_POOL_NAME', 'MAIL_FROM_DOMAIN_NOT_VERIFIED', 'MESSAGE_REJECTED', 'SUCCESS', 'TEMPLATE_NOT_FOUND', 'TRANSIENT_FAILURE']]

### Error
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]


# BulkEmailEntryTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DestinationTypeDef'>
- **Required**: Yes

### ReplacementTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.MessageTagTypeDef]]

### ReplacementEmailContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ReplacementEmailContentTypeDef]

### ReplacementHeaders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.MessageHeaderTypeDef]]


# CancelExportJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchDestinationOutputTypeDef

### DimensionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.CloudWatchDimensionConfigurationTypeDef]
- **Required**: Yes


# CloudWatchDestinationTypeDef

### DimensionConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.CloudWatchDimensionConfigurationTypeDef]
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


# ComplaintTypeDef

### ComplaintSubType
- **Type**: typing.Optional[str]

### ComplaintFeedbackType
- **Type**: typing.Optional[str]


# ContactListDestinationTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### ContactListImportAction
- **Type**: typing.Literal['DELETE', 'PUT']
- **Required**: Yes


# ContactListTypeDef

### ContactListName
- **Type**: typing.Optional[str]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ContactTypeDef

### EmailAddress
- **Type**: typing.Optional[str]

### TopicPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TopicPreferenceTypeDef]]

### TopicDefaultPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TopicPreferenceTypeDef]]

### UnsubscribeAll
- **Type**: typing.Optional[bool]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EventDestinationDefinitionTypeDef'>
- **Required**: Yes


# CreateConfigurationSetRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TrackingOptionsTypeDef]

### DeliveryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.DeliveryOptionsTypeDef]

### ReputationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ReputationOptionsTypeDef]

### SendingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SendingOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]

### SuppressionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SuppressionOptionsTypeDef]

### VdmOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.VdmOptionsTypeDef]


# CreateContactListRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TopicTypeDef]]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]


# CreateContactRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TopicPreferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TopicPreferenceTypeDef]]

### UnsubscribeAll
- **Type**: typing.Optional[bool]

### AttributesData
- **Type**: typing.Optional[str]


# CreateCustomVerificationEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateSubject
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessRedirectionURL
- **Type**: <class 'str'>
- **Required**: Yes

### FailureRedirectionURL
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDedicatedIpPoolRequestRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]

### ScalingMode
- **Type**: typing.Optional[typing.Literal['MANAGED', 'STANDARD']]


# CreateDeliverabilityTestReportRequestRequestTypeDef

### FromEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EmailContentTypeDef'>
- **Required**: Yes

### ReportName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]


# CreateDeliverabilityTestReportResponseTypeDef

### ReportId
- **Type**: <class 'str'>
- **Required**: Yes

### DeliverabilityTestStatus
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEmailIdentityPolicyRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# CreateEmailIdentityRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]

### DkimSigningAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.DkimSigningAttributesTypeDef]

### ConfigurationSetName
- **Type**: typing.Optional[str]


# CreateEmailIdentityResponseTypeDef

### IdentityType
- **Type**: typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']
- **Required**: Yes

### VerifiedForSendingStatus
- **Type**: <class 'bool'>
- **Required**: Yes

### DkimAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DkimAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EmailTemplateContentTypeDef'>
- **Required**: Yes


# CreateExportJobRequestRequestTypeDef

### ExportDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ExportDataSourceTypeDef'>
- **Required**: Yes

### ExportDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ExportDestinationTypeDef'>
- **Required**: Yes


# CreateExportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImportJobRequestRequestTypeDef

### ImportDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ImportDestinationTypeDef'>
- **Required**: Yes

### ImportDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ImportDataSourceTypeDef'>
- **Required**: Yes


# CreateImportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomVerificationEmailTemplateMetadataTypeDef

### TemplateName
- **Type**: typing.Optional[str]

### FromEmailAddress
- **Type**: typing.Optional[str]

### TemplateSubject
- **Type**: typing.Optional[str]

### SuccessRedirectionURL
- **Type**: typing.Optional[str]

### FailureRedirectionURL
- **Type**: typing.Optional[str]


# DailyVolumeTypeDef

### StartDate
- **Type**: typing.Optional[datetime.datetime]

### VolumeStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.VolumeStatisticsTypeDef]

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DomainIspPlacementTypeDef]]


# DashboardAttributesTypeDef

### EngagementMetrics
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DashboardOptionsTypeDef

### EngagementMetrics
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DedicatedIpPoolTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingMode
- **Type**: typing.Literal['MANAGED', 'STANDARD']
- **Required**: Yes


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


# DeleteContactListRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomVerificationEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDedicatedIpPoolRequestRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailIdentityPolicyRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailIdentityRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSuppressedDestinationRequestRequestTypeDef

### EmailAddress
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

### SigningAttributesOrigin
- **Type**: typing.Optional[typing.Literal['AWS_SES', 'EXTERNAL']]

### NextSigningKeyLength
- **Type**: typing.Optional[typing.Literal['RSA_1024_BIT', 'RSA_2048_BIT']]

### CurrentSigningKeyLength
- **Type**: typing.Optional[typing.Literal['RSA_1024_BIT', 'RSA_2048_BIT']]

### LastKeyGenerationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# DkimSigningAttributesTypeDef

### DomainSigningSelector
- **Type**: typing.Optional[str]

### DomainSigningPrivateKey
- **Type**: typing.Optional[str]

### NextSigningKeyLength
- **Type**: typing.Optional[typing.Literal['RSA_1024_BIT', 'RSA_2048_BIT']]


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


# DomainDeliverabilityTrackingOptionOutputTypeDef

### Domain
- **Type**: typing.Optional[str]

### SubscriptionStartDate
- **Type**: typing.Optional[datetime.datetime]

### InboxPlacementTrackingOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.InboxPlacementTrackingOptionOutputTypeDef]


# DomainDeliverabilityTrackingOptionTypeDef

### Domain
- **Type**: typing.Optional[str]

### SubscriptionStartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### InboxPlacementTrackingOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.InboxPlacementTrackingOptionTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MessageTypeDef]

### Raw
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.RawMessageTypeDef]

### Template
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TemplateTypeDef]


# EmailInsightsTypeDef

### Destination
- **Type**: typing.Optional[str]

### Isp
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2_classes.InsightsEventTypeDef]]


# EmailTemplateContentTypeDef

### Subject
- **Type**: typing.Optional[str]

### Text
- **Type**: typing.Optional[str]

### Html
- **Type**: typing.Optional[str]


# EmailTemplateMetadataTypeDef

### TemplateName
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# EventBridgeDestinationTypeDef

### EventBusArn
- **Type**: <class 'str'>
- **Required**: Yes


# EventDestinationDefinitionTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### MatchingEventTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_DELAY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND', 'SUBSCRIPTION']]]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.KinesisFirehoseDestinationTypeDef]

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.CloudWatchDestinationTypeDef]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SnsDestinationTypeDef]

### EventBridgeDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.EventBridgeDestinationTypeDef]

### PinpointDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.PinpointDestinationTypeDef]


# EventDestinationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.List[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_DELAY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND', 'SUBSCRIPTION']]
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.KinesisFirehoseDestinationTypeDef]

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.CloudWatchDestinationOutputTypeDef]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SnsDestinationTypeDef]

### EventBridgeDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.EventBridgeDestinationTypeDef]

### PinpointDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.PinpointDestinationTypeDef]


# EventDetailsTypeDef

### Bounce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.BounceTypeDef]

### Complaint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ComplaintTypeDef]


# ExportDataSourceOutputTypeDef

### MetricsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MetricsDataSourceOutputTypeDef]

### MessageInsightsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MessageInsightsDataSourceOutputTypeDef]


# ExportDataSourceTypeDef

### MetricsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MetricsDataSourceTypeDef]

### MessageInsightsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MessageInsightsDataSourceTypeDef]


# ExportDestinationTypeDef

### DataFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### S3Url
- **Type**: typing.Optional[str]


# ExportJobSummaryTypeDef

### JobId
- **Type**: typing.Optional[str]

### ExportSourceType
- **Type**: typing.Optional[typing.Literal['MESSAGE_INSIGHTS', 'METRICS_DATA']]

### JobStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'FAILED', 'PROCESSING']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CompletedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ExportMetricTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_CLICK', 'DELIVERY_COMPLAINT', 'DELIVERY_OPEN', 'OPEN', 'PERMANENT_BOUNCE', 'SEND', 'TRANSIENT_BOUNCE']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['RATE', 'VOLUME']]


# ExportStatisticsTypeDef

### ProcessedRecordsCount
- **Type**: typing.Optional[int]

### ExportedRecordsCount
- **Type**: typing.Optional[int]


# FailureInfoTypeDef

### FailedRecordsS3Url
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetAccountResponseTypeDef

### DedicatedIpAutoWarmupEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### EnforcementStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionAccessEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SendQuota
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.SendQuotaTypeDef'>
- **Required**: Yes

### SendingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SuppressionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.SuppressionAttributesTypeDef'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.AccountDetailsTypeDef'>
- **Required**: Yes

### VdmAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.VdmAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBlacklistReportsRequestRequestTypeDef

### BlacklistItemNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetBlacklistReportsResponseTypeDef

### BlacklistReport
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.sesv2_classes.BlacklistEntryTypeDef]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsResponseTypeDef

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.EventDestinationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TrackingOptionsTypeDef'>
- **Required**: Yes

### DeliveryOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DeliveryOptionsTypeDef'>
- **Required**: Yes

### ReputationOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ReputationOptionsOutputTypeDef'>
- **Required**: Yes

### SendingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.SendingOptionsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]
- **Required**: Yes

### SuppressionOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.SuppressionOptionsOutputTypeDef'>
- **Required**: Yes

### VdmOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.VdmOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContactListRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactListResponseTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TopicTypeDef]
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContactRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactResponseTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TopicPreferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TopicPreferenceTypeDef]
- **Required**: Yes

### TopicDefaultPreferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TopicPreferenceTypeDef]
- **Required**: Yes

### UnsubscribeAll
- **Type**: <class 'bool'>
- **Required**: Yes

### AttributesData
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCustomVerificationEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomVerificationEmailTemplateResponseTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateSubject
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessRedirectionURL
- **Type**: <class 'str'>
- **Required**: Yes

### FailureRedirectionURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDedicatedIpPoolRequestRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDedicatedIpPoolResponseTypeDef

### DedicatedIpPool
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DedicatedIpPoolTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDedicatedIpRequestRequestTypeDef

### Ip
- **Type**: <class 'str'>
- **Required**: Yes


# GetDedicatedIpResponseTypeDef

### DedicatedIp
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DedicatedIpTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDedicatedIpsRequestRequestTypeDef

### PoolName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# GetDedicatedIpsResponseTypeDef

### DedicatedIps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DedicatedIpTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DomainDeliverabilityTrackingOptionOutputTypeDef]
- **Required**: Yes

### PendingExpirationSubscribedDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DomainDeliverabilityTrackingOptionOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeliverabilityTestReportRequestRequestTypeDef

### ReportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliverabilityTestReportResponseTypeDef

### DeliverabilityTestReport
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DeliverabilityTestReportTypeDef'>
- **Required**: Yes

### OverallPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.PlacementStatisticsTypeDef'>
- **Required**: Yes

### IspPlacements
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.IspPlacementTypeDef]
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainDeliverabilityCampaignRequestRequestTypeDef

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainDeliverabilityCampaignResponseTypeDef

### DomainDeliverabilityCampaign
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DomainDeliverabilityCampaignTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.OverallVolumeTypeDef'>
- **Required**: Yes

### DailyVolumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DailyVolumeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEmailIdentityPoliciesRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailIdentityPoliciesResponseTypeDef

### Policies
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DkimAttributesTypeDef'>
- **Required**: Yes

### MailFromAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.MailFromAttributesTypeDef'>
- **Required**: Yes

### Policies
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationStatus
- **Type**: typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']
- **Required**: Yes

### VerificationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.VerificationInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailTemplateResponseTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EmailTemplateContentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExportJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportSourceType
- **Type**: typing.Literal['MESSAGE_INSIGHTS', 'METRICS_DATA']
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'FAILED', 'PROCESSING']
- **Required**: Yes

### ExportDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ExportDestinationTypeDef'>
- **Required**: Yes

### ExportDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ExportDataSourceOutputTypeDef'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.FailureInfoTypeDef'>
- **Required**: Yes

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ExportStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ImportDestinationTypeDef'>
- **Required**: Yes

### ImportDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ImportDataSourceTypeDef'>
- **Required**: Yes

### FailureInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.FailureInfoTypeDef'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'FAILED', 'PROCESSING']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProcessedRecordsCount
- **Type**: <class 'int'>
- **Required**: Yes

### FailedRecordsCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMessageInsightsRequestRequestTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMessageInsightsResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### EmailTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.MessageTagTypeDef]
- **Required**: Yes

### Insights
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.EmailInsightsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSuppressedDestinationRequestRequestTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuppressedDestinationResponseTypeDef

### SuppressedDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.SuppressedDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GuardianAttributesTypeDef

### OptimizedSharedDelivery
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GuardianOptionsTypeDef

### OptimizedSharedDelivery
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# IdentityInfoTypeDef

### IdentityType
- **Type**: typing.Optional[typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']]

### IdentityName
- **Type**: typing.Optional[str]

### SendingEnabled
- **Type**: typing.Optional[bool]

### VerificationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']]


# ImportDataSourceTypeDef

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# ImportDestinationTypeDef

### SuppressionListDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SuppressionListDestinationTypeDef]

### ContactListDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ContactListDestinationTypeDef]


# ImportJobSummaryTypeDef

### JobId
- **Type**: typing.Optional[str]

### ImportDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ImportDestinationTypeDef]

### JobStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'FAILED', 'PROCESSING']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ProcessedRecordsCount
- **Type**: typing.Optional[int]

### FailedRecordsCount
- **Type**: typing.Optional[int]


# InboxPlacementTrackingOptionOutputTypeDef

### Global
- **Type**: typing.Optional[bool]

### TrackedIsps
- **Type**: typing.Optional[typing.List[str]]


# InboxPlacementTrackingOptionTypeDef

### Global
- **Type**: typing.Optional[bool]

### TrackedIsps
- **Type**: typing.Optional[typing.Sequence[str]]


# InsightsEventTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_DELAY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND', 'SUBSCRIPTION']]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.EventDetailsTypeDef]


# IspPlacementTypeDef

### IspName
- **Type**: typing.Optional[str]

### PlacementStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.PlacementStatisticsTypeDef]


# KinesisFirehoseDestinationTypeDef

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListConfigurationSetsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListConfigurationSetsResponseTypeDef

### ConfigurationSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactListsRequestRequestTypeDef

### PageSize
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListContactListsResponseTypeDef

### ContactLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.ContactListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactsFilterTypeDef

### FilteredStatus
- **Type**: typing.Optional[typing.Literal['OPT_IN', 'OPT_OUT']]

### TopicFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TopicFilterTypeDef]


# ListContactsRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ListContactsFilterTypeDef]

### PageSize
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListContactsResponseTypeDef

### Contacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.ContactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomVerificationEmailTemplatesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListCustomVerificationEmailTemplatesResponseTypeDef

### CustomVerificationEmailTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.CustomVerificationEmailTemplateMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDedicatedIpPoolsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDedicatedIpPoolsResponseTypeDef

### DedicatedIpPools
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeliverabilityTestReportsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDeliverabilityTestReportsResponseTypeDef

### DeliverabilityTestReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DeliverabilityTestReportTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DomainDeliverabilityCampaignTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEmailIdentitiesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListEmailIdentitiesResponseTypeDef

### EmailIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.IdentityInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEmailTemplatesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListEmailTemplatesResponseTypeDef

### TemplatesMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.EmailTemplateMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExportJobsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### ExportSourceType
- **Type**: typing.Optional[typing.Literal['MESSAGE_INSIGHTS', 'METRICS_DATA']]

### JobStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'FAILED', 'PROCESSING']]


# ListExportJobsResponseTypeDef

### ExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.ExportJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportJobsRequestRequestTypeDef

### ImportDestinationType
- **Type**: typing.Optional[typing.Literal['CONTACT_LIST', 'SUPPRESSION_LIST']]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListImportJobsResponseTypeDef

### ImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.ImportJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagementOptionsTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: typing.Optional[str]


# ListRecommendationsRequestRequestTypeDef

### Filter
- **Type**: typing.Optional[typing.Mapping[typing.Literal['IMPACT', 'RESOURCE_ARN', 'STATUS', 'TYPE'], str]]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListRecommendationsResponseTypeDef

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.RecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSuppressedDestinationsRequestRequestTypeDef

### Reasons
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'COMPLAINT']]]

### StartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListSuppressedDestinationsResponseTypeDef

### SuppressedDestinationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.SuppressedDestinationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
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


# MessageHeaderTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# MessageInsightsDataSourceOutputTypeDef

### StartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Include
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MessageInsightsFiltersOutputTypeDef]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MessageInsightsFiltersOutputTypeDef]

### MaxResults
- **Type**: typing.Optional[int]


# MessageInsightsDataSourceTypeDef

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Include
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MessageInsightsFiltersTypeDef]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.MessageInsightsFiltersTypeDef]

### MaxResults
- **Type**: typing.Optional[int]


# MessageInsightsFiltersOutputTypeDef

### FromEmailAddress
- **Type**: typing.Optional[typing.List[str]]

### Destination
- **Type**: typing.Optional[typing.List[str]]

### Subject
- **Type**: typing.Optional[typing.List[str]]

### Isp
- **Type**: typing.Optional[typing.List[str]]

### LastDeliveryEvent
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLAINT', 'DELIVERY', 'PERMANENT_BOUNCE', 'SEND', 'TRANSIENT_BOUNCE', 'UNDETERMINED_BOUNCE']]]

### LastEngagementEvent
- **Type**: typing.Optional[typing.List[typing.Literal['CLICK', 'OPEN']]]


# MessageInsightsFiltersTypeDef

### FromEmailAddress
- **Type**: typing.Optional[typing.Sequence[str]]

### Destination
- **Type**: typing.Optional[typing.Sequence[str]]

### Subject
- **Type**: typing.Optional[typing.Sequence[str]]

### Isp
- **Type**: typing.Optional[typing.Sequence[str]]

### LastDeliveryEvent
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLAINT', 'DELIVERY', 'PERMANENT_BOUNCE', 'SEND', 'TRANSIENT_BOUNCE', 'UNDETERMINED_BOUNCE']]]

### LastEngagementEvent
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLICK', 'OPEN']]]


# MessageTagTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# MessageTypeDef

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ContentTypeDef'>
- **Required**: Yes

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.BodyTypeDef'>
- **Required**: Yes

### Headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.MessageHeaderTypeDef]]


# MetricDataErrorTypeDef

### Id
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'INTERNAL_FAILURE']]

### Message
- **Type**: typing.Optional[str]


# MetricDataResultTypeDef

### Id
- **Type**: typing.Optional[str]

### Timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### Values
- **Type**: typing.Optional[typing.List[int]]


# MetricsDataSourceOutputTypeDef

### Dimensions
- **Type**: typing.Dict[typing.Literal['CONFIGURATION_SET', 'EMAIL_IDENTITY', 'ISP'], typing.List[str]]
- **Required**: Yes

### Namespace
- **Type**: typing.Literal['VDM']
- **Required**: Yes

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.ExportMetricTypeDef]
- **Required**: Yes

### StartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# MetricsDataSourceTypeDef

### Dimensions
- **Type**: typing.Mapping[typing.Literal['CONFIGURATION_SET', 'EMAIL_IDENTITY', 'ISP'], typing.Sequence[str]]
- **Required**: Yes

### Namespace
- **Type**: typing.Literal['VDM']
- **Required**: Yes

### Metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.ExportMetricTypeDef]
- **Required**: Yes

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# OverallVolumeTypeDef

### VolumeStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.VolumeStatisticsTypeDef]

### ReadRatePercent
- **Type**: typing.Optional[float]

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DomainIspPlacementTypeDef]]


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


# PutAccountDetailsRequestRequestTypeDef

### MailType
- **Type**: typing.Literal['MARKETING', 'TRANSACTIONAL']
- **Required**: Yes

### WebsiteURL
- **Type**: <class 'str'>
- **Required**: Yes

### UseCaseDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ContactLanguage
- **Type**: typing.Optional[typing.Literal['EN', 'JA']]

### AdditionalContactEmailAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### ProductionAccessEnabled
- **Type**: typing.Optional[bool]


# PutAccountSendingAttributesRequestRequestTypeDef

### SendingEnabled
- **Type**: typing.Optional[bool]


# PutAccountSuppressionAttributesRequestRequestTypeDef

### SuppressedReasons
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'COMPLAINT']]]


# PutAccountVdmAttributesRequestRequestTypeDef

### VdmAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.VdmAttributesTypeDef'>
- **Required**: Yes


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


# PutConfigurationSetSuppressionOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SuppressedReasons
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'COMPLAINT']]]


# PutConfigurationSetTrackingOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomRedirectDomain
- **Type**: typing.Optional[str]


# PutConfigurationSetVdmOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### VdmOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.VdmOptionsTypeDef]


# PutDedicatedIpInPoolRequestRequestTypeDef

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPoolName
- **Type**: <class 'str'>
- **Required**: Yes


# PutDedicatedIpPoolScalingAttributesRequestRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingMode
- **Type**: typing.Literal['MANAGED', 'STANDARD']
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
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.sesv2_classes.DomainDeliverabilityTrackingOptionTypeDef, aws_resource_validator.pydantic_models.sesv2_classes.DomainDeliverabilityTrackingOptionOutputTypeDef]]]


# PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: typing.Optional[str]


# PutEmailIdentityDkimAttributesRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### SigningEnabled
- **Type**: typing.Optional[bool]


# PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### SigningAttributesOrigin
- **Type**: typing.Literal['AWS_SES', 'EXTERNAL']
- **Required**: Yes

### SigningAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.DkimSigningAttributesTypeDef]


# PutEmailIdentityDkimSigningAttributesResponseTypeDef

### DkimStatus
- **Type**: typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']
- **Required**: Yes

### DkimTokens
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# PutSuppressedDestinationRequestRequestTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Literal['BOUNCE', 'COMPLAINT']
- **Required**: Yes


# RawMessageTypeDef

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# RecommendationTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['BIMI', 'DKIM', 'DMARC', 'SPF']]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FIXED', 'OPEN']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Impact
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW']]


# ReplacementEmailContentTypeDef

### ReplacementTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ReplacementTemplateTypeDef]


# ReplacementTemplateTypeDef

### ReplacementTemplateData
- **Type**: typing.Optional[str]


# ReputationOptionsOutputTypeDef

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]

### LastFreshStart
- **Type**: typing.Optional[datetime.datetime]


# ReputationOptionsTypeDef

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]

### LastFreshStart
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# ReviewDetailsTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DENIED', 'FAILED', 'GRANTED', 'PENDING']]

### CaseId
- **Type**: typing.Optional[str]


# SOARecordTypeDef

### PrimaryNameServer
- **Type**: typing.Optional[str]

### AdminEmail
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[int]


# SendBulkEmailRequestRequestTypeDef

### DefaultContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.BulkEmailContentTypeDef'>
- **Required**: Yes

### BulkEmailEntries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.BulkEmailEntryTypeDef]
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[str]

### FromEmailAddressIdentityArn
- **Type**: typing.Optional[str]

### ReplyToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### FeedbackForwardingEmailAddress
- **Type**: typing.Optional[str]

### FeedbackForwardingEmailAddressIdentityArn
- **Type**: typing.Optional[str]

### DefaultEmailTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.MessageTagTypeDef]]

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendBulkEmailResponseTypeDef

### BulkEmailEntryResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.BulkEmailEntryResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendCustomVerificationEmailRequestRequestTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendCustomVerificationEmailResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendEmailRequestRequestTypeDef

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EmailContentTypeDef'>
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[str]

### FromEmailAddressIdentityArn
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.DestinationTypeDef]

### ReplyToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### FeedbackForwardingEmailAddress
- **Type**: typing.Optional[str]

### FeedbackForwardingEmailAddressIdentityArn
- **Type**: typing.Optional[str]

### EmailTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.MessageTagTypeDef]]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### ListManagementOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ListManagementOptionsTypeDef]


# SendEmailResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
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


# SuppressedDestinationAttributesTypeDef

### MessageId
- **Type**: typing.Optional[str]

### FeedbackId
- **Type**: typing.Optional[str]


# SuppressedDestinationSummaryTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Literal['BOUNCE', 'COMPLAINT']
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# SuppressedDestinationTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Literal['BOUNCE', 'COMPLAINT']
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SuppressedDestinationAttributesTypeDef]


# SuppressionAttributesTypeDef

### SuppressedReasons
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'COMPLAINT']]]


# SuppressionListDestinationTypeDef

### SuppressionListImportAction
- **Type**: typing.Literal['DELETE', 'PUT']
- **Required**: Yes


# SuppressionOptionsOutputTypeDef

### SuppressedReasons
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'COMPLAINT']]]


# SuppressionOptionsTypeDef

### SuppressedReasons
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'COMPLAINT']]]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateTypeDef

### TemplateName
- **Type**: typing.Optional[str]

### TemplateArn
- **Type**: typing.Optional[str]

### TemplateData
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.MessageHeaderTypeDef]]


# TestRenderEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateData
- **Type**: <class 'str'>
- **Required**: Yes


# TestRenderEmailTemplateResponseTypeDef

### RenderedTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TopicFilterTypeDef

### TopicName
- **Type**: typing.Optional[str]

### UseDefaultIfPreferenceUnavailable
- **Type**: typing.Optional[bool]


# TopicPreferenceTypeDef

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionStatus
- **Type**: typing.Literal['OPT_IN', 'OPT_OUT']
- **Required**: Yes


# TopicTypeDef

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultSubscriptionStatus
- **Type**: typing.Literal['OPT_IN', 'OPT_OUT']
- **Required**: Yes

### Description
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EventDestinationDefinitionTypeDef'>
- **Required**: Yes


# UpdateContactListRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TopicTypeDef]]

### Description
- **Type**: typing.Optional[str]


# UpdateContactRequestRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TopicPreferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TopicPreferenceTypeDef]]

### UnsubscribeAll
- **Type**: typing.Optional[bool]

### AttributesData
- **Type**: typing.Optional[str]


# UpdateCustomVerificationEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateSubject
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessRedirectionURL
- **Type**: <class 'str'>
- **Required**: Yes

### FailureRedirectionURL
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateEmailIdentityPolicyRequestRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EmailTemplateContentTypeDef'>
- **Required**: Yes


# VdmAttributesTypeDef

### VdmEnabled
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DashboardAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.DashboardAttributesTypeDef]

### GuardianAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.GuardianAttributesTypeDef]


# VdmOptionsTypeDef

### DashboardOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.DashboardOptionsTypeDef]

### GuardianOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.GuardianOptionsTypeDef]


# VerificationInfoTypeDef

### LastCheckedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ErrorType
- **Type**: typing.Optional[typing.Literal['DNS_SERVER_ERROR', 'HOST_NOT_FOUND', 'INVALID_VALUE', 'SERVICE_ERROR', 'TYPE_NOT_FOUND']]

### SOARecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SOARecordTypeDef]


# VolumeStatisticsTypeDef

### InboxRawCount
- **Type**: typing.Optional[int]

### SpamRawCount
- **Type**: typing.Optional[int]

### ProjectedInbox
- **Type**: typing.Optional[int]

### ProjectedSpam
- **Type**: typing.Optional[int]


