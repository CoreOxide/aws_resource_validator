# Location Classes

# ApiKeyFilterTypeDef

### KeyStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Expired']]


# ApiKeyRestrictionsExtraOutputTypeDef

### AllowActions
- **Type**: typing.List[str]
- **Required**: Yes

### AllowResources
- **Type**: typing.List[str]
- **Required**: Yes

### AllowReferers
- **Type**: typing.Optional[typing.List[str]]


# ApiKeyRestrictionsOutputTypeDef

### AllowActions
- **Type**: typing.List[str]
- **Required**: Yes

### AllowResources
- **Type**: typing.List[str]
- **Required**: Yes

### AllowReferers
- **Type**: typing.Optional[typing.List[str]]


# ApiKeyRestrictionsTypeDef

### AllowActions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AllowResources
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AllowReferers
- **Type**: typing.Optional[typing.Sequence[str]]


# AssociateTrackerConsumerRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteDevicePositionHistoryErrorTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.BatchItemErrorTypeDef'>
- **Required**: Yes


# BatchDeleteDevicePositionHistoryRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteDevicePositionHistoryResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.BatchDeleteDevicePositionHistoryErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteGeofenceErrorTypeDef

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.BatchItemErrorTypeDef'>
- **Required**: Yes


# BatchDeleteGeofenceRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### GeofenceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteGeofenceResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.BatchDeleteGeofenceErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchEvaluateGeofencesErrorTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.BatchItemErrorTypeDef'>
- **Required**: Yes


# BatchEvaluateGeofencesRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DevicePositionUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.location_classes.DevicePositionUpdateTypeDef]
- **Required**: Yes


# BatchEvaluateGeofencesResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.BatchEvaluateGeofencesErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetDevicePositionErrorTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.BatchItemErrorTypeDef'>
- **Required**: Yes


# BatchGetDevicePositionRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDevicePositionResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.BatchGetDevicePositionErrorTypeDef]
- **Required**: Yes

### DevicePositions
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.DevicePositionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchItemErrorTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['AccessDeniedError', 'ConflictError', 'InternalServerError', 'ResourceNotFoundError', 'ThrottlingError', 'ValidationError']]

### Message
- **Type**: typing.Optional[str]


# BatchPutGeofenceErrorTypeDef

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.BatchItemErrorTypeDef'>
- **Required**: Yes


# BatchPutGeofenceRequestEntryTypeDef

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.GeofenceGeometryTypeDef'>
- **Required**: Yes

### GeofenceProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# BatchPutGeofenceRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.location_classes.BatchPutGeofenceRequestEntryTypeDef]
- **Required**: Yes


# BatchPutGeofenceResponseTypeDef

### Successes
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.BatchPutGeofenceSuccessTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.BatchPutGeofenceErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutGeofenceSuccessTypeDef

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchUpdateDevicePositionErrorTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.BatchItemErrorTypeDef'>
- **Required**: Yes


# BatchUpdateDevicePositionRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.location_classes.DevicePositionUpdateTypeDef]
- **Required**: Yes


# BatchUpdateDevicePositionResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.BatchUpdateDevicePositionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CalculateRouteCarModeOptionsTypeDef

### AvoidFerries
- **Type**: typing.Optional[bool]

### AvoidTolls
- **Type**: typing.Optional[bool]


# CalculateRouteMatrixRequestRequestTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### DeparturePositions
- **Type**: typing.Sequence[typing.Sequence[float]]
- **Required**: Yes

### DestinationPositions
- **Type**: typing.Sequence[typing.Sequence[float]]
- **Required**: Yes

### TravelMode
- **Type**: typing.Optional[typing.Literal['Bicycle', 'Car', 'Motorcycle', 'Truck', 'Walking']]

### DepartureTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DepartNow
- **Type**: typing.Optional[bool]

### DistanceUnit
- **Type**: typing.Optional[typing.Literal['Kilometers', 'Miles']]

### CarModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.CalculateRouteCarModeOptionsTypeDef]

### TruckModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.CalculateRouteTruckModeOptionsTypeDef]

### Key
- **Type**: typing.Optional[str]


# CalculateRouteMatrixResponseTypeDef

### RouteMatrix
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.location_classes.RouteMatrixEntryTypeDef]]
- **Required**: Yes

### SnappedDeparturePositions
- **Type**: typing.List[typing.List[float]]
- **Required**: Yes

