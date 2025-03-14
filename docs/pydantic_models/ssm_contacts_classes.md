# Ssm Contacts Classes

# AcceptPageRequestTypeDef

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


# ActivateContactChannelRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ActivationCode
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelTargetInfoTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### RetryIntervalInMinutes
- **Type**: typing.Optional[int]


# ContactChannelAddressTypeDef

### SimpleAddress
- **Type**: typing.Optional[str]


# ContactChannelTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContactTargetInfoTypeDef

### IsEssential
- **Type**: <class 'bool'>
- **Required**: Yes

### ContactId
- **Type**: typing.Optional[str]


# ContactTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CoverageTimeTypeDef

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef]


# CreateContactChannelResultTypeDef

### ContactChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContactResultTypeDef

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRotationOverrideRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### NewContactIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateRotationOverrideResultTypeDef

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRotationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContactIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsUnionTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.TagTypeDef]]

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateRotationResultTypeDef

### RotationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeactivateContactChannelRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactChannelRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRotationOverrideRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRotationRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEngagementRequestTypeDef

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEngagementResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePageRequestTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePageResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EngagementTypeDef

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


# GetContactChannelRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactPolicyRequestTypeDef

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactPolicyResultTypeDef

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRotationOverrideRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRotationOverrideResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRotationRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRotationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HandOffTimeTypeDef

### HourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### MinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes


# ListContactChannelsRequestPaginateTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListContactChannelsRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContactChannelsResultTypeDef

### ContactChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactChannelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContactsResultTypeDef

### Contacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngagementsRequestPaginateTypeDef

### IncidentId
- **Type**: typing.Optional[str]

### TimeRangeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimeRangeTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListEngagementsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncidentId
- **Type**: typing.Optional[str]

### TimeRangeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimeRangeTypeDef]


# ListEngagementsResultTypeDef

### Engagements
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.EngagementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPageReceiptsRequestPaginateTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPageReceiptsRequestTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPageReceiptsResultTypeDef

### Receipts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.ReceiptTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPageResolutionsRequestPaginateTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPageResolutionsRequestTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPageResolutionsResultTypeDef

### PageResolutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.ResolutionContactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPagesByContactRequestPaginateTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPagesByContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPagesByContactResultTypeDef

### Pages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.PageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPagesByEngagementRequestPaginateTypeDef

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPagesByEngagementRequestTypeDef

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPagesByEngagementResultTypeDef

### Pages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.PageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPreviewRotationShiftsRequestPaginateTypeDef

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### Members
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsUnionTypeDef'>
- **Required**: Yes

### RotationStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### Overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.PreviewOverrideTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPreviewRotationShiftsRequestTypeDef

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### Members
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsUnionTypeDef'>
- **Required**: Yes

### RotationStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### Overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.PreviewOverrideTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPreviewRotationShiftsResultTypeDef

### RotationShifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.RotationShiftTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRotationOverridesRequestPaginateTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListRotationOverridesRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRotationOverridesResultTypeDef

### RotationOverrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.RotationOverrideTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRotationShiftsRequestPaginateTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListRotationShiftsRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRotationShiftsResultTypeDef

### RotationShifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.RotationShiftTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRotationsRequestPaginateTypeDef

### RotationNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListRotationsRequestTypeDef

### RotationNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRotationsResultTypeDef

### Rotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.RotationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResultTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MonthlySettingTypeDef

### DayOfMonth
- **Type**: <class 'int'>
- **Required**: Yes

### HandOffTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef'>
- **Required**: Yes


# PageTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlanOutputTypeDef

### Stages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.StageOutputTypeDef]]

### RotationIds
- **Type**: typing.Optional[typing.List[str]]


# PlanTypeDef

### Stages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.StageTypeDef]]

### RotationIds
- **Type**: typing.Optional[typing.Sequence[str]]


# PlanUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PreviewOverrideTypeDef

### NewMembers
- **Type**: typing.Optional[typing.Sequence[str]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]


# PutContactPolicyRequestTypeDef

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# ReceiptTypeDef

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


# RecurrenceSettingsOutputTypeDef

### NumberOfOnCalls
- **Type**: <class 'int'>
- **Required**: Yes

### RecurrenceMultiplier
- **Type**: <class 'int'>
- **Required**: Yes

### MonthlySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.MonthlySettingTypeDef]]

### WeeklySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.WeeklySettingTypeDef]]

### DailySettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef]]

### ShiftCoverages
- **Type**: typing.Optional[typing.Dict[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED'], typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.CoverageTimeTypeDef]]]


# RecurrenceSettingsTypeDef

### NumberOfOnCalls
- **Type**: <class 'int'>
- **Required**: Yes

### RecurrenceMultiplier
- **Type**: <class 'int'>
- **Required**: Yes

### MonthlySettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.MonthlySettingTypeDef]]

### WeeklySettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.WeeklySettingTypeDef]]

### DailySettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef]]

### ShiftCoverages
- **Type**: typing.Optional[typing.Mapping[typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED'], typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.CoverageTimeTypeDef]]]


# RecurrenceSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResolutionContactTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RotationOverrideTypeDef

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


# RotationShiftTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RotationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsOutputTypeDef]


# SendActivationCodeRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# ShiftDetailsTypeDef

### OverriddenContactIds
- **Type**: typing.List[str]
- **Required**: Yes


# StageOutputTypeDef

### DurationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.TargetTypeDef]
- **Required**: Yes


# StageTypeDef

### DurationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.TargetTypeDef]
- **Required**: Yes


# StartEngagementRequestTypeDef

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


# StartEngagementResultTypeDef

### EngagementArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopEngagementRequestTypeDef

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TargetTypeDef

### ChannelTargetInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.ChannelTargetInfoTypeDef]

### ContactTargetInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactTargetInfoTypeDef]


# TimeRangeTypeDef

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateContactChannelRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DeliveryAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactChannelAddressTypeDef]


# UpdateContactRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Plan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PlanUnionTypeDef]


# UpdateRotationRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsUnionTypeDef'>
- **Required**: Yes

### ContactIds
- **Type**: typing.Optional[typing.Sequence[str]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimestampTypeDef]

### TimeZoneId
- **Type**: typing.Optional[str]


# WeeklySettingTypeDef

### DayOfWeek
- **Type**: typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']
- **Required**: Yes

### HandOffTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef'>
- **Required**: Yes


