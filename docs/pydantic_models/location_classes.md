# Location Classes

# ApiKeyFilter

### KeyStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Expired']]


# ApiKeyRestrictions

### AllowActions
- **Type**: typing.List[str]
- **Required**: Yes

### AllowResources
- **Type**: typing.List[str]
- **Required**: Yes

### AllowReferers
- **Type**: typing.Optional[typing.List[str]]


# ApiKeyRestrictionsOutput

### AllowActions
- **Type**: typing.List[str]
- **Required**: Yes

### AllowResources
- **Type**: typing.List[str]
- **Required**: Yes

### AllowReferers
- **Type**: typing.Optional[typing.List[str]]


# AssociateTrackerConsumerRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteDevicePositionHistoryError

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.BatchItemError'>
- **Required**: Yes


# BatchDeleteDevicePositionHistoryRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteDevicePositionHistoryResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.BatchDeleteDevicePositionHistoryError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteGeofenceError

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.BatchItemError'>
- **Required**: Yes


# BatchDeleteGeofenceRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### GeofenceIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteGeofenceResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.BatchDeleteGeofenceError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# BatchEvaluateGeofencesError

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.BatchItemError'>
- **Required**: Yes


# BatchEvaluateGeofencesRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DevicePositionUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.DevicePositionUpdate]
- **Required**: Yes


# BatchEvaluateGeofencesResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.BatchEvaluateGeofencesError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDevicePositionError

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.BatchItemError'>
- **Required**: Yes


# BatchGetDevicePositionRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetDevicePositionResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.BatchGetDevicePositionError]
- **Required**: Yes

### DevicePositions
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.DevicePosition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# BatchItemError

### Code
- **Type**: typing.Optional[typing.Literal['AccessDeniedError', 'ConflictError', 'InternalServerError', 'ResourceNotFoundError', 'ThrottlingError', 'ValidationError']]

### Message
- **Type**: typing.Optional[str]


# BatchPutGeofenceError

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.BatchItemError'>
- **Required**: Yes


# BatchPutGeofenceRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.BatchPutGeofenceRequestEntry]
- **Required**: Yes


# BatchPutGeofenceRequestEntry

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Geometry
- **Type**: typing.Union[aws_resource_validator.pydantic_models.location.location_classes.GeofenceGeometry, aws_resource_validator.pydantic_models.location.location_classes.GeofenceGeometryOutput]
- **Required**: Yes

### GeofenceProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# BatchPutGeofenceResponse

### Successes
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.BatchPutGeofenceSuccess]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.BatchPutGeofenceError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutGeofenceSuccess

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchUpdateDevicePositionError

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.BatchItemError'>
- **Required**: Yes


# BatchUpdateDevicePositionRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.DevicePositionUpdate]
- **Required**: Yes


# BatchUpdateDevicePositionResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.BatchUpdateDevicePositionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# CalculateRouteCarModeOptions

### AvoidFerries
- **Type**: typing.Optional[bool]

### AvoidTolls
- **Type**: typing.Optional[bool]


# CalculateRouteMatrixRequest

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### DeparturePositions
- **Type**: typing.List[typing.List[float]]
- **Required**: Yes

### DestinationPositions
- **Type**: typing.List[typing.List[float]]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.CalculateRouteCarModeOptions]

### TruckModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.CalculateRouteTruckModeOptions]

### Key
- **Type**: typing.Optional[str]


# CalculateRouteMatrixResponse

### RouteMatrix
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.location.location_classes.RouteMatrixEntry]]
- **Required**: Yes

### SnappedDeparturePositions
- **Type**: typing.List[typing.List[float]]
- **Required**: Yes

### SnappedDestinationPositions
- **Type**: typing.List[typing.List[float]]
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.CalculateRouteMatrixSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# CalculateRouteMatrixSummary

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


# CalculateRouteRequest

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### DeparturePosition
- **Type**: typing.List[float]
- **Required**: Yes

### DestinationPosition
- **Type**: typing.List[float]
- **Required**: Yes

### WaypointPositions
- **Type**: typing.Optional[typing.List[typing.List[float]]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.CalculateRouteCarModeOptions]

### TruckModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.CalculateRouteTruckModeOptions]

### ArrivalTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### OptimizeFor
- **Type**: typing.Optional[typing.Literal['FastestRoute', 'ShortestRoute']]

### Key
- **Type**: typing.Optional[str]


# CalculateRouteResponse

### Legs
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.Leg]
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.CalculateRouteSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# CalculateRouteSummary

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


# CalculateRouteTruckModeOptions

### AvoidFerries
- **Type**: typing.Optional[bool]

### AvoidTolls
- **Type**: typing.Optional[bool]

### Dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.TruckDimensions]

### Weight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.TruckWeight]


# CellSignals

### LteCellDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.LteCellDetails]
- **Required**: Yes


# Circle

### Center
- **Type**: typing.List[float]
- **Required**: Yes

### Radius
- **Type**: <class 'float'>
- **Required**: Yes


# CircleOutput

### Center
- **Type**: typing.List[float]
- **Required**: Yes

### Radius
- **Type**: <class 'float'>
- **Required**: Yes


# CreateGeofenceCollectionRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### KmsKeyId
- **Type**: typing.Optional[str]


# CreateGeofenceCollectionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKeyRequest

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Restrictions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.location.location_classes.ApiKeyRestrictions, aws_resource_validator.pydantic_models.location.location_classes.ApiKeyRestrictionsOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ExpireTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NoExpiry
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMapRequest

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.location.location_classes.MapConfiguration, aws_resource_validator.pydantic_models.location.location_classes.MapConfigurationOutput]
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMapResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePlaceIndexRequest

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
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePlaceIndexResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRouteCalculatorRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRouteCalculatorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrackerRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### PositionFiltering
- **Type**: typing.Optional[typing.Literal['AccuracyBased', 'DistanceBased', 'TimeBased']]

### EventBridgeEnabled
- **Type**: typing.Optional[bool]

### KmsKeyEnableGeospatialQueries
- **Type**: typing.Optional[bool]


# CreateTrackerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# DataSourceConfiguration

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse', 'Storage']]


# DeleteGeofenceCollectionRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyRequest

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DeleteMapRequest

### MapName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaceIndexRequest

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteCalculatorRequest

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrackerRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGeofenceCollectionRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGeofenceCollectionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeKeyRequest

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ApiKeyRestrictionsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMapRequest

### MapName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMapResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.MapConfigurationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePlaceIndexRequest

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePlaceIndexResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.DataSourceConfiguration'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRouteCalculatorRequest

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRouteCalculatorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrackerRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrackerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# DevicePosition

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PositionalAccuracy]

### PositionProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# DevicePositionUpdate

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Accuracy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PositionalAccuracy]

### PositionProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeviceState

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### SampleTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Accuracy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PositionalAccuracy]

### Ipv4Address
- **Type**: typing.Optional[str]

### WiFiAccessPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.location.location_classes.WiFiAccessPoint]]

### CellSignals
- **Type**: <class 'NoneType'>


# DisassociateTrackerConsumerRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerArn
- **Type**: <class 'str'>
- **Required**: Yes


# ForecastGeofenceEventsDeviceState

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Speed
- **Type**: typing.Optional[float]


# ForecastGeofenceEventsRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceState
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ForecastGeofenceEventsDeviceState'>
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


# ForecastGeofenceEventsRequestPaginate

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceState
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ForecastGeofenceEventsDeviceState'>
- **Required**: Yes

### TimeHorizonMinutes
- **Type**: typing.Optional[float]

### DistanceUnit
- **Type**: typing.Optional[typing.Literal['Kilometers', 'Miles']]

### SpeedUnit
- **Type**: typing.Optional[typing.Literal['KilometersPerHour', 'MilesPerHour']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ForecastGeofenceEventsResponse

### ForecastedEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ForecastedEvent]
- **Required**: Yes

### DistanceUnit
- **Type**: typing.Literal['Kilometers', 'Miles']
- **Required**: Yes

### SpeedUnit
- **Type**: typing.Literal['KilometersPerHour', 'MilesPerHour']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ForecastedEvent

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


# GeofenceGeometry

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]

### Circle
- **Type**: typing.Union[aws_resource_validator.pydantic_models.location.location_classes.Circle, aws_resource_validator.pydantic_models.location.location_classes.CircleOutput, NoneType]

### Geobuf
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# GeofenceGeometryOutput

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]