### SnappedDestinationPositions
- **Type**: typing.List[typing.List[float]]
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.CalculateRouteMatrixSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CalculateRouteMatrixSummaryTypeDef

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### RouteCount
- **Type**: <class 'int'>
- **Required**: Yes

### ErrorCount
- **Type**: <class 'int'>
- **Required**: Yes

### DistanceUnit
- **Type**: typing.Literal['Kilometers', 'Miles']
- **Required**: Yes


# CalculateRouteRequestRequestTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### DeparturePosition
- **Type**: typing.Sequence[float]
- **Required**: Yes

### DestinationPosition
- **Type**: typing.Sequence[float]
- **Required**: Yes

### WaypointPositions
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[float]]]

### TravelMode
- **Type**: typing.Optional[typing.Literal['Bicycle', 'Car', 'Motorcycle', 'Truck', 'Walking']]

### DepartureTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DepartNow
- **Type**: typing.Optional[bool]

### DistanceUnit
- **Type**: typing.Optional[typing.Literal['Kilometers', 'Miles']]

### IncludeLegGeometry
- **Type**: typing.Optional[bool]

### CarModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.CalculateRouteCarModeOptionsTypeDef]

### TruckModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.CalculateRouteTruckModeOptionsTypeDef]

### ArrivalTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### OptimizeFor
- **Type**: typing.Optional[typing.Literal['FastestRoute', 'ShortestRoute']]

### Key
- **Type**: typing.Optional[str]


# CalculateRouteResponseTypeDef

### Legs
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.LegTypeDef]
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.CalculateRouteSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CalculateRouteSummaryTypeDef

### RouteBBox
- **Type**: typing.List[float]
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### Distance
- **Type**: <class 'float'>
- **Required**: Yes

### DurationSeconds
- **Type**: <class 'float'>
- **Required**: Yes

### DistanceUnit
- **Type**: typing.Literal['Kilometers', 'Miles']
- **Required**: Yes


# CalculateRouteTruckModeOptionsTypeDef

### AvoidFerries
- **Type**: typing.Optional[bool]

### AvoidTolls
- **Type**: typing.Optional[bool]

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.TruckDimensionsTypeDef]

### Weight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.TruckWeightTypeDef]


# CellSignalsTypeDef

### LteCellDetails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.location_classes.LteCellDetailsTypeDef]
- **Required**: Yes


# CircleExtraOutputTypeDef

### Center
- **Type**: typing.List[float]
- **Required**: Yes

### Radius
- **Type**: <class 'float'>
- **Required**: Yes


# CircleOutputTypeDef

### Center
- **Type**: typing.List[float]
- **Required**: Yes

### Radius
- **Type**: <class 'float'>
- **Required**: Yes


# CircleTypeDef

### Center
- **Type**: typing.Sequence[float]
- **Required**: Yes

### Radius
- **Type**: <class 'float'>
- **Required**: Yes


# CreateGeofenceCollectionRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### PricingPlanDataSource
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KmsKeyId
- **Type**: typing.Optional[str]


# CreateGeofenceCollectionResponseTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### CollectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKeyRequestRequestTypeDef

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Restrictions
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ApiKeyRestrictionsTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ExpireTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NoExpiry
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKeyResponseTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMapRequestRequestTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.MapConfigurationTypeDef'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMapResponseTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### MapArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePlaceIndexRequestRequestTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]

### DataSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.DataSourceConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePlaceIndexResponseTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRouteCalculatorRequestRequestTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRouteCalculatorResponseTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrackerRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### KmsKeyId
- **Type**: typing.Optional[str]

### PricingPlanDataSource
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PositionFiltering
- **Type**: typing.Optional[typing.Literal['AccuracyBased', 'DistanceBased', 'TimeBased']]

### EventBridgeEnabled
- **Type**: typing.Optional[bool]

### KmsKeyEnableGeospatialQueries
- **Type**: typing.Optional[bool]


# CreateTrackerResponseTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackerArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSourceConfigurationTypeDef

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse', 'Storage']]


# DeleteGeofenceCollectionRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyRequestRequestTypeDef

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DeleteMapRequestRequestTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaceIndexRequestRequestTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteCalculatorRequestRequestTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrackerRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGeofenceCollectionRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGeofenceCollectionResponseTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### CollectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']
- **Required**: Yes

