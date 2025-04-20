# Pinpoint Pinpoint Classes

# ADMChannelRequest

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]


# ADMChannelResponse

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


# ADMMessage

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### ConsolidationKey
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Dict[str, str]]

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# APNSChannelRequest

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


# APNSChannelResponse

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


# APNSMessage

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
- **Type**: typing.Optional[typing.Dict[str, str]]

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### ThreadId
- **Type**: typing.Optional[str]

### TimeToLive
- **Type**: typing.Optional[int]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# APNSPushNotificationTemplate

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


# APNSSandboxChannelRequest

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


# APNSSandboxChannelResponse

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


# APNSVoipChannelRequest

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


# APNSVoipChannelResponse

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


# APNSVoipSandboxChannelRequest

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


# APNSVoipSandboxChannelResponse

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


# ActivitiesResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ActivityResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Activity

### CUSTOM
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomMessageActivity, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomMessageActivityOutput, NoneType]

### ConditionalSplit
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ConditionalSplitActivity, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ConditionalSplitActivityOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### EMAIL
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailMessageActivity]

### Holdout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.HoldoutActivity]

### MultiCondition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MultiConditionalSplitActivity, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MultiConditionalSplitActivityOutput, NoneType]

### PUSH
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.PushMessageActivity]

### RandomSplit
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RandomSplitActivity, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RandomSplitActivityOutput, NoneType]

### SMS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSMessageActivity]

### Wait
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WaitActivity]

### ContactCenter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ContactCenterActivity]


# ActivityOutput

### CUSTOM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomMessageActivityOutput]

### ConditionalSplit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ConditionalSplitActivityOutput]

### Description
- **Type**: typing.Optional[str]

### EMAIL
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailMessageActivity]

### Holdout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.HoldoutActivity]

### MultiCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MultiConditionalSplitActivityOutput]

### PUSH
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.PushMessageActivity]

### RandomSplit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RandomSplitActivityOutput]

### SMS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSMessageActivity]

### Wait
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WaitActivity]

### ContactCenter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ContactCenterActivity]


# ActivityResponse

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


# AddressConfiguration

### BodyOverride
- **Type**: typing.Optional[str]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### Context
- **Type**: typing.Optional[typing.Dict[str, str]]

### RawContent
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### TitleOverride
- **Type**: typing.Optional[str]


# AndroidPushNotificationTemplate

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


# ApplicationDateRangeKpiResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.BaseKpiResult'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ApplicationResponse

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


# ApplicationSettingsJourneyLimits

### DailyCap
- **Type**: typing.Optional[int]

### TimeframeCap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyTimeframeCap]

### TotalCap
- **Type**: typing.Optional[int]


# ApplicationSettingsResource

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignHook
- **Type**: <class 'NoneType'>

### LastModifiedDate
- **Type**: typing.Optional[str]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignLimits]

### QuietTime
- **Type**: <class 'NoneType'>

### JourneyLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationSettingsJourneyLimits]


# ApplicationsResponse

### Item
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationResponse]]

### NextToken
- **Type**: typing.Optional[str]


# AttributeDimension

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### AttributeType
- **Type**: typing.Optional[typing.Literal['AFTER', 'BEFORE', 'BETWEEN', 'CONTAINS', 'EXCLUSIVE', 'INCLUSIVE', 'ON']]


# AttributeDimensionOutput

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### AttributeType
- **Type**: typing.Optional[typing.Literal['AFTER', 'BEFORE', 'BETWEEN', 'CONTAINS', 'EXCLUSIVE', 'INCLUSIVE', 'ON']]


# AttributesResource

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeType
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.List[str]]


# BaiduChannelRequest

### ApiKey
- **Type**: <class 'str'>
- **Required**: Yes

### SecretKey
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]


# BaiduChannelResponse

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


# BaiduMessage

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Dict[str, str]]

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### TimeToLive
- **Type**: typing.Optional[int]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# BaseKpiResult

### Rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResultRow]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CampaignCustomMessage

### Data
- **Type**: typing.Optional[str]


# CampaignDateRangeKpiResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.BaseKpiResult'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CampaignEmailMessage

### Body
- **Type**: typing.Optional[str]

### FromAddress
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageHeader]]

### HtmlBody
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]


# CampaignEmailMessageOutput

### Body
- **Type**: typing.Optional[str]

### FromAddress
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageHeader]]

### HtmlBody
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]


# CampaignEventFilter

### Dimensions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensions, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensionsOutput]
- **Required**: Yes

### FilterType
- **Type**: typing.Literal['ENDPOINT', 'SYSTEM']
- **Required**: Yes


# CampaignEventFilterOutput

### Dimensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensionsOutput'>
- **Required**: Yes

### FilterType
- **Type**: typing.Literal['ENDPOINT', 'SYSTEM']
- **Required**: Yes


# CampaignHook

### LambdaFunctionName
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['DELIVERY', 'FILTER']]

### WebUrl
- **Type**: typing.Optional[str]


# CampaignInAppMessage

### Body
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageContent]]

### CustomConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]


# CampaignInAppMessageOutput

### Body
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageContent]]

### CustomConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]


# CampaignLimits

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


# CampaignResponse

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TreatmentResource]]

### CustomDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomDeliveryConfigurationOutput]

### DefaultState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignState]

### Description
- **Type**: typing.Optional[str]

### HoldoutPercent
- **Type**: typing.Optional[int]

### Hook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignHook]

### IsPaused
- **Type**: typing.Optional[bool]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignLimits]

### MessageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageConfigurationOutput]

### Name
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ScheduleOutput]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignState]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateConfiguration
- **Type**: <class 'NoneType'>

### TreatmentDescription
- **Type**: typing.Optional[str]

### TreatmentName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Priority
- **Type**: typing.Optional[int]


# CampaignSmsMessage

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


# CampaignState

### CampaignStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'EXECUTING', 'INVALID', 'PAUSED', 'PENDING_NEXT_RUN', 'SCHEDULED']]


# CampaignsResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ChannelResponse

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


# ChannelsResponse

### Channels
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ChannelResponse]
- **Required**: Yes


# ClosedDays

### EMAIL
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]

### SMS
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]

### PUSH
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]

### VOICE
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]

### CUSTOM
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]


# ClosedDaysOutput

### EMAIL
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]

### SMS
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]

### PUSH
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]

### VOICE
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]

### CUSTOM
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysRule]]


# ClosedDaysRule

### Name
- **Type**: typing.Optional[str]

### StartDateTime
- **Type**: typing.Optional[str]

### EndDateTime
- **Type**: typing.Optional[str]


# Condition

### Conditions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleCondition, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleConditionOutput]]]

### Operator
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY']]


# ConditionOutput

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleConditionOutput]]

### Operator
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY']]


# ConditionalSplitActivity

### Condition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Condition, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ConditionOutput, NoneType]

### EvaluationWaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WaitTime]

### FalseActivity
- **Type**: typing.Optional[str]

### TrueActivity
- **Type**: typing.Optional[str]


# ConditionalSplitActivityOutput

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ConditionOutput]

### EvaluationWaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WaitTime]

### FalseActivity
- **Type**: typing.Optional[str]

### TrueActivity
- **Type**: typing.Optional[str]


# ContactCenterActivity

### NextActivity
- **Type**: typing.Optional[str]


# CreateAppRequest

### CreateApplicationRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CreateApplicationRequest'>
- **Required**: Yes


# CreateAppResponse

### ApplicationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApplicationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCampaignRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteCampaignRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteCampaignRequest'>
- **Required**: Yes


# CreateCampaignResponse

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEmailTemplateRequest

### EmailTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailTemplateRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateEmailTemplateResponse

### CreateTemplateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CreateTemplateMessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExportJobRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportJobRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ExportJobRequest'>
- **Required**: Yes


# CreateExportJobResponse

### ExportJobResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ExportJobResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImportJobRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportJobRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ImportJobRequest'>
- **Required**: Yes


# CreateImportJobResponse

### ImportJobResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ImportJobResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInAppTemplateRequest

### InAppTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppTemplateRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateInAppTemplateResponse

### TemplateCreateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TemplateCreateMessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJourneyRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteJourneyRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteJourneyRequest'>
- **Required**: Yes


# CreateJourneyResponse

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePushTemplateRequest

### PushNotificationTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.PushNotificationTemplateRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePushTemplateResponse

### CreateTemplateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CreateTemplateMessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRecommenderConfiguration

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


# CreateRecommenderConfigurationRequest

### CreateRecommenderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CreateRecommenderConfiguration'>
- **Required**: Yes


# CreateRecommenderConfigurationResponse

### RecommenderConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RecommenderConfigurationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSegmentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteSegmentRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteSegmentRequest'>
- **Required**: Yes


# CreateSegmentResponse

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSmsTemplateRequest

### SMSTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSTemplateRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSmsTemplateResponse

### CreateTemplateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CreateTemplateMessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTemplateMessageBody

### Arn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### RequestID
- **Type**: typing.Optional[str]


# CreateVoiceTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VoiceTemplateRequest'>
- **Required**: Yes


# CreateVoiceTemplateResponse

### CreateTemplateMessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CreateTemplateMessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# CustomDeliveryConfiguration

### DeliveryUri
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]]


# CustomDeliveryConfigurationOutput

### DeliveryUri
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]]


# CustomMessageActivity

### DeliveryUri
- **Type**: typing.Optional[str]

### EndpointTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]]

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyCustomMessage]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# CustomMessageActivityOutput

### DeliveryUri
- **Type**: typing.Optional[str]

### EndpointTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]]

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyCustomMessage]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# DefaultButtonConfiguration

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


# DefaultMessage

### Body
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# DefaultPushNotificationMessage

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Dict[str, str]]

### SilentPush
- **Type**: typing.Optional[bool]

### Substitutions
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# DefaultPushNotificationTemplate

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


# DeleteAdmChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAdmChannelResponse

### ADMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ADMChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApnsChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApnsChannelResponse

### APNSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApnsSandboxChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApnsSandboxChannelResponse

### APNSSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSSandboxChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApnsVoipChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApnsVoipChannelResponse

### APNSVoipChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSVoipChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApnsVoipSandboxChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApnsVoipSandboxChannelResponse

### APNSVoipSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSVoipSandboxChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAppRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppResponse

### ApplicationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBaiduChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBaiduChannelResponse

### BaiduChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.BaiduChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCampaignRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCampaignResponse

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEmailChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailChannelResponse

### EmailChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeleteEmailTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEndpointRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointResponse

### EndpointResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEventStreamRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventStreamResponse

### EventStream
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventStream'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGcmChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGcmChannelResponse

### GCMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.GCMChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInAppTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeleteInAppTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteJourneyRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJourneyResponse

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePushTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeletePushTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRecommenderConfigurationRequest

### RecommenderId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecommenderConfigurationResponse

### RecommenderConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RecommenderConfigurationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSegmentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSegmentResponse

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSmsChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSmsChannelResponse

### SMSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSmsTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeleteSmsTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUserEndpointsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserEndpointsResponse

### EndpointsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVoiceChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceChannelResponse

### VoiceChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VoiceChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVoiceTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# DeleteVoiceTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# DirectMessageConfiguration

### ADMMessage
- **Type**: <class 'NoneType'>

### APNSMessage
- **Type**: <class 'NoneType'>

### BaiduMessage
- **Type**: <class 'NoneType'>

### DefaultMessage
- **Type**: <class 'NoneType'>

### DefaultPushNotificationMessage
- **Type**: <class 'NoneType'>

### EmailMessage
- **Type**: <class 'NoneType'>

### GCMMessage
- **Type**: <class 'NoneType'>

