# Geo Routes Geo Routes Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CalculateIsolinesRequest

### Thresholds
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineThresholds'>
- **Required**: Yes

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineAllowOptions]

### ArrivalTime
- **Type**: typing.Optional[str]

### Avoid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineAvoidanceOptions]

### DepartNow
- **Type**: typing.Optional[bool]

### DepartureTime
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[typing.List[float]]

### DestinationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineDestinationOptions]

### IsolineGeometryFormat
- **Type**: typing.Optional[typing.Literal['FlexiblePolyline', 'Simple']]

### IsolineGranularity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineGranularityOptions]

### Key
- **Type**: typing.Optional[str]

### OptimizeIsolineFor
- **Type**: typing.Optional[typing.Literal['AccurateCalculation', 'BalancedCalculation', 'FastCalculation']]

### OptimizeRoutingFor
- **Type**: typing.Optional[typing.Literal['FastestRoute', 'ShortestRoute']]

### Origin
- **Type**: typing.Optional[typing.List[float]]

### OriginOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineOriginOptions]

### Traffic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineTrafficOptions]

### TravelMode
- **Type**: typing.Optional[typing.Literal['Car', 'Pedestrian', 'Scooter', 'Truck']]

### TravelModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineTravelModeOptions]


# CalculateIsolinesResponse

### ArrivalTime
- **Type**: <class 'str'>
- **Required**: Yes

### DepartureTime
- **Type**: <class 'str'>
- **Required**: Yes

### IsolineGeometryFormat
- **Type**: typing.Literal['FlexiblePolyline', 'Simple']
- **Required**: Yes

### Isolines
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.Isoline]
- **Required**: Yes

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### SnappedDestination
- **Type**: typing.List[float]
- **Required**: Yes

### SnappedOrigin
- **Type**: typing.List[float]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.ResponseMetadata'>
- **Required**: Yes


# CalculateRouteMatrixRequest

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixDestination]
- **Required**: Yes

### Origins
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixOrigin]
- **Required**: Yes

### RoutingBoundary
- **Type**: typing.Union[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixBoundary, aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixBoundaryOutput]
- **Required**: Yes

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixAllowOptions]

### Avoid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixAvoidanceOptions]

### DepartNow
- **Type**: typing.Optional[bool]

### DepartureTime
- **Type**: typing.Optional[str]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixExclusionOptions]

### Key
- **Type**: typing.Optional[str]

### OptimizeRoutingFor
- **Type**: typing.Optional[typing.Literal['FastestRoute', 'ShortestRoute']]

### Traffic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixTrafficOptions]

### TravelMode
- **Type**: typing.Optional[typing.Literal['Car', 'Pedestrian', 'Scooter', 'Truck']]

### TravelModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixTravelModeOptions]


# CalculateRouteMatrixResponse

### ErrorCount
- **Type**: <class 'int'>
- **Required**: Yes

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### RouteMatrix
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixEntry]]
- **Required**: Yes

### RoutingBoundary
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixBoundaryOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.ResponseMetadata'>
- **Required**: Yes


# CalculateRoutesRequest

### Destination
- **Type**: typing.List[float]
- **Required**: Yes

### Origin
- **Type**: typing.List[float]
- **Required**: Yes

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteAllowOptions]

### ArrivalTime
- **Type**: typing.Optional[str]

### Avoid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteAvoidanceOptions]

### DepartNow
- **Type**: typing.Optional[bool]

### DepartureTime
- **Type**: typing.Optional[str]

### DestinationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteDestinationOptions]

### Driver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteDriverOptions]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteExclusionOptions]

### InstructionsMeasurementSystem
- **Type**: typing.Optional[typing.Literal['Imperial', 'Metric']]

### Key
- **Type**: typing.Optional[str]

### Languages
- **Type**: typing.Optional[typing.List[str]]

### LegAdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['Elevation', 'Incidents', 'PassThroughWaypoints', 'Summary', 'Tolls', 'TravelStepInstructions', 'TruckRoadTypes', 'TypicalDuration', 'Zones']]]

### LegGeometryFormat
- **Type**: typing.Optional[typing.Literal['FlexiblePolyline', 'Simple']]

### MaxAlternatives
- **Type**: typing.Optional[int]

### OptimizeRoutingFor
- **Type**: typing.Optional[typing.Literal['FastestRoute', 'ShortestRoute']]

### OriginOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteOriginOptions]

### SpanAdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['BestCaseDuration', 'CarAccess', 'Consumption', 'Country', 'Distance', 'Duration', 'DynamicSpeed', 'FunctionalClassification', 'Gates', 'Incidents', 'Names', 'Notices', 'PedestrianAccess', 'RailwayCrossings', 'Region', 'RoadAttributes', 'RouteNumbers', 'ScooterAccess', 'SpeedLimit', 'TollSystems', 'TruckAccess', 'TruckRoadTypes', 'TypicalDuration', 'Zones']]]

### Tolls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollOptions]

### Traffic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTrafficOptions]

### TravelMode
- **Type**: typing.Optional[typing.Literal['Car', 'Pedestrian', 'Scooter', 'Truck']]

### TravelModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTravelModeOptions]

### TravelStepType
- **Type**: typing.Optional[typing.Literal['Default', 'TurnByTurn']]

### Waypoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteWaypoint]]


# CalculateRoutesResponse

### LegGeometryFormat
- **Type**: typing.Literal['FlexiblePolyline', 'Simple']
- **Required**: Yes

### Notices
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteResponseNotice]
- **Required**: Yes

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.Route]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.ResponseMetadata'>
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


# Corridor

### LineString
- **Type**: typing.List[typing.List[float]]
- **Required**: Yes

### Radius
- **Type**: <class 'int'>
- **Required**: Yes


# Isoline

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineConnection]
- **Required**: Yes

### Geometries
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineShapeGeometry]
- **Required**: Yes

### DistanceThreshold
- **Type**: typing.Optional[int]

### TimeThreshold
- **Type**: typing.Optional[int]


# IsolineAllowOptions

### Hot
- **Type**: typing.Optional[bool]

### Hov
- **Type**: typing.Optional[bool]


# IsolineAvoidanceArea

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineAvoidanceAreaGeometry'>
- **Required**: Yes

### Except
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineAvoidanceAreaGeometry]]


# IsolineAvoidanceAreaGeometry

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### Corridor
- **Type**: <class 'NoneType'>

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]

### PolylineCorridor
- **Type**: <class 'NoneType'>

### PolylinePolygon
- **Type**: typing.Optional[typing.List[str]]


# IsolineAvoidanceOptions

### Areas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineAvoidanceArea]]

### CarShuttleTrains
- **Type**: typing.Optional[bool]

### ControlledAccessHighways
- **Type**: typing.Optional[bool]

