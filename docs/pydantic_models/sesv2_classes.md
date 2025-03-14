# Sesv2 Classes

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


# ArchivingOptionsTypeDef

### ArchiveArn
- **Type**: typing.Optional[str]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
- **Required**: Yes

### EndDate
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CONFIGURATION_SET', 'EMAIL_IDENTITY', 'ISP'], str]]


# BatchGetMetricDataRequestTypeDef

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


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BodyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# CancelExportJobRequestTypeDef

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


# CloudWatchDestinationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# CreateConfigurationSetEventDestinationRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EventDestinationDefinitionTypeDef'>
- **Required**: Yes


# CreateConfigurationSetRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TrackingOptionsTypeDef]

### DeliveryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.DeliveryOptionsTypeDef]

### ReputationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ReputationOptionsUnionTypeDef]

### SendingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SendingOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]

### SuppressionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.SuppressionOptionsUnionTypeDef]

### VdmOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.VdmOptionsTypeDef]

### ArchivingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.ArchivingOptionsTypeDef]


# CreateContactListRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TopicTypeDef]]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]


# CreateContactRequestTypeDef

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


# CreateCustomVerificationEmailTemplateRequestTypeDef

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


# CreateDedicatedIpPoolRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]

### ScalingMode
- **Type**: typing.Optional[typing.Literal['MANAGED', 'STANDARD']]


# CreateDeliverabilityTestReportRequestTypeDef

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


# CreateEmailIdentityPolicyRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# CreateEmailIdentityRequestTypeDef

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


# CreateEmailTemplateRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateContent
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EmailTemplateContentTypeDef'>
- **Required**: Yes


# CreateExportJobRequestTypeDef

### ExportDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ExportDataSourceUnionTypeDef'>
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


# CreateImportJobRequestTypeDef

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


# CreateMultiRegionEndpointRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.DetailsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TagTypeDef]]


# CreateMultiRegionEndpointResponseTypeDef

### Status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY']
- **Required**: Yes

### EndpointId
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


# DeleteConfigurationSetEventDestinationRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationSetRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactListRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomVerificationEmailTemplateRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDedicatedIpPoolRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailIdentityPolicyRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailIdentityRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailTemplateRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiRegionEndpointRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiRegionEndpointResponseTypeDef

### Status
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'READY']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSuppressedDestinationRequestTypeDef

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

### MaxDeliverySeconds
- **Type**: typing.Optional[int]


# DestinationTypeDef

### ToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### CcAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### BccAddresses
- **Type**: typing.Optional[typing.Sequence[str]]


# DetailsTypeDef

### RoutesDetails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.RouteDetailsTypeDef]
- **Required**: Yes


# DkimAttributesTypeDef

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


# DkimSigningAttributesTypeDef

### DomainSigningSelector
- **Type**: typing.Optional[str]

### DomainSigningPrivateKey
- **Type**: typing.Optional[str]

### NextSigningKeyLength
- **Type**: typing.Optional[typing.Literal['RSA_1024_BIT', 'RSA_2048_BIT']]

### DomainSigningAttributesOrigin
- **Type**: typing.Optional[typing.Literal['AWS_SES', 'AWS_SES_AF_SOUTH_1', 'AWS_SES_AP_NORTHEAST_1', 'AWS_SES_AP_NORTHEAST_2', 'AWS_SES_AP_NORTHEAST_3', 'AWS_SES_AP_SOUTHEAST_1', 'AWS_SES_AP_SOUTHEAST_2', 'AWS_SES_AP_SOUTHEAST_3', 'AWS_SES_AP_SOUTH_1', 'AWS_SES_CA_CENTRAL_1', 'AWS_SES_EU_CENTRAL_1', 'AWS_SES_EU_NORTH_1', 'AWS_SES_EU_SOUTH_1', 'AWS_SES_EU_WEST_1', 'AWS_SES_EU_WEST_2', 'AWS_SES_EU_WEST_3', 'AWS_SES_IL_CENTRAL_1', 'AWS_SES_ME_SOUTH_1', 'AWS_SES_SA_EAST_1', 'AWS_SES_US_EAST_1', 'AWS_SES_US_EAST_2', 'AWS_SES_US_WEST_1', 'AWS_SES_US_WEST_2', 'EXTERNAL']]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef]

### InboxPlacementTrackingOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.InboxPlacementTrackingOptionUnionTypeDef]


# DomainDeliverabilityTrackingOptionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.CloudWatchDestinationUnionTypeDef]

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


# ExportDataSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# GetBlacklistReportsRequestTypeDef

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