### SMSMessage
- **Type**: <class 'NoneType'>

### VoiceMessage
- **Type**: <class 'NoneType'>


# EmailChannelRequest

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


# EmailChannelResponse

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


# EmailMessage

### Body
- **Type**: typing.Optional[str]

### FeedbackForwardingAddress
- **Type**: typing.Optional[str]

### FromAddress
- **Type**: typing.Optional[str]

### RawEmail
- **Type**: <class 'NoneType'>

### ReplyToAddresses
- **Type**: typing.Optional[typing.List[str]]

### SimpleEmail
- **Type**: <class 'NoneType'>

### Substitutions
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# EmailMessageActivity

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyEmailMessage]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# EmailTemplateRequest

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### HtmlPart
- **Type**: typing.Optional[str]

### RecommenderId
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageHeader]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### TextPart
- **Type**: typing.Optional[str]


# EmailTemplateResponse

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageHeader]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### TextPart
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointBatchItem

### Address
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointDemographic]

### EffectiveDate
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointLocation]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### OptOut
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointUser, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointUserOutput, NoneType]


# EndpointBatchRequest

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointBatchItem]
- **Required**: Yes


# EndpointDemographic

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


# EndpointItemResponse

### Message
- **Type**: typing.Optional[str]

### StatusCode
- **Type**: typing.Optional[int]


# EndpointLocation

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


# EndpointMessageResult

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


# EndpointRequest

### Address
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointDemographic]

### EffectiveDate
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointLocation]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### OptOut
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointUser, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointUserOutput, NoneType]


# EndpointResponse

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointDemographic]

### EffectiveDate
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointLocation]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### OptOut
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointUserOutput]


# EndpointSendConfiguration

### BodyOverride
- **Type**: typing.Optional[str]

### Context
- **Type**: typing.Optional[typing.Dict[str, str]]

### RawContent
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### TitleOverride
- **Type**: typing.Optional[str]


# EndpointUser

### UserAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### UserId
- **Type**: typing.Optional[str]


# EndpointUserOutput

### UserAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### UserId
- **Type**: typing.Optional[str]


# EndpointsResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointResponse]
- **Required**: Yes


# Event

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### ClientSdkVersion
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### SdkName
- **Type**: typing.Optional[str]

### Session
- **Type**: <class 'NoneType'>


# EventCondition

### Dimensions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensions, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensionsOutput, NoneType]

### MessageActivity
- **Type**: typing.Optional[str]


# EventConditionOutput

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensionsOutput]

### MessageActivity
- **Type**: typing.Optional[str]


# EventDimensions

### Attributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimensionOutput]]]

### EventType
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput, NoneType]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MetricDimension]]


# EventDimensionsOutput

### Attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimensionOutput]]

### EventType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MetricDimension]]


# EventFilter

### Dimensions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensions, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensionsOutput]
- **Required**: Yes

### FilterType
- **Type**: typing.Literal['ENDPOINT', 'SYSTEM']
- **Required**: Yes


# EventFilterOutput

### Dimensions
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventDimensionsOutput'>
- **Required**: Yes

### FilterType
- **Type**: typing.Literal['ENDPOINT', 'SYSTEM']
- **Required**: Yes


# EventItemResponse

### Message
- **Type**: typing.Optional[str]

### StatusCode
- **Type**: typing.Optional[int]


# EventStartCondition

### EventFilter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventFilter, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventFilterOutput, NoneType]

### SegmentId
- **Type**: typing.Optional[str]


# EventStartConditionOutput

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventFilterOutput]

### SegmentId
- **Type**: typing.Optional[str]


# EventStream

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


# EventsBatch

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.PublicEndpoint'>
- **Required**: Yes

### Events
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Event]
- **Required**: Yes


# EventsRequest

### BatchItem
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventsBatch]
- **Required**: Yes


# EventsResponse

### Results
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ItemResponse]]


# ExportJobRequest

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


# ExportJobResource

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


# ExportJobResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ExportJobResource'>
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


# ExportJobsResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ExportJobResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GCMChannelRequest

### ApiKey
- **Type**: typing.Optional[str]

### DefaultAuthenticationMethod
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### ServiceJson
- **Type**: typing.Optional[str]


# GCMChannelResponse

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


# GCMMessage

### Action
- **Type**: typing.Optional[typing.Literal['DEEP_LINK', 'OPEN_APP', 'URL']]

### Body
- **Type**: typing.Optional[str]

### CollapseKey
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Dict[str, str]]

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### TimeToLive
- **Type**: typing.Optional[int]

### Title
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# GPSCoordinates

### Latitude
- **Type**: <class 'float'>
- **Required**: Yes

### Longitude
- **Type**: <class 'float'>
- **Required**: Yes


# GPSPointDimension

### Coordinates
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.GPSCoordinates'>
- **Required**: Yes

### RangeInKilometers
- **Type**: typing.Optional[float]


# GetAdmChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdmChannelResponse

### ADMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ADMChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetApnsChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApnsChannelResponse

### APNSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetApnsSandboxChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApnsSandboxChannelResponse

### APNSSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSSandboxChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetApnsVoipChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApnsVoipChannelResponse

### APNSVoipChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSVoipChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetApnsVoipSandboxChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApnsVoipSandboxChannelResponse

### APNSVoipSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSVoipSandboxChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppResponse

### ApplicationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationDateRangeKpiRequest

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


# GetApplicationDateRangeKpiResponse

### ApplicationDateRangeKpiResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationDateRangeKpiResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationSettingsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationSettingsResponse

### ApplicationSettingsResource
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationSettingsResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppsRequest

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetAppsResponse

### ApplicationsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetBaiduChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBaiduChannelResponse

### BaiduChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.BaiduChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetCampaignActivitiesRequest

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


# GetCampaignActivitiesResponse

### ActivitiesResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ActivitiesResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetCampaignDateRangeKpiRequest

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


# GetCampaignDateRangeKpiResponse

### CampaignDateRangeKpiResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignDateRangeKpiResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetCampaignRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCampaignResponse

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetCampaignVersionRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes


# GetCampaignVersionResponse

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetCampaignVersionsRequest

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


# GetCampaignVersionsResponse

### CampaignsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetCampaignsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetCampaignsResponse

### CampaignsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelsResponse

### ChannelsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ChannelsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetEmailChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailChannelResponse

### EmailChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetEmailTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetEmailTemplateResponse

### EmailTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailTemplateResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetEndpointRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEndpointResponse

### EndpointResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventStreamRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventStreamResponse

### EventStream
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventStream'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetExportJobRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportJobResponse

### ExportJobResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ExportJobResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetExportJobsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetExportJobsResponse

### ExportJobsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ExportJobsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetGcmChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGcmChannelResponse

### GCMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.GCMChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportJobRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportJobResponse

### ImportJobResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ImportJobResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportJobsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetImportJobsResponse

### ImportJobsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ImportJobsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetInAppMessagesRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInAppMessagesResponse

### InAppMessagesResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessagesResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetInAppTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetInAppTemplateResponse

### InAppTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppTemplateResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetJourneyDateRangeKpiRequest

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


# GetJourneyDateRangeKpiResponse

### JourneyDateRangeKpiResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyDateRangeKpiResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetJourneyExecutionActivityMetricsRequest

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


# GetJourneyExecutionActivityMetricsResponse

### JourneyExecutionActivityMetricsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyExecutionActivityMetricsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetJourneyExecutionMetricsRequest

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


# GetJourneyExecutionMetricsResponse

### JourneyExecutionMetricsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyExecutionMetricsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetJourneyRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJourneyResponse

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetJourneyRunExecutionActivityMetricsRequest

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


# GetJourneyRunExecutionActivityMetricsResponse

### JourneyRunExecutionActivityMetricsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyRunExecutionActivityMetricsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetJourneyRunExecutionMetricsRequest

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


# GetJourneyRunExecutionMetricsResponse

### JourneyRunExecutionMetricsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyRunExecutionMetricsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetJourneyRunsRequest

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


# GetJourneyRunsResponse

### JourneyRunsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyRunsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetPushTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetPushTemplateResponse

### PushNotificationTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.PushNotificationTemplateResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecommenderConfigurationRequest

### RecommenderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecommenderConfigurationResponse

### RecommenderConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RecommenderConfigurationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecommenderConfigurationsRequest

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetRecommenderConfigurationsResponse

### ListRecommenderConfigurationsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ListRecommenderConfigurationsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentExportJobsRequest

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


# GetSegmentExportJobsResponse

### ExportJobsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ExportJobsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentImportJobsRequest

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


# GetSegmentImportJobsResponse

### ImportJobsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ImportJobsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentResponse

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentVersionRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentVersionResponse

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentVersionsRequest

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


# GetSegmentVersionsResponse

### SegmentsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# GetSegmentsResponse

### SegmentsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetSmsChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSmsChannelResponse

### SMSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetSmsTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetSmsTemplateResponse

### SMSTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSTemplateResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserEndpointsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserEndpointsResponse

### EndpointsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceChannelResponse

### VoiceChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VoiceChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]


# GetVoiceTemplateResponse

### VoiceTemplateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VoiceTemplateResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# HoldoutActivity

### Percentage
- **Type**: <class 'int'>
- **Required**: Yes

### NextActivity
- **Type**: typing.Optional[str]


# ImportJobRequest

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


# ImportJobResource

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


# ImportJobResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ImportJobResource'>
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


# ImportJobsResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ImportJobResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# InAppCampaignSchedule

### EndDate
- **Type**: typing.Optional[str]

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignEventFilterOutput]

### QuietTime
- **Type**: <class 'NoneType'>


# InAppMessage

### Content
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageContent]]

### CustomConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]


# InAppMessageBodyConfig

### Alignment
- **Type**: typing.Literal['CENTER', 'LEFT', 'RIGHT']
- **Required**: Yes

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### TextColor
- **Type**: <class 'str'>
- **Required**: Yes


# InAppMessageButton

### Android
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OverrideButtonConfiguration]

### DefaultConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.DefaultButtonConfiguration]

### IOS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OverrideButtonConfiguration]

### Web
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OverrideButtonConfiguration]


# InAppMessageCampaign

### CampaignId
- **Type**: typing.Optional[str]

### DailyCap
- **Type**: typing.Optional[int]

### InAppMessage
- **Type**: <class 'NoneType'>

### Priority
- **Type**: typing.Optional[int]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppCampaignSchedule]

### SessionCap
- **Type**: typing.Optional[int]

### TotalCap
- **Type**: typing.Optional[int]

### TreatmentId
- **Type**: typing.Optional[str]


# InAppMessageContent

### BackgroundColor
- **Type**: typing.Optional[str]

### BodyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageBodyConfig]

### HeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageHeaderConfig]

### ImageUrl
- **Type**: typing.Optional[str]

### PrimaryBtn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageButton]

### SecondaryBtn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageButton]


# InAppMessageHeaderConfig

### Alignment
- **Type**: typing.Literal['CENTER', 'LEFT', 'RIGHT']
- **Required**: Yes

### Header
- **Type**: <class 'str'>
- **Required**: Yes

### TextColor
- **Type**: <class 'str'>
- **Required**: Yes


# InAppMessagesResponse

### InAppMessageCampaigns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageCampaign]]


# InAppTemplateRequest

### Content
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageContent]]

### CustomConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### Layout
- **Type**: typing.Optional[typing.Literal['BOTTOM_BANNER', 'CAROUSEL', 'MIDDLE_BANNER', 'MOBILE_FEED', 'OVERLAYS', 'TOP_BANNER']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]


