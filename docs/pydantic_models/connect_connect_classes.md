# Connect Connect Classes

# ActionSummary

### ActionType
- **Type**: typing.Literal['ASSIGN_CONTACT_CATEGORY', 'CREATE_CASE', 'CREATE_TASK', 'END_ASSOCIATED_TASKS', 'GENERATE_EVENTBRIDGE_EVENT', 'SEND_NOTIFICATION', 'SUBMIT_AUTO_EVALUATION', 'UPDATE_CASE']
- **Required**: Yes


# ActivateEvaluationFormRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes


# ActivateEvaluationFormResponse

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# AdditionalEmailRecipients

### ToList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EmailRecipient]]

### CcList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EmailRecipient]]


# AgentConfig

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Distribution]
- **Required**: Yes


# AgentConfigOutput

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Distribution]
- **Required**: Yes


# AgentContactReference

### ContactId
- **Type**: typing.Optional[str]

### Channel
- **Type**: typing.Optional[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]

### InitiationMethod
- **Type**: typing.Optional[typing.Literal['AGENT_REPLY', 'API', 'CALLBACK', 'DISCONNECT', 'EXTERNAL_OUTBOUND', 'FLOW', 'INBOUND', 'MONITOR', 'OUTBOUND', 'QUEUE_TRANSFER', 'TRANSFER', 'WEBRTC_API']]

### AgentContactState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'CONNECTED_ONHOLD', 'CONNECTING', 'ENDED', 'ERROR', 'INCOMING', 'MISSED', 'PENDING', 'REJECTED']]

### StateStartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ConnectedToAgentTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Queue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QueueReference]


# AgentHierarchyGroup

### Arn
- **Type**: typing.Optional[str]


# AgentHierarchyGroups

### L1Ids
- **Type**: typing.Optional[typing.List[str]]

### L2Ids
- **Type**: typing.Optional[typing.List[str]]

### L3Ids
- **Type**: typing.Optional[typing.List[str]]

### L4Ids
- **Type**: typing.Optional[typing.List[str]]

### L5Ids
- **Type**: typing.Optional[typing.List[str]]


# AgentInfo

### Id
- **Type**: typing.Optional[str]

### ConnectedToAgentTimestamp
- **Type**: typing.Optional[datetime.datetime]

### AgentPauseDurationInSeconds
- **Type**: typing.Optional[int]

### HierarchyGroups
- **Type**: <class 'NoneType'>

### DeviceInfo
- **Type**: <class 'NoneType'>

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantCapabilities]


# AgentQualityMetrics

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AudioQualityMetricsInfo]


# AgentStatus

### AgentStatusARN
- **Type**: typing.Optional[str]

### AgentStatusId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'OFFLINE', 'ROUTABLE']]

### DisplayOrder
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# AgentStatusReference

### StatusStartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StatusArn
- **Type**: typing.Optional[str]

### StatusName
- **Type**: typing.Optional[str]


# AgentStatusSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# AgentStatusSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# AgentStatusSearchFilter

### AttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneAttributeFilter]


# AgentStatusSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'OFFLINE', 'ROUTABLE']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# AgentsCriteria

### AgentIds
- **Type**: typing.Optional[typing.List[str]]


# AgentsCriteriaOutput

### AgentIds
- **Type**: typing.Optional[typing.List[str]]


# AllowedCapabilities

### Customer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantCapabilities]

### Agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantCapabilities]


# AnalyticsDataAssociationResult

### DataSetId
- **Type**: typing.Optional[str]

### TargetAccountId
- **Type**: typing.Optional[str]

### ResourceShareId
- **Type**: typing.Optional[str]

### ResourceShareArn
- **Type**: typing.Optional[str]

### ResourceShareStatus
- **Type**: typing.Optional[str]


# AnalyticsDataSetsResult

### DataSetId
- **Type**: typing.Optional[str]

### DataSetName
- **Type**: typing.Optional[str]


# AnswerMachineDetectionConfig

### EnableAnswerMachineDetection
- **Type**: typing.Optional[bool]

### AwaitAnswerMachinePrompt
- **Type**: typing.Optional[bool]


# Application

### Namespace
- **Type**: typing.Optional[str]

### ApplicationPermissions
- **Type**: typing.Optional[typing.List[str]]


# ApplicationOutput

### Namespace
- **Type**: typing.Optional[str]

### ApplicationPermissions
- **Type**: typing.Optional[typing.List[str]]


# AssociateAnalyticsDataSetRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAccountId
- **Type**: typing.Optional[str]


# AssociateAnalyticsDataSetResponse

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceShareId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateApprovedOriginRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateBotRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexBot
- **Type**: <class 'NoneType'>

### LexV2Bot
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]


# AssociateDefaultVocabularyRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']
- **Required**: Yes

### VocabularyId
- **Type**: typing.Optional[str]


# AssociateFlowRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### FlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'SMS_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']
- **Required**: Yes


# AssociateInstanceStorageConfigRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes

### StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.InstanceStorageConfig'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateInstanceStorageConfigResponse

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateLambdaFunctionRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateLexBotRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexBot
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.LexBot'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociatePhoneNumberContactFlowRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateQueueQuickConnectsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectIds
- **Type**: typing.List[str]
- **Required**: Yes


# AssociateRoutingProfileQueuesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileQueueConfig]
- **Required**: Yes


# AssociateSecurityKeyRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateSecurityKeyResponse

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateTrafficDistributionGroupUserRequest

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateUserProficienciesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProficiencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.UserProficiency]
- **Required**: Yes


# AssociatedContactSummary

### ContactId
- **Type**: typing.Optional[str]

### ContactArn
- **Type**: typing.Optional[str]

### InitiationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DisconnectTimestamp
- **Type**: typing.Optional[datetime.datetime]

### InitialContactId
- **Type**: typing.Optional[str]

### PreviousContactId
- **Type**: typing.Optional[str]

### RelatedContactId
- **Type**: typing.Optional[str]

### InitiationMethod
- **Type**: typing.Optional[typing.Literal['AGENT_REPLY', 'API', 'CALLBACK', 'DISCONNECT', 'EXTERNAL_OUTBOUND', 'FLOW', 'INBOUND', 'MONITOR', 'OUTBOUND', 'QUEUE_TRANSFER', 'TRANSFER', 'WEBRTC_API']]

### Channel
- **Type**: typing.Optional[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]


# AttachedFile

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### FileArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileId
- **Type**: <class 'str'>
- **Required**: Yes

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### FileSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### FileStatus
- **Type**: typing.Literal['APPROVED', 'FAILED', 'PROCESSING', 'REJECTED']
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.CreatedByInfo]

### FileUseCaseType
- **Type**: typing.Optional[typing.Literal['ATTACHMENT', 'EMAIL_MESSAGE']]

### AssociatedResourceArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AttachedFileError

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### FileId
- **Type**: typing.Optional[str]


# AttachmentReference

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'AVAILABLE', 'DELETED', 'FAILED', 'PROCESSING', 'REJECTED']]

### Arn
- **Type**: typing.Optional[str]


# Attendee

### AttendeeId
- **Type**: typing.Optional[str]

### JoinToken
- **Type**: typing.Optional[str]


# Attribute

### AttributeType
- **Type**: typing.Optional[typing.Literal['AUTO_RESOLVE_BEST_VOICES', 'CONTACTFLOW_LOGS', 'CONTACT_LENS', 'EARLY_MEDIA', 'ENHANCED_CHAT_MONITORING', 'ENHANCED_CONTACT_MONITORING', 'HIGH_VOLUME_OUTBOUND', 'INBOUND_CALLS', 'MULTI_PARTY_CHAT_CONFERENCE', 'MULTI_PARTY_CONFERENCE', 'OUTBOUND_CALLS', 'USE_CUSTOM_TTS_VOICES']]

### Value
- **Type**: typing.Optional[str]


# AttributeAndCondition

### TagConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TagCondition]]

### HierarchyGroupCondition
- **Type**: <class 'NoneType'>


# AttributeCondition

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### ProficiencyLevel
- **Type**: typing.Optional[float]

### Range
- **Type**: <class 'NoneType'>

### MatchCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.MatchCriteria, aws_resource_validator.pydantic_models.connect.connect_classes.MatchCriteriaOutput, NoneType]

### ComparisonOperator
- **Type**: typing.Optional[str]


# AttributeConditionOutput

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### ProficiencyLevel
- **Type**: typing.Optional[float]

### Range
- **Type**: <class 'NoneType'>

### MatchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.MatchCriteriaOutput]

### ComparisonOperator
- **Type**: typing.Optional[str]


# AudioFeatures

### EchoReduction
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'UNAVAILABLE']]


# AudioQualityMetricsInfo

### QualityScore
- **Type**: typing.Optional[float]

### PotentialQualityIssues
- **Type**: typing.Optional[typing.List[str]]


# AuthenticationProfile

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### AllowedIps
- **Type**: typing.Optional[typing.List[str]]

### BlockedIps
- **Type**: typing.Optional[typing.List[str]]

### IsDefault
- **Type**: typing.Optional[bool]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]

### PeriodicSessionDuration
- **Type**: typing.Optional[int]

### MaxSessionDuration
- **Type**: typing.Optional[int]


# AuthenticationProfileSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### IsDefault
- **Type**: typing.Optional[bool]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# AvailableNumberSummary

### PhoneNumber
- **Type**: typing.Optional[str]

### PhoneNumberCountryCode
- **Type**: typing.Optional[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]

### PhoneNumberType
- **Type**: typing.Optional[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateAnalyticsDataSetRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### TargetAccountId
- **Type**: typing.Optional[str]


# BatchAssociateAnalyticsDataSetResponse

### Created
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AnalyticsDataAssociationResult]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ErrorResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateAnalyticsDataSetRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIds
- **Type**: typing.List[str]
- **Required**: Yes

### TargetAccountId
- **Type**: typing.Optional[str]


# BatchDisassociateAnalyticsDataSetResponse

### Deleted
- **Type**: typing.List[str]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ErrorResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetAttachedFileMetadataRequest

### FileIds
- **Type**: typing.List[str]
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetAttachedFileMetadataResponse

### Files
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AttachedFile]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AttachedFileError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetFlowAssociationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'VOICE_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']]


# BatchGetFlowAssociationResponse

### FlowAssociationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.FlowAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactDataRequestList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ContactDataRequest]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# BatchPutContactResponse

### SuccessfulRequestList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.SuccessfulRequest]
- **Required**: Yes

### FailedRequestList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.FailedRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# Campaign

### CampaignId
- **Type**: typing.Optional[str]


# ChatEvent

### Type
- **Type**: typing.Literal['DISCONNECT', 'EVENT', 'MESSAGE']
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]


# ChatMessage

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# ChatParticipantRoleConfig

### ParticipantTimerConfigList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantTimerConfiguration]
- **Required**: Yes


# ChatStreamingConfiguration

### StreamingEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# ClaimPhoneNumberRequest

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### PhoneNumberDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ClientToken
- **Type**: typing.Optional[str]


# ClaimPhoneNumberResponse

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# ClaimedPhoneNumberSummary

### PhoneNumberId
- **Type**: typing.Optional[str]

### PhoneNumberArn
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### PhoneNumberCountryCode
- **Type**: typing.Optional[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]

### PhoneNumberType
- **Type**: typing.Optional[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]

### PhoneNumberDescription
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PhoneNumberStatus
- **Type**: <class 'NoneType'>

### SourcePhoneNumberArn
- **Type**: typing.Optional[str]


# CommonAttributeAndCondition

### TagConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TagCondition]]


# CompleteAttachedFileUploadRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FileId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# Condition

### StringCondition
- **Type**: <class 'NoneType'>

### NumberCondition
- **Type**: <class 'NoneType'>


# ConnectionData

### Attendee
- **Type**: <class 'NoneType'>

### Meeting
- **Type**: <class 'NoneType'>


# Contact

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### InitialContactId
- **Type**: typing.Optional[str]

### PreviousContactId
- **Type**: typing.Optional[str]

### ContactAssociationId
- **Type**: typing.Optional[str]

### InitiationMethod
- **Type**: typing.Optional[typing.Literal['AGENT_REPLY', 'API', 'CALLBACK', 'DISCONNECT', 'EXTERNAL_OUTBOUND', 'FLOW', 'INBOUND', 'MONITOR', 'OUTBOUND', 'QUEUE_TRANSFER', 'TRANSFER', 'WEBRTC_API']]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Channel
- **Type**: typing.Optional[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]

### QueueInfo
- **Type**: <class 'NoneType'>

### AgentInfo
- **Type**: <class 'NoneType'>

### InitiationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DisconnectTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastPausedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastResumedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### TotalPauseCount
- **Type**: typing.Optional[int]

### TotalPauseDurationInSeconds
- **Type**: typing.Optional[int]

### ScheduledTimestamp
- **Type**: typing.Optional[datetime.datetime]

### RelatedContactId
- **Type**: typing.Optional[str]

### WisdomInfo
- **Type**: <class 'NoneType'>

### CustomerId
- **Type**: typing.Optional[str]

### CustomerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EndpointInfo]

### SystemEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EndpointInfo]

### QueueTimeAdjustmentSeconds
- **Type**: typing.Optional[int]

### QueuePriority
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ConnectedToSystemTimestamp
- **Type**: typing.Optional[datetime.datetime]

### RoutingCriteria
- **Type**: <class 'NoneType'>

### Customer
- **Type**: <class 'NoneType'>

### Campaign
- **Type**: <class 'NoneType'>

### AnsweringMachineDetectionStatus
- **Type**: typing.Optional[typing.Literal['AMD_ERROR', 'AMD_NOT_APPLICABLE', 'AMD_UNANSWERED', 'AMD_UNRESOLVED', 'ANSWERED', 'ERROR', 'FAX_MACHINE_DETECTED', 'HUMAN_ANSWERED', 'SIT_TONE_BUSY', 'SIT_TONE_DETECTED', 'SIT_TONE_INVALID_NUMBER', 'UNDETECTED', 'VOICEMAIL_BEEP', 'VOICEMAIL_NO_BEEP']]

### CustomerVoiceActivity
- **Type**: <class 'NoneType'>

### QualityMetrics
- **Type**: <class 'NoneType'>

### DisconnectDetails
- **Type**: <class 'NoneType'>

### AdditionalEmailRecipients
- **Type**: <class 'NoneType'>

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValueOutput]]


# ContactAnalysis