### PricingPlanDataSource
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GeofenceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeKeyRequestRequestTypeDef

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeKeyResponseTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Restrictions
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ApiKeyRestrictionsOutputTypeDef'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExpireTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMapRequestRequestTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMapResponseTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### MapArn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.MapConfigurationOutputTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePlaceIndexRequestRequestTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePlaceIndexResponseTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexArn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.DataSourceConfigurationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRouteCalculatorRequestRequestTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRouteCalculatorResponseTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrackerRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrackerResponseTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']
- **Required**: Yes

### PricingPlanDataSource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### PositionFiltering
- **Type**: typing.Literal['AccuracyBased', 'DistanceBased', 'TimeBased']
- **Required**: Yes

### EventBridgeEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### KmsKeyEnableGeospatialQueries
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DevicePositionTypeDef

### SampleTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReceivedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### DeviceId
- **Type**: typing.Optional[str]

### Accuracy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PositionalAccuracyTypeDef]

### PositionProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# DevicePositionUpdateTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Position
- **Type**: typing.Sequence[float]
- **Required**: Yes

### Accuracy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PositionalAccuracyTypeDef]

### PositionProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeviceStateTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Position
- **Type**: typing.Sequence[float]
- **Required**: Yes

### Accuracy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PositionalAccuracyTypeDef]

### Ipv4Address
- **Type**: typing.Optional[str]

### WiFiAccessPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.location_classes.WiFiAccessPointTypeDef]]

### CellSignals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.CellSignalsTypeDef]


# DisassociateTrackerConsumerRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerArn
- **Type**: <class 'str'>
- **Required**: Yes


# ForecastGeofenceEventsDeviceStateTypeDef

### Position
- **Type**: typing.Sequence[float]
- **Required**: Yes

### Speed
- **Type**: typing.Optional[float]


# ForecastGeofenceEventsRequestForecastGeofenceEventsPaginateTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceState
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ForecastGeofenceEventsDeviceStateTypeDef'>
- **Required**: Yes

### TimeHorizonMinutes
- **Type**: typing.Optional[float]

### DistanceUnit
- **Type**: typing.Optional[typing.Literal['Kilometers', 'Miles']]

### SpeedUnit
- **Type**: typing.Optional[typing.Literal['KilometersPerHour', 'MilesPerHour']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ForecastGeofenceEventsRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceState
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ForecastGeofenceEventsDeviceStateTypeDef'>
- **Required**: Yes

### TimeHorizonMinutes
- **Type**: typing.Optional[float]

### DistanceUnit
- **Type**: typing.Optional[typing.Literal['Kilometers', 'Miles']]

### SpeedUnit
- **Type**: typing.Optional[typing.Literal['KilometersPerHour', 'MilesPerHour']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ForecastGeofenceEventsResponseTypeDef

### ForecastedEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ForecastedEventTypeDef]
- **Required**: Yes

### DistanceUnit
- **Type**: typing.Literal['Kilometers', 'Miles']
- **Required**: Yes

### SpeedUnit
- **Type**: typing.Literal['KilometersPerHour', 'MilesPerHour']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ForecastedEventTypeDef

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### IsDeviceInGeofence
- **Type**: <class 'bool'>
- **Required**: Yes

### NearestDistance
- **Type**: <class 'float'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['ENTER', 'EXIT', 'IDLE']
- **Required**: Yes

### ForecastedBreachTime
- **Type**: typing.Optional[datetime.datetime]

### GeofenceProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# GeofenceGeometryExtraOutputTypeDef

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]

### Circle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.CircleExtraOutputTypeDef]

### Geobuf
- **Type**: typing.Optional[bytes]


# GeofenceGeometryOutputTypeDef

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]

### Circle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.CircleOutputTypeDef]

### Geobuf
- **Type**: typing.Optional[bytes]


# GeofenceGeometryTypeDef

### Polygon
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[typing.Sequence[float]]]]

### Circle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.CircleTypeDef]

### Geobuf
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTimeInclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTimeExclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# GetDevicePositionHistoryRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### StartTimeInclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTimeExclusive
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]


# GetDevicePositionHistoryResponseTypeDef

### DevicePositions
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.DevicePositionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDevicePositionRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevicePositionResponseTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReceivedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Accuracy
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.PositionalAccuracyTypeDef'>
- **Required**: Yes

### PositionProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGeofenceRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGeofenceResponseTypeDef

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.GeofenceGeometryOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GeofenceProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMapGlyphsRequestRequestTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### FontStack
- **Type**: <class 'str'>
- **Required**: Yes