# InAppTemplateResponse

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppMessageContent]]

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


# ItemResponse

### EndpointItemResponse
- **Type**: <class 'NoneType'>

### EventsItemResponse
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventItemResponse]]


# JourneyChannelSettings

### ConnectCampaignArn
- **Type**: typing.Optional[str]

### ConnectCampaignExecutionRoleArn
- **Type**: typing.Optional[str]


# JourneyCustomMessage

### Data
- **Type**: typing.Optional[str]


# JourneyDateRangeKpiResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.BaseKpiResult'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# JourneyEmailMessage

### FromAddress
- **Type**: typing.Optional[str]


# JourneyExecutionActivityMetricsResponse

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


# JourneyExecutionMetricsResponse

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


# JourneyLimits

### DailyCap
- **Type**: typing.Optional[int]

### EndpointReentryCap
- **Type**: typing.Optional[int]

### MessagesPerSecond
- **Type**: typing.Optional[int]

### EndpointReentryInterval
- **Type**: typing.Optional[str]

### TimeframeCap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyTimeframeCap]

### TotalCap
- **Type**: typing.Optional[int]


# JourneyPushMessage

### TimeToLive
- **Type**: typing.Optional[str]


# JourneyResponse

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ActivityOutput]]

### CreationDate
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyLimits]

### LocalTime
- **Type**: typing.Optional[bool]

### QuietTime
- **Type**: <class 'NoneType'>

### RefreshFrequency
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyScheduleOutput]

### StartActivity
- **Type**: typing.Optional[str]

### StartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.StartConditionOutput]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELLED', 'CLOSED', 'COMPLETED', 'DRAFT', 'PAUSED']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### WaitForQuietTime
- **Type**: typing.Optional[bool]

### RefreshOnSegmentUpdate
- **Type**: typing.Optional[bool]

### JourneyChannelSettings
- **Type**: <class 'NoneType'>

### SendingSchedule
- **Type**: typing.Optional[bool]

### OpenHours
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursOutput]

### ClosedDays
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysOutput]

### TimezoneEstimationMethods
- **Type**: typing.Optional[typing.List[typing.Literal['PHONE_NUMBER', 'POSTAL_CODE']]]


# JourneyRunExecutionActivityMetricsResponse

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


# JourneyRunExecutionMetricsResponse

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


# JourneyRunResponse

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


# JourneyRunsResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyRunResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# JourneySMSMessage

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


# JourneySchedule

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Timezone
- **Type**: typing.Optional[str]


# JourneyScheduleOutput

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Timezone
- **Type**: typing.Optional[str]


# JourneyStateRequest

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELLED', 'CLOSED', 'COMPLETED', 'DRAFT', 'PAUSED']]


# JourneyTimeframeCap

### Cap
- **Type**: typing.Optional[int]

### Days
- **Type**: typing.Optional[int]


# JourneysResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJourneysRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PageSize
- **Type**: typing.Optional[str]

### Token
- **Type**: typing.Optional[str]


# ListJourneysResponse

### JourneysResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneysResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# ListRecommenderConfigurationsResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RecommenderConfigurationResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### TagsModel
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TagsModelOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# ListTemplateVersionsRequest

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


# ListTemplateVersionsResponse

### TemplateVersionsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TemplateVersionsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# ListTemplatesRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### TemplateType
- **Type**: typing.Optional[str]


# ListTemplatesResponse

### TemplatesResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TemplatesResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# Message

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


# MessageBody

### Message
- **Type**: typing.Optional[str]

### RequestID
- **Type**: typing.Optional[str]


# MessageConfiguration

### ADMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### APNSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### BaiduMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### CustomMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignCustomMessage]

### DefaultMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### EmailMessage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignEmailMessage, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignEmailMessageOutput, NoneType]

### GCMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### SMSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignSmsMessage]

### InAppMessage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignInAppMessage, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignInAppMessageOutput, NoneType]


# MessageConfigurationOutput

### ADMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### APNSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### BaiduMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### CustomMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignCustomMessage]

### DefaultMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### EmailMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignEmailMessageOutput]

### GCMMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Message]

### SMSMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignSmsMessage]

### InAppMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignInAppMessageOutput]


# MessageHeader

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# MessageRequest

### MessageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.DirectMessageConfiguration'>
- **Required**: Yes

### Addresses
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AddressConfiguration]]

### Context
- **Type**: typing.Optional[typing.Dict[str, str]]

### Endpoints
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointSendConfiguration]]

### TemplateConfiguration
- **Type**: <class 'NoneType'>

### TraceId
- **Type**: typing.Optional[str]


# MessageResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointResult
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointMessageResult]]

### RequestId
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageResult]]


# MessageResult

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


# MetricDimension

### ComparisonOperator
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# MultiConditionalBranch

### Condition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleCondition, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleConditionOutput, NoneType]

### NextActivity
- **Type**: typing.Optional[str]


# MultiConditionalBranchOutput

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleConditionOutput]

### NextActivity
- **Type**: typing.Optional[str]


# MultiConditionalSplitActivity

### Branches
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MultiConditionalBranch, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MultiConditionalBranchOutput]]]

### DefaultActivity
- **Type**: typing.Optional[str]

### EvaluationWaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WaitTime]


# MultiConditionalSplitActivityOutput

### Branches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MultiConditionalBranchOutput]]

### DefaultActivity
- **Type**: typing.Optional[str]

### EvaluationWaitTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WaitTime]


# NumberValidateRequest

### IsoCountryCode
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]


# NumberValidateResponse

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


# OpenHours

### EMAIL
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]

### SMS
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]

### PUSH
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]

### VOICE
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]

### CUSTOM
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]


# OpenHoursOutput

### EMAIL
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]

### SMS
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]

### PUSH
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]

### VOICE
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]

### CUSTOM
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY'], typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursRule]]]


# OpenHoursRule

### StartTime
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[str]


# OverrideButtonConfiguration

