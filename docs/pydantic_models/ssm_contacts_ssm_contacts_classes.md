# Ssm Contacts Ssm Contacts Classes

# AcceptPageRequest

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptType
- **Type**: typing.Literal['DELIVERED', 'READ']
- **Required**: Yes

### AcceptCode
- **Type**: <class 'str'>
- **Required**: Yes

### ContactChannelId
- **Type**: typing.Optional[str]

### Note
- **Type**: typing.Optional[str]

### AcceptCodeValidation
- **Type**: typing.Optional[typing.Literal['ENFORCE', 'IGNORE']]


# ActivateContactChannelRequest

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ActivationCode
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelTargetInfo

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### RetryIntervalInMinutes
- **Type**: typing.Optional[int]


# Contact

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# ContactChannel

### ContactChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ContactChannelAddress'>
- **Required**: Yes

### ActivationStatus
- **Type**: typing.Literal['ACTIVATED', 'NOT_ACTIVATED']
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SMS', 'VOICE']]


# ContactChannelAddress

### SimpleAddress
- **Type**: typing.Optional[str]


# ContactTargetInfo

### IsEssential
- **Type**: <class 'bool'>
- **Required**: Yes

### ContactId
- **Type**: typing.Optional[str]


# CoverageTime

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.HandOffTime]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.HandOffTime]


# CreateContactChannelRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['EMAIL', 'SMS', 'VOICE']
- **Required**: Yes

### DeliveryAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ContactChannelAddress'>
- **Required**: Yes

### DeferActivation
- **Type**: typing.Optional[bool]

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateContactChannelResult

### ContactChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContactRequest

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']
- **Required**: Yes

### Plan
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Plan, aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PlanOutput]
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Tag]]

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateContactResult

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRotationOverrideRequest

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### NewContactIds
- **Type**: typing.List[str]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateRotationOverrideResult

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRotationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContactIds
- **Type**: typing.List[str]
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettings, aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettingsOutput]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Tag]]

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateRotationResult

### RotationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# DeactivateContactChannelRequest

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactChannelRequest

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRotationOverrideRequest

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRotationRequest

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEngagementRequest

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEngagementResult

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sender
- **Type**: <class 'str'>
- **Required**: Yes

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### PublicSubject
- **Type**: <class 'str'>
- **Required**: Yes

### PublicContent
- **Type**: <class 'str'>
- **Required**: Yes

### IncidentId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StopTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePageRequest

### PageId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePageResult

### PageArn
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sender
- **Type**: <class 'str'>
- **Required**: Yes

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### PublicSubject
- **Type**: <class 'str'>
- **Required**: Yes

### PublicContent
- **Type**: <class 'str'>
- **Required**: Yes

### IncidentId
- **Type**: <class 'str'>
- **Required**: Yes

### SentTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReadTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeliveryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# Engagement

### EngagementArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sender
- **Type**: <class 'str'>
- **Required**: Yes

### IncidentId
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### StopTime
- **Type**: typing.Optional[datetime.datetime]


# GetContactChannelRequest

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactChannelResult

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContactChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['EMAIL', 'SMS', 'VOICE']
- **Required**: Yes

### DeliveryAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ContactChannelAddress'>
- **Required**: Yes

### ActivationStatus
- **Type**: typing.Literal['ACTIVATED', 'NOT_ACTIVATED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# GetContactPolicyRequest

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactPolicyResult

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# GetContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactResult

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']
- **Required**: Yes

### Plan
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PlanOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# GetRotationOverrideRequest

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRotationOverrideResult

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NewContactIds
- **Type**: typing.List[str]
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# GetRotationRequest

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRotationResult

### RotationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContactIds
- **Type**: typing.List[str]
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettingsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# HandOffTime

### HourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### MinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes


# ListContactChannelsRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContactChannelsRequestPaginate

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListContactChannelsResult

### ContactChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ContactChannel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AliasPrefix
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']]


# ListContactsRequestPaginate

### AliasPrefix
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListContactsResult

### Contacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Contact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngagementsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncidentId
- **Type**: typing.Optional[str]

### TimeRangeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.TimeRange]


# ListEngagementsRequestPaginate

### IncidentId
- **Type**: typing.Optional[str]

### TimeRangeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.TimeRange]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListEngagementsResult

### Engagements
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Engagement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPageReceiptsRequest

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPageReceiptsRequestPaginate

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListPageReceiptsResult

### Receipts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Receipt]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPageResolutionsRequest

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPageResolutionsRequestPaginate

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListPageResolutionsResult

### PageResolutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResolutionContact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPagesByContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPagesByContactRequestPaginate

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListPagesByContactResult

### Pages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Page]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPagesByEngagementRequest

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPagesByEngagementRequestPaginate

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListPagesByEngagementResult

### Pages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Page]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPreviewRotationShiftsRequest

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Members
- **Type**: typing.List[str]
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettings, aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettingsOutput]
- **Required**: Yes

### RotationStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PreviewOverride]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPreviewRotationShiftsRequestPaginate

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Members
- **Type**: typing.List[str]
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettings, aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettingsOutput]
- **Required**: Yes

### RotationStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PreviewOverride]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListPreviewRotationShiftsResult

### RotationShifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RotationShift]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRotationOverridesRequest

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRotationOverridesRequestPaginate

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListRotationOverridesResult

### RotationOverrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RotationOverride]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRotationShiftsRequest

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRotationShiftsRequestPaginate

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListRotationShiftsResult

### RotationShifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RotationShift]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRotationsRequest

### RotationNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRotationsRequestPaginate

### RotationNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PaginatorConfig]


# ListRotationsResult

### Rotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Rotation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResult

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# MonthlySetting

### DayOfMonth
- **Type**: <class 'int'>
- **Required**: Yes

### HandOffTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.HandOffTime'>
- **Required**: Yes


# Page

### PageArn
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sender
- **Type**: <class 'str'>
- **Required**: Yes

### IncidentId
- **Type**: typing.Optional[str]

### SentTime
- **Type**: typing.Optional[datetime.datetime]

### DeliveryTime
- **Type**: typing.Optional[datetime.datetime]

### ReadTime
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Plan

### Stages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Stage]]

### RotationIds
- **Type**: typing.Optional[typing.List[str]]


# PlanOutput

### Stages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.StageOutput]]

### RotationIds
- **Type**: typing.Optional[typing.List[str]]


# PreviewOverride

### NewMembers
- **Type**: typing.Optional[typing.List[str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PutContactPolicyRequest

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# Receipt

### ReceiptType
- **Type**: typing.Literal['DELIVERED', 'ERROR', 'READ', 'SENT', 'STOP']
- **Required**: Yes

### ReceiptTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ContactChannelArn
- **Type**: typing.Optional[str]

### ReceiptInfo
- **Type**: typing.Optional[str]


# RecurrenceSettings

### NumberOfOnCalls
- **Type**: <class 'int'>
- **Required**: Yes

### RecurrenceMultiplier
- **Type**: <class 'int'>
- **Required**: Yes

### MonthlySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.MonthlySetting]]

### WeeklySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.WeeklySetting]]

### DailySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.HandOffTime]]

### ShiftCoverages
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED'], typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.CoverageTime]]]


# RecurrenceSettingsOutput

### NumberOfOnCalls
- **Type**: <class 'int'>
- **Required**: Yes

### RecurrenceMultiplier
- **Type**: <class 'int'>
- **Required**: Yes

### MonthlySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.MonthlySetting]]

### WeeklySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.WeeklySetting]]

### DailySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.HandOffTime]]

### ShiftCoverages
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED'], typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.CoverageTime]]]


# ResolutionContact

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']
- **Required**: Yes

### StageIndex
- **Type**: typing.Optional[int]


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


# Rotation

### RotationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContactIds
- **Type**: typing.Optional[typing.List[str]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### TimeZoneId
- **Type**: typing.Optional[str]

### Recurrence
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettingsOutput]


# RotationOverride

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes

### NewContactIds
- **Type**: typing.List[str]
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# RotationShift

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ContactIds
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[typing.Literal['OVERRIDDEN', 'REGULAR']]

### ShiftDetails
- **Type**: <class 'NoneType'>


# SendActivationCodeRequest

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# ShiftDetails

### OverriddenContactIds
- **Type**: typing.List[str]
- **Required**: Yes


# Stage

### DurationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Target]
- **Required**: Yes


# StageOutput

### DurationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Target]
- **Required**: Yes


# StartEngagementRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### Sender
- **Type**: <class 'str'>
- **Required**: Yes

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### PublicSubject
- **Type**: typing.Optional[str]

### PublicContent
- **Type**: typing.Optional[str]

### IncidentId
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]


# StartEngagementResult

### EngagementArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ResponseMetadata'>
- **Required**: Yes


# StopEngagementRequest

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Tag]
- **Required**: Yes


# Target

### ChannelTargetInfo
- **Type**: <class 'NoneType'>

### ContactTargetInfo
- **Type**: <class 'NoneType'>


# TimeRange

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateContactChannelRequest

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DeliveryAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.ContactChannelAddress]


# UpdateContactRequest

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Plan
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.Plan, aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.PlanOutput, NoneType]


# UpdateRotationRequest

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettings, aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.RecurrenceSettingsOutput]
- **Required**: Yes

### ContactIds
- **Type**: typing.Optional[typing.List[str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### TimeZoneId
- **Type**: typing.Optional[str]


# WeeklySetting

### DayOfWeek
- **Type**: typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']
- **Required**: Yes

### HandOffTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_classes.HandOffTime'>
- **Required**: Yes