### FontUnicodeRange
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# GetMapGlyphsResponseTypeDef

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMapSpritesRequestRequestTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# GetMapSpritesResponseTypeDef

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMapStyleDescriptorRequestRequestTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# GetMapStyleDescriptorResponseTypeDef

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMapTileRequestRequestTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### Z
- **Type**: <class 'str'>
- **Required**: Yes

### X
- **Type**: <class 'str'>
- **Required**: Yes

### Y
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# GetMapTileResponseTypeDef

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPlaceRequestRequestTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceId
- **Type**: <class 'str'>
- **Required**: Yes

### Language
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# GetPlaceResponseTypeDef

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.PlaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InferredStateTypeDef

### ProxyDetected
- **Type**: <class 'bool'>
- **Required**: Yes

### Position
- **Type**: typing.Optional[typing.List[float]]

### Accuracy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PositionalAccuracyTypeDef]

### DeviationDistance
- **Type**: typing.Optional[float]


# LegGeometryTypeDef

### LineString
- **Type**: typing.Optional[typing.List[typing.List[float]]]


# LegTypeDef

### StartPosition
- **Type**: typing.List[float]
- **Required**: Yes

### EndPosition
- **Type**: typing.List[float]
- **Required**: Yes

### Distance
- **Type**: <class 'float'>
- **Required**: Yes

### DurationSeconds
- **Type**: <class 'float'>
- **Required**: Yes

### Steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.StepTypeDef]
- **Required**: Yes

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.LegGeometryTypeDef]


# ListDevicePositionsRequestListDevicePositionsPaginateTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### FilterGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.TrackingFilterGeometryTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListDevicePositionsRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### FilterGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.TrackingFilterGeometryTypeDef]


# ListDevicePositionsResponseEntryTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Accuracy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PositionalAccuracyTypeDef]

### PositionProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListDevicePositionsResponseTypeDef

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ListDevicePositionsResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListGeofenceCollectionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGeofenceCollectionsResponseEntryTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### PricingPlanDataSource
- **Type**: typing.Optional[str]


# ListGeofenceCollectionsResponseTypeDef

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ListGeofenceCollectionsResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGeofenceResponseEntryTypeDef

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.GeofenceGeometryOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GeofenceProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListGeofencesRequestListGeofencesPaginateTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListGeofencesRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGeofencesResponseTypeDef

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ListGeofenceResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKeysRequestListKeysPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.ApiKeyFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListKeysRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.ApiKeyFilterTypeDef]


# ListKeysResponseEntryTypeDef

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpireTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Restrictions
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ApiKeyRestrictionsOutputTypeDef'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ListKeysResponseTypeDef

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ListKeysResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMapsRequestListMapsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListMapsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMapsResponseEntryTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]


# ListMapsResponseTypeDef

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ListMapsResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListPlaceIndexesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlaceIndexesResponseEntryTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]


# ListPlaceIndexesResponseTypeDef

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ListPlaceIndexesResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListRouteCalculatorsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRouteCalculatorsResponseEntryTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]


# ListRouteCalculatorsResponseTypeDef

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ListRouteCalculatorsResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListTrackerConsumersRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrackerConsumersResponseTypeDef

### ConsumerArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrackersRequestListTrackersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.PaginatorConfigTypeDef]


# ListTrackersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrackersResponseEntryTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### PricingPlanDataSource
- **Type**: typing.Optional[str]


# ListTrackersResponseTypeDef

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.ListTrackersResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LteCellDetailsTypeDef

### CellId
- **Type**: <class 'int'>
- **Required**: Yes

### Mcc
- **Type**: <class 'int'>
- **Required**: Yes

### Mnc
- **Type**: <class 'int'>
- **Required**: Yes

### LocalId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.LteLocalIdTypeDef]

### NetworkMeasurements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.location_classes.LteNetworkMeasurementsTypeDef]]

### TimingAdvance
- **Type**: typing.Optional[int]

### NrCapable
- **Type**: typing.Optional[bool]

### Rsrp
- **Type**: typing.Optional[int]

### Rsrq
- **Type**: typing.Optional[float]

### Tac
- **Type**: typing.Optional[int]


# LteLocalIdTypeDef

### Earfcn
- **Type**: <class 'int'>
- **Required**: Yes

