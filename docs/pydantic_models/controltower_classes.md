# Controltower Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaselineOperation

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


# BaselineSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ControlOperation

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


# ControlOperationFilter

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


# ControlOperationSummary

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


# CreateLandingZoneInput

### manifest
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLandingZoneOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLandingZoneInput

### landingZoneIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLandingZoneOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# DisableBaselineInput

### enabledBaselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisableBaselineOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# DisableControlInput

### controlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisableControlOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# DriftStatusSummary

### driftStatus
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKING', 'UNKNOWN']]


# EnableBaselineInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineParameter]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# EnableBaselineOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# EnableControlInput

### controlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.controltower_classes.EnabledControlParameter]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# EnableControlOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# EnabledBaselineDetails

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### baselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.EnablementStatusSummary'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### baselineVersion
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineParameterSummary]]

### parentIdentifier
- **Type**: typing.Optional[str]


# EnabledBaselineFilter

### baselineIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### parentIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### targetIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# EnabledBaselineParameter

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# EnabledBaselineParameterSummary

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# EnabledBaselineSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### baselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.EnablementStatusSummary'>
- **Required**: Yes

### targetIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### baselineVersion
- **Type**: typing.Optional[str]

### parentIdentifier
- **Type**: typing.Optional[str]


# EnabledControlDetails

### arn
- **Type**: typing.Optional[str]

### controlIdentifier
- **Type**: typing.Optional[str]

### driftStatusSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.DriftStatusSummary]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.controltower_classes.EnabledControlParameterSummary]]

### statusSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.EnablementStatusSummary]

### targetIdentifier
- **Type**: typing.Optional[str]

### targetRegions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.controltower_classes.Region]]


# EnabledControlFilter

### controlIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### driftStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DRIFTED', 'IN_SYNC', 'NOT_CHECKING', 'UNKNOWN']]]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'SUCCEEDED', 'UNDER_CHANGE']]]


# EnabledControlParameter

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# EnabledControlParameterSummary

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# EnabledControlSummary

### arn
- **Type**: typing.Optional[str]

### controlIdentifier
- **Type**: typing.Optional[str]

### driftStatusSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.DriftStatusSummary]

### statusSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.EnablementStatusSummary]

### targetIdentifier
- **Type**: typing.Optional[str]


# EnablementStatusSummary

### lastOperationIdentifier
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED', 'UNDER_CHANGE']]


# GetBaselineInput

### baselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetBaselineOperationInput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetBaselineOperationOutput

### baselineOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.BaselineOperation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# GetBaselineOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# GetControlOperationInput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetControlOperationOutput

### controlOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ControlOperation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnabledBaselineInput

### enabledBaselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnabledBaselineOutput

### enabledBaselineDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# GetEnabledControlInput

### enabledControlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnabledControlOutput

### enabledControlDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.EnabledControlDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# GetLandingZoneInput

### landingZoneIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLandingZoneOperationInput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLandingZoneOperationOutput

### operationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.LandingZoneOperationDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# GetLandingZoneOutput

### landingZone
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.LandingZoneDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# LandingZoneDetail

### manifest
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### driftStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.LandingZoneDriftStatusSummary]

### latestAvailableVersion
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'PROCESSING']]


# LandingZoneDriftStatusSummary

### status
- **Type**: typing.Optional[typing.Literal['DRIFTED', 'IN_SYNC']]


# LandingZoneOperationDetail

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


# LandingZoneOperationSummary

### operationIdentifier
- **Type**: typing.Optional[str]

### operationType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'RESET', 'UPDATE']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# LandingZoneSummary

### arn
- **Type**: typing.Optional[str]


# ListBaselinesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBaselinesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.PaginatorConfig]


# ListBaselinesOutput

### baselines
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.BaselineSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListControlOperationsOutput

### controlOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.ControlOperationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnabledBaselinesOutput

### enabledBaselines
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEnabledControlsOutput

### enabledControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.EnabledControlSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLandingZoneOperationsOutput

### landingZoneOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.LandingZoneOperationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLandingZonesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLandingZonesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controltower_classes.PaginatorConfig]


# ListLandingZonesOutput

### landingZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.controltower_classes.LandingZoneSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Region

### name
- **Type**: typing.Optional[str]


# ResetEnabledBaselineInput

### enabledBaselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResetEnabledBaselineOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# ResetEnabledControlInput

### enabledControlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResetEnabledControlOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# ResetLandingZoneInput

### landingZoneIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResetLandingZoneOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
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


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnabledBaselineInput

### baselineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### enabledBaselineIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.controltower_classes.EnabledBaselineParameter]]


# UpdateEnabledBaselineOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEnabledControlInput

### enabledControlIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.controltower_classes.EnabledControlParameter]
- **Required**: Yes


# UpdateEnabledControlOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLandingZoneInput

### landingZoneIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### manifest
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateLandingZoneOutput

### operationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controltower_classes.ResponseMetadata'>
- **Required**: Yes


