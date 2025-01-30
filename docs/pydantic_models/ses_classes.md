# ses_classes

# AddHeaderActionTypeDef

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### HeaderValue
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BodyTypeDef

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.ContentTypeDef]

### Html
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.ContentTypeDef]


# BounceActionTypeDef

### SmtpReplyCode
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Sender
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]

### StatusCode
- **Type**: typing.Optional[str]


# BouncedRecipientInfoTypeDef

### Recipient
- **Type**: <class 'str'>
- **Required**: Yes

### RecipientArn
- **Type**: typing.Optional[str]

### BounceType
- **Type**: typing.Optional[typing.Literal['ContentRejected', 'DoesNotExist', 'ExceededQuota', 'MessageTooLarge', 'TemporaryFailure', 'Undefined']]

### RecipientDsnFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.RecipientDsnFieldsTypeDef]


# BulkEmailDestinationStatusTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['AccountDailyQuotaExceeded', 'AccountSendingPaused', 'AccountSuspended', 'AccountThrottled', 'ConfigurationSetDoesNotExist', 'ConfigurationSetSendingPaused', 'Failed', 'InvalidParameterValue', 'InvalidSendingPoolName', 'MailFromDomainNotVerified', 'MessageRejected', 'Success', 'TemplateDoesNotExist', 'TransientFailure']]

### Error
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]


# BulkEmailDestinationTypeDef

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.DestinationTypeDef'>
- **Required**: Yes

### ReplacementTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.MessageTagTypeDef]]

### ReplacementTemplateData
- **Type**: typing.Optional[str]


# CloneReceiptRuleSetRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginalRuleSetName
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchDestinationOutputTypeDef

### DimensionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.CloudWatchDimensionConfigurationTypeDef]
- **Required**: Yes


# CloudWatchDestinationTypeDef

### DimensionConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.CloudWatchDimensionConfigurationTypeDef]
- **Required**: Yes


# CloudWatchDimensionConfigurationTypeDef

### DimensionName
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueSource
- **Type**: typing.Literal['emailHeader', 'linkTag', 'messageTag']
- **Required**: Yes

### DefaultDimensionValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationSetTypeDef

### Name
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

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.EventDestinationTypeDef'>
- **Required**: Yes


# CreateConfigurationSetRequestRequestTypeDef

### ConfigurationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ConfigurationSetTypeDef'>
- **Required**: Yes


# CreateConfigurationSetTrackingOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.TrackingOptionsTypeDef'>
- **Required**: Yes


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


# CreateReceiptFilterRequestRequestTypeDef

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ReceiptFilterTypeDef'>
- **Required**: Yes


# CreateReceiptRuleRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ReceiptRuleTypeDef'>
- **Required**: Yes

### After
- **Type**: typing.Optional[str]


# CreateReceiptRuleSetRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTemplateRequestRequestTypeDef

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.TemplateTypeDef'>
- **Required**: Yes


# CustomVerificationEmailTemplateTypeDef

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


# DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomVerificationEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityPolicyRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReceiptFilterRequestRequestTypeDef

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReceiptRuleRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReceiptRuleSetRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVerifiedEmailAddressRequestRequestTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# DeliveryOptionsTypeDef

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['Optional', 'Require']]


# DescribeActiveReceiptRuleSetResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ReceiptRuleSetMetadataTypeDef'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.ReceiptRuleOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConfigurationSetRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetAttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['deliveryOptions', 'eventDestinations', 'reputationOptions', 'trackingOptions']]]


# DescribeConfigurationSetResponseTypeDef

### ConfigurationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ConfigurationSetTypeDef'>
- **Required**: Yes

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.EventDestinationOutputTypeDef]
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.TrackingOptionsTypeDef'>
- **Required**: Yes

### DeliveryOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.DeliveryOptionsTypeDef'>
- **Required**: Yes

### ReputationOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ReputationOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReceiptRuleRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReceiptRuleResponseTypeDef

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ReceiptRuleOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReceiptRuleSetRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReceiptRuleSetResponseTypeDef

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ReceiptRuleSetMetadataTypeDef'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.ReceiptRuleOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

### ToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### CcAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### BccAddresses
- **Type**: typing.Optional[typing.Sequence[str]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventDestinationOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.List[typing.Literal['bounce', 'click', 'complaint', 'delivery', 'open', 'reject', 'renderingFailure', 'send']]
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.KinesisFirehoseDestinationTypeDef]

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.CloudWatchDestinationOutputTypeDef]

### SNSDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.SNSDestinationTypeDef]


# EventDestinationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.Sequence[typing.Literal['bounce', 'click', 'complaint', 'delivery', 'open', 'reject', 'renderingFailure', 'send']]
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.KinesisFirehoseDestinationTypeDef]

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.CloudWatchDestinationTypeDef]

### SNSDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.SNSDestinationTypeDef]


# ExtensionFieldTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountSendingEnabledResponseTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityDkimAttributesRequestRequestTypeDef

### Identities
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetIdentityDkimAttributesResponseTypeDef

### DkimAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ses_classes.IdentityDkimAttributesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityMailFromDomainAttributesRequestRequestTypeDef

### Identities
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetIdentityMailFromDomainAttributesResponseTypeDef

### MailFromDomainAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ses_classes.IdentityMailFromDomainAttributesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityNotificationAttributesRequestRequestTypeDef

### Identities
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetIdentityNotificationAttributesResponseTypeDef

### NotificationAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ses_classes.IdentityNotificationAttributesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityPoliciesRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetIdentityPoliciesResponseTypeDef

### Policies
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityVerificationAttributesRequestIdentityExistsWaitTypeDef

### Identities
- **Type**: typing.Sequence[str]
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.WaiterConfigTypeDef]


# GetIdentityVerificationAttributesRequestRequestTypeDef

### Identities
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetIdentityVerificationAttributesResponseTypeDef

### VerificationAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ses_classes.IdentityVerificationAttributesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSendQuotaResponseTypeDef

### Max24HourSend
- **Type**: <class 'float'>
- **Required**: Yes

### MaxSendRate
- **Type**: <class 'float'>
- **Required**: Yes

### SentLast24Hours
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSendStatisticsResponseTypeDef

### SendDataPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.SendDataPointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateResponseTypeDef

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.TemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityDkimAttributesTypeDef

### DkimEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### DkimVerificationStatus
- **Type**: typing.Literal['Failed', 'NotStarted', 'Pending', 'Success', 'TemporaryFailure']
- **Required**: Yes

### DkimTokens
- **Type**: typing.Optional[typing.List[str]]


# IdentityMailFromDomainAttributesTypeDef

### MailFromDomain
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomainStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Success', 'TemporaryFailure']
- **Required**: Yes

### BehaviorOnMXFailure
- **Type**: typing.Literal['RejectMessage', 'UseDefaultValue']
- **Required**: Yes


# IdentityNotificationAttributesTypeDef

### BounceTopic
- **Type**: <class 'str'>
- **Required**: Yes

### ComplaintTopic
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryTopic
- **Type**: <class 'str'>
- **Required**: Yes

### ForwardingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### HeadersInBounceNotificationsEnabled
- **Type**: typing.Optional[bool]

### HeadersInComplaintNotificationsEnabled
- **Type**: typing.Optional[bool]

### HeadersInDeliveryNotificationsEnabled
- **Type**: typing.Optional[bool]


# IdentityVerificationAttributesTypeDef

### VerificationStatus
- **Type**: typing.Literal['Failed', 'NotStarted', 'Pending', 'Success', 'TemporaryFailure']
- **Required**: Yes

### VerificationToken
- **Type**: typing.Optional[str]


# KinesisFirehoseDestinationTypeDef

### IAMRoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamARN
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaActionTypeDef

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]

### InvocationType
- **Type**: typing.Optional[typing.Literal['Event', 'RequestResponse']]


# ListConfigurationSetsRequestListConfigurationSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.PaginatorConfigTypeDef]


# ListConfigurationSetsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListConfigurationSetsResponseTypeDef

### ConfigurationSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.ConfigurationSetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomVerificationEmailTemplatesRequestListCustomVerificationEmailTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.PaginatorConfigTypeDef]


# ListCustomVerificationEmailTemplatesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCustomVerificationEmailTemplatesResponseTypeDef

### CustomVerificationEmailTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.CustomVerificationEmailTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentitiesRequestListIdentitiesPaginateTypeDef

