# Ses Classes

# AddHeaderAction

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### HeaderValue
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Body

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses.ses_classes.Content]

### Html
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses.ses_classes.Content]


# BounceAction

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


# BouncedRecipientInfo

### Recipient
- **Type**: <class 'str'>
- **Required**: Yes

### RecipientArn
- **Type**: typing.Optional[str]

### BounceType
- **Type**: typing.Optional[typing.Literal['ContentRejected', 'DoesNotExist', 'ExceededQuota', 'MessageTooLarge', 'TemporaryFailure', 'Undefined']]

### RecipientDsnFields
- **Type**: <class 'NoneType'>


# BulkEmailDestination

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Destination'>
- **Required**: Yes

### ReplacementTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.MessageTag]]

### ReplacementTemplateData
- **Type**: typing.Optional[str]


# BulkEmailDestinationStatus

### Status
- **Type**: typing.Optional[typing.Literal['AccountDailyQuotaExceeded', 'AccountSendingPaused', 'AccountSuspended', 'AccountThrottled', 'ConfigurationSetDoesNotExist', 'ConfigurationSetSendingPaused', 'Failed', 'InvalidParameterValue', 'InvalidSendingPoolName', 'MailFromDomainNotVerified', 'MessageRejected', 'Success', 'TemplateDoesNotExist', 'TransientFailure']]

### Error
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]


# CloneReceiptRuleSetRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginalRuleSetName
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchDestination

### DimensionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.CloudWatchDimensionConfiguration]
- **Required**: Yes


# CloudWatchDestinationOutput

### DimensionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.CloudWatchDimensionConfiguration]
- **Required**: Yes


# CloudWatchDimensionConfiguration

### DimensionName
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueSource
- **Type**: typing.Literal['emailHeader', 'linkTag', 'messageTag']
- **Required**: Yes

### DefaultDimensionValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationSet

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ConnectAction

### InstanceARN
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleARN
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

### EventDestination
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ses.ses_classes.EventDestination, aws_resource_validator.pydantic_models.ses.ses_classes.EventDestinationOutput]
- **Required**: Yes


# CreateConfigurationSetRequest

### ConfigurationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ConfigurationSet'>
- **Required**: Yes


# CreateConfigurationSetTrackingOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.TrackingOptions'>
- **Required**: Yes


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


# CreateReceiptFilterRequest

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptFilter'>
- **Required**: Yes


# CreateReceiptRuleRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Rule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRule, aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRuleOutput]
- **Required**: Yes

### After
- **Type**: typing.Optional[str]


# CreateReceiptRuleSetRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTemplateRequest

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Template'>
- **Required**: Yes


# CustomVerificationEmailTemplate

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


# DeleteConfigurationSetTrackingOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomVerificationEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityPolicyRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReceiptFilterRequest

### FilterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReceiptRuleRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReceiptRuleSetRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVerifiedEmailAddressRequest

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# DeliveryOptions

### TlsPolicy
- **Type**: typing.Optional[typing.Literal['Optional', 'Require']]


# DescribeActiveReceiptRuleSetResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRuleSetMetadata'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRuleOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConfigurationSetRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetAttributeNames
- **Type**: typing.Optional[typing.List[typing.Literal['deliveryOptions', 'eventDestinations', 'reputationOptions', 'trackingOptions']]]


# DescribeConfigurationSetResponse

### ConfigurationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ConfigurationSet'>
- **Required**: Yes

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.EventDestinationOutput]
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.TrackingOptions'>
- **Required**: Yes

### DeliveryOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.DeliveryOptions'>
- **Required**: Yes

### ReputationOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ReputationOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReceiptRuleRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReceiptRuleResponse

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRuleOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReceiptRuleSetRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReceiptRuleSetResponse

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRuleSetMetadata'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRuleOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

### ToAddresses
- **Type**: typing.Optional[typing.List[str]]

### CcAddresses
- **Type**: typing.Optional[typing.List[str]]

### BccAddresses
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# EventDestination

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.List[typing.Literal['bounce', 'click', 'complaint', 'delivery', 'open', 'reject', 'renderingFailure', 'send']]
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### CloudWatchDestination
- **Type**: <class 'NoneType'>

### SNSDestination
- **Type**: <class 'NoneType'>


# EventDestinationOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.List[typing.Literal['bounce', 'click', 'complaint', 'delivery', 'open', 'reject', 'renderingFailure', 'send']]
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### CloudWatchDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses.ses_classes.CloudWatchDestinationOutput]

### SNSDestination
- **Type**: <class 'NoneType'>


# ExtensionField

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountSendingEnabledResponse

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityDkimAttributesRequest

### Identities
- **Type**: typing.List[str]
- **Required**: Yes


# GetIdentityDkimAttributesResponse

### DkimAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ses.ses_classes.IdentityDkimAttributes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityMailFromDomainAttributesRequest

### Identities
- **Type**: typing.List[str]
- **Required**: Yes


# GetIdentityMailFromDomainAttributesResponse

### MailFromDomainAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ses.ses_classes.IdentityMailFromDomainAttributes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityNotificationAttributesRequest

### Identities
- **Type**: typing.List[str]
- **Required**: Yes


# GetIdentityNotificationAttributesResponse

### NotificationAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ses.ses_classes.IdentityNotificationAttributes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityPoliciesRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes


# GetIdentityPoliciesResponse

### Policies
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityVerificationAttributesRequest

### Identities
- **Type**: typing.List[str]
- **Required**: Yes


# GetIdentityVerificationAttributesRequestWait

### Identities
- **Type**: typing.List[str]
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetIdentityVerificationAttributesResponse

### VerificationAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ses.ses_classes.IdentityVerificationAttributes]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# GetSendQuotaResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# GetSendStatisticsResponse

### SendDataPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.SendDataPoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateResponse

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Template'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# IdentityDkimAttributes

### DkimEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### DkimVerificationStatus
- **Type**: typing.Literal['Failed', 'NotStarted', 'Pending', 'Success', 'TemporaryFailure']
- **Required**: Yes

### DkimTokens
- **Type**: typing.Optional[typing.List[str]]


# IdentityMailFromDomainAttributes

### MailFromDomain
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomainStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Success', 'TemporaryFailure']
- **Required**: Yes

### BehaviorOnMXFailure
- **Type**: typing.Literal['RejectMessage', 'UseDefaultValue']
- **Required**: Yes


# IdentityNotificationAttributes

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


# IdentityVerificationAttributes

### VerificationStatus
- **Type**: typing.Literal['Failed', 'NotStarted', 'Pending', 'Success', 'TemporaryFailure']
- **Required**: Yes

### VerificationToken
- **Type**: typing.Optional[str]


# KinesisFirehoseDestination

### IAMRoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamARN
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaAction

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]

### InvocationType
- **Type**: typing.Optional[typing.Literal['Event', 'RequestResponse']]


# ListConfigurationSetsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListConfigurationSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses.ses_classes.PaginatorConfig]


# ListConfigurationSetsResponse

### ConfigurationSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ConfigurationSet]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomVerificationEmailTemplatesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCustomVerificationEmailTemplatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses.ses_classes.PaginatorConfig]


# ListCustomVerificationEmailTemplatesResponse

### CustomVerificationEmailTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.CustomVerificationEmailTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentitiesRequest

### IdentityType
- **Type**: typing.Optional[typing.Literal['Domain', 'EmailAddress']]

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListIdentitiesRequestPaginate

### IdentityType
- **Type**: typing.Optional[typing.Literal['Domain', 'EmailAddress']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses.ses_classes.PaginatorConfig]


# ListIdentitiesResponse

### Identities
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPoliciesRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes


# ListIdentityPoliciesResponse

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# ListReceiptFiltersResponse

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptFilter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# ListReceiptRuleSetsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListReceiptRuleSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses.ses_classes.PaginatorConfig]


# ListReceiptRuleSetsResponse

### RuleSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRuleSetMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTemplatesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListTemplatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ses.ses_classes.PaginatorConfig]


# ListTemplatesResponse

### TemplatesMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.TemplateMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVerifiedEmailAddressesResponse

### VerifiedEmailAddresses
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# Message

### Subject
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Content'>
- **Required**: Yes

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Body'>
- **Required**: Yes


# MessageDsn

### ReportingMta
- **Type**: <class 'str'>
- **Required**: Yes

### ArrivalDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ExtensionFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ExtensionField]]


# MessageTag

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutConfigurationSetDeliveryOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryOptions
- **Type**: <class 'NoneType'>


# PutIdentityPolicyRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# RawMessage

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# ReceiptAction

### S3Action
- **Type**: <class 'NoneType'>

### BounceAction
- **Type**: <class 'NoneType'>

### WorkmailAction
- **Type**: <class 'NoneType'>

### LambdaAction
- **Type**: <class 'NoneType'>

### StopAction
- **Type**: <class 'NoneType'>

### AddHeaderAction
- **Type**: <class 'NoneType'>

### SNSAction
- **Type**: <class 'NoneType'>

### ConnectAction
- **Type**: <class 'NoneType'>


# ReceiptFilter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IpFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptIpFilter'>
- **Required**: Yes


# ReceiptIpFilter

### Policy
- **Type**: typing.Literal['Allow', 'Block']
- **Required**: Yes

### Cidr
- **Type**: <class 'str'>
- **Required**: Yes


# ReceiptRule

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptAction]]

### ScanEnabled
- **Type**: typing.Optional[bool]


# ReceiptRuleOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptAction]]

### ScanEnabled
- **Type**: typing.Optional[bool]


# ReceiptRuleSetMetadata

### Name
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# RecipientDsnFields

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.ExtensionField]]


# ReorderReceiptRuleSetRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleNames
- **Type**: typing.List[str]
- **Required**: Yes


# ReputationOptions

### SendingEnabled
- **Type**: typing.Optional[bool]

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


# S3Action

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]

