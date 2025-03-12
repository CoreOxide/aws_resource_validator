from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.geo_routes_constants import *

class IsolineAllowOptionsTypeDef(BaseValidatorModel):
    Hot: Optional[bool] = None
    Hov: Optional[bool] = None


class IsolineGranularityOptionsTypeDef(BaseValidatorModel):
    MaxPoints: Optional[int] = None
    MaxResolution: Optional[int] = None


class IsolineThresholdsTypeDef(BaseValidatorModel):
    Distance: Optional[Sequence[int]] = None
    Time: Optional[Sequence[int]] = None


class IsolineTrafficOptionsTypeDef(BaseValidatorModel):
    FlowEventThresholdOverride: Optional[int] = None
    Usage: Optional[TrafficUsageType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RouteMatrixAllowOptionsTypeDef(BaseValidatorModel):
    Hot: Optional[bool] = None
    Hov: Optional[bool] = None


class RouteMatrixExclusionOptionsTypeDef(BaseValidatorModel):
    Countries: Sequence[str]


class RouteMatrixTrafficOptionsTypeDef(BaseValidatorModel):
    FlowEventThresholdOverride: Optional[int] = None
    Usage: Optional[TrafficUsageType] = None


class RouteMatrixEntryTypeDef(BaseValidatorModel):
    Distance: int
    Duration: int
    Error: Optional[RouteMatrixErrorCodeType] = None


class RouteAllowOptionsTypeDef(BaseValidatorModel):
    Hot: Optional[bool] = None
    Hov: Optional[bool] = None


class RouteExclusionOptionsTypeDef(BaseValidatorModel):
    Countries: Sequence[str]


class RouteTrafficOptionsTypeDef(BaseValidatorModel):
    FlowEventThresholdOverride: Optional[int] = None
    Usage: Optional[TrafficUsageType] = None


class RouteResponseNoticeTypeDef(BaseValidatorModel):
    Code: RouteResponseNoticeCodeType
    Impact: Optional[RouteNoticeImpactType] = None


class CircleOutputTypeDef(BaseValidatorModel):
    Center: List[float]
    Radius: float


class CircleTypeDef(BaseValidatorModel):
    Center: Sequence[float]
    Radius: float


class CorridorTypeDef(BaseValidatorModel):
    LineString: Sequence[Sequence[float]]
    Radius: int


class PolylineCorridorTypeDef(BaseValidatorModel):
    Polyline: str
    Radius: int


class IsolineAvoidanceZoneCategoryTypeDef(BaseValidatorModel):
    Category: Optional[IsolineZoneCategoryType] = None


class IsolineVehicleLicensePlateTypeDef(BaseValidatorModel):
    LastCharacter: Optional[str] = None


class IsolineConnectionGeometryTypeDef(BaseValidatorModel):
    LineString: Optional[List[List[float]]] = None
    Polyline: Optional[str] = None


class IsolineMatchingOptionsTypeDef(BaseValidatorModel):
    NameHint: Optional[str] = None
    OnRoadThreshold: Optional[int] = None
    Radius: Optional[int] = None
    Strategy: Optional[MatchingStrategyType] = None


class IsolineSideOfStreetOptionsTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    UseWith: Optional[SideOfStreetMatchingStrategyType] = None


class IsolineShapeGeometryTypeDef(BaseValidatorModel):
    Polygon: Optional[List[List[List[float]]]] = None
    PolylinePolygon: Optional[List[str]] = None


class IsolineTrailerOptionsTypeDef(BaseValidatorModel):
    AxleCount: Optional[int] = None
    TrailerCount: Optional[int] = None


class WeightPerAxleGroupTypeDef(BaseValidatorModel):
    Single: Optional[int] = None
    Tandem: Optional[int] = None
    Triple: Optional[int] = None
    Quad: Optional[int] = None
    Quint: Optional[int] = None


class LocalizedStringTypeDef(BaseValidatorModel):
    Value: str
    Language: Optional[str] = None


class WaypointOptimizationExclusionOptionsTypeDef(BaseValidatorModel):
    Countries: Sequence[str]


class WaypointOptimizationOriginOptionsTypeDef(BaseValidatorModel):
    Id: Optional[str] = None


class WaypointOptimizationTrafficOptionsTypeDef(BaseValidatorModel):
    Usage: Optional[TrafficUsageType] = None


class WaypointOptimizationConnectionTypeDef(BaseValidatorModel):
    Distance: int
    From: str
    RestDuration: int
    To: str
    TravelDuration: int
    WaitDuration: int


class WaypointOptimizationOptimizedWaypointTypeDef(BaseValidatorModel):
    DepartureTime: str
    Id: str
    Position: List[float]
    ArrivalTime: Optional[str] = None
    ClusterIndex: Optional[int] = None


class WaypointOptimizationTimeBreakdownTypeDef(BaseValidatorModel):
    RestDuration: int
    ServiceDuration: int
    TravelDuration: int
    WaitDuration: int


class RoadSnapNoticeTypeDef(BaseValidatorModel):
    Code: RoadSnapNoticeCodeType
    Title: str
    TracePointIndexes: List[int]


class RoadSnapSnappedGeometryTypeDef(BaseValidatorModel):
    LineString: Optional[List[List[float]]] = None
    Polyline: Optional[str] = None


class RoadSnapSnappedTracePointTypeDef(BaseValidatorModel):
    Confidence: float
    OriginalPosition: List[float]
    SnappedPosition: List[float]


class RoadSnapTracePointTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    Heading: Optional[float] = None
    Speed: Optional[float] = None
    Timestamp: Optional[str] = None


class RoadSnapTrailerOptionsTypeDef(BaseValidatorModel):
    TrailerCount: Optional[int] = None


class RouteAvoidanceZoneCategoryTypeDef(BaseValidatorModel):
    Category: RouteZoneCategoryType


class RouteVehicleLicensePlateTypeDef(BaseValidatorModel):
    LastCharacter: Optional[str] = None


class RouteMatchingOptionsTypeDef(BaseValidatorModel):
    NameHint: Optional[str] = None
    OnRoadThreshold: Optional[int] = None
    Radius: Optional[int] = None
    Strategy: Optional[MatchingStrategyType] = None


class RouteSideOfStreetOptionsTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    UseWith: Optional[SideOfStreetMatchingStrategyType] = None


class RouteDriverScheduleIntervalTypeDef(BaseValidatorModel):
    DriveDuration: int
    RestDuration: int


class RouteFerryPlaceTypeDef(BaseValidatorModel):
    Position: List[float]
    Name: Optional[str] = None
    OriginalPosition: Optional[List[float]] = None
    WaypointIndex: Optional[int] = None


class RouteFerryNoticeTypeDef(BaseValidatorModel):
    Code: RouteFerryNoticeCodeType
    Impact: Optional[RouteNoticeImpactType] = None


class RouteFerryOverviewSummaryTypeDef(BaseValidatorModel):
    Distance: int
    Duration: int


class RouteFerryTravelOnlySummaryTypeDef(BaseValidatorModel):
    Duration: int


class RouteLegGeometryTypeDef(BaseValidatorModel):
    LineString: Optional[List[List[float]]] = None
    Polyline: Optional[str] = None


class RouteNumberTypeDef(BaseValidatorModel):
    Value: str
    Direction: Optional[RouteDirectionType] = None
    Language: Optional[str] = None


class RouteMatrixAutoCircleTypeDef(BaseValidatorModel):
    Margin: Optional[int] = None
    MaxRadius: Optional[int] = None


class RouteMatrixAvoidanceAreaGeometryTypeDef(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None
    PolylinePolygon: Optional[Sequence[str]] = None


class RouteMatrixAvoidanceZoneCategoryTypeDef(BaseValidatorModel):
    Category: Optional[RouteMatrixZoneCategoryType] = None


class RouteMatrixVehicleLicensePlateTypeDef(BaseValidatorModel):
    LastCharacter: Optional[str] = None


class RouteMatrixMatchingOptionsTypeDef(BaseValidatorModel):
    NameHint: Optional[str] = None
    OnRoadThreshold: Optional[int] = None
    Radius: Optional[int] = None
    Strategy: Optional[MatchingStrategyType] = None


class RouteMatrixSideOfStreetOptionsTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    UseWith: Optional[SideOfStreetMatchingStrategyType] = None


class RouteMatrixTrailerOptionsTypeDef(BaseValidatorModel):
    TrailerCount: Optional[int] = None


class RouteNoticeDetailRangeTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class RoutePassThroughPlaceTypeDef(BaseValidatorModel):
    Position: List[float]
    OriginalPosition: Optional[List[float]] = None
    WaypointIndex: Optional[int] = None


class RoutePedestrianPlaceTypeDef(BaseValidatorModel):
    Position: List[float]
    Name: Optional[str] = None
    OriginalPosition: Optional[List[float]] = None
    SideOfStreet: Optional[RouteSideOfStreetType] = None
    WaypointIndex: Optional[int] = None


class RoutePedestrianNoticeTypeDef(BaseValidatorModel):
    Code: RoutePedestrianNoticeCodeType
    Impact: Optional[RouteNoticeImpactType] = None


class RoutePedestrianOptionsTypeDef(BaseValidatorModel):
    Speed: Optional[float] = None


class RoutePedestrianOverviewSummaryTypeDef(BaseValidatorModel):
    Distance: int
    Duration: int


class RouteSpanDynamicSpeedDetailsTypeDef(BaseValidatorModel):
    BestCaseSpeed: Optional[float] = None
    TurnDuration: Optional[int] = None
    TypicalSpeed: Optional[float] = None


class RouteSpanSpeedLimitDetailsTypeDef(BaseValidatorModel):
    MaxSpeed: Optional[float] = None
    Unlimited: Optional[bool] = None


class RoutePedestrianTravelOnlySummaryTypeDef(BaseValidatorModel):
    Duration: int


class RouteTollPassValidityPeriodTypeDef(BaseValidatorModel):
    Period: RouteTollPassValidityPeriodTypeType
    PeriodCount: Optional[int] = None


class RouteTollPaymentSiteTypeDef(BaseValidatorModel):
    Position: List[float]
    Name: Optional[str] = None


class RouteTollPriceValueRangeTypeDef(BaseValidatorModel):
    Min: float
    Max: float


class RouteTransponderTypeDef(BaseValidatorModel):
    SystemName: Optional[str] = None


class RouteTollSystemTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class RouteTrailerOptionsTypeDef(BaseValidatorModel):
    AxleCount: Optional[int] = None
    TrailerCount: Optional[int] = None


class RouteVehiclePlaceTypeDef(BaseValidatorModel):
    Position: List[float]
    Name: Optional[str] = None
    OriginalPosition: Optional[List[float]] = None
    SideOfStreet: Optional[RouteSideOfStreetType] = None
    WaypointIndex: Optional[int] = None


class RouteZoneTypeDef(BaseValidatorModel):
    Category: Optional[RouteZoneCategoryType] = None
    Name: Optional[str] = None


class RouteVehicleOverviewSummaryTypeDef(BaseValidatorModel):
    Distance: int
    Duration: int
    BestCaseDuration: Optional[int] = None
    TypicalDuration: Optional[int] = None


class RouteVehicleTravelOnlySummaryTypeDef(BaseValidatorModel):
    Duration: int
    BestCaseDuration: Optional[int] = None
    TypicalDuration: Optional[int] = None


class WaypointOptimizationAccessHoursEntryTypeDef(BaseValidatorModel):
    DayOfWeek: DayOfWeekType
    TimeOfDay: str


class WaypointOptimizationAvoidanceAreaGeometryTypeDef(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None


class WaypointOptimizationDrivingDistanceOptionsTypeDef(BaseValidatorModel):
    DrivingDistance: int


class WaypointOptimizationSideOfStreetOptionsTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    UseWith: Optional[SideOfStreetMatchingStrategyType] = None


class WaypointOptimizationRestProfileTypeDef(BaseValidatorModel):
    Profile: str


class WaypointOptimizationFailedConstraintTypeDef(BaseValidatorModel):
    Constraint: Optional[WaypointOptimizationConstraintType] = None
    Reason: Optional[str] = None


class WaypointOptimizationPedestrianOptionsTypeDef(BaseValidatorModel):
    Speed: Optional[float] = None


class WaypointOptimizationRestCycleDurationsTypeDef(BaseValidatorModel):
    RestDuration: int
    WorkDuration: int


class WaypointOptimizationTrailerOptionsTypeDef(BaseValidatorModel):
    TrailerCount: Optional[int] = None


class IsolineAvoidanceAreaGeometryTypeDef(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    Corridor: Optional[CorridorTypeDef] = None
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None
    PolylineCorridor: Optional[PolylineCorridorTypeDef] = None
    PolylinePolygon: Optional[Sequence[str]] = None


class RouteAvoidanceAreaGeometryTypeDef(BaseValidatorModel):
    Corridor: Optional[CorridorTypeDef] = None
    BoundingBox: Optional[Sequence[float]] = None
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None
    PolylineCorridor: Optional[PolylineCorridorTypeDef] = None
    PolylinePolygon: Optional[Sequence[str]] = None


class IsolineCarOptionsTypeDef(BaseValidatorModel):
    EngineType: Optional[IsolineEngineTypeType] = None
    LicensePlate: Optional[IsolineVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class IsolineScooterOptionsTypeDef(BaseValidatorModel):
    EngineType: Optional[IsolineEngineTypeType] = None
    LicensePlate: Optional[IsolineVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class IsolineConnectionTypeDef(BaseValidatorModel):
    FromPolygonIndex: int
    Geometry: IsolineConnectionGeometryTypeDef
    ToPolygonIndex: int


class IsolineDestinationOptionsTypeDef(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    Heading: Optional[float] = None
    Matching: Optional[IsolineMatchingOptionsTypeDef] = None
    SideOfStreet: Optional[IsolineSideOfStreetOptionsTypeDef] = None


class IsolineOriginOptionsTypeDef(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    Heading: Optional[float] = None
    Matching: Optional[IsolineMatchingOptionsTypeDef] = None
    SideOfStreet: Optional[IsolineSideOfStreetOptionsTypeDef] = None


class IsolineTruckOptionsTypeDef(BaseValidatorModel):
    AxleCount: Optional[int] = None
    EngineType: Optional[IsolineEngineTypeType] = None
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[Sequence[IsolineHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    HeightAboveFirstAxle: Optional[int] = None
    KpraLength: Optional[int] = None
    Length: Optional[int] = None
    LicensePlate: Optional[IsolineVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None
    PayloadCapacity: Optional[int] = None
    TireCount: Optional[int] = None
    Trailer: Optional[IsolineTrailerOptionsTypeDef] = None
    TruckType: Optional[IsolineTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None
    WeightPerAxle: Optional[int] = None
    WeightPerAxleGroup: Optional[WeightPerAxleGroupTypeDef] = None
    Width: Optional[int] = None


class RouteContinueHighwayStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteContinueStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]


class RouteEnterHighwayStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteExitStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    RelativeExit: Optional[int] = None
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteFerrySpanTypeDef(BaseValidatorModel):
    Country: Optional[str] = None
    Distance: Optional[int] = None
    Duration: Optional[int] = None
    GeometryOffset: Optional[int] = None
    Names: Optional[List[LocalizedStringTypeDef]] = None
    Region: Optional[str] = None


class RouteKeepStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteRampStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteRoundaboutEnterStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteRoundaboutExitStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    RelativeExit: Optional[int] = None
    RoundaboutAngle: Optional[float] = None
    SteeringDirection: Optional[RouteSteeringDirectionType] = None


class RouteRoundaboutPassStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteTurnStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class RouteUTurnStepDetailsTypeDef(BaseValidatorModel):
    Intersection: List[LocalizedStringTypeDef]
    SteeringDirection: Optional[RouteSteeringDirectionType] = None
    TurnAngle: Optional[float] = None
    TurnIntensity: Optional[RouteTurnIntensityType] = None


class SnapToRoadsResponseTypeDef(BaseValidatorModel):
    Notices: List[RoadSnapNoticeTypeDef]
    PricingBucket: str
    SnappedGeometry: RoadSnapSnappedGeometryTypeDef
    SnappedGeometryFormat: GeometryFormatType
    SnappedTracePoints: List[RoadSnapSnappedTracePointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RoadSnapTruckOptionsTypeDef(BaseValidatorModel):
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[Sequence[RoadSnapHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    Length: Optional[int] = None
    Trailer: Optional[RoadSnapTrailerOptionsTypeDef] = None
    TunnelRestrictionCode: Optional[str] = None
    Width: Optional[int] = None


class RouteCarOptionsTypeDef(BaseValidatorModel):
    EngineType: Optional[RouteEngineTypeType] = None
    LicensePlate: Optional[RouteVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class RouteScooterOptionsTypeDef(BaseValidatorModel):
    EngineType: Optional[RouteEngineTypeType] = None
    LicensePlate: Optional[RouteVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class RouteDestinationOptionsTypeDef(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    AvoidUTurns: Optional[bool] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatchingOptionsTypeDef] = None
    SideOfStreet: Optional[RouteSideOfStreetOptionsTypeDef] = None
    StopDuration: Optional[int] = None


class RouteOriginOptionsTypeDef(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    AvoidUTurns: Optional[bool] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatchingOptionsTypeDef] = None
    SideOfStreet: Optional[RouteSideOfStreetOptionsTypeDef] = None


class RouteWaypointTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    AvoidActionsForDistance: Optional[int] = None
    AvoidUTurns: Optional[bool] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatchingOptionsTypeDef] = None
    PassThrough: Optional[bool] = None
    SideOfStreet: Optional[RouteSideOfStreetOptionsTypeDef] = None
    StopDuration: Optional[int] = None


class RouteDriverOptionsTypeDef(BaseValidatorModel):
    Schedule: Optional[Sequence[RouteDriverScheduleIntervalTypeDef]] = None


class RouteEmissionTypeTypeDef(BaseValidatorModel):
    pass


class RouteTollOptionsTypeDef(BaseValidatorModel):
    AllTransponders: Optional[bool] = None
    AllVignettes: Optional[bool] = None
    Currency: Optional[str] = None
    EmissionType: Optional[RouteEmissionTypeTypeDef] = None
    VehicleCategory: Optional[Literal["Minibus"]] = None


class RouteFerryArrivalTypeDef(BaseValidatorModel):
    Place: RouteFerryPlaceTypeDef
    Time: Optional[str] = None


class RouteFerryDepartureTypeDef(BaseValidatorModel):
    Place: RouteFerryPlaceTypeDef
    Time: Optional[str] = None


class RouteFerrySummaryTypeDef(BaseValidatorModel):
    Overview: Optional[RouteFerryOverviewSummaryTypeDef] = None
    TravelOnly: Optional[RouteFerryTravelOnlySummaryTypeDef] = None


class RouteMajorRoadLabelTypeDef(BaseValidatorModel):
    RoadName: Optional[LocalizedStringTypeDef] = None
    RouteNumber: Optional[RouteNumberTypeDef] = None


class RouteMatrixBoundaryGeometryOutputTypeDef(BaseValidatorModel):
    AutoCircle: Optional[RouteMatrixAutoCircleTypeDef] = None
    Circle: Optional[CircleOutputTypeDef] = None
    BoundingBox: Optional[List[float]] = None
    Polygon: Optional[List[List[List[float]]]] = None


class RouteMatrixBoundaryGeometryTypeDef(BaseValidatorModel):
    AutoCircle: Optional[RouteMatrixAutoCircleTypeDef] = None
    Circle: Optional[CircleTypeDef] = None
    BoundingBox: Optional[Sequence[float]] = None
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None


class RouteMatrixAvoidanceAreaTypeDef(BaseValidatorModel):
    Geometry: RouteMatrixAvoidanceAreaGeometryTypeDef


class RouteMatrixCarOptionsTypeDef(BaseValidatorModel):
    LicensePlate: Optional[RouteMatrixVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class RouteMatrixScooterOptionsTypeDef(BaseValidatorModel):
    LicensePlate: Optional[RouteMatrixVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None


class RouteMatrixDestinationOptionsTypeDef(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatrixMatchingOptionsTypeDef] = None
    SideOfStreet: Optional[RouteMatrixSideOfStreetOptionsTypeDef] = None


class RouteMatrixOriginOptionsTypeDef(BaseValidatorModel):
    AvoidActionsForDistance: Optional[int] = None
    Heading: Optional[float] = None
    Matching: Optional[RouteMatrixMatchingOptionsTypeDef] = None
    SideOfStreet: Optional[RouteMatrixSideOfStreetOptionsTypeDef] = None


class RouteMatrixTruckOptionsTypeDef(BaseValidatorModel):
    AxleCount: Optional[int] = None
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[Sequence[RouteMatrixHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    KpraLength: Optional[int] = None
    Length: Optional[int] = None
    LicensePlate: Optional[RouteMatrixVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None
    PayloadCapacity: Optional[int] = None
    Trailer: Optional[RouteMatrixTrailerOptionsTypeDef] = None
    TruckType: Optional[RouteMatrixTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None
    WeightPerAxle: Optional[int] = None
    WeightPerAxleGroup: Optional[WeightPerAxleGroupTypeDef] = None
    Width: Optional[int] = None


class RoutePassThroughWaypointTypeDef(BaseValidatorModel):
    Place: RoutePassThroughPlaceTypeDef
    GeometryOffset: Optional[int] = None


class RoutePedestrianArrivalTypeDef(BaseValidatorModel):
    Place: RoutePedestrianPlaceTypeDef
    Time: Optional[str] = None


class RoutePedestrianDepartureTypeDef(BaseValidatorModel):
    Place: RoutePedestrianPlaceTypeDef
    Time: Optional[str] = None


class RoutePedestrianSpanTypeDef(BaseValidatorModel):
    BestCaseDuration: Optional[int] = None
    Country: Optional[str] = None
    Distance: Optional[int] = None
    Duration: Optional[int] = None
    DynamicSpeed: Optional[RouteSpanDynamicSpeedDetailsTypeDef] = None
    FunctionalClassification: Optional[int] = None
    GeometryOffset: Optional[int] = None
    Incidents: Optional[List[int]] = None
    Names: Optional[List[LocalizedStringTypeDef]] = None
    PedestrianAccess: Optional[List[RouteSpanPedestrianAccessAttributeType]] = None
    Region: Optional[str] = None
    RoadAttributes: Optional[List[RouteSpanRoadAttributeType]] = None
    RouteNumbers: Optional[List[RouteNumberTypeDef]] = None
    SpeedLimit: Optional[RouteSpanSpeedLimitDetailsTypeDef] = None
    TypicalDuration: Optional[int] = None


class RouteVehicleSpanTypeDef(BaseValidatorModel):
    BestCaseDuration: Optional[int] = None
    CarAccess: Optional[List[RouteSpanCarAccessAttributeType]] = None
    Country: Optional[str] = None
    Distance: Optional[int] = None
    Duration: Optional[int] = None
    DynamicSpeed: Optional[RouteSpanDynamicSpeedDetailsTypeDef] = None
    FunctionalClassification: Optional[int] = None
    Gate: Optional[RouteSpanGateAttributeType] = None
    GeometryOffset: Optional[int] = None
    Incidents: Optional[List[int]] = None
    Names: Optional[List[LocalizedStringTypeDef]] = None
    Notices: Optional[List[int]] = None
    RailwayCrossing: Optional[RouteSpanRailwayCrossingAttributeType] = None
    Region: Optional[str] = None
    RoadAttributes: Optional[List[RouteSpanRoadAttributeType]] = None
    RouteNumbers: Optional[List[RouteNumberTypeDef]] = None
    ScooterAccess: Optional[List[RouteSpanScooterAccessAttributeType]] = None
    SpeedLimit: Optional[RouteSpanSpeedLimitDetailsTypeDef] = None
    TollSystems: Optional[List[int]] = None
    TruckAccess: Optional[List[RouteSpanTruckAccessAttributeType]] = None
    TruckRoadTypes: Optional[List[int]] = None
    TypicalDuration: Optional[int] = None
    Zones: Optional[List[int]] = None


class RoutePedestrianSummaryTypeDef(BaseValidatorModel):
    Overview: Optional[RoutePedestrianOverviewSummaryTypeDef] = None
    TravelOnly: Optional[RoutePedestrianTravelOnlySummaryTypeDef] = None


class RouteTollPassTypeDef(BaseValidatorModel):
    IncludesReturnTrip: Optional[bool] = None
    SeniorPass: Optional[bool] = None
    TransferCount: Optional[int] = None
    TripCount: Optional[int] = None
    ValidityPeriod: Optional[RouteTollPassValidityPeriodTypeDef] = None


class RouteTollPriceSummaryTypeDef(BaseValidatorModel):
    Currency: str
    Estimate: bool
    Range: bool
    Value: float
    RangeValue: Optional[RouteTollPriceValueRangeTypeDef] = None


class RouteTollPriceTypeDef(BaseValidatorModel):
    Currency: str
    Estimate: bool
    Range: bool
    Value: float
    PerDuration: Optional[int] = None
    RangeValue: Optional[RouteTollPriceValueRangeTypeDef] = None


class RouteTruckOptionsTypeDef(BaseValidatorModel):
    AxleCount: Optional[int] = None
    EngineType: Optional[RouteEngineTypeType] = None
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[Sequence[RouteHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    HeightAboveFirstAxle: Optional[int] = None
    KpraLength: Optional[int] = None
    Length: Optional[int] = None
    LicensePlate: Optional[RouteVehicleLicensePlateTypeDef] = None
    MaxSpeed: Optional[float] = None
    Occupancy: Optional[int] = None
    PayloadCapacity: Optional[int] = None
    TireCount: Optional[int] = None
    Trailer: Optional[RouteTrailerOptionsTypeDef] = None
    TruckType: Optional[RouteTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None
    WeightPerAxle: Optional[int] = None
    WeightPerAxleGroup: Optional[WeightPerAxleGroupTypeDef] = None
    Width: Optional[int] = None


class RouteVehicleArrivalTypeDef(BaseValidatorModel):
    Place: RouteVehiclePlaceTypeDef
    Time: Optional[str] = None


class RouteVehicleDepartureTypeDef(BaseValidatorModel):
    Place: RouteVehiclePlaceTypeDef
    Time: Optional[str] = None


class RouteVehicleSummaryTypeDef(BaseValidatorModel):
    Overview: Optional[RouteVehicleOverviewSummaryTypeDef] = None
    TravelOnly: Optional[RouteVehicleTravelOnlySummaryTypeDef] = None


class RouteWeightConstraintTypeDef(BaseValidatorModel):
    pass


class RouteViolatedConstraintsTypeDef(BaseValidatorModel):
    HazardousCargos: List[RouteHazardousCargoTypeType]
    AllHazardsRestricted: Optional[bool] = None
    AxleCount: Optional[RouteNoticeDetailRangeTypeDef] = None
    MaxHeight: Optional[int] = None
    MaxKpraLength: Optional[int] = None
    MaxLength: Optional[int] = None
    MaxPayloadCapacity: Optional[int] = None
    MaxWeight: Optional[RouteWeightConstraintTypeDef] = None
    MaxWeightPerAxle: Optional[int] = None
    MaxWeightPerAxleGroup: Optional[WeightPerAxleGroupTypeDef] = None
    MaxWidth: Optional[int] = None
    Occupancy: Optional[RouteNoticeDetailRangeTypeDef] = None
    RestrictedTimes: Optional[str] = None
    TimeDependent: Optional[bool] = None
    TrailerCount: Optional[RouteNoticeDetailRangeTypeDef] = None
    TravelMode: Optional[bool] = None
    TruckRoadType: Optional[str] = None
    TruckType: Optional[RouteTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None


class WaypointOptimizationAccessHoursTypeDef(BaseValidatorModel):
    From: WaypointOptimizationAccessHoursEntryTypeDef
    To: WaypointOptimizationAccessHoursEntryTypeDef


class WaypointOptimizationAvoidanceAreaTypeDef(BaseValidatorModel):
    Geometry: WaypointOptimizationAvoidanceAreaGeometryTypeDef


class WaypointOptimizationClusteringOptionsTypeDef(BaseValidatorModel):
    Algorithm: WaypointOptimizationClusteringAlgorithmType
    DrivingDistanceOptions: Optional[WaypointOptimizationDrivingDistanceOptionsTypeDef] = None


class WaypointOptimizationImpedingWaypointTypeDef(BaseValidatorModel):
    FailedConstraints: List[WaypointOptimizationFailedConstraintTypeDef]
    Id: str
    Position: List[float]


class WaypointOptimizationRestCyclesTypeDef(BaseValidatorModel):
    LongCycle: WaypointOptimizationRestCycleDurationsTypeDef
    ShortCycle: WaypointOptimizationRestCycleDurationsTypeDef


class WaypointOptimizationTruckOptionsTypeDef(BaseValidatorModel):
    GrossWeight: Optional[int] = None
    HazardousCargos: Optional[Sequence[WaypointOptimizationHazardousCargoTypeType]] = None
    Height: Optional[int] = None
    Length: Optional[int] = None
    Trailer: Optional[WaypointOptimizationTrailerOptionsTypeDef] = None
    TruckType: Optional[WaypointOptimizationTruckTypeType] = None
    TunnelRestrictionCode: Optional[str] = None
    WeightPerAxle: Optional[int] = None
    Width: Optional[int] = None


class IsolineAvoidanceAreaTypeDef(BaseValidatorModel):
    Geometry: IsolineAvoidanceAreaGeometryTypeDef
    Except: Optional[Sequence[IsolineAvoidanceAreaGeometryTypeDef]] = None


class RouteAvoidanceAreaTypeDef(BaseValidatorModel):
    Geometry: RouteAvoidanceAreaGeometryTypeDef
    Except: Optional[Sequence[RouteAvoidanceAreaGeometryTypeDef]] = None


class IsolineTypeDef(BaseValidatorModel):
    Connections: List[IsolineConnectionTypeDef]
    Geometries: List[IsolineShapeGeometryTypeDef]
    DistanceThreshold: Optional[int] = None
    TimeThreshold: Optional[int] = None


class IsolineTravelModeOptionsTypeDef(BaseValidatorModel):
    Car: Optional[IsolineCarOptionsTypeDef] = None
    Scooter: Optional[IsolineScooterOptionsTypeDef] = None
    Truck: Optional[IsolineTruckOptionsTypeDef] = None


class RoadSnapTravelModeOptionsTypeDef(BaseValidatorModel):
    Truck: Optional[RoadSnapTruckOptionsTypeDef] = None


class RouteSignpostLabelTypeDef(BaseValidatorModel):
    pass


class RouteSignpostTypeDef(BaseValidatorModel):
    Labels: List[RouteSignpostLabelTypeDef]


class RouteMatrixBoundaryOutputTypeDef(BaseValidatorModel):
    Geometry: Optional[RouteMatrixBoundaryGeometryOutputTypeDef] = None
    Unbounded: Optional[bool] = None


class RouteMatrixBoundaryTypeDef(BaseValidatorModel):
    Geometry: Optional[RouteMatrixBoundaryGeometryTypeDef] = None
    Unbounded: Optional[bool] = None


class RouteMatrixAvoidanceOptionsTypeDef(BaseValidatorModel):
    Areas: Optional[Sequence[RouteMatrixAvoidanceAreaTypeDef]] = None
    CarShuttleTrains: Optional[bool] = None
    ControlledAccessHighways: Optional[bool] = None
    DirtRoads: Optional[bool] = None
    Ferries: Optional[bool] = None
    TollRoads: Optional[bool] = None
    TollTransponders: Optional[bool] = None
    TruckRoadTypes: Optional[Sequence[str]] = None
    Tunnels: Optional[bool] = None
    UTurns: Optional[bool] = None
    ZoneCategories: Optional[Sequence[RouteMatrixAvoidanceZoneCategoryTypeDef]] = None


class RouteMatrixDestinationTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    Options: Optional[RouteMatrixDestinationOptionsTypeDef] = None


class RouteMatrixOriginTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    Options: Optional[RouteMatrixOriginOptionsTypeDef] = None


class RouteMatrixTravelModeOptionsTypeDef(BaseValidatorModel):
    Car: Optional[RouteMatrixCarOptionsTypeDef] = None
    Scooter: Optional[RouteMatrixScooterOptionsTypeDef] = None
    Truck: Optional[RouteMatrixTruckOptionsTypeDef] = None


class RouteFerryAfterTravelStepTypeDef(BaseValidatorModel):
    pass


class RouteFerryTravelStepTypeDef(BaseValidatorModel):
    pass


class RouteFerryBeforeTravelStepTypeDef(BaseValidatorModel):
    pass


class RouteFerryLegDetailsTypeDef(BaseValidatorModel):
    AfterTravelSteps: List[RouteFerryAfterTravelStepTypeDef]
    Arrival: RouteFerryArrivalTypeDef
    BeforeTravelSteps: List[RouteFerryBeforeTravelStepTypeDef]
    Departure: RouteFerryDepartureTypeDef
    Notices: List[RouteFerryNoticeTypeDef]
    PassThroughWaypoints: List[RoutePassThroughWaypointTypeDef]
    Spans: List[RouteFerrySpanTypeDef]
    TravelSteps: List[RouteFerryTravelStepTypeDef]
    RouteName: Optional[str] = None
    Summary: Optional[RouteFerrySummaryTypeDef] = None


class RouteTollSummaryTypeDef(BaseValidatorModel):
    Total: Optional[RouteTollPriceSummaryTypeDef] = None


class RouteTollRateTypeDef(BaseValidatorModel):
    Id: str
    LocalPrice: RouteTollPriceTypeDef
    Name: str
    PaymentMethods: List[RouteTollPaymentMethodType]
    Transponders: List[RouteTransponderTypeDef]
    ApplicableTimes: Optional[str] = None
    ConvertedPrice: Optional[RouteTollPriceTypeDef] = None
    Pass: Optional[RouteTollPassTypeDef] = None


class RouteTravelModeOptionsTypeDef(BaseValidatorModel):
    Car: Optional[RouteCarOptionsTypeDef] = None
    Pedestrian: Optional[RoutePedestrianOptionsTypeDef] = None
    Scooter: Optional[RouteScooterOptionsTypeDef] = None
    Truck: Optional[RouteTruckOptionsTypeDef] = None


class RouteVehicleNoticeDetailTypeDef(BaseValidatorModel):
    Title: Optional[str] = None
    ViolatedConstraints: Optional[RouteViolatedConstraintsTypeDef] = None


class WaypointOptimizationDestinationOptionsTypeDef(BaseValidatorModel):
    AccessHours: Optional[WaypointOptimizationAccessHoursTypeDef] = None
    AppointmentTime: Optional[str] = None
    Heading: Optional[float] = None
    Id: Optional[str] = None
    ServiceDuration: Optional[int] = None
    SideOfStreet: Optional[WaypointOptimizationSideOfStreetOptionsTypeDef] = None


class WaypointOptimizationWaypointTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    AccessHours: Optional[WaypointOptimizationAccessHoursTypeDef] = None
    AppointmentTime: Optional[str] = None
    Before: Optional[Sequence[int]] = None
    Heading: Optional[float] = None
    Id: Optional[str] = None
    ServiceDuration: Optional[int] = None
    SideOfStreet: Optional[WaypointOptimizationSideOfStreetOptionsTypeDef] = None


class WaypointOptimizationAvoidanceOptionsTypeDef(BaseValidatorModel):
    Areas: Optional[Sequence[WaypointOptimizationAvoidanceAreaTypeDef]] = None
    CarShuttleTrains: Optional[bool] = None
    ControlledAccessHighways: Optional[bool] = None
    DirtRoads: Optional[bool] = None
    Ferries: Optional[bool] = None
    TollRoads: Optional[bool] = None
    Tunnels: Optional[bool] = None
    UTurns: Optional[bool] = None


class OptimizeWaypointsResponseTypeDef(BaseValidatorModel):
    Connections: List[WaypointOptimizationConnectionTypeDef]
    Distance: int
    Duration: int
    ImpedingWaypoints: List[WaypointOptimizationImpedingWaypointTypeDef]
    OptimizedWaypoints: List[WaypointOptimizationOptimizedWaypointTypeDef]
    PricingBucket: str
    TimeBreakdown: WaypointOptimizationTimeBreakdownTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WaypointOptimizationDriverOptionsTypeDef(BaseValidatorModel):
    RestCycles: Optional[WaypointOptimizationRestCyclesTypeDef] = None
    RestProfile: Optional[WaypointOptimizationRestProfileTypeDef] = None
    TreatServiceTimeAs: Optional[WaypointOptimizationServiceTimeTreatmentType] = None


class WaypointOptimizationTravelModeOptionsTypeDef(BaseValidatorModel):
    Pedestrian: Optional[WaypointOptimizationPedestrianOptionsTypeDef] = None
    Truck: Optional[WaypointOptimizationTruckOptionsTypeDef] = None


class IsolineAvoidanceOptionsTypeDef(BaseValidatorModel):
    Areas: Optional[Sequence[IsolineAvoidanceAreaTypeDef]] = None
    CarShuttleTrains: Optional[bool] = None
    ControlledAccessHighways: Optional[bool] = None
    DirtRoads: Optional[bool] = None
    Ferries: Optional[bool] = None
    SeasonalClosure: Optional[bool] = None
    TollRoads: Optional[bool] = None
    TollTransponders: Optional[bool] = None
    TruckRoadTypes: Optional[Sequence[str]] = None
    Tunnels: Optional[bool] = None
    UTurns: Optional[bool] = None
    ZoneCategories: Optional[Sequence[IsolineAvoidanceZoneCategoryTypeDef]] = None


class RouteAvoidanceOptionsTypeDef(BaseValidatorModel):
    Areas: Optional[Sequence[RouteAvoidanceAreaTypeDef]] = None
    CarShuttleTrains: Optional[bool] = None
    ControlledAccessHighways: Optional[bool] = None
    DirtRoads: Optional[bool] = None
    Ferries: Optional[bool] = None
    SeasonalClosure: Optional[bool] = None
    TollRoads: Optional[bool] = None
    TollTransponders: Optional[bool] = None
    TruckRoadTypes: Optional[Sequence[str]] = None
    Tunnels: Optional[bool] = None
    UTurns: Optional[bool] = None
    ZoneCategories: Optional[Sequence[RouteAvoidanceZoneCategoryTypeDef]] = None


class CalculateIsolinesResponseTypeDef(BaseValidatorModel):
    ArrivalTime: str
    DepartureTime: str
    IsolineGeometryFormat: GeometryFormatType
    Isolines: List[IsolineTypeDef]
    PricingBucket: str
    SnappedDestination: List[float]
    SnappedOrigin: List[float]
    ResponseMetadata: ResponseMetadataTypeDef


class SnapToRoadsRequestTypeDef(BaseValidatorModel):
    TracePoints: Sequence[RoadSnapTracePointTypeDef]
    Key: Optional[str] = None
    SnappedGeometryFormat: Optional[GeometryFormatType] = None
    SnapRadius: Optional[int] = None
    TravelMode: Optional[RoadSnapTravelModeType] = None
    TravelModeOptions: Optional[RoadSnapTravelModeOptionsTypeDef] = None


class CalculateRouteMatrixResponseTypeDef(BaseValidatorModel):
    ErrorCount: int
    PricingBucket: str
    RouteMatrix: List[List[RouteMatrixEntryTypeDef]]
    RoutingBoundary: RouteMatrixBoundaryOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RouteSummaryTypeDef(BaseValidatorModel):
    Distance: Optional[int] = None
    Duration: Optional[int] = None
    Tolls: Optional[RouteTollSummaryTypeDef] = None


class RouteTollTypeDef(BaseValidatorModel):
    PaymentSites: List[RouteTollPaymentSiteTypeDef]
    Rates: List[RouteTollRateTypeDef]
    Systems: List[int]
    Country: Optional[str] = None


class RouteVehicleNoticeTypeDef(BaseValidatorModel):
    Code: RouteVehicleNoticeCodeType
    Details: List[RouteVehicleNoticeDetailTypeDef]
    Impact: Optional[RouteNoticeImpactType] = None


class OptimizeWaypointsRequestTypeDef(BaseValidatorModel):
    Origin: Sequence[float]
    Avoid: Optional[WaypointOptimizationAvoidanceOptionsTypeDef] = None
    Clustering: Optional[WaypointOptimizationClusteringOptionsTypeDef] = None
    DepartureTime: Optional[str] = None
    Destination: Optional[Sequence[float]] = None
    DestinationOptions: Optional[WaypointOptimizationDestinationOptionsTypeDef] = None
    Driver: Optional[WaypointOptimizationDriverOptionsTypeDef] = None
    Exclude: Optional[WaypointOptimizationExclusionOptionsTypeDef] = None
    Key: Optional[str] = None
    OptimizeSequencingFor: Optional[WaypointOptimizationSequencingObjectiveType] = None
    OriginOptions: Optional[WaypointOptimizationOriginOptionsTypeDef] = None
    Traffic: Optional[WaypointOptimizationTrafficOptionsTypeDef] = None
    TravelMode: Optional[WaypointOptimizationTravelModeType] = None
    TravelModeOptions: Optional[WaypointOptimizationTravelModeOptionsTypeDef] = None
    Waypoints: Optional[Sequence[WaypointOptimizationWaypointTypeDef]] = None


class CalculateIsolinesRequestTypeDef(BaseValidatorModel):
    Thresholds: IsolineThresholdsTypeDef
    Allow: Optional[IsolineAllowOptionsTypeDef] = None
    ArrivalTime: Optional[str] = None
    Avoid: Optional[IsolineAvoidanceOptionsTypeDef] = None
    DepartNow: Optional[bool] = None
    DepartureTime: Optional[str] = None
    Destination: Optional[Sequence[float]] = None
    DestinationOptions: Optional[IsolineDestinationOptionsTypeDef] = None
    IsolineGeometryFormat: Optional[GeometryFormatType] = None
    IsolineGranularity: Optional[IsolineGranularityOptionsTypeDef] = None
    Key: Optional[str] = None
    OptimizeIsolineFor: Optional[IsolineOptimizationObjectiveType] = None
    OptimizeRoutingFor: Optional[RoutingObjectiveType] = None
    Origin: Optional[Sequence[float]] = None
    OriginOptions: Optional[IsolineOriginOptionsTypeDef] = None
    Traffic: Optional[IsolineTrafficOptionsTypeDef] = None
    TravelMode: Optional[IsolineTravelModeType] = None
    TravelModeOptions: Optional[IsolineTravelModeOptionsTypeDef] = None


class CalculateRoutesRequestTypeDef(BaseValidatorModel):
    Destination: Sequence[float]
    Origin: Sequence[float]
    Allow: Optional[RouteAllowOptionsTypeDef] = None
    ArrivalTime: Optional[str] = None
    Avoid: Optional[RouteAvoidanceOptionsTypeDef] = None
    DepartNow: Optional[bool] = None
    DepartureTime: Optional[str] = None
    DestinationOptions: Optional[RouteDestinationOptionsTypeDef] = None
    Driver: Optional[RouteDriverOptionsTypeDef] = None
    Exclude: Optional[RouteExclusionOptionsTypeDef] = None
    InstructionsMeasurementSystem: Optional[MeasurementSystemType] = None
    Key: Optional[str] = None
    Languages: Optional[Sequence[str]] = None
    LegAdditionalFeatures: Optional[Sequence[RouteLegAdditionalFeatureType]] = None
    LegGeometryFormat: Optional[GeometryFormatType] = None
    MaxAlternatives: Optional[int] = None
    OptimizeRoutingFor: Optional[RoutingObjectiveType] = None
    OriginOptions: Optional[RouteOriginOptionsTypeDef] = None
    SpanAdditionalFeatures: Optional[Sequence[RouteSpanAdditionalFeatureType]] = None
    Tolls: Optional[RouteTollOptionsTypeDef] = None
    Traffic: Optional[RouteTrafficOptionsTypeDef] = None
    TravelMode: Optional[RouteTravelModeType] = None
    TravelModeOptions: Optional[RouteTravelModeOptionsTypeDef] = None
    TravelStepType: Optional[RouteTravelStepTypeType] = None
    Waypoints: Optional[Sequence[RouteWaypointTypeDef]] = None


class RoutePedestrianTravelStepTypeDef(BaseValidatorModel):
    pass


class RoutePedestrianLegDetailsTypeDef(BaseValidatorModel):
    Arrival: RoutePedestrianArrivalTypeDef
    Departure: RoutePedestrianDepartureTypeDef
    Notices: List[RoutePedestrianNoticeTypeDef]
    PassThroughWaypoints: List[RoutePassThroughWaypointTypeDef]
    Spans: List[RoutePedestrianSpanTypeDef]
    TravelSteps: List[RoutePedestrianTravelStepTypeDef]
    Summary: Optional[RoutePedestrianSummaryTypeDef] = None


class RouteMatrixBoundaryUnionTypeDef(BaseValidatorModel):
    pass


class CalculateRouteMatrixRequestTypeDef(BaseValidatorModel):
    Destinations: Sequence[RouteMatrixDestinationTypeDef]
    Origins: Sequence[RouteMatrixOriginTypeDef]
    RoutingBoundary: RouteMatrixBoundaryUnionTypeDef
    Allow: Optional[RouteMatrixAllowOptionsTypeDef] = None
    Avoid: Optional[RouteMatrixAvoidanceOptionsTypeDef] = None
    DepartNow: Optional[bool] = None
    DepartureTime: Optional[str] = None
    Exclude: Optional[RouteMatrixExclusionOptionsTypeDef] = None
    Key: Optional[str] = None
    OptimizeRoutingFor: Optional[RoutingObjectiveType] = None
    Traffic: Optional[RouteMatrixTrafficOptionsTypeDef] = None
    TravelMode: Optional[RouteMatrixTravelModeType] = None
    TravelModeOptions: Optional[RouteMatrixTravelModeOptionsTypeDef] = None


class RouteVehicleIncidentTypeDef(BaseValidatorModel):
    pass


class RouteVehicleTravelStepTypeDef(BaseValidatorModel):
    pass


class RouteVehicleLegDetailsTypeDef(BaseValidatorModel):
    Arrival: RouteVehicleArrivalTypeDef
    Departure: RouteVehicleDepartureTypeDef
    Incidents: List[RouteVehicleIncidentTypeDef]
    Notices: List[RouteVehicleNoticeTypeDef]
    PassThroughWaypoints: List[RoutePassThroughWaypointTypeDef]
    Spans: List[RouteVehicleSpanTypeDef]
    Tolls: List[RouteTollTypeDef]
    TollSystems: List[RouteTollSystemTypeDef]
    TravelSteps: List[RouteVehicleTravelStepTypeDef]
    TruckRoadTypes: List[str]
    Zones: List[RouteZoneTypeDef]
    Summary: Optional[RouteVehicleSummaryTypeDef] = None


class RouteLegTypeDef(BaseValidatorModel):
    pass


class RouteTypeDef(BaseValidatorModel):
    Legs: List[RouteLegTypeDef]
    MajorRoadLabels: List[RouteMajorRoadLabelTypeDef]
    Summary: Optional[RouteSummaryTypeDef] = None


class CalculateRoutesResponseTypeDef(BaseValidatorModel):
    LegGeometryFormat: GeometryFormatType
    Notices: List[RouteResponseNoticeTypeDef]
    PricingBucket: str
    Routes: List[RouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


