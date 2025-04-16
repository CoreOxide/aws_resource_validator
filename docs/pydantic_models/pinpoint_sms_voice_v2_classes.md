# Pinpoint Sms Voice V2 Classes

# AccountAttribute

### Name
- **Type**: typing.Literal['ACCOUNT_TIER', 'DEFAULT_PROTECT_CONFIGURATION_ID']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# AccountLimit

### Name
- **Type**: typing.Literal['CONFIGURATION_SETS', 'OPT_OUT_LISTS', 'PHONE_NUMBERS', 'POOLS', 'REGISTRATIONS', 'REGISTRATION_ATTACHMENTS', 'SENDER_IDS', 'VERIFIED_DESTINATION_NUMBERS']
- **Required**: Yes

### Used
- **Type**: <class 'int'>
- **Required**: Yes

### Max
- **Type**: <class 'int'>
- **Required**: Yes


# AssociateOriginationIdentityRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateOriginationIdentityResult

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentityArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateProtectConfigurationRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateProtectConfigurationResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsDestination

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationSetFilter

### Name
- **Type**: typing.Literal['default-message-feedback-enabled', 'default-message-type', 'default-sender-id', 'event-destination-name', 'matching-event-types', 'protect-configuration-id']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ConfigurationSetInformation

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestination]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultMessageType
- **Type**: typing.Optional[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]

### DefaultSenderId
- **Type**: typing.Optional[str]

### DefaultMessageFeedbackEnabled
- **Type**: typing.Optional[bool]

### ProtectConfigurationId
- **Type**: typing.Optional[str]


# CreateConfigurationSetRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateConfigurationSetResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.Sequence[typing.Literal['ALL', 'MEDIA_ALL', 'MEDIA_BLOCKED', 'MEDIA_CARRIER_BLOCKED', 'MEDIA_CARRIER_UNREACHABLE', 'MEDIA_DELIVERED', 'MEDIA_FILE_INACCESSIBLE', 'MEDIA_FILE_SIZE_EXCEEDED', 'MEDIA_FILE_TYPE_UNSUPPORTED', 'MEDIA_INVALID', 'MEDIA_INVALID_MESSAGE', 'MEDIA_PENDING', 'MEDIA_QUEUED', 'MEDIA_SPAM', 'MEDIA_SUCCESSFUL', 'MEDIA_TTL_EXPIRED', 'MEDIA_UNKNOWN', 'MEDIA_UNREACHABLE', 'TEXT_ALL', 'TEXT_BLOCKED', 'TEXT_CARRIER_BLOCKED', 'TEXT_CARRIER_UNREACHABLE', 'TEXT_DELIVERED', 'TEXT_INVALID', 'TEXT_INVALID_MESSAGE', 'TEXT_PENDING', 'TEXT_PROTECT_BLOCKED', 'TEXT_QUEUED', 'TEXT_SENT', 'TEXT_SPAM', 'TEXT_SUCCESSFUL', 'TEXT_TTL_EXPIRED', 'TEXT_UNKNOWN', 'TEXT_UNREACHABLE', 'VOICE_ALL', 'VOICE_ANSWERED', 'VOICE_BUSY', 'VOICE_COMPLETED', 'VOICE_FAILED', 'VOICE_INITIATED', 'VOICE_NO_ANSWER', 'VOICE_RINGING', 'VOICE_TTL_EXPIRED']]
- **Required**: Yes

### CloudWatchLogsDestination
- **Type**: <class 'NoneType'>

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### SnsDestination
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]


# CreateEventDestinationResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOptOutListRequest

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateOptOutListResult

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePoolRequest

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreatePoolResult

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING']
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### TwoWayEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TwoWayChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayChannelRole
- **Type**: <class 'str'>
- **Required**: Yes

### SelfManagedOptOutsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### SharedRoutesEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProtectConfigurationRequest

### ClientToken
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]


# CreateProtectConfigurationResult

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccountDefault
- **Type**: <class 'bool'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegistrationAssociationRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRegistrationAssociationResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegistrationAttachmentRequest

### AttachmentBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Blob]

### AttachmentUrl
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateRegistrationAttachmentResult

### RegistrationAttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### AttachmentStatus
- **Type**: typing.Literal['DELETED', 'UPLOAD_COMPLETE', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegistrationRequest

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateRegistrationResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationStatus
- **Type**: typing.Literal['CLOSED', 'COMPLETE', 'CREATED', 'DELETED', 'PROVISIONING', 'REQUIRES_AUTHENTICATION', 'REQUIRES_UPDATES', 'REVIEWING', 'SUBMITTED']
- **Required**: Yes

### CurrentVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### AdditionalAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegistrationVersionRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRegistrationVersionResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### RegistrationVersionStatus
- **Type**: typing.Literal['APPROVED', 'ARCHIVED', 'DENIED', 'DISCARDED', 'DRAFT', 'REQUIRES_AUTHENTICATION', 'REVIEWING', 'REVOKED', 'SUBMITTED']
- **Required**: Yes

### RegistrationVersionStatusHistory
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionStatusHistory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVerifiedDestinationNumberRequest

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateVerifiedDestinationNumberResult

### VerifiedDestinationNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'VERIFIED']
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAccountDefaultProtectConfigurationResult

### DefaultProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConfigurationSetRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationSetResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestination]
- **Required**: Yes

### DefaultMessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### DefaultSenderId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultMessageFeedbackEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDefaultMessageTypeRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDefaultMessageTypeResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDefaultSenderIdRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDefaultSenderIdResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventDestinationResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteKeywordRequest

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeywordResult

### OriginationIdentityArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordMessage
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordAction
- **Type**: typing.Literal['AUTOMATIC_RESPONSE', 'OPT_IN', 'OPT_OUT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMediaMessageSpendLimitOverrideResult

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteOptOutListRequest

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptOutListResult

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteOptedOutNumberRequest

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptedOutNumberResult

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndUserOptedOut
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePoolRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePoolResult

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING']
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### TwoWayEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TwoWayChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayChannelRole
- **Type**: <class 'str'>
- **Required**: Yes

### SelfManagedOptOutsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### SharedRoutesEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProtectConfigurationRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProtectConfigurationResult

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccountDefault
- **Type**: <class 'bool'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProtectConfigurationRuleSetNumberOverrideRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProtectConfigurationRuleSetNumberOverrideResult

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRegistrationAttachmentRequest

### RegistrationAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistrationAttachmentResult

### RegistrationAttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### AttachmentStatus
- **Type**: typing.Literal['DELETED', 'UPLOAD_COMPLETE', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']
- **Required**: Yes

### AttachmentUploadErrorReason
- **Type**: typing.Literal['INTERNAL_ERROR']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRegistrationFieldValueRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### FieldPath
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistrationFieldValueResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### FieldPath
- **Type**: <class 'str'>
- **Required**: Yes

### SelectChoices
- **Type**: typing.List[str]
- **Required**: Yes

### TextValue
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRegistrationRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistrationResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationStatus
- **Type**: typing.Literal['CLOSED', 'COMPLETE', 'CREATED', 'DELETED', 'PROVISIONING', 'REQUIRES_AUTHENTICATION', 'REQUIRES_UPDATES', 'REVIEWING', 'SUBMITTED']
- **Required**: Yes

### CurrentVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ApprovedVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### LatestDeniedVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### AdditionalAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyResult

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTextMessageSpendLimitOverrideResult

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVerifiedDestinationNumberRequest

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVerifiedDestinationNumberResult

### VerifiedDestinationNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVoiceMessageSpendLimitOverrideResult

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountAttributesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAccountAttributesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeAccountAttributesResult

### AccountAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.AccountAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountLimitsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAccountLimitsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeAccountLimitsResult

### AccountLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.AccountLimit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationSetsRequest

### ConfigurationSetNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ConfigurationSetFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeConfigurationSetsRequestPaginate

### ConfigurationSetNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ConfigurationSetFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeConfigurationSetsResult

### ConfigurationSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ConfigurationSetInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeKeywordsRequest

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KeywordFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeKeywordsRequestPaginate

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KeywordFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeKeywordsResult

### OriginationIdentityArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KeywordInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOptOutListsRequest

### OptOutListNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]


# DescribeOptOutListsRequestPaginate

### OptOutListNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeOptOutListsResult

### OptOutLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OptOutListInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOptedOutNumbersRequest

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumbers
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OptedOutFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeOptedOutNumbersRequestPaginate

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumbers
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OptedOutFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeOptedOutNumbersResult

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OptedOutNumberInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePhoneNumbersRequest

### PhoneNumberIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PhoneNumberFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]


# DescribePhoneNumbersRequestPaginate

### PhoneNumberIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PhoneNumberFilter]]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribePhoneNumbersResult

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PhoneNumberInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePoolsRequest

### PoolIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]


# DescribePoolsRequestPaginate

### PoolIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolFilter]]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribePoolsResult

### Pools
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeProtectConfigurationsRequest

### ProtectConfigurationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeProtectConfigurationsRequestPaginate

### ProtectConfigurationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeProtectConfigurationsResult

### ProtectConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationAttachmentsRequest

### RegistrationAttachmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAttachmentFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationAttachmentsRequestPaginate

### RegistrationAttachmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAttachmentFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeRegistrationAttachmentsResult

### RegistrationAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAttachmentsInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationFieldDefinitionsRequest

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### SectionPath
- **Type**: typing.Optional[str]

### FieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationFieldDefinitionsRequestPaginate

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### SectionPath
- **Type**: typing.Optional[str]

### FieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeRegistrationFieldDefinitionsResult

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationFieldDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFieldDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationFieldValuesRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]

### SectionPath
- **Type**: typing.Optional[str]

### FieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationFieldValuesRequestPaginate

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]

### SectionPath
- **Type**: typing.Optional[str]

### FieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeRegistrationFieldValuesResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### RegistrationFieldValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFieldValueInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationSectionDefinitionsRequest

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### SectionPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationSectionDefinitionsRequestPaginate

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### SectionPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeRegistrationSectionDefinitionsResult

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationSectionDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationSectionDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationVersionsRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumbers
- **Type**: typing.Optional[typing.Sequence[int]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationVersionsRequestPaginate

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumbers
- **Type**: typing.Optional[typing.Sequence[int]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeRegistrationVersionsResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationinitionsRequest

### RegistrationTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationTypeFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationinitionsRequestPaginate

### RegistrationTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationTypeFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeRegistrationinitionsResult

### Registrationinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Registrationinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationsRequest

### RegistrationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationsRequestPaginate

### RegistrationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeRegistrationsResult

### Registrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSenderIdsRequest

### SenderIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdAndCountry]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]


# DescribeSenderIdsRequestPaginate

### SenderIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdAndCountry]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdFilter]]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeSenderIdsResult

### SenderIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSpendLimitsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeSpendLimitsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeSpendLimitsResult

### SpendLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SpendLimit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVerifiedDestinationNumbersRequest

### VerifiedDestinationNumberIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DestinationPhoneNumbers
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.VerifiedDestinationNumberFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeVerifiedDestinationNumbersRequestPaginate

### VerifiedDestinationNumberIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DestinationPhoneNumbers
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.VerifiedDestinationNumberFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# DescribeVerifiedDestinationNumbersResult

### VerifiedDestinationNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.VerifiedDestinationNumberInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateOriginationIdentityRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateOriginationIdentityResult

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentityArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateProtectConfigurationRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateProtectConfigurationResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# DiscardRegistrationVersionRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes


# DiscardRegistrationVersionResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### RegistrationVersionStatus
- **Type**: typing.Literal['APPROVED', 'ARCHIVED', 'DENIED', 'DISCARDED', 'DRAFT', 'REQUIRES_AUTHENTICATION', 'REVIEWING', 'REVOKED', 'SUBMITTED']
- **Required**: Yes

### RegistrationVersionStatusHistory
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionStatusHistory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# EventDestination

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MatchingEventTypes
- **Type**: typing.List[typing.Literal['ALL', 'MEDIA_ALL', 'MEDIA_BLOCKED', 'MEDIA_CARRIER_BLOCKED', 'MEDIA_CARRIER_UNREACHABLE', 'MEDIA_DELIVERED', 'MEDIA_FILE_INACCESSIBLE', 'MEDIA_FILE_SIZE_EXCEEDED', 'MEDIA_FILE_TYPE_UNSUPPORTED', 'MEDIA_INVALID', 'MEDIA_INVALID_MESSAGE', 'MEDIA_PENDING', 'MEDIA_QUEUED', 'MEDIA_SPAM', 'MEDIA_SUCCESSFUL', 'MEDIA_TTL_EXPIRED', 'MEDIA_UNKNOWN', 'MEDIA_UNREACHABLE', 'TEXT_ALL', 'TEXT_BLOCKED', 'TEXT_CARRIER_BLOCKED', 'TEXT_CARRIER_UNREACHABLE', 'TEXT_DELIVERED', 'TEXT_INVALID', 'TEXT_INVALID_MESSAGE', 'TEXT_PENDING', 'TEXT_PROTECT_BLOCKED', 'TEXT_QUEUED', 'TEXT_SENT', 'TEXT_SPAM', 'TEXT_SUCCESSFUL', 'TEXT_TTL_EXPIRED', 'TEXT_UNKNOWN', 'TEXT_UNREACHABLE', 'VOICE_ALL', 'VOICE_ANSWERED', 'VOICE_BUSY', 'VOICE_COMPLETED', 'VOICE_FAILED', 'VOICE_INITIATED', 'VOICE_NO_ANSWER', 'VOICE_RINGING', 'VOICE_TTL_EXPIRED']]
- **Required**: Yes

### CloudWatchLogsDestination
- **Type**: <class 'NoneType'>

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### SnsDestination
- **Type**: <class 'NoneType'>


# GetProtectConfigurationCountryRuleSetRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberCapability
- **Type**: typing.Literal['MMS', 'SMS', 'VOICE']
- **Required**: Yes


# GetProtectConfigurationCountryRuleSetResult

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberCapability
- **Type**: typing.Literal['MMS', 'SMS', 'VOICE']
- **Required**: Yes

### CountryRuleSet
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationCountryRuleSetInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResult

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# KeywordFilter

### Name
- **Type**: typing.Literal['keyword-action']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# KeywordInformation

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordMessage
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordAction
- **Type**: typing.Literal['AUTOMATIC_RESPONSE', 'OPT_IN', 'OPT_OUT']
- **Required**: Yes


# KinesisFirehoseDestination

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListPoolOriginationIdentitiesRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolOriginationIdentitiesFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPoolOriginationIdentitiesRequestPaginate

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolOriginationIdentitiesFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# ListPoolOriginationIdentitiesResult

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OriginationIdentityMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectConfigurationRuleSetNumberOverridesRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationRuleSetNumberOverrideFilterItem]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProtectConfigurationRuleSetNumberOverridesRequestPaginate

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationRuleSetNumberOverrideFilterItem]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# ListProtectConfigurationRuleSetNumberOverridesResult

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetNumberOverrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationRuleSetNumberOverride]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegistrationAssociationsRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAssociationFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRegistrationAssociationsRequestPaginate

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAssociationFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfig]


# ListRegistrationAssociationsResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAssociationMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResult

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# OptOutListInformation

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# OptedOutFilter

### Name
- **Type**: typing.Literal['end-user-opted-out']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# OptedOutNumberInformation

### OptedOutNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndUserOptedOut
- **Type**: <class 'bool'>
- **Required**: Yes


# OriginationIdentityMetadata

### OriginationIdentityArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### NumberCapabilities
- **Type**: typing.List[typing.Literal['MMS', 'SMS', 'VOICE']]
- **Required**: Yes

### PhoneNumber
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhoneNumberFilter

### Name
- **Type**: typing.Literal['deletion-protection-enabled', 'iso-country-code', 'message-type', 'number-capability', 'number-type', 'opt-out-list-name', 'self-managed-opt-outs-enabled', 'status', 'two-way-channel-arn', 'two-way-enabled']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PhoneNumberInformation

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ASSOCIATING', 'DELETED', 'DISASSOCIATING', 'PENDING']
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### NumberCapabilities
- **Type**: typing.List[typing.Literal['MMS', 'SMS', 'VOICE']]
- **Required**: Yes

### NumberType
- **Type**: typing.Literal['LONG_CODE', 'SHORT_CODE', 'SIMULATOR', 'TEN_DLC', 'TOLL_FREE']
- **Required**: Yes