### Transcript
- **Type**: <class 'NoneType'>


# ContactConfiguration

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']]

### IncludeRawMessage
- **Type**: typing.Optional[bool]


# ContactDataRequest

### SystemEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.Endpoint]

### CustomerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.Endpoint]

### RequestIdentifier
- **Type**: typing.Optional[str]

### QueueId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Campaign
- **Type**: <class 'NoneType'>


# ContactFilter

### ContactStates
- **Type**: typing.Optional[typing.List[typing.Literal['CONNECTED', 'CONNECTED_ONHOLD', 'CONNECTING', 'ENDED', 'ERROR', 'INCOMING', 'MISSED', 'PENDING', 'REJECTED']]]


# ContactFlow

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### Status
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]

### Description
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### FlowContentSha256
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### VersionDescription
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# ContactFlowModule

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### Status
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ContactFlowModuleSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### StateCondition
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### StatusCondition
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowModuleSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### StateCondition
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### StatusCondition
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowModuleSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# ContactFlowModuleSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]


# ContactFlowSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### TypeCondition
- **Type**: typing.Optional[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]

### StateCondition
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### StatusCondition
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### TypeCondition
- **Type**: typing.Optional[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]

### StateCondition
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### StatusCondition
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# ContactFlowSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ContactFlowType
- **Type**: typing.Optional[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]

### ContactFlowState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### ContactFlowStatus
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowVersionSummary

### Arn
- **Type**: typing.Optional[str]

### VersionDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# ContactSearchSummary

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### InitialContactId
- **Type**: typing.Optional[str]

### PreviousContactId
- **Type**: typing.Optional[str]

### InitiationMethod
- **Type**: typing.Optional[typing.Literal['AGENT_REPLY', 'API', 'CALLBACK', 'DISCONNECT', 'EXTERNAL_OUTBOUND', 'FLOW', 'INBOUND', 'MONITOR', 'OUTBOUND', 'QUEUE_TRANSFER', 'TRANSFER', 'WEBRTC_API']]

### Channel
- **Type**: typing.Optional[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]

### QueueInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactSearchSummaryQueueInfo]

### AgentInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactSearchSummaryAgentInfo]

### InitiationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DisconnectTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ScheduledTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.ContactSearchSummarySegmentAttributeValue]]


# ContactSearchSummaryAgentInfo

### Id
- **Type**: typing.Optional[str]

### ConnectedToAgentTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ContactSearchSummaryQueueInfo

### Id
- **Type**: typing.Optional[str]

### EnqueueTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ContactSearchSummarySegmentAttributeValue

### ValueString
- **Type**: typing.Optional[str]


# ControlPlaneAttributeFilter

### OrConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.CommonAttributeAndCondition]]

### AndCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.CommonAttributeAndCondition]

### TagCondition
- **Type**: <class 'NoneType'>


# ControlPlaneTagFilter

### OrConditions
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TagCondition]]]

### AndConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TagCondition]]

### TagCondition
- **Type**: <class 'NoneType'>


# ControlPlaneUserAttributeFilter

### OrConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AttributeAndCondition]]

### AndCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AttributeAndCondition]

### TagCondition
- **Type**: <class 'NoneType'>

### HierarchyGroupCondition
- **Type**: <class 'NoneType'>


# CreateAgentStatusRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayOrder
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAgentStatusResponse

### AgentStatusARN
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCaseActionDefinition

### Fields
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.FieldValue, aws_resource_validator.pydantic_models.connect.connect_classes.FieldValueOutput]]
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCaseActionDefinitionOutput

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.FieldValueOutput]
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateContactFlowModuleRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateContactFlowModuleResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContactFlowRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateContactFlowResponse

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowContentSha256
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContactFlowVersionRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### FlowContentSha256
- **Type**: typing.Optional[str]

### ContactFlowVersion
- **Type**: typing.Optional[int]

### LastModifiedTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# CreateContactFlowVersionResponse

### ContactFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Channel
- **Type**: typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']
- **Required**: Yes

### InitiationMethod
- **Type**: typing.Literal['AGENT_REPLY', 'API', 'CALLBACK', 'DISCONNECT', 'EXTERNAL_OUTBOUND', 'FLOW', 'INBOUND', 'MONITOR', 'OUTBOUND', 'QUEUE_TRANSFER', 'TRANSFER', 'WEBRTC_API']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### RelatedContactId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.Reference]]

### ExpiryDurationInMinutes
- **Type**: typing.Optional[int]

### UserInfo
- **Type**: <class 'NoneType'>

### InitiateAs
- **Type**: typing.Optional[typing.Literal['CONNECTED_TO_USER']]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValue, aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValueOutput]]]

### PreviousContactId
- **Type**: typing.Optional[str]


# CreateContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEmailAddressRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateEmailAddressResponse

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEvaluationFormRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormItem, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormItemOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ScoringStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormScoringStrategy]

### ClientToken
- **Type**: typing.Optional[str]


# CreateEvaluationFormResponse

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHoursOfOperationOverrideRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Config
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationOverrideConfig]
- **Default**: <class 'aws_resource_validator.pydantic_models.base_validator_model.BaseValidatorModel.Config'>

### EffectiveFrom
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveTill
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateHoursOfOperationOverrideResponse

### HoursOfOperationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHoursOfOperationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeZone
- **Type**: <class 'str'>
- **Required**: Yes

### Config
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationConfig]
- **Default**: <class 'aws_resource_validator.pydantic_models.base_validator_model.BaseValidatorModel.Config'>

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateHoursOfOperationResponse

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstanceRequest

### IdentityManagementType
- **Type**: typing.Literal['CONNECT_MANAGED', 'EXISTING_DIRECTORY', 'SAML']
- **Required**: Yes

### InboundCallsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OutboundCallsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### InstanceAlias
- **Type**: typing.Optional[str]

### DirectoryId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateInstanceResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntegrationAssociationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationType
- **Type**: typing.Literal['ANALYTICS_CONNECTOR', 'APPLICATION', 'CALL_TRANSFER_CONNECTOR', 'CASES_DOMAIN', 'COGNITO_USER_POOL', 'EVENT', 'FILE_SCANNER', 'PINPOINT_APP', 'Q_MESSAGE_TEMPLATES', 'SES_IDENTITY', 'VOICE_ID', 'WISDOM_ASSISTANT', 'WISDOM_KNOWLEDGE_BASE', 'WISDOM_QUICK_RESPONSES']
- **Required**: Yes

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceApplicationUrl
- **Type**: typing.Optional[str]

### SourceApplicationName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['CASES', 'SALESFORCE', 'ZENDESK']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateIntegrationAssociationResponse

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateParticipantRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantDetailsToAdd'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateParticipantResponse

### ParticipantCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantTokenCredentials'>
- **Required**: Yes

### ParticipantId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePersistentContactAssociationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### RehydrationType
- **Type**: typing.Literal['ENTIRE_PAST_SESSION', 'FROM_SEGMENT']
- **Required**: Yes

### SourceContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreatePersistentContactAssociationResponse

### ContinuedFromContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePredefinedAttributeRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttributeValues, aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttributeValuesOutput]
- **Required**: Yes


# CreatePromptRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePromptResponse

### PromptARN
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePushNotificationRegistrationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PinpointAppArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceToken
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceType
- **Type**: typing.Literal['APNS', 'APNS_SANDBOX', 'GCM']
- **Required**: Yes

### ContactConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ContactConfiguration'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreatePushNotificationRegistrationResponse

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQueueRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OutboundCallerConfig
- **Type**: <class 'NoneType'>

### OutboundEmailConfig
- **Type**: <class 'NoneType'>

### MaxContacts
- **Type**: typing.Optional[int]

### QuickConnectIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateQueueResponse

### QueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQuickConnectRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnectConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateQuickConnectResponse

### QuickConnectARN
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRoutingProfileRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultOutboundQueueId
- **Type**: <class 'str'>
- **Required**: Yes

### MediaConcurrencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.MediaConcurrency]
- **Required**: Yes

### QueueConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileQueueConfig]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### AgentAvailabilityTimer
- **Type**: typing.Optional[typing.Literal['TIME_SINCE_LAST_ACTIVITY', 'TIME_SINCE_LAST_INBOUND']]


# CreateRoutingProfileResponse

### RoutingProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TriggerEventSource
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.RuleTriggerEventSource'>
- **Required**: Yes

### Function
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.RuleAction, aws_resource_validator.pydantic_models.connect.connect_classes.RuleActionOutput]]
- **Required**: Yes

### PublishStatus
- **Type**: typing.Literal['DRAFT', 'PUBLISHED']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateRuleResponse

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecurityProfileRequest

### SecurityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### AllowedAccessControlTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TagRestrictedResources
- **Type**: typing.Optional[typing.List[str]]

### Applications
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.Application, aws_resource_validator.pydantic_models.connect.connect_classes.ApplicationOutput]]]

### HierarchyRestrictedResources
- **Type**: typing.Optional[typing.List[str]]

### AllowedAccessControlHierarchyGroupId
- **Type**: typing.Optional[str]


# CreateSecurityProfileResponse

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTaskTemplateRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Fields
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateField, aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ContactFlowId
- **Type**: typing.Optional[str]

### SelfAssignFlowId
- **Type**: typing.Optional[str]

### Constraints
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateConstraints, aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateConstraintsOutput, NoneType]

### Defaults
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateDefaults, aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateDefaultsOutput, NoneType]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### ClientToken
- **Type**: typing.Optional[str]


# CreateTaskTemplateResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrafficDistributionGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateTrafficDistributionGroupResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUseCaseRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### UseCaseType
- **Type**: typing.Literal['CONNECT_CAMPAIGNS', 'RULES_EVALUATION']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateUseCaseResponse

### UseCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### UseCaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserHierarchyGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ParentGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateUserHierarchyGroupResponse

### HierarchyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### HierarchyGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.UserPhoneConfig'>
- **Required**: Yes

### SecurityProfileIds
- **Type**: typing.List[str]
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: typing.Optional[str]

### IdentityInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserIdentityInfo]

### DirectoryUserId
- **Type**: typing.Optional[str]

### HierarchyGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateUserResponse

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateViewRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ViewInputContent'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateViewResponse

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.View'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateViewVersionRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionDescription
- **Type**: typing.Optional[str]

### ViewContentSha256
- **Type**: typing.Optional[str]


# CreateViewVersionResponse

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.View'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVocabularyRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateVocabularyResponse

### VocabularyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VocabularyId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# CreatedByInfo

### ConnectUserArn
- **Type**: typing.Optional[str]

### AWSIdentityArn
- **Type**: typing.Optional[str]


# Credentials

### AccessToken
- **Type**: typing.Optional[str]

### AccessTokenExpiration
- **Type**: typing.Optional[datetime.datetime]

### RefreshToken
- **Type**: typing.Optional[str]

### RefreshTokenExpiration
- **Type**: typing.Optional[datetime.datetime]


# CrossChannelBehavior

### BehaviorType
- **Type**: typing.Literal['ROUTE_ANY_CHANNEL', 'ROUTE_CURRENT_CHANNEL_ONLY']
- **Required**: Yes


# CurrentMetric

### Name
- **Type**: typing.Optional[typing.Literal['AGENTS_AFTER_CONTACT_WORK', 'AGENTS_AVAILABLE', 'AGENTS_ERROR', 'AGENTS_NON_PRODUCTIVE', 'AGENTS_ONLINE', 'AGENTS_ON_CALL', 'AGENTS_ON_CONTACT', 'AGENTS_STAFFED', 'CONTACTS_IN_QUEUE', 'CONTACTS_SCHEDULED', 'OLDEST_CONTACT_AGE', 'SLOTS_ACTIVE', 'SLOTS_AVAILABLE']]

### Unit
- **Type**: typing.Optional[typing.Literal['COUNT', 'PERCENT', 'SECONDS']]


# CurrentMetricData

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.CurrentMetric]

### Value
- **Type**: typing.Optional[float]


# CurrentMetricResult

### Dimensions
- **Type**: <class 'NoneType'>

### Collections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.CurrentMetricData]]


# CurrentMetricSortCriteria

### SortByMetric
- **Type**: typing.Optional[typing.Literal['AGENTS_AFTER_CONTACT_WORK', 'AGENTS_AVAILABLE', 'AGENTS_ERROR', 'AGENTS_NON_PRODUCTIVE', 'AGENTS_ONLINE', 'AGENTS_ON_CALL', 'AGENTS_ON_CONTACT', 'AGENTS_STAFFED', 'CONTACTS_IN_QUEUE', 'CONTACTS_SCHEDULED', 'OLDEST_CONTACT_AGE', 'SLOTS_ACTIVE', 'SLOTS_AVAILABLE']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# Customer

### DeviceInfo
- **Type**: <class 'NoneType'>

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantCapabilities]


# CustomerQualityMetrics

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AudioQualityMetricsInfo]


# CustomerVoiceActivity

### GreetingStartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### GreetingEndTimestamp
- **Type**: typing.Optional[datetime.datetime]


# DateCondition

### FieldName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### ComparisonType
- **Type**: typing.Optional[typing.Literal['EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO']]


# DateReference

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# DeactivateEvaluationFormRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DeactivateEvaluationFormResponse

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DefaultVocabulary

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']
- **Required**: Yes

### VocabularyId
- **Type**: <class 'str'>
- **Required**: Yes

### VocabularyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAttachedFileRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FileId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactEvaluationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactFlowModuleRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactFlowRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactFlowVersionRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteEmailAddressRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEvaluationFormRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: typing.Optional[int]


# DeleteHoursOfOperationOverrideRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHoursOfOperationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteIntegrationAssociationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePredefinedAttributeRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePromptRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePushNotificationRegistrationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQuickConnectRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoutingProfileRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSecurityProfileRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTaskTemplateRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficDistributionGroupRequest

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUseCaseRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### UseCaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserHierarchyGroupRequest

### HierarchyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteViewRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteViewVersionRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteVocabularyRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### VocabularyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVocabularyResponse

### VocabularyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VocabularyId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAgentStatusRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgentStatusResponse

### AgentStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.AgentStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAuthenticationProfileRequest

### AuthenticationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuthenticationProfileResponse

### AuthenticationProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.AuthenticationProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContactEvaluationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactEvaluationResponse

