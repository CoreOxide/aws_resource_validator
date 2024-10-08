# Pydantic Models in sns_classes

# AddPermissionInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### AWSAccountId
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ActionName
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AddPermissionInputTopicAddPermissionTypeDef

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### AWSAccountId
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ActionName
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchResultErrorEntryTypeDef

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


# CheckIfPhoneNumberIsOptedOutInputRequestTypeDef

### phoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# CheckIfPhoneNumberIsOptedOutResponseTypeDef

### isOptedOut
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfirmSubscriptionInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticateOnUnsubscribe
- **Type**: typing.Optional[str]


# ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticateOnUnsubscribe
- **Type**: typing.Optional[str]


# ConfirmSubscriptionResponseTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEndpointResponseTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePlatformApplicationInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# CreatePlatformApplicationResponseTypeDef

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### CustomUserData
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePlatformEndpointInputRequestTypeDef

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### CustomUserData
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSMSSandboxPhoneNumberInputRequestTypeDef

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-GB', 'en-US', 'es-419', 'es-ES', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'kr-KR', 'pt-BR', 'zh-CN', 'zh-TW']]


# CreateTopicInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sns_classes.TagTypeDef]]

### DataProtectionPolicy
- **Type**: typing.Optional[str]


# CreateTopicInputServiceResourceCreateTopicTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sns_classes.TagTypeDef]]

### DataProtectionPolicy
- **Type**: typing.Optional[str]


# CreateTopicResponseTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEndpointInputRequestTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlatformApplicationInputRequestTypeDef

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSMSSandboxPhoneNumberInputRequestTypeDef

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTopicInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointTypeDef

### EndpointArn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetDataProtectionPolicyInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataProtectionPolicyResponseTypeDef

### DataProtectionPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEndpointAttributesInputRequestTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEndpointAttributesResponseTypeDef

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPlatformApplicationAttributesInputRequestTypeDef

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPlatformApplicationAttributesResponseTypeDef

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSMSAttributesInputRequestTypeDef

### attributes
- **Type**: typing.Optional[typing.Sequence[str]]


# GetSMSAttributesResponseTypeDef

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSMSSandboxAccountStatusResultTypeDef

### IsInSandbox
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriptionAttributesInputRequestTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionAttributesResponseTypeDef

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTopicAttributesInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTopicAttributesResponseTypeDef

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEndpointsByPlatformApplicationInputRequestTypeDef

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointsByPlatformApplicationResponseTypeDef

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.EndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOriginationNumbersRequestListOriginationNumbersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns_classes.PaginatorConfigTypeDef]


# ListOriginationNumbersRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOriginationNumbersResultTypeDef

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.PhoneNumberInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersOptedOutInputListPhoneNumbersOptedOutPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns_classes.PaginatorConfigTypeDef]


# ListPhoneNumbersOptedOutInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersOptedOutResponseTypeDef

### phoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPlatformApplicationsInputListPlatformApplicationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns_classes.PaginatorConfigTypeDef]


# ListPlatformApplicationsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListPlatformApplicationsResponseTypeDef

### PlatformApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.PlatformApplicationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSMSSandboxPhoneNumbersInputListSMSSandboxPhoneNumbersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns_classes.PaginatorConfigTypeDef]


# ListSMSSandboxPhoneNumbersInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSMSSandboxPhoneNumbersResultTypeDef

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.SMSSandboxPhoneNumberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsByTopicInputListSubscriptionsByTopicPaginateTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns_classes.PaginatorConfigTypeDef]


# ListSubscriptionsByTopicInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsByTopicResponseTypeDef

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.SubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsInputListSubscriptionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns_classes.PaginatorConfigTypeDef]


# ListSubscriptionsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListSubscriptionsResponseTypeDef

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.SubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTopicsInputListTopicsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sns_classes.PaginatorConfigTypeDef]


# ListTopicsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListTopicsResponseTypeDef

### Topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.TopicTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MessageAttributeValueTypeDef

### DataType
- **Type**: <class 'str'>
- **Required**: Yes

### StringValue
- **Type**: typing.Optional[str]

### BinaryValue
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# OptInPhoneNumberInputRequestTypeDef

### phoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhoneNumberInformationTypeDef

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


# PlatformApplicationTypeDef

### PlatformApplicationArn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# PublishBatchInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### PublishBatchRequestEntries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sns_classes.PublishBatchRequestEntryTypeDef]
- **Required**: Yes


# PublishBatchRequestEntryTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sns_classes.MessageAttributeValueTypeDef]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# PublishBatchResponseTypeDef

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.PublishBatchResultEntryTypeDef]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sns_classes.BatchResultErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PublishBatchResultEntryTypeDef

### Id
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]

### SequenceNumber
- **Type**: typing.Optional[str]


# PublishInputPlatformEndpointPublishTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sns_classes.MessageAttributeValueTypeDef]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# PublishInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sns_classes.MessageAttributeValueTypeDef]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# PublishInputTopicPublishTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sns_classes.MessageAttributeValueTypeDef]]

### MessageDeduplicationId
- **Type**: typing.Optional[str]

### MessageGroupId
- **Type**: typing.Optional[str]


# PublishResponseTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### SequenceNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDataProtectionPolicyInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataProtectionPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# RemovePermissionInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes


# RemovePermissionInputTopicRemovePermissionTypeDef

### Label
- **Type**: <class 'str'>
- **Required**: Yes


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


# SMSSandboxPhoneNumberTypeDef

### PhoneNumber
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Pending', 'Verified']]


# SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# SetEndpointAttributesInputRequestTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# SetPlatformApplicationAttributesInputRequestTypeDef

### PlatformApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# SetSMSAttributesInputRequestTypeDef

### attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# SetSubscriptionAttributesInputRequestTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# SetTopicAttributesInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# SetTopicAttributesInputTopicSetAttributesTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# SubscribeInputRequestTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoint
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ReturnSubscriptionArn
- **Type**: typing.Optional[bool]


# SubscribeInputTopicSubscribeTypeDef

### Protocol
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoint
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ReturnSubscriptionArn
- **Type**: typing.Optional[bool]


# SubscribeResponseTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sns_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubscriptionTypeDef

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


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sns_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TopicTypeDef

### TopicArn
- **Type**: typing.Optional[str]


# UnsubscribeInputRequestTypeDef

### SubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VerifySMSSandboxPhoneNumberInputRequestTypeDef

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OneTimePassword
- **Type**: <class 'str'>
- **Required**: Yes