### DirtRoads
- **Type**: typing.Optional[bool]

### Ferries
- **Type**: typing.Optional[bool]

### SeasonalClosure
- **Type**: typing.Optional[bool]

### TollRoads
- **Type**: typing.Optional[bool]

### TollTransponders
- **Type**: typing.Optional[bool]

### TruckRoadTypes
- **Type**: typing.Optional[typing.List[str]]

### Tunnels
- **Type**: typing.Optional[bool]

### UTurns
- **Type**: typing.Optional[bool]

### ZoneCategories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineAvoidanceZoneCategory]]


# IsolineAvoidanceZoneCategory

### Category
- **Type**: typing.Optional[typing.Literal['CongestionPricing', 'Environmental', 'Vignette']]


# IsolineCarOptions

### EngineType
- **Type**: typing.Optional[typing.Literal['Electric', 'InternalCombustion', 'PluginHybrid']]

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]


# IsolineConnection

### FromPolygonIndex
- **Type**: <class 'int'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineConnectionGeometry'>
- **Required**: Yes

### ToPolygonIndex
- **Type**: <class 'int'>
- **Required**: Yes


# IsolineConnectionGeometry

### LineString
- **Type**: typing.Optional[typing.List[typing.List[float]]]

### Polyline
- **Type**: typing.Optional[str]


# IsolineDestinationOptions

### AvoidActionsForDistance
- **Type**: typing.Optional[int]

### Heading
- **Type**: typing.Optional[float]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineMatchingOptions]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineSideOfStreetOptions]


# IsolineGranularityOptions

### MaxPoints
- **Type**: typing.Optional[int]

### MaxResolution
- **Type**: typing.Optional[int]


# IsolineMatchingOptions

### NameHint
- **Type**: typing.Optional[str]

### OnRoadThreshold
- **Type**: typing.Optional[int]

### Radius
- **Type**: typing.Optional[int]

### Strategy
- **Type**: typing.Optional[typing.Literal['MatchAny', 'MatchMostSignificantRoad']]


# IsolineOriginOptions

### AvoidActionsForDistance
- **Type**: typing.Optional[int]

### Heading
- **Type**: typing.Optional[float]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineMatchingOptions]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineSideOfStreetOptions]


# IsolineScooterOptions

### EngineType
- **Type**: typing.Optional[typing.Literal['Electric', 'InternalCombustion', 'PluginHybrid']]

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]


# IsolineShapeGeometry

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]

### PolylinePolygon
- **Type**: typing.Optional[typing.List[str]]


# IsolineSideOfStreetOptions

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### UseWith
- **Type**: typing.Optional[typing.Literal['AnyStreet', 'DividedStreetOnly']]


# IsolineThresholds

### Distance
- **Type**: typing.Optional[typing.List[int]]

### Time
- **Type**: typing.Optional[typing.List[int]]


# IsolineTrafficOptions

### FlowEventThresholdOverride
- **Type**: typing.Optional[int]

### Usage
- **Type**: typing.Optional[typing.Literal['IgnoreTrafficData', 'UseTrafficData']]


# IsolineTrailerOptions

### AxleCount
- **Type**: typing.Optional[int]

### TrailerCount
- **Type**: typing.Optional[int]


# IsolineTravelModeOptions

### Car
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineCarOptions]

### Scooter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineScooterOptions]

### Truck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineTruckOptions]


# IsolineTruckOptions

### AxleCount
- **Type**: typing.Optional[int]

### EngineType
- **Type**: typing.Optional[typing.Literal['Electric', 'InternalCombustion', 'PluginHybrid']]

### GrossWeight
- **Type**: typing.Optional[int]

### HazardousCargos
- **Type**: typing.Optional[typing.List[typing.Literal['Combustible', 'Corrosive', 'Explosive', 'Flammable', 'Gas', 'HarmfulToWater', 'Organic', 'Other', 'Poison', 'PoisonousInhalation', 'Radioactive']]]

### Height
- **Type**: typing.Optional[int]

### HeightAboveFirstAxle
- **Type**: typing.Optional[int]

### KpraLength
- **Type**: typing.Optional[int]

### Length
- **Type**: typing.Optional[int]

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]

### PayloadCapacity
- **Type**: typing.Optional[int]

### TireCount
- **Type**: typing.Optional[int]

### Trailer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.IsolineTrailerOptions]

### TruckType
- **Type**: typing.Optional[typing.Literal['LightTruck', 'StraightTruck', 'Tractor']]

### TunnelRestrictionCode
- **Type**: typing.Optional[str]

### WeightPerAxle
- **Type**: typing.Optional[int]

### WeightPerAxleGroup
- **Type**: <class 'NoneType'>

### Width
- **Type**: typing.Optional[int]


# IsolineVehicleLicensePlate

### LastCharacter
- **Type**: typing.Optional[str]


# LocalizedString

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Language
- **Type**: typing.Optional[str]


# OptimizeWaypointsRequest

### Origin
- **Type**: typing.List[float]
- **Required**: Yes

### Avoid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationAvoidanceOptions]

### Clustering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationClusteringOptions]

### DepartureTime
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[typing.List[float]]

### DestinationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationDestinationOptions]

### Driver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationDriverOptions]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationExclusionOptions]

### Key
- **Type**: typing.Optional[str]

### OptimizeSequencingFor
- **Type**: typing.Optional[typing.Literal['FastestRoute', 'ShortestRoute']]

### OriginOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationOriginOptions]

### Traffic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationTrafficOptions]

### TravelMode
- **Type**: typing.Optional[typing.Literal['Car', 'Pedestrian', 'Scooter', 'Truck']]

### TravelModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationTravelModeOptions]

### Waypoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationWaypoint]]


# OptimizeWaypointsResponse

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationConnection]
- **Required**: Yes

### Distance
- **Type**: <class 'int'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### ImpedingWaypoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationImpedingWaypoint]
- **Required**: Yes

### OptimizedWaypoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationOptimizedWaypoint]
- **Required**: Yes

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### TimeBreakdown
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationTimeBreakdown'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.ResponseMetadata'>
- **Required**: Yes


# PolylineCorridor

### Polyline
- **Type**: <class 'str'>
- **Required**: Yes

### Radius
- **Type**: <class 'int'>
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


# RoadSnapNotice

### Code
- **Type**: typing.Literal['TracePointsHeadingIgnored', 'TracePointsIgnored', 'TracePointsMovedByLargeDistance', 'TracePointsNotMatched', 'TracePointsOutOfSequence', 'TracePointsSpeedEstimated', 'TracePointsSpeedIgnored']
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### TracePointIndexes
- **Type**: typing.List[int]
- **Required**: Yes


# RoadSnapSnappedGeometry

### LineString
- **Type**: typing.Optional[typing.List[typing.List[float]]]