### Pci
- **Type**: <class 'int'>
- **Required**: Yes


# LteNetworkMeasurementsTypeDef

### Earfcn
- **Type**: <class 'int'>
- **Required**: Yes

### CellId
- **Type**: <class 'int'>
- **Required**: Yes

### Pci
- **Type**: <class 'int'>
- **Required**: Yes

### Rsrp
- **Type**: typing.Optional[int]

### Rsrq
- **Type**: typing.Optional[float]


# MapConfigurationOutputTypeDef

### Style
- **Type**: <class 'str'>
- **Required**: Yes

### PoliticalView
- **Type**: typing.Optional[str]

### CustomLayers
- **Type**: typing.Optional[typing.List[str]]


# MapConfigurationTypeDef

### Style
- **Type**: <class 'str'>
- **Required**: Yes

### PoliticalView
- **Type**: typing.Optional[str]

### CustomLayers
- **Type**: typing.Optional[typing.Sequence[str]]


# MapConfigurationUpdateTypeDef

### PoliticalView
- **Type**: typing.Optional[str]

### CustomLayers
- **Type**: typing.Optional[typing.Sequence[str]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlaceGeometryTypeDef

### Point
- **Type**: typing.Optional[typing.List[float]]


# PlaceTypeDef

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.PlaceGeometryTypeDef'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]

### AddressNumber
- **Type**: typing.Optional[str]

### Street
- **Type**: typing.Optional[str]

### Neighborhood
- **Type**: typing.Optional[str]

### Municipality
- **Type**: typing.Optional[str]

### SubRegion
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### PostalCode
- **Type**: typing.Optional[str]

### Interpolated
- **Type**: typing.Optional[bool]

### TimeZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.TimeZoneTypeDef]

### UnitType
- **Type**: typing.Optional[str]

### UnitNumber
- **Type**: typing.Optional[str]

### Categories
- **Type**: typing.Optional[typing.List[str]]

### SupplementalCategories
- **Type**: typing.Optional[typing.List[str]]

### SubMunicipality
- **Type**: typing.Optional[str]


# PositionalAccuracyTypeDef

### Horizontal
- **Type**: <class 'float'>
- **Required**: Yes


# PutGeofenceRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.GeofenceGeometryTypeDef'>
- **Required**: Yes

### GeofenceProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutGeofenceResponseTypeDef

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
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


# RouteMatrixEntryErrorTypeDef

### Code
- **Type**: typing.Literal['DeparturePositionNotFound', 'DestinationPositionNotFound', 'OtherValidationError', 'PositionsNotFound', 'RouteNotFound', 'RouteTooLong']
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]


# RouteMatrixEntryTypeDef

### Distance
- **Type**: typing.Optional[float]

### DurationSeconds
- **Type**: typing.Optional[float]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.RouteMatrixEntryErrorTypeDef]


# SearchForPositionResultTypeDef

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.PlaceTypeDef'>
- **Required**: Yes

### Distance
- **Type**: <class 'float'>
- **Required**: Yes

### PlaceId
- **Type**: typing.Optional[str]


# SearchForSuggestionsResultTypeDef

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceId
- **Type**: typing.Optional[str]

### Categories
- **Type**: typing.Optional[typing.List[str]]

### SupplementalCategories
- **Type**: typing.Optional[typing.List[str]]


# SearchForTextResultTypeDef

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.PlaceTypeDef'>
- **Required**: Yes

### Distance
- **Type**: typing.Optional[float]

### Relevance
- **Type**: typing.Optional[float]

### PlaceId
- **Type**: typing.Optional[str]


# SearchPlaceIndexForPositionRequestRequestTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Position
- **Type**: typing.Sequence[float]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### Language
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# SearchPlaceIndexForPositionResponseTypeDef

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.SearchPlaceIndexForPositionSummaryTypeDef'>
- **Required**: Yes

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.SearchForPositionResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchPlaceIndexForPositionSummaryTypeDef

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### Language
- **Type**: typing.Optional[str]


# SearchPlaceIndexForSuggestionsRequestRequestTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### BiasPosition
- **Type**: typing.Optional[typing.Sequence[float]]

### FilterBBox
- **Type**: typing.Optional[typing.Sequence[float]]

### FilterCountries
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### Language
- **Type**: typing.Optional[str]

### FilterCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Key
- **Type**: typing.Optional[str]


