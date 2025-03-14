# Connect Classes

# ActionSummaryTypeDef

### ActionType
- **Type**: typing.Literal['ASSIGN_CONTACT_CATEGORY', 'CREATE_CASE', 'CREATE_TASK', 'END_ASSOCIATED_TASKS', 'GENERATE_EVENTBRIDGE_EVENT', 'SEND_NOTIFICATION', 'SUBMIT_AUTO_EVALUATION', 'UPDATE_CASE']
- **Required**: Yes


# ActivateEvaluationFormRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes


# ActivateEvaluationFormResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdditionalEmailRecipientsTypeDef

### ToList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.EmailRecipientTypeDef]]

### CcList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.EmailRecipientTypeDef]]


# AgentConfigOutputTypeDef

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.DistributionTypeDef]
- **Required**: Yes


# AgentConfigTypeDef

### Distributions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.DistributionTypeDef]
- **Required**: Yes


# AgentConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AgentContactReferenceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueReferenceTypeDef]


# AgentHierarchyGroupTypeDef

### Arn
- **Type**: typing.Optional[str]


# AgentHierarchyGroupsTypeDef

### L1Ids
- **Type**: typing.Optional[typing.Sequence[str]]

### L2Ids
- **Type**: typing.Optional[typing.Sequence[str]]

### L3Ids
- **Type**: typing.Optional[typing.Sequence[str]]

### L4Ids
- **Type**: typing.Optional[typing.Sequence[str]]

### L5Ids
- **Type**: typing.Optional[typing.Sequence[str]]


# AgentInfoTypeDef

### Id
- **Type**: typing.Optional[str]

### ConnectedToAgentTimestamp
- **Type**: typing.Optional[datetime.datetime]

### AgentPauseDurationInSeconds
- **Type**: typing.Optional[int]

### HierarchyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupsTypeDef]

### DeviceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DeviceInfoTypeDef]

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ParticipantCapabilitiesTypeDef]


# AgentQualityMetricsTypeDef

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AudioQualityMetricsInfoTypeDef]


# AgentStatusReferenceTypeDef

### StatusStartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StatusArn
- **Type**: typing.Optional[str]

### StatusName
- **Type**: typing.Optional[str]


# AgentStatusSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# AgentStatusSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# AgentStatusSearchFilterTypeDef

### AttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneAttributeFilterTypeDef]


# AgentStatusSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AgentStatusTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AgentsCriteriaOutputTypeDef

### AgentIds
- **Type**: typing.Optional[typing.List[str]]


# AgentsCriteriaTypeDef

### AgentIds
- **Type**: typing.Optional[typing.Sequence[str]]


# AgentsCriteriaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AllowedCapabilitiesTypeDef

### Customer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ParticipantCapabilitiesTypeDef]

### Agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ParticipantCapabilitiesTypeDef]


# AnalyticsDataAssociationResultTypeDef

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


# AnalyticsDataSetsResultTypeDef

### DataSetId
- **Type**: typing.Optional[str]

### DataSetName
- **Type**: typing.Optional[str]


# AnswerMachineDetectionConfigTypeDef

### EnableAnswerMachineDetection
- **Type**: typing.Optional[bool]

### AwaitAnswerMachinePrompt
- **Type**: typing.Optional[bool]


# ApplicationOutputTypeDef

### Namespace
- **Type**: typing.Optional[str]

### ApplicationPermissions
- **Type**: typing.Optional[typing.List[str]]


# ApplicationTypeDef

### Namespace
- **Type**: typing.Optional[str]

### ApplicationPermissions
- **Type**: typing.Optional[typing.Sequence[str]]


# ApplicationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateAnalyticsDataSetRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAccountId
- **Type**: typing.Optional[str]


# AssociateAnalyticsDataSetResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateApprovedOriginRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateBotRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexBot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.LexBotTypeDef]

### LexV2Bot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.LexV2BotTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# AssociateDefaultVocabularyRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']
- **Required**: Yes

### VocabularyId
- **Type**: typing.Optional[str]


# AssociateFlowRequestTypeDef

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


# AssociateInstanceStorageConfigRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes

### StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.InstanceStorageConfigTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateInstanceStorageConfigResponseTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateLambdaFunctionRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateLexBotRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexBot
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.LexBotTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociatePhoneNumberContactFlowRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateQueueQuickConnectsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssociateRoutingProfileQueuesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileQueueConfigTypeDef]
- **Required**: Yes


# AssociateSecurityKeyRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AssociateSecurityKeyResponseTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateTrafficDistributionGroupUserRequestTypeDef

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateUserProficienciesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProficiencies
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.UserProficiencyTypeDef]
- **Required**: Yes


# AssociatedContactSummaryTypeDef

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


# AttachedFileErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### FileId
- **Type**: typing.Optional[str]


# AttachedFileTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CreatedByInfoTypeDef]

### FileUseCaseType
- **Type**: typing.Optional[typing.Literal['ATTACHMENT', 'EMAIL_MESSAGE']]

### AssociatedResourceArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AttachmentReferenceTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'AVAILABLE', 'DELETED', 'FAILED', 'PROCESSING', 'REJECTED']]

### Arn
- **Type**: typing.Optional[str]


# AttendeeTypeDef

### AttendeeId
- **Type**: typing.Optional[str]

### JoinToken
- **Type**: typing.Optional[str]


# AttributeAndConditionTypeDef

### TagConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.TagConditionTypeDef]]

### HierarchyGroupCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupConditionTypeDef]


# AttributeConditionOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### ProficiencyLevel
- **Type**: typing.Optional[float]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RangeTypeDef]

### MatchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.MatchCriteriaOutputTypeDef]

### ComparisonOperator
- **Type**: typing.Optional[str]


# AttributeConditionTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### ProficiencyLevel
- **Type**: typing.Optional[float]

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RangeTypeDef]

### MatchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.MatchCriteriaUnionTypeDef]

### ComparisonOperator
- **Type**: typing.Optional[str]


# AttributeConditionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttributeTypeDef

### AttributeType
- **Type**: typing.Optional[typing.Literal['AUTO_RESOLVE_BEST_VOICES', 'CONTACTFLOW_LOGS', 'CONTACT_LENS', 'EARLY_MEDIA', 'ENHANCED_CHAT_MONITORING', 'ENHANCED_CONTACT_MONITORING', 'HIGH_VOLUME_OUTBOUND', 'INBOUND_CALLS', 'MULTI_PARTY_CHAT_CONFERENCE', 'MULTI_PARTY_CONFERENCE', 'OUTBOUND_CALLS', 'USE_CUSTOM_TTS_VOICES']]

### Value
- **Type**: typing.Optional[str]


# AudioFeaturesTypeDef

### EchoReduction
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'UNAVAILABLE']]


# AudioQualityMetricsInfoTypeDef

### QualityScore
- **Type**: typing.Optional[float]

### PotentialQualityIssues
- **Type**: typing.Optional[typing.List[str]]


# AuthenticationProfileSummaryTypeDef

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


# AuthenticationProfileTypeDef

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


# AvailableNumberSummaryTypeDef

### PhoneNumber
- **Type**: typing.Optional[str]

### PhoneNumberCountryCode
- **Type**: typing.Optional[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]

### PhoneNumberType
- **Type**: typing.Optional[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateAnalyticsDataSetRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TargetAccountId
- **Type**: typing.Optional[str]


# BatchAssociateAnalyticsDataSetResponseTypeDef

### Created
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AnalyticsDataAssociationResultTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ErrorResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateAnalyticsDataSetRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TargetAccountId
- **Type**: typing.Optional[str]


# BatchDisassociateAnalyticsDataSetResponseTypeDef

### Deleted
- **Type**: typing.List[str]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ErrorResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetAttachedFileMetadataRequestTypeDef

### FileIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetAttachedFileMetadataResponseTypeDef

### Files
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AttachedFileTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AttachedFileErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetFlowAssociationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'VOICE_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']]


# BatchGetFlowAssociationResponseTypeDef

### FlowAssociationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.FlowAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutContactRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactDataRequestList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.ContactDataRequestTypeDef]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# BatchPutContactResponseTypeDef

### SuccessfulRequestList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.SuccessfulRequestTypeDef]
- **Required**: Yes

### FailedRequestList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.FailedRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CampaignTypeDef

### CampaignId
- **Type**: typing.Optional[str]


# ChatEventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChatMessageTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# ChatParticipantRoleConfigTypeDef

### ParticipantTimerConfigList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.ParticipantTimerConfigurationTypeDef]
- **Required**: Yes


# ChatStreamingConfigurationTypeDef

### StreamingEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# ClaimPhoneNumberRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]


# ClaimPhoneNumberResponseTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClaimedPhoneNumberSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PhoneNumberStatusTypeDef]

### SourcePhoneNumberArn
- **Type**: typing.Optional[str]


# CommonAttributeAndConditionTypeDef

### TagConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.TagConditionTypeDef]]


# CompleteAttachedFileUploadRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FileId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConditionTypeDef

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### NumberCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.NumberConditionTypeDef]


# ConnectionDataTypeDef

### Attendee
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AttendeeTypeDef]

### Meeting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.MeetingTypeDef]


# ContactAnalysisTypeDef

### Transcript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TranscriptTypeDef]


# ContactConfigurationTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']]

### IncludeRawMessage
- **Type**: typing.Optional[bool]


# ContactDataRequestTypeDef

### SystemEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EndpointTypeDef]

### CustomerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EndpointTypeDef]

### RequestIdentifier
- **Type**: typing.Optional[str]

### QueueId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Campaign
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CampaignTypeDef]


# ContactFilterTypeDef

### ContactStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONNECTED', 'CONNECTED_ONHOLD', 'CONNECTING', 'ENDED', 'ERROR', 'INCOMING', 'MISSED', 'PENDING', 'REJECTED']]]


# ContactFlowModuleSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### StateCondition
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### StatusCondition
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowModuleSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### StateCondition
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### StatusCondition
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowModuleSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# ContactFlowModuleSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]


# ContactFlowModuleTypeDef

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


# ContactFlowSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### TypeCondition
- **Type**: typing.Optional[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]

### StateCondition
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### StatusCondition
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### TypeCondition
- **Type**: typing.Optional[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]

### StateCondition
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### StatusCondition
- **Type**: typing.Optional[typing.Literal['PUBLISHED', 'SAVED']]


# ContactFlowSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# ContactFlowSummaryTypeDef

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


# ContactFlowTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContactFlowVersionSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### VersionDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# ContactSearchSummaryAgentInfoTypeDef

### Id
- **Type**: typing.Optional[str]

### ConnectedToAgentTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ContactSearchSummaryQueueInfoTypeDef

### Id
- **Type**: typing.Optional[str]

### EnqueueTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ContactSearchSummarySegmentAttributeValueTypeDef

### ValueString
- **Type**: typing.Optional[str]


# ContactSearchSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactSearchSummaryQueueInfoTypeDef]

### AgentInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactSearchSummaryAgentInfoTypeDef]

### InitiationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DisconnectTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ScheduledTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect_classes.ContactSearchSummarySegmentAttributeValueTypeDef]]


# ContactTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueInfoTypeDef]

### AgentInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentInfoTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.WisdomInfoTypeDef]

### CustomerId
- **Type**: typing.Optional[str]

### CustomerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EndpointInfoTypeDef]

### SystemEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EndpointInfoTypeDef]

### QueueTimeAdjustmentSeconds
- **Type**: typing.Optional[int]

### QueuePriority
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ConnectedToSystemTimestamp
- **Type**: typing.Optional[datetime.datetime]

### RoutingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingCriteriaTypeDef]

### Customer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CustomerTypeDef]

### Campaign
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CampaignTypeDef]

### AnsweringMachineDetectionStatus
- **Type**: typing.Optional[typing.Literal['AMD_ERROR', 'AMD_NOT_APPLICABLE', 'AMD_UNANSWERED', 'AMD_UNRESOLVED', 'ANSWERED', 'ERROR', 'FAX_MACHINE_DETECTED', 'HUMAN_ANSWERED', 'SIT_TONE_BUSY', 'SIT_TONE_DETECTED', 'SIT_TONE_INVALID_NUMBER', 'UNDETECTED', 'VOICEMAIL_BEEP', 'VOICEMAIL_NO_BEEP']]

### CustomerVoiceActivity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CustomerVoiceActivityTypeDef]

### QualityMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QualityMetricsTypeDef]

### DisconnectDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DisconnectDetailsTypeDef]

### AdditionalEmailRecipients
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AdditionalEmailRecipientsTypeDef]

### SegmentAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect_classes.SegmentAttributeValueOutputTypeDef]]


# ControlPlaneAttributeFilterTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.CommonAttributeAndConditionTypeDef]]

### AndCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CommonAttributeAndConditionTypeDef]

### TagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TagConditionTypeDef]


# ControlPlaneTagFilterTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.TagConditionTypeDef]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.TagConditionTypeDef]]

### TagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TagConditionTypeDef]


# ControlPlaneUserAttributeFilterTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.AttributeAndConditionTypeDef]]

### AndCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AttributeAndConditionTypeDef]

### TagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TagConditionTypeDef]

### HierarchyGroupCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupConditionTypeDef]


# CreateAgentStatusRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAgentStatusResponseTypeDef

### AgentStatusARN
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCaseActionDefinitionOutputTypeDef

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.FieldValueOutputTypeDef]
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCaseActionDefinitionTypeDef

### Fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.FieldValueUnionExtraTypeDef]
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCaseActionDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateContactFlowModuleRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateContactFlowModuleResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContactFlowResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContactFlowVersionRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# CreateContactFlowVersionResponseTypeDef

### ContactFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContactRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### References
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.ReferenceTypeDef]]

### ExpiryDurationInMinutes
- **Type**: typing.Optional[int]

### UserInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserInfoTypeDef]

### InitiateAs
- **Type**: typing.Optional[typing.Literal['CONNECTED_TO_USER']]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SegmentAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.SegmentAttributeValueUnionTypeDef]]

### PreviousContactId
- **Type**: typing.Optional[str]


# CreateContactResponseTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEmailAddressRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateEmailAddressResponseTypeDef

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEvaluationFormRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormItemUnionTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ScoringStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormScoringStrategyTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# CreateEvaluationFormResponseTypeDef

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHoursOfOperationOverrideRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationOverrideConfigTypeDef]
- **Default**: <class 'aws_resource_validator.pydantic_models.base_validator_model.BaseValidatorModel.Config'>

### EffectiveFrom
- **Type**: <class 'str'>
- **Required**: Yes

### EffectiveTill
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CreateHoursOfOperationOverrideResponseTypeDef

### HoursOfOperationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHoursOfOperationRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationConfigTypeDef]
- **Default**: <class 'aws_resource_validator.pydantic_models.base_validator_model.BaseValidatorModel.Config'>

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateHoursOfOperationResponseTypeDef

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstanceRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateInstanceResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationAssociationRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateIntegrationAssociationResponseTypeDef

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateParticipantRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ParticipantDetailsToAddTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateParticipantResponseTypeDef

### ParticipantCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ParticipantTokenCredentialsTypeDef'>
- **Required**: Yes

### ParticipantId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePersistentContactAssociationRequestTypeDef

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


# CreatePersistentContactAssociationResponseTypeDef

### ContinuedFromContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePredefinedAttributeRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.PredefinedAttributeValuesUnionTypeDef'>
- **Required**: Yes


# CreatePromptRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePromptResponseTypeDef

### PromptARN
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePushNotificationRegistrationRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ContactConfigurationTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreatePushNotificationRegistrationResponseTypeDef

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQueueRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OutboundCallerConfigTypeDef]

### OutboundEmailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OutboundEmailConfigTypeDef]

### MaxContacts
- **Type**: typing.Optional[int]

### QuickConnectIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueResponseTypeDef

### QueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQuickConnectRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.QuickConnectConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQuickConnectResponseTypeDef

### QuickConnectARN
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoutingProfileRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.MediaConcurrencyTypeDef]
- **Required**: Yes

### QueueConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileQueueConfigTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AgentAvailabilityTimer
- **Type**: typing.Optional[typing.Literal['TIME_SINCE_LAST_ACTIVITY', 'TIME_SINCE_LAST_INBOUND']]


# CreateRoutingProfileResponseTypeDef

### RoutingProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TriggerEventSource
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.RuleTriggerEventSourceTypeDef'>
- **Required**: Yes

### Function
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.RuleActionUnionTypeDef]
- **Required**: Yes

### PublishStatus
- **Type**: typing.Literal['DRAFT', 'PUBLISHED']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateRuleResponseTypeDef

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecurityProfileRequestTypeDef

### SecurityProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AllowedAccessControlTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TagRestrictedResources
- **Type**: typing.Optional[typing.Sequence[str]]

### Applications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.ApplicationUnionTypeDef]]

### HierarchyRestrictedResources
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowedAccessControlHierarchyGroupId
- **Type**: typing.Optional[str]


# CreateSecurityProfileResponseTypeDef

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTaskTemplateRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateFieldUnionTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ContactFlowId
- **Type**: typing.Optional[str]

### SelfAssignFlowId
- **Type**: typing.Optional[str]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateConstraintsUnionTypeDef]

### Defaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateDefaultsUnionTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### ClientToken
- **Type**: typing.Optional[str]


# CreateTaskTemplateResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrafficDistributionGroupRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTrafficDistributionGroupResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUseCaseRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateUseCaseResponseTypeDef

### UseCaseId
- **Type**: <class 'str'>
- **Required**: Yes

### UseCaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserHierarchyGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ParentGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateUserHierarchyGroupResponseTypeDef

### HierarchyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### HierarchyGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.UserPhoneConfigTypeDef'>
- **Required**: Yes

### SecurityProfileIds
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserIdentityInfoTypeDef]

### DirectoryUserId
- **Type**: typing.Optional[str]

### HierarchyGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateUserResponseTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateViewRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ViewInputContentTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateViewResponseTypeDef

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateViewVersionRequestTypeDef

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


# CreateViewVersionResponseTypeDef

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVocabularyRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVocabularyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatedByInfoTypeDef

### ConnectUserArn
- **Type**: typing.Optional[str]

### AWSIdentityArn
- **Type**: typing.Optional[str]


# CredentialsTypeDef

### AccessToken
- **Type**: typing.Optional[str]

### AccessTokenExpiration
- **Type**: typing.Optional[datetime.datetime]

### RefreshToken
- **Type**: typing.Optional[str]

### RefreshTokenExpiration
- **Type**: typing.Optional[datetime.datetime]


# CrossChannelBehaviorTypeDef

### BehaviorType
- **Type**: typing.Literal['ROUTE_ANY_CHANNEL', 'ROUTE_CURRENT_CHANNEL_ONLY']
- **Required**: Yes


# CurrentMetricDataTypeDef

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CurrentMetricTypeDef]

### Value
- **Type**: typing.Optional[float]


# CurrentMetricResultTypeDef

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DimensionsTypeDef]

### Collections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.CurrentMetricDataTypeDef]]


# CurrentMetricSortCriteriaTypeDef

### SortByMetric
- **Type**: typing.Optional[typing.Literal['AGENTS_AFTER_CONTACT_WORK', 'AGENTS_AVAILABLE', 'AGENTS_ERROR', 'AGENTS_NON_PRODUCTIVE', 'AGENTS_ONLINE', 'AGENTS_ON_CALL', 'AGENTS_ON_CONTACT', 'AGENTS_STAFFED', 'CONTACTS_IN_QUEUE', 'CONTACTS_SCHEDULED', 'OLDEST_CONTACT_AGE', 'SLOTS_ACTIVE', 'SLOTS_AVAILABLE']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# CurrentMetricTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['AGENTS_AFTER_CONTACT_WORK', 'AGENTS_AVAILABLE', 'AGENTS_ERROR', 'AGENTS_NON_PRODUCTIVE', 'AGENTS_ONLINE', 'AGENTS_ON_CALL', 'AGENTS_ON_CONTACT', 'AGENTS_STAFFED', 'CONTACTS_IN_QUEUE', 'CONTACTS_SCHEDULED', 'OLDEST_CONTACT_AGE', 'SLOTS_ACTIVE', 'SLOTS_AVAILABLE']]

### Unit
- **Type**: typing.Optional[typing.Literal['COUNT', 'PERCENT', 'SECONDS']]


# CustomerQualityMetricsTypeDef

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AudioQualityMetricsInfoTypeDef]


# CustomerTypeDef

### DeviceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DeviceInfoTypeDef]

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ParticipantCapabilitiesTypeDef]


# CustomerVoiceActivityTypeDef

### GreetingStartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### GreetingEndTimestamp
- **Type**: typing.Optional[datetime.datetime]


# DateConditionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DateReferenceTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# DeactivateEvaluationFormRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DeactivateEvaluationFormResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefaultVocabularyTypeDef

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


# DeleteAttachedFileRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FileId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactEvaluationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactFlowModuleRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactFlowRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactFlowVersionRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteEmailAddressRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEvaluationFormRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: typing.Optional[int]


# DeleteHoursOfOperationOverrideRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHoursOfOperationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteIntegrationAssociationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePredefinedAttributeRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePromptRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePushNotificationRegistrationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQuickConnectRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoutingProfileRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSecurityProfileRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTaskTemplateRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficDistributionGroupRequestTypeDef

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUseCaseRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### UseCaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserHierarchyGroupRequestTypeDef

### HierarchyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteViewRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteViewVersionRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteVocabularyRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### VocabularyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVocabularyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAgentStatusRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgentStatusResponseTypeDef

### AgentStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.AgentStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAuthenticationProfileRequestTypeDef

### AuthenticationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAuthenticationProfileResponseTypeDef

### AuthenticationProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.AuthenticationProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeContactEvaluationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactEvaluationResponseTypeDef

### Evaluation
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EvaluationTypeDef'>
- **Required**: Yes

### EvaluationForm
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EvaluationFormContentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeContactFlowModuleRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactFlowModuleResponseTypeDef

### ContactFlowModule
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ContactFlowModuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeContactFlowRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactFlowResponseTypeDef

### ContactFlow
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ContactFlowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeContactRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContactResponseTypeDef

### Contact
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ContactTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEmailAddressRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEmailAddressResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEvaluationFormRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormVersion
- **Type**: typing.Optional[int]


# DescribeEvaluationFormResponseTypeDef

### EvaluationForm
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EvaluationFormTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHoursOfOperationOverrideRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHoursOfOperationOverrideResponseTypeDef

### HoursOfOperationOverride
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationOverrideTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHoursOfOperationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHoursOfOperationResponseTypeDef

### HoursOfOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInstanceAttributeRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeType
- **Type**: typing.Literal['AUTO_RESOLVE_BEST_VOICES', 'CONTACTFLOW_LOGS', 'CONTACT_LENS', 'EARLY_MEDIA', 'ENHANCED_CHAT_MONITORING', 'ENHANCED_CONTACT_MONITORING', 'HIGH_VOLUME_OUTBOUND', 'INBOUND_CALLS', 'MULTI_PARTY_CHAT_CONFERENCE', 'MULTI_PARTY_CONFERENCE', 'OUTBOUND_CALLS', 'USE_CUSTOM_TTS_VOICES']
- **Required**: Yes


# DescribeInstanceAttributeResponseTypeDef

### Attribute
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.AttributeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInstanceResponseTypeDef

### Instance
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.InstanceTypeDef'>
- **Required**: Yes

### ReplicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ReplicationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInstanceStorageConfigRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes


# DescribeInstanceStorageConfigResponseTypeDef

### StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.InstanceStorageConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePhoneNumberResponseTypeDef

### ClaimedPhoneNumberSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ClaimedPhoneNumberSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePredefinedAttributeRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePredefinedAttributeResponseTypeDef

### PredefinedAttribute
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.PredefinedAttributeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePromptRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePromptResponseTypeDef

### Prompt
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.PromptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeQueueRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQueueResponseTypeDef

### Queue
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.QueueTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeQuickConnectRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQuickConnectResponseTypeDef

### QuickConnect
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.QuickConnectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRoutingProfileRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoutingProfileResponseTypeDef

### RoutingProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.RoutingProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRuleRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRuleResponseTypeDef

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.RuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSecurityProfileRequestTypeDef

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityProfileResponseTypeDef

### SecurityProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.SecurityProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrafficDistributionGroupRequestTypeDef

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrafficDistributionGroupResponseTypeDef

### TrafficDistributionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TrafficDistributionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserHierarchyGroupRequestTypeDef

### HierarchyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserHierarchyGroupResponseTypeDef

### HierarchyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserHierarchyStructureRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserHierarchyStructureResponseTypeDef

### HierarchyStructure
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.HierarchyStructureTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeViewRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeViewResponseTypeDef

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVocabularyRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### VocabularyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVocabularyResponseTypeDef

### Vocabulary
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.VocabularyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceInfoTypeDef

### PlatformName
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### OperatingSystem
- **Type**: typing.Optional[str]


# DimensionsTypeDef

### Queue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueReferenceTypeDef]

### Channel
- **Type**: typing.Optional[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]

### RoutingProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileReferenceTypeDef]

### RoutingStepExpression
- **Type**: typing.Optional[str]


# DisassociateAnalyticsDataSetRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAccountId
- **Type**: typing.Optional[str]


# DisassociateApprovedOriginRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateBotRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexBot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.LexBotTypeDef]

### LexV2Bot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.LexV2BotTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateFlowRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'SMS_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']
- **Required**: Yes


# DisassociateInstanceStorageConfigRequestTypeDef

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


# DisassociateLambdaFunctionRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateLexBotRequestTypeDef

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


# DisassociatePhoneNumberContactFlowRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateQueueQuickConnectsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociateRoutingProfileQueuesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueReferences
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileQueueReferenceTypeDef]
- **Required**: Yes


# DisassociateSecurityKeyRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DisassociateTrafficDistributionGroupUserRequestTypeDef

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateUserProficienciesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProficiencies
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.UserProficiencyDisassociateTypeDef]
- **Required**: Yes


# DisconnectDetailsTypeDef

### PotentialDisconnectIssue
- **Type**: typing.Optional[str]


# DisconnectReasonTypeDef

### Code
- **Type**: typing.Optional[str]


# DismissUserContactRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# DistributionTypeDef

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### Percentage
- **Type**: <class 'int'>
- **Required**: Yes


# DownloadUrlMetadataTypeDef

### Url
- **Type**: typing.Optional[str]

### UrlExpiry
- **Type**: typing.Optional[str]


# EffectiveHoursOfOperationsTypeDef

### Date
- **Type**: typing.Optional[str]

### OperationalHours
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.OperationalHourTypeDef]]


# EmailAddressInfoTypeDef

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# EmailAddressMetadataTypeDef

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


# EmailAddressSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# EmailAddressSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# EmailAttachmentTypeDef

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes


# EmailMessageReferenceTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# EmailRecipientTypeDef

### Address
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# EmailReferenceTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionConfigTypeDef

### EncryptionType
- **Type**: typing.Literal['KMS']
- **Required**: Yes

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# EndpointInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EndpointTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ErrorResultTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# EvaluationAnswerDataTypeDef

### StringValue
- **Type**: typing.Optional[str]

### NumericValue
- **Type**: typing.Optional[float]

### NotApplicable
- **Type**: typing.Optional[bool]


# EvaluationAnswerInputTypeDef

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationAnswerDataTypeDef]


# EvaluationAnswerOutputTypeDef

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationAnswerDataTypeDef]

### SystemSuggestedValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationAnswerDataTypeDef]


# EvaluationFormContentTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormItemOutputTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ScoringStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormScoringStrategyTypeDef]


# EvaluationFormItemOutputTypeDef

### Section
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSectionOutputTypeDef]

### Question
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormQuestionOutputTypeDef]


# EvaluationFormItemTypeDef

### Section
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSectionUnionTypeDef]

### Question
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormQuestionUnionTypeDef]


# EvaluationFormItemUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFormNumericQuestionAutomationTypeDef

### PropertyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.NumericQuestionPropertyValueAutomationTypeDef]


# EvaluationFormNumericQuestionOptionTypeDef

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


# EvaluationFormNumericQuestionPropertiesOutputTypeDef

### MinValue
- **Type**: <class 'int'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'int'>
- **Required**: Yes

### Options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormNumericQuestionOptionTypeDef]]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormNumericQuestionAutomationTypeDef]


# EvaluationFormNumericQuestionPropertiesTypeDef

### MinValue
- **Type**: <class 'int'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'int'>
- **Required**: Yes

### Options
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormNumericQuestionOptionTypeDef]]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormNumericQuestionAutomationTypeDef]


# EvaluationFormNumericQuestionPropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFormQuestionOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormQuestionTypePropertiesOutputTypeDef]

### Weight
- **Type**: typing.Optional[float]


# EvaluationFormQuestionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormQuestionTypePropertiesUnionTypeDef]

### Weight
- **Type**: typing.Optional[float]


# EvaluationFormQuestionTypePropertiesOutputTypeDef

### Numeric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormNumericQuestionPropertiesOutputTypeDef]

### SingleSelect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef]


# EvaluationFormQuestionTypePropertiesTypeDef

### Numeric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormNumericQuestionPropertiesUnionTypeDef]

### SingleSelect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSingleSelectQuestionPropertiesUnionTypeDef]


# EvaluationFormQuestionTypePropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFormQuestionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFormScoringStrategyTypeDef

### Mode
- **Type**: typing.Literal['QUESTION_ONLY', 'SECTION_ONLY']
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# EvaluationFormSectionOutputTypeDef

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


# EvaluationFormSectionTypeDef

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### RefId
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Mapping[str, typing.Any]]
- **Required**: Yes

### Instructions
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[float]


# EvaluationFormSectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFormSingleSelectQuestionAutomationOptionTypeDef

### RuleCategory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SingleSelectQuestionRuleCategoryAutomationTypeDef]


# EvaluationFormSingleSelectQuestionAutomationOutputTypeDef

### Options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSingleSelectQuestionAutomationOptionTypeDef]
- **Required**: Yes

### DefaultOptionRefId
- **Type**: typing.Optional[str]


# EvaluationFormSingleSelectQuestionAutomationTypeDef

### Options
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSingleSelectQuestionAutomationOptionTypeDef]
- **Required**: Yes

### DefaultOptionRefId
- **Type**: typing.Optional[str]


# EvaluationFormSingleSelectQuestionAutomationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFormSingleSelectQuestionOptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef

### Options
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSingleSelectQuestionOptionTypeDef]
- **Required**: Yes

### DisplayAs
- **Type**: typing.Optional[typing.Literal['DROPDOWN', 'RADIO']]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSingleSelectQuestionAutomationOutputTypeDef]


# EvaluationFormSingleSelectQuestionPropertiesTypeDef

### Options
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSingleSelectQuestionOptionTypeDef]
- **Required**: Yes

### DisplayAs
- **Type**: typing.Optional[typing.Literal['DROPDOWN', 'RADIO']]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSingleSelectQuestionAutomationUnionTypeDef]


# EvaluationFormSingleSelectQuestionPropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFormSummaryTypeDef

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


# EvaluationFormTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormItemOutputTypeDef]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormScoringStrategyTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EvaluationFormVersionSummaryTypeDef

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


# EvaluationMetadataTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContactAgentId
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationScoreTypeDef]


# EvaluationNoteTypeDef

### Value
- **Type**: typing.Optional[str]


# EvaluationScoreTypeDef

### Percentage
- **Type**: typing.Optional[float]

### NotApplicable
- **Type**: typing.Optional[bool]

### AutomaticFail
- **Type**: typing.Optional[bool]


# EvaluationSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationScoreTypeDef]


# EvaluationTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EvaluationMetadataTypeDef'>
- **Required**: Yes

### Answers
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.connect_classes.EvaluationAnswerOutputTypeDef]
- **Required**: Yes

### Notes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.connect_classes.EvaluationNoteTypeDef]
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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect_classes.EvaluationScoreTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventBridgeActionDefinitionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ExpiryTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]

### ExpiryTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ExpressionOutputTypeDef

### AttributeCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AttributeConditionOutputTypeDef]

### AndExpression
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### OrExpression
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### NotAttributeCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AttributeConditionOutputTypeDef]


# ExpressionTypeDef

### AttributeCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AttributeConditionUnionTypeDef]

### AndExpression
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### OrExpression
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### NotAttributeCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AttributeConditionUnionTypeDef]


# ExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FailedRequestTypeDef

### RequestIdentifier
- **Type**: typing.Optional[str]

### FailureReasonCode
- **Type**: typing.Optional[typing.Literal['IDEMPOTENCY_EXCEPTION', 'INTERNAL_ERROR', 'INVALID_ATTRIBUTE_KEY', 'INVALID_CUSTOMER_ENDPOINT', 'INVALID_QUEUE', 'INVALID_SYSTEM_ENDPOINT', 'MISSING_CAMPAIGN', 'MISSING_CUSTOMER_ENDPOINT', 'MISSING_QUEUE_ID_AND_SYSTEM_ENDPOINT', 'REQUEST_THROTTLED']]

### FailureReasonMessage
- **Type**: typing.Optional[str]


# FieldValueOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.FieldValueUnionOutputTypeDef'>
- **Required**: Yes


# FieldValueTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.FieldValueUnionUnionTypeDef'>
- **Required**: Yes


# FieldValueUnionExtraTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValueUnionOutputTypeDef

### BooleanValue
- **Type**: typing.Optional[bool]

### DoubleValue
- **Type**: typing.Optional[float]

### EmptyValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### StringValue
- **Type**: typing.Optional[str]


# FieldValueUnionTypeDef

### BooleanValue
- **Type**: typing.Optional[bool]

### DoubleValue
- **Type**: typing.Optional[float]

### EmptyValue
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### StringValue
- **Type**: typing.Optional[str]


# FieldValueUnionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterV2TypeDef

### FilterKey
- **Type**: typing.Optional[str]

### FilterValues
- **Type**: typing.Optional[typing.Sequence[str]]


# FiltersTypeDef

### Queues
- **Type**: typing.Optional[typing.Sequence[str]]

### Channels
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]]

### RoutingProfiles
- **Type**: typing.Optional[typing.Sequence[str]]

### RoutingStepExpressions
- **Type**: typing.Optional[typing.Sequence[str]]


# FlowAssociationSummaryTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### FlowId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'VOICE_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']]


# GetAttachedFileRequestTypeDef

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


# GetAttachedFileResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.CreatedByInfoTypeDef'>
- **Required**: Yes

### DownloadUrlMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.DownloadUrlMetadataTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContactAttributesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactAttributesResponseTypeDef

### Attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCurrentMetricDataRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.FiltersTypeDef'>
- **Required**: Yes

### CurrentMetrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.CurrentMetricTypeDef]
- **Required**: Yes

### Groupings
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CHANNEL', 'QUEUE', 'ROUTING_PROFILE', 'ROUTING_STEP_EXPRESSION']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortCriteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.CurrentMetricSortCriteriaTypeDef]]


# GetCurrentMetricDataResponseTypeDef

### MetricResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.CurrentMetricResultTypeDef]
- **Required**: Yes

### DataSnapshotTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCurrentUserDataRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.UserDataFiltersTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetCurrentUserDataResponseTypeDef

### UserDataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.UserDataTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetEffectiveHoursOfOperationsRequestTypeDef

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


# GetEffectiveHoursOfOperationsResponseTypeDef

### EffectiveHoursOfOperationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EffectiveHoursOfOperationsTypeDef]
- **Required**: Yes

### TimeZone
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFederationTokenRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFederationTokenResponseTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.CredentialsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFlowAssociationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'SMS_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']
- **Required**: Yes


# GetFlowAssociationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetricDataRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.FiltersTypeDef'>
- **Required**: Yes

### HistoricalMetrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.HistoricalMetricTypeDef]
- **Required**: Yes

### Groupings
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CHANNEL', 'QUEUE', 'ROUTING_PROFILE', 'ROUTING_STEP_EXPRESSION']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# GetMetricDataRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.FiltersTypeDef'>
- **Required**: Yes

### HistoricalMetrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.HistoricalMetricTypeDef]
- **Required**: Yes

### Groupings
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CHANNEL', 'QUEUE', 'ROUTING_PROFILE', 'ROUTING_STEP_EXPRESSION']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetMetricDataResponseTypeDef

### MetricResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.HistoricalMetricResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMetricDataV2RequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.FilterV2TypeDef]
- **Required**: Yes

### Metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.MetricV2UnionTypeDef]
- **Required**: Yes

### Interval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.IntervalDetailsTypeDef]

### Groupings
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetMetricDataV2ResponseTypeDef

### MetricResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.MetricResultV2TypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPromptFileRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPromptFileResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTaskTemplateRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotVersion
- **Type**: typing.Optional[str]


# GetTaskTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TaskTemplateConstraintsOutputTypeDef'>
- **Required**: Yes

### Defaults
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TaskTemplateDefaultsOutputTypeDef'>
- **Required**: Yes

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateFieldOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrafficDistributionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrafficDistributionResponseTypeDef

### TelephonyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TelephonyConfigOutputTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### SignInConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.SignInConfigOutputTypeDef'>
- **Required**: Yes

### AgentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.AgentConfigOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HierarchyGroupConditionTypeDef

### Value
- **Type**: typing.Optional[str]

### HierarchyGroupMatchType
- **Type**: typing.Optional[typing.Literal['EXACT', 'WITH_CHILD_GROUPS']]


# HierarchyGroupSummaryReferenceTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# HierarchyGroupSummaryTypeDef

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


# HierarchyGroupTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LevelId
- **Type**: typing.Optional[str]

### HierarchyPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyPathTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# HierarchyGroupsTypeDef

### Level1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentHierarchyGroupTypeDef]

### Level2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentHierarchyGroupTypeDef]

### Level3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentHierarchyGroupTypeDef]

### Level4
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentHierarchyGroupTypeDef]

### Level5
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentHierarchyGroupTypeDef]


# HierarchyLevelTypeDef

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


# HierarchyLevelUpdateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# HierarchyPathReferenceTypeDef

### LevelOne
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryReferenceTypeDef]

### LevelTwo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryReferenceTypeDef]

### LevelThree
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryReferenceTypeDef]

### LevelFour
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryReferenceTypeDef]

### LevelFive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryReferenceTypeDef]


# HierarchyPathTypeDef

### LevelOne
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryTypeDef]

### LevelTwo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryTypeDef]

### LevelThree
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryTypeDef]

### LevelFour
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryTypeDef]

### LevelFive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryTypeDef]


# HierarchyStructureTypeDef

### LevelOne
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelTypeDef]

### LevelTwo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelTypeDef]

### LevelThree
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelTypeDef]

### LevelFour
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelTypeDef]

### LevelFive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelTypeDef]


# HierarchyStructureUpdateTypeDef

### LevelOne
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelUpdateTypeDef]

### LevelTwo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelUpdateTypeDef]

### LevelThree
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelUpdateTypeDef]

### LevelFour
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelUpdateTypeDef]

### LevelFive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyLevelUpdateTypeDef]


# HistoricalMetricDataTypeDef

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HistoricalMetricTypeDef]

### Value
- **Type**: typing.Optional[float]


# HistoricalMetricResultTypeDef

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DimensionsTypeDef]

### Collections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.HistoricalMetricDataTypeDef]]


# HistoricalMetricTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['ABANDON_TIME', 'AFTER_CONTACT_WORK_TIME', 'API_CONTACTS_HANDLED', 'CALLBACK_CONTACTS_HANDLED', 'CONTACTS_ABANDONED', 'CONTACTS_AGENT_HUNG_UP_FIRST', 'CONTACTS_CONSULTED', 'CONTACTS_HANDLED', 'CONTACTS_HANDLED_INCOMING', 'CONTACTS_HANDLED_OUTBOUND', 'CONTACTS_HOLD_ABANDONS', 'CONTACTS_MISSED', 'CONTACTS_QUEUED', 'CONTACTS_TRANSFERRED_IN', 'CONTACTS_TRANSFERRED_IN_FROM_QUEUE', 'CONTACTS_TRANSFERRED_OUT', 'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE', 'HANDLE_TIME', 'HOLD_TIME', 'INTERACTION_AND_HOLD_TIME', 'INTERACTION_TIME', 'OCCUPANCY', 'QUEUED_TIME', 'QUEUE_ANSWER_TIME', 'SERVICE_LEVEL']]

### Threshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ThresholdTypeDef]

### Statistic
- **Type**: typing.Optional[typing.Literal['AVG', 'MAX', 'SUM']]

### Unit
- **Type**: typing.Optional[typing.Literal['COUNT', 'PERCENT', 'SECONDS']]


# HoursOfOperationConfigTypeDef

### Day
- **Type**: typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationTimeSliceTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationTimeSliceTypeDef'>
- **Required**: Yes


# HoursOfOperationOverrideConfigTypeDef

### Day
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OverrideTimeSliceTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OverrideTimeSliceTypeDef]


# HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### DateCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DateConditionTypeDef]


# HoursOfOperationOverrideSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### DateCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DateConditionTypeDef]


# HoursOfOperationOverrideTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationOverrideConfigTypeDef]]

### EffectiveFrom
- **Type**: typing.Optional[str]

### EffectiveTill
- **Type**: typing.Optional[str]


# HoursOfOperationSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# HoursOfOperationSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# HoursOfOperationSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# HoursOfOperationSummaryTypeDef

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


# HoursOfOperationTimeSliceTypeDef

### Hours
- **Type**: <class 'int'>
- **Required**: Yes

### Minutes
- **Type**: <class 'int'>
- **Required**: Yes


# HoursOfOperationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationConfigTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# ImportPhoneNumberRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SourcePhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]


# ImportPhoneNumberResponseTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InboundAdditionalRecipientsTypeDef

### ToAddresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EmailAddressInfoTypeDef]]

### CcAddresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EmailAddressInfoTypeDef]]


# InboundEmailContentTypeDef

### MessageSourceType
- **Type**: typing.Literal['RAW']
- **Required**: Yes

### RawMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.InboundRawMessageTypeDef]


# InboundRawMessageTypeDef

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
- **Type**: typing.Optional[typing.Mapping[typing.Literal['IN_REPLY_TO', 'MESSAGE_ID', 'REFERENCES', 'X_SES_SPAM_VERDICT', 'X_SES_VIRUS_VERDICT'], str]]


# InstanceStatusReasonTypeDef

### Message
- **Type**: typing.Optional[str]


# InstanceStorageConfigTypeDef

### StorageType
- **Type**: typing.Literal['KINESIS_FIREHOSE', 'KINESIS_STREAM', 'KINESIS_VIDEO_STREAM', 'S3']
- **Required**: Yes

### AssociationId
- **Type**: typing.Optional[str]

### S3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.S3ConfigTypeDef]

### KinesisVideoStreamConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.KinesisVideoStreamConfigTypeDef]

### KinesisStreamConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.KinesisStreamConfigTypeDef]

### KinesisFirehoseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.KinesisFirehoseConfigTypeDef]


# InstanceSummaryTypeDef

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


# InstanceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.InstanceStatusReasonTypeDef]

### InboundCallsEnabled
- **Type**: typing.Optional[bool]

### OutboundCallsEnabled
- **Type**: typing.Optional[bool]

### InstanceAccessUrl
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# IntegrationAssociationSummaryTypeDef

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


# IntervalDetailsTypeDef

### TimeZone
- **Type**: typing.Optional[str]

### IntervalPeriod
- **Type**: typing.Optional[typing.Literal['DAY', 'FIFTEEN_MIN', 'HOUR', 'THIRTY_MIN', 'TOTAL', 'WEEK']]


# InvisibleFieldInfoTypeDef

### Id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateFieldIdentifierTypeDef]


# KinesisFirehoseConfigTypeDef

### FirehoseArn
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamConfigTypeDef

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisVideoStreamConfigTypeDef

### Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriodHours
- **Type**: <class 'int'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EncryptionConfigTypeDef'>
- **Required**: Yes


# LexBotConfigTypeDef

### LexBot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.LexBotTypeDef]

### LexV2Bot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.LexV2BotTypeDef]


# LexBotTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LexRegion
- **Type**: <class 'str'>
- **Required**: Yes


# LexV2BotTypeDef

### AliasArn
- **Type**: typing.Optional[str]


# ListAgentStatusRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CUSTOM', 'OFFLINE', 'ROUTABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListAgentStatusRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AgentStatusTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CUSTOM', 'OFFLINE', 'ROUTABLE']]]


# ListAgentStatusResponseTypeDef

### AgentStatusSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AgentStatusSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnalyticsDataAssociationsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAnalyticsDataAssociationsResponseTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AnalyticsDataAssociationResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnalyticsDataLakeDataSetsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAnalyticsDataLakeDataSetsResponseTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AnalyticsDataSetsResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApprovedOriginsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListApprovedOriginsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApprovedOriginsResponseTypeDef

### Origins
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedContactsRequestTypeDef

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


# ListAssociatedContactsResponseTypeDef

### ContactSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AssociatedContactSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAuthenticationProfilesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListAuthenticationProfilesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAuthenticationProfilesResponseTypeDef

### AuthenticationProfileSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AuthenticationProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBotsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LexVersion
- **Type**: typing.Literal['V1', 'V2']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListBotsRequestTypeDef

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


# ListBotsResponseTypeDef

### LexBots
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.LexBotConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConditionTypeDef

### TargetListType
- **Type**: typing.Optional[typing.Literal['PROFICIENCIES']]

### Conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.ConditionTypeDef]]


# ListContactEvaluationsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListContactEvaluationsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactEvaluationsResponseTypeDef

### EvaluationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EvaluationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactFlowModulesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListContactFlowModulesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ContactFlowModuleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]


# ListContactFlowModulesResponseTypeDef

### ContactFlowModulesSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ContactFlowModuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactFlowVersionsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListContactFlowVersionsRequestTypeDef

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


# ListContactFlowVersionsResponseTypeDef

### ContactFlowVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ContactFlowVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactFlowsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListContactFlowsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGENT_HOLD', 'AGENT_TRANSFER', 'AGENT_WHISPER', 'CAMPAIGN', 'CONTACT_FLOW', 'CUSTOMER_HOLD', 'CUSTOMER_QUEUE', 'CUSTOMER_WHISPER', 'OUTBOUND_WHISPER', 'QUEUE_TRANSFER']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContactFlowsResponseTypeDef

### ContactFlowSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ContactFlowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactReferencesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceTypes
- **Type**: typing.Sequence[typing.Literal['ATTACHMENT', 'CONTACT_ANALYSIS', 'DATE', 'EMAIL', 'EMAIL_MESSAGE', 'NUMBER', 'STRING', 'URL']]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListContactReferencesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceTypes
- **Type**: typing.Sequence[typing.Literal['ATTACHMENT', 'CONTACT_ANALYSIS', 'DATE', 'EMAIL', 'EMAIL_MESSAGE', 'NUMBER', 'STRING', 'URL']]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactReferencesResponseTypeDef

### ReferenceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ReferenceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDefaultVocabulariesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListDefaultVocabulariesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar-AE', 'ca-ES', 'da-DK', 'de-CH', 'de-DE', 'en-AB', 'en-AU', 'en-GB', 'en-IE', 'en-IN', 'en-NZ', 'en-US', 'en-WL', 'en-ZA', 'es-ES', 'es-US', 'fi-FI', 'fr-CA', 'fr-FR', 'hi-IN', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'sv-SE', 'tl-PH', 'zh-CN']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDefaultVocabulariesResponseTypeDef

### DefaultVocabularyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.DefaultVocabularyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEvaluationFormVersionsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListEvaluationFormVersionsRequestTypeDef

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


# ListEvaluationFormVersionsResponseTypeDef

### EvaluationFormVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEvaluationFormsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListEvaluationFormsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEvaluationFormsResponseTypeDef

### EvaluationFormSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlowAssociationsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'VOICE_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListFlowAssociationsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'INBOUND_EMAIL', 'OUTBOUND_EMAIL', 'VOICE_PHONE_NUMBER', 'WHATSAPP_MESSAGING_PHONE_NUMBER']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFlowAssociationsResponseTypeDef

### FlowAssociationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.FlowAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHoursOfOperationOverridesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListHoursOfOperationOverridesRequestTypeDef

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


# ListHoursOfOperationOverridesResponseTypeDef

### HoursOfOperationOverrideList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationOverrideTypeDef]
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHoursOfOperationsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListHoursOfOperationsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHoursOfOperationsResponseTypeDef

### HoursOfOperationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstanceAttributesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListInstanceAttributesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInstanceAttributesResponseTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstanceStorageConfigsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AGENT_EVENTS', 'ATTACHMENTS', 'CALL_RECORDINGS', 'CHAT_TRANSCRIPTS', 'CONTACT_EVALUATIONS', 'CONTACT_TRACE_RECORDS', 'EMAIL_MESSAGES', 'MEDIA_STREAMS', 'REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_SEGMENTS', 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS', 'SCHEDULED_REPORTS', 'SCREEN_RECORDINGS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListInstanceStorageConfigsRequestTypeDef

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


# ListInstanceStorageConfigsResponseTypeDef

### StorageConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.InstanceStorageConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListInstancesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInstancesResponseTypeDef

### InstanceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.InstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIntegrationAssociationsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationType
- **Type**: typing.Optional[typing.Literal['ANALYTICS_CONNECTOR', 'APPLICATION', 'CALL_TRANSFER_CONNECTOR', 'CASES_DOMAIN', 'COGNITO_USER_POOL', 'EVENT', 'FILE_SCANNER', 'PINPOINT_APP', 'Q_MESSAGE_TEMPLATES', 'SES_IDENTITY', 'VOICE_ID', 'WISDOM_ASSISTANT', 'WISDOM_KNOWLEDGE_BASE', 'WISDOM_QUICK_RESPONSES']]

### IntegrationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListIntegrationAssociationsRequestTypeDef

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


# ListIntegrationAssociationsResponseTypeDef

### IntegrationAssociationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.IntegrationAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLambdaFunctionsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListLambdaFunctionsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLambdaFunctionsResponseTypeDef

### LambdaFunctions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLexBotsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListLexBotsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLexBotsResponseTypeDef

### LexBots
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.LexBotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]]

### PhoneNumberCountryCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListPhoneNumbersRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]]

### PhoneNumberCountryCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPhoneNumbersResponseTypeDef

### PhoneNumberSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.PhoneNumberSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersSummaryTypeDef

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


# ListPhoneNumbersV2RequestPaginateTypeDef

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### PhoneNumberCountryCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### PhoneNumberTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]]

### PhoneNumberPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListPhoneNumbersV2RequestTypeDef

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### PhoneNumberCountryCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### PhoneNumberTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DID', 'SHARED', 'SHORT_CODE', 'THIRD_PARTY_DID', 'THIRD_PARTY_TF', 'TOLL_FREE', 'UIFN']]]

### PhoneNumberPrefix
- **Type**: typing.Optional[str]


# ListPhoneNumbersV2ResponseTypeDef

### ListPhoneNumbersSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ListPhoneNumbersSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPredefinedAttributesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListPredefinedAttributesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPredefinedAttributesResponseTypeDef

### PredefinedAttributeSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.PredefinedAttributeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPromptsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListPromptsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPromptsResponseTypeDef

### PromptSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.PromptSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueueQuickConnectsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListQueueQuickConnectsRequestTypeDef

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


# ListQueueQuickConnectsResponseTypeDef

### QuickConnectSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.QuickConnectSummaryTypeDef]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueuesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGENT', 'STANDARD']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListQueuesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGENT', 'STANDARD']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQueuesResponseTypeDef

### QueueSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.QueueSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQuickConnectsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PHONE_NUMBER', 'QUEUE', 'USER']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListQuickConnectsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### QuickConnectTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PHONE_NUMBER', 'QUEUE', 'USER']]]


# ListQuickConnectsResponseTypeDef

### QuickConnectSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.QuickConnectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRealtimeContactAnalysisSegmentsV2RequestTypeDef

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
- **Type**: typing.Sequence[typing.Literal['Attachments', 'Categories', 'Event', 'Issues', 'PostContactSummary', 'Transcript']]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef

### Channel
- **Type**: typing.Literal['CHAT', 'VOICE']
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### Segments
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RealtimeContactAnalysisSegmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingProfileQueuesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListRoutingProfileQueuesRequestTypeDef

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


# ListRoutingProfileQueuesResponseTypeDef

### RoutingProfileQueueConfigSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileQueueConfigSummaryTypeDef]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingProfilesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListRoutingProfilesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRoutingProfilesResponseTypeDef

### RoutingProfileSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRulesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PublishStatus
- **Type**: typing.Optional[typing.Literal['DRAFT', 'PUBLISHED']]

### EventSourceName
- **Type**: typing.Optional[typing.Literal['OnCaseCreate', 'OnCaseUpdate', 'OnContactEvaluationSubmit', 'OnMetricDataUpdate', 'OnPostCallAnalysisAvailable', 'OnPostChatAnalysisAvailable', 'OnRealTimeCallAnalysisAvailable', 'OnRealTimeChatAnalysisAvailable', 'OnSalesforceCaseCreate', 'OnZendeskTicketCreate', 'OnZendeskTicketStatusUpdate']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListRulesRequestTypeDef

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


# ListRulesResponseTypeDef

### RuleSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityKeysRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListSecurityKeysRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSecurityKeysResponseTypeDef

### SecurityKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.SecurityKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityProfileApplicationsRequestPaginateTypeDef

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListSecurityProfileApplicationsRequestTypeDef

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


# ListSecurityProfileApplicationsResponseTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ApplicationOutputTypeDef]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityProfilePermissionsRequestPaginateTypeDef

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListSecurityProfilePermissionsRequestTypeDef

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


# ListSecurityProfilePermissionsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityProfilesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListSecurityProfilesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSecurityProfilesResponseTypeDef

### SecurityProfileSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.SecurityProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTaskTemplatesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### Name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListTaskTemplatesRequestTypeDef

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


# ListTaskTemplatesResponseTypeDef

### TaskTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrafficDistributionGroupUsersRequestPaginateTypeDef

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListTrafficDistributionGroupUsersRequestTypeDef

### TrafficDistributionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrafficDistributionGroupUsersResponseTypeDef

### TrafficDistributionGroupUserSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.TrafficDistributionGroupUserSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrafficDistributionGroupsRequestPaginateTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListTrafficDistributionGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]


# ListTrafficDistributionGroupsResponseTypeDef

### TrafficDistributionGroupSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.TrafficDistributionGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUseCasesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListUseCasesRequestTypeDef

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


# ListUseCasesResponseTypeDef

### UseCaseSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.UseCaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserHierarchyGroupsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListUserHierarchyGroupsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUserHierarchyGroupsResponseTypeDef

### UserHierarchyGroupSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserProficienciesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListUserProficienciesRequestTypeDef

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


# ListUserProficienciesResponseTypeDef

### UserProficiencyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.UserProficiencyTypeDef]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListUsersRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListUsersResponseTypeDef

### UserSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.UserSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListViewVersionsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# ListViewVersionsRequestTypeDef

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


# ListViewVersionsResponseTypeDef

### ViewVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ViewVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListViewsResponseTypeDef

### ViewsSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ViewSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MatchCriteriaOutputTypeDef

### AgentsCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentsCriteriaOutputTypeDef]


# MatchCriteriaTypeDef

### AgentsCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentsCriteriaUnionTypeDef]


# MatchCriteriaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaConcurrencyTypeDef

### Channel
- **Type**: typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']
- **Required**: Yes

### Concurrency
- **Type**: <class 'int'>
- **Required**: Yes

### CrossChannelBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CrossChannelBehaviorTypeDef]


# MediaPlacementTypeDef

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


# MeetingFeaturesConfigurationTypeDef

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AudioFeaturesTypeDef]


# MeetingTypeDef

### MediaRegion
- **Type**: typing.Optional[str]

### MediaPlacement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.MediaPlacementTypeDef]

### MeetingFeatures
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.MeetingFeaturesConfigurationTypeDef]

### MeetingId
- **Type**: typing.Optional[str]


# MetricDataV2TypeDef

### Metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.MetricV2OutputTypeDef]

### Value
- **Type**: typing.Optional[float]


# MetricFilterV2OutputTypeDef

### MetricFilterKey
- **Type**: typing.Optional[str]

### MetricFilterValues
- **Type**: typing.Optional[typing.List[str]]

### Negate
- **Type**: typing.Optional[bool]


# MetricFilterV2TypeDef

### MetricFilterKey
- **Type**: typing.Optional[str]

### MetricFilterValues
- **Type**: typing.Optional[typing.Sequence[str]]

### Negate
- **Type**: typing.Optional[bool]


# MetricFilterV2UnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetricIntervalTypeDef

### Interval
- **Type**: typing.Optional[typing.Literal['DAY', 'FIFTEEN_MIN', 'HOUR', 'THIRTY_MIN', 'TOTAL', 'WEEK']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# MetricResultV2TypeDef

### Dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### MetricInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.MetricIntervalTypeDef]

### Collections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.MetricDataV2TypeDef]]


# MetricV2OutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.ThresholdV2TypeDef]]

### MetricFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.MetricFilterV2OutputTypeDef]]


# MetricV2TypeDef

### Name
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.ThresholdV2TypeDef]]

### MetricFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.MetricFilterV2UnionTypeDef]]


# MetricV2UnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MonitorContactRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BARGE', 'SILENT_MONITOR']]]

### ClientToken
- **Type**: typing.Optional[str]


# MonitorContactResponseTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NewSessionDetailsTypeDef

### SupportedMessagingContentTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### ParticipantDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ParticipantDetailsTypeDef]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### StreamingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ChatStreamingConfigurationTypeDef]


# NotificationRecipientTypeOutputTypeDef

### UserTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserIds
- **Type**: typing.Optional[typing.List[str]]


# NotificationRecipientTypeTypeDef

### UserTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UserIds
- **Type**: typing.Optional[typing.Sequence[str]]


# NotificationRecipientTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NumberConditionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NumberReferenceTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# NumericQuestionPropertyValueAutomationTypeDef

### Label
- **Type**: typing.Literal['AGENT_INTERACTION_DURATION', 'CONTACT_DURATION', 'CUSTOMER_HOLD_TIME', 'NON_TALK_TIME', 'NON_TALK_TIME_PERCENTAGE', 'NUMBER_OF_INTERRUPTIONS', 'OVERALL_AGENT_SENTIMENT_SCORE', 'OVERALL_CUSTOMER_SENTIMENT_SCORE']
- **Required**: Yes


# OperationalHourTypeDef

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OverrideTimeSliceTypeDef]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OverrideTimeSliceTypeDef]


# OutboundAdditionalRecipientsTypeDef

### CcEmailAddresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EmailAddressInfoTypeDef]]


# OutboundCallerConfigTypeDef

### OutboundCallerIdName
- **Type**: typing.Optional[str]

### OutboundCallerIdNumberId
- **Type**: typing.Optional[str]

### OutboundFlowId
- **Type**: typing.Optional[str]


# OutboundEmailConfigTypeDef

### OutboundEmailAddressId
- **Type**: typing.Optional[str]


# OutboundEmailContentTypeDef

### MessageSourceType
- **Type**: typing.Literal['RAW', 'TEMPLATE']
- **Required**: Yes

### TemplatedMessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TemplatedMessageConfigTypeDef]

### RawMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OutboundRawMessageTypeDef]


# OutboundRawMessageTypeDef

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes


# OverrideTimeSliceTypeDef

### Hours
- **Type**: <class 'int'>
- **Required**: Yes

### Minutes
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipantCapabilitiesTypeDef

### Video
- **Type**: typing.Optional[typing.Literal['SEND']]

### ScreenShare
- **Type**: typing.Optional[typing.Literal['SEND']]


# ParticipantDetailsToAddTypeDef

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']]

### DisplayName
- **Type**: typing.Optional[str]


# ParticipantDetailsTypeDef

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes


# ParticipantTimerConfigurationTypeDef

### ParticipantRole
- **Type**: typing.Literal['AGENT', 'CUSTOMER']
- **Required**: Yes

### TimerType
- **Type**: typing.Literal['DISCONNECT_NONCUSTOMER', 'IDLE']
- **Required**: Yes

### TimerValue
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ParticipantTimerValueTypeDef'>
- **Required**: Yes


# ParticipantTimerValueTypeDef

### ParticipantTimerAction
- **Type**: typing.Optional[typing.Literal['Unset']]

### ParticipantTimerDurationInMinutes
- **Type**: typing.Optional[int]


# ParticipantTokenCredentialsTypeDef

### ParticipantToken
- **Type**: typing.Optional[str]

### Expiry
- **Type**: typing.Optional[str]


# PauseContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: typing.Optional[str]


# PersistentChatTypeDef

### RehydrationType
- **Type**: typing.Optional[typing.Literal['ENTIRE_PAST_SESSION', 'FROM_SEGMENT']]

### SourceContactId
- **Type**: typing.Optional[str]


# PhoneNumberQuickConnectConfigTypeDef

### PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# PhoneNumberStatusTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['CLAIMED', 'FAILED', 'IN_PROGRESS']]

### Message
- **Type**: typing.Optional[str]


# PhoneNumberSummaryTypeDef

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


# PredefinedAttributeSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# PredefinedAttributeSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# PredefinedAttributeSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# PredefinedAttributeTypeDef

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PredefinedAttributeValuesOutputTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# PredefinedAttributeValuesOutputTypeDef

### StringList
- **Type**: typing.Optional[typing.List[str]]


# PredefinedAttributeValuesTypeDef

### StringList
- **Type**: typing.Optional[typing.Sequence[str]]


# PredefinedAttributeValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# PromptSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# PromptSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# PromptSummaryTypeDef

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


# PromptTypeDef

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


# PutUserStatusRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentStatusId
- **Type**: <class 'str'>
- **Required**: Yes


# QualityMetricsTypeDef

### Agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentQualityMetricsTypeDef]

### Customer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CustomerQualityMetricsTypeDef]


# QueueInfoInputTypeDef

### Id
- **Type**: typing.Optional[str]


# QueueInfoTypeDef

### Id
- **Type**: typing.Optional[str]

### EnqueueTimestamp
- **Type**: typing.Optional[datetime.datetime]


# QueueQuickConnectConfigTypeDef

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# QueueReferenceTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# QueueSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### QueueTypeCondition
- **Type**: typing.Optional[typing.Literal['STANDARD']]


# QueueSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### QueueTypeCondition
- **Type**: typing.Optional[typing.Literal['STANDARD']]


# QueueSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# QueueSummaryTypeDef

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


# QueueTypeDef

### Name
- **Type**: typing.Optional[str]

### QueueArn
- **Type**: typing.Optional[str]

### QueueId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### OutboundCallerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OutboundCallerConfigTypeDef]

### OutboundEmailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OutboundEmailConfigTypeDef]

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


# QuickConnectConfigTypeDef

### QuickConnectType
- **Type**: typing.Literal['PHONE_NUMBER', 'QUEUE', 'USER']
- **Required**: Yes

### UserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserQuickConnectConfigTypeDef]

### QueueConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueQuickConnectConfigTypeDef]

### PhoneConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PhoneNumberQuickConnectConfigTypeDef]


# QuickConnectSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# QuickConnectSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# QuickConnectSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# QuickConnectSummaryTypeDef

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


# QuickConnectTypeDef

### QuickConnectARN
- **Type**: typing.Optional[str]

### QuickConnectId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### QuickConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QuickConnectConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedRegion
- **Type**: typing.Optional[str]


# RangeTypeDef

### MinProficiencyLevel
- **Type**: typing.Optional[float]

### MaxProficiencyLevel
- **Type**: typing.Optional[float]


# ReadOnlyFieldInfoTypeDef

### Id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateFieldIdentifierTypeDef]


# RealTimeContactAnalysisAttachmentTypeDef

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


# RealTimeContactAnalysisCategoryDetailsTypeDef

### PointsOfInterest
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisPointOfInterestTypeDef]
- **Required**: Yes


# RealTimeContactAnalysisCharacterIntervalTypeDef

### BeginOffsetChar
- **Type**: <class 'int'>
- **Required**: Yes

### EndOffsetChar
- **Type**: <class 'int'>
- **Required**: Yes


# RealTimeContactAnalysisIssueDetectedTypeDef

### TranscriptItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisTranscriptItemWithContentTypeDef]
- **Required**: Yes


# RealTimeContactAnalysisPointOfInterestTypeDef

### TranscriptItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef]]


# RealTimeContactAnalysisSegmentAttachmentsTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisAttachmentTypeDef]
- **Required**: Yes

### Time
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisTimeDataTypeDef'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# RealTimeContactAnalysisSegmentCategoriesTypeDef

### MatchedDetails
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisCategoryDetailsTypeDef]
- **Required**: Yes


# RealTimeContactAnalysisSegmentEventTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### EventType
- **Type**: <class 'str'>
- **Required**: Yes

### Time
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisTimeDataTypeDef'>
- **Required**: Yes

### ParticipantId
- **Type**: typing.Optional[str]

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']]

### DisplayName
- **Type**: typing.Optional[str]


# RealTimeContactAnalysisSegmentIssuesTypeDef

### IssuesDetected
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisIssueDetectedTypeDef]
- **Required**: Yes


# RealTimeContactAnalysisSegmentPostContactSummaryTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED']
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### FailureCode
- **Type**: typing.Optional[typing.Literal['FAILED_SAFETY_GUIDELINES', 'INSUFFICIENT_CONVERSATION_CONTENT', 'INTERNAL_ERROR', 'INVALID_ANALYSIS_CONFIGURATION', 'QUOTA_EXCEEDED']]


# RealTimeContactAnalysisSegmentTranscriptTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisTimeDataTypeDef'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### Redaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisTranscriptItemRedactionTypeDef]

### Sentiment
- **Type**: typing.Optional[typing.Literal['NEGATIVE', 'NEUTRAL', 'POSITIVE']]


# RealTimeContactAnalysisTimeDataTypeDef

### AbsoluteTime
- **Type**: typing.Optional[datetime.datetime]


# RealTimeContactAnalysisTranscriptItemRedactionTypeDef

### CharacterOffsets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisCharacterIntervalTypeDef]]


# RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CharacterOffsets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisCharacterIntervalTypeDef]


# RealTimeContactAnalysisTranscriptItemWithContentTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### CharacterOffsets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisCharacterIntervalTypeDef]


# RealtimeContactAnalysisSegmentTypeDef

### Transcript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisSegmentTranscriptTypeDef]

### Categories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisSegmentCategoriesTypeDef]

### Issues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisSegmentIssuesTypeDef]

### Event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisSegmentEventTypeDef]

### Attachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisSegmentAttachmentsTypeDef]

### PostContactSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RealTimeContactAnalysisSegmentPostContactSummaryTypeDef]


# ReferenceSummaryTypeDef

### Url
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UrlReferenceTypeDef]

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AttachmentReferenceTypeDef]

### EmailMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EmailMessageReferenceTypeDef]

### String
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringReferenceTypeDef]

### Number
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.NumberReferenceTypeDef]

### Date
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DateReferenceTypeDef]

### Email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EmailReferenceTypeDef]


# ReferenceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReleasePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# ReplicateInstanceRequestTypeDef

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


# ReplicateInstanceResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplicationConfigurationTypeDef

### ReplicationStatusSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.ReplicationStatusSummaryTypeDef]]

### SourceRegion
- **Type**: typing.Optional[str]

### GlobalSignInEndpoint
- **Type**: typing.Optional[str]


# ReplicationStatusSummaryTypeDef

### Region
- **Type**: typing.Optional[str]

### ReplicationStatus
- **Type**: typing.Optional[typing.Literal['INSTANCE_REPLICATION_COMPLETE', 'INSTANCE_REPLICATION_DELETION_FAILED', 'INSTANCE_REPLICATION_FAILED', 'INSTANCE_REPLICATION_IN_PROGRESS', 'INSTANCE_REPLICA_DELETING', 'RESOURCE_REPLICATION_NOT_STARTED']]

### ReplicationStatusReason
- **Type**: typing.Optional[str]


# RequiredFieldInfoTypeDef

### Id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateFieldIdentifierTypeDef]


# ResourceTagsSearchCriteriaTypeDef

### TagSearchCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TagSearchConditionTypeDef]


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


# ResumeContactRecordingRequestTypeDef

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


# ResumeContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: typing.Optional[str]


# RoutingCriteriaInputStepExpiryTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]


# RoutingCriteriaInputStepTypeDef

### Expiry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingCriteriaInputStepExpiryTypeDef]

### Expression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ExpressionUnionTypeDef]


# RoutingCriteriaInputTypeDef

### Steps
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.RoutingCriteriaInputStepTypeDef]]


# RoutingCriteriaTypeDef

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.StepTypeDef]]

### ActivationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Index
- **Type**: typing.Optional[int]


# RoutingProfileQueueConfigSummaryTypeDef

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


# RoutingProfileQueueConfigTypeDef

### QueueReference
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.RoutingProfileQueueReferenceTypeDef'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Delay
- **Type**: <class 'int'>
- **Required**: Yes


# RoutingProfileQueueReferenceTypeDef

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### Channel
- **Type**: typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']
- **Required**: Yes


# RoutingProfileReferenceTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# RoutingProfileSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# RoutingProfileSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# RoutingProfileSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# RoutingProfileSummaryTypeDef

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


# RoutingProfileTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.MediaConcurrencyTypeDef]]

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


# RuleActionOutputTypeDef

### ActionType
- **Type**: typing.Literal['ASSIGN_CONTACT_CATEGORY', 'CREATE_CASE', 'CREATE_TASK', 'END_ASSOCIATED_TASKS', 'GENERATE_EVENTBRIDGE_EVENT', 'SEND_NOTIFICATION', 'SUBMIT_AUTO_EVALUATION', 'UPDATE_CASE']
- **Required**: Yes

### TaskAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskActionDefinitionOutputTypeDef]

### EventBridgeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EventBridgeActionDefinitionTypeDef]

### AssignContactCategoryAction
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SendNotificationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SendNotificationActionDefinitionOutputTypeDef]

### CreateCaseAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CreateCaseActionDefinitionOutputTypeDef]

### UpdateCaseAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UpdateCaseActionDefinitionOutputTypeDef]

### EndAssociatedTasksAction
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SubmitAutoEvaluationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SubmitAutoEvaluationActionDefinitionTypeDef]


# RuleActionTypeDef

### ActionType
- **Type**: typing.Literal['ASSIGN_CONTACT_CATEGORY', 'CREATE_CASE', 'CREATE_TASK', 'END_ASSOCIATED_TASKS', 'GENERATE_EVENTBRIDGE_EVENT', 'SEND_NOTIFICATION', 'SUBMIT_AUTO_EVALUATION', 'UPDATE_CASE']
- **Required**: Yes

### TaskAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskActionDefinitionUnionTypeDef]

### EventBridgeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EventBridgeActionDefinitionTypeDef]

### AssignContactCategoryAction
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### SendNotificationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SendNotificationActionDefinitionUnionTypeDef]

### CreateCaseAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CreateCaseActionDefinitionUnionTypeDef]

### UpdateCaseAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UpdateCaseActionDefinitionUnionTypeDef]

### EndAssociatedTasksAction
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### SubmitAutoEvaluationAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SubmitAutoEvaluationActionDefinitionTypeDef]


# RuleActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleSummaryTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ActionSummaryTypeDef]
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# RuleTriggerEventSourceTypeDef

### EventSourceName
- **Type**: typing.Literal['OnCaseCreate', 'OnCaseUpdate', 'OnContactEvaluationSubmit', 'OnMetricDataUpdate', 'OnPostCallAnalysisAvailable', 'OnPostChatAnalysisAvailable', 'OnRealTimeCallAnalysisAvailable', 'OnRealTimeChatAnalysisAvailable', 'OnSalesforceCaseCreate', 'OnZendeskTicketCreate', 'OnZendeskTicketStatusUpdate']
- **Required**: Yes

### IntegrationAssociationId
- **Type**: typing.Optional[str]


# RuleTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.RuleTriggerEventSourceTypeDef'>
- **Required**: Yes

### Function
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RuleActionOutputTypeDef]
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


# S3ConfigTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### BucketPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EncryptionConfigTypeDef]


# SearchAgentStatusesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentStatusSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentStatusSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchAgentStatusesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentStatusSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentStatusSearchCriteriaTypeDef]


# SearchAgentStatusesResponseTypeDef

### AgentStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AgentStatusTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchAvailablePhoneNumbersRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchAvailablePhoneNumbersRequestTypeDef

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


# SearchAvailablePhoneNumbersResponseTypeDef

### AvailableNumbersList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.AvailableNumberSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchContactFlowModulesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFlowModuleSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFlowModuleSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchContactFlowModulesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFlowModuleSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFlowModuleSearchCriteriaTypeDef]


# SearchContactFlowModulesResponseTypeDef

### ContactFlowModules
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ContactFlowModuleTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchContactFlowsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFlowSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFlowSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchContactFlowsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFlowSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFlowSearchCriteriaTypeDef]


# SearchContactFlowsResponseTypeDef

### ContactFlows
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ContactFlowTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchContactsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.SearchContactsTimeRangeTypeDef'>
- **Required**: Yes

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SearchCriteriaTypeDef]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SortTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchContactsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.SearchContactsTimeRangeTypeDef'>
- **Required**: Yes

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SearchCriteriaTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SortTypeDef]


# SearchContactsResponseTypeDef

### Contacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.ContactSearchSummaryTypeDef]
- **Required**: Yes

### TotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchContactsTimeRangeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchCriteriaTypeDef

### AgentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AgentHierarchyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentHierarchyGroupsTypeDef]

### Channels
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE']]]

### ContactAnalysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactAnalysisTypeDef]

### InitiationMethods
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGENT_REPLY', 'API', 'CALLBACK', 'DISCONNECT', 'EXTERNAL_OUTBOUND', 'FLOW', 'INBOUND', 'MONITOR', 'OUTBOUND', 'QUEUE_TRANSFER', 'TRANSFER', 'WEBRTC_API']]]

### QueueIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SearchableContactAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SearchableContactAttributesTypeDef]

### SearchableSegmentAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SearchableSegmentAttributesTypeDef]


# SearchEmailAddressesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EmailAddressSearchCriteriaTypeDef]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EmailAddressSearchFilterTypeDef]


# SearchEmailAddressesResponseTypeDef

### EmailAddresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.EmailAddressMetadataTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchHoursOfOperationOverridesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchHoursOfOperationOverridesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationOverrideSearchCriteriaTypeDef]


# SearchHoursOfOperationOverridesResponseTypeDef

### HoursOfOperationOverrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationOverrideTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchHoursOfOperationsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchHoursOfOperationsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationSearchCriteriaTypeDef]


# SearchHoursOfOperationsResponseTypeDef

### HoursOfOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchPredefinedAttributesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PredefinedAttributeSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchPredefinedAttributesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PredefinedAttributeSearchCriteriaTypeDef]


# SearchPredefinedAttributesResponseTypeDef

### PredefinedAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.PredefinedAttributeTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchPromptsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PromptSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PromptSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchPromptsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PromptSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PromptSearchCriteriaTypeDef]


# SearchPromptsResponseTypeDef

### Prompts
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.PromptTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchQueuesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchQueuesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueSearchCriteriaTypeDef]


# SearchQueuesResponseTypeDef

### Queues
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.QueueTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchQuickConnectsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QuickConnectSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QuickConnectSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchQuickConnectsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QuickConnectSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QuickConnectSearchCriteriaTypeDef]


# SearchQuickConnectsResponseTypeDef

### QuickConnects
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.QuickConnectTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchResourceTagsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ResourceTagsSearchCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchResourceTagsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ResourceTagsSearchCriteriaTypeDef]


# SearchResourceTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.TagSetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchRoutingProfilesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchRoutingProfilesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileSearchCriteriaTypeDef]


# SearchRoutingProfilesResponseTypeDef

### RoutingProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchSecurityProfilesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SecurityProfileSearchCriteriaPaginatorTypeDef]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SecurityProfilesSearchFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchSecurityProfilesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SecurityProfileSearchCriteriaTypeDef]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SecurityProfilesSearchFilterTypeDef]


# SearchSecurityProfilesResponseTypeDef

### SecurityProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.SecurityProfileSearchSummaryTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchUserHierarchyGroupsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserHierarchyGroupSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserHierarchyGroupSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchUserHierarchyGroupsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserHierarchyGroupSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserHierarchyGroupSearchCriteriaTypeDef]


# SearchUserHierarchyGroupsResponseTypeDef

### UserHierarchyGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchUsersRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserSearchCriteriaPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchUsersRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SearchFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserSearchFilterTypeDef]

### SearchCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserSearchCriteriaTypeDef]


# SearchUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.UserSearchSummaryTypeDef]
- **Required**: Yes

### ApproximateTotalCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchVocabulariesRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PaginatorConfigTypeDef]


# SearchVocabulariesRequestTypeDef

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


# SearchVocabulariesResponseTypeDef

### VocabularySummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.VocabularySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchableContactAttributesCriteriaTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SearchableContactAttributesTypeDef

### Criteria
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.SearchableContactAttributesCriteriaTypeDef]
- **Required**: Yes

### MatchType
- **Type**: typing.Optional[typing.Literal['MATCH_ALL', 'MATCH_ANY']]


# SearchableSegmentAttributesCriteriaTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SearchableSegmentAttributesTypeDef

### Criteria
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.SearchableSegmentAttributesCriteriaTypeDef]
- **Required**: Yes

### MatchType
- **Type**: typing.Optional[typing.Literal['MATCH_ALL', 'MATCH_ANY']]


# SecurityKeyTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# SecurityProfileSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# SecurityProfileSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# SecurityProfileSearchSummaryTypeDef

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


# SecurityProfileSummaryTypeDef

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


# SecurityProfileTypeDef

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


# SecurityProfilesSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]


# SegmentAttributeValueOutputTypeDef

### ValueString
- **Type**: typing.Optional[str]

### ValueMap
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### ValueInteger
- **Type**: typing.Optional[int]


# SegmentAttributeValueTypeDef

### ValueString
- **Type**: typing.Optional[str]

### ValueMap
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### ValueInteger
- **Type**: typing.Optional[int]


# SegmentAttributeValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SendChatIntegrationEventRequestTypeDef

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationId
- **Type**: <class 'str'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ChatEventTypeDef'>
- **Required**: Yes

### Subtype
- **Type**: typing.Optional[str]

### NewSessionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.NewSessionDetailsTypeDef]


# SendChatIntegrationEventResponseTypeDef

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NewChatCreated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendNotificationActionDefinitionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.NotificationRecipientTypeOutputTypeDef'>
- **Required**: Yes

### Subject
- **Type**: typing.Optional[str]


# SendNotificationActionDefinitionTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.NotificationRecipientTypeUnionTypeDef'>
- **Required**: Yes

### Subject
- **Type**: typing.Optional[str]


# SendNotificationActionDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SendOutboundEmailRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EmailAddressInfoTypeDef'>
- **Required**: Yes

### DestinationEmailAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EmailAddressInfoTypeDef'>
- **Required**: Yes

### EmailMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.OutboundEmailContentTypeDef'>
- **Required**: Yes

### TrafficType
- **Type**: typing.Literal['CAMPAIGN', 'GENERAL']
- **Required**: Yes

### AdditionalRecipients
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OutboundAdditionalRecipientsTypeDef]

### SourceCampaign
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SourceCampaignTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# SignInConfigOutputTypeDef

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.SignInDistributionTypeDef]
- **Required**: Yes


# SignInConfigTypeDef

### Distributions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.SignInDistributionTypeDef]
- **Required**: Yes


# SignInConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignInDistributionTypeDef

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# SingleSelectQuestionRuleCategoryAutomationTypeDef

### Category
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['NOT_PRESENT', 'PRESENT']
- **Required**: Yes

### OptionRefId
- **Type**: <class 'str'>
- **Required**: Yes


# SortTypeDef

### FieldName
- **Type**: typing.Literal['CHANNEL', 'CONNECTED_TO_AGENT_TIMESTAMP', 'DISCONNECT_TIMESTAMP', 'INITIATION_METHOD', 'INITIATION_TIMESTAMP', 'SCHEDULED_TIMESTAMP']
- **Required**: Yes

### Order
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# SourceCampaignTypeDef

### CampaignId
- **Type**: typing.Optional[str]

### OutboundRequestId
- **Type**: typing.Optional[str]


# StartAttachedFileUploadRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.CreatedByInfoTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartAttachedFileUploadResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.CreatedByInfoTypeDef'>
- **Required**: Yes

### UploadUrlMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.UploadUrlMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartChatContactRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ParticipantDetailsTypeDef'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### InitialMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ChatMessageTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### ChatDurationInMinutes
- **Type**: typing.Optional[int]

### SupportedMessagingContentTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### PersistentChat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PersistentChatTypeDef]

### RelatedContactId
- **Type**: typing.Optional[str]

### SegmentAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.SegmentAttributeValueUnionTypeDef]]

### CustomerId
- **Type**: typing.Optional[str]


# StartChatContactResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartContactEvaluationRequestTypeDef

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


# StartContactEvaluationResponseTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartContactRecordingRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.VoiceRecordingConfigurationTypeDef'>
- **Required**: Yes


# StartContactStreamingRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ChatStreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ChatStreamingConfigurationTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartContactStreamingResponseTypeDef

### StreamingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartEmailContactRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### FromEmailAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EmailAddressInfoTypeDef'>
- **Required**: Yes

### DestinationEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### EmailMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.InboundEmailContentTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.ReferenceTypeDef]]

### Name
- **Type**: typing.Optional[str]

### AdditionalRecipients
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.InboundAdditionalRecipientsTypeDef]

### Attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EmailAttachmentTypeDef]]

### ContactFlowId
- **Type**: typing.Optional[str]

### RelatedContactId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SegmentAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.SegmentAttributeValueUnionTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# StartEmailContactResponseTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartOutboundChatContactRequestTypeDef

### SourceEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EndpointTypeDef'>
- **Required**: Yes

### DestinationEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EndpointTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentAttributes
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.SegmentAttributeValueUnionTypeDef]
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ChatDurationInMinutes
- **Type**: typing.Optional[int]

### ParticipantDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ParticipantDetailsTypeDef]

### InitialSystemMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ChatMessageTypeDef]

### RelatedContactId
- **Type**: typing.Optional[str]

### SupportedMessagingContentTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### ClientToken
- **Type**: typing.Optional[str]


# StartOutboundChatContactResponseTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartOutboundEmailContactRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationEmailAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.EmailAddressInfoTypeDef'>
- **Required**: Yes

### EmailMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.OutboundEmailContentTypeDef'>
- **Required**: Yes

### FromEmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EmailAddressInfoTypeDef]

### AdditionalRecipients
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.OutboundAdditionalRecipientsTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# StartOutboundEmailContactResponseTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartOutboundVoiceContactRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.ReferenceTypeDef]]

### RelatedContactId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### SourcePhoneNumber
- **Type**: typing.Optional[str]

### QueueId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AnswerMachineDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AnswerMachineDetectionConfigTypeDef]

### CampaignId
- **Type**: typing.Optional[str]

### TrafficType
- **Type**: typing.Optional[typing.Literal['CAMPAIGN', 'GENERAL']]


# StartOutboundVoiceContactResponseTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartScreenSharingRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# StartTaskContactRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### References
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.ReferenceTypeDef]]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### ScheduledTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef]

### TaskTemplateId
- **Type**: typing.Optional[str]

### QuickConnectId
- **Type**: typing.Optional[str]

### RelatedContactId
- **Type**: typing.Optional[str]

### SegmentAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.SegmentAttributeValueUnionTypeDef]]


# StartTaskContactResponseTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartWebRTCContactRequestTypeDef

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ParticipantDetailsTypeDef'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]

### AllowedCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AllowedCapabilitiesTypeDef]

### RelatedContactId
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.ReferenceTypeDef]]

### Description
- **Type**: typing.Optional[str]


# StartWebRTCContactResponseTypeDef

### ConnectionData
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ConnectionDataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StepTypeDef

### Expiry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ExpiryTypeDef]

### Expression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ExpressionOutputTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'EXPIRED', 'INACTIVE', 'JOINED']]


# StopContactRecordingRequestTypeDef

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


# StopContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DisconnectReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.DisconnectReasonTypeDef]


# StopContactStreamingRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingId
- **Type**: <class 'str'>
- **Required**: Yes


# StringConditionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StringReferenceTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# SubmitAutoEvaluationActionDefinitionTypeDef

### EvaluationFormId
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitContactEvaluationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### Answers
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.EvaluationAnswerInputTypeDef]]

### Notes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.EvaluationNoteTypeDef]]


# SubmitContactEvaluationResponseTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SuccessfulRequestTypeDef

### RequestIdentifier
- **Type**: typing.Optional[str]

### ContactId
- **Type**: typing.Optional[str]


# SuspendContactRecordingRequestTypeDef

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


# TagConditionTypeDef

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]


# TagContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagSearchConditionTypeDef

### tagKey
- **Type**: typing.Optional[str]

### tagValue
- **Type**: typing.Optional[str]

### tagKeyComparisonType
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT', 'STARTS_WITH']]

### tagValueComparisonType
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EXACT', 'STARTS_WITH']]


# TagSetTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TaskActionDefinitionOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.connect_classes.ReferenceTypeDef]]


# TaskActionDefinitionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### References
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.ReferenceTypeDef]]


# TaskActionDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskTemplateConstraintsOutputTypeDef

### RequiredFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.RequiredFieldInfoTypeDef]]

### ReadOnlyFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.ReadOnlyFieldInfoTypeDef]]

### InvisibleFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.InvisibleFieldInfoTypeDef]]


# TaskTemplateConstraintsTypeDef

### RequiredFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.RequiredFieldInfoTypeDef]]

### ReadOnlyFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.ReadOnlyFieldInfoTypeDef]]

### InvisibleFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.InvisibleFieldInfoTypeDef]]


# TaskTemplateConstraintsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskTemplateDefaultFieldValueTypeDef

### Id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateFieldIdentifierTypeDef]

### DefaultValue
- **Type**: typing.Optional[str]


# TaskTemplateDefaultsOutputTypeDef

### DefaultFieldValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateDefaultFieldValueTypeDef]]


# TaskTemplateDefaultsTypeDef

### DefaultFieldValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateDefaultFieldValueTypeDef]]


# TaskTemplateDefaultsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskTemplateFieldIdentifierTypeDef

### Name
- **Type**: typing.Optional[str]


# TaskTemplateFieldOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskTemplateFieldUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskTemplateMetadataTypeDef

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


# TelephonyConfigOutputTypeDef

### Distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.DistributionTypeDef]
- **Required**: Yes


# TelephonyConfigTypeDef

### Distributions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.DistributionTypeDef]
- **Required**: Yes


# TelephonyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TemplateAttributesTypeDef

### CustomAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CustomerProfileAttributes
- **Type**: typing.Optional[str]


# TemplatedMessageConfigTypeDef

### KnowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TemplateAttributesTypeDef'>
- **Required**: Yes


# ThresholdTypeDef

### Comparison
- **Type**: typing.Optional[typing.Literal['LT']]

### ThresholdValue
- **Type**: typing.Optional[float]


# ThresholdV2TypeDef

### Comparison
- **Type**: typing.Optional[str]

### ThresholdValue
- **Type**: typing.Optional[float]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrafficDistributionGroupSummaryTypeDef

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


# TrafficDistributionGroupTypeDef

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


# TrafficDistributionGroupUserSummaryTypeDef

### UserId
- **Type**: typing.Optional[str]


# TranscriptCriteriaTypeDef

### ParticipantRole
- **Type**: typing.Literal['AGENT', 'CUSTOMER', 'CUSTOM_BOT', 'SUPERVISOR', 'SYSTEM']
- **Required**: Yes

### SearchText
- **Type**: typing.Sequence[str]
- **Required**: Yes

### MatchType
- **Type**: typing.Literal['MATCH_ALL', 'MATCH_ANY']
- **Required**: Yes


# TranscriptTypeDef

### Criteria
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.TranscriptCriteriaTypeDef]
- **Required**: Yes

### MatchType
- **Type**: typing.Optional[typing.Literal['MATCH_ALL', 'MATCH_ANY']]


# TransferContactRequestTypeDef

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


# TransferContactResponseTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAgentStatusRequestTypeDef

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


# UpdateAuthenticationProfileRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### BlockedIps
- **Type**: typing.Optional[typing.Sequence[str]]

### PeriodicSessionDuration
- **Type**: typing.Optional[int]


# UpdateCaseActionDefinitionOutputTypeDef

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.FieldValueOutputTypeDef]
- **Required**: Yes


# UpdateCaseActionDefinitionTypeDef

### Fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.FieldValueUnionExtraTypeDef]
- **Required**: Yes


# UpdateCaseActionDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateContactAttributesRequestTypeDef

### InitialContactId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UpdateContactEvaluationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### Answers
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.EvaluationAnswerInputTypeDef]]

### Notes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.EvaluationNoteTypeDef]]


# UpdateContactEvaluationResponseTypeDef

### EvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateContactFlowContentRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateContactFlowMetadataRequestTypeDef

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


# UpdateContactFlowModuleContentRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowModuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateContactFlowModuleMetadataRequestTypeDef

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


# UpdateContactFlowNameRequestTypeDef

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


# UpdateContactRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.ReferenceTypeDef]]

### SegmentAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.connect_classes.SegmentAttributeValueUnionTypeDef]]

### QueueInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.QueueInfoInputTypeDef]

### UserInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserInfoTypeDef]

### CustomerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EndpointTypeDef]

### SystemEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EndpointTypeDef]


# UpdateContactRoutingDataRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingCriteriaInputTypeDef]


# UpdateContactScheduleRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledTime
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TimestampTypeDef'>
- **Required**: Yes


# UpdateEmailAddressMetadataRequestTypeDef

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


# UpdateEmailAddressMetadataResponseTypeDef

### EmailAddressId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddressArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEvaluationFormRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormItemUnionTypeDef]
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### ScoringStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.EvaluationFormScoringStrategyTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# UpdateEvaluationFormResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateHoursOfOperationOverrideRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationOverrideConfigTypeDef]]

### EffectiveFrom
- **Type**: typing.Optional[str]

### EffectiveTill
- **Type**: typing.Optional[str]


# UpdateHoursOfOperationRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.HoursOfOperationConfigTypeDef]]


# UpdateInstanceAttributeRequestTypeDef

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


# UpdateInstanceStorageConfigRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.InstanceStorageConfigTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# UpdateParticipantAuthenticationRequestTypeDef

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


# UpdateParticipantRoleConfigChannelInfoTypeDef

### Chat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ChatParticipantRoleConfigTypeDef]


# UpdateParticipantRoleConfigRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.UpdateParticipantRoleConfigChannelInfoTypeDef'>
- **Required**: Yes


# UpdatePhoneNumberMetadataRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberDescription
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# UpdatePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# UpdatePhoneNumberResponseTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### PhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePredefinedAttributeRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.PredefinedAttributeValuesUnionTypeDef]


# UpdatePromptRequestTypeDef

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


# UpdatePromptResponseTypeDef

### PromptARN
- **Type**: <class 'str'>
- **Required**: Yes

### PromptId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQueueHoursOfOperationRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### HoursOfOperationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateQueueMaxContactsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxContacts
- **Type**: typing.Optional[int]


# UpdateQueueNameRequestTypeDef

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


# UpdateQueueOutboundCallerConfigRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### OutboundCallerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.OutboundCallerConfigTypeDef'>
- **Required**: Yes


# UpdateQueueOutboundEmailConfigRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### OutboundEmailConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.OutboundEmailConfigTypeDef'>
- **Required**: Yes


# UpdateQueueStatusRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateQuickConnectConfigRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectId
- **Type**: <class 'str'>
- **Required**: Yes

### QuickConnectConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.QuickConnectConfigTypeDef'>
- **Required**: Yes


# UpdateQuickConnectNameRequestTypeDef

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


# UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### AgentAvailabilityTimer
- **Type**: typing.Literal['TIME_SINCE_LAST_ACTIVITY', 'TIME_SINCE_LAST_INBOUND']
- **Required**: Yes


# UpdateRoutingProfileConcurrencyRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### MediaConcurrencies
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.MediaConcurrencyTypeDef]
- **Required**: Yes


# UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultOutboundQueueId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoutingProfileNameRequestTypeDef

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


# UpdateRoutingProfileQueuesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### QueueConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileQueueConfigTypeDef]
- **Required**: Yes


# UpdateRuleRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.RuleActionUnionTypeDef]
- **Required**: Yes

### PublishStatus
- **Type**: typing.Literal['DRAFT', 'PUBLISHED']
- **Required**: Yes


# UpdateSecurityProfileRequestTypeDef

### SecurityProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowedAccessControlTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TagRestrictedResources
- **Type**: typing.Optional[typing.Sequence[str]]

### Applications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.ApplicationUnionTypeDef]]

### HierarchyRestrictedResources
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowedAccessControlHierarchyGroupId
- **Type**: typing.Optional[str]


# UpdateTaskTemplateRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateConstraintsUnionTypeDef]

### Defaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateDefaultsUnionTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### Fields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateFieldUnionTypeDef]]


# UpdateTaskTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TaskTemplateConstraintsOutputTypeDef'>
- **Required**: Yes

### Defaults
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.TaskTemplateDefaultsOutputTypeDef'>
- **Required**: Yes

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_classes.TaskTemplateFieldOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrafficDistributionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### TelephonyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.TelephonyConfigUnionTypeDef]

### SignInConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.SignInConfigUnionTypeDef]

### AgentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentConfigUnionTypeDef]


# UpdateUserHierarchyGroupNameRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HierarchyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserHierarchyRequestTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### HierarchyGroupId
- **Type**: typing.Optional[str]


# UpdateUserHierarchyStructureRequestTypeDef

### HierarchyStructure
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.HierarchyStructureUpdateTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserIdentityInfoRequestTypeDef

### IdentityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.UserIdentityInfoTypeDef'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserPhoneConfigRequestTypeDef

### PhoneConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.UserPhoneConfigTypeDef'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserProficienciesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProficiencies
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.connect_classes.UserProficiencyTypeDef]
- **Required**: Yes


# UpdateUserRoutingProfileRequestTypeDef

### RoutingProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserSecurityProfilesRequestTypeDef

### SecurityProfileIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateViewContentRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ViewInputContentTypeDef'>
- **Required**: Yes


# UpdateViewContentResponseTypeDef

### View
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ViewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateViewMetadataRequestTypeDef

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


# UploadUrlMetadataTypeDef

### Url
- **Type**: typing.Optional[str]

### UrlExpiry
- **Type**: typing.Optional[str]

### HeadersToInclude
- **Type**: typing.Optional[typing.Dict[str, str]]


# UrlReferenceTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UseCaseTypeDef

### UseCaseId
- **Type**: typing.Optional[str]

### UseCaseArn
- **Type**: typing.Optional[str]

### UseCaseType
- **Type**: typing.Optional[typing.Literal['CONNECT_CAMPAIGNS', 'RULES_EVALUATION']]


# UserDataFiltersTypeDef

### Queues
- **Type**: typing.Optional[typing.Sequence[str]]

### ContactFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ContactFilterTypeDef]

### RoutingProfiles
- **Type**: typing.Optional[typing.Sequence[str]]

### Agents
- **Type**: typing.Optional[typing.Sequence[str]]

### UserHierarchyGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# UserDataTypeDef

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserReferenceTypeDef]

### RoutingProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.RoutingProfileReferenceTypeDef]

### HierarchyPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyPathReferenceTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.AgentStatusReferenceTypeDef]

### AvailableSlotsByChannel
- **Type**: typing.Optional[typing.Dict[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE'], int]]

### MaxSlotsByChannel
- **Type**: typing.Optional[typing.Dict[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE'], int]]

### ActiveSlotsByChannel
- **Type**: typing.Optional[typing.Dict[typing.Literal['CHAT', 'EMAIL', 'TASK', 'VOICE'], int]]

### Contacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_classes.AgentContactReferenceTypeDef]]

### NextStatus
- **Type**: typing.Optional[str]


# UserHierarchyGroupSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# UserHierarchyGroupSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]


# UserHierarchyGroupSearchFilterTypeDef

### AttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneAttributeFilterTypeDef]


# UserIdentityInfoLiteTypeDef

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]


# UserIdentityInfoTypeDef

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


# UserInfoTypeDef

### UserId
- **Type**: typing.Optional[str]


# UserPhoneConfigTypeDef

### PhoneType
- **Type**: typing.Literal['DESK_PHONE', 'SOFT_PHONE']
- **Required**: Yes

### AutoAccept
- **Type**: typing.Optional[bool]

### AfterContactWorkTimeLimit
- **Type**: typing.Optional[int]

### DeskPhoneNumber
- **Type**: typing.Optional[str]


# UserProficiencyDisassociateTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# UserProficiencyTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes

### Level
- **Type**: <class 'float'>
- **Required**: Yes


# UserQuickConnectConfigTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# UserReferenceTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# UserSearchCriteriaPaginatorTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### ListCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ListConditionTypeDef]

### HierarchyGroupCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupConditionTypeDef]


# UserSearchCriteriaTypeDef

### OrConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### AndConditions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### StringCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.StringConditionTypeDef]

### ListCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ListConditionTypeDef]

### HierarchyGroupCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.HierarchyGroupConditionTypeDef]


# UserSearchFilterTypeDef

### TagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneTagFilterTypeDef]

### UserAttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.ControlPlaneUserAttributeFilterTypeDef]


# UserSearchSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### DirectoryUserId
- **Type**: typing.Optional[str]

### HierarchyGroupId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### IdentityInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserIdentityInfoLiteTypeDef]

### PhoneConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserPhoneConfigTypeDef]

### RoutingProfileId
- **Type**: typing.Optional[str]

### SecurityProfileIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Username
- **Type**: typing.Optional[str]


# UserSummaryTypeDef

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


# UserTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### IdentityInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserIdentityInfoTypeDef]

### PhoneConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_classes.UserPhoneConfigTypeDef]

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


# ViewContentTypeDef

### InputSchema
- **Type**: typing.Optional[str]

### Template
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.List[str]]


# ViewInputContentTypeDef

### Template
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.Sequence[str]]


# ViewSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ViewTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ViewVersionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VocabularySummaryTypeDef

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


# VocabularyTypeDef

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


# VoiceRecordingConfigurationTypeDef

### VoiceRecordingTrack
- **Type**: typing.Optional[typing.Literal['ALL', 'FROM_AGENT', 'TO_AGENT']]

### IvrRecordingTrack
- **Type**: typing.Optional[typing.Literal['ALL']]


# WisdomInfoTypeDef

### SessionArn
- **Type**: typing.Optional[str]