### Polyline
- **Type**: typing.Optional[str]


# RoadSnapSnappedTracePoint

### Confidence
- **Type**: <class 'float'>
- **Required**: Yes

### OriginalPosition
- **Type**: typing.List[float]
- **Required**: Yes

### SnappedPosition
- **Type**: typing.List[float]
- **Required**: Yes


# RoadSnapTracePoint

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Heading
- **Type**: typing.Optional[float]

### Speed
- **Type**: typing.Optional[float]

### Timestamp
- **Type**: typing.Optional[str]


# RoadSnapTrailerOptions

### TrailerCount
- **Type**: typing.Optional[int]


# RoadSnapTravelModeOptions

### Truck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoadSnapTruckOptions]


# RoadSnapTruckOptions

### GrossWeight
- **Type**: typing.Optional[int]

### HazardousCargos
- **Type**: typing.Optional[typing.List[typing.Literal['Combustible', 'Corrosive', 'Explosive', 'Flammable', 'Gas', 'HarmfulToWater', 'Organic', 'Other', 'Poison', 'PoisonousInhalation', 'Radioactive']]]

### Height
- **Type**: typing.Optional[int]

### Length
- **Type**: typing.Optional[int]

### Trailer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoadSnapTrailerOptions]

### TunnelRestrictionCode
- **Type**: typing.Optional[str]

### Width
- **Type**: typing.Optional[int]


# Route

### Legs
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteLeg]
- **Required**: Yes

### MajorRoadLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMajorRoadLabel]
- **Required**: Yes

### Summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSummary]


# RouteAllowOptions

### Hot
- **Type**: typing.Optional[bool]

### Hov
- **Type**: typing.Optional[bool]


# RouteAvoidanceArea

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteAvoidanceAreaGeometry'>
- **Required**: Yes

### Except
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteAvoidanceAreaGeometry]]


# RouteAvoidanceAreaGeometry

### Corridor
- **Type**: <class 'NoneType'>

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]

### PolylineCorridor
- **Type**: <class 'NoneType'>

### PolylinePolygon
- **Type**: typing.Optional[typing.List[str]]


# RouteAvoidanceOptions

### Areas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteAvoidanceArea]]

### CarShuttleTrains
- **Type**: typing.Optional[bool]

### ControlledAccessHighways
- **Type**: typing.Optional[bool]

### DirtRoads
- **Type**: typing.Optional[bool]

### Ferries
- **Type**: typing.Optional[bool]

### SeasonalClosure
- **Type**: typing.Optional[bool]

### TollRoads
- **Type**: typing.Optional[bool]

### TollTransponders
- **Type**: typing.Optional[bool]

### TruckRoadTypes
- **Type**: typing.Optional[typing.List[str]]

### Tunnels
- **Type**: typing.Optional[bool]

### UTurns
- **Type**: typing.Optional[bool]

### ZoneCategories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteAvoidanceZoneCategory]]


# RouteAvoidanceZoneCategory

### Category
- **Type**: typing.Literal['CongestionPricing', 'Environmental', 'Vignette']
- **Required**: Yes


# RouteCarOptions

### EngineType
- **Type**: typing.Optional[typing.Literal['Electric', 'InternalCombustion', 'PluginHybrid']]

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]


# RouteContinueHighwayStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteContinueStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes


# RouteDestinationOptions

### AvoidActionsForDistance
- **Type**: typing.Optional[int]

### AvoidUTurns
- **Type**: typing.Optional[bool]

### Heading
- **Type**: typing.Optional[float]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatchingOptions]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSideOfStreetOptions]

### StopDuration
- **Type**: typing.Optional[int]


# RouteDriverOptions

### Schedule
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteDriverScheduleInterval]]


# RouteDriverScheduleInterval

### DriveDuration
- **Type**: <class 'int'>
- **Required**: Yes

### RestDuration
- **Type**: <class 'int'>
- **Required**: Yes


# RouteEmissionType

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Co2EmissionClass
- **Type**: typing.Optional[str]


# RouteEnterHighwayStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteExclusionOptions

### Countries
- **Type**: typing.List[str]
- **Required**: Yes


# RouteExitStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### RelativeExit
- **Type**: typing.Optional[int]

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteFerryAfterTravelStep

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Deboard']
- **Required**: Yes

### Instruction
- **Type**: typing.Optional[str]


# RouteFerryArrival

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryPlace'>
- **Required**: Yes

### Time
- **Type**: typing.Optional[str]


# RouteFerryBeforeTravelStep

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Board']
- **Required**: Yes

### Instruction
- **Type**: typing.Optional[str]


# RouteFerryDeparture

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryPlace'>
- **Required**: Yes

### Time
- **Type**: typing.Optional[str]


# RouteFerryLegDetails

### AfterTravelSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryAfterTravelStep]
- **Required**: Yes

### Arrival
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryArrival'>
- **Required**: Yes

### BeforeTravelSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryBeforeTravelStep]
- **Required**: Yes

### Departure
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryDeparture'>
- **Required**: Yes

### Notices
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryNotice]
- **Required**: Yes

### PassThroughWaypoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePassThroughWaypoint]
- **Required**: Yes

### Spans
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerrySpan]
- **Required**: Yes

### TravelSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryTravelStep]
- **Required**: Yes

### RouteName
- **Type**: typing.Optional[str]

### Summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerrySummary]


# RouteFerryNotice

### Code
- **Type**: typing.Literal['AccuratePolylineUnavailable', 'NoSchedule', 'Other', 'SeasonalClosure', 'ViolatedAvoidFerry', 'ViolatedAvoidRailFerry']
- **Required**: Yes

### Impact
- **Type**: typing.Optional[typing.Literal['High', 'Low']]


# RouteFerryOverviewSummary

### Distance
- **Type**: <class 'int'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# RouteFerryPlace

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### OriginalPosition
- **Type**: typing.Optional[typing.List[float]]

### WaypointIndex
- **Type**: typing.Optional[int]


# RouteFerrySpan

### Country
- **Type**: typing.Optional[str]

### Distance
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### GeometryOffset
- **Type**: typing.Optional[int]

### Names
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]]

### Region
- **Type**: typing.Optional[str]


# RouteFerrySummary

### Overview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryOverviewSummary]

### TravelOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryTravelOnlySummary]


# RouteFerryTravelOnlySummary

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# RouteFerryTravelStep

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Arrive', 'Continue', 'Depart']
- **Required**: Yes

### Distance
- **Type**: typing.Optional[int]

### GeometryOffset
- **Type**: typing.Optional[int]

### Instruction
- **Type**: typing.Optional[str]


# RouteKeepStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteLeg

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteLegGeometry'>
- **Required**: Yes

### TravelMode
- **Type**: typing.Literal['Car', 'CarShuttleTrain', 'Ferry', 'Pedestrian', 'Scooter', 'Truck']
- **Required**: Yes