### Evaluation
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Evaluation'>
- **Required**: Yes

### EvaluationForm
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormContent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContactFlowModuleRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactFlowModuleResponse

### ContactFlowModule
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowModule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContactFlowRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactFlowResponse

### ContactFlow
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactResponse

### Contact
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Contact'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEmailAddressRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEmailAddressResponse

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressArn
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### ModifiedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEvaluationFormRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: typing.Optional[int]


# DescribeEvaluationFormResponse

### EvaluationForm
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationForm'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHoursOfOperationOverrideRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHoursOfOperationOverrideResponse

### HoursOfOperationOverride
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationOverride'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHoursOfOperationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHoursOfOperationResponse

### HoursOfOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInstanceAttributeRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeType
- **Type**: typing.Literal['AUTO_RESOLVE_BEST_VOICES', 'CONTACTFLOW_LOGS', 'CONTACT_LENS', 'EARLY_MEDIA', 'ENHANCED_CHAT_MONITORING', 'ENHANCED_CONTACT_MONITORING', 'HIGH_VOLUME_OUTBOUND', 'INBOUND_CALLS', 'MULTI_PARTY_CHAT_CONFERENCE', 'MULTI_PARTY_CONFERENCE', 'OUTBOUND_CALLS', 'USE_CUSTOM_TTS_VOICES']
- **Required**: Yes


# DescribeInstanceAttributeResponse

### Attribute
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Attribute'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInstanceResponse

### Instance
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Instance'>
- **Required**: Yes

### ReplicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ReplicationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInstanceStorageConfigRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes


# DescribeInstanceStorageConfigResponse

### StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.InstanceStorageConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePhoneNumberResponse

### ClaimedPhoneNumberSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ClaimedPhoneNumberSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePredefinedAttributeRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePredefinedAttributeResponse

### PredefinedAttribute
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttribute'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePromptRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePromptResponse

### Prompt
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Prompt'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeQueueRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQueueResponse

### Queue
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Queue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeQuickConnectRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQuickConnectResponse

### QuickConnect
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnect'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRoutingProfileRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoutingProfileResponse

### RoutingProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRuleRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRuleResponse

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Rule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSecurityProfileRequest

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityProfileResponse

### SecurityProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.SecurityProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrafficDistributionGroupRequest

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrafficDistributionGroupResponse

### TrafficDistributionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TrafficDistributionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserHierarchyGroupRequest

### HierarchyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserHierarchyGroupResponse

### HierarchyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserHierarchyStructureRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserHierarchyStructureResponse

### HierarchyStructure
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyStructure'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserRequest

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeViewRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeViewResponse

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.View'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVocabularyRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### VocabularyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVocabularyResponse

### Vocabulary
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Vocabulary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# DeviceInfo

### PlatformName
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### OperatingSystem
- **Type**: typing.Optional[str]


# Dimensions

### Queue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QueueReference]

### Channel
- **Type**: typing.Optional[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]

### RoutingProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileReference]

### RoutingStepExpression
- **Type**: typing.Optional[str]


# DisassociateAnalyticsDataSetRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAccountId
- **Type**: typing.Optional[str]


# DisassociateApprovedOriginRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateBotRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexBot
- **Type**: <class 'NoneType'>

### LexV2Bot
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateFlowRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'SMS_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']
- **Required**: Yes


# DisassociateInstanceStorageConfigRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateLambdaFunctionRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateLexBotRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### BotName
- **Type**: <class 'str'>
- **Required**: Yes

### LexRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociatePhoneNumberContactFlowRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateQueueQuickConnectsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectIds
- **Type**: typing.List[str]
- **Required**: Yes


# DisassociateRoutingProfileQueuesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileQueueReference]
- **Required**: Yes


# DisassociateSecurityKeyRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateTrafficDistributionGroupUserRequest

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateUserProficienciesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProficiencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.UserProficiencyDisassociate]
- **Required**: Yes


# DisconnectDetails

### PotentialDisconnectIssue
- **Type**: typing.Optional[str]


# DisconnectReason

### Code
- **Type**: typing.Optional[str]


# DismissUserContactRequest

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# Distribution

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### Percentage
- **Type**: <class 'int'>
- **Required**: Yes


# DownloadUrlMetadata

### Url
- **Type**: typing.Optional[str]

### UrlExpiry
- **Type**: typing.Optional[str]


# EffectiveHoursOfOperations

### Date
- **Type**: typing.Optional[str]

### OperationalHours
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.OperationalHour]]


# EmailAddressInfo

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# EmailAddressMetadata

### EmailAddressId
- **Type**: typing.Optional[str]

### EmailAddressArn
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# EmailAddressSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# EmailAddressSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# EmailAttachment

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes


# EmailMessageReference

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# EmailRecipient

### Address
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# EmailReference

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionConfig

### EncryptionType
- **Type**: typing.Literal['KMS']
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# Endpoint

### Type
- **Type**: typing.Optional[typing.Literal['CONNECT_PHONENUMBER_ARN', 'CONTACT_FLOW', 'EMAIL_ADDRESS', 'TELEPHONE_NUMBER', 'VOIP']]

### Address
- **Type**: typing.Optional[str]


# EndpointInfo

### Type
- **Type**: typing.Optional[typing.Literal['CONNECT_PHONENUMBER_ARN', 'CONTACT_FLOW', 'EMAIL_ADDRESS', 'TELEPHONE_NUMBER', 'VOIP']]

### Address
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# ErrorResult

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# Evaluation

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationMetadata'>
- **Required**: Yes

### Answers
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationAnswerOutput]
- **Required**: Yes

### Notes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationNote]
- **Required**: Yes

### Status
- **Type**: typing.Literal['DRAFT', 'SUBMITTED']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Scores
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationScore]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EvaluationAnswerData

### StringValue
- **Type**: typing.Optional[str]

### NumericValue
- **Type**: typing.Optional[float]

### NotApplicable
- **Type**: typing.Optional[bool]


# EvaluationAnswerInput

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationAnswerData]


# EvaluationAnswerOutput

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationAnswerData]

### SystemSuggestedValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationAnswerData]


# EvaluationForm

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Locked
- **Type**: <class 'bool'>
- **Required**: Yes

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DRAFT']
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormItemOutput]
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ScoringStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormScoringStrategy]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EvaluationFormContent

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormItemOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ScoringStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormScoringStrategy]


# EvaluationFormItem

### Section
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSection, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSectionOutput, NoneType]

### Question
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormQuestion, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormQuestionOutput, NoneType]


# EvaluationFormItemOutput

### Section
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSectionOutput]

### Question
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormQuestionOutput]


# EvaluationFormNumericQuestionAutomation

### PropertyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.NumericQuestionPropertyValueAutomation]


# EvaluationFormNumericQuestionOption

### MinValue
- **Type**: <class 'int'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'int'>
- **Required**: Yes

### Score
- **Type**: typing.Optional[int]

### AutomaticFail
- **Type**: typing.Optional[bool]


# EvaluationFormNumericQuestionProperties

### MinValue
- **Type**: <class 'int'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'int'>
- **Required**: Yes

### Options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormNumericQuestionOption]]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormNumericQuestionAutomation]


# EvaluationFormNumericQuestionPropertiesOutput

### MinValue
- **Type**: <class 'int'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'int'>
- **Required**: Yes

### Options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormNumericQuestionOption]]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormNumericQuestionAutomation]


# EvaluationFormQuestion

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### RefId
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionType
- **Type**: typing.Literal['NUMERIC', 'SINGLESELECT', 'TEXT']
- **Required**: Yes

### Instructions
- **Type**: typing.Optional[str]

### NotApplicableEnabled
- **Type**: typing.Optional[bool]

### QuestionTypeProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormQuestionTypeProperties, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormQuestionTypePropertiesOutput, NoneType]

### Weight
- **Type**: typing.Optional[float]


# EvaluationFormQuestionOutput

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### RefId
- **Type**: <class 'str'>
- **Required**: Yes

### QuestionType
- **Type**: typing.Literal['NUMERIC', 'SINGLESELECT', 'TEXT']
- **Required**: Yes

### Instructions
- **Type**: typing.Optional[str]

### NotApplicableEnabled
- **Type**: typing.Optional[bool]

### QuestionTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormQuestionTypePropertiesOutput]

### Weight
- **Type**: typing.Optional[float]


# EvaluationFormQuestionTypeProperties

### Numeric
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormNumericQuestionProperties, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormNumericQuestionPropertiesOutput, NoneType]

### SingleSelect
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionProperties, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionPropertiesOutput, NoneType]


# EvaluationFormQuestionTypePropertiesOutput

### Numeric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormNumericQuestionPropertiesOutput]

### SingleSelect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionPropertiesOutput]


# EvaluationFormScoringStrategy

### Mode
- **Type**: typing.Literal['QUESTION_ONLY', 'SECTION_ONLY']
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# EvaluationFormSection

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### RefId
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes

### Instructions
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[float]


# EvaluationFormSectionOutput

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### RefId
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes

### Instructions
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[float]


# EvaluationFormSingleSelectQuestionAutomation

### Options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionAutomationOption]
- **Required**: Yes

### DefaultOptionRefId
- **Type**: typing.Optional[str]


# EvaluationFormSingleSelectQuestionAutomationOption

### RuleCategory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.SingleSelectQuestionRuleCategoryAutomation]


# EvaluationFormSingleSelectQuestionAutomationOutput

### Options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionAutomationOption]
- **Required**: Yes

### DefaultOptionRefId
- **Type**: typing.Optional[str]


# EvaluationFormSingleSelectQuestionOption

### RefId
- **Type**: <class 'str'>
- **Required**: Yes

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### Score
- **Type**: typing.Optional[int]

### AutomaticFail
- **Type**: typing.Optional[bool]


# EvaluationFormSingleSelectQuestionProperties

### Options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionOption]
- **Required**: Yes

### DisplayAs
- **Type**: typing.Optional[typing.Literal['DROPDOWN', 'RADIO']]

### Automation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionAutomation, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionAutomationOutput, NoneType]


# EvaluationFormSingleSelectQuestionPropertiesOutput

### Options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionOption]
- **Required**: Yes

### DisplayAs
- **Type**: typing.Optional[typing.Literal['DROPDOWN', 'RADIO']]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSingleSelectQuestionAutomationOutput]


# EvaluationFormSummary

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LatestVersion
- **Type**: <class 'int'>
- **Required**: Yes

### LastActivatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastActivatedBy
- **Type**: typing.Optional[str]

### ActiveVersion
- **Type**: typing.Optional[int]


# EvaluationFormVersionSummary

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Locked
- **Type**: <class 'bool'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'DRAFT']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluationMetadata

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContactAgentId
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationScore]


# EvaluationNote

### Value
- **Type**: typing.Optional[str]


# EvaluationScore

### Percentage
- **Type**: typing.Optional[float]

### NotApplicable
- **Type**: typing.Optional[bool]

### AutomaticFail
- **Type**: typing.Optional[bool]


# EvaluationSummary

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormTitle
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DRAFT', 'SUBMITTED']
- **Required**: Yes

### EvaluatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Score
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationScore]


# EventBridgeActionDefinition

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# Expiry

### DurationInSeconds
- **Type**: typing.Optional[int]

### ExpiryTimestamp
- **Type**: typing.Optional[datetime.datetime]


# Expression

### AttributeCondition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.AttributeCondition, aws_resource_validator.pydantic_models.connect.connect_classes.AttributeConditionOutput, NoneType]

### AndExpression
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### OrExpression
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### NotAttributeCondition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.AttributeCondition, aws_resource_validator.pydantic_models.connect.connect_classes.AttributeConditionOutput, NoneType]


# ExpressionOutput

### AttributeCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AttributeConditionOutput]

### AndExpression
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### OrExpression
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### NotAttributeCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AttributeConditionOutput]


# FailedRequest

### RequestIdentifier
- **Type**: typing.Optional[str]

### FailureReasonCode
- **Type**: typing.Optional[typing.Literal['IDEMPOTENCY_EXCEPTION', 'INTERNAL_ERROR', 'INVALID_ATTRIBUTE_KEY', 'INVALID_CUSTOMER_ENDPOINT', 'INVALID_QUEUE', 'INVALID_SYSTEM_ENDPOINT', 'MISSING_CAMPAIGN', 'MISSING_CUSTOMER_ENDPOINT', 'MISSING_QUEUE_ID_AND_SYSTEM_ENDPOINT', 'REQUEST_THROTTLED']]

### FailureReasonMessage
- **Type**: typing.Optional[str]


# FieldValue

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.FieldValueUnion, aws_resource_validator.pydantic_models.connect.connect_classes.FieldValueUnionOutput]
- **Required**: Yes


# FieldValueOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.FieldValueUnionOutput'>
- **Required**: Yes


# FieldValueUnion

### BooleanValue
- **Type**: typing.Optional[bool]

### DoubleValue
- **Type**: typing.Optional[float]

### EmptyValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### StringValue
- **Type**: typing.Optional[str]


# FieldValueUnionOutput

### BooleanValue
- **Type**: typing.Optional[bool]

### DoubleValue
- **Type**: typing.Optional[float]

### EmptyValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### StringValue
- **Type**: typing.Optional[str]


# FilterV2

### FilterKey
- **Type**: typing.Optional[str]

### FilterValues
- **Type**: typing.Optional[typing.List[str]]


# Filters

### Queues
- **Type**: typing.Optional[typing.List[str]]

### Channels
- **Type**: typing.Optional[typing.List[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]]

### RoutingProfiles
- **Type**: typing.Optional[typing.List[str]]

### RoutingStepExpressions
- **Type**: typing.Optional[typing.List[str]]


# FlowAssociationSummary

### ResourceId
- **Type**: typing.Optional[str]

### FlowId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'VOICE_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']]


# GetAttachedFileRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FileId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### UrlExpiryInSeconds
- **Type**: typing.Optional[int]


# GetAttachedFileResponse

### FileArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### FileStatus
- **Type**: typing.Literal['APPROVED', 'FAILED', 'PROCESSING', 'REJECTED']
- **Required**: Yes

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### FileSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileUseCaseType
- **Type**: typing.Literal['ATTACHMENT', 'EMAIL_MESSAGE']
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.CreatedByInfo'>
- **Required**: Yes

### DownloadUrlMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.DownloadUrlMetadata'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# GetContactAttributesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactAttributesResponse

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# GetCurrentMetricDataRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Filters'>
- **Required**: Yes

### CurrentMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.CurrentMetric]
- **Required**: Yes

### Groupings
- **Type**: typing.Optional[typing.List[typing.Literal['CHANNEL', 'QUEUE', 'ROUTING_PROFILE', 'ROUTING_STEP_EXPRESSION']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortCriteria
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.CurrentMetricSortCriteria]]


# GetCurrentMetricDataResponse

### MetricResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.CurrentMetricResult]
- **Required**: Yes

### DataSnapshotTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCurrentUserDataRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.UserDataFilters'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetCurrentUserDataResponse

### UserDataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.UserData]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetEffectiveHoursOfOperationsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### FromDate
- **Type**: <class 'str'>
- **Required**: Yes

### ToDate
- **Type**: <class 'str'>
- **Required**: Yes


# GetEffectiveHoursOfOperationsResponse

### EffectiveHoursOfOperationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EffectiveHoursOfOperations]
- **Required**: Yes

### TimeZone
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# GetFederationTokenRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFederationTokenResponse

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Credentials'>
- **Required**: Yes

### SignInUrl
- **Type**: <class 'str'>
- **Required**: Yes

### UserArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# GetFlowAssociationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'SMS_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']
- **Required**: Yes


# GetFlowAssociationResponse

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### FlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'SMS_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetricDataRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Filters'>
- **Required**: Yes

### HistoricalMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HistoricalMetric]
- **Required**: Yes

### Groupings
- **Type**: typing.Optional[typing.List[typing.Literal['CHANNEL', 'QUEUE', 'ROUTING_PROFILE', 'ROUTING_STEP_EXPRESSION']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetMetricDataRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Filters'>
- **Required**: Yes

### HistoricalMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HistoricalMetric]
- **Required**: Yes

### Groupings
- **Type**: typing.Optional[typing.List[typing.Literal['CHANNEL', 'QUEUE', 'ROUTING_PROFILE', 'ROUTING_STEP_EXPRESSION']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# GetMetricDataResponse

### MetricResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HistoricalMetricResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMetricDataV2Request

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.FilterV2]
- **Required**: Yes

### Metrics
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.MetricV2, aws_resource_validator.pydantic_models.connect.connect_classes.MetricV2Output]]
- **Required**: Yes

### Interval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.IntervalDetails]

### Groupings
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetMetricDataV2Response

### MetricResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.MetricResultV2]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPromptFileRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPromptFileResponse

### PromptPresignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# GetTaskTemplateRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotVersion
- **Type**: typing.Optional[str]


# GetTaskTemplateResponse

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### SelfAssignFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Constraints
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateConstraintsOutput'>
- **Required**: Yes

### Defaults
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateDefaultsOutput'>
- **Required**: Yes

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldOutput]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrafficDistributionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrafficDistributionResponse

### TelephonyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TelephonyConfigOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### SignInConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.SignInConfigOutput'>
- **Required**: Yes

### AgentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.AgentConfigOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# HierarchyGroup

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LevelId
- **Type**: typing.Optional[str]

### HierarchyPath
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# HierarchyGroupCondition

### Value
- **Type**: typing.Optional[str]

### HierarchyGroupMatchType
- **Type**: typing.Optional[typing.Literal['EXACT', 'WITH_CHILD_GROUPS']]


# HierarchyGroupSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# HierarchyGroupSummaryReference

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# HierarchyGroups

### Level1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentHierarchyGroup]

### Level2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentHierarchyGroup]

### Level3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentHierarchyGroup]

### Level4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentHierarchyGroup]

### Level5
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentHierarchyGroup]


# HierarchyLevel

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# HierarchyLevelUpdate

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# HierarchyPath

### LevelOne
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummary]

### LevelTwo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummary]

### LevelThree
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummary]

### LevelFour
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummary]

### LevelFive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummary]


# HierarchyPathReference

### LevelOne
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummaryReference]

### LevelTwo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummaryReference]

### LevelThree
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummaryReference]

### LevelFour
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummaryReference]

### LevelFive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummaryReference]


# HierarchyStructure

### LevelOne
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevel]

### LevelTwo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevel]

### LevelThree
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevel]

### LevelFour
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevel]

### LevelFive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevel]


# HierarchyStructureUpdate

### LevelOne
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevelUpdate]

### LevelTwo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevelUpdate]

### LevelThree
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevelUpdate]

### LevelFour
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevelUpdate]

### LevelFive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyLevelUpdate]


# HistoricalMetric

### Name
- **Type**: typing.Optional[typing.Literal['ABANDON_TIME', 'AFTER_CONTACT_WORK_TIME', 'API_CONTACTS_HANDLED', 'CALLBACK_CONTACTS_HANDLED', 'CONTACTS_ABANDONED', 'CONTACTS_AGENT_HUNG_UP_FIRST', 'CONTACTS_CONSULTED', 'CONTACTS_HANDLED', 'CONTACTS_HANDLED_INCOMING', 'CONTACTS_HANDLED_OUTBOUND', 'CONTACTS_HOLD_ABANDONS', 'CONTACTS_MISSED', 'CONTACTS_QUEUED', 'CONTACTS_TRANSFERRED_IN', 'CONTACTS_TRANSFERRED_IN_FROM_QUEUE', 'CONTACTS_TRANSFERRED_OUT', 'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE', 'HANDLE_TIME', 'HOLD_TIME', 'INTERACTION_AND_HOLD_TIME', 'INTERACTION_TIME', 'OCCUPANCY', 'QUEUED_TIME', 'QUEUE_ANSWER_TIME', 'SERVICE_LEVEL']]

### Threshold
- **Type**: <class 'NoneType'>

### Statistic
- **Type**: typing.Optional[typing.Literal['AVG', 'MAX', 'SUM']]

### Unit
- **Type**: typing.Optional[typing.Literal['COUNT', 'PERCENT', 'SECONDS']]


# HistoricalMetricData

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HistoricalMetric]

### Value
- **Type**: typing.Optional[float]


# HistoricalMetricResult

### Dimensions
- **Type**: <class 'NoneType'>

### Collections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HistoricalMetricData]]


# HoursOfOperation

### HoursOfOperationId
- **Type**: typing.Optional[str]

### HoursOfOperationArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### TimeZone
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationConfig]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# HoursOfOperationConfig

### Day
- **Type**: typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationTimeSlice'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationTimeSlice'>
- **Required**: Yes


# HoursOfOperationOverride

### HoursOfOperationOverrideId
- **Type**: typing.Optional[str]

### HoursOfOperationId
- **Type**: typing.Optional[str]

### HoursOfOperationArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationOverrideConfig]]

### EffectiveFrom
- **Type**: typing.Optional[str]

### EffectiveTill
- **Type**: typing.Optional[str]


# HoursOfOperationOverrideConfig

### Day
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.OverrideTimeSlice]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.OverrideTimeSlice]


# HoursOfOperationOverrideSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### DateCondition
- **Type**: <class 'NoneType'>


# HoursOfOperationOverrideSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### DateCondition
- **Type**: <class 'NoneType'>


# HoursOfOperationSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# HoursOfOperationSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# HoursOfOperationSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# HoursOfOperationSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# HoursOfOperationTimeSlice

### Hours
- **Type**: <class 'int'>
- **Required**: Yes

### Minutes
- **Type**: <class 'int'>
- **Required**: Yes


# ImportPhoneNumberRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SourcePhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ClientToken
- **Type**: typing.Optional[str]


# ImportPhoneNumberResponse

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# InboundAdditionalRecipients

### ToAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressInfo]]

### CcAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressInfo]]


# InboundEmailContent

### MessageSourceType
- **Type**: typing.Literal['RAW']
- **Required**: Yes

### RawMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.InboundRawMessage]


# InboundRawMessage

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Headers
- **Type**: typing.Optional[typing.Dict[typing.Literal['IN_REPLY_TO', 'MESSAGE_ID', 'REFERENCES', 'X_SES_SPAM_VERDICT', 'X_SES_VIRUS_VERDICT'], str]]


# Instance

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### IdentityManagementType
- **Type**: typing.Optional[typing.Literal['CONNECT_MANAGED', 'EXISTING_DIRECTORY', 'SAML']]

### InstanceAlias
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### ServiceRole
- **Type**: typing.Optional[str]

### InstanceStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS']]

### StatusReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.InstanceStatusReason]

### InboundCallsEnabled
- **Type**: typing.Optional[bool]

### OutboundCallsEnabled
- **Type**: typing.Optional[bool]

### InstanceAccessUrl
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# InstanceStatusReason

### Message
- **Type**: typing.Optional[str]


# InstanceStorageConfig

### StorageType
- **Type**: typing.Literal['KINESIS_FIREHOSE', 'KINESIS_STREAM', 'KINESIS_VIDEO_STREAM', 'S3']
- **Required**: Yes

### AssociationId
- **Type**: typing.Optional[str]

### S3Config
- **Type**: <class 'NoneType'>

### KinesisVideoStreamConfig
- **Type**: <class 'NoneType'>

### KinesisStreamConfig
- **Type**: <class 'NoneType'>

### KinesisFirehoseConfig
- **Type**: <class 'NoneType'>


# InstanceSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### IdentityManagementType
- **Type**: typing.Optional[typing.Literal['CONNECT_MANAGED', 'EXISTING_DIRECTORY', 'SAML']]

### InstanceAlias
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### ServiceRole
- **Type**: typing.Optional[str]

### InstanceStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS']]

### InboundCallsEnabled
- **Type**: typing.Optional[bool]

### OutboundCallsEnabled
- **Type**: typing.Optional[bool]

### InstanceAccessUrl
- **Type**: typing.Optional[str]


# IntegrationAssociationSummary

### IntegrationAssociationId
- **Type**: typing.Optional[str]

### IntegrationAssociationArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### IntegrationType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'APPLICATION', 'CALL_TRANSFER_CONNECTOR', 'CASES_DOMAIN', 'COGNITO_USER_POOL', 'EVENT', 'FILE_SCANNER', 'PINPOINT_APP', 'Q_MESSAGE_TEMPLATES', 'SES_IDENTITY', 'VOICE_ID', 'WISDOM_ASSISTANT', 'WISDOM_KNOWLEDGE_BASE', 'WISDOM_QUICK_RESPONSES']]

### IntegrationArn
- **Type**: typing.Optional[str]

### SourceApplicationUrl
- **Type**: typing.Optional[str]

### SourceApplicationName
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['CASES', 'SALESFORCE', 'ZENDESK']]


# IntervalDetails

### TimeZone
- **Type**: typing.Optional[str]

### IntervalPeriod
- **Type**: typing.Optional[typing.Literal['DAY', 'FIFTEEN_MIN', 'HOUR', 'THIRTY_MIN', 'TOTAL', 'WEEK']]


# InvisibleFieldInfo

### Id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldIdentifier]


# KinesisFirehoseConfig

### FirehoseArn
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamConfig

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisVideoStreamConfig

### Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriodHours
- **Type**: <class 'int'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.EncryptionConfig'>
- **Required**: Yes


# LexBot

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LexRegion
- **Type**: <class 'str'>
- **Required**: Yes


# LexBotConfig

### LexBot
- **Type**: <class 'NoneType'>

### LexV2Bot
- **Type**: <class 'NoneType'>


# LexV2Bot

### AliasArn
- **Type**: typing.Optional[str]


# ListAgentStatusRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AgentStatusTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CUSTOM', 'OFFLINE', 'ROUTABLE']]]


# ListAgentStatusRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CUSTOM', 'OFFLINE', 'ROUTABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListAgentStatusResponse

### AgentStatusSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AgentStatusSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnalyticsDataAssociationsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAnalyticsDataAssociationsResponse

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AnalyticsDataAssociationResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnalyticsDataLakeDataSetsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAnalyticsDataLakeDataSetsResponse

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AnalyticsDataSetsResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApprovedOriginsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApprovedOriginsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListApprovedOriginsResponse

### Origins
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedContactsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedContactsResponse

### ContactSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AssociatedContactSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAuthenticationProfilesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAuthenticationProfilesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListAuthenticationProfilesResponse

### AuthenticationProfileSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AuthenticationProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBotsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexVersion
- **Type**: typing.Literal['V1', 'V2']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBotsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexVersion
- **Type**: typing.Literal['V1', 'V2']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListBotsResponse

### LexBots
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.LexBotConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCondition

### TargetListType
- **Type**: typing.Optional[typing.Literal['PROFICIENCIES']]

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Condition]]


# ListContactEvaluationsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactEvaluationsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListContactEvaluationsResponse

### EvaluationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactFlowModulesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ContactFlowModuleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]


# ListContactFlowModulesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListContactFlowModulesResponse

### ContactFlowModulesSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowModuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactFlowVersionsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContactFlowVersionsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListContactFlowVersionsResponse

### ContactFlowVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactFlowsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContactFlowsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListContactFlowsResponse

### ContactFlowSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactReferencesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceTypes
- **Type**: typing.List[typing.Literal['ATTACHMENT', 'CONTACT_ANALYSIS', 'DATE', 'EMAIL', 'EMAIL_MESSAGE', 'NUMBER', 'STRING', 'URL']]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactReferencesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceTypes
- **Type**: typing.List[typing.Literal['ATTACHMENT', 'CONTACT_ANALYSIS', 'DATE', 'EMAIL', 'EMAIL_MESSAGE', 'NUMBER', 'STRING', 'URL']]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListContactReferencesResponse

### ReferenceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ReferenceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDefaultVocabulariesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDefaultVocabulariesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListDefaultVocabulariesResponse

### DefaultVocabularyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.DefaultVocabulary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEvaluationFormVersionsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEvaluationFormVersionsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListEvaluationFormVersionsResponse

### EvaluationFormVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEvaluationFormsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEvaluationFormsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListEvaluationFormsResponse

### EvaluationFormSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlowAssociationsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'VOICE_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFlowAssociationsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'VOICE_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListFlowAssociationsResponse

### FlowAssociationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.FlowAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHoursOfOperationOverridesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHoursOfOperationOverridesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListHoursOfOperationOverridesResponse

### HoursOfOperationOverrideList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationOverride]
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHoursOfOperationsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHoursOfOperationsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListHoursOfOperationsResponse

### HoursOfOperationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstanceAttributesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInstanceAttributesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListInstanceAttributesResponse

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Attribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstanceStorageConfigsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInstanceStorageConfigsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListInstanceStorageConfigsResponse

### StorageConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.InstanceStorageConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInstancesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListInstancesResponse

### InstanceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.InstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIntegrationAssociationsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'APPLICATION', 'CALL_TRANSFER_CONNECTOR', 'CASES_DOMAIN', 'COGNITO_USER_POOL', 'EVENT', 'FILE_SCANNER', 'PINPOINT_APP', 'Q_MESSAGE_TEMPLATES', 'SES_IDENTITY', 'VOICE_ID', 'WISDOM_ASSISTANT', 'WISDOM_KNOWLEDGE_BASE', 'WISDOM_QUICK_RESPONSES']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IntegrationArn
- **Type**: typing.Optional[str]


# ListIntegrationAssociationsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'APPLICATION', 'CALL_TRANSFER_CONNECTOR', 'CASES_DOMAIN', 'COGNITO_USER_POOL', 'EVENT', 'FILE_SCANNER', 'PINPOINT_APP', 'Q_MESSAGE_TEMPLATES', 'SES_IDENTITY', 'VOICE_ID', 'WISDOM_ASSISTANT', 'WISDOM_KNOWLEDGE_BASE', 'WISDOM_QUICK_RESPONSES']]

### IntegrationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListIntegrationAssociationsResponse

### IntegrationAssociationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.IntegrationAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLambdaFunctionsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLambdaFunctionsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListLambdaFunctionsResponse

### LambdaFunctions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLexBotsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLexBotsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListLexBotsResponse

### LexBots
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.LexBot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberTypes
- **Type**: typing.Optional[typing.List[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]]

### PhoneNumberCountryCodes
- **Type**: typing.Optional[typing.List[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPhoneNumbersRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberTypes
- **Type**: typing.Optional[typing.List[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]]

### PhoneNumberCountryCodes
- **Type**: typing.Optional[typing.List[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListPhoneNumbersResponse

### PhoneNumberSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.PhoneNumberSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersSummary

### PhoneNumberId
- **Type**: typing.Optional[str]

### PhoneNumberArn
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### PhoneNumberCountryCode
- **Type**: typing.Optional[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]

### PhoneNumberType
- **Type**: typing.Optional[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### PhoneNumberDescription
- **Type**: typing.Optional[str]

### SourcePhoneNumberArn
- **Type**: typing.Optional[str]


# ListPhoneNumbersV2Request

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### PhoneNumberCountryCodes
- **Type**: typing.Optional[typing.List[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### PhoneNumberTypes
- **Type**: typing.Optional[typing.List[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]]

### PhoneNumberPrefix
- **Type**: typing.Optional[str]


# ListPhoneNumbersV2RequestPaginate

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### PhoneNumberCountryCodes
- **Type**: typing.Optional[typing.List[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### PhoneNumberTypes
- **Type**: typing.Optional[typing.List[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]]

### PhoneNumberPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListPhoneNumbersV2Response

### ListPhoneNumbersSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ListPhoneNumbersSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPredefinedAttributesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPredefinedAttributesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListPredefinedAttributesResponse

### PredefinedAttributeSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttributeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPromptsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPromptsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListPromptsResponse

### PromptSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.PromptSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueueQuickConnectsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQueueQuickConnectsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListQueueQuickConnectsResponse

### QuickConnectSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnectSummary]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueuesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT', 'STANDARD']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQueuesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT', 'STANDARD']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListQueuesResponse

### QueueSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.QueueSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQuickConnectsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### QuickConnectTypes
- **Type**: typing.Optional[typing.List[typing.Literal['PHONE_NUMBER', 'QUEUE', 'USER']]]


# ListQuickConnectsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectTypes
- **Type**: typing.Optional[typing.List[typing.Literal['PHONE_NUMBER', 'QUEUE', 'USER']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListQuickConnectsResponse

### QuickConnectSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRealtimeContactAnalysisSegmentsV2Request

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputType
- **Type**: typing.Literal['Raw', 'Redacted']
- **Required**: Yes

### SegmentTypes
- **Type**: typing.List[typing.Literal['Attachments', 'Categories', 'Event', 'Issues', 'PostContactSummary', 'Transcript']]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRealtimeContactAnalysisSegmentsV2Response

### Channel
- **Type**: typing.Literal['CHAT', 'VOICE']
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### Segments
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RealtimeContactAnalysisSegment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingProfileQueuesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRoutingProfileQueuesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListRoutingProfileQueuesResponse

### RoutingProfileQueueConfigSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileQueueConfigSummary]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingProfilesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRoutingProfilesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListRoutingProfilesResponse

### RoutingProfileSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRulesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PublishStatus
- **Type**: typing.Optional[typing.Literal['DRAFT', 'PUBLISHED']]

### EventSourceName
- **Type**: typing.Optional[typing.Literal['OnCaseCreate', 'OnCaseUpdate', 'OnContactEvaluationSubmit', 'OnMetricDataUpdate', 'OnPostCallAnalysisAvailable', 'OnPostChatAnalysisAvailable', 'OnRealTimeCallAnalysisAvailable', 'OnRealTimeChatAnalysisAvailable', 'OnSalesforceCaseCreate', 'OnZendeskTicketCreate', 'OnZendeskTicketStatusUpdate']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRulesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PublishStatus
- **Type**: typing.Optional[typing.Literal['DRAFT', 'PUBLISHED']]

### EventSourceName
- **Type**: typing.Optional[typing.Literal['OnCaseCreate', 'OnCaseUpdate', 'OnContactEvaluationSubmit', 'OnMetricDataUpdate', 'OnPostCallAnalysisAvailable', 'OnPostChatAnalysisAvailable', 'OnRealTimeCallAnalysisAvailable', 'OnRealTimeChatAnalysisAvailable', 'OnSalesforceCaseCreate', 'OnZendeskTicketCreate', 'OnZendeskTicketStatusUpdate']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListRulesResponse

### RuleSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityKeysRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSecurityKeysRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListSecurityKeysResponse

### SecurityKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.SecurityKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityProfileApplicationsRequest

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSecurityProfileApplicationsRequestPaginate

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListSecurityProfileApplicationsResponse

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ApplicationOutput]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityProfilePermissionsRequest

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSecurityProfilePermissionsRequestPaginate

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListSecurityProfilePermissionsResponse

### Permissions
- **Type**: typing.List[str]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityProfilesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSecurityProfilesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListSecurityProfilesResponse

### SecurityProfileSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.SecurityProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# ListTaskTemplatesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### Name
- **Type**: typing.Optional[str]


# ListTaskTemplatesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### Name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListTaskTemplatesResponse

### TaskTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrafficDistributionGroupUsersRequest

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrafficDistributionGroupUsersRequestPaginate

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListTrafficDistributionGroupUsersResponse

### TrafficDistributionGroupUserSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TrafficDistributionGroupUserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrafficDistributionGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]


# ListTrafficDistributionGroupsRequestPaginate

### InstanceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListTrafficDistributionGroupsResponse

### TrafficDistributionGroupSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TrafficDistributionGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUseCasesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUseCasesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListUseCasesResponse

### UseCaseSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.UseCase]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserHierarchyGroupsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUserHierarchyGroupsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListUserHierarchyGroupsResponse

### UserHierarchyGroupSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserProficienciesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUserProficienciesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListUserProficienciesResponse

### UserProficiencyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.UserProficiency]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUsersRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListUsersResponse

### UserSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.UserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListViewVersionsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListViewVersionsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListViewVersionsResponse

### ViewVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ViewVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListViewsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOMER_MANAGED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListViewsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOMER_MANAGED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# ListViewsResponse

### ViewsSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ViewSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MatchCriteria

### AgentsCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.AgentsCriteria, aws_resource_validator.pydantic_models.connect.connect_classes.AgentsCriteriaOutput, NoneType]


# MatchCriteriaOutput

### AgentsCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentsCriteriaOutput]


# MediaConcurrency

### Channel
- **Type**: typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']
- **Required**: Yes

### Concurrency
- **Type**: <class 'int'>
- **Required**: Yes

### CrossChannelBehavior
- **Type**: <class 'NoneType'>


# MediaPlacement

### AudioHostUrl
- **Type**: typing.Optional[str]

### AudioFallbackUrl
- **Type**: typing.Optional[str]

### SignalingUrl
- **Type**: typing.Optional[str]

### TurnControlUrl
- **Type**: typing.Optional[str]

### EventIngestionUrl
- **Type**: typing.Optional[str]


# Meeting

### MediaRegion
- **Type**: typing.Optional[str]

### MediaPlacement
- **Type**: <class 'NoneType'>

### MeetingFeatures
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.MeetingFeaturesConfiguration]

### MeetingId
- **Type**: typing.Optional[str]


# MeetingFeaturesConfiguration

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AudioFeatures]


# MetricDataV2

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.MetricV2Output]

### Value
- **Type**: typing.Optional[float]


# MetricFilterV2

### MetricFilterKey
- **Type**: typing.Optional[str]

### MetricFilterValues
- **Type**: typing.Optional[typing.List[str]]

### Negate
- **Type**: typing.Optional[bool]


# MetricFilterV2Output

### MetricFilterKey
- **Type**: typing.Optional[str]

### MetricFilterValues
- **Type**: typing.Optional[typing.List[str]]

### Negate
- **Type**: typing.Optional[bool]


# MetricInterval

### Interval
- **Type**: typing.Optional[typing.Literal['DAY', 'FIFTEEN_MIN', 'HOUR', 'THIRTY_MIN', 'TOTAL', 'WEEK']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# MetricResultV2

### Dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### MetricInterval
- **Type**: <class 'NoneType'>

### Collections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.MetricDataV2]]


# MetricV2

### Name
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ThresholdV2]]

### MetricFilters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.MetricFilterV2, aws_resource_validator.pydantic_models.connect.connect_classes.MetricFilterV2Output]]]


# MetricV2Output

### Name
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ThresholdV2]]

### MetricFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.MetricFilterV2Output]]


# MonitorContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AllowedMonitorCapabilities
- **Type**: typing.Optional[typing.List[typing.Literal['BARGE', 'SILENT_MONITOR']]]

### ClientToken
- **Type**: typing.Optional[str]


# MonitorContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# NewSessionDetails

### SupportedMessagingContentTypes
- **Type**: typing.Optional[typing.List[str]]

### ParticipantDetails
- **Type**: <class 'NoneType'>

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### StreamingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ChatStreamingConfiguration]


# NotificationRecipientType

### UserTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserIds
- **Type**: typing.Optional[typing.List[str]]


# NotificationRecipientTypeOutput

### UserTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserIds
- **Type**: typing.Optional[typing.List[str]]


# NumberCondition

### FieldName
- **Type**: typing.Optional[str]

### MinValue
- **Type**: typing.Optional[int]

### MaxValue
- **Type**: typing.Optional[int]

### ComparisonType
- **Type**: typing.Optional[typing.Literal['EQUAL', 'GREATER', 'GREATER_OR_EQUAL', 'LESSER', 'LESSER_OR_EQUAL', 'NOT_EQUAL', 'RANGE']]


# NumberReference

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# NumericQuestionPropertyValueAutomation

### Label
- **Type**: typing.Literal['AGENT_INTERACTION_DURATION', 'CONTACT_DURATION', 'CUSTOMER_HOLD_TIME', 'NON_TALK_TIME', 'NON_TALK_TIME_PERCENTAGE', 'NUMBER_OF_INTERRUPTIONS', 'OVERALL_AGENT_SENTIMENT_SCORE', 'OVERALL_CUSTOMER_SENTIMENT_SCORE']
- **Required**: Yes


# OperationalHour

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.OverrideTimeSlice]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.OverrideTimeSlice]


# OutboundAdditionalRecipients

### CcEmailAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressInfo]]


# OutboundCallerConfig

### OutboundCallerIdName
- **Type**: typing.Optional[str]

### OutboundCallerIdNumberId
- **Type**: typing.Optional[str]

### OutboundFlowId
- **Type**: typing.Optional[str]


# OutboundEmailConfig

### OutboundEmailAddressId
- **Type**: typing.Optional[str]


# OutboundEmailContent

### MessageSourceType
- **Type**: typing.Literal['RAW', 'TEMPLATE']
- **Required**: Yes

### TemplatedMessageConfig
- **Type**: <class 'NoneType'>

### RawMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.OutboundRawMessage]


# OutboundRawMessage

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes


# OverrideTimeSlice

### Hours
- **Type**: <class 'int'>
- **Required**: Yes

### Minutes
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipantCapabilities

### Video
- **Type**: typing.Optional[typing.Literal['SEND']]

### ScreenShare
- **Type**: typing.Optional[typing.Literal['SEND']]


# ParticipantDetails

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes


# ParticipantDetailsToAdd

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']]

### DisplayName
- **Type**: typing.Optional[str]


# ParticipantTimerConfiguration

### ParticipantRole
- **Type**: typing.Literal['AGENT', 'CUSTOMER']
- **Required**: Yes

### TimerType
- **Type**: typing.Literal['DISCONNECT_NONCUSTOMER', 'IDLE']
- **Required**: Yes

### TimerValue
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantTimerValue'>
- **Required**: Yes


# ParticipantTimerValue

### ParticipantTimerAction
- **Type**: typing.Optional[typing.Literal['Unset']]

### ParticipantTimerDurationInMinutes
- **Type**: typing.Optional[int]


# ParticipantTokenCredentials

### ParticipantToken
- **Type**: typing.Optional[str]

### Expiry
- **Type**: typing.Optional[str]


# PauseContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: typing.Optional[str]


# PersistentChat

### RehydrationType
- **Type**: typing.Optional[typing.Literal['ENTIRE_PAST_SESSION', 'FROM_SEGMENT']]

### SourceContactId
- **Type**: typing.Optional[str]


# PhoneNumberQuickConnectConfig

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# PhoneNumberStatus

### Status
- **Type**: typing.Optional[typing.Literal['CLAIMED', 'FAILED', 'IN_PROGRESS']]

### Message
- **Type**: typing.Optional[str]


# PhoneNumberSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### PhoneNumberType
- **Type**: typing.Optional[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]

### PhoneNumberCountryCode
- **Type**: typing.Optional[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]


# PredefinedAttribute

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttributeValuesOutput]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# PredefinedAttributeSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# PredefinedAttributeSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# PredefinedAttributeSummary

### Name
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# PredefinedAttributeValues

### StringList
- **Type**: typing.Optional[typing.List[str]]


# PredefinedAttributeValuesOutput

### StringList
- **Type**: typing.Optional[typing.List[str]]


# Prompt

### PromptARN
- **Type**: typing.Optional[str]

### PromptId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# PromptSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# PromptSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# PromptSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# PromptSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# PutUserStatusRequest

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusId
- **Type**: <class 'str'>
- **Required**: Yes


# QualityMetrics

### Agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentQualityMetrics]

### Customer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.CustomerQualityMetrics]


# Queue

### Name
- **Type**: typing.Optional[str]

### QueueArn
- **Type**: typing.Optional[str]

### QueueId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### OutboundCallerConfig
- **Type**: <class 'NoneType'>

### OutboundEmailConfig
- **Type**: <class 'NoneType'>

### HoursOfOperationId
- **Type**: typing.Optional[str]

### MaxContacts
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# QueueInfo

### Id
- **Type**: typing.Optional[str]

### EnqueueTimestamp
- **Type**: typing.Optional[datetime.datetime]


# QueueInfoInput

### Id
- **Type**: typing.Optional[str]


# QueueQuickConnectConfig

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# QueueReference

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# QueueSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### QueueTypeCondition
- **Type**: typing.Optional[typing.Literal['STANDARD']]


# QueueSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### QueueTypeCondition
- **Type**: typing.Optional[typing.Literal['STANDARD']]


# QueueSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# QueueSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### QueueType
- **Type**: typing.Optional[typing.Literal['AGENT', 'STANDARD']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# QuickConnect

### QuickConnectARN
- **Type**: typing.Optional[str]

### QuickConnectId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### QuickConnectConfig
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# QuickConnectConfig

### QuickConnectType
- **Type**: typing.Literal['PHONE_NUMBER', 'QUEUE', 'USER']
- **Required**: Yes

### UserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserQuickConnectConfig]

### QueueConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QueueQuickConnectConfig]

### PhoneConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PhoneNumberQuickConnectConfig]


# QuickConnectSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# QuickConnectSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# QuickConnectSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# QuickConnectSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### QuickConnectType
- **Type**: typing.Optional[typing.Literal['PHONE_NUMBER', 'QUEUE', 'USER']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# Range

### MinProficiencyLevel
- **Type**: typing.Optional[float]

### MaxProficiencyLevel
- **Type**: typing.Optional[float]


# ReadOnlyFieldInfo

### Id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldIdentifier]


# RealTimeContactAnalysisAttachment

### AttachmentName
- **Type**: <class 'str'>
- **Required**: Yes

### AttachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'IN_PROGRESS', 'REJECTED']]


# RealTimeContactAnalysisCategoryDetails

### PointsOfInterest
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisPointOfInterest]
- **Required**: Yes


# RealTimeContactAnalysisCharacterInterval

### BeginOffsetChar
- **Type**: <class 'int'>
- **Required**: Yes

### EndOffsetChar
- **Type**: <class 'int'>
- **Required**: Yes


# RealTimeContactAnalysisIssueDetected

### TranscriptItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisTranscriptItemWithContent]
- **Required**: Yes


# RealTimeContactAnalysisPointOfInterest

### TranscriptItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisTranscriptItemWithCharacterOffsets]]


# RealTimeContactAnalysisSegmentAttachments

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantRole
- **Type**: typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']
- **Required**: Yes

### Attachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisAttachment]
- **Required**: Yes

### Time
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisTimeData'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# RealTimeContactAnalysisSegmentCategories

### MatchedDetails
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisCategoryDetails]
- **Required**: Yes


# RealTimeContactAnalysisSegmentEvent

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### EventType
- **Type**: <class 'str'>
- **Required**: Yes

### Time
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisTimeData'>
- **Required**: Yes

### ParticipantId
- **Type**: typing.Optional[str]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']]

### DisplayName
- **Type**: typing.Optional[str]


# RealTimeContactAnalysisSegmentIssues

### IssuesDetected
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisIssueDetected]
- **Required**: Yes


# RealTimeContactAnalysisSegmentPostContactSummary

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED']
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### FailureCode
- **Type**: typing.Optional[typing.Literal['FAILED_SAFETY_GUIDELINES', 'INSUFFICIENT_CONVERSATION_CONTENT', 'INTERNAL_ERROR', 'INVALID_ANALYSIS_CONFIGURATION', 'QUOTA_EXCEEDED']]


# RealTimeContactAnalysisSegmentTranscript

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantRole
- **Type**: typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Time
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisTimeData'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### Redaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisTranscriptItemRedaction]

### Sentiment
- **Type**: typing.Optional[typing.Literal['NEGATIVE', 'NEUTRAL', 'POSITIVE']]


# RealTimeContactAnalysisTimeData

### AbsoluteTime
- **Type**: typing.Optional[datetime.datetime]


# RealTimeContactAnalysisTranscriptItemRedaction

### CharacterOffsets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisCharacterInterval]]


# RealTimeContactAnalysisTranscriptItemWithCharacterOffsets

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CharacterOffsets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisCharacterInterval]


# RealTimeContactAnalysisTranscriptItemWithContent

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### CharacterOffsets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisCharacterInterval]


# RealtimeContactAnalysisSegment

### Transcript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisSegmentTranscript]

### Categories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisSegmentCategories]

### Issues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisSegmentIssues]

### Event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisSegmentEvent]

### Attachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisSegmentAttachments]

### PostContactSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RealTimeContactAnalysisSegmentPostContactSummary]


# Reference

### Type
- **Type**: typing.Literal['ATTACHMENT', 'CONTACT_ANALYSIS', 'DATE', 'EMAIL', 'EMAIL_MESSAGE', 'NUMBER', 'STRING', 'URL']
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'AVAILABLE', 'DELETED', 'FAILED', 'PROCESSING', 'REJECTED']]

