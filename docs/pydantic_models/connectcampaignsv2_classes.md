# Connectcampaignsv2 Classes

# AnswerMachineDetectionConfig

### enableAnswerMachineDetection
- **Type**: <class 'bool'>
- **Required**: Yes

### awaitAnswerMachinePrompt
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Campaign

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### channelSubtypeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ChannelSubtypeConfigOutput'>
- **Required**: Yes

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.Source]

### connectCampaignFlowArn
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ScheduleOutput]

### communicationTimeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationTimeConfigOutput]

### communicationLimitsOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimitsConfigOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CampaignFilters

### instanceIdFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.InstanceIdFilter]


# CampaignSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### channelSubtypes
- **Type**: typing.List[typing.Literal['EMAIL', 'SMS', 'TELEPHONY']]
- **Required**: Yes

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ScheduleOutput]

### connectCampaignFlowArn
- **Type**: typing.Optional[str]


# ChannelSubtypeConfig

### telephony
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TelephonyChannelSubtypeConfig]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SmsChannelSubtypeConfig]

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EmailChannelSubtypeConfig]


# ChannelSubtypeConfigOutput

### telephony
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TelephonyChannelSubtypeConfigOutput]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SmsChannelSubtypeConfigOutput]

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EmailChannelSubtypeConfigOutput]


# ChannelSubtypeParameters

### telephony
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TelephonyChannelSubtypeParameters]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SmsChannelSubtypeParameters]

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EmailChannelSubtypeParameters]


# CommunicationLimit

### maxCountPerRecipient
- **Type**: <class 'int'>
- **Required**: Yes

### frequency
- **Type**: <class 'int'>
- **Required**: Yes

### unit
- **Type**: typing.Literal['DAY']
- **Required**: Yes


# CommunicationLimits

### communicationLimitsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimit]]


# CommunicationLimitsConfig

### allChannelSubtypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimits]


# CommunicationLimitsConfigOutput

### allChannelSubtypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimitsOutput]


# CommunicationLimitsOutput

### communicationLimitsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimit]]


# CommunicationTimeConfig

### localTimeZoneConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.LocalTimeZoneConfig'>
- **Required**: Yes

### telephony
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TimeWindow]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TimeWindow]

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TimeWindow]


# CommunicationTimeConfigOutput

### localTimeZoneConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.LocalTimeZoneConfigOutput'>
- **Required**: Yes

### telephony
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TimeWindowOutput]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TimeWindowOutput]

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TimeWindowOutput]


# CreateCampaignRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### channelSubtypeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ChannelSubtypeConfig, aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ChannelSubtypeConfigOutput]
- **Required**: Yes

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.Source]

### connectCampaignFlowArn
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.Schedule, aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ScheduleOutput, NoneType]

### communicationTimeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationTimeConfig, aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationTimeConfigOutput, NoneType]

### communicationLimitsOverride
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimitsConfig, aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimitsConfigOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCampaignResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerProfilesIntegrationConfig

### domainArn
- **Type**: <class 'str'>
- **Required**: Yes

### objectTypeNames
- **Type**: typing.Dict[typing.Literal['Campaign-Email', 'Campaign-Orchestration', 'Campaign-SMS', 'Campaign-Telephony'], str]
- **Required**: Yes


# CustomerProfilesIntegrationIdentifier

### domainArn
- **Type**: <class 'str'>
- **Required**: Yes


# CustomerProfilesIntegrationSummary

### domainArn
- **Type**: <class 'str'>
- **Required**: Yes

### objectTypeNames
- **Type**: typing.Dict[typing.Literal['Campaign-Email', 'Campaign-Orchestration', 'Campaign-SMS', 'Campaign-Telephony'], str]
- **Required**: Yes


# DeleteCampaignChannelSubtypeConfigRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS', 'TELEPHONY']
- **Required**: Yes


# DeleteCampaignCommunicationLimitsRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### config
- **Type**: typing.Literal['ALL_CHANNEL_SUBTYPES']
- **Required**: Yes


# DeleteCampaignCommunicationTimeRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### config
- **Type**: typing.Literal['EMAIL', 'SMS', 'TELEPHONY']
- **Required**: Yes


# DeleteCampaignRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectInstanceConfigRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### campaignDeletionPolicy
- **Type**: typing.Optional[typing.Literal['DELETE_ALL', 'RETAIN_ALL']]


# DeleteConnectInstanceIntegrationRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### integrationIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.IntegrationIdentifier'>
- **Required**: Yes


# DeleteInstanceOnboardingJobRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCampaignRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCampaignResponse

### campaign
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.Campaign'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# EmailChannelSubtypeConfig

### outboundMode
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EmailOutboundMode'>
- **Required**: Yes

### defaultOutboundConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EmailOutboundConfig'>
- **Required**: Yes

### capacity
- **Type**: typing.Optional[float]


# EmailChannelSubtypeConfigOutput

### outboundMode
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EmailOutboundModeOutput'>
- **Required**: Yes

### defaultOutboundConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EmailOutboundConfig'>
- **Required**: Yes

### capacity
- **Type**: typing.Optional[float]


# EmailChannelSubtypeParameters

### destinationEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### templateParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### connectSourceEmailAddress
- **Type**: typing.Optional[str]

### templateArn
- **Type**: typing.Optional[str]


# EmailOutboundConfig

### connectSourceEmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### wisdomTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceEmailAddressDisplayName
- **Type**: typing.Optional[str]


# EmailOutboundMode

### agentless
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# EmailOutboundModeOutput

### agentless
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionConfig

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### encryptionType
- **Type**: typing.Optional[typing.Literal['KMS']]

### keyArn
- **Type**: typing.Optional[str]


# EventTrigger

### customerProfilesDomainArn
- **Type**: typing.Optional[str]


# FailedCampaignStateResponse

### campaignId
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['ResourceNotFound', 'UnknownError']]


# FailedProfileOutboundRequest

### clientToken
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['Conflict', 'InvalidInput', 'RequestThrottled', 'ResourceNotFound', 'UnknownError']]


# FailedRequest

### clientToken
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['BufferLimitExceeded', 'InvalidInput', 'RequestThrottled', 'UnknownError']]


# GetCampaignStateBatchRequest

### campaignIds
- **Type**: typing.List[str]
- **Required**: Yes


# GetCampaignStateBatchResponse

### successfulRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SuccessfulCampaignStateResponse]
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.FailedCampaignStateResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetCampaignStateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCampaignStateResponse

### state
- **Type**: typing.Literal['Completed', 'Failed', 'Initialized', 'Paused', 'Running', 'Stopped']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectInstanceConfigRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectInstanceConfigResponse

### connectInstanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.InstanceConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceOnboardingJobStatusRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceOnboardingJobStatusResponse

### connectInstanceOnboardingJobStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.InstanceOnboardingJobStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceConfig

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceLinkedRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EncryptionConfig'>
- **Required**: Yes


# InstanceIdFilter

### value
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['Eq']
- **Required**: Yes


# InstanceOnboardingJobStatus

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### failureCode
- **Type**: typing.Optional[typing.Literal['EVENT_BRIDGE_ACCESS_DENIED', 'EVENT_BRIDGE_MANAGED_RULE_LIMIT_EXCEEDED', 'IAM_ACCESS_DENIED', 'INTERNAL_FAILURE', 'KMS_ACCESS_DENIED', 'KMS_KEY_NOT_FOUND']]


# IntegrationConfig

### customerProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CustomerProfilesIntegrationConfig]

### qConnect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.QConnectIntegrationConfig]


# IntegrationIdentifier

### customerProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CustomerProfilesIntegrationIdentifier]

### qConnect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.QConnectIntegrationIdentifier]


# IntegrationSummary

### customerProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CustomerProfilesIntegrationSummary]

### qConnect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.QConnectIntegrationSummary]


# ListCampaignsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CampaignFilters]


# ListCampaignsRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CampaignFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.PaginatorConfig]


# ListCampaignsResponse

### campaignSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CampaignSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConnectInstanceIntegrationsRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectInstanceIntegrationsRequestPaginate

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.PaginatorConfig]


# ListConnectInstanceIntegrationsResponse

### integrationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.IntegrationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# LocalTimeZoneConfig

### defaultTimeZone
- **Type**: typing.Optional[str]

### localTimeZoneDetection
- **Type**: typing.Optional[typing.List[typing.Literal['AREA_CODE', 'ZIP_CODE']]]


# LocalTimeZoneConfigOutput

### defaultTimeZone
- **Type**: typing.Optional[str]

### localTimeZoneDetection
- **Type**: typing.Optional[typing.List[typing.Literal['AREA_CODE', 'ZIP_CODE']]]


# OpenHours

### dailyHours
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TimeRange]]]


# OpenHoursOutput

### dailyHours
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TimeRange]]]


# OutboundRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### expirationTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### channelSubtypeParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ChannelSubtypeParameters'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PauseCampaignRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# PredictiveConfig

### bandwidthAllocation
- **Type**: <class 'float'>
- **Required**: Yes


# ProfileOutboundRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### profileId
- **Type**: <class 'str'>
- **Required**: Yes

### expirationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ProgressiveConfig

### bandwidthAllocation
- **Type**: <class 'float'>
- **Required**: Yes


# PutConnectInstanceIntegrationRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### integrationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.IntegrationConfig'>
- **Required**: Yes


# PutOutboundRequestBatchRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### outboundRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.OutboundRequest]
- **Required**: Yes


# PutOutboundRequestBatchResponse

### successfulRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SuccessfulRequest]
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.FailedRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# PutProfileOutboundRequestBatchRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### profileOutboundRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ProfileOutboundRequest]
- **Required**: Yes


# PutProfileOutboundRequestBatchResponse

### successfulRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SuccessfulProfileOutboundRequest]
- **Required**: Yes

### failedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.FailedProfileOutboundRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# QConnectIntegrationConfig

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes


# QConnectIntegrationIdentifier

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes


# QConnectIntegrationSummary

### knowledgeBaseArn
- **Type**: <class 'str'>
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


# RestrictedPeriod

### startDate
- **Type**: <class 'str'>
- **Required**: Yes

### endDate
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# RestrictedPeriods

### restrictedPeriodList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.RestrictedPeriod]]


# RestrictedPeriodsOutput

### restrictedPeriodList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.RestrictedPeriod]]


# ResumeCampaignRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# Schedule

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### refreshFrequency
- **Type**: typing.Optional[str]


# ScheduleOutput

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### refreshFrequency
- **Type**: typing.Optional[str]


# SmsChannelSubtypeConfig

### outboundMode
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SmsOutboundMode'>
- **Required**: Yes

### defaultOutboundConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SmsOutboundConfig'>
- **Required**: Yes

### capacity
- **Type**: typing.Optional[float]


# SmsChannelSubtypeConfigOutput

### outboundMode
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SmsOutboundModeOutput'>
- **Required**: Yes

### defaultOutboundConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.SmsOutboundConfig'>
- **Required**: Yes

### capacity
- **Type**: typing.Optional[float]


# SmsChannelSubtypeParameters

### destinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### templateParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### connectSourcePhoneNumberArn
- **Type**: typing.Optional[str]

### templateArn
- **Type**: typing.Optional[str]


# SmsOutboundConfig

### connectSourcePhoneNumberArn
- **Type**: <class 'str'>
- **Required**: Yes

### wisdomTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# SmsOutboundMode

### agentless
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# SmsOutboundModeOutput

### agentless
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# Source

### customerProfilesSegmentArn
- **Type**: typing.Optional[str]

### eventTrigger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EventTrigger]


# StartCampaignRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StartInstanceOnboardingJobRequest

### connectInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.EncryptionConfig'>
- **Required**: Yes


# StartInstanceOnboardingJobResponse

### connectInstanceOnboardingJobStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.InstanceOnboardingJobStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ResponseMetadata'>
- **Required**: Yes


# StopCampaignRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# SuccessfulCampaignStateResponse

### campaignId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'Initialized', 'Paused', 'Running', 'Stopped']]


# SuccessfulProfileOutboundRequest

### clientToken
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# SuccessfulRequest

### clientToken
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# TagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TelephonyChannelSubtypeConfig

### outboundMode
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TelephonyOutboundMode'>
- **Required**: Yes

### defaultOutboundConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TelephonyOutboundConfig'>
- **Required**: Yes

### capacity
- **Type**: typing.Optional[float]

### connectQueueId
- **Type**: typing.Optional[str]


# TelephonyChannelSubtypeConfigOutput

### outboundMode
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TelephonyOutboundModeOutput'>
- **Required**: Yes

### defaultOutboundConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.TelephonyOutboundConfig'>
- **Required**: Yes

### capacity
- **Type**: typing.Optional[float]

### connectQueueId
- **Type**: typing.Optional[str]


# TelephonyChannelSubtypeParameters

### destinationPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### connectSourcePhoneNumber
- **Type**: typing.Optional[str]

### answerMachineDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.AnswerMachineDetectionConfig]


# TelephonyOutboundConfig

### connectContactFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### connectSourcePhoneNumber
- **Type**: typing.Optional[str]

### answerMachineDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.AnswerMachineDetectionConfig]


# TelephonyOutboundMode

### progressive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ProgressiveConfig]

### predictive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.PredictiveConfig]

### agentless
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TelephonyOutboundModeOutput

### progressive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ProgressiveConfig]

### predictive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.PredictiveConfig]

### agentless
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TimeRange

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'str'>
- **Required**: Yes


# TimeWindow

### openHours
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.OpenHours'>
- **Required**: Yes

### restrictedPeriods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.RestrictedPeriods]


# TimeWindowOutput

### openHours
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.OpenHoursOutput'>
- **Required**: Yes

### restrictedPeriods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.RestrictedPeriodsOutput]


# UntagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCampaignChannelSubtypeConfigRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### channelSubtypeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ChannelSubtypeConfig, aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ChannelSubtypeConfigOutput]
- **Required**: Yes


# UpdateCampaignCommunicationLimitsRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### communicationLimitsOverride
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimitsConfig, aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationLimitsConfigOutput]
- **Required**: Yes


# UpdateCampaignCommunicationTimeRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### communicationTimeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationTimeConfig, aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.CommunicationTimeConfigOutput]
- **Required**: Yes


# UpdateCampaignFlowAssociationRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### connectCampaignFlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCampaignNameRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCampaignScheduleRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.Schedule, aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.ScheduleOutput]
- **Required**: Yes


# UpdateCampaignSourceRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.connectcampaignsv2.connectcampaignsv2_classes.Source'>
- **Required**: Yes


