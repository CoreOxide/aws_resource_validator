# Sesv2 Sesv2 Classes

# AccountDetails

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
- **Type**: <class 'NoneType'>


# ArchivingOptions

### ArchiveArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetMetricDataQuery

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['CONFIGURATION_SET', 'EMAIL_IDENTITY', 'ISP'], str]]


# BatchGetMetricDataRequest

### Queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.BatchGetMetricDataQuery]
- **Required**: Yes


# BatchGetMetricDataResponse

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MetricDataResult]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MetricDataError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# BlacklistEntry

### RblName
- **Type**: typing.Optional[str]

### ListingTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]


# Body

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Content]

### Html
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Content]


# Bounce

### BounceType
- **Type**: typing.Optional[typing.Literal['PERMANENT', 'TRANSIENT', 'UNDETERMINED']]

### BounceSubType
- **Type**: typing.Optional[str]

### DiagnosticCode
- **Type**: typing.Optional[str]


# BulkEmailContent

### Template
- **Type**: <class 'NoneType'>


# BulkEmailEntry

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Destination'>
- **Required**: Yes

### ReplacementTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageTag]]

### ReplacementEmailContent
- **Type**: <class 'NoneType'>

### ReplacementHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageHeader]]


# BulkEmailEntryResult

### Status
- **Type**: typing.Optional[typing.Literal['ACCOUNT_DAILY_QUOTA_EXCEEDED', 'ACCOUNT_SENDING_PAUSED', 'ACCOUNT_SUSPENDED', 'ACCOUNT_THROTTLED', 'CONFIGURATION_SET_NOT_FOUND', 'CONFIGURATION_SET_SENDING_PAUSED', 'FAILED', 'INVALID_PARAMETER', 'INVALID_SENDING_POOL_NAME', 'MAIL_FROM_DOMAIN_NOT_VERIFIED', 'MESSAGE_REJECTED', 'SUCCESS', 'TEMPLATE_NOT_FOUND', 'TRANSIENT_FAILURE']]

### Error
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]


# CancelExportJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchDestination

### DimensionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.CloudWatchDimensionConfiguration]
- **Required**: Yes


# CloudWatchDestinationOutput

### DimensionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.CloudWatchDimensionConfiguration]
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


# Complaint

### ComplaintSubType
- **Type**: typing.Optional[str]

### ComplaintFeedbackType
- **Type**: typing.Optional[str]


# Contact

### EmailAddress
- **Type**: typing.Optional[str]

### TopicPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.TopicPreference]]

### TopicDefaultPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.TopicPreference]]

### UnsubscribeAll
- **Type**: typing.Optional[bool]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ContactList

### ContactListName
- **Type**: typing.Optional[str]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ContactListDestination

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### ContactListImportAction
- **Type**: typing.Literal['DELETE', 'PUT']
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EventDestinationDefinition'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ReputationOptions, aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ReputationOptionsOutput, NoneType]

### SendingOptions
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]]

### SuppressionOptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SuppressionOptions, aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SuppressionOptionsOutput, NoneType]

### VdmOptions
- **Type**: <class 'NoneType'>

### ArchivingOptions
- **Type**: <class 'NoneType'>


# CreateContactListRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Topic]]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]]


# CreateContactRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TopicPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.TopicPreference]]

### UnsubscribeAll
- **Type**: typing.Optional[bool]

### AttributesData
- **Type**: typing.Optional[str]


# CreateCustomVerificationEmailTemplateRequest

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


# CreateDedicatedIpPoolRequest

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]]

### ScalingMode
- **Type**: typing.Optional[typing.Literal['MANAGED', 'STANDARD']]


# CreateDeliverabilityTestReportRequest

### FromEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EmailContent'>
- **Required**: Yes

### ReportName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]]


# CreateDeliverabilityTestReportResponse

### ReportId
- **Type**: <class 'str'>
- **Required**: Yes

### DeliverabilityTestStatus
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEmailIdentityPolicyRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# CreateEmailIdentityRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]]

### DkimSigningAttributes
- **Type**: <class 'NoneType'>

### ConfigurationSetName
- **Type**: typing.Optional[str]


# CreateEmailIdentityResponse

### IdentityType
- **Type**: typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']
- **Required**: Yes

### VerifiedForSendingStatus
- **Type**: <class 'bool'>
- **Required**: Yes

### DkimAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DkimAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EmailTemplateContent'>
- **Required**: Yes


# CreateExportJobRequest

### ExportDataSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportDataSource, aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportDataSourceOutput]
- **Required**: Yes

### ExportDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportDestination'>
- **Required**: Yes


# CreateExportJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImportJobRequest

### ImportDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ImportDestination'>
- **Required**: Yes

### ImportDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ImportDataSource'>
- **Required**: Yes


# CreateImportJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMultiRegionEndpointRequest

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Details'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]]


# CreateMultiRegionEndpointResponse

### Status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY']
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# CustomVerificationEmailTemplateMetadata

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


# DailyVolume

### StartDate
- **Type**: typing.Optional[datetime.datetime]

### VolumeStatistics
- **Type**: <class 'NoneType'>

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DomainIspPlacement]]


# DashboardAttributes

### EngagementMetrics
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DashboardOptions

### EngagementMetrics
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


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


# DedicatedIpPool

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingMode
- **Type**: typing.Literal['MANAGED', 'STANDARD']
- **Required**: Yes


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


# DeleteContactListRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomVerificationEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDedicatedIpPoolRequest

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailIdentityPolicyRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailIdentityRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiRegionEndpointRequest

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiRegionEndpointResponse

### Status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSuppressedDestinationRequest

### EmailAddress
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

### MaxDeliverySeconds
- **Type**: typing.Optional[int]


# Destination

### ToAddresses
- **Type**: typing.Optional[typing.List[str]]

### CcAddresses
- **Type**: typing.Optional[typing.List[str]]

### BccAddresses
- **Type**: typing.Optional[typing.List[str]]


# Details

### RoutesDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.RouteDetails]
- **Required**: Yes


# DkimAttributes

### SigningEnabled
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']]

### Tokens
- **Type**: typing.Optional[typing.List[str]]

### SigningAttributesOrigin
- **Type**: typing.Optional[typing.Literal['AWS_SES', 'AWS_SES_AF_SOUTH_1', 'AWS_SES_AP_NORTHEAST_1', 'AWS_SES_AP_NORTHEAST_2', 'AWS_SES_AP_NORTHEAST_3', 'AWS_SES_AP_SOUTHEAST_1', 'AWS_SES_AP_SOUTHEAST_2', 'AWS_SES_AP_SOUTHEAST_3', 'AWS_SES_AP_SOUTH_1', 'AWS_SES_CA_CENTRAL_1', 'AWS_SES_EU_CENTRAL_1', 'AWS_SES_EU_NORTH_1', 'AWS_SES_EU_SOUTH_1', 'AWS_SES_EU_WEST_1', 'AWS_SES_EU_WEST_2', 'AWS_SES_EU_WEST_3', 'AWS_SES_IL_CENTRAL_1', 'AWS_SES_ME_SOUTH_1', 'AWS_SES_SA_EAST_1', 'AWS_SES_US_EAST_1', 'AWS_SES_US_EAST_2', 'AWS_SES_US_WEST_1', 'AWS_SES_US_WEST_2', 'EXTERNAL']]

### NextSigningKeyLength
- **Type**: typing.Optional[typing.Literal['RSA_1024_BIT', 'RSA_2048_BIT']]

### CurrentSigningKeyLength
- **Type**: typing.Optional[typing.Literal['RSA_1024_BIT', 'RSA_2048_BIT']]

### LastKeyGenerationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# DkimSigningAttributes

### DomainSigningSelector
- **Type**: typing.Optional[str]

### DomainSigningPrivateKey
- **Type**: typing.Optional[str]

### NextSigningKeyLength
- **Type**: typing.Optional[typing.Literal['RSA_1024_BIT', 'RSA_2048_BIT']]

