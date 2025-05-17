from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.location.location_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApiKeyFilter(BaseValidatorModel):
    KeyStatus: Optional[StatusType] = None


class ApiKeyRestrictionsOutput(BaseValidatorModel):
    AllowActions: List[str]
    AllowResources: List[str]
    AllowReferers: Optional[List[str]] = None


class ApiKeyRestrictions(BaseValidatorModel):
    AllowActions: List[str]
    AllowResources: List[str]
    AllowReferers: Optional[List[str]] = None


class AssociateTrackerConsumerRequest(BaseValidatorModel):
    TrackerName: str
    ConsumerArn: str


class BatchItemError(BaseValidatorModel):
    Code: Optional[BatchItemErrorCodeType] = None
    Message: Optional[str] = None


# This class is the input for the 'batch_delete_device_position_history' function.
class BatchDeleteDevicePositionHistoryRequest(BaseValidatorModel):
    TrackerName: str
    DeviceIds: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'batch_delete_geofence' function.
class BatchDeleteGeofenceRequest(BaseValidatorModel):
    CollectionName: str
    GeofenceIds: List[str]


# This class is the input for the 'batch_get_device_position' function.
class BatchGetDevicePositionRequest(BaseValidatorModel):
    TrackerName: str
    DeviceIds: List[str]


class BatchPutGeofenceSuccess(BaseValidatorModel):
    GeofenceId: str
    CreateTime: datetime
    UpdateTime: datetime

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CalculateRouteCarModeOptions(BaseValidatorModel):
    AvoidFerries: Optional[bool] = None
    AvoidTolls: Optional[bool] = None

Timestamp = Union[datetime, str]


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
    Center: List[float]
    Radius: float