### Arn
- **Type**: typing.Optional[str]

### StatusReason
- **Type**: typing.Optional[str]


# ReferenceSummary

### Url
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UrlReference]

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AttachmentReference]

### EmailMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EmailMessageReference]

### String
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.StringReference]

### Number
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.NumberReference]

### Date
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.DateReference]

### Email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EmailReference]


# ReleasePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# ReplicateInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicaRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicaAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# ReplicateInstanceResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# ReplicationConfiguration

### ReplicationStatusSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ReplicationStatusSummary]]

### SourceRegion
- **Type**: typing.Optional[str]

### GlobalSignInEndpoint
- **Type**: typing.Optional[str]


# ReplicationStatusSummary

### Region
- **Type**: typing.Optional[str]

### ReplicationStatus
- **Type**: typing.Optional[typing.Literal['INSTANCE_REPLICATION_COMPLETE', 'INSTANCE_REPLICATION_DELETION_FAILED', 'INSTANCE_REPLICATION_FAILED', 'INSTANCE_REPLICATION_IN_PROGRESS', 'INSTANCE_REPLICA_DELETING', 'RESOURCE_REPLICATION_NOT_STARTED']]

### ReplicationStatusReason
- **Type**: typing.Optional[str]


# RequiredFieldInfo

### Id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldIdentifier]


# ResourceTagsSearchCriteria

### TagSearchCondition
- **Type**: <class 'NoneType'>


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


# ResumeContactRecordingRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactRecordingType
- **Type**: typing.Optional[typing.Literal['AGENT', 'IVR', 'SCREEN']]


# ResumeContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: typing.Optional[str]


# RoutingCriteria

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Step]]

### ActivationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Index
- **Type**: typing.Optional[int]


# RoutingCriteriaInput

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingCriteriaInputStep]]


# RoutingCriteriaInputStep

### Expiry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingCriteriaInputStepExpiry]

### Expression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.Expression, aws_resource_validator.pydantic_models.connect.connect_classes.ExpressionOutput, NoneType]


# RoutingCriteriaInputStepExpiry

### DurationInSeconds
- **Type**: typing.Optional[int]


# RoutingProfile

### InstanceId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RoutingProfileArn
- **Type**: typing.Optional[str]

### RoutingProfileId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### MediaConcurrencies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.MediaConcurrency]]

### DefaultOutboundQueueId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### NumberOfAssociatedQueues
- **Type**: typing.Optional[int]

### NumberOfAssociatedUsers
- **Type**: typing.Optional[int]

### AgentAvailabilityTimer
- **Type**: typing.Optional[typing.Literal['TIME_SINCE_LAST_ACTIVITY', 'TIME_SINCE_LAST_INBOUND']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]

### IsDefault
- **Type**: typing.Optional[bool]

### AssociatedQueueIds
- **Type**: typing.Optional[typing.List[str]]


# RoutingProfileQueueConfig

### QueueReference
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileQueueReference'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Delay
- **Type**: <class 'int'>
- **Required**: Yes


# RoutingProfileQueueConfigSummary

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Delay
- **Type**: <class 'int'>
- **Required**: Yes

### Channel
- **Type**: typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']
- **Required**: Yes


# RoutingProfileQueueReference

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### Channel
- **Type**: typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']
- **Required**: Yes


# RoutingProfileReference

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# RoutingProfileSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# RoutingProfileSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# RoutingProfileSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# RoutingProfileSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# Rule

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TriggerEventSource
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.RuleTriggerEventSource'>
- **Required**: Yes

### Function
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RuleActionOutput]
- **Required**: Yes

### PublishStatus
- **Type**: typing.Literal['DRAFT', 'PUBLISHED']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RuleAction

### ActionType
- **Type**: typing.Literal['ASSIGN_CONTACT_CATEGORY', 'CREATE_CASE', 'CREATE_TASK', 'END_ASSOCIATED_TASKS', 'GENERATE_EVENTBRIDGE_EVENT', 'SEND_NOTIFICATION', 'SUBMIT_AUTO_EVALUATION', 'UPDATE_CASE']
- **Required**: Yes

### TaskAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.TaskActionDefinition, aws_resource_validator.pydantic_models.connect.connect_classes.TaskActionDefinitionOutput, NoneType]

### EventBridgeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EventBridgeActionDefinition]

### AssignContactCategoryAction
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SendNotificationAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.SendNotificationActionDefinition, aws_resource_validator.pydantic_models.connect.connect_classes.SendNotificationActionDefinitionOutput, NoneType]

### CreateCaseAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.CreateCaseActionDefinition, aws_resource_validator.pydantic_models.connect.connect_classes.CreateCaseActionDefinitionOutput, NoneType]

### UpdateCaseAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.UpdateCaseActionDefinition, aws_resource_validator.pydantic_models.connect.connect_classes.UpdateCaseActionDefinitionOutput, NoneType]

### EndAssociatedTasksAction
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SubmitAutoEvaluationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.SubmitAutoEvaluationActionDefinition]


# RuleActionOutput

### ActionType
- **Type**: typing.Literal['ASSIGN_CONTACT_CATEGORY', 'CREATE_CASE', 'CREATE_TASK', 'END_ASSOCIATED_TASKS', 'GENERATE_EVENTBRIDGE_EVENT', 'SEND_NOTIFICATION', 'SUBMIT_AUTO_EVALUATION', 'UPDATE_CASE']
- **Required**: Yes

### TaskAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.TaskActionDefinitionOutput]

### EventBridgeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EventBridgeActionDefinition]

### AssignContactCategoryAction
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SendNotificationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.SendNotificationActionDefinitionOutput]

### CreateCaseAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.CreateCaseActionDefinitionOutput]

### UpdateCaseAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UpdateCaseActionDefinitionOutput]

### EndAssociatedTasksAction
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SubmitAutoEvaluationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.SubmitAutoEvaluationActionDefinition]


# RuleSummary

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceName
- **Type**: typing.Literal['OnCaseCreate', 'OnCaseUpdate', 'OnContactEvaluationSubmit', 'OnMetricDataUpdate', 'OnPostCallAnalysisAvailable', 'OnPostChatAnalysisAvailable', 'OnRealTimeCallAnalysisAvailable', 'OnRealTimeChatAnalysisAvailable', 'OnSalesforceCaseCreate', 'OnZendeskTicketCreate', 'OnZendeskTicketStatusUpdate']
- **Required**: Yes

### PublishStatus
- **Type**: typing.Literal['DRAFT', 'PUBLISHED']
- **Required**: Yes

### ActionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ActionSummary]
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# RuleTriggerEventSource

### EventSourceName
- **Type**: typing.Literal['OnCaseCreate', 'OnCaseUpdate', 'OnContactEvaluationSubmit', 'OnMetricDataUpdate', 'OnPostCallAnalysisAvailable', 'OnPostChatAnalysisAvailable', 'OnRealTimeCallAnalysisAvailable', 'OnRealTimeChatAnalysisAvailable', 'OnSalesforceCaseCreate', 'OnZendeskTicketCreate', 'OnZendeskTicketStatusUpdate']
- **Required**: Yes

### IntegrationAssociationId
- **Type**: typing.Optional[str]


# S3Config

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### BucketPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'NoneType'>


# SearchAgentStatusesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentStatusSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentStatusSearchCriteria]


# SearchAgentStatusesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentStatusSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentStatusSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchAgentStatusesResponse

### AgentStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AgentStatus]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchAvailablePhoneNumbersRequest

### PhoneNumberCountryCode
- **Type**: typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']
- **Required**: Yes

### PhoneNumberType
- **Type**: typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']
- **Required**: Yes

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### PhoneNumberPrefix
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchAvailablePhoneNumbersRequestPaginate

### PhoneNumberCountryCode
- **Type**: typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']
- **Required**: Yes

### PhoneNumberType
- **Type**: typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']
- **Required**: Yes

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### PhoneNumberPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchAvailablePhoneNumbersResponse

### AvailableNumbersList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AvailableNumberSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchContactFlowModulesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowModuleSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowModuleSearchCriteria]


# SearchContactFlowModulesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowModuleSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowModuleSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchContactFlowModulesResponse

### ContactFlowModules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowModule]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchContactFlowsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowSearchCriteria]


# SearchContactFlowsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlowSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchContactFlowsResponse

### ContactFlows
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ContactFlow]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchContactsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.SearchContactsTimeRange'>
- **Required**: Yes

### SearchCriteria
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Sort
- **Type**: <class 'NoneType'>


# SearchContactsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.SearchContactsTimeRange'>
- **Required**: Yes

### SearchCriteria
- **Type**: <class 'NoneType'>

### Sort
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchContactsResponse

### Contacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ContactSearchSummary]
- **Required**: Yes

### TotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchContactsTimeRange

### Type
- **Type**: typing.Literal['CONNECTED_TO_AGENT_TIMESTAMP', 'DISCONNECT_TIMESTAMP', 'INITIATION_TIMESTAMP', 'SCHEDULED_TIMESTAMP']
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# SearchCriteria

### AgentIds
- **Type**: typing.Optional[typing.List[str]]

### AgentHierarchyGroups
- **Type**: <class 'NoneType'>

### Channels
- **Type**: typing.Optional[typing.List[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]]

### ContactAnalysis
- **Type**: <class 'NoneType'>

### InitiationMethods
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT_REPLY', 'API', 'CALLBACK', 'DISCONNECT', 'EXTERNAL_OUTBOUND', 'FLOW', 'INBOUND', 'MONITOR', 'OUTBOUND', 'QUEUE_TRANSFER', 'TRANSFER', 'WEBRTC_API']]]

### QueueIds
- **Type**: typing.Optional[typing.List[str]]

### SearchableContactAttributes
- **Type**: <class 'NoneType'>

### SearchableSegmentAttributes
- **Type**: <class 'NoneType'>


# SearchEmailAddressesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressSearchCriteria]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressSearchFilter]


# SearchEmailAddressesResponse

### EmailAddresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressMetadata]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchHoursOfOperationOverridesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationOverrideSearchCriteria]


# SearchHoursOfOperationOverridesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationOverrideSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchHoursOfOperationOverridesResponse

### HoursOfOperationOverrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationOverride]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchHoursOfOperationsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationSearchCriteria]


# SearchHoursOfOperationsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchHoursOfOperationsResponse

### HoursOfOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperation]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchPredefinedAttributesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttributeSearchCriteria]


# SearchPredefinedAttributesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttributeSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchPredefinedAttributesResponse

### PredefinedAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttribute]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchPromptsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PromptSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PromptSearchCriteria]


# SearchPromptsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PromptSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PromptSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchPromptsResponse

### Prompts
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Prompt]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchQueuesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QueueSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QueueSearchCriteria]


# SearchQueuesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QueueSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QueueSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchQueuesResponse

### Queues
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Queue]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchQuickConnectsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnectSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnectSearchCriteria]


# SearchQuickConnectsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnectSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnectSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchQuickConnectsResponse

### QuickConnects
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnect]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchResourceTagsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ResourceTagsSearchCriteria]


# SearchResourceTagsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ResourceTagsSearchCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchResourceTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TagSet]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchRoutingProfilesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileSearchCriteria]


# SearchRoutingProfilesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchRoutingProfilesResponse

### RoutingProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfile]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchSecurityProfilesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.SecurityProfileSearchCriteria]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.SecurityProfilesSearchFilter]


# SearchSecurityProfilesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.SecurityProfileSearchCriteriaPaginator]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.SecurityProfilesSearchFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchSecurityProfilesResponse

### SecurityProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.SecurityProfileSearchSummary]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchUserHierarchyGroupsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserHierarchyGroupSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserHierarchyGroupSearchCriteria]


# SearchUserHierarchyGroupsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserHierarchyGroupSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserHierarchyGroupSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchUserHierarchyGroupsResponse

### UserHierarchyGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyGroup]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchUsersRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserSearchCriteria]


# SearchUsersRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserSearchFilter]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserSearchCriteriaPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.UserSearchSummary]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchVocabulariesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS', 'DELETE_IN_PROGRESS']]

### NameStartsWith
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']]


# SearchVocabulariesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS', 'DELETE_IN_PROGRESS']]

### NameStartsWith
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.PaginatorConfig]


# SearchVocabulariesResponse

### VocabularySummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.VocabularySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchableContactAttributes

### Criteria
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.SearchableContactAttributesCriteria]
- **Required**: Yes

### MatchType
- **Type**: typing.Optional[typing.Literal['MATCH_ALL', 'MATCH_ANY']]


# SearchableContactAttributesCriteria

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# SearchableSegmentAttributes

### Criteria
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.SearchableSegmentAttributesCriteria]
- **Required**: Yes

### MatchType
- **Type**: typing.Optional[typing.Literal['MATCH_ALL', 'MATCH_ANY']]


# SearchableSegmentAttributesCriteria

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# SecurityKey

### AssociationId
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# SecurityProfile

### Id
- **Type**: typing.Optional[str]

### OrganizationResourceId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### SecurityProfileName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### AllowedAccessControlTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TagRestrictedResources
- **Type**: typing.Optional[typing.List[str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]

### HierarchyRestrictedResources
- **Type**: typing.Optional[typing.List[str]]

### AllowedAccessControlHierarchyGroupId
- **Type**: typing.Optional[str]


# SecurityProfileSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# SecurityProfileSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# SecurityProfileSearchSummary

### Id
- **Type**: typing.Optional[str]

### OrganizationResourceId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### SecurityProfileName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SecurityProfileSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# SecurityProfilesSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]


# SegmentAttributeValue

### ValueString
- **Type**: typing.Optional[str]

### ValueMap
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### ValueInteger
- **Type**: typing.Optional[int]


# SegmentAttributeValueOutput

### ValueString
- **Type**: typing.Optional[str]

### ValueMap
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### ValueInteger
- **Type**: typing.Optional[int]


# SendChatIntegrationEventRequest

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ChatEvent'>
- **Required**: Yes

### Subtype
- **Type**: typing.Optional[str]

### NewSessionDetails
- **Type**: <class 'NoneType'>


# SendChatIntegrationEventResponse

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NewChatCreated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# SendNotificationActionDefinition

### DeliveryMethod
- **Type**: typing.Literal['EMAIL']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Literal['PLAIN_TEXT']
- **Required**: Yes

### Recipient
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.NotificationRecipientType, aws_resource_validator.pydantic_models.connect.connect_classes.NotificationRecipientTypeOutput]
- **Required**: Yes

### Subject
- **Type**: typing.Optional[str]


# SendNotificationActionDefinitionOutput

### DeliveryMethod
- **Type**: typing.Literal['EMAIL']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Literal['PLAIN_TEXT']
- **Required**: Yes

### Recipient
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.NotificationRecipientTypeOutput'>
- **Required**: Yes

### Subject
- **Type**: typing.Optional[str]


# SendOutboundEmailRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressInfo'>
- **Required**: Yes

### DestinationEmailAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressInfo'>
- **Required**: Yes

### EmailMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.OutboundEmailContent'>
- **Required**: Yes

### TrafficType
- **Type**: typing.Literal['CAMPAIGN', 'GENERAL']
- **Required**: Yes

### AdditionalRecipients
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.OutboundAdditionalRecipients]

### SourceCampaign
- **Type**: <class 'NoneType'>

### ClientToken
- **Type**: typing.Optional[str]


# SignInConfig

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.SignInDistribution]
- **Required**: Yes


# SignInConfigOutput

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.SignInDistribution]
- **Required**: Yes


# SignInDistribution

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SingleSelectQuestionRuleCategoryAutomation

### Category
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['NOT_PRESENT', 'PRESENT']
- **Required**: Yes

### OptionRefId
- **Type**: <class 'str'>
- **Required**: Yes


# Sort

### FieldName
- **Type**: typing.Literal['CHANNEL', 'CONNECTED_TO_AGENT_TIMESTAMP', 'DISCONNECT_TIMESTAMP', 'INITIATION_METHOD', 'INITIATION_TIMESTAMP', 'SCHEDULED_TIMESTAMP']
- **Required**: Yes

### Order
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# SourceCampaign

### CampaignId
- **Type**: typing.Optional[str]

### OutboundRequestId
- **Type**: typing.Optional[str]


# StartAttachedFileUploadRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### FileSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### FileUseCaseType
- **Type**: typing.Literal['ATTACHMENT', 'EMAIL_MESSAGE']
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### UrlExpiryInSeconds
- **Type**: typing.Optional[int]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.CreatedByInfo]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartAttachedFileUploadResponse

### FileArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### FileStatus
- **Type**: typing.Literal['APPROVED', 'FAILED', 'PROCESSING', 'REJECTED']
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.CreatedByInfo'>
- **Required**: Yes

### UploadUrlMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.UploadUrlMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartChatContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantDetails'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### InitialMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ChatMessage]

### ClientToken
- **Type**: typing.Optional[str]

### ChatDurationInMinutes
- **Type**: typing.Optional[int]

### SupportedMessagingContentTypes
- **Type**: typing.Optional[typing.List[str]]

### PersistentChat
- **Type**: <class 'NoneType'>

### RelatedContactId
- **Type**: typing.Optional[str]

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValue, aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValueOutput]]]

### CustomerId
- **Type**: typing.Optional[str]


# StartChatContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantToken
- **Type**: <class 'str'>
- **Required**: Yes

### ContinuedFromContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartContactEvaluationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# StartContactEvaluationResponse

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartContactRecordingRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceRecordingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.VoiceRecordingConfiguration'>
- **Required**: Yes


# StartContactStreamingRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ChatStreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ChatStreamingConfiguration'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartContactStreamingResponse

### StreamingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartEmailContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressInfo'>
- **Required**: Yes

### DestinationEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### EmailMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.InboundEmailContent'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.Reference]]

### Name
- **Type**: typing.Optional[str]

### AdditionalRecipients
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.InboundAdditionalRecipients]

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.EmailAttachment]]

### ContactFlowId
- **Type**: typing.Optional[str]

### RelatedContactId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValue, aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValueOutput]]]

### ClientToken
- **Type**: typing.Optional[str]


# StartEmailContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartOutboundChatContactRequest

### SourceEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Endpoint'>
- **Required**: Yes

### DestinationEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.Endpoint'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentAttributes
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValue, aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValueOutput]]
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### ChatDurationInMinutes
- **Type**: typing.Optional[int]

### ParticipantDetails
- **Type**: <class 'NoneType'>

### InitialSystemMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ChatMessage]

### RelatedContactId
- **Type**: typing.Optional[str]

### SupportedMessagingContentTypes
- **Type**: typing.Optional[typing.List[str]]

### ClientToken
- **Type**: typing.Optional[str]


# StartOutboundChatContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartOutboundEmailContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationEmailAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressInfo'>
- **Required**: Yes

### EmailMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.OutboundEmailContent'>
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EmailAddressInfo]

### AdditionalRecipients
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.OutboundAdditionalRecipients]

### ClientToken
- **Type**: typing.Optional[str]


# StartOutboundEmailContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartOutboundVoiceContactRequest

### DestinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.Reference]]

### RelatedContactId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### SourcePhoneNumber
- **Type**: typing.Optional[str]

### QueueId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### AnswerMachineDetectionConfig
- **Type**: <class 'NoneType'>

### CampaignId
- **Type**: typing.Optional[str]

### TrafficType
- **Type**: typing.Optional[typing.Literal['CAMPAIGN', 'GENERAL']]


# StartOutboundVoiceContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartScreenSharingRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# StartTaskContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PreviousContactId
- **Type**: typing.Optional[str]

### ContactFlowId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.Reference]]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### ScheduledTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### TaskTemplateId
- **Type**: typing.Optional[str]

### QuickConnectId
- **Type**: typing.Optional[str]

### RelatedContactId
- **Type**: typing.Optional[str]

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValue, aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValueOutput]]]


# StartTaskContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# StartWebRTCContactRequest

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ParticipantDetails'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### ClientToken
- **Type**: typing.Optional[str]

### AllowedCapabilities
- **Type**: <class 'NoneType'>

### RelatedContactId
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.Reference]]

### Description
- **Type**: typing.Optional[str]


# StartWebRTCContactResponse

### ConnectionData
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ConnectionData'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# Step

### Expiry
- **Type**: <class 'NoneType'>

### Expression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ExpressionOutput]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'EXPIRED', 'INACTIVE', 'JOINED']]


# StopContactRecordingRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactRecordingType
- **Type**: typing.Optional[typing.Literal['AGENT', 'IVR', 'SCREEN']]


# StopContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DisconnectReason
- **Type**: <class 'NoneType'>


# StopContactStreamingRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingId
- **Type**: <class 'str'>
- **Required**: Yes


# StringCondition

### FieldName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### ComparisonType
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT', 'STARTS_WITH']]


# StringReference

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# SubmitAutoEvaluationActionDefinition

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitContactEvaluationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### Answers
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationAnswerInput]]

### Notes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationNote]]


# SubmitContactEvaluationResponse

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# SuccessfulRequest

### RequestIdentifier
- **Type**: typing.Optional[str]

### ContactId
- **Type**: typing.Optional[str]


# SuspendContactRecordingRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactRecordingType
- **Type**: typing.Optional[typing.Literal['AGENT', 'IVR', 'SCREEN']]


# TagCondition

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]


# TagContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagSearchCondition

### tagKey
- **Type**: typing.Optional[str]

### tagValue
- **Type**: typing.Optional[str]

### tagKeyComparisonType
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT', 'STARTS_WITH']]

### tagValueComparisonType
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT', 'STARTS_WITH']]


# TagSet

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TaskActionDefinition

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.Reference]]


# TaskActionDefinitionOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.Reference]]


# TaskTemplateConstraints

### RequiredFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RequiredFieldInfo]]

### ReadOnlyFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ReadOnlyFieldInfo]]

### InvisibleFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.InvisibleFieldInfo]]


# TaskTemplateConstraintsOutput

### RequiredFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RequiredFieldInfo]]

### ReadOnlyFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.ReadOnlyFieldInfo]]

### InvisibleFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.InvisibleFieldInfo]]


# TaskTemplateDefaultFieldValue

### Id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldIdentifier]

### DefaultValue
- **Type**: typing.Optional[str]


# TaskTemplateDefaults

### DefaultFieldValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateDefaultFieldValue]]


# TaskTemplateDefaultsOutput

### DefaultFieldValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateDefaultFieldValue]]


# TaskTemplateField

### Id
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldIdentifier'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['BOOLEAN', 'DATE_TIME', 'DESCRIPTION', 'EMAIL', 'EXPIRY_DURATION', 'NAME', 'NUMBER', 'QUICK_CONNECT', 'SCHEDULED_TIME', 'SELF_ASSIGN', 'SINGLE_SELECT', 'TEXT', 'TEXT_AREA', 'URL']]

### SingleSelectOptions
- **Type**: typing.Optional[typing.List[str]]


# TaskTemplateFieldIdentifier

### Name
- **Type**: typing.Optional[str]


# TaskTemplateFieldOutput

