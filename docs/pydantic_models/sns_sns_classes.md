# Sns Sns Classes

# AddPermissionInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### AWSAccountId
- **Type**: typing.List[str]
- **Required**: Yes

### ActionName
- **Type**: typing.List[str]
- **Required**: Yes


# AddPermissionInputTopicAddPermission

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### AWSAccountId
- **Type**: typing.List[str]
- **Required**: Yes

### ActionName
- **Type**: typing.List[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchResultErrorEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### SenderFault
- **Type**: <class 'bool'>
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]


# CheckIfPhoneNumberIsOptedOutInput

### phoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# CheckIfPhoneNumberIsOptedOutResponse

### isOptedOut
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# ConfirmSubscriptionInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticateOnUnsubscribe
- **Type**: typing.Optional[str]


# ConfirmSubscriptionInputTopicConfirmSubscription

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticateOnUnsubscribe
- **Type**: typing.Optional[str]


# ConfirmSubscriptionResponse

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEndpointResponse

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePlatformApplicationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# CreatePlatformApplicationInputServiceResourceCreatePlatformApplication

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# CreatePlatformApplicationResponse

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePlatformEndpointInput

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### CustomUserData
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpoint

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### CustomUserData
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSMSSandboxPhoneNumberInput

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-GB', 'en-US', 'es-419', 'es-ES', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'kr-KR', 'pt-BR', 'zh-CN', 'zh-TW']]


# CreateTopicInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.Tag]]

### DataProtectionPolicy
- **Type**: typing.Optional[str]


# CreateTopicInputServiceResourceCreateTopic

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.Tag]]

### DataProtectionPolicy
- **Type**: typing.Optional[str]


# CreateTopicResponse

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEndpointInput

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlatformApplicationInput

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSMSSandboxPhoneNumberInput

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### EndpointArn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetDataProtectionPolicyInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataProtectionPolicyResponse

### DataProtectionPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# GetEndpointAttributesInput

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEndpointAttributesResponse

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# GetPlatformApplicationAttributesInput

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPlatformApplicationAttributesResponse

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# GetSMSAttributesInput

### attributes
- **Type**: typing.Optional[typing.List[str]]


# GetSMSAttributesResponse

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# GetSMSSandboxAccountStatusResult

### IsInSandbox
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# GetSubscriptionAttributesInput

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionAttributesResponse

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# GetTopicAttributesInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTopicAttributesResponse

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# ListEndpointsByPlatformApplicationInput

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointsByPlatformApplicationInputPaginate

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns.sns_classes.PaginatorConfig]


# ListEndpointsByPlatformApplicationResponse

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOriginationNumbersRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOriginationNumbersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns.sns_classes.PaginatorConfig]


# ListOriginationNumbersResult

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.PhoneNumberInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersOptedOutInput

### nextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersOptedOutInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns.sns_classes.PaginatorConfig]


# ListPhoneNumbersOptedOutResponse

### phoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPlatformApplicationsInput

### NextToken
- **Type**: typing.Optional[str]


# ListPlatformApplicationsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns.sns_classes.PaginatorConfig]


# ListPlatformApplicationsResponse

### PlatformApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.PlatformApplication]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSMSSandboxPhoneNumbersInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSMSSandboxPhoneNumbersInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns.sns_classes.PaginatorConfig]


# ListSMSSandboxPhoneNumbersResult

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.SMSSandboxPhoneNumber]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsByTopicInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsByTopicInputPaginate

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns.sns_classes.PaginatorConfig]


# ListSubscriptionsByTopicResponse

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.Subscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsInput

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns.sns_classes.PaginatorConfig]


# ListSubscriptionsResponse

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.Subscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# ListTopicsInput

### NextToken
- **Type**: typing.Optional[str]


# ListTopicsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns.sns_classes.PaginatorConfig]


# ListTopicsResponse

### Topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.Topic]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MessageAttributeValue

### DataType
- **Type**: <class 'str'>
- **Required**: Yes

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# OptInPhoneNumberInput

### phoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhoneNumberInformation

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### PhoneNumber
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Iso2CountryCode
- **Type**: typing.Optional[str]

### RouteType
- **Type**: typing.Optional[typing.Literal['Premium', 'Promotional', 'Transactional']]

### NumberCapabilities
- **Type**: typing.Optional[typing.List[typing.Literal['MMS', 'SMS', 'VOICE']]]


# PlatformApplication

### PlatformApplicationArn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# PublishBatchInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### PublishBatchRequestEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.PublishBatchRequestEntry]
- **Required**: Yes


# PublishBatchRequestEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Subject
- **Type**: typing.Optional[str]

### MessageStructure
- **Type**: typing.Optional[str]

### MessageAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sns.sns_classes.MessageAttributeValue]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# PublishBatchResponse

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.PublishBatchResultEntry]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.BatchResultErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# PublishBatchResultEntry

### Id
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]

### SequenceNumber
- **Type**: typing.Optional[str]


# PublishInput

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### MessageStructure
- **Type**: typing.Optional[str]

### MessageAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sns.sns_classes.MessageAttributeValue]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# PublishInputPlatformEndpointPublish

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### TopicArn
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### MessageStructure
- **Type**: typing.Optional[str]

### MessageAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sns.sns_classes.MessageAttributeValue]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# PublishInputTopicPublish

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### MessageStructure
- **Type**: typing.Optional[str]

### MessageAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sns.sns_classes.MessageAttributeValue]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# PublishResponse

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### SequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# PutDataProtectionPolicyInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataProtectionPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# RemovePermissionInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes


# RemovePermissionInputTopicRemovePermission

### Label
- **Type**: <class 'str'>
- **Required**: Yes


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


# SMSSandboxPhoneNumber

### PhoneNumber
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Pending', 'Verified']]


# SetEndpointAttributesInput

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# SetEndpointAttributesInputPlatformEndpointSetAttributes

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# SetPlatformApplicationAttributesInput

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# SetPlatformApplicationAttributesInputPlatformApplicationSetAttributes

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# SetSMSAttributesInput

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# SetSubscriptionAttributesInput

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# SetSubscriptionAttributesInputSubscriptionSetAttributes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# SetTopicAttributesInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# SetTopicAttributesInputTopicSetAttributes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# SubscribeInput

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoint
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### ReturnSubscriptionArn
- **Type**: typing.Optional[bool]


# SubscribeInputTopicSubscribe

### Protocol
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoint
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### ReturnSubscriptionArn
- **Type**: typing.Optional[bool]


# SubscribeResponse

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns.sns_classes.ResponseMetadata'>
- **Required**: Yes


# Subscription

### SubscriptionArn
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### TopicArn
- **Type**: typing.Optional[str]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns.sns_classes.Tag]
- **Required**: Yes


# Topic

### TopicArn
- **Type**: typing.Optional[str]


# UnsubscribeInput

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# VerifySMSSandboxPhoneNumberInput

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OneTimePassword
- **Type**: <class 'str'>
- **Required**: Yes


