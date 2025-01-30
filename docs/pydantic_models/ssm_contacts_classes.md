# ssm_contacts_classes

# AcceptPageRequestRequestTypeDef

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


# ActivateContactChannelRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactChannelAddressTypeDef'>
- **Required**: Yes

### ActivationStatus
- **Type**: typing.Literal['ACTIVATED', 'NOT_ACTIVATED']
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SMS', 'VOICE']]


# ContactTargetInfoTypeDef

### IsEssential
- **Type**: <class 'bool'>
- **Required**: Yes

### ContactId
- **Type**: typing.Optional[str]


# ContactTypeDef

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


# CoverageTimeTypeDef

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef]


# CreateContactChannelRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactChannelAddressTypeDef'>
- **Required**: Yes

### DeferActivation
- **Type**: typing.Optional[bool]

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateContactChannelResultTypeDef

### ContactChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContactRequestRequestTypeDef

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']
- **Required**: Yes

### Plan
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.PlanTypeDef'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.TagTypeDef]]

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateContactResultTypeDef

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRotationOverrideRequestRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### NewContactIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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


# CreateRotationRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# DeactivateContactChannelRequestRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactChannelRequestRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContactRequestRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRotationOverrideRequestRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### RotationOverrideId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRotationRequestRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEngagementRequestRequestTypeDef

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


# DescribePageRequestRequestTypeDef

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


# GetContactChannelRequestRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactChannelResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactChannelAddressTypeDef'>
- **Required**: Yes

### ActivationStatus
- **Type**: typing.Literal['ACTIVATED', 'NOT_ACTIVATED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContactPolicyRequestRequestTypeDef

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


# GetContactRequestRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContactResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.PlanTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRotationOverrideRequestRequestTypeDef

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


# GetRotationRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsTypeDef'>
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


# ListContactChannelsRequestListContactChannelsPaginateTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListContactChannelsRequestRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContactChannelsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ContactChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactChannelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContactsRequestListContactsPaginateTypeDef

### AliasPrefix
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListContactsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AliasPrefix
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']]


# ListContactsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Contacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEngagementsRequestListEngagementsPaginateTypeDef

### IncidentId
- **Type**: typing.Optional[str]

### TimeRangeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimeRangeTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListEngagementsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncidentId
- **Type**: typing.Optional[str]

### TimeRangeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.TimeRangeTypeDef]


# ListEngagementsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Engagements
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.EngagementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPageReceiptsRequestListPageReceiptsPaginateTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPageReceiptsRequestRequestTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPageReceiptsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Receipts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.ReceiptTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPageResolutionsRequestListPageResolutionsPaginateTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPageResolutionsRequestRequestTypeDef

### PageId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPageResolutionsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### PageResolutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.ResolutionContactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPagesByContactRequestListPagesByContactPaginateTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPagesByContactRequestRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPagesByContactResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Pages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.PageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPagesByEngagementRequestListPagesByEngagementPaginateTypeDef

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPagesByEngagementRequestRequestTypeDef

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPagesByEngagementResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Pages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.PageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPreviewRotationShiftsRequestListPreviewRotationShiftsPaginateTypeDef

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Members
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsTypeDef'>
- **Required**: Yes

### RotationStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.PreviewOverrideTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListPreviewRotationShiftsRequestRequestTypeDef

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Members
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TimeZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsTypeDef'>
- **Required**: Yes

### RotationStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRotationOverridesRequestListRotationOverridesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListRotationOverridesRequestRequestTypeDef

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


# ListRotationOverridesResultTypeDef

### RotationOverrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.RotationOverrideTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRotationShiftsRequestListRotationShiftsPaginateTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListRotationShiftsRequestRequestTypeDef

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


# ListRotationShiftsResultTypeDef

### RotationShifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.RotationShiftTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRotationsRequestListRotationsPaginateTypeDef

### RotationNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PaginatorConfigTypeDef]


# ListRotationsRequestRequestTypeDef

### RotationNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRotationsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Rotations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_contacts_classes.RotationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# PlanTypeDef

### Stages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.StageTypeDef]]

### RotationIds
- **Type**: typing.Optional[typing.Sequence[str]]


# PreviewOverrideTypeDef

### NewMembers
- **Type**: typing.Optional[typing.Sequence[str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PutContactPolicyRequestRequestTypeDef

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


# ResolutionContactTypeDef

### ContactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ESCALATION', 'ONCALL_SCHEDULE', 'PERSONAL']
- **Required**: Yes

### StageIndex
- **Type**: typing.Optional[int]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.ShiftDetailsTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsTypeDef]


# SendActivationCodeRequestRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes


# ShiftDetailsTypeDef

### OverriddenContactIds
- **Type**: typing.List[str]
- **Required**: Yes


# StageTypeDef

### DurationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_contacts_classes.TargetTypeDef]
- **Required**: Yes


# StartEngagementRequestRequestTypeDef

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


# StopEngagementRequestRequestTypeDef

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### Reason
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateContactChannelRequestRequestTypeDef

### ContactChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DeliveryAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.ContactChannelAddressTypeDef]


# UpdateContactRequestRequestTypeDef

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Plan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_contacts_classes.PlanTypeDef]


# UpdateRotationRequestRequestTypeDef

### RotationId
- **Type**: <class 'str'>
- **Required**: Yes

### Recurrence
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.RecurrenceSettingsTypeDef'>
- **Required**: Yes

### ContactIds
- **Type**: typing.Optional[typing.Sequence[str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### TimeZoneId
- **Type**: typing.Optional[str]


# WeeklySettingTypeDef

### DayOfWeek
- **Type**: typing.Literal['FRI', 'MON', 'SAT', 'SUN', 'THU', 'TUE', 'WED']
- **Required**: Yes

### HandOffTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_contacts_classes.HandOffTimeTypeDef'>
- **Required**: Yes