### Circle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.CircleOutput]

### Geobuf
- **Type**: typing.Optional[bytes]


# GetDevicePositionHistoryRequest

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


# GetDevicePositionHistoryRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# GetDevicePositionHistoryResponse

### DevicePositions
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.DevicePosition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDevicePositionRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevicePositionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.PositionalAccuracy'>
- **Required**: Yes

### PositionProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# GetGeofenceRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGeofenceResponse

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.GeofenceGeometryOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# GetMapGlyphsRequest

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


# GetMapGlyphsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# GetMapSpritesRequest

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# GetMapSpritesResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# GetMapStyleDescriptorRequest

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# GetMapStyleDescriptorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# GetMapTileRequest

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


# GetMapTileResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# GetPlaceRequest

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


# GetPlaceResponse

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.Place'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# InferredState

### ProxyDetected
- **Type**: <class 'bool'>
- **Required**: Yes

### Position
- **Type**: typing.Optional[typing.List[float]]

### Accuracy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PositionalAccuracy]

### DeviationDistance
- **Type**: typing.Optional[float]


# Leg

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.Step]
- **Required**: Yes

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.LegGeometry]


# LegGeometry

### LineString
- **Type**: typing.Optional[typing.List[typing.List[float]]]


# ListDevicePositionsRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### FilterGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.TrackingFilterGeometry]


# ListDevicePositionsRequestPaginate

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### FilterGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.TrackingFilterGeometry]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListDevicePositionsResponse

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ListDevicePositionsResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicePositionsResponseEntry

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PositionalAccuracy]

### PositionProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListGeofenceCollectionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGeofenceCollectionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListGeofenceCollectionsResponse

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ListGeofenceCollectionsResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGeofenceCollectionsResponseEntry

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


# ListGeofenceResponseEntry

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.GeofenceGeometryOutput'>
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


# ListGeofencesRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGeofencesRequestPaginate

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListGeofencesResponse

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ListGeofenceResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKeysRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.ApiKeyFilter]


# ListKeysRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.ApiKeyFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListKeysResponse

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ListKeysResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKeysResponseEntry

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpireTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Restrictions
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ApiKeyRestrictionsOutput'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ListMapsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMapsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListMapsResponse

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ListMapsResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMapsResponseEntry

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


# ListPlaceIndexesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlaceIndexesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListPlaceIndexesResponse

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ListPlaceIndexesResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPlaceIndexesResponseEntry

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


# ListRouteCalculatorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRouteCalculatorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListRouteCalculatorsResponse

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ListRouteCalculatorsResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRouteCalculatorsResponseEntry

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


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrackerConsumersRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrackerConsumersRequestPaginate

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListTrackerConsumersResponse

### ConsumerArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrackersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrackersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.PaginatorConfig]


# ListTrackersResponse

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.ListTrackersResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrackersResponseEntry

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


# LteCellDetails

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.LteLocalId]

### NetworkMeasurements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.location.location_classes.LteNetworkMeasurements]]

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


# LteLocalId

### Earfcn
- **Type**: <class 'int'>
- **Required**: Yes

### Pci
- **Type**: <class 'int'>
- **Required**: Yes


# LteNetworkMeasurements

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


# MapConfiguration

### Style
- **Type**: <class 'str'>
- **Required**: Yes

### PoliticalView
- **Type**: typing.Optional[str]

### CustomLayers
- **Type**: typing.Optional[typing.List[str]]


# MapConfigurationOutput

### Style
- **Type**: <class 'str'>
- **Required**: Yes

### PoliticalView
- **Type**: typing.Optional[str]

### CustomLayers
- **Type**: typing.Optional[typing.List[str]]


# MapConfigurationUpdate

### PoliticalView
- **Type**: typing.Optional[str]

### CustomLayers
- **Type**: typing.Optional[typing.List[str]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Place

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.PlaceGeometry'>
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
- **Type**: <class 'NoneType'>

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


# PlaceGeometry

### Point
- **Type**: typing.Optional[typing.List[float]]


# PositionalAccuracy

### Horizontal
- **Type**: <class 'float'>
- **Required**: Yes


# PutGeofenceRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### GeofenceId
- **Type**: <class 'str'>
- **Required**: Yes

### Geometry
- **Type**: typing.Union[aws_resource_validator.pydantic_models.location.location_classes.GeofenceGeometry, aws_resource_validator.pydantic_models.location.location_classes.GeofenceGeometryOutput]
- **Required**: Yes

### GeofenceProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutGeofenceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
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


# RouteMatrixEntry

### Distance
- **Type**: typing.Optional[float]

### DurationSeconds
- **Type**: typing.Optional[float]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.RouteMatrixEntryError]