### Id
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldIdentifier'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['BOOLEAN', 'DATE_TIME', 'DESCRIPTION', 'EMAIL', 'EXPIRY_DURATION', 'NAME', 'NUMBER', 'QUICK_CONNECT', 'SCHEDULED_TIME', 'SELF_ASSIGN', 'SINGLE_SELECT', 'TEXT', 'TEXT_AREA', 'URL']]

### SingleSelectOptions
- **Type**: typing.Optional[typing.List[str]]


# TaskTemplateMetadata

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# TelephonyConfig

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Distribution]
- **Required**: Yes


# TelephonyConfigOutput

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.Distribution]
- **Required**: Yes


# TemplateAttributes

### CustomAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### CustomerProfileAttributes
- **Type**: typing.Optional[str]


# TemplatedMessageConfig

### KnowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TemplateAttributes'>
- **Required**: Yes


# Threshold

### Comparison
- **Type**: typing.Optional[typing.Literal['LT']]

### ThresholdValue
- **Type**: typing.Optional[float]


# ThresholdV2

### Comparison
- **Type**: typing.Optional[str]

### ThresholdValue
- **Type**: typing.Optional[float]


# TrafficDistributionGroup

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS', 'DELETION_FAILED', 'PENDING_DELETION', 'UPDATE_IN_PROGRESS']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### IsDefault
- **Type**: typing.Optional[bool]


# TrafficDistributionGroupSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS', 'DELETION_FAILED', 'PENDING_DELETION', 'UPDATE_IN_PROGRESS']]

### IsDefault
- **Type**: typing.Optional[bool]


# TrafficDistributionGroupUserSummary

### UserId
- **Type**: typing.Optional[str]


# Transcript

### Criteria
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TranscriptCriteria]
- **Required**: Yes

### MatchType
- **Type**: typing.Optional[typing.Literal['MATCH_ALL', 'MATCH_ANY']]


# TranscriptCriteria

### ParticipantRole
- **Type**: typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']
- **Required**: Yes

### SearchText
- **Type**: typing.List[str]
- **Required**: Yes

### MatchType
- **Type**: typing.Literal['MATCH_ALL', 'MATCH_ANY']
- **Required**: Yes


# TransferContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# TransferContactResponse

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# UntagContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAgentStatusRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DisplayOrder
- **Type**: typing.Optional[int]

### ResetOrderNumber
- **Type**: typing.Optional[bool]


# UpdateAuthenticationProfileRequest

### AuthenticationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### AllowedIps
- **Type**: typing.Optional[typing.List[str]]

### BlockedIps
- **Type**: typing.Optional[typing.List[str]]

### PeriodicSessionDuration
- **Type**: typing.Optional[int]


# UpdateCaseActionDefinition

### Fields
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.FieldValue, aws_resource_validator.pydantic_models.connect.connect_classes.FieldValueOutput]]
- **Required**: Yes


# UpdateCaseActionDefinitionOutput

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.FieldValueOutput]
- **Required**: Yes


# UpdateContactAttributesRequest

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UpdateContactEvaluationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### Answers
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationAnswerInput]]

### Notes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationNote]]


# UpdateContactEvaluationResponse

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContactFlowContentRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateContactFlowMetadataRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ContactFlowState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]


# UpdateContactFlowModuleContentRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateContactFlowModuleMetadataRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]


# UpdateContactFlowNameRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateContactRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect.connect_classes.Reference]]

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValue, aws_resource_validator.pydantic_models.connect.connect_classes.SegmentAttributeValueOutput]]]

### QueueInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.QueueInfoInput]

### UserInfo
- **Type**: <class 'NoneType'>

### CustomerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.Endpoint]

### SystemEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.Endpoint]


# UpdateContactRoutingDataRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueTimeAdjustmentSeconds
- **Type**: typing.Optional[int]

### QueuePriority
- **Type**: typing.Optional[int]

### RoutingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingCriteriaInput]


# UpdateContactScheduleRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# UpdateEmailAddressMetadataRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# UpdateEmailAddressMetadataResponse

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEvaluationFormRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormItem, aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormItemOutput]]
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### ScoringStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.EvaluationFormScoringStrategy]

### ClientToken
- **Type**: typing.Optional[str]


# UpdateEvaluationFormResponse

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateHoursOfOperationOverrideRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationOverrideConfig]]

### EffectiveFrom
- **Type**: typing.Optional[str]

### EffectiveTill
- **Type**: typing.Optional[str]


# UpdateHoursOfOperationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### TimeZone
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.HoursOfOperationConfig]]


# UpdateInstanceAttributeRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeType
- **Type**: typing.Literal['AUTO_RESOLVE_BEST_VOICES', 'CONTACTFLOW_LOGS', 'CONTACT_LENS', 'EARLY_MEDIA', 'ENHANCED_CHAT_MONITORING', 'ENHANCED_CONTACT_MONITORING', 'HIGH_VOLUME_OUTBOUND', 'INBOUND_CALLS', 'MULTI_PARTY_CHAT_CONFERENCE', 'MULTI_PARTY_CONFERENCE', 'OUTBOUND_CALLS', 'USE_CUSTOM_TTS_VOICES']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# UpdateInstanceStorageConfigRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes

### StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.InstanceStorageConfig'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# UpdateParticipantAuthenticationRequest

### State
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[str]

### ErrorDescription
- **Type**: typing.Optional[str]


# UpdateParticipantRoleConfigChannelInfo

### Chat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ChatParticipantRoleConfig]


# UpdateParticipantRoleConfigRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.UpdateParticipantRoleConfigChannelInfo'>
- **Required**: Yes


# UpdatePhoneNumberMetadataRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberDescription
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# UpdatePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# UpdatePhoneNumberResponse

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePredefinedAttributeRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttributeValues, aws_resource_validator.pydantic_models.connect.connect_classes.PredefinedAttributeValuesOutput, NoneType]


# UpdatePromptRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### S3Uri
- **Type**: typing.Optional[str]


# UpdatePromptResponse

### PromptARN
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQueueHoursOfOperationRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateQueueMaxContactsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxContacts
- **Type**: typing.Optional[int]


# UpdateQueueNameRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateQueueOutboundCallerConfigRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### OutboundCallerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.OutboundCallerConfig'>
- **Required**: Yes


# UpdateQueueOutboundEmailConfigRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### OutboundEmailConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.OutboundEmailConfig'>
- **Required**: Yes


# UpdateQueueStatusRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateQuickConnectConfigRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.QuickConnectConfig'>
- **Required**: Yes


# UpdateQuickConnectNameRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateRoutingProfileAgentAvailabilityTimerRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentAvailabilityTimer
- **Type**: typing.Literal['TIME_SINCE_LAST_ACTIVITY', 'TIME_SINCE_LAST_INBOUND']
- **Required**: Yes


# UpdateRoutingProfileConcurrencyRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### MediaConcurrencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.MediaConcurrency]
- **Required**: Yes


# UpdateRoutingProfileDefaultOutboundQueueRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultOutboundQueueId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoutingProfileNameRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateRoutingProfileQueuesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileQueueConfig]
- **Required**: Yes


# UpdateRuleRequest

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Function
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.RuleAction, aws_resource_validator.pydantic_models.connect.connect_classes.RuleActionOutput]]
- **Required**: Yes

### PublishStatus
- **Type**: typing.Literal['DRAFT', 'PUBLISHED']
- **Required**: Yes


# UpdateSecurityProfileRequest

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[str]]

### AllowedAccessControlTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TagRestrictedResources
- **Type**: typing.Optional[typing.List[str]]

### Applications
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.Application, aws_resource_validator.pydantic_models.connect.connect_classes.ApplicationOutput]]]

### HierarchyRestrictedResources
- **Type**: typing.Optional[typing.List[str]]

### AllowedAccessControlHierarchyGroupId
- **Type**: typing.Optional[str]


# UpdateTaskTemplateRequest

### TaskTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ContactFlowId
- **Type**: typing.Optional[str]

### SelfAssignFlowId
- **Type**: typing.Optional[str]

### Constraints
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateConstraints, aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateConstraintsOutput, NoneType]

### Defaults
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateDefaults, aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateDefaultsOutput, NoneType]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### Fields
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateField, aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldOutput]]]


# UpdateTaskTemplateResponse

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### SelfAssignFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Constraints
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateConstraintsOutput'>
- **Required**: Yes

### Defaults
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateDefaultsOutput'>
- **Required**: Yes

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.TaskTemplateFieldOutput]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrafficDistributionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### TelephonyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.TelephonyConfig, aws_resource_validator.pydantic_models.connect.connect_classes.TelephonyConfigOutput, NoneType]

### SignInConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.SignInConfig, aws_resource_validator.pydantic_models.connect.connect_classes.SignInConfigOutput, NoneType]

### AgentConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connect.connect_classes.AgentConfig, aws_resource_validator.pydantic_models.connect.connect_classes.AgentConfigOutput, NoneType]


# UpdateUserHierarchyGroupNameRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HierarchyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserHierarchyRequest

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HierarchyGroupId
- **Type**: typing.Optional[str]


# UpdateUserHierarchyStructureRequest

### HierarchyStructure
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyStructureUpdate'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserIdentityInfoRequest

### IdentityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.UserIdentityInfo'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserPhoneConfigRequest

### PhoneConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.UserPhoneConfig'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserProficienciesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProficiencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.UserProficiency]
- **Required**: Yes


# UpdateUserRoutingProfileRequest

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserSecurityProfilesRequest

### SecurityProfileIds
- **Type**: typing.List[str]
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateViewContentRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ViewInputContent'>
- **Required**: Yes


# UpdateViewContentResponse

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.View'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect.connect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateViewMetadataRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UploadUrlMetadata

### Url
- **Type**: typing.Optional[str]

### UrlExpiry
- **Type**: typing.Optional[str]

### HeadersToInclude
- **Type**: typing.Optional[typing.Dict[str, str]]


# UrlReference

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UseCase

### UseCaseId
- **Type**: typing.Optional[str]

### UseCaseArn
- **Type**: typing.Optional[str]

### UseCaseType
- **Type**: typing.Optional[typing.Literal['CONNECT_CAMPAIGNS', 'RULES_EVALUATION']]


# User

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### IdentityInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserIdentityInfo]

### PhoneConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserPhoneConfig]

### DirectoryUserId
- **Type**: typing.Optional[str]

### SecurityProfileIds
- **Type**: typing.Optional[typing.List[str]]

### RoutingProfileId
- **Type**: typing.Optional[str]

### HierarchyGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# UserData

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserReference]

### RoutingProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.RoutingProfileReference]

### HierarchyPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.HierarchyPathReference]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.AgentStatusReference]

### AvailableSlotsByChannel
- **Type**: typing.Optional[typing.Dict[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE'], int]]

### MaxSlotsByChannel
- **Type**: typing.Optional[typing.Dict[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE'], int]]

### ActiveSlotsByChannel
- **Type**: typing.Optional[typing.Dict[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE'], int]]

### Contacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect.connect_classes.AgentContactReference]]

### NextStatus
- **Type**: typing.Optional[str]


# UserDataFilters

### Queues
- **Type**: typing.Optional[typing.List[str]]

### ContactFilter
- **Type**: <class 'NoneType'>

### RoutingProfiles
- **Type**: typing.Optional[typing.List[str]]

### Agents
- **Type**: typing.Optional[typing.List[str]]

### UserHierarchyGroups
- **Type**: typing.Optional[typing.List[str]]


# UserHierarchyGroupSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# UserHierarchyGroupSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>


# UserHierarchyGroupSearchFilter

### AttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneAttributeFilter]


# UserIdentityInfo

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### SecondaryEmail
- **Type**: typing.Optional[str]

### Mobile
- **Type**: typing.Optional[str]


# UserIdentityInfoLite

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]


# UserInfo

### UserId
- **Type**: typing.Optional[str]


# UserPhoneConfig

### PhoneType
- **Type**: typing.Literal['DESK_PHONE', 'SOFT_PHONE']
- **Required**: Yes

### AutoAccept
- **Type**: typing.Optional[bool]

### AfterContactWorkTimeLimit
- **Type**: typing.Optional[int]

### DeskPhoneNumber
- **Type**: typing.Optional[str]


# UserProficiency

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes

### Level
- **Type**: <class 'float'>
- **Required**: Yes


# UserProficiencyDisassociate

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# UserQuickConnectConfig

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# UserReference

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# UserSearchCriteria

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### ListCondition
- **Type**: <class 'NoneType'>

### HierarchyGroupCondition
- **Type**: <class 'NoneType'>


# UserSearchCriteriaPaginator

### OrConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### StringCondition
- **Type**: <class 'NoneType'>

### ListCondition
- **Type**: <class 'NoneType'>

### HierarchyGroupCondition
- **Type**: <class 'NoneType'>


# UserSearchFilter

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneTagFilter]

### UserAttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ControlPlaneUserAttributeFilter]


# UserSearchSummary

### Arn
- **Type**: typing.Optional[str]

### DirectoryUserId
- **Type**: typing.Optional[str]

### HierarchyGroupId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### IdentityInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserIdentityInfoLite]

### PhoneConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.UserPhoneConfig]

### RoutingProfileId
- **Type**: typing.Optional[str]

### SecurityProfileIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Username
- **Type**: typing.Optional[str]


# UserSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# View

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOMER_MANAGED']]

### Description
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### VersionDescription
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect.connect_classes.ViewContent]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### ViewContentSha256
- **Type**: typing.Optional[str]


# ViewContent

### InputSchema
- **Type**: typing.Optional[str]

### Template
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[str]]


# ViewInputContent

### Template
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[str]]


# ViewSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOMER_MANAGED']]

### Status
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]

### Description
- **Type**: typing.Optional[str]


# ViewVersionSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOMER_MANAGED']]

### Version
- **Type**: typing.Optional[int]

### VersionDescription
- **Type**: typing.Optional[str]


# Vocabulary

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# VocabularySummary

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATION_FAILED', 'CREATION_IN_PROGRESS', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# VoiceRecordingConfiguration

### VoiceRecordingTrack
- **Type**: typing.Optional[typing.Literal['ALL', 'FROM_AGENT', 'TO_AGENT']]

### IvrRecordingTrack
- **Type**: typing.Optional[typing.Literal['ALL']]


# WisdomInfo

### SessionArn
- **Type**: typing.Optional[str]