### DomainSigningAttributesOrigin
- **Type**: typing.Optional[typing.Literal['AWS_SES', 'AWS_SES_AF_SOUTH_1', 'AWS_SES_AP_NORTHEAST_1', 'AWS_SES_AP_NORTHEAST_2', 'AWS_SES_AP_NORTHEAST_3', 'AWS_SES_AP_SOUTHEAST_1', 'AWS_SES_AP_SOUTHEAST_2', 'AWS_SES_AP_SOUTHEAST_3', 'AWS_SES_AP_SOUTH_1', 'AWS_SES_CA_CENTRAL_1', 'AWS_SES_EU_CENTRAL_1', 'AWS_SES_EU_NORTH_1', 'AWS_SES_EU_SOUTH_1', 'AWS_SES_EU_WEST_1', 'AWS_SES_EU_WEST_2', 'AWS_SES_EU_WEST_3', 'AWS_SES_IL_CENTRAL_1', 'AWS_SES_ME_SOUTH_1', 'AWS_SES_SA_EAST_1', 'AWS_SES_US_EAST_1', 'AWS_SES_US_EAST_2', 'AWS_SES_US_WEST_1', 'AWS_SES_US_WEST_2', 'EXTERNAL']]


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.InboxPlacementTrackingOption, aws_resource_validator.pydantic_models.sesv2.sesv2_classes.InboxPlacementTrackingOptionOutput, NoneType]


# DomainDeliverabilityTrackingOptionOutput

### Domain
- **Type**: typing.Optional[str]

### SubscriptionStartDate
- **Type**: typing.Optional[datetime.datetime]

### InboxPlacementTrackingOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.InboxPlacementTrackingOptionOutput]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Message]

### Raw
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.RawMessage]

### Template
- **Type**: <class 'NoneType'>


# EmailInsights

### Destination
- **Type**: typing.Optional[str]

### Isp
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.InsightsEvent]]


# EmailTemplateContent

### Subject
- **Type**: typing.Optional[str]

### Text
- **Type**: typing.Optional[str]

### Html
- **Type**: typing.Optional[str]


# EmailTemplateMetadata

### TemplateName
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# EventBridgeDestination

### EventBusArn
- **Type**: <class 'str'>
- **Required**: Yes


# EventDestination

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.List[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_DELAY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND', 'SUBSCRIPTION']]
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.CloudWatchDestinationOutput]

### SnsDestination
- **Type**: <class 'NoneType'>

### EventBridgeDestination
- **Type**: <class 'NoneType'>

### PinpointDestination
- **Type**: <class 'NoneType'>


# EventDestinationDefinition

### Enabled
- **Type**: typing.Optional[bool]

### MatchingEventTypes
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_DELAY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND', 'SUBSCRIPTION']]]

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### CloudWatchDestination
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.CloudWatchDestination, aws_resource_validator.pydantic_models.sesv2.sesv2_classes.CloudWatchDestinationOutput, NoneType]

### SnsDestination
- **Type**: <class 'NoneType'>

### EventBridgeDestination
- **Type**: <class 'NoneType'>

### PinpointDestination
- **Type**: <class 'NoneType'>


# EventDetails

### Bounce
- **Type**: <class 'NoneType'>

### Complaint
- **Type**: <class 'NoneType'>


# ExportDataSource

### MetricsDataSource
- **Type**: <class 'NoneType'>

### MessageInsightsDataSource
- **Type**: <class 'NoneType'>


# ExportDataSourceOutput

### MetricsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MetricsDataSourceOutput]

### MessageInsightsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageInsightsDataSourceOutput]


# ExportDestination

### DataFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### S3Url
- **Type**: typing.Optional[str]


# ExportJobSummary

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


# ExportMetric

### Name
- **Type**: typing.Optional[typing.Literal['CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_CLICK', 'DELIVERY_COMPLAINT', 'DELIVERY_OPEN', 'OPEN', 'PERMANENT_BOUNCE', 'SEND', 'TRANSIENT_BOUNCE']]

### Aggregation
- **Type**: typing.Optional[typing.Literal['RATE', 'VOLUME']]


# ExportStatistics

### ProcessedRecordsCount
- **Type**: typing.Optional[int]

### ExportedRecordsCount
- **Type**: typing.Optional[int]


# FailureInfo

### FailedRecordsS3Url
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetAccountResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SendQuota'>
- **Required**: Yes

### SendingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SuppressionAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SuppressionAttributes'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.AccountDetails'>
- **Required**: Yes

### VdmAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.VdmAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetBlacklistReportsRequest

### BlacklistItemNames
- **Type**: typing.List[str]
- **Required**: Yes


# GetBlacklistReportsResponse

### BlacklistReport
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.BlacklistEntry]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationSetEventDestinationsResponse

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EventDestination]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.TrackingOptions'>
- **Required**: Yes

### DeliveryOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DeliveryOptions'>
- **Required**: Yes

### ReputationOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ReputationOptionsOutput'>
- **Required**: Yes

### SendingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SendingOptions'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]
- **Required**: Yes

### SuppressionOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SuppressionOptionsOutput'>
- **Required**: Yes

### VdmOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.VdmOptions'>
- **Required**: Yes

### ArchivingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ArchivingOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetContactListRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactListResponse

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Topic]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetContactRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactResponse

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TopicPreferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.TopicPreference]
- **Required**: Yes

### TopicDefaultPreferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.TopicPreference]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetCustomVerificationEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomVerificationEmailTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDedicatedIpPoolRequest

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDedicatedIpPoolResponse

### DedicatedIpPool
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DedicatedIpPool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDedicatedIpRequest

### Ip
- **Type**: <class 'str'>
- **Required**: Yes


# GetDedicatedIpResponse

### DedicatedIp
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DedicatedIp'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDedicatedIpsRequest

### PoolName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# GetDedicatedIpsResponse

### DedicatedIps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DedicatedIp]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DomainDeliverabilityTrackingOptionOutput]
- **Required**: Yes

### PendingExpirationSubscribedDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DomainDeliverabilityTrackingOptionOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeliverabilityTestReportRequest

### ReportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliverabilityTestReportResponse

### DeliverabilityTestReport
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DeliverabilityTestReport'>
- **Required**: Yes

### OverallPlacement
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.PlacementStatistics'>
- **Required**: Yes

### IspPlacements
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.IspPlacement]
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainDeliverabilityCampaignRequest

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainDeliverabilityCampaignResponse

### DomainDeliverabilityCampaign
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DomainDeliverabilityCampaign'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.OverallVolume'>
- **Required**: Yes

### DailyVolumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DailyVolume]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetEmailIdentityPoliciesRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailIdentityPoliciesResponse

### Policies
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DkimAttributes'>
- **Required**: Yes

### MailFromAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MailFromAttributes'>
- **Required**: Yes

### Policies
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationStatus
- **Type**: typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']
- **Required**: Yes

### VerificationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.VerificationInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailTemplateResponse

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EmailTemplateContent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetExportJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportDestination'>
- **Required**: Yes

### ExportDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportDataSourceOutput'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.FailureInfo'>
- **Required**: Yes

### Statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ImportDestination'>
- **Required**: Yes

### ImportDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ImportDataSource'>
- **Required**: Yes

### FailureInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.FailureInfo'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetMessageInsightsRequest

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMessageInsightsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageTag]
- **Required**: Yes

### Insights
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EmailInsights]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetMultiRegionEndpointRequest

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionEndpointResponse

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Route]
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetSuppressedDestinationRequest

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# GetSuppressedDestinationResponse

### SuppressedDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SuppressedDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# GuardianAttributes

### OptimizedSharedDelivery
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GuardianOptions

### OptimizedSharedDelivery
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# IdentityInfo

### IdentityType
- **Type**: typing.Optional[typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'MANAGED_DOMAIN']]

### IdentityName
- **Type**: typing.Optional[str]

### SendingEnabled
- **Type**: typing.Optional[bool]

### VerificationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']]


# ImportDataSource

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# ImportDestination

### SuppressionListDestination
- **Type**: <class 'NoneType'>

### ContactListDestination
- **Type**: <class 'NoneType'>


# ImportJobSummary

### JobId
- **Type**: typing.Optional[str]

### ImportDestination
- **Type**: <class 'NoneType'>

### JobStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'FAILED', 'PROCESSING']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ProcessedRecordsCount
- **Type**: typing.Optional[int]

### FailedRecordsCount
- **Type**: typing.Optional[int]


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


# InsightsEvent

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['BOUNCE', 'CLICK', 'COMPLAINT', 'DELIVERY', 'DELIVERY_DELAY', 'OPEN', 'REJECT', 'RENDERING_FAILURE', 'SEND', 'SUBSCRIPTION']]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EventDetails]


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


# ListConfigurationSetsResponse

### ConfigurationSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactListsRequest

### PageSize
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListContactListsResponse

### ContactLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ContactList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactsFilter

### FilteredStatus
- **Type**: typing.Optional[typing.Literal['OPT_IN', 'OPT_OUT']]

### TopicFilter
- **Type**: <class 'NoneType'>


# ListContactsRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ListContactsFilter]

### PageSize
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListContactsResponse

### Contacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Contact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomVerificationEmailTemplatesRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListCustomVerificationEmailTemplatesResponse

### CustomVerificationEmailTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.CustomVerificationEmailTemplateMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDedicatedIpPoolsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDedicatedIpPoolsResponse

### DedicatedIpPools
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeliverabilityTestReportsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListDeliverabilityTestReportsResponse

### DeliverabilityTestReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DeliverabilityTestReport]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DomainDeliverabilityCampaign]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEmailIdentitiesRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListEmailIdentitiesResponse

### EmailIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.IdentityInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEmailTemplatesRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListEmailTemplatesResponse

### TemplatesMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EmailTemplateMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExportJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### ExportSourceType
- **Type**: typing.Optional[typing.Literal['MESSAGE_INSIGHTS', 'METRICS_DATA']]

### JobStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'FAILED', 'PROCESSING']]


# ListExportJobsResponse

### ExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportJobsRequest

### ImportDestinationType
- **Type**: typing.Optional[typing.Literal['CONTACT_LIST', 'SUPPRESSION_LIST']]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListImportJobsResponse

### ImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ImportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagementOptions

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: typing.Optional[str]


# ListMultiRegionEndpointsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListMultiRegionEndpointsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.PaginatorConfig]


# ListMultiRegionEndpointsResponse

### MultiRegionEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MultiRegionEndpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecommendationsRequest

### Filter
- **Type**: typing.Optional[typing.Dict[typing.Literal['IMPACT', 'RESOURCE_ARN', 'STATUS', 'TYPE'], str]]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListRecommendationsResponse

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Recommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSuppressedDestinationsRequest

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'COMPLAINT']]]

### StartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListSuppressedDestinationsResponse

### SuppressedDestinationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SuppressedDestinationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Content'>
- **Required**: Yes

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Body'>
- **Required**: Yes

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageHeader]]


# MessageHeader

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# MessageInsightsDataSource

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Include
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageInsightsFilters]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageInsightsFilters]

### MaxResults
- **Type**: typing.Optional[int]


# MessageInsightsDataSourceOutput

### StartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Include
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageInsightsFiltersOutput]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageInsightsFiltersOutput]

### MaxResults
- **Type**: typing.Optional[int]


# MessageInsightsFilters

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


# MessageInsightsFiltersOutput

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


# MessageTag

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# MetricDataError

### Id
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'INTERNAL_FAILURE']]

### Message
- **Type**: typing.Optional[str]


# MetricDataResult

### Id
- **Type**: typing.Optional[str]

### Timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### Values
- **Type**: typing.Optional[typing.List[int]]


# MetricsDataSource

### Dimensions
- **Type**: typing.Dict[typing.Literal['CONFIGURATION_SET', 'EMAIL_IDENTITY', 'ISP'], typing.List[str]]
- **Required**: Yes

### Namespace
- **Type**: typing.Literal['VDM']
- **Required**: Yes

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportMetric]
- **Required**: Yes

### StartDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# MetricsDataSourceOutput

### Dimensions
- **Type**: typing.Dict[typing.Literal['CONFIGURATION_SET', 'EMAIL_IDENTITY', 'ISP'], typing.List[str]]
- **Required**: Yes

### Namespace
- **Type**: typing.Literal['VDM']
- **Required**: Yes

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ExportMetric]
- **Required**: Yes

### StartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# MultiRegionEndpoint

### EndpointName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY']]

### EndpointId
- **Type**: typing.Optional[str]

### Regions
- **Type**: typing.Optional[typing.List[str]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# OverallVolume

### VolumeStatistics
- **Type**: <class 'NoneType'>

### ReadRatePercent
- **Type**: typing.Optional[float]

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DomainIspPlacement]]


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


# PutAccountDetailsRequest

### MailType
- **Type**: typing.Literal['MARKETING', 'TRANSACTIONAL']
- **Required**: Yes

### WebsiteURL
- **Type**: <class 'str'>
- **Required**: Yes

### ContactLanguage
- **Type**: typing.Optional[typing.Literal['EN', 'JA']]

### UseCaseDescription
- **Type**: typing.Optional[str]

### AdditionalContactEmailAddresses
- **Type**: typing.Optional[typing.List[str]]

### ProductionAccessEnabled
- **Type**: typing.Optional[bool]


# PutAccountSendingAttributesRequest

### SendingEnabled
- **Type**: typing.Optional[bool]


# PutAccountSuppressionAttributesRequest

### SuppressedReasons
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'COMPLAINT']]]