# RouteMatrixEntryError

### Code
- **Type**: typing.Literal['DeparturePositionNotFound', 'DestinationPositionNotFound', 'OtherValidationError', 'PositionsNotFound', 'RouteNotFound', 'RouteTooLong']
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]


# SearchForPositionResult

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.Place'>
- **Required**: Yes

### Distance
- **Type**: <class 'float'>
- **Required**: Yes

### PlaceId
- **Type**: typing.Optional[str]


# SearchForSuggestionsResult

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceId
- **Type**: typing.Optional[str]

### Categories
- **Type**: typing.Optional[typing.List[str]]

### SupplementalCategories
- **Type**: typing.Optional[typing.List[str]]


# SearchForTextResult

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.Place'>
- **Required**: Yes

### Distance
- **Type**: typing.Optional[float]

### Relevance
- **Type**: typing.Optional[float]

### PlaceId
- **Type**: typing.Optional[str]


# SearchPlaceIndexForPositionRequest

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### Language
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# SearchPlaceIndexForPositionResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.SearchPlaceIndexForPositionSummary'>
- **Required**: Yes

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.SearchForPositionResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# SearchPlaceIndexForPositionSummary

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


# SearchPlaceIndexForSuggestionsRequest

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Text
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

### Key
- **Type**: typing.Optional[str]


# SearchPlaceIndexForSuggestionsResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.SearchPlaceIndexForSuggestionsSummary'>
- **Required**: Yes

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.SearchForSuggestionsResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# SearchPlaceIndexForSuggestionsSummary

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


# SearchPlaceIndexForTextRequest

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### Text
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

### Key
- **Type**: typing.Optional[str]


# SearchPlaceIndexForTextResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.SearchPlaceIndexForTextSummary'>
- **Required**: Yes

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.location.location_classes.SearchForTextResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# SearchPlaceIndexForTextSummary

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


# Step

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


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TimeZone

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Offset
- **Type**: typing.Optional[int]


# TrackingFilterGeometry

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]


# TruckDimensions

### Length
- **Type**: typing.Optional[float]

### Height
- **Type**: typing.Optional[float]

### Width
- **Type**: typing.Optional[float]

### Unit
- **Type**: typing.Optional[typing.Literal['Feet', 'Meters']]


# TruckWeight

### Total
- **Type**: typing.Optional[float]

### Unit
- **Type**: typing.Optional[typing.Literal['Kilograms', 'Pounds']]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateGeofenceCollectionRequest

### CollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### PricingPlanDataSource
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateGeofenceCollectionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKeyRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.location.location_classes.ApiKeyRestrictions, aws_resource_validator.pydantic_models.location.location_classes.ApiKeyRestrictionsOutput, NoneType]


# UpdateKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMapRequest

### MapName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]

### ConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.location.location_classes.MapConfigurationUpdate]


# UpdateMapResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePlaceIndexRequest

### IndexName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]

### DataSourceConfiguration
- **Type**: <class 'NoneType'>


# UpdatePlaceIndexResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRouteCalculatorRequest

### CalculatorName
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlan
- **Type**: typing.Optional[typing.Literal['MobileAssetManagement', 'MobileAssetTracking', 'RequestBasedUsage']]

### Description
- **Type**: typing.Optional[str]


# UpdateRouteCalculatorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrackerRequest

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


# UpdateTrackerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# VerifyDevicePositionRequest

### TrackerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceState
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.DeviceState'>
- **Required**: Yes

### DistanceUnit
- **Type**: typing.Optional[typing.Literal['Kilometers', 'Miles']]


# VerifyDevicePositionResponse

### InferredState
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.InferredState'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.location.location_classes.ResponseMetadata'>
- **Required**: Yes


# WiFiAccessPoint

### MacAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Rss
- **Type**: <class 'int'>
- **Required**: Yes