### IdentityType
- **Type**: typing.Optional[typing.Literal['Domain', 'EmailAddress']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.PaginatorConfigTypeDef]


# ListIdentitiesRequestRequestTypeDef

### IdentityType
- **Type**: typing.Optional[typing.Literal['Domain', 'EmailAddress']]

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListIdentitiesResponseTypeDef

### Identities
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPoliciesRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes


# ListIdentityPoliciesResponseTypeDef

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReceiptFiltersResponseTypeDef

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.ReceiptFilterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReceiptRuleSetsRequestListReceiptRuleSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.PaginatorConfigTypeDef]


# ListReceiptRuleSetsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListReceiptRuleSetsResponseTypeDef

### RuleSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.ReceiptRuleSetMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTemplatesRequestListTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.PaginatorConfigTypeDef]


# ListTemplatesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListTemplatesResponseTypeDef

### TemplatesMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.TemplateMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVerifiedEmailAddressesResponseTypeDef

### VerifiedEmailAddresses
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MessageDsnTypeDef

### ReportingMta
- **Type**: <class 'str'>
- **Required**: Yes

### ArrivalDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ExtensionFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.ExtensionFieldTypeDef]]


# MessageTagTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# MessageTypeDef

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ContentTypeDef'>
- **Required**: Yes

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.BodyTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutConfigurationSetDeliveryOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.DeliveryOptionsTypeDef]


# PutIdentityPolicyRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# RawMessageTypeDef

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# ReceiptActionTypeDef

### S3Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.S3ActionTypeDef]

### BounceAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.BounceActionTypeDef]

### WorkmailAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.WorkmailActionTypeDef]

### LambdaAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.LambdaActionTypeDef]

### StopAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.StopActionTypeDef]

### AddHeaderAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.AddHeaderActionTypeDef]

### SNSAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.SNSActionTypeDef]


# ReceiptFilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IpFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ReceiptIpFilterTypeDef'>
- **Required**: Yes


# ReceiptIpFilterTypeDef

### Policy
- **Type**: typing.Literal['Allow', 'Block']
- **Required**: Yes

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes


# ReceiptRuleOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['Optional', 'Require']]

### Recipients
- **Type**: typing.Optional[typing.List[str]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses_classes.ReceiptActionTypeDef]]

### ScanEnabled
- **Type**: typing.Optional[bool]


# ReceiptRuleSetMetadataTypeDef

### Name
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ReceiptRuleTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['Optional', 'Require']]

### Recipients
- **Type**: typing.Optional[typing.Sequence[str]]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.ReceiptActionTypeDef]]

### ScanEnabled
- **Type**: typing.Optional[bool]


# RecipientDsnFieldsTypeDef

### Action
- **Type**: typing.Literal['delayed', 'delivered', 'expanded', 'failed', 'relayed']
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### FinalRecipient
- **Type**: typing.Optional[str]

### RemoteMta
- **Type**: typing.Optional[str]

### DiagnosticCode
- **Type**: typing.Optional[str]

### LastAttemptDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ExtensionFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.ExtensionFieldTypeDef]]


# ReorderReceiptRuleSetRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ReputationOptionsTypeDef

### SendingEnabled
- **Type**: typing.Optional[bool]

### ReputationMetricsEnabled
- **Type**: typing.Optional[bool]

### LastFreshStart
- **Type**: typing.Optional[datetime.datetime]


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


# S3ActionTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]

### ObjectKeyPrefix
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# SNSActionTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Encoding
- **Type**: typing.Optional[typing.Literal['Base64', 'UTF-8']]


# SNSDestinationTypeDef

### TopicARN
- **Type**: <class 'str'>
- **Required**: Yes


# SendBounceRequestRequestTypeDef

### OriginalMessageId
- **Type**: <class 'str'>
- **Required**: Yes

### BounceSender
- **Type**: <class 'str'>
- **Required**: Yes

### BouncedRecipientInfoList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.BouncedRecipientInfoTypeDef]
- **Required**: Yes

### Explanation
- **Type**: typing.Optional[str]

### MessageDsn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses_classes.MessageDsnTypeDef]

### BounceSenderArn
- **Type**: typing.Optional[str]


# SendBounceResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendBulkTemplatedEmailRequestRequestTypeDef

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Template
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.BulkEmailDestinationTypeDef]
- **Required**: Yes