### ButtonAction
- **Type**: typing.Literal['CLOSE', 'DEEP_LINK', 'LINK']
- **Required**: Yes

### Link
- **Type**: typing.Optional[str]


# PhoneNumberValidateRequest

### NumberValidateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.NumberValidateRequest'>
- **Required**: Yes


# PhoneNumberValidateResponse

### NumberValidateResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.NumberValidateResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# PublicEndpoint

### Address
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### ChannelType
- **Type**: typing.Optional[typing.Literal['ADM', 'APNS', 'APNS_SANDBOX', 'APNS_VOIP', 'APNS_VOIP_SANDBOX', 'BAIDU', 'CUSTOM', 'EMAIL', 'GCM', 'IN_APP', 'PUSH', 'SMS', 'VOICE']]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointDemographic]

### EffectiveDate
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointLocation]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### OptOut
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointUser, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointUserOutput, NoneType]


# PushMessageActivity

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyPushMessage]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# PushNotificationTemplateRequest

### ADM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AndroidPushNotificationTemplate]

### APNS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSPushNotificationTemplate]

### Baidu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AndroidPushNotificationTemplate]

### Default
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.DefaultPushNotificationTemplate]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### GCM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AndroidPushNotificationTemplate]

### RecommenderId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]


# PushNotificationTemplateResponse

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AndroidPushNotificationTemplate]

### APNS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSPushNotificationTemplate]

### Arn
- **Type**: typing.Optional[str]

### Baidu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AndroidPushNotificationTemplate]

### Default
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.DefaultPushNotificationTemplate]

### DefaultSubstitutions
- **Type**: typing.Optional[str]

### GCM
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AndroidPushNotificationTemplate]

### RecommenderId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateDescription
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# PutEventStreamRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteEventStream
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteEventStream'>
- **Required**: Yes


# PutEventStreamResponse

### EventStream
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventStream'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# PutEventsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EventsRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventsRequest'>
- **Required**: Yes


# PutEventsResponse

### EventsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# QuietTime

### End
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Optional[str]


# RandomSplitActivity

### Branches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RandomSplitEntry]]


# RandomSplitActivityOutput

### Branches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RandomSplitEntry]]


# RandomSplitEntry

### NextActivity
- **Type**: typing.Optional[str]

### Percentage
- **Type**: typing.Optional[int]


# RawEmail

### Data
- **Type**: typing.Union[str, bytes, typing.IO, botocore.response.StreamingBody, NoneType]


# RecencyDimension

### Duration
- **Type**: typing.Literal['DAY_14', 'DAY_30', 'DAY_7', 'HR_24']
- **Required**: Yes

### RecencyType
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes


# RecommenderConfigurationResponse

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


# RemoveAttributesRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeType
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateAttributesRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.UpdateAttributesRequest'>
- **Required**: Yes


# RemoveAttributesResponse

### AttributesResource
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributesResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
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


# ResultRow

### GroupedBys
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResultRowValue]
- **Required**: Yes

### Values
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResultRowValue]
- **Required**: Yes


# ResultRowValue

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SMSChannelRequest

### Enabled
- **Type**: typing.Optional[bool]

### SenderId
- **Type**: typing.Optional[str]

### ShortCode
- **Type**: typing.Optional[str]


# SMSChannelResponse

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


# SMSMessage

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### EntityId
- **Type**: typing.Optional[str]

### TemplateId
- **Type**: typing.Optional[str]


# SMSMessageActivity

### MessageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneySMSMessage]

### NextActivity
- **Type**: typing.Optional[str]

### TemplateName
- **Type**: typing.Optional[str]

### TemplateVersion
- **Type**: typing.Optional[str]


# SMSTemplateRequest

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


# SMSTemplateResponse

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


# Schedule

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[str]

### EventFilter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignEventFilter, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignEventFilterOutput, NoneType]

### Frequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'EVENT', 'HOURLY', 'IN_APP_EVENT', 'MONTHLY', 'ONCE', 'WEEKLY']]

### IsLocalTime
- **Type**: typing.Optional[bool]

### QuietTime
- **Type**: <class 'NoneType'>

### Timezone
- **Type**: typing.Optional[str]


# ScheduleOutput

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[str]

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignEventFilterOutput]

### Frequency
- **Type**: typing.Optional[typing.Literal['DAILY', 'EVENT', 'HOURLY', 'IN_APP_EVENT', 'MONTHLY', 'ONCE', 'WEEKLY']]

### IsLocalTime
- **Type**: typing.Optional[bool]

### QuietTime
- **Type**: <class 'NoneType'>

### Timezone
- **Type**: typing.Optional[str]


# SegmentBehaviors

### Recency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RecencyDimension]


# SegmentCondition

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes


# SegmentDemographics

### AppVersion
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput, NoneType]

### Channel
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput, NoneType]

### DeviceType
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput, NoneType]

### Make
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput, NoneType]

### Model
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput, NoneType]

### Platform
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput, NoneType]


# SegmentDemographicsOutput

### AppVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput]

### Channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput]

### DeviceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput]

### Make
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput]

### Model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput]

### Platform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput]


# SegmentDimensions

### Attributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimensionOutput]]]

### Behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentBehaviors]

### Demographic
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDemographics, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDemographicsOutput, NoneType]

### Location
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentLocation, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentLocationOutput, NoneType]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MetricDimension]]

### UserAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimensionOutput]]]


# SegmentDimensionsOutput

### Attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimensionOutput]]

### Behavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentBehaviors]

### Demographic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDemographicsOutput]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentLocationOutput]

### Metrics
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MetricDimension]]

### UserAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.AttributeDimensionOutput]]


# SegmentGroup

### Dimensions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensions, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensionsOutput]]]

### SourceSegments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentReference]]

### SourceType
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupList

### Groups
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentGroup, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentGroupOutput]]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupListOutput

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentGroupOutput]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupOutput

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensionsOutput]]

### SourceSegments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentReference]]

