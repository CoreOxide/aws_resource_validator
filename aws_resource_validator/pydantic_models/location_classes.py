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

class ApiKeyFilterTypeDef(BaseValidatorModel):
    KeyStatus: Optional[StatusType] = None


class ApiKeyRestrictionsOutputTypeDef(BaseValidatorModel):
    AllowActions: List[str]
    AllowResources: List[str]
    AllowReferers: Optional[List[str]] = None


class ApiKeyRestrictionsTypeDef(BaseValidatorModel):
    AllowActions: Sequence[str]
    AllowResources: Sequence[str]
    AllowReferers: Optional[Sequence[str]] = None


class AssociateTrackerConsumerRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    ConsumerArn: str


class BatchItemErrorTypeDef(BaseValidatorModel):
    Code: Optional[BatchItemErrorCodeType] = None
    Message: Optional[str] = None


class BatchDeleteDevicePositionHistoryRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceIds: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteGeofenceRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    GeofenceIds: Sequence[str]


class BatchGetDevicePositionRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceIds: Sequence[str]


class BatchPutGeofenceSuccessTypeDef(BaseValidatorModel):
    GeofenceId: str
    CreateTime: datetime
    UpdateTime: datetime


class CalculateRouteCarModeOptionsTypeDef(BaseValidatorModel):
    AvoidFerries: Optional[bool] = None
    AvoidTolls: Optional[bool] = None


class CalculateRouteMatrixSummaryTypeDef(BaseValidatorModel):
    DataSource: str
    RouteCount: int
    ErrorCount: int
    DistanceUnit: DistanceUnitType


class CalculateRouteSummaryTypeDef(BaseValidatorModel):
    RouteBBox: List[float]
    DataSource: str
    Distance: float
    DurationSeconds: float
    DistanceUnit: DistanceUnitType


class TruckDimensionsTypeDef(BaseValidatorModel):
    Length: Optional[float] = None
    Height: Optional[float] = None
    Width: Optional[float] = None
    Unit: Optional[DimensionUnitType] = None


class TruckWeightTypeDef(BaseValidatorModel):
    Total: Optional[float] = None
    Unit: Optional[VehicleWeightUnitType] = None


class CircleOutputTypeDef(BaseValidatorModel):
    Center: List[float]
    Radius: float


class CircleTypeDef(BaseValidatorModel):
    Center: Sequence[float]
    Radius: float


class CreateGeofenceCollectionRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyId: Optional[str] = None


class DataSourceConfigurationTypeDef(BaseValidatorModel):
    IntendedUse: Optional[IntendedUseType] = None


class CreateRouteCalculatorRequestTypeDef(BaseValidatorModel):
    CalculatorName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateTrackerRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    KmsKeyId: Optional[str] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None


class DeleteGeofenceCollectionRequestTypeDef(BaseValidatorModel):
    CollectionName: str


class DeleteKeyRequestTypeDef(BaseValidatorModel):
    KeyName: str
    ForceDelete: Optional[bool] = None


class DeleteMapRequestTypeDef(BaseValidatorModel):
    MapName: str


class DeletePlaceIndexRequestTypeDef(BaseValidatorModel):
    IndexName: str


class DeleteRouteCalculatorRequestTypeDef(BaseValidatorModel):
    CalculatorName: str


class DeleteTrackerRequestTypeDef(BaseValidatorModel):
    TrackerName: str


class DescribeGeofenceCollectionRequestTypeDef(BaseValidatorModel):
    CollectionName: str


class DescribeKeyRequestTypeDef(BaseValidatorModel):
    KeyName: str


class DescribeMapRequestTypeDef(BaseValidatorModel):
    MapName: str