### SourceArn
- **Type**: typing.Optional[str]

### ReplyToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### ReturnPath
- **Type**: typing.Optional[str]

### ReturnPathArn
- **Type**: typing.Optional[str]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### DefaultTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.MessageTagTypeDef]]

### TemplateArn
- **Type**: typing.Optional[str]

### DefaultTemplateData
- **Type**: typing.Optional[str]


# SendBulkTemplatedEmailResponseTypeDef

### Status
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses_classes.BulkEmailDestinationStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendDataPointTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### DeliveryAttempts
- **Type**: typing.Optional[int]

### Bounces
- **Type**: typing.Optional[int]

### Complaints
- **Type**: typing.Optional[int]

### Rejects
- **Type**: typing.Optional[int]


# SendEmailRequestRequestTypeDef

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.DestinationTypeDef'>
- **Required**: Yes

### Message
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.MessageTypeDef'>
- **Required**: Yes

### ReplyToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### ReturnPath
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### ReturnPathArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.MessageTagTypeDef]]

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendEmailResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendRawEmailRequestRequestTypeDef

### RawMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.RawMessageTypeDef'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Destinations
- **Type**: typing.Optional[typing.Sequence[str]]

### FromArn
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### ReturnPathArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.MessageTagTypeDef]]

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendRawEmailResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendTemplatedEmailRequestRequestTypeDef

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.DestinationTypeDef'>
- **Required**: Yes

### Template
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateData
- **Type**: <class 'str'>
- **Required**: Yes

### ReplyToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### ReturnPath
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### ReturnPathArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ses_classes.MessageTagTypeDef]]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### TemplateArn
- **Type**: typing.Optional[str]


# SendTemplatedEmailResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetActiveReceiptRuleSetRequestRequestTypeDef

### RuleSetName
- **Type**: typing.Optional[str]


# SetIdentityDkimEnabledRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### DkimEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### ForwardingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationType
- **Type**: typing.Literal['Bounce', 'Complaint', 'Delivery']
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SetIdentityMailFromDomainRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomain
- **Type**: typing.Optional[str]

### BehaviorOnMXFailure
- **Type**: typing.Optional[typing.Literal['RejectMessage', 'UseDefaultValue']]


# SetIdentityNotificationTopicRequestRequestTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationType
- **Type**: typing.Literal['Bounce', 'Complaint', 'Delivery']
- **Required**: Yes

### SnsTopic
- **Type**: typing.Optional[str]


# SetReceiptRulePositionRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### After
- **Type**: typing.Optional[str]


# StopActionTypeDef

### Scope
- **Type**: typing.Literal['RuleSet']
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]


# TemplateMetadataTypeDef

### Name
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# TemplateTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### SubjectPart
- **Type**: typing.Optional[str]

### TextPart
- **Type**: typing.Optional[str]

### HtmlPart
- **Type**: typing.Optional[str]


# TestRenderTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateData
- **Type**: <class 'str'>
- **Required**: Yes


# TestRenderTemplateResponseTypeDef

### RenderedTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TrackingOptionsTypeDef

### CustomRedirectDomain
- **Type**: typing.Optional[str]


# UpdateAccountSendingEnabledRequestRequestTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# UpdateConfigurationSetEventDestinationRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.EventDestinationTypeDef'>
- **Required**: Yes


# UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateConfigurationSetSendingEnabledRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.TrackingOptionsTypeDef'>
- **Required**: Yes


# UpdateCustomVerificationEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[str]

### TemplateSubject
- **Type**: typing.Optional[str]

### TemplateContent
- **Type**: typing.Optional[str]

### SuccessRedirectionURL
- **Type**: typing.Optional[str]

### FailureRedirectionURL
- **Type**: typing.Optional[str]


# UpdateReceiptRuleRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ReceiptRuleTypeDef'>
- **Required**: Yes


# UpdateTemplateRequestRequestTypeDef

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.TemplateTypeDef'>
- **Required**: Yes


# VerifyDomainDkimRequestRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyDomainDkimResponseTypeDef

### DkimTokens
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifyDomainIdentityRequestRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyDomainIdentityResponseTypeDef

### VerificationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifyEmailAddressRequestRequestTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyEmailIdentityRequestRequestTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkmailActionTypeDef

### OrganizationArn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]


