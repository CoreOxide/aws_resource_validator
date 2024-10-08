# Pydantic Models in arc_zonal_shift_classes

# AutoshiftInResourceTypeDef

### appliedStatus
- **Type**: typing.Literal['APPLIED', 'NOT_APPLIED']
- **Required**: Yes

### awayFrom
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# AutoshiftSummaryTypeDef

### awayFrom
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COMPLETED']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelZonalShiftRequestRequestTypeDef

### zonalShiftId
- **Type**: <class 'str'>
- **Required**: Yes


# ControlConditionTypeDef

### alarmIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CLOUDWATCH']
- **Required**: Yes


# CreatePracticeRunConfigurationRequestRequestTypeDef

### outcomeAlarms
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ControlConditionTypeDef]
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### blockedDates
- **Type**: typing.Optional[typing.Sequence[str]]

### blockedWindows
- **Type**: typing.Optional[typing.Sequence[str]]

### blockingAlarms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ControlConditionTypeDef]]


# CreatePracticeRunConfigurationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### practiceRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.PracticeRunConfigurationTypeDef'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePracticeRunConfigurationRequestRequestTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePracticeRunConfigurationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetManagedResourceRequestRequestTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedResourceResponseTypeDef

### appliedWeights
- **Type**: typing.Dict[str, float]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### autoshifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.AutoshiftInResourceTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### practiceRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.PracticeRunConfigurationTypeDef'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### zonalShifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ZonalShiftInResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAutoshiftsRequestListAutoshiftsPaginateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.PaginatorConfigTypeDef]


# ListAutoshiftsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETED']]


# ListAutoshiftsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.AutoshiftSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListManagedResourcesRequestListManagedResourcesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.PaginatorConfigTypeDef]


# ListManagedResourcesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedResourcesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ManagedResourceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListZonalShiftsRequestListZonalShiftsPaginateTypeDef

### resourceIdentifier
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELED', 'EXPIRED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.PaginatorConfigTypeDef]


# ListZonalShiftsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELED', 'EXPIRED']]


# ListZonalShiftsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ZonalShiftSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagedResourceSummaryTypeDef

### availabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### appliedWeights
- **Type**: typing.Optional[typing.Dict[str, float]]

### arn
- **Type**: typing.Optional[str]

### autoshifts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.AutoshiftInResourceTypeDef]]

### name
- **Type**: typing.Optional[str]

### practiceRunStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### zonalAutoshiftStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### zonalShifts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ZonalShiftInResourceTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PracticeRunConfigurationTypeDef

### outcomeAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ControlConditionTypeDef]
- **Required**: Yes

### blockedDates
- **Type**: typing.Optional[typing.List[str]]

### blockedWindows
- **Type**: typing.Optional[typing.List[str]]

### blockingAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ControlConditionTypeDef]]


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


# StartZonalShiftRequestRequestTypeDef

### awayFrom
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: <class 'str'>
- **Required**: Yes

### expiresIn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePracticeRunConfigurationRequestRequestTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### blockedDates
- **Type**: typing.Optional[typing.Sequence[str]]

### blockedWindows
- **Type**: typing.Optional[typing.Sequence[str]]

### blockingAlarms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ControlConditionTypeDef]]

### outcomeAlarms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ControlConditionTypeDef]]


# UpdatePracticeRunConfigurationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### practiceRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.PracticeRunConfigurationTypeDef'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateZonalAutoshiftConfigurationRequestRequestTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateZonalAutoshiftConfigurationResponseTypeDef

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateZonalShiftRequestRequestTypeDef

### zonalShiftId
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: typing.Optional[str]

### expiresIn
- **Type**: typing.Optional[str]


# ZonalShiftInResourceTypeDef

### appliedStatus
- **Type**: typing.Literal['APPLIED', 'NOT_APPLIED']
- **Required**: Yes

### awayFrom
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: <class 'str'>
- **Required**: Yes

### expiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### zonalShiftId
- **Type**: <class 'str'>
- **Required**: Yes

### practiceRunOutcome
- **Type**: typing.Optional[typing.Literal['FAILED', 'INTERRUPTED', 'PENDING', 'SUCCEEDED']]


# ZonalShiftSummaryTypeDef

### awayFrom
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: <class 'str'>
- **Required**: Yes

### expiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'EXPIRED']
- **Required**: Yes

### zonalShiftId
- **Type**: <class 'str'>
- **Required**: Yes

### practiceRunOutcome
- **Type**: typing.Optional[typing.Literal['FAILED', 'INTERRUPTED', 'PENDING', 'SUCCEEDED']]


# ZonalShiftTypeDef

### awayFrom
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: <class 'str'>
- **Required**: Yes

### expiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'EXPIRED']
- **Required**: Yes

### zonalShiftId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


