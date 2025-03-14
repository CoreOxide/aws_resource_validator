# Pinpoint Sms Voice V2 Classes

# AccountAttributeTypeDef

### Name
- **Type**: typing.Literal['ACCOUNT_TIER', 'DEFAULT_PROTECT_CONFIGURATION_ID']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# AccountLimitTypeDef

### Name
- **Type**: typing.Literal['CONFIGURATION_SETS', 'OPT_OUT_LISTS', 'PHONE_NUMBERS', 'POOLS', 'REGISTRATIONS', 'REGISTRATION_ATTACHMENTS', 'SENDER_IDS', 'VERIFIED_DESTINATION_NUMBERS']
- **Required**: Yes

### Used
- **Type**: <class 'int'>
- **Required**: Yes

### Max
- **Type**: <class 'int'>
- **Required**: Yes


# AssociateOriginationIdentityRequestTypeDef

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


# AssociateOriginationIdentityResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateProtectConfigurationRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateProtectConfigurationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsDestinationTypeDef

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationSetFilterTypeDef

### Name
- **Type**: typing.Literal['default-message-feedback-enabled', 'default-message-type', 'default-sender-id', 'event-destination-name', 'matching-event-types', 'protect-configuration-id']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ConfigurationSetInformationTypeDef

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestinationTypeDef]
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


# CreateConfigurationSetRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateConfigurationSetResultTypeDef

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventDestinationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.CloudWatchLogsDestinationTypeDef]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KinesisFirehoseDestinationTypeDef]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SnsDestinationTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# CreateEventDestinationResultTypeDef

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOptOutListRequestTypeDef

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateOptOutListResultTypeDef

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePoolRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreatePoolResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProtectConfigurationRequestTypeDef

### ClientToken
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]


# CreateProtectConfigurationResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRegistrationAssociationRequestTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRegistrationAssociationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRegistrationAttachmentRequestTypeDef

### AttachmentBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.BlobTypeDef]

### AttachmentUrl
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateRegistrationAttachmentResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRegistrationRequestTypeDef

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateRegistrationResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRegistrationVersionRequestTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRegistrationVersionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionStatusHistoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVerifiedDestinationNumberRequestTypeDef

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateVerifiedDestinationNumberResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAccountDefaultProtectConfigurationResultTypeDef

### DefaultProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConfigurationSetRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationSetResultTypeDef

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestinationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDefaultMessageTypeRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDefaultMessageTypeResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDefaultSenderIdRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDefaultSenderIdResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEventDestinationRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventDestinationResultTypeDef

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteKeywordRequestTypeDef

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeywordResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMediaMessageSpendLimitOverrideResultTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteOptOutListRequestTypeDef

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptOutListResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteOptedOutNumberRequestTypeDef

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptedOutNumberResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePoolRequestTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePoolResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProtectConfigurationRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProtectConfigurationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRegistrationAttachmentRequestTypeDef

### RegistrationAttachmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistrationAttachmentResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRegistrationFieldValueRequestTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### FieldPath
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistrationFieldValueResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRegistrationRequestTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegistrationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTextMessageSpendLimitOverrideResultTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVerifiedDestinationNumberRequestTypeDef

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVerifiedDestinationNumberResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVoiceMessageSpendLimitOverrideResultTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountAttributesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeAccountAttributesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAccountAttributesResultTypeDef

### AccountAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.AccountAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountLimitsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeAccountLimitsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAccountLimitsResultTypeDef

### AccountLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.AccountLimitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationSetsRequestPaginateTypeDef

### ConfigurationSetNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ConfigurationSetFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeConfigurationSetsRequestTypeDef

### ConfigurationSetNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ConfigurationSetFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeConfigurationSetsResultTypeDef

### ConfigurationSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ConfigurationSetInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeKeywordsRequestPaginateTypeDef

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KeywordFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeKeywordsRequestTypeDef

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KeywordFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeKeywordsResultTypeDef

### OriginationIdentityArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KeywordInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOptOutListsRequestPaginateTypeDef

### OptOutListNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeOptOutListsRequestTypeDef

### OptOutListNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]


# DescribeOptOutListsResultTypeDef

### OptOutLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OptOutListInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOptedOutNumbersRequestPaginateTypeDef

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumbers
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OptedOutFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeOptedOutNumbersRequestTypeDef

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumbers
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OptedOutFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeOptedOutNumbersResultTypeDef

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OptedOutNumberInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePhoneNumbersRequestPaginateTypeDef

### PhoneNumberIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PhoneNumberFilterTypeDef]]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribePhoneNumbersRequestTypeDef

### PhoneNumberIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PhoneNumberFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]


# DescribePhoneNumbersResultTypeDef

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PhoneNumberInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePoolsRequestPaginateTypeDef

### PoolIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolFilterTypeDef]]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribePoolsRequestTypeDef

### PoolIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]


# DescribePoolsResultTypeDef

### Pools
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeProtectConfigurationsRequestPaginateTypeDef

### ProtectConfigurationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeProtectConfigurationsRequestTypeDef

### ProtectConfigurationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeProtectConfigurationsResultTypeDef

### ProtectConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationAttachmentsRequestPaginateTypeDef

### RegistrationAttachmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAttachmentFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeRegistrationAttachmentsRequestTypeDef

### RegistrationAttachmentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAttachmentFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationAttachmentsResultTypeDef

### RegistrationAttachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAttachmentsInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationFieldDefinitionsRequestPaginateTypeDef

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### SectionPath
- **Type**: typing.Optional[str]

### FieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeRegistrationFieldDefinitionsRequestTypeDef

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


# DescribeRegistrationFieldDefinitionsResultTypeDef

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationFieldDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFieldDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationFieldValuesRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeRegistrationFieldValuesRequestTypeDef

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


# DescribeRegistrationFieldValuesResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFieldValueInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationSectionDefinitionsRequestPaginateTypeDef

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### SectionPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeRegistrationSectionDefinitionsRequestTypeDef

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### SectionPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationSectionDefinitionsResultTypeDef

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationSectionDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationSectionDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationTypeDefinitionsRequestPaginateTypeDef

### RegistrationTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationTypeFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeRegistrationTypeDefinitionsRequestTypeDef

### RegistrationTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationTypeFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationTypeDefinitionsResultTypeDef

### RegistrationTypeDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationTypeDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationVersionsRequestPaginateTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumbers
- **Type**: typing.Optional[typing.Sequence[int]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeRegistrationVersionsRequestTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumbers
- **Type**: typing.Optional[typing.Sequence[int]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationVersionsResultTypeDef

### RegistrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegistrationsRequestPaginateTypeDef

### RegistrationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeRegistrationsRequestTypeDef

### RegistrationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeRegistrationsResultTypeDef

### Registrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSenderIdsRequestPaginateTypeDef

### SenderIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdAndCountryTypeDef]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdFilterTypeDef]]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeSenderIdsRequestTypeDef

### SenderIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdAndCountryTypeDef]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Owner
- **Type**: typing.Optional[typing.Literal['SELF', 'SHARED']]


# DescribeSenderIdsResultTypeDef

### SenderIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SenderIdInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSpendLimitsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeSpendLimitsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeSpendLimitsResultTypeDef

### SpendLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SpendLimitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVerifiedDestinationNumbersRequestPaginateTypeDef

### VerifiedDestinationNumberIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DestinationPhoneNumbers
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.VerifiedDestinationNumberFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# DescribeVerifiedDestinationNumbersRequestTypeDef

### VerifiedDestinationNumberIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DestinationPhoneNumbers
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.VerifiedDestinationNumberFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeVerifiedDestinationNumbersResultTypeDef

### VerifiedDestinationNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.VerifiedDestinationNumberInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateOriginationIdentityRequestTypeDef

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


# DisassociateOriginationIdentityResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateProtectConfigurationRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateProtectConfigurationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DiscardRegistrationVersionRequestTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes


# DiscardRegistrationVersionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionStatusHistoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventDestinationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.CloudWatchLogsDestinationTypeDef]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KinesisFirehoseDestinationTypeDef]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SnsDestinationTypeDef]


# GetProtectConfigurationCountryRuleSetRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberCapability
- **Type**: typing.Literal['MMS', 'SMS', 'VOICE']
- **Required**: Yes


# GetProtectConfigurationCountryRuleSetResultTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationCountryRuleSetInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KeywordFilterTypeDef

### Name
- **Type**: typing.Literal['keyword-action']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# KeywordInformationTypeDef

### Keyword
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordMessage
- **Type**: <class 'str'>
- **Required**: Yes

### KeywordAction
- **Type**: typing.Literal['AUTOMATIC_RESPONSE', 'OPT_IN', 'OPT_OUT']
- **Required**: Yes


# KinesisFirehoseDestinationTypeDef

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListPoolOriginationIdentitiesRequestPaginateTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolOriginationIdentitiesFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# ListPoolOriginationIdentitiesRequestTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PoolOriginationIdentitiesFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPoolOriginationIdentitiesResultTypeDef

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.OriginationIdentityMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectConfigurationRuleSetNumberOverridesRequestPaginateTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProtectConfigurationRuleSetNumberOverridesResultTypeDef

### ProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetNumberOverrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationRuleSetNumberOverrideTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegistrationAssociationsRequestPaginateTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAssociationFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.PaginatorConfigTypeDef]


# ListRegistrationAssociationsRequestTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAssociationFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRegistrationAssociationsResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationAssociationMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResultTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OptOutListInformationTypeDef

### OptOutListArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# OptedOutFilterTypeDef

### Name
- **Type**: typing.Literal['end-user-opted-out']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# OptedOutNumberInformationTypeDef

### OptedOutNumber
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndUserOptedOut
- **Type**: <class 'bool'>
- **Required**: Yes


# OriginationIdentityMetadataTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhoneNumberFilterTypeDef

### Name
- **Type**: typing.Literal['deletion-protection-enabled', 'iso-country-code', 'message-type', 'number-capability', 'number-type', 'opt-out-list-name', 'self-managed-opt-outs-enabled', 'status', 'two-way-channel-arn', 'two-way-enabled']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PhoneNumberInformationTypeDef

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


# PoolFilterTypeDef

### Name
- **Type**: typing.Literal['deletion-protection-enabled', 'message-type', 'opt-out-list-name', 'self-managed-opt-outs-enabled', 'shared-routes-enabled', 'status', 'two-way-channel-arn', 'two-way-enabled']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PoolInformationTypeDef

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


# PoolOriginationIdentitiesFilterTypeDef

### Name
- **Type**: typing.Literal['iso-country-code', 'number-capability']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ProtectConfigurationCountryRuleSetInformationTypeDef

### ProtectStatus
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes


# ProtectConfigurationFilterTypeDef

### Name
- **Type**: typing.Literal['account-default', 'deletion-protection-enabled']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ProtectConfigurationInformationTypeDef

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


# ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef

### Name
- **Type**: typing.Literal['action', 'created-after', 'created-before', 'destination-phone-number-begins-with', 'expires-after', 'expires-before', 'iso-country-code']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ProtectConfigurationRuleSetNumberOverrideTypeDef

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


# PutKeywordRequestTypeDef

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


# PutKeywordResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutMessageFeedbackRequestTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageFeedbackStatus
- **Type**: typing.Literal['FAILED', 'RECEIVED']
- **Required**: Yes


# PutMessageFeedbackResultTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageFeedbackStatus
- **Type**: typing.Literal['FAILED', 'RECEIVED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutOptedOutNumberRequestTypeDef

### OptOutListName
- **Type**: <class 'str'>
- **Required**: Yes

### OptedOutNumber
- **Type**: <class 'str'>
- **Required**: Yes


# PutOptedOutNumberResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TimestampTypeDef]


# PutProtectConfigurationRuleSetNumberOverrideResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRegistrationFieldValueRequestTypeDef

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


# PutRegistrationFieldValueResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegistrationAssociationFilterTypeDef

### Name
- **Type**: typing.Literal['iso-country-code', 'resource-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationAssociationMetadataTypeDef

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


# RegistrationAttachmentFilterTypeDef

### Name
- **Type**: typing.Literal['attachment-status']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationAttachmentsInformationTypeDef

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


# RegistrationDeniedReasonInformationTypeDef

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


# RegistrationFieldDefinitionTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationFieldDisplayHintsTypeDef'>
- **Required**: Yes

### SelectValidation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SelectValidationTypeDef]

### TextValidation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TextValidationTypeDef]


# RegistrationFieldDisplayHintsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SelectOptionDescriptionTypeDef]]

### TextValidationDescription
- **Type**: typing.Optional[str]

### ExampleTextValue
- **Type**: typing.Optional[str]


# RegistrationFieldValueInformationTypeDef

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


# RegistrationFilterTypeDef

### Name
- **Type**: typing.Literal['registration-status', 'registration-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationInformationTypeDef

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


# RegistrationSectionDefinitionTypeDef

### SectionPath
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayHints
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationSectionDisplayHintsTypeDef'>
- **Required**: Yes


# RegistrationSectionDisplayHintsTypeDef

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


# RegistrationTypeDefinitionTypeDef

### RegistrationType
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayHints
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationTypeDisplayHintsTypeDef'>
- **Required**: Yes

### SupportedAssociations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SupportedAssociationTypeDef]]


# RegistrationTypeDisplayHintsTypeDef

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


# RegistrationTypeFilterTypeDef

### Name
- **Type**: typing.Literal['supported-association-iso-country-code', 'supported-association-resource-type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationVersionFilterTypeDef

### Name
- **Type**: typing.Literal['registration-version-status']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegistrationVersionInformationTypeDef

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### RegistrationVersionStatus
- **Type**: typing.Literal['APPROVED', 'ARCHIVED', 'DENIED', 'DISCARDED', 'DRAFT', 'REQUIRES_AUTHENTICATION', 'REVIEWING', 'REVOKED', 'SUBMITTED']
- **Required**: Yes

### RegistrationVersionStatusHistory
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionStatusHistoryTypeDef'>
- **Required**: Yes

### DeniedReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationDeniedReasonInformationTypeDef]]


# RegistrationVersionStatusHistoryTypeDef

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


# ReleasePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# ReleasePhoneNumberResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReleaseSenderIdRequestTypeDef

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes


# ReleaseSenderIdResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RequestPhoneNumberRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# RequestPhoneNumberResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RequestSenderIdRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# RequestSenderIdResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
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


# SelectOptionDescriptionTypeDef

### Option
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# SelectValidationTypeDef

### MinChoices
- **Type**: <class 'int'>
- **Required**: Yes

### MaxChoices
- **Type**: <class 'int'>
- **Required**: Yes

### Options
- **Type**: typing.List[str]
- **Required**: Yes


# SendDestinationNumberVerificationCodeRequestTypeDef

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


# SendDestinationNumberVerificationCodeResultTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendMediaMessageRequestTypeDef

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


# SendMediaMessageResultTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendTextMessageRequestTypeDef

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


# SendTextMessageResultTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendVoiceMessageRequestTypeDef

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


# SendVoiceMessageResultTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SenderIdAndCountryTypeDef

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes


# SenderIdFilterTypeDef

### Name
- **Type**: typing.Literal['deletion-protection-enabled', 'iso-country-code', 'message-type', 'registered', 'sender-id']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SenderIdInformationTypeDef

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


# SetAccountDefaultProtectConfigurationRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# SetAccountDefaultProtectConfigurationResultTypeDef

### DefaultProtectConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetDefaultMessageFeedbackEnabledRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MessageFeedbackEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SetDefaultMessageFeedbackEnabledResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetDefaultMessageTypeRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MessageType
- **Type**: typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']
- **Required**: Yes


# SetDefaultMessageTypeResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetDefaultSenderIdRequestTypeDef

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes


# SetDefaultSenderIdResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetMediaMessageSpendLimitOverrideRequestTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes


# SetMediaMessageSpendLimitOverrideResultTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetTextMessageSpendLimitOverrideRequestTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes


# SetTextMessageSpendLimitOverrideResultTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetVoiceMessageSpendLimitOverrideRequestTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes


# SetVoiceMessageSpendLimitOverrideResultTypeDef

### MonthlyLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SnsDestinationTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# SpendLimitTypeDef

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


# SubmitRegistrationVersionRequestTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitRegistrationVersionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.RegistrationVersionStatusHistoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SupportedAssociationTypeDef

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


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TextValidationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEventDestinationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.CloudWatchLogsDestinationTypeDef]

### KinesisFirehoseDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.KinesisFirehoseDestinationTypeDef]

### SnsDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.SnsDestinationTypeDef]


# UpdateEventDestinationResultTypeDef

### ConfigurationSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSetName
- **Type**: <class 'str'>
- **Required**: Yes

### EventDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.EventDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePhoneNumberRequestTypeDef

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


# UpdatePhoneNumberResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePoolRequestTypeDef

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


# UpdatePoolResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProtectConfigurationCountryRuleSetRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberCapability
- **Type**: typing.Literal['MMS', 'SMS', 'VOICE']
- **Required**: Yes

### CountryRuleSetUpdates
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationCountryRuleSetInformationTypeDef]
- **Required**: Yes


# UpdateProtectConfigurationCountryRuleSetResultTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ProtectConfigurationCountryRuleSetInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProtectConfigurationRequestTypeDef

### ProtectConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdateProtectConfigurationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSenderIdRequestTypeDef

### SenderId
- **Type**: <class 'str'>
- **Required**: Yes

### IsoCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdateSenderIdResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifiedDestinationNumberFilterTypeDef

### Name
- **Type**: typing.Literal['status']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VerifiedDestinationNumberInformationTypeDef

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


# VerifyDestinationNumberRequestTypeDef

### VerifiedDestinationNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### VerificationCode
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyDestinationNumberResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_sms_voice_v2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