### Type
- **Type**: typing.Literal['Ferry', 'Pedestrian', 'Vehicle']
- **Required**: Yes

### FerryLegDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteFerryLegDetails]

### Language
- **Type**: typing.Optional[str]

### PedestrianLegDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianLegDetails]

### VehicleLegDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleLegDetails]


# RouteLegGeometry

### LineString
- **Type**: typing.Optional[typing.List[typing.List[float]]]

### Polyline
- **Type**: typing.Optional[str]


# RouteMajorRoadLabel

### RoadName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]

### RouteNumber
- **Type**: <class 'NoneType'>


# RouteMatchingOptions

### NameHint
- **Type**: typing.Optional[str]

### OnRoadThreshold
- **Type**: typing.Optional[int]

### Radius
- **Type**: typing.Optional[int]

### Strategy
- **Type**: typing.Optional[typing.Literal['MatchAny', 'MatchMostSignificantRoad']]


# RouteMatrixAllowOptions

### Hot
- **Type**: typing.Optional[bool]

### Hov
- **Type**: typing.Optional[bool]


# RouteMatrixAutoCircle

### Margin
- **Type**: typing.Optional[int]

### MaxRadius
- **Type**: typing.Optional[int]


# RouteMatrixAvoidanceArea

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixAvoidanceAreaGeometry'>
- **Required**: Yes


# RouteMatrixAvoidanceAreaGeometry

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]

### PolylinePolygon
- **Type**: typing.Optional[typing.List[str]]


# RouteMatrixAvoidanceOptions

### Areas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixAvoidanceArea]]

### CarShuttleTrains
- **Type**: typing.Optional[bool]

### ControlledAccessHighways
- **Type**: typing.Optional[bool]

### DirtRoads
- **Type**: typing.Optional[bool]

### Ferries
- **Type**: typing.Optional[bool]

### TollRoads
- **Type**: typing.Optional[bool]

### TollTransponders
- **Type**: typing.Optional[bool]

### TruckRoadTypes
- **Type**: typing.Optional[typing.List[str]]

### Tunnels
- **Type**: typing.Optional[bool]

### UTurns
- **Type**: typing.Optional[bool]

### ZoneCategories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixAvoidanceZoneCategory]]


# RouteMatrixAvoidanceZoneCategory

### Category
- **Type**: typing.Optional[typing.Literal['CongestionPricing', 'Environmental', 'Vignette']]


# RouteMatrixBoundary

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixBoundaryGeometry]

### Unbounded
- **Type**: typing.Optional[bool]


# RouteMatrixBoundaryGeometry

### AutoCircle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixAutoCircle]

### Circle
- **Type**: <class 'NoneType'>

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]


# RouteMatrixBoundaryGeometryOutput

### AutoCircle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixAutoCircle]

### Circle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.CircleOutput]

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### Polygon
- **Type**: typing.Optional[typing.List[typing.List[typing.List[float]]]]


# RouteMatrixBoundaryOutput

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixBoundaryGeometryOutput]

### Unbounded
- **Type**: typing.Optional[bool]


# RouteMatrixCarOptions

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]


# RouteMatrixDestination

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixDestinationOptions]


# RouteMatrixDestinationOptions

### AvoidActionsForDistance
- **Type**: typing.Optional[int]

### Heading
- **Type**: typing.Optional[float]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixMatchingOptions]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixSideOfStreetOptions]


# RouteMatrixEntry

### Distance
- **Type**: <class 'int'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Error
- **Type**: typing.Optional[typing.Literal['NoMatch', 'NoMatchDestination', 'NoMatchOrigin', 'NoRoute', 'Other', 'OutOfBounds', 'OutOfBoundsDestination', 'OutOfBoundsOrigin', 'Violation']]


# RouteMatrixExclusionOptions

### Countries
- **Type**: typing.List[str]
- **Required**: Yes


# RouteMatrixMatchingOptions

### NameHint
- **Type**: typing.Optional[str]

### OnRoadThreshold
- **Type**: typing.Optional[int]

### Radius
- **Type**: typing.Optional[int]

### Strategy
- **Type**: typing.Optional[typing.Literal['MatchAny', 'MatchMostSignificantRoad']]


# RouteMatrixOrigin

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixOriginOptions]


# RouteMatrixOriginOptions

### AvoidActionsForDistance
- **Type**: typing.Optional[int]

### Heading
- **Type**: typing.Optional[float]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixMatchingOptions]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixSideOfStreetOptions]


# RouteMatrixScooterOptions

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]


# RouteMatrixSideOfStreetOptions

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### UseWith
- **Type**: typing.Optional[typing.Literal['AnyStreet', 'DividedStreetOnly']]


# RouteMatrixTrafficOptions

### FlowEventThresholdOverride
- **Type**: typing.Optional[int]

### Usage
- **Type**: typing.Optional[typing.Literal['IgnoreTrafficData', 'UseTrafficData']]


# RouteMatrixTrailerOptions

### TrailerCount
- **Type**: typing.Optional[int]


# RouteMatrixTravelModeOptions

### Car
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixCarOptions]

### Scooter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixScooterOptions]

### Truck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixTruckOptions]


# RouteMatrixTruckOptions

### AxleCount
- **Type**: typing.Optional[int]

### GrossWeight
- **Type**: typing.Optional[int]

### HazardousCargos
- **Type**: typing.Optional[typing.List[typing.Literal['Combustible', 'Corrosive', 'Explosive', 'Flammable', 'Gas', 'HarmfulToWater', 'Organic', 'Other', 'Poison', 'PoisonousInhalation', 'Radioactive']]]

### Height
- **Type**: typing.Optional[int]

### KpraLength
- **Type**: typing.Optional[int]

### Length
- **Type**: typing.Optional[int]

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]

### PayloadCapacity
- **Type**: typing.Optional[int]

### Trailer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatrixTrailerOptions]

### TruckType
- **Type**: typing.Optional[typing.Literal['LightTruck', 'StraightTruck', 'Tractor']]

### TunnelRestrictionCode
- **Type**: typing.Optional[str]

### WeightPerAxle
- **Type**: typing.Optional[int]

### WeightPerAxleGroup
- **Type**: <class 'NoneType'>

### Width
- **Type**: typing.Optional[int]


# RouteMatrixVehicleLicensePlate

### LastCharacter
- **Type**: typing.Optional[str]


# RouteNoticeDetailRange

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# RouteNumber

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Direction
- **Type**: typing.Optional[typing.Literal['East', 'North', 'South', 'West']]

### Language
- **Type**: typing.Optional[str]


# RouteOriginOptions

### AvoidActionsForDistance
- **Type**: typing.Optional[int]

### AvoidUTurns
- **Type**: typing.Optional[bool]

