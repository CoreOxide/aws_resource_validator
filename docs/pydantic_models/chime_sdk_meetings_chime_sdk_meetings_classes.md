# Chime Sdk Meetings Chime Sdk Meetings Classes

# Attendee

### ExternalUserId
- **Type**: typing.Optional[str]

### AttendeeId
- **Type**: typing.Optional[str]

### JoinToken
- **Type**: typing.Optional[str]

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.AttendeeCapabilities]


# AttendeeCapabilities

### Audio
- **Type**: typing.Literal['None', 'Receive', 'Send', 'SendReceive']
- **Required**: Yes

### Video
- **Type**: typing.Literal['None', 'Receive', 'Send', 'SendReceive']
- **Required**: Yes

### Content
- **Type**: typing.Literal['None', 'Receive', 'Send', 'SendReceive']
- **Required**: Yes


# AttendeeFeatures

### MaxCount
- **Type**: typing.Optional[int]


# AttendeeIdItem

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# AudioFeatures

### EchoReduction
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'UNAVAILABLE']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateAttendeeRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.CreateAttendeeRequestItem]
- **Required**: Yes


# BatchCreateAttendeeResponse

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Attendee]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.CreateAttendeeError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateAttendeeCapabilitiesExceptRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludedAttendeeIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.AttendeeIdItem]
- **Required**: Yes

### Capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.AttendeeCapabilities'>
- **Required**: Yes


# ContentFeatures

### MaxResolution
- **Type**: typing.Optional[typing.Literal['FHD', 'None', 'UHD']]


# CreateAttendeeError

### ExternalUserId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# CreateAttendeeRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.AttendeeCapabilities]


# CreateAttendeeRequestItem

### ExternalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.AttendeeCapabilities]


# CreateAttendeeResponse

### Attendee
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Attendee'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMeetingRequest

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
- **Type**: <class 'NoneType'>

### MeetingFeatures
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.MeetingFeaturesConfiguration]

### PrimaryMeetingId
- **Type**: typing.Optional[str]

### TenantIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Tag]]


# CreateMeetingResponse

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Meeting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMeetingWithAttendeesRequest

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.CreateAttendeeRequestItem]
- **Required**: Yes

### MeetingHostId
- **Type**: typing.Optional[str]

### MeetingFeatures
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.MeetingFeaturesConfiguration]

### NotificationsConfiguration
- **Type**: <class 'NoneType'>

### PrimaryMeetingId
- **Type**: typing.Optional[str]

### TenantIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Tag]]


# CreateMeetingWithAttendeesResponse

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Meeting'>
- **Required**: Yes

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Attendee]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.CreateAttendeeError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAttendeeRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMeetingRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# EngineTranscribeMedicalSettings

### LanguageCode
- **Type**: typing.Literal['en-US']
- **Required**: Yes

### Specialty
- **Type**: typing.Literal['CARDIOLOGY', 'NEUROLOGY', 'ONCOLOGY', 'PRIMARYCARE', 'RADIOLOGY', 'UROLOGY']
- **Required**: Yes

### Type
- **Type**: typing.Literal['CONVERSATION', 'DICTATION']
- **Required**: Yes

### VocabularyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[typing.Literal['ap-southeast-2', 'auto', 'ca-central-1', 'eu-west-1', 'us-east-1', 'us-east-2', 'us-west-2']]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PHI']]


# EngineTranscribeSettings

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


# GetAttendeeRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAttendeeResponse

### Attendee
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Attendee'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# GetMeetingRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMeetingResponse

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Meeting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# ListAttendeesRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAttendeesResponse

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Attendee]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# MediaPlacement

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


# Meeting

### MeetingId
- **Type**: typing.Optional[str]

### MeetingHostId
- **Type**: typing.Optional[str]

### ExternalMeetingId
- **Type**: typing.Optional[str]

### MediaRegion
- **Type**: typing.Optional[str]

### MediaPlacement
- **Type**: <class 'NoneType'>

### MeetingFeatures
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.MeetingFeaturesConfiguration]

### PrimaryMeetingId
- **Type**: typing.Optional[str]

### TenantIds
- **Type**: typing.Optional[typing.List[str]]

### MeetingArn
- **Type**: typing.Optional[str]


# MeetingFeaturesConfiguration

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.AudioFeatures]

### Video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.VideoFeatures]

### Content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ContentFeatures]

### Attendee
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.AttendeeFeatures]


# NotificationsConfiguration

### LambdaFunctionArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SqsQueueArn
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


# StartMeetingTranscriptionRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### TranscriptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.TranscriptionConfiguration'>
- **Required**: Yes


# StopMeetingTranscriptionRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Tag]
- **Required**: Yes


# TranscriptionConfiguration

### EngineTranscribeSettings
- **Type**: <class 'NoneType'>

### EngineTranscribeMedicalSettings
- **Type**: <class 'NoneType'>


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAttendeeCapabilitiesRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.AttendeeCapabilities'>
- **Required**: Yes


# UpdateAttendeeCapabilitiesResponse

### Attendee
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.Attendee'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_meetings.chime_sdk_meetings_classes.ResponseMetadata'>
- **Required**: Yes


# VideoFeatures

### MaxResolution
- **Type**: typing.Optional[typing.Literal['FHD', 'HD', 'None']]