### MonthlyLeasingPrice
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SelfManagedOptOutsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PhoneNumberId
- **Type**: typing.Optional[str]

### TwoWayChannelArn
- **Type**: typing.Optional[str]

### TwoWayChannelRole
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### RegistrationId
- **Type**: typing.Optional[str]


# PoolFilter

### Name
- **Type**: typing.Literal['deletion-protection-enabled', 'message-type', 'opt-out-list-name', 'self-managed-opt-outs-enabled', 'shared-routes-enabled', 'status', 'two-way-channel-arn', 'two-way-enabled']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PoolInformation

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING']
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### TwoWayEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SelfManagedOptOutsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### SharedRoutesEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TwoWayChannelArn
- **Type**: typing.Optional[str]

### TwoWayChannelRole
- **Type**: typing.Optional[str]


# PoolOriginationIdentitiesFilter

### Name
- **Type**: typing.Literal['iso-country-code', 'number-capability']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ProtectConfigurationCountryRuleSetInformation

### ProtectStatus
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes


# ProtectConfigurationFilter

### Name
- **Type**: typing.Literal['account-default', 'deletion-protection-enabled']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ProtectConfigurationInformation

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccountDefault
- **Type**: <class 'bool'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ProtectConfigurationRuleSetNumberOverride

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes

### IsoCountryCode
- **Type**: typing.Optional[str]

### ExpirationTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ProtectConfigurationRuleSetNumberOverrideFilterItem

### Name
- **Type**: typing.Literal['action', 'created-after', 'created-before', 'destination-phone-number-begins-with', 'expires-after', 'expires-before', 'iso-country-code']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PutKeywordRequest

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordMessage
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordAction
- **Type**: typing.Optional[typing.Literal['AUTOMATIC_RESPONSE', 'OPT_IN', 'OPT_OUT']]


# PutKeywordResult

### OriginationIdentityArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordMessage
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordAction
- **Type**: typing.Literal['AUTOMATIC_RESPONSE', 'OPT_IN', 'OPT_OUT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# PutMessageFeedbackRequest

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageFeedbackStatus
- **Type**: typing.Literal['FAILED', 'RECEIVED']
- **Required**: Yes


# PutMessageFeedbackResult

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageFeedbackStatus
- **Type**: typing.Literal['FAILED', 'RECEIVED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# PutOptedOutNumberRequest

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumber
- **Type**: <class 'str'>
- **Required**: Yes


# PutOptedOutNumberResult

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndUserOptedOut
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# PutProtectConfigurationRuleSetNumberOverrideRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ExpirationTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Timestamp]


# PutProtectConfigurationRuleSetNumberOverrideResult

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# PutRegistrationFieldValueRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### FieldPath
- **Type**: <class 'str'>
- **Required**: Yes

### SelectChoices
- **Type**: typing.Optional[typing.Sequence[str]]

### TextValue
- **Type**: typing.Optional[str]

### RegistrationAttachmentId
- **Type**: typing.Optional[str]


# PutRegistrationFieldValueResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### FieldPath
- **Type**: <class 'str'>
- **Required**: Yes

### SelectChoices
- **Type**: typing.List[str]
- **Required**: Yes

### TextValue
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyResult

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# RegistrationAssociationFilter

### Name
- **Type**: typing.Literal['iso-country-code', 'resource-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationAssociationMetadata

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]


# RegistrationAttachmentFilter

### Name
- **Type**: typing.Literal['attachment-status']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationAttachmentsInformation

### RegistrationAttachmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### AttachmentStatus
- **Type**: typing.Literal['DELETED', 'UPLOAD_COMPLETE', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AttachmentUploadErrorReason
- **Type**: typing.Optional[typing.Literal['INTERNAL_ERROR']]


# RegistrationDeniedReasonInformation

### Reason
- **Type**: <class 'str'>
- **Required**: Yes

### ShortDescription
- **Type**: <class 'str'>
- **Required**: Yes

### LongDescription
- **Type**: typing.Optional[str]

### DocumentationTitle
- **Type**: typing.Optional[str]

### DocumentationLink
- **Type**: typing.Optional[str]


# RegistrationFieldDefinition

### SectionPath
- **Type**: <class 'str'>
- **Required**: Yes

### FieldPath
- **Type**: <class 'str'>
- **Required**: Yes

### FieldType
- **Type**: typing.Literal['ATTACHMENT', 'SELECT', 'TEXT']
- **Required**: Yes

### FieldRequirement
- **Type**: typing.Literal['CONDITIONAL', 'OPTIONAL', 'REQUIRED']
- **Required**: Yes

### DisplayHints
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFieldDisplayHints'>
- **Required**: Yes

### SelectValidation
- **Type**: <class 'NoneType'>

### TextValidation
- **Type**: <class 'NoneType'>


# RegistrationFieldDisplayHints

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### ShortDescription
- **Type**: <class 'str'>
- **Required**: Yes

### LongDescription
- **Type**: typing.Optional[str]

### DocumentationTitle
- **Type**: typing.Optional[str]

### DocumentationLink
- **Type**: typing.Optional[str]

### SelectOptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SelectOptionDescription]]

### TextValidationDescription
- **Type**: typing.Optional[str]

### ExampleTextValue
- **Type**: typing.Optional[str]


# RegistrationFieldValueInformation

### FieldPath
- **Type**: <class 'str'>
- **Required**: Yes

### SelectChoices
- **Type**: typing.Optional[typing.List[str]]

### TextValue
- **Type**: typing.Optional[str]

### RegistrationAttachmentId
- **Type**: typing.Optional[str]

### DeniedReason
- **Type**: typing.Optional[str]


# RegistrationFilter

### Name
- **Type**: typing.Literal['registration-status', 'registration-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationInformation

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationStatus
- **Type**: typing.Literal['CLOSED', 'COMPLETE', 'CREATED', 'DELETED', 'PROVISIONING', 'REQUIRES_AUTHENTICATION', 'REQUIRES_UPDATES', 'REVIEWING', 'SUBMITTED']
- **Required**: Yes

### CurrentVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ApprovedVersionNumber
- **Type**: typing.Optional[int]

### LatestDeniedVersionNumber
- **Type**: typing.Optional[int]

### AdditionalAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# RegistrationSectionDefinition

### SectionPath
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayHints
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationSectionDisplayHints'>
- **Required**: Yes


# RegistrationSectionDisplayHints

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### ShortDescription
- **Type**: <class 'str'>
- **Required**: Yes

### LongDescription
- **Type**: typing.Optional[str]

### DocumentationTitle
- **Type**: typing.Optional[str]

### DocumentationLink
- **Type**: typing.Optional[str]


# RegistrationTypeDisplayHints

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### ShortDescription
- **Type**: typing.Optional[str]

### LongDescription
- **Type**: typing.Optional[str]

### DocumentationTitle
- **Type**: typing.Optional[str]

### DocumentationLink
- **Type**: typing.Optional[str]


# RegistrationTypeFilter

### Name
- **Type**: typing.Literal['supported-association-iso-country-code', 'supported-association-resource-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationVersionFilter

### Name
- **Type**: typing.Literal['registration-version-status']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationVersionInformation

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### RegistrationVersionStatus
- **Type**: typing.Literal['APPROVED', 'ARCHIVED', 'DENIED', 'DISCARDED', 'DRAFT', 'REQUIRES_AUTHENTICATION', 'REVIEWING', 'REVOKED', 'SUBMITTED']
- **Required**: Yes

### RegistrationVersionStatusHistory
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionStatusHistory'>
- **Required**: Yes

### DeniedReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationDeniedReasonInformation]]


# RegistrationVersionStatusHistory

### DraftTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SubmittedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ReviewingTimestamp
- **Type**: typing.Optional[datetime.datetime]

### RequiresAuthenticationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ApprovedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DiscardedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DeniedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### RevokedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ArchivedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# Registrationinition

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayHints
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationTypeDisplayHints'>
- **Required**: Yes

### SupportedAssociations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SupportedAssociation]]


# ReleasePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# ReleasePhoneNumberResult

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ASSOCIATING', 'DELETED', 'DISASSOCIATING', 'PENDING']
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### NumberCapabilities
- **Type**: typing.List[typing.Literal['MMS', 'SMS', 'VOICE']]
- **Required**: Yes

### NumberType
- **Type**: typing.Literal['LONG_CODE', 'SHORT_CODE', 'SIMULATOR', 'TEN_DLC', 'TOLL_FREE']
- **Required**: Yes

### MonthlyLeasingPrice
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TwoWayChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayChannelRole
- **Type**: <class 'str'>
- **Required**: Yes

### SelfManagedOptOutsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# ReleaseSenderIdRequest

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes


# ReleaseSenderIdResult

### SenderIdArn
- **Type**: <class 'str'>
- **Required**: Yes

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageTypes
- **Type**: typing.List[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]
- **Required**: Yes

### MonthlyLeasingPrice
- **Type**: <class 'str'>
- **Required**: Yes

### Registered
- **Type**: <class 'bool'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# RequestPhoneNumberRequest

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### NumberCapabilities
- **Type**: typing.Sequence[typing.Literal['MMS', 'SMS', 'VOICE']]
- **Required**: Yes

### NumberType
- **Type**: typing.Literal['LONG_CODE', 'SIMULATOR', 'TEN_DLC', 'TOLL_FREE']
- **Required**: Yes

### OptOutListName
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### RegistrationId
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# RequestPhoneNumberResult

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ASSOCIATING', 'DELETED', 'DISASSOCIATING', 'PENDING']
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### NumberCapabilities
- **Type**: typing.List[typing.Literal['MMS', 'SMS', 'VOICE']]
- **Required**: Yes

### NumberType
- **Type**: typing.Literal['LONG_CODE', 'SIMULATOR', 'TEN_DLC', 'TOLL_FREE']
- **Required**: Yes

### MonthlyLeasingPrice
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TwoWayChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayChannelRole
- **Type**: <class 'str'>
- **Required**: Yes

### SelfManagedOptOutsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# RequestSenderIdRequest

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# RequestSenderIdResult

### SenderIdArn
- **Type**: <class 'str'>
- **Required**: Yes

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageTypes
- **Type**: typing.List[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]
- **Required**: Yes

### MonthlyLeasingPrice
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Registered
- **Type**: <class 'bool'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
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


# SelectOptionDescription

### Option
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# SelectValidation

### MinChoices
- **Type**: <class 'int'>
- **Required**: Yes

### MaxChoices
- **Type**: <class 'int'>
- **Required**: Yes

### Options
- **Type**: typing.List[str]
- **Required**: Yes


# SendDestinationNumberVerificationCodeRequest

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationChannel
- **Type**: typing.Literal['TEXT', 'VOICE']
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[typing.Literal['DE_DE', 'EN_GB', 'EN_US', 'ES_419', 'ES_ES', 'FR_CA', 'FR_FR', 'IT_IT', 'JA_JP', 'KO_KR', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### OriginationIdentity
- **Type**: typing.Optional[str]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DestinationCountryParameters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['IN_ENTITY_ID', 'IN_TEMPLATE_ID'], str]]


# SendDestinationNumberVerificationCodeResult

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SendMediaMessageRequest

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### MessageBody
- **Type**: typing.Optional[str]

### MediaUrls
- **Type**: typing.Optional[typing.Sequence[str]]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### MaxPrice
- **Type**: typing.Optional[str]

### TimeToLive
- **Type**: typing.Optional[int]

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DryRun
- **Type**: typing.Optional[bool]

### ProtectConfigurationId
- **Type**: typing.Optional[str]

### MessageFeedbackEnabled
- **Type**: typing.Optional[bool]


# SendMediaMessageResult

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SendTextMessageRequest

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: typing.Optional[str]

### MessageBody
- **Type**: typing.Optional[str]

### MessageType
- **Type**: typing.Optional[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]

### Keyword
- **Type**: typing.Optional[str]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### MaxPrice
- **Type**: typing.Optional[str]

### TimeToLive
- **Type**: typing.Optional[int]

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DestinationCountryParameters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['IN_ENTITY_ID', 'IN_TEMPLATE_ID'], str]]

### DryRun
- **Type**: typing.Optional[bool]

### ProtectConfigurationId
- **Type**: typing.Optional[str]

### MessageFeedbackEnabled
- **Type**: typing.Optional[bool]


# SendTextMessageResult

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SendVoiceMessageRequest

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### MessageBody
- **Type**: typing.Optional[str]

### MessageBodyTextType
- **Type**: typing.Optional[typing.Literal['SSML', 'TEXT']]

### VoiceId
- **Type**: typing.Optional[typing.Literal['AMY', 'ASTRID', 'BIANCA', 'BRIAN', 'CAMILA', 'CARLA', 'CARMEN', 'CELINE', 'CHANTAL', 'CONCHITA', 'CRISTIANO', 'DORA', 'EMMA', 'ENRIQUE', 'EWA', 'FILIZ', 'GERAINT', 'GIORGIO', 'GWYNETH', 'HANS', 'INES', 'IVY', 'JACEK', 'JAN', 'JOANNA', 'JOEY', 'JUSTIN', 'KARL', 'KENDRA', 'KIMBERLY', 'LEA', 'LIV', 'LOTTE', 'LUCIA', 'LUPE', 'MADS', 'MAJA', 'MARLENE', 'MATHIEU', 'MATTHEW', 'MAXIM', 'MIA', 'MIGUEL', 'MIZUKI', 'NAJA', 'NICOLE', 'PENELOPE', 'RAVEENA', 'RICARDO', 'RUBEN', 'RUSSELL', 'SALLI', 'SEOYEON', 'TAKUMI', 'TATYANA', 'VICKI', 'VITORIA', 'ZEINA', 'ZHIYU']]

### ConfigurationSetName
- **Type**: typing.Optional[str]

### MaxPricePerMinute
- **Type**: typing.Optional[str]

### TimeToLive
- **Type**: typing.Optional[int]

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DryRun
- **Type**: typing.Optional[bool]

### ProtectConfigurationId
- **Type**: typing.Optional[str]

### MessageFeedbackEnabled
- **Type**: typing.Optional[bool]


# SendVoiceMessageResult

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SenderIdAndCountry

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes


# SenderIdFilter

### Name
- **Type**: typing.Literal['deletion-protection-enabled', 'iso-country-code', 'message-type', 'registered', 'sender-id']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SenderIdInformation

### SenderIdArn
- **Type**: <class 'str'>
- **Required**: Yes

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageTypes
- **Type**: typing.List[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]
- **Required**: Yes

### MonthlyLeasingPrice
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Registered
- **Type**: <class 'bool'>
- **Required**: Yes

### RegistrationId
- **Type**: typing.Optional[str]


# SetAccountDefaultProtectConfigurationRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# SetAccountDefaultProtectConfigurationResult

### DefaultProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SetDefaultMessageFeedbackEnabledRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MessageFeedbackEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SetDefaultMessageFeedbackEnabledResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MessageFeedbackEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SetDefaultMessageTypeRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes


# SetDefaultMessageTypeResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SetDefaultSenderIdRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes


# SetDefaultSenderIdResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SetMediaMessageSpendLimitOverrideRequest

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes


# SetMediaMessageSpendLimitOverrideResult

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SetTextMessageSpendLimitOverrideRequest

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes


# SetTextMessageSpendLimitOverrideResult

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SetVoiceMessageSpendLimitOverrideRequest

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes


# SetVoiceMessageSpendLimitOverrideResult

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SnsDestination

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# SpendLimit

### Name
- **Type**: typing.Literal['MEDIA_MESSAGE_MONTHLY_SPEND_LIMIT', 'TEXT_MESSAGE_MONTHLY_SPEND_LIMIT', 'VOICE_MESSAGE_MONTHLY_SPEND_LIMIT']
- **Required**: Yes

### EnforcedLimit
- **Type**: <class 'int'>
- **Required**: Yes

### MaxLimit
- **Type**: <class 'int'>
- **Required**: Yes

### Overridden
- **Type**: <class 'bool'>
- **Required**: Yes


# SubmitRegistrationVersionRequest

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitRegistrationVersionResult

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### RegistrationVersionStatus
- **Type**: typing.Literal['APPROVED', 'ARCHIVED', 'DENIED', 'DISCARDED', 'DRAFT', 'REQUIRES_AUTHENTICATION', 'REVIEWING', 'REVOKED', 'SUBMITTED']
- **Required**: Yes

### RegistrationVersionStatusHistory
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionStatusHistory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# SupportedAssociation

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationBehavior
- **Type**: typing.Literal['ASSOCIATE_AFTER_COMPLETE', 'ASSOCIATE_BEFORE_SUBMIT', 'ASSOCIATE_ON_APPROVAL']
- **Required**: Yes

### DisassociationBehavior
- **Type**: typing.Literal['DELETE_REGISTRATION_DISASSOCIATES', 'DISASSOCIATE_ALL_ALLOWS_DELETE_REGISTRATION', 'DISASSOCIATE_ALL_CLOSES_REGISTRATION']
- **Required**: Yes

### IsoCountryCode
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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.Tag]
- **Required**: Yes


# TextValidation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEventDestinationRequest

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]

### MatchingEventTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'MEDIA_ALL', 'MEDIA_BLOCKED', 'MEDIA_CARRIER_BLOCKED', 'MEDIA_CARRIER_UNREACHABLE', 'MEDIA_DELIVERED', 'MEDIA_FILE_INACCESSIBLE', 'MEDIA_FILE_SIZE_EXCEEDED', 'MEDIA_FILE_TYPE_UNSUPPORTED', 'MEDIA_INVALID', 'MEDIA_INVALID_MESSAGE', 'MEDIA_PENDING', 'MEDIA_QUEUED', 'MEDIA_SPAM', 'MEDIA_SUCCESSFUL', 'MEDIA_TTL_EXPIRED', 'MEDIA_UNKNOWN', 'MEDIA_UNREACHABLE', 'TEXT_ALL', 'TEXT_BLOCKED', 'TEXT_CARRIER_BLOCKED', 'TEXT_CARRIER_UNREACHABLE', 'TEXT_DELIVERED', 'TEXT_INVALID', 'TEXT_INVALID_MESSAGE', 'TEXT_PENDING', 'TEXT_PROTECT_BLOCKED', 'TEXT_QUEUED', 'TEXT_SENT', 'TEXT_SPAM', 'TEXT_SUCCESSFUL', 'TEXT_TTL_EXPIRED', 'TEXT_UNKNOWN', 'TEXT_UNREACHABLE', 'VOICE_ALL', 'VOICE_ANSWERED', 'VOICE_BUSY', 'VOICE_COMPLETED', 'VOICE_FAILED', 'VOICE_INITIATED', 'VOICE_NO_ANSWER', 'VOICE_RINGING', 'VOICE_TTL_EXPIRED']]]

### CloudWatchLogsDestination
- **Type**: <class 'NoneType'>

### KinesisFirehoseDestination
- **Type**: <class 'NoneType'>

### SnsDestination
- **Type**: <class 'NoneType'>


# UpdateEventDestinationResult

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayEnabled
- **Type**: typing.Optional[bool]

### TwoWayChannelArn
- **Type**: typing.Optional[str]

### TwoWayChannelRole
- **Type**: typing.Optional[str]

### SelfManagedOptOutsEnabled
- **Type**: typing.Optional[bool]

### OptOutListName
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdatePhoneNumberResult

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ASSOCIATING', 'DELETED', 'DISASSOCIATING', 'PENDING']
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### NumberCapabilities
- **Type**: typing.List[typing.Literal['MMS', 'SMS', 'VOICE']]
- **Required**: Yes

### NumberType
- **Type**: typing.Literal['LONG_CODE', 'SHORT_CODE', 'SIMULATOR', 'TEN_DLC', 'TOLL_FREE']
- **Required**: Yes

### MonthlyLeasingPrice
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TwoWayChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayChannelRole
- **Type**: <class 'str'>
- **Required**: Yes

### SelfManagedOptOutsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePoolRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayEnabled
- **Type**: typing.Optional[bool]

### TwoWayChannelArn
- **Type**: typing.Optional[str]

### TwoWayChannelRole
- **Type**: typing.Optional[str]

### SelfManagedOptOutsEnabled
- **Type**: typing.Optional[bool]

### OptOutListName
- **Type**: typing.Optional[str]

### SharedRoutesEnabled
- **Type**: typing.Optional[bool]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdatePoolResult

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING']
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes

### TwoWayEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TwoWayChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### TwoWayChannelRole
- **Type**: <class 'str'>
- **Required**: Yes

### SelfManagedOptOutsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### SharedRoutesEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProtectConfigurationCountryRuleSetRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberCapability
- **Type**: typing.Literal['MMS', 'SMS', 'VOICE']
- **Required**: Yes

### CountryRuleSetUpdates
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationCountryRuleSetInformation]
- **Required**: Yes


# UpdateProtectConfigurationCountryRuleSetResult

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberCapability
- **Type**: typing.Literal['MMS', 'SMS', 'VOICE']
- **Required**: Yes

### CountryRuleSet
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationCountryRuleSetInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProtectConfigurationRequest

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdateProtectConfigurationResult

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccountDefault
- **Type**: <class 'bool'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSenderIdRequest

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdateSenderIdResult

### SenderIdArn
- **Type**: <class 'str'>
- **Required**: Yes

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageTypes
- **Type**: typing.List[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]
- **Required**: Yes

### MonthlyLeasingPrice
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Registered
- **Type**: <class 'bool'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


# VerifiedDestinationNumberFilter

### Name
- **Type**: typing.Literal['status']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VerifiedDestinationNumberInformation

### VerifiedDestinationNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'VERIFIED']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# VerifyDestinationNumberRequest

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationCode
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyDestinationNumberResult

### VerifiedDestinationNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'VERIFIED']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadata'>
- **Required**: Yes


