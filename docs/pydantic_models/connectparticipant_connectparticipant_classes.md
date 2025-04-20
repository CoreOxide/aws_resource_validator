# Connectparticipant Connectparticipant Classes

# AttachmentItem

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

# CancelParticipantAuthenticationRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# CompleteAttachmentUploadRequest

### AttachmentIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# ConnectionCredentials

### ConnectionToken
- **Type**: typing.Optional[str]

### Expiry
- **Type**: typing.Optional[str]


# CreateParticipantConnectionRequest

### ParticipantToken
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.List[typing.Literal['CONNECTION_CREDENTIALS', 'WEBSOCKET']]]

### ConnectParticipant
- **Type**: typing.Optional[bool]


# CreateParticipantConnectionResponse

### Websocket
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.Websocket'>
- **Required**: Yes

### ConnectionCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ConnectionCredentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeViewRequest

### ViewToken
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeViewResponse

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.View'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ResponseMetadata'>
- **Required**: Yes


# DisconnectParticipantRequest

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# GetAttachmentRequest

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes

### UrlExpiryInSeconds
- **Type**: typing.Optional[int]


# GetAttachmentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ResponseMetadata'>
- **Required**: Yes


# GetAuthenticationUrlRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### RedirectUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthenticationUrlResponse

### AuthenticationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ResponseMetadata'>
- **Required**: Yes


# GetTranscriptRequest

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
- **Type**: <class 'NoneType'>


# GetTranscriptResponse

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### Transcript
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.Item]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Item

### AbsoluteTime
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ATTACHMENT', 'CHAT_ENDED', 'CONNECTION_ACK', 'EVENT', 'MESSAGE', 'MESSAGE_DELIVERED', 'MESSAGE_READ', 'PARTICIPANT_JOINED', 'PARTICIPANT_LEFT', 'TRANSFER_FAILED', 'TRANSFER_SUCCEEDED', 'TYPING']]

### ParticipantId
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']]

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.AttachmentItem]]

### MessageMetadata
- **Type**: <class 'NoneType'>

### RelatedContactId
- **Type**: typing.Optional[str]

### ContactId
- **Type**: typing.Optional[str]


# MessageMetadata

### MessageId
- **Type**: typing.Optional[str]

### Receipts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.Receipt]]


# Receipt

### DeliveredTimestamp
- **Type**: typing.Optional[str]

### ReadTimestamp
- **Type**: typing.Optional[str]

### RecipientParticipantId
- **Type**: typing.Optional[str]


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


# SendEventRequest

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


# SendEventResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AbsoluteTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ResponseMetadata'>
- **Required**: Yes


# SendMessageRequest

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


# SendMessageResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AbsoluteTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ResponseMetadata'>
- **Required**: Yes


# StartAttachmentUploadRequest

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


# StartAttachmentUploadResponse

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### UploadMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.UploadMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ResponseMetadata'>
- **Required**: Yes


# StartPosition

### Id
- **Type**: typing.Optional[str]

### AbsoluteTime
- **Type**: typing.Optional[str]

### MostRecent
- **Type**: typing.Optional[int]


# UploadMetadata

### Url
- **Type**: typing.Optional[str]

### UrlExpiry
- **Type**: typing.Optional[str]

### HeadersToInclude
- **Type**: typing.Optional[typing.Dict[str, str]]


# View

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_classes.ViewContent]


# ViewContent

### InputSchema
- **Type**: typing.Optional[str]

### Template
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[str]]


# Websocket

### Url
- **Type**: typing.Optional[str]

### ConnectionExpiry
- **Type**: typing.Optional[str]