### Heading
- **Type**: typing.Optional[float]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatchingOptions]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSideOfStreetOptions]


# RoutePassThroughPlace

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### OriginalPosition
- **Type**: typing.Optional[typing.List[float]]

### WaypointIndex
- **Type**: typing.Optional[int]


# RoutePassThroughWaypoint

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePassThroughPlace'>
- **Required**: Yes

### GeometryOffset
- **Type**: typing.Optional[int]


# RoutePedestrianArrival

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianPlace'>
- **Required**: Yes

### Time
- **Type**: typing.Optional[str]


# RoutePedestrianDeparture

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianPlace'>
- **Required**: Yes

### Time
- **Type**: typing.Optional[str]


# RoutePedestrianLegDetails

### Arrival
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianArrival'>
- **Required**: Yes

### Departure
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianDeparture'>
- **Required**: Yes

### Notices
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianNotice]
- **Required**: Yes

### PassThroughWaypoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePassThroughWaypoint]
- **Required**: Yes

### Spans
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianSpan]
- **Required**: Yes

### TravelSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianTravelStep]
- **Required**: Yes

### Summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianSummary]


# RoutePedestrianNotice

### Code
- **Type**: typing.Literal['AccuratePolylineUnavailable', 'Other', 'ViolatedAvoidDirtRoad', 'ViolatedAvoidTunnel', 'ViolatedPedestrianOption']
- **Required**: Yes

### Impact
- **Type**: typing.Optional[typing.Literal['High', 'Low']]


# RoutePedestrianOptions

### Speed
- **Type**: typing.Optional[float]


# RoutePedestrianOverviewSummary

### Distance
- **Type**: <class 'int'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# RoutePedestrianPlace

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### OriginalPosition
- **Type**: typing.Optional[typing.List[float]]

### SideOfStreet
- **Type**: typing.Optional[typing.Literal['Left', 'Right']]

### WaypointIndex
- **Type**: typing.Optional[int]


# RoutePedestrianSpan

### BestCaseDuration
- **Type**: typing.Optional[int]

### Country
- **Type**: typing.Optional[str]

### Distance
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### DynamicSpeed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSpanDynamicSpeedDetails]

### FunctionalClassification
- **Type**: typing.Optional[int]

### GeometryOffset
- **Type**: typing.Optional[int]

### Incidents
- **Type**: typing.Optional[typing.List[int]]

### Names
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]]

### PedestrianAccess
- **Type**: typing.Optional[typing.List[typing.Literal['Allowed', 'Indoors', 'NoThroughTraffic', 'Park', 'Stairs', 'TollRoad']]]

### Region
- **Type**: typing.Optional[str]

### RoadAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['Bridge', 'BuiltUpArea', 'ControlledAccessHighway', 'DirtRoad', 'DividedRoad', 'Motorway', 'PrivateRoad', 'Ramp', 'RightHandTraffic', 'Roundabout', 'Tunnel', 'UnderConstruction']]]

### RouteNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteNumber]]

### SpeedLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSpanSpeedLimitDetails]

### TypicalDuration
- **Type**: typing.Optional[int]


# RoutePedestrianSummary

### Overview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianOverviewSummary]

### TravelOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianTravelOnlySummary]


# RoutePedestrianTravelOnlySummary

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# RoutePedestrianTravelStep

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Arrive', 'Continue', 'Depart', 'Exit', 'Keep', 'Ramp', 'RoundaboutEnter', 'RoundaboutExit', 'RoundaboutPass', 'Turn', 'UTurn']
- **Required**: Yes

### ContinueStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteContinueStepDetails]

### CurrentRoad
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoad]

### Distance
- **Type**: typing.Optional[int]

### ExitNumber
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]]

### GeometryOffset
- **Type**: typing.Optional[int]

### Instruction
- **Type**: typing.Optional[str]

### KeepStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteKeepStepDetails]

### NextRoad
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoad]

### RoundaboutEnterStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoundaboutEnterStepDetails]

### RoundaboutExitStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoundaboutExitStepDetails]

### RoundaboutPassStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoundaboutPassStepDetails]

### Signpost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSignpost]

### TurnStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTurnStepDetails]


# RouteRampStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteResponseNotice

### Code
- **Type**: typing.Literal['MainLanguageNotFound', 'Other', 'TravelTimeExceedsDriverWorkHours']
- **Required**: Yes

### Impact
- **Type**: typing.Optional[typing.Literal['High', 'Low']]


# RouteRoad

### RoadName
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### RouteNumber
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteNumber]
- **Required**: Yes

### Towards
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['Highway', 'Rural', 'Urban']]


# RouteRoundaboutEnterStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteRoundaboutExitStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### RelativeExit
- **Type**: typing.Optional[int]

### RoundaboutAngle
- **Type**: typing.Optional[float]

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]


# RouteRoundaboutPassStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteScooterOptions

### EngineType
- **Type**: typing.Optional[typing.Literal['Electric', 'InternalCombustion', 'PluginHybrid']]

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]


# RouteSideOfStreetOptions

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### UseWith
- **Type**: typing.Optional[typing.Literal['AnyStreet', 'DividedStreetOnly']]


# RouteSignpost

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSignpostLabel]
- **Required**: Yes


# RouteSignpostLabel

### RouteNumber
- **Type**: <class 'NoneType'>

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]


# RouteSpanDynamicSpeedDetails

### BestCaseSpeed
- **Type**: typing.Optional[float]

### TurnDuration
- **Type**: typing.Optional[int]

### TypicalSpeed
- **Type**: typing.Optional[float]


# RouteSpanSpeedLimitDetails

### MaxSpeed
- **Type**: typing.Optional[float]

### Unlimited
- **Type**: typing.Optional[bool]


# RouteSummary

### Distance
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### Tolls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollSummary]


# RouteToll

### PaymentSites
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollPaymentSite]
- **Required**: Yes

### Rates
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollRate]
- **Required**: Yes

### Systems
- **Type**: typing.List[int]
- **Required**: Yes

### Country
- **Type**: typing.Optional[str]


# RouteTollOptions

### AllTransponders
- **Type**: typing.Optional[bool]

### AllVignettes
- **Type**: typing.Optional[bool]

### Currency
- **Type**: typing.Optional[str]

### EmissionType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteEmissionType]

### VehicleCategory
- **Type**: typing.Optional[typing.Literal['Minibus']]


# RouteTollPass

### IncludesReturnTrip
- **Type**: typing.Optional[bool]

### SeniorPass
- **Type**: typing.Optional[bool]

### TransferCount
- **Type**: typing.Optional[int]

### TripCount
- **Type**: typing.Optional[int]

### ValidityPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollPassValidityPeriod]


# RouteTollPassValidityPeriod

