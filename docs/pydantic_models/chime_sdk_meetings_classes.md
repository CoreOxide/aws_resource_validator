# Chime Sdk Meetings Classes

# AttendeeCapabilitiesTypeDef

### Audio
- **Type**: typing.Literal['None', 'Receive', 'Send', 'SendReceive']
- **Required**: Yes

### Video
- **Type**: typing.Literal['None', 'Receive', 'Send', 'SendReceive']
- **Required**: Yes

### Content
- **Type**: typing.Literal['None', 'Receive', 'Send', 'SendReceive']
- **Required**: Yes


# AttendeeFeaturesTypeDef

### MaxCount
- **Type**: typing.Optional[int]


# AttendeeIdItemTypeDef

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# AttendeeTypeDef

### ExternalUserId
- **Type**: typing.Optional[str]

### AttendeeId
- **Type**: typing.Optional[str]

### JoinToken
- **Type**: typing.Optional[str]

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeCapabilitiesTypeDef]


# AudioFeaturesTypeDef

### EchoReduction
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'UNAVAILABLE']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateAttendeeRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### Attendees
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.CreateAttendeeRequestItemTypeDef]
- **Required**: Yes


# BatchCreateAttendeeResponseTypeDef

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.CreateAttendeeErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateAttendeeCapabilitiesExceptRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludedAttendeeIds
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeIdItemTypeDef]
- **Required**: Yes

### Capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeCapabilitiesTypeDef'>
- **Required**: Yes


# ContentFeaturesTypeDef

### MaxResolution
- **Type**: typing.Optional[typing.Literal['FHD', 'None', 'UHD']]


# CreateAttendeeErrorTypeDef

### ExternalUserId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# CreateAttendeeRequestItemTypeDef

### ExternalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeCapabilitiesTypeDef]


# CreateAttendeeRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeCapabilitiesTypeDef]


# CreateAttendeeResponseTypeDef

### Attendee
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMeetingRequestTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### MediaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalMeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### MeetingHostId
- **Type**: typing.Optional[str]

### NotificationsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.NotificationsConfigurationTypeDef]

### MeetingFeatures
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.MeetingFeaturesConfigurationTypeDef]

### PrimaryMeetingId
- **Type**: typing.Optional[str]

### TenantIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.TagTypeDef]]


# CreateMeetingResponseTypeDef

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.MeetingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMeetingWithAttendeesRequestTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### MediaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalMeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### Attendees
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.CreateAttendeeRequestItemTypeDef]
- **Required**: Yes

### MeetingHostId
- **Type**: typing.Optional[str]

### MeetingFeatures
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.MeetingFeaturesConfigurationTypeDef]

### NotificationsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.NotificationsConfigurationTypeDef]

### PrimaryMeetingId
- **Type**: typing.Optional[str]

### TenantIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.TagTypeDef]]


# CreateMeetingWithAttendeesResponseTypeDef

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.MeetingTypeDef'>
- **Required**: Yes

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.CreateAttendeeErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAttendeeRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMeetingRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EngineTranscribeMedicalSettingsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EngineTranscribeSettingsTypeDef

### LanguageCode
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'fr-CA', 'fr-FR', 'hi-IN', 'it-IT', 'ja-JP', 'ko-KR', 'pt-BR', 'th-TH', 'zh-CN']]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-southeast-2', 'auto', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-west-1', 'us-west-2']]

### EnablePartialResultsStabilization
- **Type**: typing.Optional[bool]

### PartialResultsStability
- **Type**: typing.Optional[typing.Literal['high', 'low', 'medium']]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PII']]

### ContentRedactionType
- **Type**: typing.Optional[typing.Literal['PII']]

### PiiEntityTypes
- **Type**: typing.Optional[str]

### LanguageModelName
- **Type**: typing.Optional[str]

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### LanguageOptions
- **Type**: typing.Optional[str]

### PreferredLanguage
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'fr-CA', 'fr-FR', 'hi-IN', 'it-IT', 'ja-JP', 'ko-KR', 'pt-BR', 'th-TH', 'zh-CN']]

### VocabularyNames
- **Type**: typing.Optional[str]

### VocabularyFilterNames
- **Type**: typing.Optional[str]


# GetAttendeeRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAttendeeResponseTypeDef

### Attendee
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMeetingRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMeetingResponseTypeDef

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.MeetingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttendeesRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAttendeesResponseTypeDef

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MediaPlacementTypeDef

### AudioHostUrl
- **Type**: typing.Optional[str]

### AudioFallbackUrl
- **Type**: typing.Optional[str]

### SignalingUrl
- **Type**: typing.Optional[str]

### TurnControlUrl
- **Type**: typing.Optional[str]

### ScreenDataUrl
- **Type**: typing.Optional[str]

### ScreenViewingUrl
- **Type**: typing.Optional[str]

### ScreenSharingUrl
- **Type**: typing.Optional[str]

### EventIngestionUrl
- **Type**: typing.Optional[str]


# MeetingFeaturesConfigurationTypeDef

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AudioFeaturesTypeDef]

### Video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.VideoFeaturesTypeDef]

### Content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ContentFeaturesTypeDef]

### Attendee
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeFeaturesTypeDef]


# MeetingTypeDef

### MeetingId
- **Type**: typing.Optional[str]

### MeetingHostId
- **Type**: typing.Optional[str]

### ExternalMeetingId
- **Type**: typing.Optional[str]

### MediaRegion
- **Type**: typing.Optional[str]

### MediaPlacement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.MediaPlacementTypeDef]

### MeetingFeatures
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.MeetingFeaturesConfigurationTypeDef]

### PrimaryMeetingId
- **Type**: typing.Optional[str]

### TenantIds
- **Type**: typing.Optional[typing.List[str]]

### MeetingArn
- **Type**: typing.Optional[str]


# NotificationsConfigurationTypeDef

### LambdaFunctionArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SqsQueueArn
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


# StartMeetingTranscriptionRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### TranscriptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.TranscriptionConfigurationTypeDef'>
- **Required**: Yes


# StopMeetingTranscriptionRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TranscriptionConfigurationTypeDef

### EngineTranscribeSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.EngineTranscribeSettingsTypeDef]

### EngineTranscribeMedicalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.EngineTranscribeMedicalSettingsTypeDef]


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAttendeeCapabilitiesRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeCapabilitiesTypeDef'>
- **Required**: Yes


# UpdateAttendeeCapabilitiesResponseTypeDef

### Attendee
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.AttendeeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VideoFeaturesTypeDef

### MaxResolution
- **Type**: typing.Optional[typing.Literal['FHD', 'HD', 'None']]