### ObjectKeyPrefix
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# SNSAction

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Encoding
- **Type**: typing.Optional[typing.Literal['Base64', 'UTF-8']]


# SNSDestination

### TopicARN
- **Type**: <class 'str'>
- **Required**: Yes


# SendBounceRequest

### OriginalMessageId
- **Type**: <class 'str'>
- **Required**: Yes

### BounceSender
- **Type**: <class 'str'>
- **Required**: Yes

### BouncedRecipientInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.BouncedRecipientInfo]
- **Required**: Yes

### Explanation
- **Type**: typing.Optional[str]

### MessageDsn
- **Type**: <class 'NoneType'>

### BounceSenderArn
- **Type**: typing.Optional[str]


# SendBounceResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# SendBulkTemplatedEmailRequest

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Template
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultTemplateData
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.BulkEmailDestination]
- **Required**: Yes

### SourceArn
- **Type**: typing.Optional[str]

### ReplyToAddresses
- **Type**: typing.Optional[typing.List[str]]

### ReturnPath
- **Type**: typing.Optional[str]

### ReturnPathArn
- **Type**: typing.Optional[str]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### DefaultTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.MessageTag]]

### TemplateArn
- **Type**: typing.Optional[str]


# SendBulkTemplatedEmailResponse

### Status
- **Type**: typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.BulkEmailDestinationStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# SendDataPoint

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


# SendEmailRequest

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Destination'>
- **Required**: Yes

### Message
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Message'>
- **Required**: Yes

### ReplyToAddresses
- **Type**: typing.Optional[typing.List[str]]

### ReturnPath
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### ReturnPathArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.MessageTag]]

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendEmailResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# SendRawEmailRequest

### RawMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.RawMessage'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### Destinations
- **Type**: typing.Optional[typing.List[str]]

### FromArn
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### ReturnPathArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.MessageTag]]

### ConfigurationSetName
- **Type**: typing.Optional[str]


# SendRawEmailResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# SendTemplatedEmailRequest

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Destination'>
- **Required**: Yes

### Template
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateData
- **Type**: <class 'str'>
- **Required**: Yes

### ReplyToAddresses
- **Type**: typing.Optional[typing.List[str]]

### ReturnPath
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### ReturnPathArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ses.ses_classes.MessageTag]]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### TemplateArn
- **Type**: typing.Optional[str]


# SendTemplatedEmailResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# SetActiveReceiptRuleSetRequest

### RuleSetName
- **Type**: typing.Optional[str]


# SetIdentityDkimEnabledRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### DkimEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SetIdentityFeedbackForwardingEnabledRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### ForwardingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SetIdentityHeadersInNotificationsEnabledRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationType
- **Type**: typing.Literal['Bounce', 'Complaint', 'Delivery']
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SetIdentityMailFromDomainRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### MailFromDomain
- **Type**: typing.Optional[str]

### BehaviorOnMXFailure
- **Type**: typing.Optional[typing.Literal['RejectMessage', 'UseDefaultValue']]


# SetIdentityNotificationTopicRequest

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationType
- **Type**: typing.Literal['Bounce', 'Complaint', 'Delivery']
- **Required**: Yes

### SnsTopic
- **Type**: typing.Optional[str]


# SetReceiptRulePositionRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### After
- **Type**: typing.Optional[str]


# StopAction

### Scope
- **Type**: typing.Literal['RuleSet']
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]


# Template

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### SubjectPart
- **Type**: typing.Optional[str]

### TextPart
- **Type**: typing.Optional[str]

### HtmlPart
- **Type**: typing.Optional[str]


# TemplateMetadata

### Name
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# TestRenderTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateData
- **Type**: <class 'str'>
- **Required**: Yes


# TestRenderTemplateResponse

### RenderedTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# TrackingOptions

### CustomRedirectDomain
- **Type**: typing.Optional[str]


# UpdateAccountSendingEnabledRequest

### Enabled
- **Type**: typing.Optional[bool]


# UpdateConfigurationSetEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ses.ses_classes.EventDestination, aws_resource_validator.pydantic_models.ses.ses_classes.EventDestinationOutput]
- **Required**: Yes


# UpdateConfigurationSetReputationMetricsEnabledRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateConfigurationSetSendingEnabledRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateConfigurationSetTrackingOptionsRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.TrackingOptions'>
- **Required**: Yes


# UpdateCustomVerificationEmailTemplateRequest

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


# UpdateReceiptRuleRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Rule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRule, aws_resource_validator.pydantic_models.ses.ses_classes.ReceiptRuleOutput]
- **Required**: Yes


# UpdateTemplateRequest

### Template
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.Template'>
- **Required**: Yes


# VerifyDomainDkimRequest

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyDomainDkimResponse

### DkimTokens
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# VerifyDomainIdentityRequest

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyDomainIdentityResponse

### VerificationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ses.ses_classes.ResponseMetadata'>
- **Required**: Yes


# VerifyEmailAddressRequest

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyEmailIdentityRequest

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkmailAction

### OrganizationArn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]