### Period
- **Type**: typing.Literal['Annual', 'Days', 'ExtendedAnnual', 'Minutes', 'Months']
- **Required**: Yes

### PeriodCount
- **Type**: typing.Optional[int]


# RouteTollPaymentSite

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# RouteTollPrice

### Currency
- **Type**: <class 'str'>
- **Required**: Yes

### Estimate
- **Type**: <class 'bool'>
- **Required**: Yes

### Range
- **Type**: <class 'bool'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes

### PerDuration
- **Type**: typing.Optional[int]

### RangeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollPriceValueRange]


# RouteTollPriceSummary

### Currency
- **Type**: <class 'str'>
- **Required**: Yes

### Estimate
- **Type**: <class 'bool'>
- **Required**: Yes

### Range
- **Type**: <class 'bool'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes

### RangeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollPriceValueRange]


# RouteTollPriceValueRange

### Min
- **Type**: <class 'float'>
- **Required**: Yes

### Max
- **Type**: <class 'float'>
- **Required**: Yes


# RouteTollRate

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPrice
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollPrice'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaymentMethods
- **Type**: typing.List[typing.Literal['BankCard', 'Cash', 'CashExact', 'CreditCard', 'PassSubscription', 'Transponder', 'TravelCard', 'VideoToll']]
- **Required**: Yes

### Transponders
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTransponder]
- **Required**: Yes

### ApplicableTimes
- **Type**: typing.Optional[str]

### ConvertedPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollPrice]

### Pass
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollPass]


# RouteTollSummary

### Total
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollPriceSummary]


# RouteTollSystem

### Name
- **Type**: typing.Optional[str]


# RouteTrafficOptions

### FlowEventThresholdOverride
- **Type**: typing.Optional[int]

### Usage
- **Type**: typing.Optional[typing.Literal['IgnoreTrafficData', 'UseTrafficData']]


# RouteTrailerOptions

### AxleCount
- **Type**: typing.Optional[int]

### TrailerCount
- **Type**: typing.Optional[int]


# RouteTransponder

### SystemName
- **Type**: typing.Optional[str]


# RouteTravelModeOptions

### Car
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteCarOptions]

### Pedestrian
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePedestrianOptions]

### Scooter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteScooterOptions]

### Truck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTruckOptions]


# RouteTruckOptions

### AxleCount
- **Type**: typing.Optional[int]

### EngineType
- **Type**: typing.Optional[typing.Literal['Electric', 'InternalCombustion', 'PluginHybrid']]

### GrossWeight
- **Type**: typing.Optional[int]

### HazardousCargos
- **Type**: typing.Optional[typing.List[typing.Literal['Combustible', 'Corrosive', 'Explosive', 'Flammable', 'Gas', 'HarmfulToWater', 'Organic', 'Other', 'Poison', 'PoisonousInhalation', 'Radioactive']]]

### Height
- **Type**: typing.Optional[int]

### HeightAboveFirstAxle
- **Type**: typing.Optional[int]

### KpraLength
- **Type**: typing.Optional[int]

### Length
- **Type**: typing.Optional[int]

### LicensePlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleLicensePlate]

### MaxSpeed
- **Type**: typing.Optional[float]

### Occupancy
- **Type**: typing.Optional[int]

### PayloadCapacity
- **Type**: typing.Optional[int]

### TireCount
- **Type**: typing.Optional[int]

### Trailer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTrailerOptions]

### TruckType
- **Type**: typing.Optional[typing.Literal['LightTruck', 'StraightTruck', 'Tractor']]

### TunnelRestrictionCode
- **Type**: typing.Optional[str]

### WeightPerAxle
- **Type**: typing.Optional[int]

### WeightPerAxleGroup
- **Type**: <class 'NoneType'>

### Width
- **Type**: typing.Optional[int]


# RouteTurnStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteUTurnStepDetails

### Intersection
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]
- **Required**: Yes

### SteeringDirection
- **Type**: typing.Optional[typing.Literal['Left', 'Right', 'Straight']]

### TurnAngle
- **Type**: typing.Optional[float]

### TurnIntensity
- **Type**: typing.Optional[typing.Literal['Sharp', 'Slight', 'Typical']]


# RouteVehicleArrival

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehiclePlace'>
- **Required**: Yes

### Time
- **Type**: typing.Optional[str]


# RouteVehicleDeparture

### Place
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehiclePlace'>
- **Required**: Yes

### Time
- **Type**: typing.Optional[str]


# RouteVehicleIncident

### Description
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['Critical', 'High', 'Low', 'Medium']]

### StartTime
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['Accident', 'Congestion', 'Construction', 'DisabledVehicle', 'LaneRestriction', 'MassTransit', 'Other', 'PlannedEvent', 'RoadClosure', 'RoadHazard', 'Weather']]


# RouteVehicleLegDetails

### Arrival
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleArrival'>
- **Required**: Yes

### Departure
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleDeparture'>
- **Required**: Yes

### Incidents
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleIncident]
- **Required**: Yes

### Notices
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleNotice]
- **Required**: Yes

### PassThroughWaypoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoutePassThroughWaypoint]
- **Required**: Yes

### Spans
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleSpan]
- **Required**: Yes

### Tolls
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteToll]
- **Required**: Yes

### TollSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTollSystem]
- **Required**: Yes

### TravelSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleTravelStep]
- **Required**: Yes

### TruckRoadTypes
- **Type**: typing.List[str]
- **Required**: Yes

### Zones
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteZone]
- **Required**: Yes

### Summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleSummary]


# RouteVehicleLicensePlate

### LastCharacter
- **Type**: typing.Optional[str]


# RouteVehicleNotice

### Code
- **Type**: typing.Literal['AccuratePolylineUnavailable', 'Other', 'PotentialViolatedAvoidTollRoadUsage', 'PotentialViolatedCarpoolUsage', 'PotentialViolatedTurnRestrictionUsage', 'PotentialViolatedVehicleRestrictionUsage', 'PotentialViolatedZoneRestrictionUsage', 'SeasonalClosure', 'TollTransponder', 'TollsDataTemporarilyUnavailable', 'TollsDataUnavailable', 'ViolatedAvoidControlledAccessHighway', 'ViolatedAvoidDifficultTurns', 'ViolatedAvoidDirtRoad', 'ViolatedAvoidSeasonalClosure', 'ViolatedAvoidTollRoad', 'ViolatedAvoidTollTransponder', 'ViolatedAvoidTruckRoadType', 'ViolatedAvoidTunnel', 'ViolatedAvoidUTurns', 'ViolatedBlockedRoad', 'ViolatedCarpool', 'ViolatedEmergencyGate', 'ViolatedStartDirection', 'ViolatedTurnRestriction', 'ViolatedVehicleRestriction', 'ViolatedZoneRestriction']
- **Required**: Yes

### Details
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleNoticeDetail]
- **Required**: Yes

