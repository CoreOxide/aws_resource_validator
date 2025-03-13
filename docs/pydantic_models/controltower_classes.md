# Controltower Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaselineOperationTypeDef

### endTime
- **Type**: typing.Optional[datetime.datetime]

### operationIdentifier
- **Type**: typing.Optional[str]

### operationType
- **Type**: typing.Optional[typing.Literal['DISABLE_BASELINE', 'ENABLE_BASELINE', 'RESET_ENABLED_BASELINE', 'UPDATE_ENABLED_BASELINE']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]


# BaselineSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ControlOperationFilterTypeDef

### controlIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### controlOperationTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DISABLE_CONTROL', 'ENABLE_CONTROL', 'RESET_ENABLED_CONTROL', 'UPDATE_ENABLED_CONTROL']]]

### enabledControlIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]]

### targetIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# ControlOperationSummaryTypeDef

### controlIdentifier
- **Type**: typing.Optional[str]

### enabledControlIdentifier
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### operationIdentifier
- **Type**: typing.Optional[str]

### operationType
- **Type**: typing.Optional[typing.Literal['DISABLE_CONTROL', 'ENABLE_CONTROL', 'RESET_ENABLED_CONTROL', 'UPDATE_ENABLED_CONTROL']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]

### targetIdentifier
- **Type**: typing.Optional[str]


# ControlOperationTypeDef

### controlIdentifier
- **Type**: typing.Optional[str]

### enabledControlIdentifier
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### operationIdentifier
- **Type**: typing.Optional[str]

### operationType
- **Type**: typing.Optional[typing.Literal['DISABLE_CONTROL', 'ENABLE_CONTROL', 'RESET_ENABLED_CONTROL', 'UPDATE_ENABLED_CONTROL']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]

### targetIdentifier
- **Type**: typing.Optional[str]


# CreateLandingZoneInputTypeDef

### manifest
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLandingZoneOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLandingZoneInputTypeDef

### landingZoneIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLandingZoneOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableBaselineInputTypeDef

### enabledBaselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisableBaselineOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableControlInputTypeDef

### controlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisableControlOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DriftStatusSummaryTypeDef

### driftStatus
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKING', 'UNKNOWN']]


# EnableBaselineInputTypeDef

### baselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### baselineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineParameterTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# EnableBaselineOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableControlInputTypeDef

### controlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.controltower_classes.EnabledControlParameterTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# EnableControlOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnabledBaselineDetailsTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### baselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.EnablementStatusSummaryTypeDef'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### baselineVersion
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineParameterSummaryTypeDef]]

### parentIdentifier
- **Type**: typing.Optional[str]


# EnabledBaselineFilterTypeDef

### baselineIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### parentIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### targetIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# EnabledBaselineParameterSummaryTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# EnabledBaselineParameterTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# EnabledBaselineSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### baselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.EnablementStatusSummaryTypeDef'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### baselineVersion
- **Type**: typing.Optional[str]

### parentIdentifier
- **Type**: typing.Optional[str]


# EnabledControlDetailsTypeDef

### arn
- **Type**: typing.Optional[str]

### controlIdentifier
- **Type**: typing.Optional[str]

### driftStatusSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.DriftStatusSummaryTypeDef]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.controltower_classes.EnabledControlParameterSummaryTypeDef]]

### statusSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.EnablementStatusSummaryTypeDef]

### targetIdentifier
- **Type**: typing.Optional[str]

### targetRegions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.controltower_classes.RegionTypeDef]]


# EnabledControlFilterTypeDef

### controlIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### driftStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKING', 'UNKNOWN']]]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'SUCCEEDED', 'UNDER_CHANGE']]]


# EnabledControlParameterSummaryTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# EnabledControlParameterTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# EnabledControlSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### controlIdentifier
- **Type**: typing.Optional[str]

### driftStatusSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.DriftStatusSummaryTypeDef]

### statusSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.EnablementStatusSummaryTypeDef]

### targetIdentifier
- **Type**: typing.Optional[str]


# EnablementStatusSummaryTypeDef

### lastOperationIdentifier
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED', 'UNDER_CHANGE']]


# GetBaselineInputTypeDef

### baselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetBaselineOperationInputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetBaselineOperationOutputTypeDef

### baselineOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.BaselineOperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBaselineOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetControlOperationInputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetControlOperationOutputTypeDef

### controlOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ControlOperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnabledBaselineInputTypeDef

### enabledBaselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnabledBaselineOutputTypeDef

### enabledBaselineDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnabledControlInputTypeDef

### enabledControlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnabledControlOutputTypeDef

### enabledControlDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.EnabledControlDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLandingZoneInputTypeDef

### landingZoneIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLandingZoneOperationInputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLandingZoneOperationOutputTypeDef

### operationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.LandingZoneOperationDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLandingZoneOutputTypeDef

### landingZone
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.LandingZoneDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LandingZoneDetailTypeDef

### manifest
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### driftStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.LandingZoneDriftStatusSummaryTypeDef]

### latestAvailableVersion
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'PROCESSING']]


# LandingZoneDriftStatusSummaryTypeDef

### status
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC']]


# LandingZoneOperationDetailTypeDef

### endTime
- **Type**: typing.Optional[datetime.datetime]

### operationIdentifier
- **Type**: typing.Optional[str]

### operationType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'RESET', 'UPDATE']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]


# LandingZoneOperationSummaryTypeDef

### operationIdentifier
- **Type**: typing.Optional[str]

### operationType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'RESET', 'UPDATE']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# LandingZoneSummaryTypeDef

### arn
- **Type**: typing.Optional[str]


# ListBaselinesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.PaginatorConfigTypeDef]


# ListBaselinesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBaselinesOutputTypeDef

### baselines
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.BaselineSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListControlOperationsOutputTypeDef

### controlOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.ControlOperationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnabledBaselinesOutputTypeDef

### enabledBaselines
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnabledControlsOutputTypeDef

### enabledControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.EnabledControlSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLandingZoneOperationsOutputTypeDef

### landingZoneOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.LandingZoneOperationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLandingZonesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.PaginatorConfigTypeDef]


# ListLandingZonesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLandingZonesOutputTypeDef

### landingZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.LandingZoneSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegionTypeDef

### name
- **Type**: typing.Optional[str]


# ResetEnabledBaselineInputTypeDef

### enabledBaselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResetEnabledBaselineOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResetEnabledControlInputTypeDef

### enabledControlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResetEnabledControlOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResetLandingZoneInputTypeDef

### landingZoneIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResetLandingZoneOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
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


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnabledBaselineInputTypeDef

### baselineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### enabledBaselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineParameterTypeDef]]


# UpdateEnabledBaselineOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEnabledControlInputTypeDef

### enabledControlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.controltower_classes.EnabledControlParameterTypeDef]
- **Required**: Yes


# UpdateEnabledControlOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLandingZoneInputTypeDef

### landingZoneIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### manifest
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateLandingZoneOutputTypeDef

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


