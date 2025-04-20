# Arc Zonal Shift Arc Zonal Shift Classes

# AutoshiftInResource

### appliedStatus
- **Type**: typing.Literal['APPLIED', 'NOT_APPLIED']
- **Required**: Yes

### awayFrom
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# AutoshiftSummary

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

# CancelZonalShiftRequest

### zonalShiftId
- **Type**: <class 'str'>
- **Required**: Yes


# ControlCondition

### alarmIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['CLOUDWATCH']
- **Required**: Yes


# CreatePracticeRunConfigurationRequest

### outcomeAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ControlCondition]
- **Required**: Yes

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### blockedDates
- **Type**: typing.Optional[typing.List[str]]

### blockedWindows
- **Type**: typing.Optional[typing.List[str]]

### blockingAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ControlCondition]]


# CreatePracticeRunConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### practiceRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.PracticeRunConfiguration'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePracticeRunConfigurationRequest

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePracticeRunConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes


# GetAutoshiftObserverNotificationStatusResponse

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedResourceRequest

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedResourceResponse

### appliedWeights
- **Type**: typing.Dict[str, float]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### autoshifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.AutoshiftInResource]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### practiceRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.PracticeRunConfiguration'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### zonalShifts
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ZonalShiftInResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes


# ListAutoshiftsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETED']]


# ListAutoshiftsRequestPaginate

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.PaginatorConfig]


# ListAutoshiftsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.AutoshiftSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedResourcesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedResourcesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.PaginatorConfig]


# ListManagedResourcesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ManagedResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListZonalShiftsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELED', 'EXPIRED']]


# ListZonalShiftsRequestPaginate

### resourceIdentifier
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELED', 'EXPIRED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.PaginatorConfig]


# ListZonalShiftsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ZonalShiftSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ManagedResourceSummary

### availabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### appliedWeights
- **Type**: typing.Optional[typing.Dict[str, float]]

### arn
- **Type**: typing.Optional[str]

### autoshifts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.AutoshiftInResource]]

### name
- **Type**: typing.Optional[str]

### practiceRunStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### zonalAutoshiftStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### zonalShifts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ZonalShiftInResource]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PracticeRunConfiguration

### outcomeAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ControlCondition]
- **Required**: Yes

### blockedDates
- **Type**: typing.Optional[typing.List[str]]

### blockedWindows
- **Type**: typing.Optional[typing.List[str]]

### blockingAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ControlCondition]]


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


# StartZonalShiftRequest

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


# UpdateAutoshiftObserverNotificationStatusRequest

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateAutoshiftObserverNotificationStatusResponse

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePracticeRunConfigurationRequest

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### blockedDates
- **Type**: typing.Optional[typing.List[str]]

### blockedWindows
- **Type**: typing.Optional[typing.List[str]]

### blockingAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ControlCondition]]

### outcomeAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ControlCondition]]


# UpdatePracticeRunConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### practiceRunConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.PracticeRunConfiguration'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateZonalAutoshiftConfigurationRequest

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# UpdateZonalAutoshiftConfigurationResponse

### resourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### zonalAutoshiftStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateZonalShiftRequest

### zonalShiftId
- **Type**: <class 'str'>
- **Required**: Yes

### comment
- **Type**: typing.Optional[str]

### expiresIn
- **Type**: typing.Optional[str]


# ZonalShift

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
- **Type**: <class 'aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_classes.ResponseMetadata'>
- **Required**: Yes


# ZonalShiftInResource

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


# ZonalShiftSummary

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


