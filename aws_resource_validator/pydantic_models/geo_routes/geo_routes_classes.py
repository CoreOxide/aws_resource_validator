from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.geo_routes.geo_routes_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class IsolineAllowOptions(BaseValidatorModel):
    Hot: Optional[bool] = None
    Hov: Optional[bool] = None


class IsolineGranularityOptions(BaseValidatorModel):
    MaxPoints: Optional[int] = None
    MaxResolution: Optional[int] = None


class IsolineThresholds(BaseValidatorModel):
    Distance: Optional[List[int]] = None
    Time: Optional[List[int]] = None


class IsolineTrafficOptions(BaseValidatorModel):
    FlowEventThresholdOverride: Optional[int] = None
    Usage: Optional[TrafficUsageType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RouteMatrixAllowOptions(BaseValidatorModel):
    Hot: Optional[bool] = None
    Hov: Optional[bool] = None


class RouteMatrixExclusionOptions(BaseValidatorModel):
    Countries: List[str]


class RouteMatrixTrafficOptions(BaseValidatorModel):
    FlowEventThresholdOverride: Optional[int] = None
    Usage: Optional[TrafficUsageType] = None


class RouteMatrixEntry(BaseValidatorModel):
    Distance: int
    Duration: int
    Error: Optional[RouteMatrixErrorCodeType] = None


class RouteAllowOptions(BaseValidatorModel):
    Hot: Optional[bool] = None
    Hov: Optional[bool] = None


class RouteExclusionOptions(BaseValidatorModel):
    Countries: List[str]


class RouteTrafficOptions(BaseValidatorModel):
    FlowEventThresholdOverride: Optional[int] = None
    Usage: Optional[TrafficUsageType] = None


class RouteResponseNotice(BaseValidatorModel):
    Code: RouteResponseNoticeCodeType
    Impact: Optional[RouteNoticeImpactType] = None


class CircleOutput(BaseValidatorModel):
    Center: List[float]
    Radius: float


class Circle(BaseValidatorModel):
    Center: List[float]
    Radius: float


class Corridor(BaseValidatorModel):
    LineString: List[List[float]]
    Radius: int


class PolylineCorridor(BaseValidatorModel):
    Polyline: str
    Radius: int


class IsolineAvoidanceZoneCategory(BaseValidatorModel):
    Category: Optional[IsolineZoneCategoryType] = None


class IsolineVehicleLicensePlate(BaseValidatorModel):
    LastCharacter: Optional[str] = None


class IsolineConnectionGeometry(BaseValidatorModel):
    LineString: Optional[List[List[float]]] = None
    Polyline: Optional[str] = None


class IsolineMatchingOptions(BaseValidatorModel):
    NameHint: Optional[str] = None
    OnRoadThreshold: Optional[int] = None
    Radius: Optional[int] = None
    Strategy: Optional[MatchingStrategyType] = None


class IsolineSideOfStreetOptions(BaseValidatorModel):
    Position: List[float]
    UseWith: Optional[SideOfStreetMatchingStrategyType] = None


class IsolineShapeGeometry(BaseValidatorModel):
    Polygon: Optional[List[List[List[float]]]] = None
    PolylinePolygon: Optional[List[str]] = None


class IsolineTrailerOptions(BaseValidatorModel):
    AxleCount: Optional[int] = None
    TrailerCount: Optional[int] = None


class WeightPerAxleGroup(BaseValidatorModel):
    Single: Optional[int] = None
    Tandem: Optional[int] = None
    Triple: Optional[int] = None
    Quad: Optional[int] = None
    Quint: Optional[int] = None


class LocalizedString(BaseValidatorModel):
    Value: str
    Language: Optional[str] = None


class WaypointOptimizationExclusionOptions(BaseValidatorModel):
    Countries: List[str]


class WaypointOptimizationOriginOptions(BaseValidatorModel):
    Id: Optional[str] = None


class WaypointOptimizationTrafficOptions(BaseValidatorModel):
    Usage: Optional[TrafficUsageType] = None


class WaypointOptimizationConnection(BaseValidatorModel):
    Distance: int
    From: str
    RestDuration: int
    To: str
    TravelDuration: int
    WaitDuration: int


class WaypointOptimizationOptimizedWaypoint(BaseValidatorModel):
    DepartureTime: str
    Id: str
    Position: List[float]
    ArrivalTime: Optional[str] = None
    ClusterIndex: Optional[int] = None


class WaypointOptimizationTimeBreakdown(BaseValidatorModel):
    RestDuration: int
    ServiceDuration: int
    TravelDuration: int
    WaitDuration: int


class RoadSnapNotice(BaseValidatorModel):
    Code: RoadSnapNoticeCodeType
    Title: str
    TracePointIndexes: List[int]


class RoadSnapSnappedGeometry(BaseValidatorModel):
    LineString: Optional[List[List[float]]] = None
    Polyline: Optional[str] = None


class RoadSnapSnappedTracePoint(BaseValidatorModel):
    Confidence: float
    OriginalPosition: List[float]
    SnappedPosition: List[float]


class RoadSnapTracePoint(BaseValidatorModel):
    Position: List[float]
    Heading: Optional[float] = None
    Speed: Optional[float] = None
    Timestamp: Optional[str] = None


class RoadSnapTrailerOptions(BaseValidatorModel):
    TrailerCount: Optional[int] = None


class RouteAvoidanceZoneCategory(BaseValidatorModel):
    Category: RouteZoneCategoryType


class RouteVehicleLicensePlate(BaseValidatorModel):
    LastCharacter: Optional[str] = None


class RouteMatchingOptions(BaseValidatorModel):
    NameHint: Optional[str] = None
    OnRoadThreshold: Optional[int] = None
    Radius: Optional[int] = None
    Strategy: Optional[MatchingStrategyType] = None


class RouteSideOfStreetOptions(BaseValidatorModel):
    Position: List[float]
    UseWith: Optional[SideOfStreetMatchingStrategyType] = None


class RouteDriverScheduleInterval(BaseValidatorModel):
    DriveDuration: int
    RestDuration: int


class RouteEmissionType(BaseValidatorModel):
    Type: str
    Co2EmissionClass: Optional[str] = None


class RouteFerryAfterTravelStep(BaseValidatorModel):
    Duration: int
    Type: Literal['Deboard']
    Instruction: Optional[str] = None


class RouteFerryPlace(BaseValidatorModel):
    Position: List[float]
    Name: Optional[str] = None
    OriginalPosition: Optional[List[float]] = None
    WaypointIndex: Optional[int] = None


class RouteFerryBeforeTravelStep(BaseValidatorModel):
    Duration: int
    Type: Literal['Board']
    Instruction: Optional[str] = None


class RouteFerryNotice(BaseValidatorModel):
    Code: RouteFerryNoticeCodeType
    Impact: Optional[RouteNoticeImpactType] = None


class RouteFerryTravelStep(BaseValidatorModel):
    Duration: int
    Type: RouteFerryTravelStepTypeType
    Distance: Optional[int] = None
    GeometryOffset: Optional[int] = None
    Instruction: Optional[str] = None


class RouteFerryOverviewSummary(BaseValidatorModel):
    Distance: int
    Duration: int


class RouteFerryTravelOnlySummary(BaseValidatorModel):
    Duration: int


class RouteLegGeometry(BaseValidatorModel):
    LineString: Optional[List[List[float]]] = None
    Polyline: Optional[str] = None


class RouteNumber(BaseValidatorModel):
    Value: str
    Direction: Optional[RouteDirectionType] = None
    Language: Optional[str] = None


class RouteMatrixAutoCircle(BaseValidatorModel):
    Margin: Optional[int] = None
    MaxRadius: Optional[int] = None


class RouteMatrixAvoidanceAreaGeometry(BaseValidatorModel):
    BoundingBox: Optional[List[float]] = None
    Polygon: Optional[List[List[List[float]]]] = None
    PolylinePolygon: Optional[List[str]] = None


class RouteMatrixAvoidanceZoneCategory(BaseValidatorModel):
    Category: Optional[RouteMatrixZoneCategoryType] = None


class RouteMatrixVehicleLicensePlate(BaseValidatorModel):
    LastCharacter: Optional[str] = None


class RouteMatrixMatchingOptions(BaseValidatorModel):
    NameHint: Optional[str] = None
    OnRoadThreshold: Optional[int] = None
    Radius: Optional[int] = None
    Strategy: Optional[MatchingStrategyType] = None


class RouteMatrixSideOfStreetOptions(BaseValidatorModel):
    Position: List[float]
    UseWith: Optional[SideOfStreetMatchingStrategyType] = None


class RouteMatrixTrailerOptions(BaseValidatorModel):
    TrailerCount: Optional[int] = None


class RouteNoticeDetailRange(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class RoutePassThroughPlace(BaseValidatorModel):
    Position: List[float]
    OriginalPosition: Optional[List[float]] = None
    WaypointIndex: Optional[int] = None


class RoutePedestrianPlace(BaseValidatorModel):
    Position: List[float]
    Name: Optional[str] = None
    OriginalPosition: Optional[List[float]] = None
    SideOfStreet: Optional[RouteSideOfStreetType] = None
    WaypointIndex: Optional[int] = None


class RoutePedestrianNotice(BaseValidatorModel):
    Code: RoutePedestrianNoticeCodeType
    Impact: Optional[RouteNoticeImpactType] = None


class RoutePedestrianOptions(BaseValidatorModel):
    Speed: Optional[float] = None


class RoutePedestrianOverviewSummary(BaseValidatorModel):
    Distance: int
    Duration: int


class RouteSpanDynamicSpeedDetails(BaseValidatorModel):
    BestCaseSpeed: Optional[float] = None
    TurnDuration: Optional[int] = None
    TypicalSpeed: Optional[float] = None


class RouteSpanSpeedLimitDetails(BaseValidatorModel):
    MaxSpeed: Optional[float] = None
    Unlimited: Optional[bool] = None


class RoutePedestrianTravelOnlySummary(BaseValidatorModel):
    Duration: int


class RouteTollPassValidityPeriod(BaseValidatorModel):
    Period: RouteTollPassValidityPeriodTypeType
    PeriodCount: Optional[int] = None


class RouteTollPaymentSite(BaseValidatorModel):
    Position: List[float]
    Name: Optional[str] = None


class RouteTollPriceValueRange(BaseValidatorModel):
    Min: float
    Max: float


class RouteTransponder(BaseValidatorModel):
    SystemName: Optional[str] = None


class RouteTollSystem(BaseValidatorModel):
    Name: Optional[str] = None


class RouteTrailerOptions(BaseValidatorModel):
    AxleCount: Optional[int] = None
    TrailerCount: Optional[int] = None


class RouteVehiclePlace(BaseValidatorModel):
    Position: List[float]
    Name: Optional[str] = None
    OriginalPosition: Optional[List[float]] = None
    SideOfStreet: Optional[RouteSideOfStreetType] = None
    WaypointIndex: Optional[int] = None


class RouteVehicleIncident(BaseValidatorModel):
    Description: Optional[str] = None
    EndTime: Optional[str] = None
    Severity: Optional[RouteVehicleIncidentSeverityType] = None
    StartTime: Optional[str] = None
    Type: Optional[RouteVehicleIncidentTypeType] = None


class RouteZone(BaseValidatorModel):
    Category: Optional[RouteZoneCategoryType] = None
    Name: Optional[str] = None


class RouteVehicleOverviewSummary(BaseValidatorModel):
    Distance: int
    Duration: int
    BestCaseDuration: Optional[int] = None
    TypicalDuration: Optional[int] = None


class RouteVehicleTravelOnlySummary(BaseValidatorModel):
    Duration: int
    BestCaseDuration: Optional[int] = None
    TypicalDuration: Optional[int] = None


class RouteWeightConstraint(BaseValidatorModel):
    Type: RouteWeightConstraintTypeType
    Value: int


class WaypointOptimizationAccessHoursEntry(BaseValidatorModel):
    DayOfWeek: DayOfWeekType
    TimeOfDay: str


class WaypointOptimizationAvoidanceAreaGeometry(BaseValidatorModel):
    BoundingBox: Optional[List[float]] = None


class WaypointOptimizationDrivingDistanceOptions(BaseValidatorModel):
    DrivingDistance: int


class WaypointOptimizationSideOfStreetOptions(BaseValidatorModel):
    Position: List[float]
    UseWith: Optional[SideOfStreetMatchingStrategyType] = None


class WaypointOptimizationRestProfile(BaseValidatorModel):
    Profile: str


class WaypointOptimizationFailedConstraint(BaseValidatorModel):
    Constraint: Optional[WaypointOptimizationConstraintType] = None
    Reason: Optional[str] = None


class WaypointOptimizationPedestrianOptions(BaseValidatorModel):
    Speed: Optional[float] = None


class WaypointOptimizationRestCycleDurations(BaseValidatorModel):
    RestDuration: int
    WorkDuration: int


class WaypointOptimizationTrailerOptions(BaseValidatorModel):
    TrailerCount: Optional[int] = None


class IsolineAvoidanceAreaGeometry(BaseValidatorModel):
    BoundingBox: Optional[List[float]] = None
    Corridor: Optional[Corridor] = None
    Polygon: Optional[List[List[List[float]]]] = None
    PolylineCorridor: Optional[PolylineCorridor] = None
    PolylinePolygon: Optional[List[str]] = None


class RouteAvoidanceAreaGeometry(BaseValidatorModel):
    Corridor: Optional[Corridor] = None
    BoundingBox: Optional[List[float]] = None
    Polygon: Optional[List[List[List[float]]]] = None
    PolylineCorridor: Optional[PolylineCorridor] = None
    PolylinePolygon: Optional[List[str]] = None


class IsolineCarOptions(BaseValidatorModel):
    EngineType: Optional[IsolineEngineTypeType] = None
    LicensePlate: Optional[IsolineVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class IsolineScooterOptions(BaseValidatorModel):
    EngineType: Optional[IsolineEngineTypeType] = None
    LicensePlate: Optional[IsolineVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class IsolineConnection(BaseValidatorModel):
    FromPolygonIndex: int
    Geometry: IsolineConnectionGeometry
    ToPolygonIndex: int


class IsolineDestinationOptions(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    Heading: Optional[float] = None
    Matching: Optional[IsolineMatchingOptions] = None
    SideOfStreet: Optional[IsolineSideOfStreetOptions] = None


class IsolineOriginOptions(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    Heading: Optional[float] = None
    Matching: Optional[IsolineMatchingOptions] = None
    SideOfStreet: Optional[IsolineSideOfStreetOptions] = None


class IsolineTruckOptions(BaseValidatorModel):
    AxleCount: Optional[int] = None
    EngineType: Optional[IsolineEngineTypeType] = None
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[List[IsolineHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    HeightAboveFirstAxle: Optional[int] = None
    KpraLength: Optional[int] = None
    Length: Optional[int] = None
    LicensePlate: Optional[IsolineVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None
    PayloadCapacity: Optional[int] = None
    TireCount: Optional[int] = None
    Trailer: Optional[IsolineTrailerOptions] = None
    TruckType: Optional[IsolineTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None
    WeightPerAxle: Optional[int] = None
    WeightPerAxleGroup: Optional[WeightPerAxleGroup] = None
    Width: Optional[int] = None


class RouteContinueHighwayStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteContinueStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]


class RouteEnterHighwayStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteExitStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    RelativeExit: Optional[int] = None
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteFerrySpan(BaseValidatorModel):
    Country: Optional[str] = None
    Distance: Optional[int] = None
    Duration: Optional[int] = None
    GeometryOffset: Optional[int] = None
    Names: Optional[List[LocalizedString]] = None
    Region: Optional[str] = None


class RouteKeepStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteRampStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteRoundaboutEnterStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteRoundaboutExitStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    RelativeExit: Optional[int] = None
    RoundaboutAngle: Optional[float] = None
    SteeringDirection: Optional[RouteSteeringDirectionType] = None


class RouteRoundaboutPassStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteTurnStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteUTurnStepDetails(BaseValidatorModel):
    Intersection: List[LocalizedString]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


# This class is the output for the 'snap_to_roads' function.
class SnapToRoadsResponse(BaseValidatorModel):
    Notices: List[RoadSnapNotice]
    PricingBucket: str
    SnappedGeometry: RoadSnapSnappedGeometry
    SnappedGeometryFormat: GeometryFormatType
    SnappedTracePoints: List[RoadSnapSnappedTracePoint]
    ResponseMetadata: ResponseMetadata


class RoadSnapTruckOptions(BaseValidatorModel):
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[List[RoadSnapHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    Length: Optional[int] = None
    Trailer: Optional[RoadSnapTrailerOptions] = None
    TunnelRestrictionCode: Optional[str] = None
    Width: Optional[int] = None


class RouteCarOptions(BaseValidatorModel):
    EngineType: Optional[RouteEngineTypeType] = None
    LicensePlate: Optional[RouteVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class RouteScooterOptions(BaseValidatorModel):
    EngineType: Optional[RouteEngineTypeType] = None
    LicensePlate: Optional[RouteVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class RouteDestinationOptions(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    AvoidUTurns: Optional[bool] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatchingOptions] = None
    SideOfStreet: Optional[RouteSideOfStreetOptions] = None
    StopDuration: Optional[int] = None


class RouteOriginOptions(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    AvoidUTurns: Optional[bool] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatchingOptions] = None
    SideOfStreet: Optional[RouteSideOfStreetOptions] = None


class RouteWaypoint(BaseValidatorModel):
    Position: List[float]
    AvoidActionsForDistance: Optional[int] = None
    AvoidUTurns: Optional[bool] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatchingOptions] = None
    PassThrough: Optional[bool] = None
    SideOfStreet: Optional[RouteSideOfStreetOptions] = None
    StopDuration: Optional[int] = None


class RouteDriverOptions(BaseValidatorModel):
    Schedule: Optional[List[RouteDriverScheduleInterval]] = None


class RouteTollOptions(BaseValidatorModel):
    AllTransponders: Optional[bool] = None
    AllVignettes: Optional[bool] = None
    Currency: Optional[str] = None
    EmissionType: Optional[RouteEmissionType] = None
    VehicleCategory: Optional[Literal['Minibus']] = None


class RouteFerryArrival(BaseValidatorModel):
    Place: RouteFerryPlace
    Time: Optional[str] = None


class RouteFerryDeparture(BaseValidatorModel):
    Place: RouteFerryPlace
    Time: Optional[str] = None


class RouteFerrySummary(BaseValidatorModel):
    Overview: Optional[RouteFerryOverviewSummary] = None
    TravelOnly: Optional[RouteFerryTravelOnlySummary] = None


class RouteMajorRoadLabel(BaseValidatorModel):
    RoadName: Optional[LocalizedString] = None
    RouteNumber: Optional[RouteNumber] = None


class RouteRoad(BaseValidatorModel):
    RoadName: List[LocalizedString]
    RouteNumber: List[RouteNumber]
    Towards: List[LocalizedString]
    Type: Optional[RouteRoadTypeType] = None


class RouteSignpostLabel(BaseValidatorModel):
    RouteNumber: Optional[RouteNumber] = None
    Text: Optional[LocalizedString] = None


class RouteMatrixBoundaryGeometryOutput(BaseValidatorModel):
    AutoCircle: Optional[RouteMatrixAutoCircle] = None
    Circle: Optional[CircleOutput] = None
    BoundingBox: Optional[List[float]] = None
    Polygon: Optional[List[List[List[float]]]] = None


class RouteMatrixBoundaryGeometry(BaseValidatorModel):
    AutoCircle: Optional[RouteMatrixAutoCircle] = None
    Circle: Optional[Circle] = None
    BoundingBox: Optional[List[float]] = None
    Polygon: Optional[List[List[List[float]]]] = None


class RouteMatrixAvoidanceArea(BaseValidatorModel):
    Geometry: RouteMatrixAvoidanceAreaGeometry


class RouteMatrixCarOptions(BaseValidatorModel):
    LicensePlate: Optional[RouteMatrixVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class RouteMatrixScooterOptions(BaseValidatorModel):
    LicensePlate: Optional[RouteMatrixVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class RouteMatrixDestinationOptions(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatrixMatchingOptions] = None
    SideOfStreet: Optional[RouteMatrixSideOfStreetOptions] = None


class RouteMatrixOriginOptions(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatrixMatchingOptions] = None
    SideOfStreet: Optional[RouteMatrixSideOfStreetOptions] = None


class RouteMatrixTruckOptions(BaseValidatorModel):
    AxleCount: Optional[int] = None
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[List[RouteMatrixHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    KpraLength: Optional[int] = None
    Length: Optional[int] = None
    LicensePlate: Optional[RouteMatrixVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None
    PayloadCapacity: Optional[int] = None
    Trailer: Optional[RouteMatrixTrailerOptions] = None
    TruckType: Optional[RouteMatrixTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None
    WeightPerAxle: Optional[int] = None
    WeightPerAxleGroup: Optional[WeightPerAxleGroup] = None
    Width: Optional[int] = None


class RoutePassThroughWaypoint(BaseValidatorModel):
    Place: RoutePassThroughPlace
    GeometryOffset: Optional[int] = None


class RoutePedestrianArrival(BaseValidatorModel):
    Place: RoutePedestrianPlace
    Time: Optional[str] = None


class RoutePedestrianDeparture(BaseValidatorModel):
    Place: RoutePedestrianPlace
    Time: Optional[str] = None


class RoutePedestrianSpan(BaseValidatorModel):
    BestCaseDuration: Optional[int] = None
    Country: Optional[str] = None
    Distance: Optional[int] = None
    Duration: Optional[int] = None
    DynamicSpeed: Optional[RouteSpanDynamicSpeedDetails] = None
    FunctionalClassification: Optional[int] = None
    GeometryOffset: Optional[int] = None
    Incidents: Optional[List[int]] = None
    Names: Optional[List[LocalizedString]] = None
    PedestrianAccess: Optional[List[RouteSpanPedestrianAccessAttributeType]] = None
    Region: Optional[str] = None
    RoadAttributes: Optional[List[RouteSpanRoadAttributeType]] = None
    RouteNumbers: Optional[List[RouteNumber]] = None
    SpeedLimit: Optional[RouteSpanSpeedLimitDetails] = None
    TypicalDuration: Optional[int] = None


class RouteVehicleSpan(BaseValidatorModel):
    BestCaseDuration: Optional[int] = None
    CarAccess: Optional[List[RouteSpanCarAccessAttributeType]] = None
    Country: Optional[str] = None
    Distance: Optional[int] = None
    Duration: Optional[int] = None
    DynamicSpeed: Optional[RouteSpanDynamicSpeedDetails] = None
    FunctionalClassification: Optional[int] = None
    Gate: Optional[RouteSpanGateAttributeType] = None
    GeometryOffset: Optional[int] = None
    Incidents: Optional[List[int]] = None
    Names: Optional[List[LocalizedString]] = None
    Notices: Optional[List[int]] = None
    RailwayCrossing: Optional[RouteSpanRailwayCrossingAttributeType] = None
    Region: Optional[str] = None
    RoadAttributes: Optional[List[RouteSpanRoadAttributeType]] = None
    RouteNumbers: Optional[List[RouteNumber]] = None
    ScooterAccess: Optional[List[RouteSpanScooterAccessAttributeType]] = None
    SpeedLimit: Optional[RouteSpanSpeedLimitDetails] = None
    TollSystems: Optional[List[int]] = None
    TruckAccess: Optional[List[RouteSpanTruckAccessAttributeType]] = None
    TruckRoadTypes: Optional[List[int]] = None
    TypicalDuration: Optional[int] = None
    Zones: Optional[List[int]] = None


class RoutePedestrianSummary(BaseValidatorModel):
    Overview: Optional[RoutePedestrianOverviewSummary] = None
    TravelOnly: Optional[RoutePedestrianTravelOnlySummary] = None


class RouteTollPass(BaseValidatorModel):
    IncludesReturnTrip: Optional[bool] = None
    SeniorPass: Optional[bool] = None
    TransferCount: Optional[int] = None
    TripCount: Optional[int] = None
    ValidityPeriod: Optional[RouteTollPassValidityPeriod] = None


class RouteTollPriceSummary(BaseValidatorModel):
    Currency: str
    Estimate: bool
    Range: bool
    Value: float
    RangeValue: Optional[RouteTollPriceValueRange] = None


class RouteTollPrice(BaseValidatorModel):
    Currency: str
    Estimate: bool
    Range: bool
    Value: float
    PerDuration: Optional[int] = None
    RangeValue: Optional[RouteTollPriceValueRange] = None


class RouteTruckOptions(BaseValidatorModel):
    AxleCount: Optional[int] = None
    EngineType: Optional[RouteEngineTypeType] = None
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[List[RouteHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    HeightAboveFirstAxle: Optional[int] = None
    KpraLength: Optional[int] = None
    Length: Optional[int] = None
    LicensePlate: Optional[RouteVehicleLicensePlate] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None
    PayloadCapacity: Optional[int] = None
    TireCount: Optional[int] = None
    Trailer: Optional[RouteTrailerOptions] = None
    TruckType: Optional[RouteTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None
    WeightPerAxle: Optional[int] = None
    WeightPerAxleGroup: Optional[WeightPerAxleGroup] = None
    Width: Optional[int] = None


class RouteVehicleArrival(BaseValidatorModel):
    Place: RouteVehiclePlace
    Time: Optional[str] = None


class RouteVehicleDeparture(BaseValidatorModel):
    Place: RouteVehiclePlace
    Time: Optional[str] = None


class RouteVehicleSummary(BaseValidatorModel):
    Overview: Optional[RouteVehicleOverviewSummary] = None
    TravelOnly: Optional[RouteVehicleTravelOnlySummary] = None


class RouteViolatedConstraints(BaseValidatorModel):
    HazardousCargos: List[RouteHazardousCargoTypeType]
    AllHazardsRestricted: Optional[bool] = None
    AxleCount: Optional[RouteNoticeDetailRange] = None
    MaxHeight: Optional[int] = None
    MaxKpraLength: Optional[int] = None
    MaxLength: Optional[int] = None
    MaxPayloadCapacity: Optional[int] = None
    MaxWeight: Optional[RouteWeightConstraint] = None
    MaxWeightPerAxle: Optional[int] = None
    MaxWeightPerAxleGroup: Optional[WeightPerAxleGroup] = None
    MaxWidth: Optional[int] = None
    Occupancy: Optional[RouteNoticeDetailRange] = None
    RestrictedTimes: Optional[str] = None
    TimeDependent: Optional[bool] = None
    TrailerCount: Optional[RouteNoticeDetailRange] = None
    TravelMode: Optional[bool] = None
    TruckRoadType: Optional[str] = None
    TruckType: Optional[RouteTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None


class WaypointOptimizationAccessHours(BaseValidatorModel):
    From: WaypointOptimizationAccessHoursEntry
    To: WaypointOptimizationAccessHoursEntry


class WaypointOptimizationAvoidanceArea(BaseValidatorModel):
    Geometry: WaypointOptimizationAvoidanceAreaGeometry


class WaypointOptimizationClusteringOptions(BaseValidatorModel):
    Algorithm: WaypointOptimizationClusteringAlgorithmType
    DrivingDistanceOptions: Optional[WaypointOptimizationDrivingDistanceOptions] = None


class WaypointOptimizationImpedingWaypoint(BaseValidatorModel):
    FailedConstraints: List[WaypointOptimizationFailedConstraint]
    Id: str
    Position: List[float]


class WaypointOptimizationRestCycles(BaseValidatorModel):
    LongCycle: WaypointOptimizationRestCycleDurations
    ShortCycle: WaypointOptimizationRestCycleDurations


class WaypointOptimizationTruckOptions(BaseValidatorModel):
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[List[WaypointOptimizationHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    Length: Optional[int] = None
    Trailer: Optional[WaypointOptimizationTrailerOptions] = None
    TruckType: Optional[WaypointOptimizationTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None
    WeightPerAxle: Optional[int] = None
    Width: Optional[int] = None


class IsolineAvoidanceArea(BaseValidatorModel):
    Geometry: IsolineAvoidanceAreaGeometry
    Except: Optional[List[IsolineAvoidanceAreaGeometry]] = None


class RouteAvoidanceArea(BaseValidatorModel):
    Geometry: RouteAvoidanceAreaGeometry
    Except: Optional[List[RouteAvoidanceAreaGeometry]] = None


class Isoline(BaseValidatorModel):
    Connections: List[IsolineConnection]
    Geometries: List[IsolineShapeGeometry]
    DistanceThreshold: Optional[int] = None
    TimeThreshold: Optional[int] = None


class IsolineTravelModeOptions(BaseValidatorModel):
    Car: Optional[IsolineCarOptions] = None
    Scooter: Optional[IsolineScooterOptions] = None
    Truck: Optional[IsolineTruckOptions] = None


class RoadSnapTravelModeOptions(BaseValidatorModel):
    Truck: Optional[RoadSnapTruckOptions] = None


class RouteSignpost(BaseValidatorModel):
    Labels: List[RouteSignpostLabel]


class RouteMatrixBoundaryOutput(BaseValidatorModel):
    Geometry: Optional[RouteMatrixBoundaryGeometryOutput] = None
    Unbounded: Optional[bool] = None


class RouteMatrixBoundary(BaseValidatorModel):
    Geometry: Optional[RouteMatrixBoundaryGeometry] = None
    Unbounded: Optional[bool] = None


class RouteMatrixAvoidanceOptions(BaseValidatorModel):
    Areas: Optional[List[RouteMatrixAvoidanceArea]] = None
    CarShuttleTrains: Optional[bool] = None
    ControlledAccessHighways: Optional[bool] = None
    DirtRoads: Optional[bool] = None
    Ferries: Optional[bool] = None
    TollRoads: Optional[bool] = None
    TollTransponders: Optional[bool] = None
    TruckRoadTypes: Optional[List[str]] = None
    Tunnels: Optional[bool] = None
    UTurns: Optional[bool] = None
    ZoneCategories: Optional[List[RouteMatrixAvoidanceZoneCategory]] = None


class RouteMatrixDestination(BaseValidatorModel):
    Position: List[float]
    Options: Optional[RouteMatrixDestinationOptions] = None


class RouteMatrixOrigin(BaseValidatorModel):
    Position: List[float]
    Options: Optional[RouteMatrixOriginOptions] = None


class RouteMatrixTravelModeOptions(BaseValidatorModel):
    Car: Optional[RouteMatrixCarOptions] = None
    Scooter: Optional[RouteMatrixScooterOptions] = None
    Truck: Optional[RouteMatrixTruckOptions] = None


class RouteFerryLegDetails(BaseValidatorModel):
    AfterTravelSteps: List[RouteFerryAfterTravelStep]
    Arrival: RouteFerryArrival
    BeforeTravelSteps: List[RouteFerryBeforeTravelStep]
    Departure: RouteFerryDeparture
    Notices: List[RouteFerryNotice]
    PassThroughWaypoints: List[RoutePassThroughWaypoint]
    Spans: List[RouteFerrySpan]
    TravelSteps: List[RouteFerryTravelStep]
    RouteName: Optional[str] = None
    Summary: Optional[RouteFerrySummary] = None


class RouteTollSummary(BaseValidatorModel):
    Total: Optional[RouteTollPriceSummary] = None


class RouteTollRate(BaseValidatorModel):
    Id: str
    LocalPrice: RouteTollPrice
    Name: str
    PaymentMethods: List[RouteTollPaymentMethodType]
    Transponders: List[RouteTransponder]
    ApplicableTimes: Optional[str] = None
    ConvertedPrice: Optional[RouteTollPrice] = None
    Pass: Optional[RouteTollPass] = None


class RouteTravelModeOptions(BaseValidatorModel):
    Car: Optional[RouteCarOptions] = None
    Pedestrian: Optional[RoutePedestrianOptions] = None
    Scooter: Optional[RouteScooterOptions] = None
    Truck: Optional[RouteTruckOptions] = None


class RouteVehicleNoticeDetail(BaseValidatorModel):
    Title: Optional[str] = None
    ViolatedConstraints: Optional[RouteViolatedConstraints] = None


class WaypointOptimizationDestinationOptions(BaseValidatorModel):
    AccessHours: Optional[WaypointOptimizationAccessHours] = None
    AppointmentTime: Optional[str] = None
    Heading: Optional[float] = None
    Id: Optional[str] = None
    ServiceDuration: Optional[int] = None
    SideOfStreet: Optional[WaypointOptimizationSideOfStreetOptions] = None


class WaypointOptimizationWaypoint(BaseValidatorModel):
    Position: List[float]
    AccessHours: Optional[WaypointOptimizationAccessHours] = None
    AppointmentTime: Optional[str] = None
    Before: Optional[List[int]] = None
    Heading: Optional[float] = None
    Id: Optional[str] = None
    ServiceDuration: Optional[int] = None
    SideOfStreet: Optional[WaypointOptimizationSideOfStreetOptions] = None


class WaypointOptimizationAvoidanceOptions(BaseValidatorModel):
    Areas: Optional[List[WaypointOptimizationAvoidanceArea]] = None
    CarShuttleTrains: Optional[bool] = None
    ControlledAccessHighways: Optional[bool] = None
    DirtRoads: Optional[bool] = None
    Ferries: Optional[bool] = None
    TollRoads: Optional[bool] = None
    Tunnels: Optional[bool] = None
    UTurns: Optional[bool] = None


# This class is the output for the 'optimize_waypoints' function.
class OptimizeWaypointsResponse(BaseValidatorModel):
    Connections: List[WaypointOptimizationConnection]
    Distance: int
    Duration: int
    ImpedingWaypoints: List[WaypointOptimizationImpedingWaypoint]
    OptimizedWaypoints: List[WaypointOptimizationOptimizedWaypoint]
    PricingBucket: str
    TimeBreakdown: WaypointOptimizationTimeBreakdown
    ResponseMetadata: ResponseMetadata


class WaypointOptimizationDriverOptions(BaseValidatorModel):
    RestCycles: Optional[WaypointOptimizationRestCycles] = None
    RestProfile: Optional[WaypointOptimizationRestProfile] = None
    TreatServiceTimeAs: Optional[WaypointOptimizationServiceTimeTreatmentType] = None


class WaypointOptimizationTravelModeOptions(BaseValidatorModel):
    Pedestrian: Optional[WaypointOptimizationPedestrianOptions] = None
    Truck: Optional[WaypointOptimizationTruckOptions] = None


class IsolineAvoidanceOptions(BaseValidatorModel):
    Areas: Optional[List[IsolineAvoidanceArea]] = None
    CarShuttleTrains: Optional[bool] = None
    ControlledAccessHighways: Optional[bool] = None
    DirtRoads: Optional[bool] = None
    Ferries: Optional[bool] = None
    SeasonalClosure: Optional[bool] = None
    TollRoads: Optional[bool] = None
    TollTransponders: Optional[bool] = None
    TruckRoadTypes: Optional[List[str]] = None
    Tunnels: Optional[bool] = None
    UTurns: Optional[bool] = None
    ZoneCategories: Optional[List[IsolineAvoidanceZoneCategory]] = None


class RouteAvoidanceOptions(BaseValidatorModel):
    Areas: Optional[List[RouteAvoidanceArea]] = None
    CarShuttleTrains: Optional[bool] = None
    ControlledAccessHighways: Optional[bool] = None
    DirtRoads: Optional[bool] = None
    Ferries: Optional[bool] = None
    SeasonalClosure: Optional[bool] = None
    TollRoads: Optional[bool] = None
    TollTransponders: Optional[bool] = None
    TruckRoadTypes: Optional[List[str]] = None
    Tunnels: Optional[bool] = None
    UTurns: Optional[bool] = None
    ZoneCategories: Optional[List[RouteAvoidanceZoneCategory]] = None


# This class is the output for the 'calculate_isolines' function.
class CalculateIsolinesResponse(BaseValidatorModel):
    ArrivalTime: str
    DepartureTime: str
    IsolineGeometryFormat: GeometryFormatType
    Isolines: List[Isoline]
    PricingBucket: str
    SnappedDestination: List[float]
    SnappedOrigin: List[float]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'snap_to_roads' function.
class SnapToRoadsRequest(BaseValidatorModel):
    TracePoints: List[RoadSnapTracePoint]
    Key: Optional[str] = None
    SnappedGeometryFormat: Optional[GeometryFormatType] = None
    SnapRadius: Optional[int] = None
    TravelMode: Optional[RoadSnapTravelModeType] = None
    TravelModeOptions: Optional[RoadSnapTravelModeOptions] = None


class RoutePedestrianTravelStep(BaseValidatorModel):
    Duration: int
    Type: RoutePedestrianTravelStepTypeType
    ContinueStepDetails: Optional[RouteContinueStepDetails] = None
    CurrentRoad: Optional[RouteRoad] = None
    Distance: Optional[int] = None
    ExitNumber: Optional[List[LocalizedString]] = None
    GeometryOffset: Optional[int] = None
    Instruction: Optional[str] = None
    KeepStepDetails: Optional[RouteKeepStepDetails] = None
    NextRoad: Optional[RouteRoad] = None
    RoundaboutEnterStepDetails: Optional[RouteRoundaboutEnterStepDetails] = None
    RoundaboutExitStepDetails: Optional[RouteRoundaboutExitStepDetails] = None
    RoundaboutPassStepDetails: Optional[RouteRoundaboutPassStepDetails] = None
    Signpost: Optional[RouteSignpost] = None
    TurnStepDetails: Optional[RouteTurnStepDetails] = None


class RouteVehicleTravelStep(BaseValidatorModel):
    Duration: int
    Type: RouteVehicleTravelStepTypeType
    ContinueHighwayStepDetails: Optional[RouteContinueHighwayStepDetails] = None
    ContinueStepDetails: Optional[RouteContinueStepDetails] = None
    CurrentRoad: Optional[RouteRoad] = None
    Distance: Optional[int] = None
    EnterHighwayStepDetails: Optional[RouteEnterHighwayStepDetails] = None
    ExitNumber: Optional[List[LocalizedString]] = None
    ExitStepDetails: Optional[RouteExitStepDetails] = None
    GeometryOffset: Optional[int] = None
    Instruction: Optional[str] = None
    KeepStepDetails: Optional[RouteKeepStepDetails] = None
    NextRoad: Optional[RouteRoad] = None
    RampStepDetails: Optional[RouteRampStepDetails] = None
    RoundaboutEnterStepDetails: Optional[RouteRoundaboutEnterStepDetails] = None
    RoundaboutExitStepDetails: Optional[RouteRoundaboutExitStepDetails] = None
    RoundaboutPassStepDetails: Optional[RouteRoundaboutPassStepDetails] = None
    Signpost: Optional[RouteSignpost] = None
    TurnStepDetails: Optional[RouteTurnStepDetails] = None
    UTurnStepDetails: Optional[RouteUTurnStepDetails] = None


# This class is the output for the 'calculate_route_matrix' function.
class CalculateRouteMatrixResponse(BaseValidatorModel):
    ErrorCount: int
    PricingBucket: str
    RouteMatrix: List[List[RouteMatrixEntry]]
    RoutingBoundary: RouteMatrixBoundaryOutput
    ResponseMetadata: ResponseMetadata

RouteMatrixBoundaryUnion = Union[RouteMatrixBoundary, RouteMatrixBoundaryOutput]


class RouteSummary(BaseValidatorModel):
    Distance: Optional[int] = None
    Duration: Optional[int] = None
    Tolls: Optional[RouteTollSummary] = None


class RouteToll(BaseValidatorModel):
    PaymentSites: List[RouteTollPaymentSite]
    Rates: List[RouteTollRate]
    Systems: List[int]
    Country: Optional[str] = None


class RouteVehicleNotice(BaseValidatorModel):
    Code: RouteVehicleNoticeCodeType
    Details: List[RouteVehicleNoticeDetail]
    Impact: Optional[RouteNoticeImpactType] = None


# This class is the input for the 'optimize_waypoints' function.
class OptimizeWaypointsRequest(BaseValidatorModel):
    Origin: List[float]
    Avoid: Optional[WaypointOptimizationAvoidanceOptions] = None
    Clustering: Optional[WaypointOptimizationClusteringOptions] = None
    DepartureTime: Optional[str] = None
    Destination: Optional[List[float]] = None
    DestinationOptions: Optional[WaypointOptimizationDestinationOptions] = None
    Driver: Optional[WaypointOptimizationDriverOptions] = None
    Exclude: Optional[WaypointOptimizationExclusionOptions] = None
    Key: Optional[str] = None
    OptimizeSequencingFor: Optional[WaypointOptimizationSequencingObjectiveType] = None
    OriginOptions: Optional[WaypointOptimizationOriginOptions] = None
    Traffic: Optional[WaypointOptimizationTrafficOptions] = None
    TravelMode: Optional[WaypointOptimizationTravelModeType] = None
    TravelModeOptions: Optional[WaypointOptimizationTravelModeOptions] = None
    Waypoints: Optional[List[WaypointOptimizationWaypoint]] = None


# This class is the input for the 'calculate_isolines' function.
class CalculateIsolinesRequest(BaseValidatorModel):
    Thresholds: IsolineThresholds
    Allow: Optional[IsolineAllowOptions] = None
    ArrivalTime: Optional[str] = None
    Avoid: Optional[IsolineAvoidanceOptions] = None
    DepartNow: Optional[bool] = None
    DepartureTime: Optional[str] = None
    Destination: Optional[List[float]] = None
    DestinationOptions: Optional[IsolineDestinationOptions] = None
    IsolineGeometryFormat: Optional[GeometryFormatType] = None
    IsolineGranularity: Optional[IsolineGranularityOptions] = None
    Key: Optional[str] = None
    OptimizeIsolineFor: Optional[IsolineOptimizationObjectiveType] = None
    OptimizeRoutingFor: Optional[RoutingObjectiveType] = None
    Origin: Optional[List[float]] = None
    OriginOptions: Optional[IsolineOriginOptions] = None
    Traffic: Optional[IsolineTrafficOptions] = None
    TravelMode: Optional[IsolineTravelModeType] = None
    TravelModeOptions: Optional[IsolineTravelModeOptions] = None


# This class is the input for the 'calculate_routes' function.
class CalculateRoutesRequest(BaseValidatorModel):
    Destination: List[float]
    Origin: List[float]
    Allow: Optional[RouteAllowOptions] = None
    ArrivalTime: Optional[str] = None
    Avoid: Optional[RouteAvoidanceOptions] = None
    DepartNow: Optional[bool] = None
    DepartureTime: Optional[str] = None
    DestinationOptions: Optional[RouteDestinationOptions] = None
    Driver: Optional[RouteDriverOptions] = None
    Exclude: Optional[RouteExclusionOptions] = None
    InstructionsMeasurementSystem: Optional[MeasurementSystemType] = None
    Key: Optional[str] = None
    Languages: Optional[List[str]] = None
    LegAdditionalFeatures: Optional[List[RouteLegAdditionalFeatureType]] = None
    LegGeometryFormat: Optional[GeometryFormatType] = None
    MaxAlternatives: Optional[int] = None
    OptimizeRoutingFor: Optional[RoutingObjectiveType] = None
    OriginOptions: Optional[RouteOriginOptions] = None
    SpanAdditionalFeatures: Optional[List[RouteSpanAdditionalFeatureType]] = None
    Tolls: Optional[RouteTollOptions] = None
    Traffic: Optional[RouteTrafficOptions] = None
    TravelMode: Optional[RouteTravelModeType] = None
    TravelModeOptions: Optional[RouteTravelModeOptions] = None
    TravelStepType: Optional[RouteTravelStepTypeType] = None
    Waypoints: Optional[List[RouteWaypoint]] = None


class RoutePedestrianLegDetails(BaseValidatorModel):
    Arrival: RoutePedestrianArrival
    Departure: RoutePedestrianDeparture
    Notices: List[RoutePedestrianNotice]
    PassThroughWaypoints: List[RoutePassThroughWaypoint]
    Spans: List[RoutePedestrianSpan]
    TravelSteps: List[RoutePedestrianTravelStep]
    Summary: Optional[RoutePedestrianSummary] = None


# This class is the input for the 'calculate_route_matrix' function.
class CalculateRouteMatrixRequest(BaseValidatorModel):
    Destinations: List[RouteMatrixDestination]
    Origins: List[RouteMatrixOrigin]
    RoutingBoundary: RouteMatrixBoundaryUnion
    Allow: Optional[RouteMatrixAllowOptions] = None
    Avoid: Optional[RouteMatrixAvoidanceOptions] = None
    DepartNow: Optional[bool] = None
    DepartureTime: Optional[str] = None
    Exclude: Optional[RouteMatrixExclusionOptions] = None
    Key: Optional[str] = None
    OptimizeRoutingFor: Optional[RoutingObjectiveType] = None
    Traffic: Optional[RouteMatrixTrafficOptions] = None
    TravelMode: Optional[RouteMatrixTravelModeType] = None
    TravelModeOptions: Optional[RouteMatrixTravelModeOptions] = None


class RouteVehicleLegDetails(BaseValidatorModel):
    Arrival: RouteVehicleArrival
    Departure: RouteVehicleDeparture
    Incidents: List[RouteVehicleIncident]
    Notices: List[RouteVehicleNotice]
    PassThroughWaypoints: List[RoutePassThroughWaypoint]
    Spans: List[RouteVehicleSpan]
    Tolls: List[RouteToll]
    TollSystems: List[RouteTollSystem]
    TravelSteps: List[RouteVehicleTravelStep]
    TruckRoadTypes: List[str]
    Zones: List[RouteZone]
    Summary: Optional[RouteVehicleSummary] = None


class RouteLeg(BaseValidatorModel):
    Geometry: RouteLegGeometry
    TravelMode: RouteLegTravelModeType
    Type: RouteLegTypeType
    FerryLegDetails: Optional[RouteFerryLegDetails] = None
    Language: Optional[str] = None
    PedestrianLegDetails: Optional[RoutePedestrianLegDetails] = None
    VehicleLegDetails: Optional[RouteVehicleLegDetails] = None


class Route(BaseValidatorModel):
    Legs: List[RouteLeg]
    MajorRoadLabels: List[RouteMajorRoadLabel]
    Summary: Optional[RouteSummary] = None


# This class is the output for the 'calculate_routes' function.
class CalculateRoutesResponse(BaseValidatorModel):
    LegGeometryFormat: GeometryFormatType
    Notices: List[RouteResponseNotice]
    PricingBucket: str
    Routes: List[Route]
    ResponseMetadata: ResponseMetadata