# GetConfigurationSetEventDestinationsRequestTypeDef

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


# GetConfigurationSetRequestTypeDef

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

### ArchivingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ArchivingOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContactListRequestTypeDef

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


# GetContactRequestTypeDef

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


# GetCustomVerificationEmailTemplateRequestTypeDef

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


# GetDedicatedIpPoolRequestTypeDef

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


# GetDedicatedIpRequestTypeDef

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


# GetDedicatedIpsRequestTypeDef

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


# GetDeliverabilityTestReportRequestTypeDef

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


# GetDomainDeliverabilityCampaignRequestTypeDef

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


# GetDomainStatisticsReportRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### StartDate
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
- **Required**: Yes

### EndDate
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
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


# GetEmailIdentityPoliciesRequestTypeDef

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


# GetEmailIdentityRequestTypeDef

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


# GetEmailTemplateRequestTypeDef

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


# GetExportJobRequestTypeDef

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


# GetImportJobRequestTypeDef

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


# GetMessageInsightsRequestTypeDef

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


# GetMultiRegionEndpointRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionEndpointResponseTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.RouteTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSuppressedDestinationRequestTypeDef

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


# InboxPlacementTrackingOptionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InsightsEventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ListConfigurationSetsRequestTypeDef

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


# ListContactListsRequestTypeDef

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


# ListContactsRequestTypeDef

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


# ListCustomVerificationEmailTemplatesRequestTypeDef

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


# ListDedicatedIpPoolsRequestTypeDef

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


# ListDeliverabilityTestReportsRequestTypeDef

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


# ListDomainDeliverabilityCampaignsRequestTypeDef

### StartDate
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
- **Required**: Yes

### EndDate
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
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


# ListEmailIdentitiesRequestTypeDef

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


# ListEmailTemplatesRequestTypeDef

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


# ListExportJobsRequestTypeDef

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


# ListImportJobsRequestTypeDef

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


# ListMultiRegionEndpointsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.PaginatorConfigTypeDef]


# ListMultiRegionEndpointsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListMultiRegionEndpointsResponseTypeDef

### MultiRegionEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.MultiRegionEndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecommendationsRequestTypeDef

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


# ListSuppressedDestinationsRequestTypeDef

### Reasons
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'COMPLAINT']]]

### StartDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef]

### EndDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef]

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


# ListTagsForResourceRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
- **Required**: Yes

### EndDate
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
- **Required**: Yes

### EndDate
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef'>
- **Required**: Yes


# MultiRegionEndpointTypeDef

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


# OverallVolumeTypeDef

### VolumeStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.VolumeStatisticsTypeDef]

### ReadRatePercent
- **Type**: typing.Optional[float]

### DomainIspPlacements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sesv2_classes.DomainIspPlacementTypeDef]]


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


# PutAccountDedicatedIpWarmupAttributesRequestTypeDef

### AutoWarmupEnabled
- **Type**: typing.Optional[bool]


# PutAccountDetailsRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### ProductionAccessEnabled
- **Type**: typing.Optional[bool]


# PutAccountSendingAttributesRequestTypeDef

### SendingEnabled
- **Type**: typing.Optional[bool]


# PutAccountSuppressionAttributesRequestTypeDef

### SuppressedReasons
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'COMPLAINT']]]


# PutAccountVdmAttributesRequestTypeDef

### VdmAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.VdmAttributesTypeDef'>
- **Required**: Yes


# PutConfigurationSetArchivingOptionsRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveArn
- **Type**: typing.Optional[str]


# PutConfigurationSetDeliveryOptionsRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE']]

### SendingPoolName
- **Type**: typing.Optional[str]

### MaxDeliverySeconds
- **Type**: typing.Optional[int]


# PutConfigurationSetReputationOptionsRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]


# PutConfigurationSetSendingOptionsRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SendingEnabled
- **Type**: typing.Optional[bool]


# PutConfigurationSetSuppressionOptionsRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SuppressedReasons
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOUNCE', 'COMPLAINT']]]


# PutConfigurationSetTrackingOptionsRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomRedirectDomain
- **Type**: typing.Optional[str]

### HttpsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE', 'REQUIRE_OPEN_ONLY']]


# PutConfigurationSetVdmOptionsRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### VdmOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.VdmOptionsTypeDef]


# PutDedicatedIpInPoolRequestTypeDef

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPoolName
- **Type**: <class 'str'>
- **Required**: Yes


# PutDedicatedIpPoolScalingAttributesRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingMode
- **Type**: typing.Literal['MANAGED', 'STANDARD']
- **Required**: Yes


# PutDedicatedIpWarmupAttributesRequestTypeDef

### Ip
- **Type**: <class 'str'>
- **Required**: Yes

### WarmupPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# PutDeliverabilityDashboardOptionRequestTypeDef

### DashboardEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SubscribedDomains
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.DomainDeliverabilityTrackingOptionUnionTypeDef]]


# PutEmailIdentityConfigurationSetAttributesRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: typing.Optional[str]


# PutEmailIdentityDkimAttributesRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### SigningEnabled
- **Type**: typing.Optional[bool]


# PutEmailIdentityDkimSigningAttributesRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### SigningAttributesOrigin
- **Type**: typing.Literal['AWS_SES', 'AWS_SES_AF_SOUTH_1', 'AWS_SES_AP_NORTHEAST_1', 'AWS_SES_AP_NORTHEAST_2', 'AWS_SES_AP_NORTHEAST_3', 'AWS_SES_AP_SOUTHEAST_1', 'AWS_SES_AP_SOUTHEAST_2', 'AWS_SES_AP_SOUTHEAST_3', 'AWS_SES_AP_SOUTH_1', 'AWS_SES_CA_CENTRAL_1', 'AWS_SES_EU_CENTRAL_1', 'AWS_SES_EU_NORTH_1', 'AWS_SES_EU_SOUTH_1', 'AWS_SES_EU_WEST_1', 'AWS_SES_EU_WEST_2', 'AWS_SES_EU_WEST_3', 'AWS_SES_IL_CENTRAL_1', 'AWS_SES_ME_SOUTH_1', 'AWS_SES_SA_EAST_1', 'AWS_SES_US_EAST_1', 'AWS_SES_US_EAST_2', 'AWS_SES_US_WEST_1', 'AWS_SES_US_WEST_2', 'EXTERNAL']
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


# PutEmailIdentityFeedbackAttributesRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### EmailForwardingEnabled
- **Type**: typing.Optional[bool]


# PutEmailIdentityMailFromAttributesRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomain
- **Type**: typing.Optional[str]

### BehaviorOnMxFailure
- **Type**: typing.Optional[typing.Literal['REJECT_MESSAGE', 'USE_DEFAULT_VALUE']]


# PutSuppressedDestinationRequestTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Literal['BOUNCE', 'COMPLAINT']
- **Required**: Yes


# RawMessageTypeDef

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.BlobTypeDef'>
- **Required**: Yes


# RecommendationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.TimestampTypeDef]


# ReputationOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RouteDetailsTypeDef

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# RouteTypeDef

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# SOARecordTypeDef

### PrimaryNameServer
- **Type**: typing.Optional[str]

### AdminEmail
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[int]


# SendBulkEmailRequestTypeDef

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

### EndpointId
- **Type**: typing.Optional[str]


# SendBulkEmailResponseTypeDef

### BulkEmailEntryResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.sesv2_classes.BulkEmailEntryResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendCustomVerificationEmailRequestTypeDef

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


# SendEmailRequestTypeDef

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

### EndpointId
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


# SuppressionOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

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

### TemplateContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sesv2_classes.EmailTemplateContentTypeDef]

### TemplateData
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.MessageHeaderTypeDef]]


# TestRenderEmailTemplateRequestTypeDef

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


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### HttpsPolicy
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRE', 'REQUIRE_OPEN_ONLY']]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConfigurationSetEventDestinationRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.sesv2_classes.EventDestinationDefinitionTypeDef'>
- **Required**: Yes


# UpdateContactListRequestTypeDef

### ContactListName
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sesv2_classes.TopicTypeDef]]

### Description
- **Type**: typing.Optional[str]


# UpdateContactRequestTypeDef

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


# UpdateCustomVerificationEmailTemplateRequestTypeDef

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


# UpdateEmailIdentityPolicyRequestTypeDef

### EmailIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateEmailTemplateRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['DNS_SERVER_ERROR', 'HOST_NOT_FOUND', 'INVALID_VALUE', 'REPLICATION_ACCESS_DENIED', 'REPLICATION_PRIMARY_BYO_DKIM_NOT_SUPPORTED', 'REPLICATION_PRIMARY_INVALID_REGION', 'REPLICATION_PRIMARY_NOT_FOUND', 'REPLICATION_REPLICA_AS_PRIMARY_NOT_SUPPORTED', 'SERVICE_ERROR', 'TYPE_NOT_FOUND']]

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


