# Pydantic Models in pinpoint_classes

# ADMChannelRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]


# ADMChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# ADMMessageTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### ConsolidationKey
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ExpiresAfter
- **Type**: typing.Optional[str]

### IconReference
- **Type**: typing.Optional[str]

### ImageIconUrl
- **Type**: typing.Optional[str]

### ImageUrl
- **Type**: typing.Optional[str]

### MD5
- **Type**: typing.Optional[str]

### RawContent
- **Type**: typing.Optional[str]

### SilentPush
- **Type**: typing.Optional[bool]

### SmallImageIconUrl
- **Type**: typing.Optional[str]

### Sound
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# APNSChannelRequestTypeDef

### BundleId
- **Type**: typing.Optional[str]

### Certificate
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### PrivateKey
- **Type**: typing.Optional[str]

### TeamId
- **Type**: typing.Optional[str]

### TokenKey
- **Type**: typing.Optional[str]

### TokenKeyId
- **Type**: typing.Optional[str]


# APNSChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### HasTokenKey
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# APNSMessageTypeDef

### APNSPushType
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Badge
- **Type**: typing.Optional[int]

### Body
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### CollapseId
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Mapping[str, str]]

### MediaUrl
- **Type**: typing.Optional[str]

### PreferredAuthenticationMethod
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[str]

### RawContent
- **Type**: typing.Optional[str]

### SilentPush
- **Type**: typing.Optional[bool]

### Sound
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### ThreadId
- **Type**: typing.Optional[str]

### TimeToLive
- **Type**: typing.Optional[int]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# APNSPushNotificationTemplateTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### MediaUrl
- **Type**: typing.Optional[str]

### RawContent
- **Type**: typing.Optional[str]

### Sound
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# APNSSandboxChannelRequestTypeDef

### BundleId
- **Type**: typing.Optional[str]

### Certificate
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### PrivateKey
- **Type**: typing.Optional[str]

### TeamId
- **Type**: typing.Optional[str]

### TokenKey
- **Type**: typing.Optional[str]

### TokenKeyId
- **Type**: typing.Optional[str]


# APNSSandboxChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### HasTokenKey
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# APNSVoipChannelRequestTypeDef

### BundleId
- **Type**: typing.Optional[str]

### Certificate
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### PrivateKey
- **Type**: typing.Optional[str]

### TeamId
- **Type**: typing.Optional[str]

### TokenKey
- **Type**: typing.Optional[str]

### TokenKeyId
- **Type**: typing.Optional[str]


# APNSVoipChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### HasTokenKey
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# APNSVoipSandboxChannelRequestTypeDef

### BundleId
- **Type**: typing.Optional[str]

### Certificate
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### PrivateKey
- **Type**: typing.Optional[str]

### TeamId
- **Type**: typing.Optional[str]

### TokenKey
- **Type**: typing.Optional[str]

### TokenKeyId
- **Type**: typing.Optional[str]


# APNSVoipSandboxChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### HasTokenKey
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# ActivitiesResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ActivityResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ActivityOutputTypeDef

### CUSTOM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CustomMessageActivityOutputTypeDef]

### ConditionalSplit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ConditionalSplitActivityOutputTypeDef]

### Description
- **Type**: typing.Optional[str]

### EMAIL
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EmailMessageActivityTypeDef]

### Holdout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.HoldoutActivityTypeDef]

### MultiCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MultiConditionalSplitActivityOutputTypeDef]

### PUSH
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.PushMessageActivityTypeDef]

### RandomSplit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.RandomSplitActivityOutputTypeDef]

### SMS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SMSMessageActivityTypeDef]

### Wait
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.WaitActivityTypeDef]

### ContactCenter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ContactCenterActivityTypeDef]


# ActivityResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### End
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[str]

### ScheduledStart
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### SuccessfulEndpointCount
- **Type**: typing.Optional[int]

### TimezonesCompletedCount
- **Type**: typing.Optional[int]

### TimezonesTotalCount
- **Type**: typing.Optional[int]

### TotalEndpointCount
- **Type**: typing.Optional[int]

### TreatmentId
- **Type**: typing.Optional[str]

### ExecutionMetrics
- **Type**: typing.Optional[typing.Dict[str, str]]


# ActivityTypeDef

### CUSTOM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CustomMessageActivityTypeDef]

### ConditionalSplit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ConditionalSplitActivityTypeDef]

### Description
- **Type**: typing.Optional[str]

### EMAIL
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EmailMessageActivityTypeDef]

### Holdout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.HoldoutActivityTypeDef]

### MultiCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MultiConditionalSplitActivityTypeDef]

### PUSH
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.PushMessageActivityTypeDef]

### RandomSplit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.RandomSplitActivityTypeDef]

### SMS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SMSMessageActivityTypeDef]

### Wait
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.WaitActivityTypeDef]

### ContactCenter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ContactCenterActivityTypeDef]


# AddressConfigurationTypeDef

### BodyOverride
- **Type**: typing.Optional[str]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RawContent
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### TitleOverride
- **Type**: typing.Optional[str]


# AndroidPushNotificationTemplateTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### ImageIconUrl
- **Type**: typing.Optional[str]

### ImageUrl
- **Type**: typing.Optional[str]

### RawContent
- **Type**: typing.Optional[str]

### SmallImageIconUrl
- **Type**: typing.Optional[str]

### Sound
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ApplicationDateRangeKpiResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KpiName
- **Type**: <class 'str'>
- **Required**: Yes

### KpiResult
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.BaseKpiResultTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ApplicationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreationDate
- **Type**: typing.Optional[str]


# ApplicationSettingsJourneyLimitsTypeDef

### DailyCap
- **Type**: typing.Optional[int]

### TimeframeCap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyTimeframeCapTypeDef]

### TotalCap
- **Type**: typing.Optional[int]


# ApplicationSettingsResourceTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignHookTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignLimitsTypeDef]

### QuietTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.QuietTimeTypeDef]

### JourneyLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationSettingsJourneyLimitsTypeDef]


# ApplicationsResponseTypeDef

### Item
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationResponseTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# AttributeDimensionOutputTypeDef

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### AttributeType
- **Type**: typing.Optional[typing.Literal['AFTER', 'BEFORE', 'BETWEEN', 'CONTAINS', 'EXCLUSIVE', 'INCLUSIVE', 'ON']]


# AttributeDimensionTypeDef

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AttributeType
- **Type**: typing.Optional[typing.Literal['AFTER', 'BEFORE', 'BETWEEN', 'CONTAINS', 'EXCLUSIVE', 'INCLUSIVE', 'ON']]


# AttributesResourceTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeType
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.List[str]]


# BaiduChannelRequestTypeDef

### ApiKey
- **Type**: <class 'str'>
- **Required**: Yes

### SecretKey
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]


# BaiduChannelResponseTypeDef

### Credential
- **Type**: <class 'str'>
- **Required**: Yes

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# BaiduMessageTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Mapping[str, str]]

### IconReference
- **Type**: typing.Optional[str]

### ImageIconUrl
- **Type**: typing.Optional[str]

### ImageUrl
- **Type**: typing.Optional[str]

### RawContent
- **Type**: typing.Optional[str]

### SilentPush
- **Type**: typing.Optional[bool]

### SmallImageIconUrl
- **Type**: typing.Optional[str]

### Sound
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### TimeToLive
- **Type**: typing.Optional[int]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# BaseKpiResultTypeDef

### Rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ResultRowTypeDef]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CampaignCustomMessageTypeDef

### Data
- **Type**: typing.Optional[str]


# CampaignDateRangeKpiResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KpiName
- **Type**: <class 'str'>
- **Required**: Yes

### KpiResult
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.BaseKpiResultTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CampaignEmailMessageOutputTypeDef

### Body
- **Type**: typing.Optional[str]

### FromAddress
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.MessageHeaderTypeDef]]

### HtmlBody
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]


# CampaignEmailMessageTypeDef

### Body
- **Type**: typing.Optional[str]

### FromAddress
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.MessageHeaderTypeDef]]

### HtmlBody
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]


# CampaignEventFilterOutputTypeDef

### Dimensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventDimensionsOutputTypeDef'>
- **Required**: Yes

### FilterType
- **Type**: typing.Literal['ENDPOINT', 'SYSTEM']
- **Required**: Yes


# CampaignEventFilterTypeDef

### Dimensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventDimensionsTypeDef'>
- **Required**: Yes

### FilterType
- **Type**: typing.Literal['ENDPOINT', 'SYSTEM']
- **Required**: Yes


# CampaignHookTypeDef

### LambdaFunctionName
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['DELIVERY', 'FILTER']]

### WebUrl
- **Type**: typing.Optional[str]


# CampaignInAppMessageOutputTypeDef

### Body
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageContentTypeDef]]

### CustomConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]


# CampaignInAppMessageTypeDef

### Body
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageContentTypeDef]]

### CustomConfig
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]


# CampaignLimitsTypeDef

### Daily
- **Type**: typing.Optional[int]

### MaximumDuration
- **Type**: typing.Optional[int]

### MessagesPerSecond
- **Type**: typing.Optional[int]

### Total
- **Type**: typing.Optional[int]

### Session
- **Type**: typing.Optional[int]


# CampaignResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentVersion
- **Type**: <class 'int'>
- **Required**: Yes

### AdditionalTreatments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.TreatmentResourceTypeDef]]

### CustomDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CustomDeliveryConfigurationOutputTypeDef]

### DefaultState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignStateTypeDef]

### Description
- **Type**: typing.Optional[str]

### HoldoutPercent
- **Type**: typing.Optional[int]

### Hook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignHookTypeDef]

### IsPaused
- **Type**: typing.Optional[bool]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignLimitsTypeDef]

### MessageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageConfigurationOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ScheduleOutputTypeDef]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignStateTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateConfigurationTypeDef]

### TreatmentDescription
- **Type**: typing.Optional[str]

### TreatmentName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Priority
- **Type**: typing.Optional[int]


# CampaignSmsMessageTypeDef

### Body
- **Type**: typing.Optional[str]

### MessageType
- **Type**: typing.Optional[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]

### OriginationNumber
- **Type**: typing.Optional[str]

### SenderId
- **Type**: typing.Optional[str]

### EntityId
- **Type**: typing.Optional[str]

### TemplateId
- **Type**: typing.Optional[str]


# CampaignStateTypeDef

### CampaignStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'EXECUTING', 'INVALID', 'PAUSED', 'PENDING_NEXT_RUN', 'SCHEDULED']]


# CampaignsResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ChannelResponseTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# ChannelsResponseTypeDef

### Channels
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.ChannelResponseTypeDef]
- **Required**: Yes


# ClosedDaysOutputTypeDef

### EMAIL
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]

### SMS
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]

### PUSH
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]

### VOICE
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]

### CUSTOM
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]


# ClosedDaysRuleTypeDef

### Name
- **Type**: typing.Optional[str]

### StartDateTime
- **Type**: typing.Optional[str]

### EndDateTime
- **Type**: typing.Optional[str]


# ClosedDaysTypeDef

### EMAIL
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]

### SMS
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]

### PUSH
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]

### VOICE
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]

### CUSTOM
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysRuleTypeDef]]


# ConditionOutputTypeDef

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.SimpleConditionOutputTypeDef]]

### Operator
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY']]


# ConditionTypeDef

### Conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.SimpleConditionTypeDef]]

### Operator
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY']]


# ConditionalSplitActivityOutputTypeDef

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ConditionOutputTypeDef]

### EvaluationWaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.WaitTimeTypeDef]

### FalseActivity
- **Type**: typing.Optional[str]

### TrueActivity
- **Type**: typing.Optional[str]


# ConditionalSplitActivityTypeDef

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ConditionTypeDef]

### EvaluationWaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.WaitTimeTypeDef]

### FalseActivity
- **Type**: typing.Optional[str]

### TrueActivity
- **Type**: typing.Optional[str]


# ContactCenterActivityTypeDef

### NextActivity
- **Type**: typing.Optional[str]


# CreateAppRequestRequestTypeDef

### CreateApplicationRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CreateApplicationRequestTypeDef'>
- **Required**: Yes


# CreateAppResponseTypeDef

### ApplicationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApplicationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCampaignRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteCampaignRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.WriteCampaignRequestTypeDef'>
- **Required**: Yes


# CreateCampaignResponseTypeDef

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CampaignResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEmailTemplateRequestRequestTypeDef

### EmailTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EmailTemplateRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateEmailTemplateResponseTypeDef

### CreateTemplateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CreateTemplateMessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExportJobRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportJobRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ExportJobRequestTypeDef'>
- **Required**: Yes


# CreateExportJobResponseTypeDef

### ExportJobResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ExportJobResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImportJobRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportJobRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ImportJobRequestTypeDef'>
- **Required**: Yes


# CreateImportJobResponseTypeDef

### ImportJobResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ImportJobResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInAppTemplateRequestRequestTypeDef

### InAppTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.InAppTemplateRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateInAppTemplateResponseTypeDef

### TemplateCreateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.TemplateCreateMessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJourneyRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteJourneyRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.WriteJourneyRequestTypeDef'>
- **Required**: Yes


# CreateJourneyResponseTypeDef

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePushTemplateRequestRequestTypeDef

### PushNotificationTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.PushNotificationTemplateRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePushTemplateResponseTypeDef

### CreateTemplateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CreateTemplateMessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRecommenderConfigurationRequestRequestTypeDef

### CreateRecommenderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CreateRecommenderConfigurationTypeDef'>
- **Required**: Yes


# CreateRecommenderConfigurationResponseTypeDef

### RecommenderConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.RecommenderConfigurationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRecommenderConfigurationTypeDef

### RecommendationProviderRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationProviderUri
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RecommendationProviderIdType
- **Type**: typing.Optional[str]

### RecommendationTransformerUri
- **Type**: typing.Optional[str]

### RecommendationsDisplayName
- **Type**: typing.Optional[str]

### RecommendationsPerMessage
- **Type**: typing.Optional[int]


# CreateSegmentRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteSegmentRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.WriteSegmentRequestTypeDef'>
- **Required**: Yes


# CreateSegmentResponseTypeDef

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SegmentResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSmsTemplateRequestRequestTypeDef

### SMSTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SMSTemplateRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSmsTemplateResponseTypeDef

### CreateTemplateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CreateTemplateMessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTemplateMessageBodyTypeDef

### Arn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### RequestID
- **Type**: typing.Optional[str]


# CreateVoiceTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VoiceTemplateRequestTypeDef'>
- **Required**: Yes


# CreateVoiceTemplateResponseTypeDef

### CreateTemplateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CreateTemplateMessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomDeliveryConfigurationOutputTypeDef

### DeliveryUri
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]]


# CustomDeliveryConfigurationTypeDef

### DeliveryUri
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]]


# CustomMessageActivityOutputTypeDef

### DeliveryUri
- **Type**: typing.Optional[str]

### EndpointTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]]

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyCustomMessageTypeDef]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# CustomMessageActivityTypeDef

### DeliveryUri
- **Type**: typing.Optional[str]

### EndpointTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]]

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyCustomMessageTypeDef]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# DefaultButtonConfigurationTypeDef

### ButtonAction
- **Type**: typing.Literal['CLOSE', 'DEEP_LINK', 'LINK']
- **Required**: Yes

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### BackgroundColor
- **Type**: typing.Optional[str]

### BorderRadius
- **Type**: typing.Optional[int]

### Link
- **Type**: typing.Optional[str]

### TextColor
- **Type**: typing.Optional[str]


# DefaultMessageTypeDef

### Body
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# DefaultPushNotificationMessageTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SilentPush
- **Type**: typing.Optional[bool]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# DefaultPushNotificationTemplateTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### Sound
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# DeleteAdmChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAdmChannelResponseTypeDef

### ADMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ADMChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApnsChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApnsChannelResponseTypeDef

### APNSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApnsSandboxChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApnsSandboxChannelResponseTypeDef

### APNSSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSSandboxChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApnsVoipChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApnsVoipChannelResponseTypeDef

### APNSVoipChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSVoipChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApnsVoipSandboxChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApnsVoipSandboxChannelResponseTypeDef

### APNSVoipSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSVoipSandboxChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppResponseTypeDef

### ApplicationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBaiduChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBaiduChannelResponseTypeDef

### BaiduChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.BaiduChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCampaignRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCampaignResponseTypeDef

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CampaignResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEmailChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailChannelResponseTypeDef

### EmailChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EmailChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeleteEmailTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEndpointRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointResponseTypeDef

### EndpointResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EndpointResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEventStreamRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventStreamResponseTypeDef

### EventStream
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventStreamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGcmChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGcmChannelResponseTypeDef

### GCMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.GCMChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInAppTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeleteInAppTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteJourneyRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJourneyResponseTypeDef

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePushTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeletePushTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRecommenderConfigurationRequestRequestTypeDef

### RecommenderId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecommenderConfigurationResponseTypeDef

### RecommenderConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.RecommenderConfigurationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSegmentRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSegmentResponseTypeDef

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SegmentResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSmsChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSmsChannelResponseTypeDef

### SMSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SMSChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSmsTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeleteSmsTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUserEndpointsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserEndpointsResponseTypeDef

### EndpointsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EndpointsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVoiceChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceChannelResponseTypeDef

### VoiceChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VoiceChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVoiceTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeleteVoiceTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DirectMessageConfigurationTypeDef

### ADMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ADMMessageTypeDef]

### APNSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.APNSMessageTypeDef]

### BaiduMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.BaiduMessageTypeDef]

### DefaultMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.DefaultMessageTypeDef]

### DefaultPushNotificationMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.DefaultPushNotificationMessageTypeDef]

### EmailMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EmailMessageTypeDef]

### GCMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.GCMMessageTypeDef]

### SMSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SMSMessageTypeDef]

### VoiceMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.VoiceMessageTypeDef]


# EmailChannelRequestTypeDef

### FromAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationSet
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### RoleArn
- **Type**: typing.Optional[str]

### OrchestrationSendingRoleArn
- **Type**: typing.Optional[str]


# EmailChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### ConfigurationSet
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### FromAddress
- **Type**: typing.Optional[str]

### HasCredential
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### Identity
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### MessagesPerSecond
- **Type**: typing.Optional[int]

### RoleArn
- **Type**: typing.Optional[str]

### OrchestrationSendingRoleArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# EmailMessageActivityTypeDef

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyEmailMessageTypeDef]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# EmailMessageTypeDef

### Body
- **Type**: typing.Optional[str]

### FeedbackForwardingAddress
- **Type**: typing.Optional[str]

### FromAddress
- **Type**: typing.Optional[str]

### RawEmail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.RawEmailTypeDef]

### ReplyToAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### SimpleEmail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SimpleEmailTypeDef]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# EmailTemplateRequestTypeDef

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### HtmlPart
- **Type**: typing.Optional[str]

### RecommenderId
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.MessageHeaderTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### TextPart
- **Type**: typing.Optional[str]


# EmailTemplateResponseTypeDef

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: typing.Literal['EMAIL', 'INAPP', 'PUSH', 'SMS', 'VOICE']
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### HtmlPart
- **Type**: typing.Optional[str]

### RecommenderId
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.MessageHeaderTypeDef]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### TextPart
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointBatchItemTypeDef

### Address
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointDemographicTypeDef]

### EffectiveDate
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointLocationTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Mapping[str, float]]

### OptOut
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointUserTypeDef]


# EndpointBatchRequestTypeDef

### Item
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointBatchItemTypeDef]
- **Required**: Yes


# EndpointDemographicTypeDef

### AppVersion
- **Type**: typing.Optional[str]

### Locale
- **Type**: typing.Optional[str]

### Make
- **Type**: typing.Optional[str]

### Model
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]


# EndpointItemResponseTypeDef

### Message
- **Type**: typing.Optional[str]

### StatusCode
- **Type**: typing.Optional[int]


# EndpointLocationTypeDef

### City
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### Latitude
- **Type**: typing.Optional[float]

### Longitude
- **Type**: typing.Optional[float]

### PostalCode
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# EndpointMessageResultTypeDef

### DeliveryStatus
- **Type**: typing.Literal['DUPLICATE', 'OPT_OUT', 'PERMANENT_FAILURE', 'SUCCESSFUL', 'TEMPORARY_FAILURE', 'THROTTLED', 'UNKNOWN_FAILURE']
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### Address
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### UpdatedToken
- **Type**: typing.Optional[str]


# EndpointRequestTypeDef

### Address
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointDemographicTypeDef]

### EffectiveDate
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointLocationTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Mapping[str, float]]

### OptOut
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointUserTypeDef]


# EndpointResponseTypeDef

### Address
- **Type**: typing.Optional[str]

### ApplicationId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### CohortId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointDemographicTypeDef]

### EffectiveDate
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointLocationTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### OptOut
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointUserOutputTypeDef]


# EndpointSendConfigurationTypeDef

### BodyOverride
- **Type**: typing.Optional[str]

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RawContent
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### TitleOverride
- **Type**: typing.Optional[str]


# EndpointUserOutputTypeDef

### UserAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### UserId
- **Type**: typing.Optional[str]


# EndpointUserTypeDef

### UserAttributes
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### UserId
- **Type**: typing.Optional[str]


# EndpointsResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointResponseTypeDef]
- **Required**: Yes


# EventConditionOutputTypeDef

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EventDimensionsOutputTypeDef]

### MessageActivity
- **Type**: typing.Optional[str]


# EventConditionTypeDef

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EventDimensionsTypeDef]

### MessageActivity
- **Type**: typing.Optional[str]


# EventDimensionsOutputTypeDef

### Attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.AttributeDimensionOutputTypeDef]]

### EventType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionOutputTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.MetricDimensionTypeDef]]


# EventDimensionsTypeDef

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.AttributeDimensionTypeDef]]

### EventType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.MetricDimensionTypeDef]]


# EventFilterOutputTypeDef

### Dimensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventDimensionsOutputTypeDef'>
- **Required**: Yes

### FilterType
- **Type**: typing.Literal['ENDPOINT', 'SYSTEM']
- **Required**: Yes


# EventFilterTypeDef

### Dimensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventDimensionsTypeDef'>
- **Required**: Yes

### FilterType
- **Type**: typing.Literal['ENDPOINT', 'SYSTEM']
- **Required**: Yes


# EventItemResponseTypeDef

### Message
- **Type**: typing.Optional[str]

### StatusCode
- **Type**: typing.Optional[int]


# EventStartConditionOutputTypeDef

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EventFilterOutputTypeDef]

### SegmentId
- **Type**: typing.Optional[str]


# EventStartConditionTypeDef

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EventFilterTypeDef]

### SegmentId
- **Type**: typing.Optional[str]


# EventStreamTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### LastUpdatedBy
- **Type**: typing.Optional[str]


# EventTypeDef

### EventType
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'str'>
- **Required**: Yes

### AppPackageName
- **Type**: typing.Optional[str]

### AppTitle
- **Type**: typing.Optional[str]

### AppVersionCode
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientSdkVersion
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.Mapping[str, float]]

### SdkName
- **Type**: typing.Optional[str]

### Session
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SessionTypeDef]


# EventsBatchTypeDef

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.PublicEndpointTypeDef'>
- **Required**: Yes

### Events
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.EventTypeDef]
- **Required**: Yes


# EventsRequestTypeDef

### BatchItem
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.EventsBatchTypeDef]
- **Required**: Yes


# EventsResponseTypeDef

### Results
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.ItemResponseTypeDef]]


# ExportJobRequestTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3UrlPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: typing.Optional[str]

### SegmentVersion
- **Type**: typing.Optional[int]


# ExportJobResourceTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3UrlPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: typing.Optional[str]

### SegmentVersion
- **Type**: typing.Optional[int]


# ExportJobResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ExportJobResourceTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'COMPLETING', 'CREATED', 'FAILED', 'FAILING', 'INITIALIZING', 'PENDING_JOB', 'PREPARING_FOR_INITIALIZATION', 'PROCESSING']
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### CompletedPieces
- **Type**: typing.Optional[int]

### CompletionDate
- **Type**: typing.Optional[str]

### FailedPieces
- **Type**: typing.Optional[int]

### Failures
- **Type**: typing.Optional[typing.List[str]]

### TotalFailures
- **Type**: typing.Optional[int]

### TotalPieces
- **Type**: typing.Optional[int]

### TotalProcessed
- **Type**: typing.Optional[int]


# ExportJobsResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ExportJobResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GCMChannelRequestTypeDef

### ApiKey
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### ServiceJson
- **Type**: typing.Optional[str]


# GCMChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Credential
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### HasFcmServiceCredentials
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# GCMMessageTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### CollapseKey
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Mapping[str, str]]

### IconReference
- **Type**: typing.Optional[str]

### ImageIconUrl
- **Type**: typing.Optional[str]

### ImageUrl
- **Type**: typing.Optional[str]

### PreferredAuthenticationMethod
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[str]

### RawContent
- **Type**: typing.Optional[str]

### RestrictedPackageName
- **Type**: typing.Optional[str]

### SilentPush
- **Type**: typing.Optional[bool]

### SmallImageIconUrl
- **Type**: typing.Optional[str]

### Sound
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### TimeToLive
- **Type**: typing.Optional[int]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# GPSCoordinatesTypeDef

### Latitude
- **Type**: <class 'float'>
- **Required**: Yes

### Longitude
- **Type**: <class 'float'>
- **Required**: Yes


# GPSPointDimensionTypeDef

### Coordinates
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.GPSCoordinatesTypeDef'>
- **Required**: Yes

### RangeInKilometers
- **Type**: typing.Optional[float]


# GetAdmChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdmChannelResponseTypeDef

### ADMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ADMChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApnsChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApnsChannelResponseTypeDef

### APNSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApnsSandboxChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApnsSandboxChannelResponseTypeDef

### APNSSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSSandboxChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApnsVoipChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApnsVoipChannelResponseTypeDef

### APNSVoipChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSVoipChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApnsVoipSandboxChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApnsVoipSandboxChannelResponseTypeDef

### APNSVoipSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSVoipSandboxChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppResponseTypeDef

### ApplicationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationDateRangeKpiRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### KpiName
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetApplicationDateRangeKpiResponseTypeDef

### ApplicationDateRangeKpiResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationDateRangeKpiResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationSettingsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationSettingsResponseTypeDef

### ApplicationSettingsResource
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationSettingsResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppsRequestRequestTypeDef

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetAppsResponseTypeDef

### ApplicationsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBaiduChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBaiduChannelResponseTypeDef

### BaiduChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.BaiduChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCampaignActivitiesRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetCampaignActivitiesResponseTypeDef

### ActivitiesResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ActivitiesResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCampaignDateRangeKpiRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### KpiName
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetCampaignDateRangeKpiResponseTypeDef

### CampaignDateRangeKpiResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CampaignDateRangeKpiResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCampaignRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCampaignResponseTypeDef

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CampaignResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCampaignVersionRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes


# GetCampaignVersionResponseTypeDef

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CampaignResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCampaignVersionsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetCampaignVersionsResponseTypeDef

### CampaignsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CampaignsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCampaignsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetCampaignsResponseTypeDef

### CampaignsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CampaignsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelsResponseTypeDef

### ChannelsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ChannelsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEmailChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailChannelResponseTypeDef

### EmailChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EmailChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEmailTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetEmailTemplateResponseTypeDef

### EmailTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EmailTemplateResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEndpointRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEndpointResponseTypeDef

### EndpointResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EndpointResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventStreamRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventStreamResponseTypeDef

### EventStream
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventStreamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExportJobRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportJobResponseTypeDef

### ExportJobResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ExportJobResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExportJobsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetExportJobsResponseTypeDef

### ExportJobsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ExportJobsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGcmChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGcmChannelResponseTypeDef

### GCMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.GCMChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportJobRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportJobResponseTypeDef

### ImportJobResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ImportJobResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportJobsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetImportJobsResponseTypeDef

### ImportJobsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ImportJobsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInAppMessagesRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInAppMessagesResponseTypeDef

### InAppMessagesResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessagesResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInAppTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetInAppTemplateResponseTypeDef

### InAppTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.InAppTemplateResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJourneyDateRangeKpiRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### KpiName
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetJourneyDateRangeKpiResponseTypeDef

### JourneyDateRangeKpiResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyDateRangeKpiResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJourneyExecutionActivityMetricsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyActivityId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]


# GetJourneyExecutionActivityMetricsResponseTypeDef

### JourneyExecutionActivityMetricsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyExecutionActivityMetricsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJourneyExecutionMetricsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]


# GetJourneyExecutionMetricsResponseTypeDef

### JourneyExecutionMetricsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyExecutionMetricsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJourneyRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJourneyResponseTypeDef

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJourneyRunExecutionActivityMetricsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyActivityId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]


# GetJourneyRunExecutionActivityMetricsResponseTypeDef

### JourneyRunExecutionActivityMetricsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyRunExecutionActivityMetricsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJourneyRunExecutionMetricsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]


# GetJourneyRunExecutionMetricsResponseTypeDef

### JourneyRunExecutionMetricsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyRunExecutionMetricsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJourneyRunsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetJourneyRunsResponseTypeDef

### JourneyRunsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyRunsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPushTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetPushTemplateResponseTypeDef

### PushNotificationTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.PushNotificationTemplateResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecommenderConfigurationRequestRequestTypeDef

### RecommenderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecommenderConfigurationResponseTypeDef

### RecommenderConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.RecommenderConfigurationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecommenderConfigurationsRequestRequestTypeDef

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetRecommenderConfigurationsResponseTypeDef

### ListRecommenderConfigurationsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ListRecommenderConfigurationsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentExportJobsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetSegmentExportJobsResponseTypeDef

### ExportJobsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ExportJobsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentImportJobsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetSegmentImportJobsResponseTypeDef

### ImportJobsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ImportJobsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentResponseTypeDef

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SegmentResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentVersionRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentVersionResponseTypeDef

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SegmentResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentVersionsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetSegmentVersionsResponseTypeDef

### SegmentsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SegmentsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetSegmentsResponseTypeDef

### SegmentsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SegmentsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSmsChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSmsChannelResponseTypeDef

### SMSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SMSChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSmsTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetSmsTemplateResponseTypeDef

### SMSTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SMSTemplateResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserEndpointsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserEndpointsResponseTypeDef

### EndpointsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EndpointsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceChannelResponseTypeDef

### VoiceChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VoiceChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetVoiceTemplateResponseTypeDef

### VoiceTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VoiceTemplateResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HoldoutActivityTypeDef

### Percentage
- **Type**: <class 'int'>
- **Required**: Yes

### NextActivity
- **Type**: typing.Optional[str]


# ImportJobRequestTypeDef

### Format
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes

### DefineSegment
- **Type**: typing.Optional[bool]

### ExternalId
- **Type**: typing.Optional[str]

### RegisterEndpoints
- **Type**: typing.Optional[bool]

### SegmentId
- **Type**: typing.Optional[str]

### SegmentName
- **Type**: typing.Optional[str]


# ImportJobResourceTypeDef

### Format
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes

### DefineSegment
- **Type**: typing.Optional[bool]

### ExternalId
- **Type**: typing.Optional[str]

### RegisterEndpoints
- **Type**: typing.Optional[bool]

### SegmentId
- **Type**: typing.Optional[str]

### SegmentName
- **Type**: typing.Optional[str]


# ImportJobResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ImportJobResourceTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'COMPLETING', 'CREATED', 'FAILED', 'FAILING', 'INITIALIZING', 'PENDING_JOB', 'PREPARING_FOR_INITIALIZATION', 'PROCESSING']
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### CompletedPieces
- **Type**: typing.Optional[int]

### CompletionDate
- **Type**: typing.Optional[str]

### FailedPieces
- **Type**: typing.Optional[int]

### Failures
- **Type**: typing.Optional[typing.List[str]]

### TotalFailures
- **Type**: typing.Optional[int]

### TotalPieces
- **Type**: typing.Optional[int]

### TotalProcessed
- **Type**: typing.Optional[int]


# ImportJobsResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ImportJobResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# InAppCampaignScheduleTypeDef

### EndDate
- **Type**: typing.Optional[str]

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignEventFilterOutputTypeDef]

### QuietTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.QuietTimeTypeDef]


# InAppMessageBodyConfigTypeDef

### Alignment
- **Type**: typing.Literal['CENTER', 'LEFT', 'RIGHT']
- **Required**: Yes

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### TextColor
- **Type**: <class 'str'>
- **Required**: Yes


# InAppMessageButtonTypeDef

### Android
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.OverrideButtonConfigurationTypeDef]

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.DefaultButtonConfigurationTypeDef]

### IOS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.OverrideButtonConfigurationTypeDef]

### Web
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.OverrideButtonConfigurationTypeDef]


# InAppMessageCampaignTypeDef

### CampaignId
- **Type**: typing.Optional[str]

### DailyCap
- **Type**: typing.Optional[int]

### InAppMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageTypeDef]

### Priority
- **Type**: typing.Optional[int]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.InAppCampaignScheduleTypeDef]

### SessionCap
- **Type**: typing.Optional[int]

### TotalCap
- **Type**: typing.Optional[int]

### TreatmentId
- **Type**: typing.Optional[str]


# InAppMessageContentTypeDef

### BackgroundColor
- **Type**: typing.Optional[str]

### BodyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageBodyConfigTypeDef]

### HeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageHeaderConfigTypeDef]

### ImageUrl
- **Type**: typing.Optional[str]

### PrimaryBtn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageButtonTypeDef]

### SecondaryBtn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageButtonTypeDef]


# InAppMessageHeaderConfigTypeDef

### Alignment
- **Type**: typing.Literal['CENTER', 'LEFT', 'RIGHT']
- **Required**: Yes

### Header
- **Type**: <class 'str'>
- **Required**: Yes

### TextColor
- **Type**: <class 'str'>
- **Required**: Yes


# InAppMessageTypeDef

### Content
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageContentTypeDef]]

### CustomConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]


# InAppMessagesResponseTypeDef

### InAppMessageCampaigns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageCampaignTypeDef]]


# InAppTemplateRequestTypeDef

### Content
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageContentTypeDef]]

### CustomConfig
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]


# InAppTemplateResponseTypeDef

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: typing.Literal['EMAIL', 'INAPP', 'PUSH', 'SMS', 'VOICE']
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.InAppMessageContentTypeDef]]

### CustomConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# ItemResponseTypeDef

### EndpointItemResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointItemResponseTypeDef]

### EventsItemResponse
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.EventItemResponseTypeDef]]


# JourneyChannelSettingsTypeDef

### ConnectCampaignArn
- **Type**: typing.Optional[str]

### ConnectCampaignExecutionRoleArn
- **Type**: typing.Optional[str]


# JourneyCustomMessageTypeDef

### Data
- **Type**: typing.Optional[str]


# JourneyDateRangeKpiResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### KpiName
- **Type**: <class 'str'>
- **Required**: Yes

### KpiResult
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.BaseKpiResultTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# JourneyEmailMessageTypeDef

### FromAddress
- **Type**: typing.Optional[str]


# JourneyExecutionActivityMetricsResponseTypeDef

### ActivityType
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyActivityId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### LastEvaluatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# JourneyExecutionMetricsResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### LastEvaluatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# JourneyLimitsTypeDef

### DailyCap
- **Type**: typing.Optional[int]

### EndpointReentryCap
- **Type**: typing.Optional[int]

### MessagesPerSecond
- **Type**: typing.Optional[int]

### EndpointReentryInterval
- **Type**: typing.Optional[str]

### TimeframeCap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyTimeframeCapTypeDef]

### TotalCap
- **Type**: typing.Optional[int]


# JourneyPushMessageTypeDef

### TimeToLive
- **Type**: typing.Optional[str]


# JourneyResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Activities
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.ActivityOutputTypeDef]]

### CreationDate
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyLimitsTypeDef]

### LocalTime
- **Type**: typing.Optional[bool]

### QuietTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.QuietTimeTypeDef]

### RefreshFrequency
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyScheduleOutputTypeDef]

### StartActivity
- **Type**: typing.Optional[str]

### StartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.StartConditionOutputTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELLED', 'CLOSED', 'COMPLETED', 'DRAFT', 'PAUSED']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### WaitForQuietTime
- **Type**: typing.Optional[bool]

### RefreshOnSegmentUpdate
- **Type**: typing.Optional[bool]

### JourneyChannelSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyChannelSettingsTypeDef]

### SendingSchedule
- **Type**: typing.Optional[bool]

### OpenHours
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursOutputTypeDef]

### ClosedDays
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysOutputTypeDef]

### TimezoneEstimationMethods
- **Type**: typing.Optional[typing.List[typing.Literal['PHONE_NUMBER', 'POSTAL_CODE']]]


# JourneyRunExecutionActivityMetricsResponseTypeDef

### ActivityType
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyActivityId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### LastEvaluatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# JourneyRunExecutionMetricsResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### LastEvaluatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes


# JourneyRunResponseTypeDef

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'str'>
- **Required**: Yes

### RunId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'RUNNING', 'SCHEDULED']
- **Required**: Yes


# JourneyRunsResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyRunResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# JourneySMSMessageTypeDef

### MessageType
- **Type**: typing.Optional[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]

### OriginationNumber
- **Type**: typing.Optional[str]

### SenderId
- **Type**: typing.Optional[str]

### EntityId
- **Type**: typing.Optional[str]

### TemplateId
- **Type**: typing.Optional[str]


# JourneyScheduleOutputTypeDef

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Timezone
- **Type**: typing.Optional[str]


# JourneyScheduleTypeDef

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Timezone
- **Type**: typing.Optional[str]


# JourneyStateRequestTypeDef

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELLED', 'CLOSED', 'COMPLETED', 'DRAFT', 'PAUSED']]


# JourneyTimeframeCapTypeDef

### Cap
- **Type**: typing.Optional[int]

### Days
- **Type**: typing.Optional[int]


# JourneysResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJourneysRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# ListJourneysResponseTypeDef

### JourneysResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneysResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommenderConfigurationsResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.RecommenderConfigurationResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### TagsModel
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.TagsModelOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplateVersionsRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]


# ListTemplateVersionsResponseTypeDef

### TemplateVersionsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.TemplateVersionsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplatesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### TemplateType
- **Type**: typing.Optional[str]


# ListTemplatesResponseTypeDef

### TemplatesResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.TemplatesResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MessageBodyTypeDef

### Message
- **Type**: typing.Optional[str]

### RequestID
- **Type**: typing.Optional[str]


# MessageConfigurationOutputTypeDef

### ADMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### APNSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### BaiduMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### CustomMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignCustomMessageTypeDef]

### DefaultMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### EmailMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignEmailMessageOutputTypeDef]

### GCMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### SMSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignSmsMessageTypeDef]

### InAppMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignInAppMessageOutputTypeDef]


# MessageConfigurationTypeDef

### ADMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### APNSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### BaiduMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### CustomMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignCustomMessageTypeDef]

### DefaultMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### EmailMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignEmailMessageTypeDef]

### GCMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageTypeDef]

### SMSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignSmsMessageTypeDef]

### InAppMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignInAppMessageTypeDef]


# MessageHeaderTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# MessageRequestTypeDef

### MessageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.DirectMessageConfigurationTypeDef'>
- **Required**: Yes

