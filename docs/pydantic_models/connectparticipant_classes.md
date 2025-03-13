# Connectparticipant Classes

# AttachmentItemTypeDef

### ContentType
- **Type**: typing.Optional[str]

### AttachmentId
- **Type**: typing.Optional[str]

### AttachmentName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'IN_PROGRESS', 'REJECTED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelParticipantAuthenticationRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# CompleteAttachmentUploadRequestTypeDef

### AttachmentIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# ConnectionCredentialsTypeDef

### ConnectionToken
- **Type**: typing.Optional[str]

### Expiry
- **Type**: typing.Optional[str]


# CreateParticipantConnectionResponseTypeDef

### Websocket
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.WebsocketTypeDef'>
- **Required**: Yes

### ConnectionCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ConnectionCredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeViewRequestTypeDef

### ViewToken
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeViewResponseTypeDef

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisconnectParticipantRequestTypeDef

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# GetAttachmentRequestTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes

### UrlExpiryInSeconds
- **Type**: typing.Optional[int]


# GetAttachmentResponseTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### UrlExpiry
- **Type**: <class 'str'>
- **Required**: Yes

### AttachmentSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAuthenticationUrlRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### RedirectUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthenticationUrlResponseTypeDef

### AuthenticationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTranscriptRequestTypeDef

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ScanDirection
- **Type**: typing.Optional[typing.Literal['BACKWARD', 'FORWARD']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### StartPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectparticipant_classes.StartPositionTypeDef]


# GetTranscriptResponseTypeDef

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### Transcript
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectparticipant_classes.ItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageMetadataTypeDef

### MessageId
- **Type**: typing.Optional[str]

### Receipts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectparticipant_classes.ReceiptTypeDef]]


# ReceiptTypeDef

### DeliveredTimestamp
- **Type**: typing.Optional[str]

### ReadTimestamp
- **Type**: typing.Optional[str]

### RecipientParticipantId
- **Type**: typing.Optional[str]


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


# SendEventRequestTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# SendEventResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AbsoluteTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendMessageRequestTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# SendMessageResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AbsoluteTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartAttachmentUploadRequestTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### AttachmentSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### AttachmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartAttachmentUploadResponseTypeDef

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### UploadMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.UploadMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartPositionTypeDef

### Id
- **Type**: typing.Optional[str]

### AbsoluteTime
- **Type**: typing.Optional[str]

### MostRecent
- **Type**: typing.Optional[int]


# UploadMetadataTypeDef

### Url
- **Type**: typing.Optional[str]

### UrlExpiry
- **Type**: typing.Optional[str]

### HeadersToInclude
- **Type**: typing.Optional[typing.Dict[str, str]]


# ViewContentTypeDef

### InputSchema
- **Type**: typing.Optional[str]

### Template
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[str]]


# ViewTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectparticipant_classes.ViewContentTypeDef]


# WebsocketTypeDef

### Url
- **Type**: typing.Optional[str]

### ConnectionExpiry
- **Type**: typing.Optional[str]


