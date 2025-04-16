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
from aws_resource_validator.pydantic_models.location_constants import *

class ApiKeyFilter(BaseValidatorModel):
    KeyStatus: Optional[StatusType] = None


class ApiKeyRestrictionsOutput(BaseValidatorModel):
    AllowActions: List[str]
    AllowResources: List[str]
    AllowReferers: Optional[List[str]] = None


class ApiKeyRestrictions(BaseValidatorModel):
    AllowActions: Sequence[str]
    AllowResources: Sequence[str]
    AllowReferers: Optional[Sequence[str]] = None


class AssociateTrackerConsumerRequest(BaseValidatorModel):
    TrackerName: str
    ConsumerArn: str


class BatchItemError(BaseValidatorModel):
    Code: Optional[BatchItemErrorCodeType] = None
    Message: Optional[str] = None


class BatchDeleteDevicePositionHistoryRequest(BaseValidatorModel):
    TrackerName: str
    DeviceIds: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteGeofenceRequest(BaseValidatorModel):
    CollectionName: str
    GeofenceIds: Sequence[str]


class BatchGetDevicePositionRequest(BaseValidatorModel):
    TrackerName: str
    DeviceIds: Sequence[str]


class BatchPutGeofenceSuccess(BaseValidatorModel):
    GeofenceId: str
    CreateTime: datetime
    UpdateTime: datetime


class CalculateRouteCarModeOptions(BaseValidatorModel):
    AvoidFerries: Optional[bool] = None
    AvoidTolls: Optional[bool] = None


class CalculateRouteMatrixSummary(BaseValidatorModel):
    DataSource: str
    RouteCount: int
    ErrorCount: int
    DistanceUnit: DistanceUnitType


class CalculateRouteSummary(BaseValidatorModel):
    RouteBBox: List[float]
    DataSource: str
    Distance: float
    DurationSeconds: float
    DistanceUnit: DistanceUnitType


class TruckDimensions(BaseValidatorModel):
    Length: Optional[float] = None
    Height: Optional[float] = None
    Width: Optional[float] = None
    Unit: Optional[DimensionUnitType] = None


class TruckWeight(BaseValidatorModel):
    Total: Optional[float] = None
    Unit: Optional[VehicleWeightUnitType] = None


class CircleOutput(BaseValidatorModel):
    Center: List[float]
    Radius: float


class Circle(BaseValidatorModel):
    Center: Sequence[float]
    Radius: float