# SearchPlaceIndexForSuggestionsResponseTypeDef

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.SearchPlaceIndexForSuggestionsSummaryTypeDef'>
- **Required**: Yes

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.SearchForSuggestionsResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchPlaceIndexForSuggestionsSummaryTypeDef

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### BiasPosition
- **Type**: typing.Optional[typing.List[float]]

### FilterBBox
- **Type**: typing.Optional[typing.List[float]]

### FilterCountries
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### Language
- **Type**: typing.Optional[str]

### FilterCategories
- **Type**: typing.Optional[typing.List[str]]


# SearchPlaceIndexForTextRequestRequestTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### BiasPosition
- **Type**: typing.Optional[typing.Sequence[float]]

### FilterBBox
- **Type**: typing.Optional[typing.Sequence[float]]

### FilterCountries
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### Language
- **Type**: typing.Optional[str]

### FilterCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Key
- **Type**: typing.Optional[str]


# SearchPlaceIndexForTextResponseTypeDef

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.SearchPlaceIndexForTextSummaryTypeDef'>
- **Required**: Yes

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.location_classes.SearchForTextResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchPlaceIndexForTextSummaryTypeDef

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'str'>
- **Required**: Yes

### BiasPosition
- **Type**: typing.Optional[typing.List[float]]

### FilterBBox
- **Type**: typing.Optional[typing.List[float]]

### FilterCountries
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### ResultBBox
- **Type**: typing.Optional[typing.List[float]]

### Language
- **Type**: typing.Optional[str]

### FilterCategories
- **Type**: typing.Optional[typing.List[str]]


# StepTypeDef

### StartPosition
- **Type**: typing.List[float]
- **Required**: Yes

### EndPosition
- **Type**: typing.List[float]
- **Required**: Yes

### Distance
- **Type**: <class 'float'>
- **Required**: Yes

### DurationSeconds
- **Type**: <class 'float'>
- **Required**: Yes

### GeometryOffset
- **Type**: typing.Optional[int]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimeZoneTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Offset
- **Type**: typing.Optional[int]


# TrackingFilterGeometryTypeDef

### Polygon
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[typing.Sequence[float]]]]


# TruckDimensionsTypeDef

### Length
- **Type**: typing.Optional[float]

### Height
- **Type**: typing.Optional[float]

### Width
- **Type**: typing.Optional[float]

### Unit
- **Type**: typing.Optional[typing.Literal['Feet', 'Meters']]


# TruckWeightTypeDef

### Total
- **Type**: typing.Optional[float]

### Unit
- **Type**: typing.Optional[typing.Literal['Kilograms', 'Pounds']]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGeofenceCollectionRequestRequestTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### PricingPlanDataSource
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateGeofenceCollectionResponseTypeDef

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### CollectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKeyRequestRequestTypeDef

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ExpireTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NoExpiry
- **Type**: typing.Optional[bool]

### ForceUpdate
- **Type**: typing.Optional[bool]

### Restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.ApiKeyRestrictionsTypeDef]


# UpdateKeyResponseTypeDef

### KeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMapRequestRequestTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]

### ConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.MapConfigurationUpdateTypeDef]


# UpdateMapResponseTypeDef

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### MapArn
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePlaceIndexRequestRequestTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]

### DataSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location_classes.DataSourceConfigurationTypeDef]


# UpdatePlaceIndexResponseTypeDef

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexArn
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRouteCalculatorRequestRequestTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]


# UpdateRouteCalculatorResponseTypeDef

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrackerRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### PricingPlanDataSource
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PositionFiltering
- **Type**: typing.Optional[typing.Literal['AccuracyBased', 'DistanceBased', 'TimeBased']]

### EventBridgeEnabled
- **Type**: typing.Optional[bool]

### KmsKeyEnableGeospatialQueries
- **Type**: typing.Optional[bool]


# UpdateTrackerResponseTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### TrackerArn
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifyDevicePositionRequestRequestTypeDef

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceState
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.DeviceStateTypeDef'>
- **Required**: Yes

### DistanceUnit
- **Type**: typing.Optional[typing.Literal['Kilometers', 'Miles']]


# VerifyDevicePositionResponseTypeDef

### InferredState
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.InferredStateTypeDef'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReceivedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DistanceUnit
- **Type**: typing.Literal['Kilometers', 'Miles']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WiFiAccessPointTypeDef

### MacAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Rss
- **Type**: <class 'int'>
- **Required**: Yes