# This class is the input for the 'create_geofence_collection' function.
class CreateGeofenceCollectionRequest(BaseValidatorModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    KmsKeyId: Optional[str] = None


class DataSourceConfiguration(BaseValidatorModel):
    IntendedUse: Optional[IntendedUseType] = None


# This class is the input for the 'create_route_calculator' function.
class CreateRouteCalculatorRequest(BaseValidatorModel):
    CalculatorName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_tracker' function.
class CreateTrackerRequest(BaseValidatorModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    KmsKeyId: Optional[str] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
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


# This class is the input for the 'describe_geofence_collection' function.
class DescribeGeofenceCollectionRequest(BaseValidatorModel):
    CollectionName: str


# This class is the input for the 'describe_key' function.
class DescribeKeyRequest(BaseValidatorModel):
    KeyName: str


# This class is the input for the 'describe_map' function.
class DescribeMapRequest(BaseValidatorModel):
    MapName: str


class MapConfigurationOutput(BaseValidatorModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[List[str]] = None


# This class is the input for the 'describe_place_index' function.
class DescribePlaceIndexRequest(BaseValidatorModel):
    IndexName: str


# This class is the input for the 'describe_route_calculator' function.
class DescribeRouteCalculatorRequest(BaseValidatorModel):
    CalculatorName: str


# This class is the input for the 'describe_tracker' function.
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
    Position: List[float]
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


# This class is the input for the 'get_device_position' function.
class GetDevicePositionRequest(BaseValidatorModel):
    TrackerName: str
    DeviceId: str


# This class is the input for the 'get_geofence' function.
class GetGeofenceRequest(BaseValidatorModel):
    CollectionName: str
    GeofenceId: str


# This class is the input for the 'get_map_glyphs' function.
class GetMapGlyphsRequest(BaseValidatorModel):
    MapName: str
    FontStack: str
    FontUnicodeRange: str
    Key: Optional[str] = None


# This class is the input for the 'get_map_sprites' function.
class GetMapSpritesRequest(BaseValidatorModel):
    MapName: str
    FileName: str
    Key: Optional[str] = None


# This class is the input for the 'get_map_style_descriptor' function.
class GetMapStyleDescriptorRequest(BaseValidatorModel):
    MapName: str
    Key: Optional[str] = None


# This class is the input for the 'get_map_tile' function.
class GetMapTileRequest(BaseValidatorModel):
    MapName: str
    Z: str
    X: str
    Y: str
    Key: Optional[str] = None


# This class is the input for the 'get_place' function.
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
    Polygon: Optional[List[List[List[float]]]] = None


# This class is the input for the 'list_geofence_collections' function.
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


# This class is the input for the 'list_geofences' function.
class ListGeofencesRequest(BaseValidatorModel):
    CollectionName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_maps' function.
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


# This class is the input for the 'list_place_indexes' function.
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


# This class is the input for the 'list_route_calculators' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'list_tracker_consumers' function.
class ListTrackerConsumersRequest(BaseValidatorModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_trackers' function.
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
    CustomLayers: Optional[List[str]] = None


class MapConfigurationUpdate(BaseValidatorModel):
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[List[str]] = None


class PlaceGeometry(BaseValidatorModel):
    Point: Optional[List[float]] = None


class TimeZone(BaseValidatorModel):
    Name: str
    Offset: Optional[int] = None


class RouteMatrixEntryError(BaseValidatorModel):
    Code: RouteMatrixErrorCodeType
    Message: Optional[str] = None


class SearchForSuggestionsResult(BaseValidatorModel):
    Text: str
    PlaceId: Optional[str] = None
    Categories: Optional[List[str]] = None
    SupplementalCategories: Optional[List[str]] = None


# This class is the input for the 'search_place_index_for_position' function.
class SearchPlaceIndexForPositionRequest(BaseValidatorModel):
    IndexName: str
    Position: List[float]
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    Key: Optional[str] = None


class SearchPlaceIndexForPositionSummary(BaseValidatorModel):
    Position: List[float]
    DataSource: str
    MaxResults: Optional[int] = None
    Language: Optional[str] = None


# This class is the input for the 'search_place_index_for_suggestions' function.
class SearchPlaceIndexForSuggestionsRequest(BaseValidatorModel):
    IndexName: str
    Text: str
    BiasPosition: Optional[List[float]] = None
    FilterBBox: Optional[List[float]] = None
    FilterCountries: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[List[str]] = None
    Key: Optional[str] = None


class SearchPlaceIndexForSuggestionsSummary(BaseValidatorModel):
    Text: str
    DataSource: str
    BiasPosition: Optional[List[float]] = None
    FilterBBox: Optional[List[float]] = None
    FilterCountries: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[List[str]] = None


# This class is the input for the 'search_place_index_for_text' function.
class SearchPlaceIndexForTextRequest(BaseValidatorModel):
    IndexName: str
    Text: str
    BiasPosition: Optional[List[float]] = None
    FilterBBox: Optional[List[float]] = None
    FilterCountries: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[List[str]] = None
    Key: Optional[str] = None


class SearchPlaceIndexForTextSummary(BaseValidatorModel):
    Text: str
    DataSource: str
    BiasPosition: Optional[List[float]] = None
    FilterBBox: Optional[List[float]] = None
    FilterCountries: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    ResultBBox: Optional[List[float]] = None
    Language: Optional[str] = None
    FilterCategories: Optional[List[str]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_geofence_collection' function.
class UpdateGeofenceCollectionRequest(BaseValidatorModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'update_route_calculator' function.
class UpdateRouteCalculatorRequest(BaseValidatorModel):
    CalculatorName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None


# This class is the input for the 'update_tracker' function.
class UpdateTrackerRequest(BaseValidatorModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None


# This class is the input for the 'list_keys' function.
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

ApiKeyRestrictionsUnion = Union[ApiKeyRestrictions, ApiKeyRestrictionsOutput]


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


# This class is the output for the 'create_geofence_collection' function.
class CreateGeofenceCollectionResponse(BaseValidatorModel):
    CollectionName: str
    CollectionArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_key' function.
class CreateKeyResponse(BaseValidatorModel):
    Key: str
    KeyArn: str
    KeyName: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_map' function.
class CreateMapResponse(BaseValidatorModel):
    MapName: str
    MapArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_place_index' function.
class CreatePlaceIndexResponse(BaseValidatorModel):
    IndexName: str
    IndexArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_route_calculator' function.
class CreateRouteCalculatorResponse(BaseValidatorModel):
    CalculatorName: str
    CalculatorArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_tracker' function.
class CreateTrackerResponse(BaseValidatorModel):
    TrackerName: str
    TrackerArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_geofence_collection' function.
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


# This class is the output for the 'describe_key' function.
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


# This class is the output for the 'describe_route_calculator' function.
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


# This class is the output for the 'describe_tracker' function.
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


# This class is the output for the 'get_map_glyphs' function.
class GetMapGlyphsResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_map_sprites' function.
class GetMapSpritesResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_map_style_descriptor' function.
class GetMapStyleDescriptorResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_map_tile' function.
class GetMapTileResponse(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tracker_consumers' function.
class ListTrackerConsumersResponse(BaseValidatorModel):
    ConsumerArns: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_geofence' function.
class PutGeofenceResponse(BaseValidatorModel):
    GeofenceId: str
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_geofence_collection' function.
class UpdateGeofenceCollectionResponse(BaseValidatorModel):
    CollectionName: str
    CollectionArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_key' function.
class UpdateKeyResponse(BaseValidatorModel):
    KeyArn: str
    KeyName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_map' function.
class UpdateMapResponse(BaseValidatorModel):
    MapName: str
    MapArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_place_index' function.
class UpdatePlaceIndexResponse(BaseValidatorModel):
    IndexName: str
    IndexArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_route_calculator' function.
class UpdateRouteCalculatorResponse(BaseValidatorModel):
    CalculatorName: str
    CalculatorArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_tracker' function.
class UpdateTrackerResponse(BaseValidatorModel):
    TrackerName: str
    TrackerArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'get_device_position_history' function.
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

CircleUnion = Union[Circle, CircleOutput]


# This class is the input for the 'create_place_index' function.
class CreatePlaceIndexRequest(BaseValidatorModel):
    IndexName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfiguration] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_place_index' function.
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


# This class is the input for the 'update_place_index' function.
class UpdatePlaceIndexRequest(BaseValidatorModel):
    IndexName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfiguration] = None


# This class is the output for the 'describe_map' function.
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
    Position: List[float]
    Accuracy: Optional[PositionalAccuracy] = None
    PositionProperties: Optional[Dict[str, str]] = None


# This class is the output for the 'get_device_position' function.
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


# This class is the input for the 'forecast_geofence_events' function.
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


# This class is the output for the 'forecast_geofence_events' function.
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


# This class is the input for the 'list_device_positions' function.
class ListDevicePositionsRequest(BaseValidatorModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FilterGeometry: Optional[TrackingFilterGeometry] = None


# This class is the output for the 'list_geofence_collections' function.
class ListGeofenceCollectionsResponse(BaseValidatorModel):
    Entries: List[ListGeofenceCollectionsResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_maps' function.
class ListMapsResponse(BaseValidatorModel):
    Entries: List[ListMapsResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_place_indexes' function.
class ListPlaceIndexesResponse(BaseValidatorModel):
    Entries: List[ListPlaceIndexesResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_route_calculators' function.
class ListRouteCalculatorsResponse(BaseValidatorModel):
    Entries: List[ListRouteCalculatorsResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_trackers' function.
class ListTrackersResponse(BaseValidatorModel):
    Entries: List[ListTrackersResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LteCellDetails(BaseValidatorModel):
    CellId: int
    Mcc: int
    Mnc: int
    LocalId: Optional[LteLocalId] = None
    NetworkMeasurements: Optional[List[LteNetworkMeasurements]] = None
    TimingAdvance: Optional[int] = None
    NrCapable: Optional[bool] = None
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None
    Tac: Optional[int] = None

MapConfigurationUnion = Union[MapConfiguration, MapConfigurationOutput]


# This class is the input for the 'update_map' function.
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


# This class is the output for the 'search_place_index_for_suggestions' function.
class SearchPlaceIndexForSuggestionsResponse(BaseValidatorModel):
    Summary: SearchPlaceIndexForSuggestionsSummary
    Results: List[SearchForSuggestionsResult]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_keys' function.
class ListKeysResponse(BaseValidatorModel):
    Entries: List[ListKeysResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_key' function.
class CreateKeyRequest(BaseValidatorModel):
    KeyName: str
    Restrictions: ApiKeyRestrictionsUnion
    Description: Optional[str] = None
    ExpireTime: Optional[Timestamp] = None
    NoExpiry: Optional[bool] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_key' function.
class UpdateKeyRequest(BaseValidatorModel):
    KeyName: str
    Description: Optional[str] = None
    ExpireTime: Optional[Timestamp] = None
    NoExpiry: Optional[bool] = None
    ForceUpdate: Optional[bool] = None
    Restrictions: Optional[ApiKeyRestrictionsUnion] = None


# This class is the output for the 'batch_delete_device_position_history' function.
class BatchDeleteDevicePositionHistoryResponse(BaseValidatorModel):
    Errors: List[BatchDeleteDevicePositionHistoryError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_geofence' function.
class BatchDeleteGeofenceResponse(BaseValidatorModel):
    Errors: List[BatchDeleteGeofenceError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_evaluate_geofences' function.
class BatchEvaluateGeofencesResponse(BaseValidatorModel):
    Errors: List[BatchEvaluateGeofencesError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_put_geofence' function.
class BatchPutGeofenceResponse(BaseValidatorModel):
    Successes: List[BatchPutGeofenceSuccess]
    Errors: List[BatchPutGeofenceError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_update_device_position' function.
class BatchUpdateDevicePositionResponse(BaseValidatorModel):
    Errors: List[BatchUpdateDevicePositionError]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'calculate_route_matrix' function.
class CalculateRouteMatrixRequest(BaseValidatorModel):
    CalculatorName: str
    DeparturePositions: List[List[float]]
    DestinationPositions: List[List[float]]
    TravelMode: Optional[TravelModeType] = None
    DepartureTime: Optional[Timestamp] = None
    DepartNow: Optional[bool] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    CarModeOptions: Optional[CalculateRouteCarModeOptions] = None
    TruckModeOptions: Optional[CalculateRouteTruckModeOptions] = None
    Key: Optional[str] = None


# This class is the input for the 'calculate_route' function.
class CalculateRouteRequest(BaseValidatorModel):
    CalculatorName: str
    DeparturePosition: List[float]
    DestinationPosition: List[float]
    WaypointPositions: Optional[List[List[float]]] = None
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


# This class is the output for the 'get_geofence' function.
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


class GeofenceGeometry(BaseValidatorModel):
    Polygon: Optional[List[List[List[float]]]] = None
    Circle: Optional[CircleUnion] = None
    Geobuf: Optional[Blob] = None


# This class is the output for the 'batch_get_device_position' function.
class BatchGetDevicePositionResponse(BaseValidatorModel):
    Errors: List[BatchGetDevicePositionError]
    DevicePositions: List[DevicePosition]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_device_position_history' function.
class GetDevicePositionHistoryResponse(BaseValidatorModel):
    DevicePositions: List[DevicePosition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'batch_evaluate_geofences' function.
class BatchEvaluateGeofencesRequest(BaseValidatorModel):
    CollectionName: str
    DevicePositionUpdates: List[DevicePositionUpdate]


# This class is the input for the 'batch_update_device_position' function.
class BatchUpdateDevicePositionRequest(BaseValidatorModel):
    TrackerName: str
    Updates: List[DevicePositionUpdate]


# This class is the output for the 'verify_device_position' function.
class VerifyDevicePositionResponse(BaseValidatorModel):
    InferredState: InferredState
    DeviceId: str
    SampleTime: datetime
    ReceivedTime: datetime
    DistanceUnit: DistanceUnitType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_device_positions' function.
class ListDevicePositionsResponse(BaseValidatorModel):
    Entries: List[ListDevicePositionsResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'calculate_route' function.
class CalculateRouteResponse(BaseValidatorModel):
    Legs: List[Leg]
    Summary: CalculateRouteSummary
    ResponseMetadata: ResponseMetadata


class CellSignals(BaseValidatorModel):
    LteCellDetails: List[LteCellDetails]


# This class is the input for the 'create_map' function.
class CreateMapRequest(BaseValidatorModel):
    MapName: str
    Configuration: MapConfigurationUnion
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_place' function.
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


# This class is the output for the 'calculate_route_matrix' function.
class CalculateRouteMatrixResponse(BaseValidatorModel):
    RouteMatrix: List[List[RouteMatrixEntry]]
    SnappedDeparturePositions: List[List[float]]
    SnappedDestinationPositions: List[List[float]]
    Summary: CalculateRouteMatrixSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_geofences' function.
class ListGeofencesResponse(BaseValidatorModel):
    Entries: List[ListGeofenceResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

GeofenceGeometryUnion = Union[GeofenceGeometry, GeofenceGeometryOutput]


class DeviceState(BaseValidatorModel):
    DeviceId: str
    SampleTime: Timestamp
    Position: List[float]
    Accuracy: Optional[PositionalAccuracy] = None
    Ipv4Address: Optional[str] = None
    WiFiAccessPoints: Optional[List[WiFiAccessPoint]] = None
    CellSignals: Optional[CellSignals] = None


# This class is the output for the 'search_place_index_for_position' function.
class SearchPlaceIndexForPositionResponse(BaseValidatorModel):
    Summary: SearchPlaceIndexForPositionSummary
    Results: List[SearchForPositionResult]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_place_index_for_text' function.
class SearchPlaceIndexForTextResponse(BaseValidatorModel):
    Summary: SearchPlaceIndexForTextSummary
    Results: List[SearchForTextResult]
    ResponseMetadata: ResponseMetadata


class BatchPutGeofenceRequestEntry(BaseValidatorModel):
    GeofenceId: str
    Geometry: GeofenceGeometryUnion
    GeofenceProperties: Optional[Dict[str, str]] = None


# This class is the input for the 'put_geofence' function.
class PutGeofenceRequest(BaseValidatorModel):
    CollectionName: str
    GeofenceId: str
    Geometry: GeofenceGeometryUnion
    GeofenceProperties: Optional[Dict[str, str]] = None


# This class is the input for the 'verify_device_position' function.
class VerifyDevicePositionRequest(BaseValidatorModel):
    TrackerName: str
    DeviceState: DeviceState
    DistanceUnit: Optional[DistanceUnitType] = None


# This class is the input for the 'batch_put_geofence' function.
class BatchPutGeofenceRequest(BaseValidatorModel):
    CollectionName: str
    Entries: List[BatchPutGeofenceRequestEntry]