### SourceType
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentImportResource

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


# SegmentLocation

### Country
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimension, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput, NoneType]

### GPSPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.GPSPointDimension]


# SegmentLocationOutput

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SetDimensionOutput]

### GPSPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.GPSPointDimension]


# SegmentReference

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]


# SegmentResponse

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensionsOutput]

### ImportDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentImportResource]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SegmentGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentGroupListOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Version
- **Type**: typing.Optional[int]


# SegmentsResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SendMessagesRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageRequest'>
- **Required**: Yes


# SendMessagesResponse

### MessageResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# SendOTPMessageRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SendOTPMessageRequestParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SendOTPMessageRequestParameters'>
- **Required**: Yes


# SendOTPMessageRequestParameters

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


# SendOTPMessageResponse

### MessageResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# SendUsersMessageRequest

### MessageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.DirectMessageConfiguration'>
- **Required**: Yes

### Users
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointSendConfiguration]
- **Required**: Yes

### Context
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateConfiguration
- **Type**: <class 'NoneType'>

### TraceId
- **Type**: typing.Optional[str]


# SendUsersMessageResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestId
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointMessageResult]]]


# SendUsersMessagesRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SendUsersMessageRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SendUsersMessageRequest'>
- **Required**: Yes


# SendUsersMessagesResponse

### SendUsersMessageResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SendUsersMessageResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# Session

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


# SetDimension

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### DimensionType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE', 'INCLUSIVE']]


# SetDimensionOutput

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### DimensionType
- **Type**: typing.Optional[typing.Literal['EXCLUSIVE', 'INCLUSIVE']]


# SimpleCondition

### EventCondition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventCondition, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventConditionOutput, NoneType]

### SegmentCondition
- **Type**: <class 'NoneType'>

### SegmentDimensions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensions, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensionsOutput, NoneType]


# SimpleConditionOutput

### EventCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventConditionOutput]

### SegmentCondition
- **Type**: <class 'NoneType'>

### SegmentDimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensionsOutput]


# SimpleEmail

### HtmlPart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleEmailPart]

### Subject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleEmailPart]

### TextPart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SimpleEmailPart]

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageHeader]]


# SimpleEmailPart

### Charset
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[str]


# StartCondition

### Description
- **Type**: typing.Optional[str]

### EventStartCondition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventStartCondition, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventStartConditionOutput, NoneType]

### SegmentStartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentCondition]


# StartConditionOutput

### Description
- **Type**: typing.Optional[str]

### EventStartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EventStartConditionOutput]

### SegmentStartCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentCondition]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagsModel
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TagsModel, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TagsModelOutput]
- **Required**: Yes


# TagsModel

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagsModelOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Template

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# TemplateActiveVersionRequest

### Version
- **Type**: typing.Optional[str]


# TemplateConfiguration

### EmailTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Template]

### PushTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Template]

### SMSTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Template]

### VoiceTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Template]

### InAppTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Template]


# TemplateCreateMessageBody

### Arn
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### RequestID
- **Type**: typing.Optional[str]


# TemplateResponse

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


# TemplateVersionResponse

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


# TemplateVersionsResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TemplateVersionResponse]
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### RequestID
- **Type**: typing.Optional[str]


# TemplatesResponse

### Item
- **Type**: typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TemplateResponse]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# TreatmentResource

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SizePercent
- **Type**: <class 'int'>
- **Required**: Yes

### CustomDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomDeliveryConfigurationOutput]

### MessageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageConfigurationOutput]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ScheduleOutput]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignState]

### TemplateConfiguration
- **Type**: <class 'NoneType'>

### TreatmentDescription
- **Type**: typing.Optional[str]

### TreatmentName
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAdmChannelRequest

### ADMChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ADMChannelRequest'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAdmChannelResponse

### ADMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ADMChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApnsChannelRequest

### APNSChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSChannelRequest'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApnsChannelResponse

### APNSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApnsSandboxChannelRequest

### APNSSandboxChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSSandboxChannelRequest'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApnsSandboxChannelResponse

### APNSSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSSandboxChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApnsVoipChannelRequest

### APNSVoipChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSVoipChannelRequest'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApnsVoipChannelResponse

### APNSVoipChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSVoipChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApnsVoipSandboxChannelRequest

### APNSVoipSandboxChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSVoipSandboxChannelRequest'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApnsVoipSandboxChannelResponse

### APNSVoipSandboxChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.APNSVoipSandboxChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApplicationSettingsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteApplicationSettingsRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteApplicationSettingsRequest'>
- **Required**: Yes


# UpdateApplicationSettingsResponse

### ApplicationSettingsResource
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationSettingsResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAttributesRequest

### Blacklist
- **Type**: typing.Optional[typing.List[str]]


# UpdateBaiduChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### BaiduChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.BaiduChannelRequest'>
- **Required**: Yes


# UpdateBaiduChannelResponse

### BaiduChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.BaiduChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCampaignRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CampaignId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteCampaignRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteCampaignRequest'>
- **Required**: Yes


# UpdateCampaignResponse

### CampaignResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEmailChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EmailChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailChannelRequest'>
- **Required**: Yes


# UpdateEmailChannelResponse

### EmailChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEmailTemplateRequest

### EmailTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EmailTemplateRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdateEmailTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEndpointRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointRequest'>
- **Required**: Yes


# UpdateEndpointResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEndpointsBatchRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointBatchRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.EndpointBatchRequest'>
- **Required**: Yes


# UpdateEndpointsBatchResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGcmChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### GCMChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.GCMChannelRequest'>
- **Required**: Yes


# UpdateGcmChannelResponse

### GCMChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.GCMChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInAppTemplateRequest

### InAppTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.InAppTemplateRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdateInAppTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateJourneyRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteJourneyRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteJourneyRequest'>
- **Required**: Yes