class MapConfigurationOutputTypeDef(BaseValidatorModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[List[str]] = None


class DescribePlaceIndexRequestTypeDef(BaseValidatorModel):
    IndexName: str


class DescribeRouteCalculatorRequestTypeDef(BaseValidatorModel):
    CalculatorName: str


class DescribeTrackerRequestTypeDef(BaseValidatorModel):
    TrackerName: str


class PositionalAccuracyTypeDef(BaseValidatorModel):
    Horizontal: float


class WiFiAccessPointTypeDef(BaseValidatorModel):
    MacAddress: str
    Rss: int


class DisassociateTrackerConsumerRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    ConsumerArn: str


class ForecastGeofenceEventsDeviceStateTypeDef(BaseValidatorModel):
    Position: Sequence[float]
    Speed: Optional[float] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ForecastedEventTypeDef(BaseValidatorModel):
    EventId: str
    GeofenceId: str
    IsDeviceInGeofence: bool
    NearestDistance: float
    EventType: ForecastedGeofenceEventTypeType
    ForecastedBreachTime: Optional[datetime] = None
    GeofenceProperties: Optional[Dict[str, str]] = None


class GetDevicePositionRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceId: str


class GetGeofenceRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    GeofenceId: str


class GetMapGlyphsRequestTypeDef(BaseValidatorModel):
    MapName: str
    FontStack: str
    FontUnicodeRange: str
    Key: Optional[str] = None


class GetMapSpritesRequestTypeDef(BaseValidatorModel):
    MapName: str
    FileName: str
    Key: Optional[str] = None


class GetMapStyleDescriptorRequestTypeDef(BaseValidatorModel):
    MapName: str
    Key: Optional[str] = None


class GetMapTileRequestTypeDef(BaseValidatorModel):
    MapName: str
    Z: str
    X: str
    Y: str
    Key: Optional[str] = None


class GetPlaceRequestTypeDef(BaseValidatorModel):
    IndexName: str
    PlaceId: str
    Language: Optional[str] = None
    Key: Optional[str] = None


class LegGeometryTypeDef(BaseValidatorModel):
    LineString: Optional[List[List[float]]] = None


class StepTypeDef(BaseValidatorModel):
    StartPosition: List[float]
    EndPosition: List[float]
    Distance: float
    DurationSeconds: float
    GeometryOffset: Optional[int] = None


class TrackingFilterGeometryTypeDef(BaseValidatorModel):
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None


class ListGeofenceCollectionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGeofenceCollectionsResponseEntryTypeDef(BaseValidatorModel):
    CollectionName: str
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None


class ListGeofencesRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMapsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMapsResponseEntryTypeDef(BaseValidatorModel):
    MapName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None


class ListPlaceIndexesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPlaceIndexesResponseEntryTypeDef(BaseValidatorModel):
    IndexName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None


class ListRouteCalculatorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRouteCalculatorsResponseEntryTypeDef(BaseValidatorModel):
    CalculatorName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListTrackerConsumersRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTrackersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTrackersResponseEntryTypeDef(BaseValidatorModel):
    TrackerName: str
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None


class LteLocalIdTypeDef(BaseValidatorModel):
    Earfcn: int
    Pci: int


class LteNetworkMeasurementsTypeDef(BaseValidatorModel):
    Earfcn: int
    CellId: int
    Pci: int
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None


class MapConfigurationTypeDef(BaseValidatorModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[Sequence[str]] = None


class MapConfigurationUpdateTypeDef(BaseValidatorModel):
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[Sequence[str]] = None


class PlaceGeometryTypeDef(BaseValidatorModel):
    Point: Optional[List[float]] = None


class TimeZoneTypeDef(BaseValidatorModel):
    Name: str
    Offset: Optional[int] = None


class RouteMatrixEntryErrorTypeDef(BaseValidatorModel):
    Code: RouteMatrixErrorCodeType
    Message: Optional[str] = None


class SearchPlaceIndexForPositionRequestTypeDef(BaseValidatorModel):
    IndexName: str
    Position: Sequence[float]
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    Key: Optional[str] = None


class SearchPlaceIndexForPositionSummaryTypeDef(BaseValidatorModel):
    Position: List[float]
    DataSource: str
    MaxResults: Optional[int] = None
    Language: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateGeofenceCollectionRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None


class UpdateRouteCalculatorRequestTypeDef(BaseValidatorModel):
    CalculatorName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None


class UpdateTrackerRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None


class ListKeysRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filter: Optional[ApiKeyFilterTypeDef] = None


class ListKeysResponseEntryTypeDef(BaseValidatorModel):
    KeyName: str
    ExpireTime: datetime
    Restrictions: ApiKeyRestrictionsOutputTypeDef
    CreateTime: datetime
    UpdateTime: datetime
    Description: Optional[str] = None


class BatchDeleteDevicePositionHistoryErrorTypeDef(BaseValidatorModel):
    DeviceId: str
    Error: BatchItemErrorTypeDef


class BatchDeleteGeofenceErrorTypeDef(BaseValidatorModel):
    GeofenceId: str
    Error: BatchItemErrorTypeDef


class BatchEvaluateGeofencesErrorTypeDef(BaseValidatorModel):
    DeviceId: str
    SampleTime: datetime
    Error: BatchItemErrorTypeDef


class BatchGetDevicePositionErrorTypeDef(BaseValidatorModel):
    DeviceId: str
    Error: BatchItemErrorTypeDef


class BatchPutGeofenceErrorTypeDef(BaseValidatorModel):
    GeofenceId: str
    Error: BatchItemErrorTypeDef


class BatchUpdateDevicePositionErrorTypeDef(BaseValidatorModel):
    DeviceId: str
    SampleTime: datetime
    Error: BatchItemErrorTypeDef


class CreateGeofenceCollectionResponseTypeDef(BaseValidatorModel):
    CollectionName: str
    CollectionArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateKeyResponseTypeDef(BaseValidatorModel):
    Key: str
    KeyArn: str
    KeyName: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMapResponseTypeDef(BaseValidatorModel):
    MapName: str
    MapArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePlaceIndexResponseTypeDef(BaseValidatorModel):
    IndexName: str
    IndexArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRouteCalculatorResponseTypeDef(BaseValidatorModel):
    CalculatorName: str
    CalculatorArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTrackerResponseTypeDef(BaseValidatorModel):
    TrackerName: str
    TrackerArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeGeofenceCollectionResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeKeyResponseTypeDef(BaseValidatorModel):
    Key: str
    KeyArn: str
    KeyName: str
    Restrictions: ApiKeyRestrictionsOutputTypeDef
    CreateTime: datetime
    ExpireTime: datetime
    UpdateTime: datetime
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRouteCalculatorResponseTypeDef(BaseValidatorModel):
    CalculatorName: str
    CalculatorArn: str
    PricingPlan: PricingPlanType
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    DataSource: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTrackerResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetMapGlyphsResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMapSpritesResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMapStyleDescriptorResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMapTileResponseTypeDef(BaseValidatorModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTrackerConsumersResponseTypeDef(BaseValidatorModel):
    ConsumerArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutGeofenceResponseTypeDef(BaseValidatorModel):
    GeofenceId: str
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGeofenceCollectionResponseTypeDef(BaseValidatorModel):
    CollectionName: str
    CollectionArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateKeyResponseTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMapResponseTypeDef(BaseValidatorModel):
    MapName: str
    MapArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePlaceIndexResponseTypeDef(BaseValidatorModel):
    IndexName: str
    IndexArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRouteCalculatorResponseTypeDef(BaseValidatorModel):
    CalculatorName: str
    CalculatorArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTrackerResponseTypeDef(BaseValidatorModel):
    TrackerName: str
    TrackerArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetDevicePositionHistoryRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceId: str
    NextToken: Optional[str] = None
    StartTimeInclusive: Optional[TimestampTypeDef] = None
    EndTimeExclusive: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None


class CalculateRouteTruckModeOptionsTypeDef(BaseValidatorModel):
    AvoidFerries: Optional[bool] = None
    AvoidTolls: Optional[bool] = None
    Dimensions: Optional[TruckDimensionsTypeDef] = None
    Weight: Optional[TruckWeightTypeDef] = None


class GeofenceGeometryOutputTypeDef(BaseValidatorModel):
    Polygon: Optional[List[List[List[float]]]] = None
    Circle: Optional[CircleOutputTypeDef] = None
    Geobuf: Optional[bytes] = None


class CreatePlaceIndexRequestTypeDef(BaseValidatorModel):
    IndexName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class DescribePlaceIndexResponseTypeDef(BaseValidatorModel):
    IndexName: str
    IndexArn: str
    PricingPlan: PricingPlanType
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    DataSource: str
    DataSourceConfiguration: DataSourceConfigurationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePlaceIndexRequestTypeDef(BaseValidatorModel):
    IndexName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfigurationTypeDef] = None


class DescribeMapResponseTypeDef(BaseValidatorModel):
    MapName: str
    MapArn: str
    PricingPlan: PricingPlanType
    DataSource: str
    Configuration: MapConfigurationOutputTypeDef
    Description: str
    Tags: Dict[str, str]
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DevicePositionTypeDef(BaseValidatorModel):
    SampleTime: datetime
    ReceivedTime: datetime
    Position: List[float]
    DeviceId: Optional[str] = None
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    PositionProperties: Optional[Dict[str, str]] = None


class DevicePositionUpdateTypeDef(BaseValidatorModel):
    DeviceId: str
    SampleTime: TimestampTypeDef
    Position: Sequence[float]
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    PositionProperties: Optional[Mapping[str, str]] = None


class GetDevicePositionResponseTypeDef(BaseValidatorModel):
    DeviceId: str
    SampleTime: datetime
    ReceivedTime: datetime
    Position: List[float]
    Accuracy: PositionalAccuracyTypeDef
    PositionProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class InferredStateTypeDef(BaseValidatorModel):
    ProxyDetected: bool
    Position: Optional[List[float]] = None
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    DeviationDistance: Optional[float] = None


class ListDevicePositionsResponseEntryTypeDef(BaseValidatorModel):
    DeviceId: str
    SampleTime: datetime
    Position: List[float]
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    PositionProperties: Optional[Dict[str, str]] = None


class ForecastGeofenceEventsRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    DeviceState: ForecastGeofenceEventsDeviceStateTypeDef
    TimeHorizonMinutes: Optional[float] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    SpeedUnit: Optional[SpeedUnitType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ForecastGeofenceEventsRequestPaginateTypeDef(BaseValidatorModel):
    CollectionName: str
    DeviceState: ForecastGeofenceEventsDeviceStateTypeDef
    TimeHorizonMinutes: Optional[float] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    SpeedUnit: Optional[SpeedUnitType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDevicePositionHistoryRequestPaginateTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceId: str
    StartTimeInclusive: Optional[TimestampTypeDef] = None
    EndTimeExclusive: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGeofenceCollectionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGeofencesRequestPaginateTypeDef(BaseValidatorModel):
    CollectionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListKeysRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[ApiKeyFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMapsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPlaceIndexesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRouteCalculatorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrackerConsumersRequestPaginateTypeDef(BaseValidatorModel):
    TrackerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrackersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ForecastGeofenceEventsResponseTypeDef(BaseValidatorModel):
    ForecastedEvents: List[ForecastedEventTypeDef]
    DistanceUnit: DistanceUnitType
    SpeedUnit: SpeedUnitType
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LegTypeDef(BaseValidatorModel):
    StartPosition: List[float]
    EndPosition: List[float]
    Distance: float
    DurationSeconds: float
    Steps: List[StepTypeDef]
    Geometry: Optional[LegGeometryTypeDef] = None


class ListDevicePositionsRequestPaginateTypeDef(BaseValidatorModel):
    TrackerName: str
    FilterGeometry: Optional[TrackingFilterGeometryTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDevicePositionsRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FilterGeometry: Optional[TrackingFilterGeometryTypeDef] = None


class ListGeofenceCollectionsResponseTypeDef(BaseValidatorModel):
    Entries: List[ListGeofenceCollectionsResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMapsResponseTypeDef(BaseValidatorModel):
    Entries: List[ListMapsResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPlaceIndexesResponseTypeDef(BaseValidatorModel):
    Entries: List[ListPlaceIndexesResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRouteCalculatorsResponseTypeDef(BaseValidatorModel):
    Entries: List[ListRouteCalculatorsResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTrackersResponseTypeDef(BaseValidatorModel):
    Entries: List[ListTrackersResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LteCellDetailsTypeDef(BaseValidatorModel):
    CellId: int
    Mcc: int
    Mnc: int
    LocalId: Optional[LteLocalIdTypeDef] = None
    NetworkMeasurements: Optional[Sequence[LteNetworkMeasurementsTypeDef]] = None
    TimingAdvance: Optional[int] = None
    NrCapable: Optional[bool] = None
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None
    Tac: Optional[int] = None


class UpdateMapRequestTypeDef(BaseValidatorModel):
    MapName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    ConfigurationUpdate: Optional[MapConfigurationUpdateTypeDef] = None


class PlaceTypeDef(BaseValidatorModel):
    Geometry: PlaceGeometryTypeDef
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
    TimeZone: Optional[TimeZoneTypeDef] = None
    UnitType: Optional[str] = None
    UnitNumber: Optional[str] = None
    Categories: Optional[List[str]] = None
    SupplementalCategories: Optional[List[str]] = None
    SubMunicipality: Optional[str] = None


class RouteMatrixEntryTypeDef(BaseValidatorModel):
    Distance: Optional[float] = None
    DurationSeconds: Optional[float] = None
    Error: Optional[RouteMatrixEntryErrorTypeDef] = None


class SearchForSuggestionsResultTypeDef(BaseValidatorModel):
    pass


class SearchPlaceIndexForSuggestionsSummaryTypeDef(BaseValidatorModel):
    pass


class SearchPlaceIndexForSuggestionsResponseTypeDef(BaseValidatorModel):
    Summary: SearchPlaceIndexForSuggestionsSummaryTypeDef
    Results: List[SearchForSuggestionsResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListKeysResponseTypeDef(BaseValidatorModel):
    Entries: List[ListKeysResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ApiKeyRestrictionsUnionTypeDef(BaseValidatorModel):
    pass


class CreateKeyRequestTypeDef(BaseValidatorModel):
    KeyName: str
    Restrictions: ApiKeyRestrictionsUnionTypeDef
    Description: Optional[str] = None
    ExpireTime: Optional[TimestampTypeDef] = None
    NoExpiry: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateKeyRequestTypeDef(BaseValidatorModel):
    KeyName: str
    Description: Optional[str] = None
    ExpireTime: Optional[TimestampTypeDef] = None
    NoExpiry: Optional[bool] = None
    ForceUpdate: Optional[bool] = None
    Restrictions: Optional[ApiKeyRestrictionsUnionTypeDef] = None


class BatchDeleteDevicePositionHistoryResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchDeleteDevicePositionHistoryErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteGeofenceResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchDeleteGeofenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchEvaluateGeofencesResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchEvaluateGeofencesErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchPutGeofenceResponseTypeDef(BaseValidatorModel):
    Successes: List[BatchPutGeofenceSuccessTypeDef]
    Errors: List[BatchPutGeofenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdateDevicePositionResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchUpdateDevicePositionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CalculateRouteMatrixRequestTypeDef(BaseValidatorModel):
    CalculatorName: str
    DeparturePositions: Sequence[Sequence[float]]
    DestinationPositions: Sequence[Sequence[float]]
    TravelMode: Optional[TravelModeType] = None
    DepartureTime: Optional[TimestampTypeDef] = None
    DepartNow: Optional[bool] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    CarModeOptions: Optional[CalculateRouteCarModeOptionsTypeDef] = None
    TruckModeOptions: Optional[CalculateRouteTruckModeOptionsTypeDef] = None
    Key: Optional[str] = None


class CalculateRouteRequestTypeDef(BaseValidatorModel):
    CalculatorName: str
    DeparturePosition: Sequence[float]
    DestinationPosition: Sequence[float]
    WaypointPositions: Optional[Sequence[Sequence[float]]] = None
    TravelMode: Optional[TravelModeType] = None
    DepartureTime: Optional[TimestampTypeDef] = None
    DepartNow: Optional[bool] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    IncludeLegGeometry: Optional[bool] = None
    CarModeOptions: Optional[CalculateRouteCarModeOptionsTypeDef] = None
    TruckModeOptions: Optional[CalculateRouteTruckModeOptionsTypeDef] = None
    ArrivalTime: Optional[TimestampTypeDef] = None
    OptimizeFor: Optional[OptimizationModeType] = None
    Key: Optional[str] = None


class GetGeofenceResponseTypeDef(BaseValidatorModel):
    GeofenceId: str
    Geometry: GeofenceGeometryOutputTypeDef
    Status: str
    CreateTime: datetime
    UpdateTime: datetime
    GeofenceProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListGeofenceResponseEntryTypeDef(BaseValidatorModel):
    GeofenceId: str
    Geometry: GeofenceGeometryOutputTypeDef
    Status: str
    CreateTime: datetime
    UpdateTime: datetime
    GeofenceProperties: Optional[Dict[str, str]] = None


class CircleUnionTypeDef(BaseValidatorModel):
    pass


class BlobTypeDef(BaseValidatorModel):
    pass


class GeofenceGeometryTypeDef(BaseValidatorModel):
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None
    Circle: Optional[CircleUnionTypeDef] = None
    Geobuf: Optional[BlobTypeDef] = None


class BatchGetDevicePositionResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchGetDevicePositionErrorTypeDef]
    DevicePositions: List[DevicePositionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDevicePositionHistoryResponseTypeDef(BaseValidatorModel):
    DevicePositions: List[DevicePositionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchEvaluateGeofencesRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    DevicePositionUpdates: Sequence[DevicePositionUpdateTypeDef]


class BatchUpdateDevicePositionRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    Updates: Sequence[DevicePositionUpdateTypeDef]


class VerifyDevicePositionResponseTypeDef(BaseValidatorModel):
    InferredState: InferredStateTypeDef
    DeviceId: str
    SampleTime: datetime
    ReceivedTime: datetime
    DistanceUnit: DistanceUnitType
    ResponseMetadata: ResponseMetadataTypeDef


class ListDevicePositionsResponseTypeDef(BaseValidatorModel):
    Entries: List[ListDevicePositionsResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CalculateRouteResponseTypeDef(BaseValidatorModel):
    Legs: List[LegTypeDef]
    Summary: CalculateRouteSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CellSignalsTypeDef(BaseValidatorModel):
    LteCellDetails: Sequence[LteCellDetailsTypeDef]


class MapConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateMapRequestTypeDef(BaseValidatorModel):
    MapName: str
    Configuration: MapConfigurationUnionTypeDef
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class GetPlaceResponseTypeDef(BaseValidatorModel):
    Place: PlaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SearchForPositionResultTypeDef(BaseValidatorModel):
    Place: PlaceTypeDef
    Distance: float
    PlaceId: Optional[str] = None


class SearchForTextResultTypeDef(BaseValidatorModel):
    Place: PlaceTypeDef
    Distance: Optional[float] = None
    Relevance: Optional[float] = None
    PlaceId: Optional[str] = None


class CalculateRouteMatrixResponseTypeDef(BaseValidatorModel):
    RouteMatrix: List[List[RouteMatrixEntryTypeDef]]
    SnappedDeparturePositions: List[List[float]]
    SnappedDestinationPositions: List[List[float]]
    Summary: CalculateRouteMatrixSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListGeofencesResponseTypeDef(BaseValidatorModel):
    Entries: List[ListGeofenceResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DeviceStateTypeDef(BaseValidatorModel):
    DeviceId: str
    SampleTime: TimestampTypeDef
    Position: Sequence[float]
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    Ipv4Address: Optional[str] = None
    WiFiAccessPoints: Optional[Sequence[WiFiAccessPointTypeDef]] = None
    CellSignals: Optional[CellSignalsTypeDef] = None


class SearchPlaceIndexForPositionResponseTypeDef(BaseValidatorModel):
    Summary: SearchPlaceIndexForPositionSummaryTypeDef
    Results: List[SearchForPositionResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SearchPlaceIndexForTextSummaryTypeDef(BaseValidatorModel):
    pass


class SearchPlaceIndexForTextResponseTypeDef(BaseValidatorModel):
    Summary: SearchPlaceIndexForTextSummaryTypeDef
    Results: List[SearchForTextResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GeofenceGeometryUnionTypeDef(BaseValidatorModel):
    pass


class BatchPutGeofenceRequestEntryTypeDef(BaseValidatorModel):
    GeofenceId: str
    Geometry: GeofenceGeometryUnionTypeDef
    GeofenceProperties: Optional[Mapping[str, str]] = None


class PutGeofenceRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    GeofenceId: str
    Geometry: GeofenceGeometryUnionTypeDef
    GeofenceProperties: Optional[Mapping[str, str]] = None


class VerifyDevicePositionRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceState: DeviceStateTypeDef
    DistanceUnit: Optional[DistanceUnitType] = None


class BatchPutGeofenceRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    Entries: Sequence[BatchPutGeofenceRequestEntryTypeDef]