class CreateGeofenceCollectionRequest(BaseValidatorModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyId: Optional[str] = None


class DataSourceConfiguration(BaseValidatorModel):
    IntendedUse: Optional[IntendedUseType] = None


class CreateRouteCalculatorRequest(BaseValidatorModel):
    CalculatorName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateTrackerRequest(BaseValidatorModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    KmsKeyId: Optional[str] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None


class DeleteGeofenceCollectionRequest(BaseValidatorModel):
    CollectionName: str


class DeleteKeyRequest(BaseValidatorModel):
    KeyName: str
    ForceDelete: Optional[bool] = None


class DeleteMapRequest(BaseValidatorModel):
    MapName: str


class DeletePlaceIndexRequest(BaseValidatorModel):
    IndexName: str


class DeleteRouteCalculatorRequest(BaseValidatorModel):
    CalculatorName: str


class DeleteTrackerRequest(BaseValidatorModel):
    TrackerName: str


class DescribeGeofenceCollectionRequest(BaseValidatorModel):
    CollectionName: str


class DescribeKeyRequest(BaseValidatorModel):
    KeyName: str


class DescribeMapRequest(BaseValidatorModel):
    MapName: str


class MapConfigurationOutput(BaseValidatorModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[List[str]] = None


class DescribePlaceIndexRequest(BaseValidatorModel):
    IndexName: str


class DescribeRouteCalculatorRequest(BaseValidatorModel):
    CalculatorName: str


class DescribeTrackerRequest(BaseValidatorModel):
    TrackerName: str


class PositionalAccuracy(BaseValidatorModel):
    Horizontal: float


class WiFiAccessPoint(BaseValidatorModel):
    MacAddress: str
    Rss: int


class DisassociateTrackerConsumerRequest(BaseValidatorModel):
    TrackerName: str
    ConsumerArn: str


class ForecastGeofenceEventsDeviceState(BaseValidatorModel):
    Position: Sequence[float]
    Speed: Optional[float] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ForecastedEvent(BaseValidatorModel):
    EventId: str
    GeofenceId: str
    IsDeviceInGeofence: bool
    NearestDistance: float
    EventType: ForecastedGeofenceEventTypeType
    ForecastedBreachTime: Optional[datetime] = None
    GeofenceProperties: Optional[Dict[str, str]] = None


class GetDevicePositionRequest(BaseValidatorModel):
    TrackerName: str
    DeviceId: str


class GetGeofenceRequest(BaseValidatorModel):
    CollectionName: str
    GeofenceId: str


class GetMapGlyphsRequest(BaseValidatorModel):
    MapName: str
    FontStack: str
    FontUnicodeRange: str
    Key: Optional[str] = None


class GetMapSpritesRequest(BaseValidatorModel):
    MapName: str
    FileName: str
    Key: Optional[str] = None


class GetMapStyleDescriptorRequest(BaseValidatorModel):
    MapName: str
    Key: Optional[str] = None


class GetMapTileRequest(BaseValidatorModel):
    MapName: str
    Z: str
    X: str
    Y: str
    Key: Optional[str] = None


class GetPlaceRequest(BaseValidatorModel):
    IndexName: str
    PlaceId: str
    Language: Optional[str] = None
    Key: Optional[str] = None


class LegGeometry(BaseValidatorModel):
    LineString: Optional[List[List[float]]] = None


class Step(BaseValidatorModel):
    StartPosition: List[float]
    EndPosition: List[float]
    Distance: float
    DurationSeconds: float
    GeometryOffset: Optional[int] = None


class TrackingFilterGeometry(BaseValidatorModel):
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None


class ListGeofenceCollectionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGeofenceCollectionsResponseEntry(BaseValidatorModel):
    CollectionName: str
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None


class ListGeofencesRequest(BaseValidatorModel):
    CollectionName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMapsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMapsResponseEntry(BaseValidatorModel):
    MapName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None


class ListPlaceIndexesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPlaceIndexesResponseEntry(BaseValidatorModel):
    IndexName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None


class ListRouteCalculatorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRouteCalculatorsResponseEntry(BaseValidatorModel):
    CalculatorName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListTrackerConsumersRequest(BaseValidatorModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTrackersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTrackersResponseEntry(BaseValidatorModel):
    TrackerName: str
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None


class LteLocalId(BaseValidatorModel):
    Earfcn: int
    Pci: int


class LteNetworkMeasurements(BaseValidatorModel):
    Earfcn: int
    CellId: int
    Pci: int
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None


class MapConfiguration(BaseValidatorModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[Sequence[str]] = None


class MapConfigurationUpdate(BaseValidatorModel):
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[Sequence[str]] = None


class PlaceGeometry(BaseValidatorModel):
    Point: Optional[List[float]] = None


class TimeZone(BaseValidatorModel):
    Name: str
    Offset: Optional[int] = None


class RouteMatrixEntryError(BaseValidatorModel):
    Code: RouteMatrixErrorCodeType
    Message: Optional[str] = None


class SearchPlaceIndexForPositionRequest(BaseValidatorModel):
    IndexName: str
    Position: Sequence[float]
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    Key: Optional[str] = None


class SearchPlaceIndexForPositionSummary(BaseValidatorModel):
    Position: List[float]
    DataSource: str
    MaxResults: Optional[int] = None
    Language: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateGeofenceCollectionRequest(BaseValidatorModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None


class UpdateRouteCalculatorRequest(BaseValidatorModel):
    CalculatorName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None


class UpdateTrackerRequest(BaseValidatorModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None


class ListKeysRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filter: Optional[ApiKeyFilter] = None


class ListKeysResponseEntry(BaseValidatorModel):
    KeyName: str
    ExpireTime: datetime
    Restrictions: ApiKeyRestrictionsOutput
    CreateTime: datetime
    UpdateTime: datetime
    Description: Optional[str] = None


class BatchDeleteDevicePositionHistoryError(BaseValidatorModel):
    DeviceId: str
    Error: BatchItemError


class BatchDeleteGeofenceError(BaseValidatorModel):
    GeofenceId: str
    Error: BatchItemError


class BatchEvaluateGeofencesError(BaseValidatorModel):
    DeviceId: str
    SampleTime: datetime
    Error: BatchItemError


class BatchGetDevicePositionError(BaseValidatorModel):
    DeviceId: str
    Error: BatchItemError


class BatchPutGeofenceError(BaseValidatorModel):
    GeofenceId: str
    Error: BatchItemError


class BatchUpdateDevicePositionError(BaseValidatorModel):
    DeviceId: str
    SampleTime: datetime
    Error: BatchItemError


class CreateGeofenceCollectionResponse(BaseValidatorModel):
    CollectionName: str
    CollectionArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateKeyResponse(BaseValidatorModel):
    Key: str
    KeyArn: str
    KeyName: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateMapResponse(BaseValidatorModel):
    MapName: str
    MapArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


class CreatePlaceIndexResponse(BaseValidatorModel):
    IndexName: str
    IndexArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateRouteCalculatorResponse(BaseValidatorModel):
    CalculatorName: str
    CalculatorArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateTrackerResponse(BaseValidatorModel):
    TrackerName: str
    TrackerArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeGeofenceCollectionResponse(BaseValidatorModel):
    CollectionName: str
    CollectionArn: str
    Description: str
    PricingPlan: PricingPlanType
    PricingPlanDataSource: str
    KmsKeyId: str
    Tags: Dict[str, str]
    CreateTime: datetime
    UpdateTime: datetime
    GeofenceCount: int
    ResponseMetadata: ResponseMetadata


class DescribeKeyResponse(BaseValidatorModel):
    Key: str
    KeyArn: str
    KeyName: str
    Restrictions: ApiKeyRestrictionsOutput
    CreateTime: datetime
    ExpireTime: datetime
    UpdateTime: datetime
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeRouteCalculatorResponse(BaseValidatorModel):
    CalculatorName: str
    CalculatorArn: str
    PricingPlan: PricingPlanType
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    DataSource: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeTrackerResponse(BaseValidatorModel):
    TrackerName: str
    TrackerArn: str
    Description: str
    PricingPlan: PricingPlanType
    PricingPlanDataSource: str
    Tags: Dict[str, str]
    CreateTime: datetime
    UpdateTime: datetime
    KmsKeyId: str
    PositionFiltering: PositionFilteringType
    EventBridgeEnabled: bool
    KmsKeyEnableGeospatialQueries: bool
    ResponseMetadata: ResponseMetadata


class GetMapGlyphsResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadata


class GetMapSpritesResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadata


class GetMapStyleDescriptorResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadata


class GetMapTileResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTrackerConsumersResponse(BaseValidatorModel):
    ConsumerArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutGeofenceResponse(BaseValidatorModel):
    GeofenceId: str
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateGeofenceCollectionResponse(BaseValidatorModel):
    CollectionName: str
    CollectionArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateKeyResponse(BaseValidatorModel):
    KeyArn: str
    KeyName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateMapResponse(BaseValidatorModel):
    MapName: str
    MapArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdatePlaceIndexResponse(BaseValidatorModel):
    IndexName: str
    IndexArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateRouteCalculatorResponse(BaseValidatorModel):
    CalculatorName: str
    CalculatorArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateTrackerResponse(BaseValidatorModel):
    TrackerName: str
    TrackerArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class GetDevicePositionHistoryRequest(BaseValidatorModel):
    TrackerName: str
    DeviceId: str
    NextToken: Optional[str] = None
    StartTimeInclusive: Optional[Timestamp] = None
    EndTimeExclusive: Optional[Timestamp] = None
    MaxResults: Optional[int] = None


class CalculateRouteTruckModeOptions(BaseValidatorModel):
    AvoidFerries: Optional[bool] = None
    AvoidTolls: Optional[bool] = None
    Dimensions: Optional[TruckDimensions] = None
    Weight: Optional[TruckWeight] = None


class GeofenceGeometryOutput(BaseValidatorModel):
    Polygon: Optional[List[List[List[float]]]] = None
    Circle: Optional[CircleOutput] = None
    Geobuf: Optional[bytes] = None


class CreatePlaceIndexRequest(BaseValidatorModel):
    IndexName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfiguration] = None
    Tags: Optional[Mapping[str, str]] = None


class DescribePlaceIndexResponse(BaseValidatorModel):
    IndexName: str
    IndexArn: str
    PricingPlan: PricingPlanType
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    DataSource: str
    DataSourceConfiguration: DataSourceConfiguration
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdatePlaceIndexRequest(BaseValidatorModel):
    IndexName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfiguration] = None


class DescribeMapResponse(BaseValidatorModel):
    MapName: str
    MapArn: str
    PricingPlan: PricingPlanType
    DataSource: str
    Configuration: MapConfigurationOutput
    Description: str
    Tags: Dict[str, str]
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class DevicePosition(BaseValidatorModel):
    SampleTime: datetime
    ReceivedTime: datetime
    Position: List[float]
    DeviceId: Optional[str] = None
    Accuracy: Optional[PositionalAccuracy] = None
    PositionProperties: Optional[Dict[str, str]] = None


class DevicePositionUpdate(BaseValidatorModel):
    DeviceId: str
    SampleTime: Timestamp
    Position: Sequence[float]
    Accuracy: Optional[PositionalAccuracy] = None
    PositionProperties: Optional[Mapping[str, str]] = None


class GetDevicePositionResponse(BaseValidatorModel):
    DeviceId: str
    SampleTime: datetime
    ReceivedTime: datetime
    Position: List[float]
    Accuracy: PositionalAccuracy
    PositionProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class InferredState(BaseValidatorModel):
    ProxyDetected: bool
    Position: Optional[List[float]] = None
    Accuracy: Optional[PositionalAccuracy] = None
    DeviationDistance: Optional[float] = None


class ListDevicePositionsResponseEntry(BaseValidatorModel):
    DeviceId: str
    SampleTime: datetime
    Position: List[float]
    Accuracy: Optional[PositionalAccuracy] = None
    PositionProperties: Optional[Dict[str, str]] = None


class ForecastGeofenceEventsRequest(BaseValidatorModel):
    CollectionName: str
    DeviceState: ForecastGeofenceEventsDeviceState
    TimeHorizonMinutes: Optional[float] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    SpeedUnit: Optional[SpeedUnitType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ForecastGeofenceEventsRequestPaginate(BaseValidatorModel):
    CollectionName: str
    DeviceState: ForecastGeofenceEventsDeviceState
    TimeHorizonMinutes: Optional[float] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    SpeedUnit: Optional[SpeedUnitType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDevicePositionHistoryRequestPaginate(BaseValidatorModel):
    TrackerName: str
    DeviceId: str
    StartTimeInclusive: Optional[Timestamp] = None
    EndTimeExclusive: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGeofenceCollectionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGeofencesRequestPaginate(BaseValidatorModel):
    CollectionName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKeysRequestPaginate(BaseValidatorModel):
    Filter: Optional[ApiKeyFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMapsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPlaceIndexesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRouteCalculatorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrackerConsumersRequestPaginate(BaseValidatorModel):
    TrackerName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrackersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ForecastGeofenceEventsResponse(BaseValidatorModel):
    ForecastedEvents: List[ForecastedEvent]
    DistanceUnit: DistanceUnitType
    SpeedUnit: SpeedUnitType
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Leg(BaseValidatorModel):
    StartPosition: List[float]
    EndPosition: List[float]
    Distance: float
    DurationSeconds: float
    Steps: List[Step]
    Geometry: Optional[LegGeometry] = None


class ListDevicePositionsRequestPaginate(BaseValidatorModel):
    TrackerName: str
    FilterGeometry: Optional[TrackingFilterGeometry] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDevicePositionsRequest(BaseValidatorModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FilterGeometry: Optional[TrackingFilterGeometry] = None


class ListGeofenceCollectionsResponse(BaseValidatorModel):
    Entries: List[ListGeofenceCollectionsResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMapsResponse(BaseValidatorModel):
    Entries: List[ListMapsResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPlaceIndexesResponse(BaseValidatorModel):
    Entries: List[ListPlaceIndexesResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRouteCalculatorsResponse(BaseValidatorModel):
    Entries: List[ListRouteCalculatorsResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrackersResponse(BaseValidatorModel):
    Entries: List[ListTrackersResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LteCellDetails(BaseValidatorModel):
    CellId: int
    Mcc: int
    Mnc: int
    LocalId: Optional[LteLocalId] = None
    NetworkMeasurements: Optional[Sequence[LteNetworkMeasurements]] = None
    TimingAdvance: Optional[int] = None
    NrCapable: Optional[bool] = None
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None
    Tac: Optional[int] = None


class UpdateMapRequest(BaseValidatorModel):
    MapName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    ConfigurationUpdate: Optional[MapConfigurationUpdate] = None


class Place(BaseValidatorModel):
    Geometry: PlaceGeometry
    Label: Optional[str] = None
    AddressNumber: Optional[str] = None
    Street: Optional[str] = None
    Neighborhood: Optional[str] = None
    Municipality: Optional[str] = None
    SubRegion: Optional[str] = None
    Region: Optional[str] = None
    Country: Optional[str] = None
    PostalCode: Optional[str] = None
    Interpolated: Optional[bool] = None
    TimeZone: Optional[TimeZone] = None
    UnitType: Optional[str] = None
    UnitNumber: Optional[str] = None
    Categories: Optional[List[str]] = None
    SupplementalCategories: Optional[List[str]] = None
    SubMunicipality: Optional[str] = None


class RouteMatrixEntry(BaseValidatorModel):
    Distance: Optional[float] = None
    DurationSeconds: Optional[float] = None
    Error: Optional[RouteMatrixEntryError] = None


class SearchForSuggestionsResult(BaseValidatorModel):
    pass


class SearchPlaceIndexForSuggestionsSummary(BaseValidatorModel):
    pass


class SearchPlaceIndexForSuggestionsResponse(BaseValidatorModel):
    Summary: SearchPlaceIndexForSuggestionsSummary
    Results: List[SearchForSuggestionsResult]
    ResponseMetadata: ResponseMetadata


class ListKeysResponse(BaseValidatorModel):
    Entries: List[ListKeysResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ApiKeyRestrictionsUnion(BaseValidatorModel):
    pass


class CreateKeyRequest(BaseValidatorModel):
    KeyName: str
    Restrictions: ApiKeyRestrictionsUnion
    Description: Optional[str] = None
    ExpireTime: Optional[Timestamp] = None
    NoExpiry: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateKeyRequest(BaseValidatorModel):
    KeyName: str
    Description: Optional[str] = None
    ExpireTime: Optional[Timestamp] = None
    NoExpiry: Optional[bool] = None
    ForceUpdate: Optional[bool] = None
    Restrictions: Optional[ApiKeyRestrictionsUnion] = None


class BatchDeleteDevicePositionHistoryResponse(BaseValidatorModel):
    Errors: List[BatchDeleteDevicePositionHistoryError]
    ResponseMetadata: ResponseMetadata


class BatchDeleteGeofenceResponse(BaseValidatorModel):
    Errors: List[BatchDeleteGeofenceError]
    ResponseMetadata: ResponseMetadata


class BatchEvaluateGeofencesResponse(BaseValidatorModel):
    Errors: List[BatchEvaluateGeofencesError]
    ResponseMetadata: ResponseMetadata


class BatchPutGeofenceResponse(BaseValidatorModel):
    Successes: List[BatchPutGeofenceSuccess]
    Errors: List[BatchPutGeofenceError]
    ResponseMetadata: ResponseMetadata


class BatchUpdateDevicePositionResponse(BaseValidatorModel):
    Errors: List[BatchUpdateDevicePositionError]
    ResponseMetadata: ResponseMetadata


class CalculateRouteMatrixRequest(BaseValidatorModel):
    CalculatorName: str
    DeparturePositions: Sequence[Sequence[float]]
    DestinationPositions: Sequence[Sequence[float]]
    TravelMode: Optional[TravelModeType] = None
    DepartureTime: Optional[Timestamp] = None
    DepartNow: Optional[bool] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    CarModeOptions: Optional[CalculateRouteCarModeOptions] = None
    TruckModeOptions: Optional[CalculateRouteTruckModeOptions] = None
    Key: Optional[str] = None


class CalculateRouteRequest(BaseValidatorModel):
    CalculatorName: str
    DeparturePosition: Sequence[float]
    DestinationPosition: Sequence[float]
    WaypointPositions: Optional[Sequence[Sequence[float]]] = None
    TravelMode: Optional[TravelModeType] = None
    DepartureTime: Optional[Timestamp] = None
    DepartNow: Optional[bool] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    IncludeLegGeometry: Optional[bool] = None
    CarModeOptions: Optional[CalculateRouteCarModeOptions] = None
    TruckModeOptions: Optional[CalculateRouteTruckModeOptions] = None
    ArrivalTime: Optional[Timestamp] = None
    OptimizeFor: Optional[OptimizationModeType] = None
    Key: Optional[str] = None


class GetGeofenceResponse(BaseValidatorModel):
    GeofenceId: str
    Geometry: GeofenceGeometryOutput
    Status: str
    CreateTime: datetime
    UpdateTime: datetime
    GeofenceProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListGeofenceResponseEntry(BaseValidatorModel):
    GeofenceId: str
    Geometry: GeofenceGeometryOutput
    Status: str
    CreateTime: datetime
    UpdateTime: datetime
    GeofenceProperties: Optional[Dict[str, str]] = None


class CircleUnion(BaseValidatorModel):
    pass


class Blob(BaseValidatorModel):
    pass


class GeofenceGeometry(BaseValidatorModel):
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None
    Circle: Optional[CircleUnion] = None
    Geobuf: Optional[Blob] = None


class BatchGetDevicePositionResponse(BaseValidatorModel):
    Errors: List[BatchGetDevicePositionError]
    DevicePositions: List[DevicePosition]
    ResponseMetadata: ResponseMetadata


class GetDevicePositionHistoryResponse(BaseValidatorModel):
    DevicePositions: List[DevicePosition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchEvaluateGeofencesRequest(BaseValidatorModel):
    CollectionName: str
    DevicePositionUpdates: Sequence[DevicePositionUpdate]


class BatchUpdateDevicePositionRequest(BaseValidatorModel):
    TrackerName: str
    Updates: Sequence[DevicePositionUpdate]


class VerifyDevicePositionResponse(BaseValidatorModel):
    InferredState: InferredState
    DeviceId: str
    SampleTime: datetime
    ReceivedTime: datetime
    DistanceUnit: DistanceUnitType
    ResponseMetadata: ResponseMetadata


class ListDevicePositionsResponse(BaseValidatorModel):
    Entries: List[ListDevicePositionsResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CalculateRouteResponse(BaseValidatorModel):
    Legs: List[Leg]
    Summary: CalculateRouteSummary
    ResponseMetadata: ResponseMetadata


class CellSignals(BaseValidatorModel):
    LteCellDetails: Sequence[LteCellDetails]


class MapConfigurationUnion(BaseValidatorModel):
    pass


class CreateMapRequest(BaseValidatorModel):
    MapName: str
    Configuration: MapConfigurationUnion
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class GetPlaceResponse(BaseValidatorModel):
    Place: Place
    ResponseMetadata: ResponseMetadata


class SearchForPositionResult(BaseValidatorModel):
    Place: Place
    Distance: float
    PlaceId: Optional[str] = None


class SearchForTextResult(BaseValidatorModel):
    Place: Place
    Distance: Optional[float] = None
    Relevance: Optional[float] = None
    PlaceId: Optional[str] = None


class CalculateRouteMatrixResponse(BaseValidatorModel):
    RouteMatrix: List[List[RouteMatrixEntry]]
    SnappedDeparturePositions: List[List[float]]
    SnappedDestinationPositions: List[List[float]]
    Summary: CalculateRouteMatrixSummary
    ResponseMetadata: ResponseMetadata


class ListGeofencesResponse(BaseValidatorModel):
    Entries: List[ListGeofenceResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DeviceState(BaseValidatorModel):
    DeviceId: str
    SampleTime: Timestamp
    Position: Sequence[float]
    Accuracy: Optional[PositionalAccuracy] = None
    Ipv4Address: Optional[str] = None
    WiFiAccessPoints: Optional[Sequence[WiFiAccessPoint]] = None
    CellSignals: Optional[CellSignals] = None


class SearchPlaceIndexForPositionResponse(BaseValidatorModel):
    Summary: SearchPlaceIndexForPositionSummary
    Results: List[SearchForPositionResult]
    ResponseMetadata: ResponseMetadata


class SearchPlaceIndexForTextSummary(BaseValidatorModel):
    pass


class SearchPlaceIndexForTextResponse(BaseValidatorModel):
    Summary: SearchPlaceIndexForTextSummary
    Results: List[SearchForTextResult]
    ResponseMetadata: ResponseMetadata


class GeofenceGeometryUnion(BaseValidatorModel):
    pass


class BatchPutGeofenceRequestEntry(BaseValidatorModel):
    GeofenceId: str
    Geometry: GeofenceGeometryUnion
    GeofenceProperties: Optional[Mapping[str, str]] = None


class PutGeofenceRequest(BaseValidatorModel):
    CollectionName: str
    GeofenceId: str
    Geometry: GeofenceGeometryUnion
    GeofenceProperties: Optional[Mapping[str, str]] = None


class VerifyDevicePositionRequest(BaseValidatorModel):
    TrackerName: str
    DeviceState: DeviceState
    DistanceUnit: Optional[DistanceUnitType] = None


class BatchPutGeofenceRequest(BaseValidatorModel):
    CollectionName: str
    Entries: Sequence[BatchPutGeofenceRequestEntry]