### Impact
- **Type**: typing.Optional[typing.Literal['High', 'Low']]


# RouteVehicleNoticeDetail

### Title
- **Type**: typing.Optional[str]

### ViolatedConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteViolatedConstraints]


# RouteVehicleOverviewSummary

### Distance
- **Type**: <class 'int'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### BestCaseDuration
- **Type**: typing.Optional[int]

### TypicalDuration
- **Type**: typing.Optional[int]


# RouteVehiclePlace

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### OriginalPosition
- **Type**: typing.Optional[typing.List[float]]

### SideOfStreet
- **Type**: typing.Optional[typing.Literal['Left', 'Right']]

### WaypointIndex
- **Type**: typing.Optional[int]


# RouteVehicleSpan

### BestCaseDuration
- **Type**: typing.Optional[int]

### CarAccess
- **Type**: typing.Optional[typing.List[typing.Literal['Allowed', 'NoThroughTraffic', 'TollRoad']]]

### Country
- **Type**: typing.Optional[str]

### Distance
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### DynamicSpeed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSpanDynamicSpeedDetails]

### FunctionalClassification
- **Type**: typing.Optional[int]

### Gate
- **Type**: typing.Optional[typing.Literal['Emergency', 'KeyAccess', 'PermissionRequired']]

### GeometryOffset
- **Type**: typing.Optional[int]

### Incidents
- **Type**: typing.Optional[typing.List[int]]

### Names
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]]

### Notices
- **Type**: typing.Optional[typing.List[int]]

### RailwayCrossing
- **Type**: typing.Optional[typing.Literal['Protected', 'Unprotected']]

### Region
- **Type**: typing.Optional[str]

### RoadAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['Bridge', 'BuiltUpArea', 'ControlledAccessHighway', 'DirtRoad', 'DividedRoad', 'Motorway', 'PrivateRoad', 'Ramp', 'RightHandTraffic', 'Roundabout', 'Tunnel', 'UnderConstruction']]]

### RouteNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteNumber]]

### ScooterAccess
- **Type**: typing.Optional[typing.List[typing.Literal['Allowed', 'NoThroughTraffic', 'TollRoad']]]

### SpeedLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSpanSpeedLimitDetails]

### TollSystems
- **Type**: typing.Optional[typing.List[int]]

### TruckAccess
- **Type**: typing.Optional[typing.List[typing.Literal['Allowed', 'NoThroughTraffic', 'TollRoad']]]

### TruckRoadTypes
- **Type**: typing.Optional[typing.List[int]]

### TypicalDuration
- **Type**: typing.Optional[int]

### Zones
- **Type**: typing.Optional[typing.List[int]]


# RouteVehicleSummary

### Overview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleOverviewSummary]

### TravelOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteVehicleTravelOnlySummary]


# RouteVehicleTravelOnlySummary

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### BestCaseDuration
- **Type**: typing.Optional[int]

### TypicalDuration
- **Type**: typing.Optional[int]


# RouteVehicleTravelStep

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Arrive', 'Continue', 'ContinueHighway', 'Depart', 'EnterHighway', 'Exit', 'Keep', 'Ramp', 'RoundaboutEnter', 'RoundaboutExit', 'RoundaboutPass', 'Turn', 'UTurn']
- **Required**: Yes

### ContinueHighwayStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteContinueHighwayStepDetails]

### ContinueStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteContinueStepDetails]

### CurrentRoad
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoad]

### Distance
- **Type**: typing.Optional[int]

### EnterHighwayStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteEnterHighwayStepDetails]

### ExitNumber
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.LocalizedString]]

### ExitStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteExitStepDetails]

### GeometryOffset
- **Type**: typing.Optional[int]

### Instruction
- **Type**: typing.Optional[str]

### KeepStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteKeepStepDetails]

### NextRoad
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoad]

### RampStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRampStepDetails]

### RoundaboutEnterStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoundaboutEnterStepDetails]

### RoundaboutExitStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoundaboutExitStepDetails]

### RoundaboutPassStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteRoundaboutPassStepDetails]

### Signpost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSignpost]

### TurnStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteTurnStepDetails]

### UTurnStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteUTurnStepDetails]


# RouteViolatedConstraints

### HazardousCargos
- **Type**: typing.List[typing.Literal['Combustible', 'Corrosive', 'Explosive', 'Flammable', 'Gas', 'HarmfulToWater', 'Organic', 'Other', 'Poison', 'PoisonousInhalation', 'Radioactive']]
- **Required**: Yes

### AllHazardsRestricted
- **Type**: typing.Optional[bool]

### AxleCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteNoticeDetailRange]

### MaxHeight
- **Type**: typing.Optional[int]

### MaxKpraLength
- **Type**: typing.Optional[int]

### MaxLength
- **Type**: typing.Optional[int]

### MaxPayloadCapacity
- **Type**: typing.Optional[int]

### MaxWeight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteWeightConstraint]

### MaxWeightPerAxle
- **Type**: typing.Optional[int]

### MaxWeightPerAxleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WeightPerAxleGroup]

### MaxWidth
- **Type**: typing.Optional[int]

### Occupancy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteNoticeDetailRange]

### RestrictedTimes
- **Type**: typing.Optional[str]

### TimeDependent
- **Type**: typing.Optional[bool]

### TrailerCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteNoticeDetailRange]

### TravelMode
- **Type**: typing.Optional[bool]

### TruckRoadType
- **Type**: typing.Optional[str]

### TruckType
- **Type**: typing.Optional[typing.Literal['LightTruck', 'StraightTruck', 'Tractor']]

### TunnelRestrictionCode
- **Type**: typing.Optional[str]


# RouteWaypoint

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### AvoidActionsForDistance
- **Type**: typing.Optional[int]

### AvoidUTurns
- **Type**: typing.Optional[bool]

### Heading
- **Type**: typing.Optional[float]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteMatchingOptions]

### PassThrough
- **Type**: typing.Optional[bool]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RouteSideOfStreetOptions]

### StopDuration
- **Type**: typing.Optional[int]


# RouteWeightConstraint

### Type
- **Type**: typing.Literal['Current', 'Gross', 'Unknown']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes


# RouteZone

### Category
- **Type**: typing.Optional[typing.Literal['CongestionPricing', 'Environmental', 'Vignette']]

### Name
- **Type**: typing.Optional[str]


# SnapToRoadsRequest

### TracePoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoadSnapTracePoint]
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]

### SnappedGeometryFormat
- **Type**: typing.Optional[typing.Literal['FlexiblePolyline', 'Simple']]

### SnapRadius
- **Type**: typing.Optional[int]

### TravelMode
- **Type**: typing.Optional[typing.Literal['Car', 'Pedestrian', 'Scooter', 'Truck']]

### TravelModeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoadSnapTravelModeOptions]


# SnapToRoadsResponse