# UpdateJourneyResponse

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateJourneyStateRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyId
- **Type**: <class 'str'>
- **Required**: Yes

### JourneyStateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyStateRequest'>
- **Required**: Yes


# UpdateJourneyStateResponse

### JourneyResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePushTemplateRequest

### PushNotificationTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.PushNotificationTemplateRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdatePushTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRecommenderConfiguration

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


# UpdateRecommenderConfigurationRequest

### RecommenderId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateRecommenderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.UpdateRecommenderConfiguration'>
- **Required**: Yes


# UpdateRecommenderConfigurationResponse

### RecommenderConfigurationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.RecommenderConfigurationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSegmentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentId
- **Type**: <class 'str'>
- **Required**: Yes

### WriteSegmentRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteSegmentRequest'>
- **Required**: Yes


# UpdateSegmentResponse

### SegmentResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSmsChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SMSChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSChannelRequest'>
- **Required**: Yes


# UpdateSmsChannelResponse

### SMSChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSmsTemplateRequest

### SMSTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SMSTemplateRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdateSmsTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTemplateActiveVersionRequest

### TemplateActiveVersionRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.TemplateActiveVersionRequest'>
- **Required**: Yes

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTemplateActiveVersionResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVoiceChannelRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceChannelRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VoiceChannelRequest'>
- **Required**: Yes


# UpdateVoiceChannelResponse

### VoiceChannelResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VoiceChannelResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVoiceTemplateRequest

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceTemplateRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VoiceTemplateRequest'>
- **Required**: Yes

### CreateNewVersion
- **Type**: typing.Optional[bool]

### Version
- **Type**: typing.Optional[str]


# UpdateVoiceTemplateResponse

### MessageBody
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# VerificationResponse

### Valid
- **Type**: typing.Optional[bool]


# VerifyOTPMessageRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### VerifyOTPMessageRequestParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VerifyOTPMessageRequestParameters'>
- **Required**: Yes


# VerifyOTPMessageRequestParameters

### DestinationIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### Otp
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyOTPMessageResponse

### VerificationResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.VerificationResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ResponseMetadata'>
- **Required**: Yes


# VoiceChannelRequest

### Enabled
- **Type**: typing.Optional[bool]


# VoiceChannelResponse

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


# VoiceMessage

### Body
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### OriginationNumber
- **Type**: typing.Optional[str]

### Substitutions
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### VoiceId
- **Type**: typing.Optional[str]


# VoiceTemplateRequest

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

### VoiceId
- **Type**: typing.Optional[str]


# VoiceTemplateResponse

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


# WaitActivity

### NextActivity
- **Type**: typing.Optional[str]

### WaitTime
- **Type**: <class 'NoneType'>


# WaitTime

### WaitFor
- **Type**: typing.Optional[str]

### WaitUntil
- **Type**: typing.Optional[str]


# WriteApplicationSettingsRequest

### CampaignHook
- **Type**: <class 'NoneType'>

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### EventTaggingEnabled
- **Type**: typing.Optional[bool]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignLimits]

### QuietTime
- **Type**: <class 'NoneType'>

### JourneyLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ApplicationSettingsJourneyLimits]


# WriteCampaignRequest

### AdditionalTreatments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.WriteTreatmentResource]]

### CustomDeliveryConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomDeliveryConfiguration, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomDeliveryConfigurationOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### HoldoutPercent
- **Type**: typing.Optional[int]

### Hook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignHook]

### IsPaused
- **Type**: typing.Optional[bool]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CampaignLimits]

### MessageConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageConfiguration, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageConfigurationOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Schedule, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ScheduleOutput, NoneType]

### SegmentId
- **Type**: typing.Optional[str]

### SegmentVersion
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateConfiguration
- **Type**: <class 'NoneType'>

### TreatmentDescription
- **Type**: typing.Optional[str]

### TreatmentName
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]


# WriteEventStream

### DestinationStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# WriteJourneyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Activities
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Activity, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ActivityOutput]]]

### CreationDate
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[str]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyLimits]

### LocalTime
- **Type**: typing.Optional[bool]

### QuietTime
- **Type**: <class 'NoneType'>

### RefreshFrequency
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneySchedule, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.JourneyScheduleOutput, NoneType]

### StartActivity
- **Type**: typing.Optional[str]

### StartCondition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.StartCondition, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.StartConditionOutput, NoneType]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELLED', 'CLOSED', 'COMPLETED', 'DRAFT', 'PAUSED']]

### WaitForQuietTime
- **Type**: typing.Optional[bool]

### RefreshOnSegmentUpdate
- **Type**: typing.Optional[bool]

### JourneyChannelSettings
- **Type**: <class 'NoneType'>

### SendingSchedule
- **Type**: typing.Optional[bool]

### OpenHours
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHours, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.OpenHoursOutput, NoneType]

### ClosedDays
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDays, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ClosedDaysOutput, NoneType]

### TimezoneEstimationMethods
- **Type**: typing.Optional[typing.List[typing.Literal['PHONE_NUMBER', 'POSTAL_CODE']]]


# WriteSegmentRequest

### Dimensions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensions, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentDimensionsOutput, NoneType]

### Name
- **Type**: typing.Optional[str]

### SegmentGroups
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentGroupList, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.SegmentGroupListOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# WriteTreatmentResource

### SizePercent
- **Type**: <class 'int'>
- **Required**: Yes

### CustomDeliveryConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomDeliveryConfiguration, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.CustomDeliveryConfigurationOutput, NoneType]

### MessageConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageConfiguration, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.MessageConfigurationOutput, NoneType]

### Schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.Schedule, aws_resource_validator.pydantic_models.pinpoint.pinpoint_classes.ScheduleOutput, NoneType]

### TemplateConfiguration
- **Type**: <class 'NoneType'>

### TreatmentDescription
- **Type**: typing.Optional[str]

### TreatmentName
- **Type**: typing.Optional[str]


