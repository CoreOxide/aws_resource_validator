# Socialmessaging Socialmessaging Classes

# AssociateWhatsAppBusinessAccountInput

### signupCallback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppSignupCallback]

### setupFinalization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppSetupFinalization]


# AssociateWhatsAppBusinessAccountOutput

### signupCallbackResult
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppSignupCallbackResult'>
- **Required**: Yes

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteWhatsAppMessageMediaInput

### mediaId
- **Type**: <class 'str'>
- **Required**: Yes

### originationPhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatsAppMessageMediaOutput

### success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateWhatsAppBusinessAccountInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetLinkedWhatsAppBusinessAccountInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetLinkedWhatsAppBusinessAccountOutput

### account
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.LinkedWhatsAppBusinessAccount'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetLinkedWhatsAppBusinessAccountPhoneNumberInput

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetLinkedWhatsAppBusinessAccountPhoneNumberOutput

### phoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppPhoneNumberDetail'>
- **Required**: Yes

### linkedWhatsAppBusinessAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetWhatsAppMessageMediaInput

### mediaId
- **Type**: <class 'str'>
- **Required**: Yes

### originationPhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### metadataOnly
- **Type**: typing.Optional[bool]

### destinationS3PresignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.S3PresignedUrl]

### destinationS3File
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.S3File]


# GetWhatsAppMessageMediaOutput

### mimeType
- **Type**: <class 'str'>
- **Required**: Yes

### fileSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# LinkedWhatsAppBusinessAccount

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### wabaId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['COMPLETE', 'INCOMPLETE']
- **Required**: Yes

### linkDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### wabaName
- **Type**: <class 'str'>
- **Required**: Yes

### eventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppBusinessAccountEventDestination]
- **Required**: Yes

### phoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppPhoneNumberSummary]
- **Required**: Yes


# LinkedWhatsAppBusinessAccountIdMetaData

### accountName
- **Type**: typing.Optional[str]

### registrationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'INCOMPLETE']]

### unregisteredWhatsAppPhoneNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppPhoneNumberDetail]]

### wabaId
- **Type**: typing.Optional[str]


# LinkedWhatsAppBusinessAccountSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### wabaId
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['COMPLETE', 'INCOMPLETE']
- **Required**: Yes

### linkDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### wabaName
- **Type**: <class 'str'>
- **Required**: Yes

### eventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppBusinessAccountEventDestination]
- **Required**: Yes


# ListLinkedWhatsAppBusinessAccountsInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLinkedWhatsAppBusinessAccountsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.PaginatorConfig]


# ListLinkedWhatsAppBusinessAccountsOutput

### linkedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.LinkedWhatsAppBusinessAccountSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PostWhatsAppMessageMediaInput

### originationPhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceS3PresignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.S3PresignedUrl]

### sourceS3File
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.S3File]


# PostWhatsAppMessageMediaOutput

### mediaId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# PutWhatsAppBusinessAccountEventDestinationsInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### eventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppBusinessAccountEventDestination]
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


# S3File

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# S3PresignedUrl

### url
- **Type**: <class 'str'>
- **Required**: Yes

### headers
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# SendWhatsAppMessageInput

### originationPhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### metaApiVersion
- **Type**: <class 'str'>
- **Required**: Yes


# SendWhatsAppMessageOutput

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.Tag]
- **Required**: Yes


# TagResourceOutput

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagResourceOutput

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.ResponseMetadata'>
- **Required**: Yes


# WabaPhoneNumberSetupFinalization

### id
- **Type**: <class 'str'>
- **Required**: Yes

### twoFactorPin
- **Type**: <class 'str'>
- **Required**: Yes

### dataLocalizationRegion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.Tag]]


# WabaSetupFinalization

### id
- **Type**: typing.Optional[str]

### eventDestinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WhatsAppBusinessAccountEventDestination]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.Tag]]


# WhatsAppBusinessAccountEventDestination

### eventDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]


# WhatsAppPhoneNumberDetail

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### phoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### phoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### metaPhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### displayPhoneNumberName
- **Type**: <class 'str'>
- **Required**: Yes

### displayPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### qualityRating
- **Type**: <class 'str'>
- **Required**: Yes


# WhatsAppPhoneNumberSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### phoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### phoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### metaPhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### displayPhoneNumberName
- **Type**: <class 'str'>
- **Required**: Yes

### displayPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### qualityRating
- **Type**: <class 'str'>
- **Required**: Yes


# WhatsAppSetupFinalization

### associateInProgressToken
- **Type**: <class 'str'>
- **Required**: Yes

### phoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WabaPhoneNumberSetupFinalization]
- **Required**: Yes

### phoneNumberParent
- **Type**: typing.Optional[str]

### waba
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.WabaSetupFinalization]


# WhatsAppSignupCallback

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes


# WhatsAppSignupCallbackResult

### associateInProgressToken
- **Type**: typing.Optional[str]

### linkedAccountsWithIncompleteSetup
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_classes.LinkedWhatsAppBusinessAccountIdMetaData]]