### Notices
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoadSnapNotice]
- **Required**: Yes

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### SnappedGeometry
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoadSnapSnappedGeometry'>
- **Required**: Yes

### SnappedGeometryFormat
- **Type**: typing.Literal['FlexiblePolyline', 'Simple']
- **Required**: Yes

### SnappedTracePoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.RoadSnapSnappedTracePoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.ResponseMetadata'>
- **Required**: Yes


# WaypointOptimizationAccessHours

### From
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationAccessHoursEntry'>
- **Required**: Yes

### To
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationAccessHoursEntry'>
- **Required**: Yes


# WaypointOptimizationAccessHoursEntry

### DayOfWeek
- **Type**: typing.Literal['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
- **Required**: Yes

### TimeOfDay
- **Type**: <class 'str'>
- **Required**: Yes


# WaypointOptimizationAvoidanceArea

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationAvoidanceAreaGeometry'>
- **Required**: Yes


# WaypointOptimizationAvoidanceAreaGeometry

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]


# WaypointOptimizationAvoidanceOptions

### Areas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationAvoidanceArea]]

### CarShuttleTrains
- **Type**: typing.Optional[bool]

### ControlledAccessHighways
- **Type**: typing.Optional[bool]

### DirtRoads
- **Type**: typing.Optional[bool]

### Ferries
- **Type**: typing.Optional[bool]

### TollRoads
- **Type**: typing.Optional[bool]

### Tunnels
- **Type**: typing.Optional[bool]

### UTurns
- **Type**: typing.Optional[bool]


# WaypointOptimizationClusteringOptions

### Algorithm
- **Type**: typing.Literal['DrivingDistance', 'TopologySegment']
- **Required**: Yes

### DrivingDistanceOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationDrivingDistanceOptions]


# WaypointOptimizationConnection

### Distance
- **Type**: <class 'int'>
- **Required**: Yes

### From
- **Type**: <class 'str'>
- **Required**: Yes

### RestDuration
- **Type**: <class 'int'>
- **Required**: Yes

### To
- **Type**: <class 'str'>
- **Required**: Yes

### TravelDuration
- **Type**: <class 'int'>
- **Required**: Yes

### WaitDuration
- **Type**: <class 'int'>
- **Required**: Yes


# WaypointOptimizationDestinationOptions

### AccessHours
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationAccessHours]

### AppointmentTime
- **Type**: typing.Optional[str]

### Heading
- **Type**: typing.Optional[float]

### Id
- **Type**: typing.Optional[str]

### ServiceDuration
- **Type**: typing.Optional[int]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationSideOfStreetOptions]


# WaypointOptimizationDriverOptions

### RestCycles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationRestCycles]

### RestProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationRestProfile]

### TreatServiceTimeAs
- **Type**: typing.Optional[typing.Literal['Rest', 'Work']]


# WaypointOptimizationDrivingDistanceOptions

### DrivingDistance
- **Type**: <class 'int'>
- **Required**: Yes


# WaypointOptimizationExclusionOptions

### Countries
- **Type**: typing.List[str]
- **Required**: Yes


# WaypointOptimizationFailedConstraint

### Constraint
- **Type**: typing.Optional[typing.Literal['AccessHours', 'AppointmentTime', 'Before', 'Heading', 'ServiceDuration', 'SideOfStreet']]

### Reason
- **Type**: typing.Optional[str]


# WaypointOptimizationImpedingWaypoint

### FailedConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationFailedConstraint]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes


# WaypointOptimizationOptimizedWaypoint

### DepartureTime
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### ArrivalTime
- **Type**: typing.Optional[str]

### ClusterIndex
- **Type**: typing.Optional[int]


# WaypointOptimizationOriginOptions

### Id
- **Type**: typing.Optional[str]


# WaypointOptimizationPedestrianOptions

### Speed
- **Type**: typing.Optional[float]


# WaypointOptimizationRestCycleDurations

### RestDuration
- **Type**: <class 'int'>
- **Required**: Yes

### WorkDuration
- **Type**: <class 'int'>
- **Required**: Yes


# WaypointOptimizationRestCycles

### LongCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationRestCycleDurations'>
- **Required**: Yes

### ShortCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationRestCycleDurations'>
- **Required**: Yes


# WaypointOptimizationRestProfile

### Profile
- **Type**: <class 'str'>
- **Required**: Yes


# WaypointOptimizationSideOfStreetOptions

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### UseWith
- **Type**: typing.Optional[typing.Literal['AnyStreet', 'DividedStreetOnly']]


# WaypointOptimizationTimeBreakdown

### RestDuration
- **Type**: <class 'int'>
- **Required**: Yes

### ServiceDuration
- **Type**: <class 'int'>
- **Required**: Yes

### TravelDuration
- **Type**: <class 'int'>
- **Required**: Yes

### WaitDuration
- **Type**: <class 'int'>
- **Required**: Yes


# WaypointOptimizationTrafficOptions

### Usage
- **Type**: typing.Optional[typing.Literal['IgnoreTrafficData', 'UseTrafficData']]


# WaypointOptimizationTrailerOptions

### TrailerCount
- **Type**: typing.Optional[int]


# WaypointOptimizationTravelModeOptions

### Pedestrian
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationPedestrianOptions]

### Truck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationTruckOptions]


# WaypointOptimizationTruckOptions

### GrossWeight
- **Type**: typing.Optional[int]

### HazardousCargos
- **Type**: typing.Optional[typing.List[typing.Literal['Combustible', 'Corrosive', 'Explosive', 'Flammable', 'Gas', 'HarmfulToWater', 'Organic', 'Other', 'Poison', 'PoisonousInhalation', 'Radioactive']]]

### Height
- **Type**: typing.Optional[int]

### Length
- **Type**: typing.Optional[int]

### Trailer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationTrailerOptions]

### TruckType
- **Type**: typing.Optional[typing.Literal['StraightTruck', 'Tractor']]

### TunnelRestrictionCode
- **Type**: typing.Optional[str]

### WeightPerAxle
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]


# WaypointOptimizationWaypoint

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### AccessHours
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationAccessHours]

### AppointmentTime
- **Type**: typing.Optional[str]

### Before
- **Type**: typing.Optional[typing.List[int]]

### Heading
- **Type**: typing.Optional[float]

### Id
- **Type**: typing.Optional[str]

### ServiceDuration
- **Type**: typing.Optional[int]

### SideOfStreet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_routes.geo_routes_classes.WaypointOptimizationSideOfStreetOptions]


# WeightPerAxleGroup

### Single
- **Type**: typing.Optional[int]

### Tandem
- **Type**: typing.Optional[int]

### Triple
- **Type**: typing.Optional[int]

### Quad
- **Type**: typing.Optional[int]

### Quint
- **Type**: typing.Optional[int]