### Addresses
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.AddressConfigurationTypeDef]]

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Endpoints
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.EndpointSendConfigurationTypeDef]]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateConfigurationTypeDef]

### TraceId
- **Type**: typing.Optional[str]


# MessageResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointResult
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.EndpointMessageResultTypeDef]]

### RequestId
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.MessageResultTypeDef]]


# MessageResultTypeDef

### DeliveryStatus
- **Type**: typing.Literal['DUPLICATE', 'OPT_OUT', 'PERMANENT_FAILURE', 'SUCCESSFUL', 'TEMPORARY_FAILURE', 'THROTTLED', 'UNKNOWN_FAILURE']
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### MessageId
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### UpdatedToken
- **Type**: typing.Optional[str]


# MessageTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### ImageIconUrl
- **Type**: typing.Optional[str]

### ImageSmallIconUrl
- **Type**: typing.Optional[str]

### ImageUrl
- **Type**: typing.Optional[str]

### JsonBody
- **Type**: typing.Optional[str]

### MediaUrl
- **Type**: typing.Optional[str]

### RawContent
- **Type**: typing.Optional[str]

### SilentPush
- **Type**: typing.Optional[bool]

### TimeToLive
- **Type**: typing.Optional[int]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# MetricDimensionTypeDef

### ComparisonOperator
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# MultiConditionalBranchOutputTypeDef

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SimpleConditionOutputTypeDef]

### NextActivity
- **Type**: typing.Optional[str]


# MultiConditionalBranchTypeDef

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SimpleConditionTypeDef]

### NextActivity
- **Type**: typing.Optional[str]


# MultiConditionalSplitActivityOutputTypeDef

### Branches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.MultiConditionalBranchOutputTypeDef]]

### DefaultActivity
- **Type**: typing.Optional[str]

### EvaluationWaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.WaitTimeTypeDef]


# MultiConditionalSplitActivityTypeDef

### Branches
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.MultiConditionalBranchTypeDef]]

### DefaultActivity
- **Type**: typing.Optional[str]

### EvaluationWaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.WaitTimeTypeDef]


# NumberValidateRequestTypeDef

### IsoCountryCode
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]


# NumberValidateResponseTypeDef

### Carrier
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### CleansedPhoneNumberE164
- **Type**: typing.Optional[str]

### CleansedPhoneNumberNational
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### CountryCodeIso2
- **Type**: typing.Optional[str]

### CountryCodeNumeric
- **Type**: typing.Optional[str]

### County
- **Type**: typing.Optional[str]

### OriginalCountryCodeIso2
- **Type**: typing.Optional[str]

### OriginalPhoneNumber
- **Type**: typing.Optional[str]

### PhoneType
- **Type**: typing.Optional[str]

### PhoneTypeCode
- **Type**: typing.Optional[int]

### Timezone
- **Type**: typing.Optional[str]

### ZipCode
- **Type**: typing.Optional[str]


# OpenHoursOutputTypeDef

### EMAIL
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]

### SMS
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]

### PUSH
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]

### VOICE
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]

### CUSTOM
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]


# OpenHoursRuleTypeDef

### StartTime
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[str]


# OpenHoursTypeDef

### EMAIL
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]

### SMS
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]

### PUSH
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]

### VOICE
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]

### CUSTOM
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursRuleTypeDef]]]


# OverrideButtonConfigurationTypeDef

### ButtonAction
- **Type**: typing.Literal['CLOSE', 'DEEP_LINK', 'LINK']
- **Required**: Yes

### Link
- **Type**: typing.Optional[str]


# PhoneNumberValidateRequestRequestTypeDef

### NumberValidateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.NumberValidateRequestTypeDef'>
- **Required**: Yes


# PhoneNumberValidateResponseTypeDef

### NumberValidateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.NumberValidateResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PublicEndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointDemographicTypeDef]

### EffectiveDate
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointLocationTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Mapping[str, float]]

### OptOut
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EndpointUserTypeDef]


# PushMessageActivityTypeDef

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyPushMessageTypeDef]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# PushNotificationTemplateRequestTypeDef

### ADM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.AndroidPushNotificationTemplateTypeDef]

### APNS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.APNSPushNotificationTemplateTypeDef]

### Baidu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.AndroidPushNotificationTemplateTypeDef]

### Default
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.DefaultPushNotificationTemplateTypeDef]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### GCM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.AndroidPushNotificationTemplateTypeDef]

### RecommenderId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]


# PushNotificationTemplateResponseTypeDef

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: typing.Literal['EMAIL', 'INAPP', 'PUSH', 'SMS', 'VOICE']
- **Required**: Yes

### ADM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.AndroidPushNotificationTemplateTypeDef]

### APNS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.APNSPushNotificationTemplateTypeDef]

### Arn
- **Type**: typing.Optional[str]

### Baidu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.AndroidPushNotificationTemplateTypeDef]

### Default
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.DefaultPushNotificationTemplateTypeDef]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### GCM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.AndroidPushNotificationTemplateTypeDef]

### RecommenderId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# PutEventStreamRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteEventStream
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.WriteEventStreamTypeDef'>
- **Required**: Yes


# PutEventStreamResponseTypeDef

### EventStream
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventStreamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutEventsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EventsRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventsRequestTypeDef'>
- **Required**: Yes


# PutEventsResponseTypeDef

### EventsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EventsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QuietTimeTypeDef

### End
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Optional[str]


# RandomSplitActivityOutputTypeDef

### Branches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.RandomSplitEntryTypeDef]]


# RandomSplitActivityTypeDef

### Branches
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.RandomSplitEntryTypeDef]]


# RandomSplitEntryTypeDef

### NextActivity
- **Type**: typing.Optional[str]

### Percentage
- **Type**: typing.Optional[int]


# RawEmailTypeDef

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# RecencyDimensionTypeDef

### Duration
- **Type**: typing.Literal['DAY_14', 'DAY_30', 'DAY_7', 'HR_24']
- **Required**: Yes

### RecencyType
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes


# RecommenderConfigurationResponseTypeDef

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationProviderRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationProviderUri
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RecommendationProviderIdType
- **Type**: typing.Optional[str]

### RecommendationTransformerUri
- **Type**: typing.Optional[str]

### RecommendationsDisplayName
- **Type**: typing.Optional[str]

### RecommendationsPerMessage
- **Type**: typing.Optional[int]


# RemoveAttributesRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeType
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateAttributesRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.UpdateAttributesRequestTypeDef'>
- **Required**: Yes


# RemoveAttributesResponseTypeDef

### AttributesResource
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.AttributesResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
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


# ResultRowTypeDef

### GroupedBys
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ResultRowValueTypeDef]
- **Required**: Yes

### Values
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.ResultRowValueTypeDef]
- **Required**: Yes


# ResultRowValueTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SMSChannelRequestTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### SenderId
- **Type**: typing.Optional[str]

### ShortCode
- **Type**: typing.Optional[str]


# SMSChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### PromotionalMessagesPerSecond
- **Type**: typing.Optional[int]

### SenderId
- **Type**: typing.Optional[str]

### ShortCode
- **Type**: typing.Optional[str]

### TransactionalMessagesPerSecond
- **Type**: typing.Optional[int]

### Version
- **Type**: typing.Optional[int]


# SMSMessageActivityTypeDef

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneySMSMessageTypeDef]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# SMSMessageTypeDef

### Body
- **Type**: typing.Optional[str]

### Keyword
- **Type**: typing.Optional[str]

### MediaUrl
- **Type**: typing.Optional[str]

### MessageType
- **Type**: typing.Optional[typing.Literal['PROMOTIONAL', 'TRANSACTIONAL']]

### OriginationNumber
- **Type**: typing.Optional[str]

### SenderId
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### EntityId
- **Type**: typing.Optional[str]

### TemplateId
- **Type**: typing.Optional[str]


# SMSTemplateRequestTypeDef

### Body
- **Type**: typing.Optional[str]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### RecommenderId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]


# SMSTemplateResponseTypeDef

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: typing.Literal['EMAIL', 'INAPP', 'PUSH', 'SMS', 'VOICE']
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### Body
- **Type**: typing.Optional[str]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### RecommenderId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# ScheduleOutputTypeDef

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[str]

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignEventFilterOutputTypeDef]

### Frequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'EVENT', 'HOURLY', 'IN_APP_EVENT', 'MONTHLY', 'ONCE', 'WEEKLY']]

### IsLocalTime
- **Type**: typing.Optional[bool]

### QuietTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.QuietTimeTypeDef]

### Timezone
- **Type**: typing.Optional[str]


# ScheduleTypeDef

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[str]

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignEventFilterTypeDef]

### Frequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'EVENT', 'HOURLY', 'IN_APP_EVENT', 'MONTHLY', 'ONCE', 'WEEKLY']]

### IsLocalTime
- **Type**: typing.Optional[bool]

### QuietTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.QuietTimeTypeDef]

### Timezone
- **Type**: typing.Optional[str]


# SegmentBehaviorsTypeDef

### Recency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.RecencyDimensionTypeDef]


# SegmentConditionTypeDef

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes


# SegmentDemographicsOutputTypeDef

### AppVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionOutputTypeDef]

### Channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionOutputTypeDef]

### DeviceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionOutputTypeDef]

### Make
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionOutputTypeDef]

### Model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionOutputTypeDef]

### Platform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionOutputTypeDef]


# SegmentDemographicsTypeDef

### AppVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionTypeDef]

### Channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionTypeDef]

### DeviceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionTypeDef]

### Make
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionTypeDef]

### Model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionTypeDef]

### Platform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionTypeDef]


# SegmentDimensionsOutputTypeDef

### Attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.AttributeDimensionOutputTypeDef]]

### Behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentBehaviorsTypeDef]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentDemographicsOutputTypeDef]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentLocationOutputTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.MetricDimensionTypeDef]]

### UserAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.AttributeDimensionOutputTypeDef]]


# SegmentDimensionsTypeDef

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.AttributeDimensionTypeDef]]

### Behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentBehaviorsTypeDef]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentDemographicsTypeDef]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentLocationTypeDef]

### Metrics
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.MetricDimensionTypeDef]]

### UserAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.AttributeDimensionTypeDef]]


# SegmentGroupListOutputTypeDef

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentGroupOutputTypeDef]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupListTypeDef

### Groups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentGroupTypeDef]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupOutputTypeDef

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentDimensionsOutputTypeDef]]

### SourceSegments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentReferenceTypeDef]]

### SourceType
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupTypeDef

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentDimensionsTypeDef]]

### SourceSegments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentReferenceTypeDef]]

### SourceType
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentImportResourceTypeDef

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Url
- **Type**: <class 'str'>
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### ChannelCounts
- **Type**: typing.Optional[typing.Dict[str, int]]


# SegmentLocationOutputTypeDef

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionOutputTypeDef]

### GPSPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.GPSPointDimensionTypeDef]


# SegmentLocationTypeDef

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SetDimensionTypeDef]

### GPSPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.GPSPointDimensionTypeDef]


# SegmentReferenceTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]


# SegmentResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentType
- **Type**: typing.Literal['DIMENSIONAL', 'IMPORT']
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentDimensionsOutputTypeDef]

### ImportDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentImportResourceTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SegmentGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentGroupListOutputTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Version
- **Type**: typing.Optional[int]


# SegmentsResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SendMessagesRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageRequestTypeDef'>
- **Required**: Yes


# SendMessagesResponseTypeDef

### MessageResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendOTPMessageRequestParametersTypeDef

### BrandName
- **Type**: <class 'str'>
- **Required**: Yes

### Channel
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### OriginationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### AllowedAttempts
- **Type**: typing.Optional[int]

### CodeLength
- **Type**: typing.Optional[int]

### EntityId
- **Type**: typing.Optional[str]

### Language
- **Type**: typing.Optional[str]

### TemplateId
- **Type**: typing.Optional[str]

### ValidityPeriod
- **Type**: typing.Optional[int]


# SendOTPMessageRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SendOTPMessageRequestParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SendOTPMessageRequestParametersTypeDef'>
- **Required**: Yes


# SendOTPMessageResponseTypeDef

### MessageResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendUsersMessageRequestTypeDef

### MessageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.DirectMessageConfigurationTypeDef'>
- **Required**: Yes

### Users
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.EndpointSendConfigurationTypeDef]
- **Required**: Yes

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateConfigurationTypeDef]

### TraceId
- **Type**: typing.Optional[str]


# SendUsersMessageResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint_classes.EndpointMessageResultTypeDef]]]


# SendUsersMessagesRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SendUsersMessageRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SendUsersMessageRequestTypeDef'>
- **Required**: Yes


# SendUsersMessagesResponseTypeDef

### SendUsersMessageResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SendUsersMessageResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SessionTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### StartTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: typing.Optional[int]

### StopTimestamp
- **Type**: typing.Optional[str]


# SetDimensionOutputTypeDef

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### DimensionType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE', 'INCLUSIVE']]


# SetDimensionTypeDef

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DimensionType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE', 'INCLUSIVE']]


# SimpleConditionOutputTypeDef

### EventCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EventConditionOutputTypeDef]

### SegmentCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentConditionTypeDef]

### SegmentDimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentDimensionsOutputTypeDef]


# SimpleConditionTypeDef

### EventCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EventConditionTypeDef]

### SegmentCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentConditionTypeDef]

### SegmentDimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentDimensionsTypeDef]


# SimpleEmailPartTypeDef

### Charset
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[str]


# SimpleEmailTypeDef

### HtmlPart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SimpleEmailPartTypeDef]

### Subject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SimpleEmailPartTypeDef]

### TextPart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SimpleEmailPartTypeDef]

### Headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.MessageHeaderTypeDef]]


# StartConditionOutputTypeDef

### Description
- **Type**: typing.Optional[str]

### EventStartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EventStartConditionOutputTypeDef]

### SegmentStartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentConditionTypeDef]


# StartConditionTypeDef

### Description
- **Type**: typing.Optional[str]

### EventStartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.EventStartConditionTypeDef]

### SegmentStartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentConditionTypeDef]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagsModel
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.TagsModelTypeDef'>
- **Required**: Yes


# TagsModelOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagsModelTypeDef

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateActiveVersionRequestTypeDef

### Version
- **Type**: typing.Optional[str]


# TemplateConfigurationTypeDef

### EmailTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateTypeDef]

### PushTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateTypeDef]

### SMSTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateTypeDef]

### VoiceTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateTypeDef]

### InAppTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateTypeDef]


# TemplateCreateMessageBodyTypeDef

### Arn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### RequestID
- **Type**: typing.Optional[str]


# TemplateResponseTypeDef

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: typing.Literal['EMAIL', 'INAPP', 'PUSH', 'SMS', 'VOICE']
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# TemplateTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# TemplateVersionResponseTypeDef

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### TemplateDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# TemplateVersionsResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateVersionResponseTypeDef]
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### RequestID
- **Type**: typing.Optional[str]


# TemplatesResponseTypeDef

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# TreatmentResourceTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SizePercent
- **Type**: <class 'int'>
- **Required**: Yes

### CustomDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CustomDeliveryConfigurationOutputTypeDef]

### MessageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageConfigurationOutputTypeDef]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ScheduleOutputTypeDef]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignStateTypeDef]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateConfigurationTypeDef]

### TreatmentDescription
- **Type**: typing.Optional[str]

### TreatmentName
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAdmChannelRequestRequestTypeDef

### ADMChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ADMChannelRequestTypeDef'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAdmChannelResponseTypeDef

### ADMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ADMChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApnsChannelRequestRequestTypeDef

### APNSChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSChannelRequestTypeDef'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApnsChannelResponseTypeDef

### APNSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApnsSandboxChannelRequestRequestTypeDef

### APNSSandboxChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSSandboxChannelRequestTypeDef'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApnsSandboxChannelResponseTypeDef

### APNSSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSSandboxChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApnsVoipChannelRequestRequestTypeDef

### APNSVoipChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSVoipChannelRequestTypeDef'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApnsVoipChannelResponseTypeDef

### APNSVoipChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSVoipChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApnsVoipSandboxChannelRequestRequestTypeDef

### APNSVoipSandboxChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSVoipSandboxChannelRequestTypeDef'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApnsVoipSandboxChannelResponseTypeDef

### APNSVoipSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.APNSVoipSandboxChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApplicationSettingsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteApplicationSettingsRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.WriteApplicationSettingsRequestTypeDef'>
- **Required**: Yes


# UpdateApplicationSettingsResponseTypeDef

### ApplicationSettingsResource
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationSettingsResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAttributesRequestTypeDef

### Blacklist
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateBaiduChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### BaiduChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.BaiduChannelRequestTypeDef'>
- **Required**: Yes


# UpdateBaiduChannelResponseTypeDef

### BaiduChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.BaiduChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCampaignRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteCampaignRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.WriteCampaignRequestTypeDef'>
- **Required**: Yes


# UpdateCampaignResponseTypeDef

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.CampaignResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEmailChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EmailChannelRequestTypeDef'>
- **Required**: Yes


# UpdateEmailChannelResponseTypeDef

### EmailChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EmailChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEmailTemplateRequestRequestTypeDef

### EmailTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EmailTemplateRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdateEmailTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEndpointRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EndpointRequestTypeDef'>
- **Required**: Yes


# UpdateEndpointResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEndpointsBatchRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointBatchRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.EndpointBatchRequestTypeDef'>
- **Required**: Yes


# UpdateEndpointsBatchResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGcmChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### GCMChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.GCMChannelRequestTypeDef'>
- **Required**: Yes


# UpdateGcmChannelResponseTypeDef

### GCMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.GCMChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInAppTemplateRequestRequestTypeDef

### InAppTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.InAppTemplateRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdateInAppTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateJourneyRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteJourneyRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.WriteJourneyRequestTypeDef'>
- **Required**: Yes


# UpdateJourneyResponseTypeDef

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateJourneyStateRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyStateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyStateRequestTypeDef'>
- **Required**: Yes


# UpdateJourneyStateResponseTypeDef

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.JourneyResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePushTemplateRequestRequestTypeDef

### PushNotificationTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.PushNotificationTemplateRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdatePushTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRecommenderConfigurationRequestRequestTypeDef

### RecommenderId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateRecommenderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.UpdateRecommenderConfigurationTypeDef'>
- **Required**: Yes


# UpdateRecommenderConfigurationResponseTypeDef

### RecommenderConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.RecommenderConfigurationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRecommenderConfigurationTypeDef

### RecommendationProviderRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationProviderUri
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RecommendationProviderIdType
- **Type**: typing.Optional[str]

### RecommendationTransformerUri
- **Type**: typing.Optional[str]

### RecommendationsDisplayName
- **Type**: typing.Optional[str]

### RecommendationsPerMessage
- **Type**: typing.Optional[int]


# UpdateSegmentRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteSegmentRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.WriteSegmentRequestTypeDef'>
- **Required**: Yes


# UpdateSegmentResponseTypeDef

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SegmentResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSmsChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SMSChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SMSChannelRequestTypeDef'>
- **Required**: Yes


# UpdateSmsChannelResponseTypeDef

### SMSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SMSChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSmsTemplateRequestRequestTypeDef

### SMSTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.SMSTemplateRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdateSmsTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTemplateActiveVersionRequestRequestTypeDef

### TemplateActiveVersionRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.TemplateActiveVersionRequestTypeDef'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTemplateActiveVersionResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVoiceChannelRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VoiceChannelRequestTypeDef'>
- **Required**: Yes


# UpdateVoiceChannelResponseTypeDef

### VoiceChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VoiceChannelResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVoiceTemplateRequestRequestTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VoiceTemplateRequestTypeDef'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdateVoiceTemplateResponseTypeDef

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerificationResponseTypeDef

### Valid
- **Type**: typing.Optional[bool]


# VerifyOTPMessageRequestParametersTypeDef

### DestinationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Otp
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyOTPMessageRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### VerifyOTPMessageRequestParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VerifyOTPMessageRequestParametersTypeDef'>
- **Required**: Yes


# VerifyOTPMessageResponseTypeDef

### VerificationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.VerificationResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VoiceChannelRequestTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# VoiceChannelResponseTypeDef

### Platform
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### HasCredential
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### IsArchived
- **Type**: typing.Optional[bool]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# VoiceMessageTypeDef

### Body
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### OriginationNumber
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### VoiceId
- **Type**: typing.Optional[str]


# VoiceTemplateRequestTypeDef

### Body
- **Type**: typing.Optional[str]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### VoiceId
- **Type**: typing.Optional[str]


# VoiceTemplateResponseTypeDef

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: typing.Literal['EMAIL', 'INAPP', 'PUSH', 'SMS', 'VOICE']
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### Body
- **Type**: typing.Optional[str]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### VoiceId
- **Type**: typing.Optional[str]


# WaitActivityTypeDef

### NextActivity
- **Type**: typing.Optional[str]

### WaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.WaitTimeTypeDef]


# WaitTimeTypeDef

### WaitFor
- **Type**: typing.Optional[str]

### WaitUntil
- **Type**: typing.Optional[str]


# WriteApplicationSettingsRequestTypeDef

### CampaignHook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignHookTypeDef]

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### EventTaggingEnabled
- **Type**: typing.Optional[bool]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignLimitsTypeDef]

### QuietTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.QuietTimeTypeDef]

### JourneyLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ApplicationSettingsJourneyLimitsTypeDef]


# WriteCampaignRequestTypeDef

### AdditionalTreatments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pinpoint_classes.WriteTreatmentResourceTypeDef]]

### CustomDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CustomDeliveryConfigurationTypeDef]

### Description
- **Type**: typing.Optional[str]

### HoldoutPercent
- **Type**: typing.Optional[int]

### Hook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignHookTypeDef]

### IsPaused
- **Type**: typing.Optional[bool]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CampaignLimitsTypeDef]

### MessageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageConfigurationTypeDef]

### Name
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ScheduleTypeDef]

### SegmentId
- **Type**: typing.Optional[str]

### SegmentVersion
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateConfigurationTypeDef]

### TreatmentDescription
- **Type**: typing.Optional[str]

### TreatmentName
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]


# WriteEventStreamTypeDef

### DestinationStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# WriteJourneyRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Activities
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.pinpoint_classes.ActivityTypeDef]]

### CreationDate
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyLimitsTypeDef]

### LocalTime
- **Type**: typing.Optional[bool]

### QuietTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.QuietTimeTypeDef]

### RefreshFrequency
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyScheduleTypeDef]

### StartActivity
- **Type**: typing.Optional[str]

### StartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.StartConditionTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELLED', 'CLOSED', 'COMPLETED', 'DRAFT', 'PAUSED']]

### WaitForQuietTime
- **Type**: typing.Optional[bool]

### RefreshOnSegmentUpdate
- **Type**: typing.Optional[bool]

### JourneyChannelSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.JourneyChannelSettingsTypeDef]

### SendingSchedule
- **Type**: typing.Optional[bool]

### OpenHours
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.OpenHoursTypeDef]

### ClosedDays
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ClosedDaysTypeDef]

### TimezoneEstimationMethods
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PHONE_NUMBER', 'POSTAL_CODE']]]


# WriteSegmentRequestTypeDef

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentDimensionsTypeDef]

### Name
- **Type**: typing.Optional[str]

### SegmentGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.SegmentGroupListTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# WriteTreatmentResourceTypeDef

### SizePercent
- **Type**: <class 'int'>
- **Required**: Yes

### CustomDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.CustomDeliveryConfigurationTypeDef]

### MessageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.MessageConfigurationTypeDef]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.ScheduleTypeDef]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint_classes.TemplateConfigurationTypeDef]

### TreatmentDescription
- **Type**: typing.Optional[str]

### TreatmentName
- **Type**: typing.Optional[str]