# PutAccountVdmAttributesRequest

### VdmAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.VdmAttributes'>
- **Required**: Yes


# PutConfigurationSetArchivingOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveArn
- **Type**: typing.Optional[str]


# PutConfigurationSetDeliveryOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE']]

### SendingPoolName
- **Type**: typing.Optional[str]

### MaxDeliverySeconds
- **Type**: typing.Optional[int]


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


# PutConfigurationSetSuppressionOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SuppressedReasons
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'COMPLAINT']]]


# PutConfigurationSetTrackingOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomRedirectDomain
- **Type**: typing.Optional[str]

### HttpsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE', 'REQUIRE_OPEN_ONLY']]


# PutConfigurationSetVdmOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### VdmOptions
- **Type**: <class 'NoneType'>


# PutDedicatedIpInPoolRequest

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPoolName
- **Type**: <class 'str'>
- **Required**: Yes


# PutDedicatedIpPoolScalingAttributesRequest

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingMode
- **Type**: typing.Literal['MANAGED', 'STANDARD']
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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DomainDeliverabilityTrackingOption, aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DomainDeliverabilityTrackingOptionOutput]]]


# PutEmailIdentityConfigurationSetAttributesRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: typing.Optional[str]


# PutEmailIdentityDkimAttributesRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### SigningEnabled
- **Type**: typing.Optional[bool]


# PutEmailIdentityDkimSigningAttributesRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### SigningAttributesOrigin
- **Type**: typing.Literal['AWS_SES', 'AWS_SES_AF_SOUTH_1', 'AWS_SES_AP_NORTHEAST_1', 'AWS_SES_AP_NORTHEAST_2', 'AWS_SES_AP_NORTHEAST_3', 'AWS_SES_AP_SOUTHEAST_1', 'AWS_SES_AP_SOUTHEAST_2', 'AWS_SES_AP_SOUTHEAST_3', 'AWS_SES_AP_SOUTH_1', 'AWS_SES_CA_CENTRAL_1', 'AWS_SES_EU_CENTRAL_1', 'AWS_SES_EU_NORTH_1', 'AWS_SES_EU_SOUTH_1', 'AWS_SES_EU_WEST_1', 'AWS_SES_EU_WEST_2', 'AWS_SES_EU_WEST_3', 'AWS_SES_IL_CENTRAL_1', 'AWS_SES_ME_SOUTH_1', 'AWS_SES_SA_EAST_1', 'AWS_SES_US_EAST_1', 'AWS_SES_US_EAST_2', 'AWS_SES_US_WEST_1', 'AWS_SES_US_WEST_2', 'EXTERNAL']
- **Required**: Yes

### SigningAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.DkimSigningAttributes]


# PutEmailIdentityDkimSigningAttributesResponse

### DkimStatus
- **Type**: typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCESS', 'TEMPORARY_FAILURE']
- **Required**: Yes

### DkimTokens
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


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


# PutSuppressedDestinationRequest

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Literal['BOUNCE', 'COMPLAINT']
- **Required**: Yes


# RawMessage

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# Recommendation

### ResourceArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['BIMI', 'COMPLAINT', 'DKIM', 'DMARC', 'SPF']]

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


# ReplacementEmailContent

### ReplacementTemplate
- **Type**: <class 'NoneType'>


# ReplacementTemplate

### ReplacementTemplateData
- **Type**: typing.Optional[str]


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


# ReviewDetails

### Status
- **Type**: typing.Optional[typing.Literal['DENIED', 'FAILED', 'GRANTED', 'PENDING']]

### CaseId
- **Type**: typing.Optional[str]


# Route

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# RouteDetails

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# SOARecord

### PrimaryNameServer
- **Type**: typing.Optional[str]

### AdminEmail
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[int]


# SendBulkEmailRequest

### DefaultContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.BulkEmailContent'>
- **Required**: Yes

### BulkEmailEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.BulkEmailEntry]
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[str]

### FromEmailAddressIdentityArn
- **Type**: typing.Optional[str]

### ReplyToAddresses
- **Type**: typing.Optional[typing.List[str]]

### FeedbackForwardingEmailAddress
- **Type**: typing.Optional[str]

### FeedbackForwardingEmailAddressIdentityArn
- **Type**: typing.Optional[str]

### DefaultEmailTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageTag]]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]


# SendBulkEmailResponse

### BulkEmailEntryResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.BulkEmailEntryResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# SendCustomVerificationEmailRequest

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendCustomVerificationEmailResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# SendEmailRequest

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EmailContent'>
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[str]

### FromEmailAddressIdentityArn
- **Type**: typing.Optional[str]

### Destination
- **Type**: <class 'NoneType'>

### ReplyToAddresses
- **Type**: typing.Optional[typing.List[str]]

### FeedbackForwardingEmailAddress
- **Type**: typing.Optional[str]

### FeedbackForwardingEmailAddressIdentityArn
- **Type**: typing.Optional[str]

### EmailTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageTag]]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### ListManagementOptions
- **Type**: <class 'NoneType'>


# SendEmailResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
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


# SuppressedDestination

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.SuppressedDestinationAttributes]


# SuppressedDestinationAttributes

### MessageId
- **Type**: typing.Optional[str]

### FeedbackId
- **Type**: typing.Optional[str]


# SuppressedDestinationSummary

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Literal['BOUNCE', 'COMPLAINT']
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# SuppressionAttributes

### SuppressedReasons
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'COMPLAINT']]]


# SuppressionListDestination

### SuppressionListImportAction
- **Type**: typing.Literal['DELETE', 'PUT']
- **Required**: Yes


# SuppressionOptions

### SuppressedReasons
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'COMPLAINT']]]


# SuppressionOptionsOutput

### SuppressedReasons
- **Type**: typing.Optional[typing.List[typing.Literal['BOUNCE', 'COMPLAINT']]]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Tag]
- **Required**: Yes


# Template

### TemplateName
- **Type**: typing.Optional[str]

### TemplateArn
- **Type**: typing.Optional[str]

### TemplateContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EmailTemplateContent]

### TemplateData
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.MessageHeader]]


# TestRenderEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateData
- **Type**: <class 'str'>
- **Required**: Yes


# TestRenderEmailTemplateResponse

### RenderedTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.ResponseMetadata'>
- **Required**: Yes


# Topic

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


# TopicFilter

### TopicName
- **Type**: typing.Optional[str]

### UseDefaultIfPreferenceUnavailable
- **Type**: typing.Optional[bool]


# TopicPreference

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionStatus
- **Type**: typing.Literal['OPT_IN', 'OPT_OUT']
- **Required**: Yes


# TrackingOptions

### CustomRedirectDomain
- **Type**: <class 'str'>
- **Required**: Yes

### HttpsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE', 'REQUIRE_OPEN_ONLY']]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EventDestinationDefinition'>
- **Required**: Yes


# UpdateContactListRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.Topic]]

### Description
- **Type**: typing.Optional[str]


# UpdateContactRequest

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### TopicPreferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2.sesv2_classes.TopicPreference]]

### UnsubscribeAll
- **Type**: typing.Optional[bool]

### AttributesData
- **Type**: typing.Optional[str]


# UpdateCustomVerificationEmailTemplateRequest

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


# UpdateEmailIdentityPolicyRequest

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2.sesv2_classes.EmailTemplateContent'>
- **Required**: Yes


# VdmAttributes

### VdmEnabled
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DashboardAttributes
- **Type**: <class 'NoneType'>

### GuardianAttributes
- **Type**: <class 'NoneType'>


# VdmOptions

### DashboardOptions
- **Type**: <class 'NoneType'>

### GuardianOptions
- **Type**: <class 'NoneType'>


# VerificationInfo

### LastCheckedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ErrorType
- **Type**: typing.Optional[typing.Literal['DNS_SERVER_ERROR', 'HOST_NOT_FOUND', 'INVALID_VALUE', 'REPLICATION_ACCESS_DENIED', 'REPLICATION_PRIMARY_BYO_DKIM_NOT_SUPPORTED', 'REPLICATION_PRIMARY_INVALID_REGION', 'REPLICATION_PRIMARY_NOT_FOUND', 'REPLICATION_REPLICA_AS_PRIMARY_NOT_SUPPORTED', 'SERVICE_ERROR', 'TYPE_NOT_FOUND']]

### SOARecord
- **Type**: <class 'NoneType'>


# VolumeStatistics

### InboxRawCount
- **Type**: typing.Optional[int]

### SpamRawCount
- **Type**: typing.Optional[int]

### ProjectedInbox
- **Type**: typing.Optional[int]

### ProjectedSpam
- **Type**: typing.Optional[int]


