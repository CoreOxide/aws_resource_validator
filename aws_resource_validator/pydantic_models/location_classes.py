from datetime import datetime
from pydantic import BaseModel
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

class ApiKeyFilterTypeDef(BaseModel):
    KeyStatus: Optional[StatusType] = None

class ApiKeyRestrictionsExtraOutputTypeDef(BaseModel):
    AllowActions: List[str]
    AllowResources: List[str]
    AllowReferers: Optional[List[str]] = None

class ApiKeyRestrictionsOutputTypeDef(BaseModel):
    AllowActions: List[str]
    AllowResources: List[str]
    AllowReferers: Optional[List[str]] = None

class ApiKeyRestrictionsTypeDef(BaseModel):
    AllowActions: Sequence[str]
    AllowResources: Sequence[str]
    AllowReferers: Optional[Sequence[str]] = None

class AssociateTrackerConsumerRequestRequestTypeDef(BaseModel):
    TrackerName: str
    ConsumerArn: str

class BatchItemErrorTypeDef(BaseModel):
    Code: Optional[BatchItemErrorCodeType] = None
    Message: Optional[str] = None

class BatchDeleteDevicePositionHistoryRequestRequestTypeDef(BaseModel):
    TrackerName: str
    DeviceIds: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchDeleteGeofenceRequestRequestTypeDef(BaseModel):
    CollectionName: str
    GeofenceIds: Sequence[str]

class BatchGetDevicePositionRequestRequestTypeDef(BaseModel):
    TrackerName: str
    DeviceIds: Sequence[str]

class BatchPutGeofenceSuccessTypeDef(BaseModel):
    GeofenceId: str
    CreateTime: datetime
    UpdateTime: datetime

class CalculateRouteCarModeOptionsTypeDef(BaseModel):
    AvoidFerries: Optional[bool] = None
    AvoidTolls: Optional[bool] = None

class CalculateRouteMatrixSummaryTypeDef(BaseModel):
    DataSource: str
    RouteCount: int
    ErrorCount: int
    DistanceUnit: DistanceUnitType

class CalculateRouteSummaryTypeDef(BaseModel):
    RouteBBox: List[float]
    DataSource: str
    Distance: float
    DurationSeconds: float
    DistanceUnit: DistanceUnitType

class TruckDimensionsTypeDef(BaseModel):
    Length: Optional[float] = None
    Height: Optional[float] = None
    Width: Optional[float] = None
    Unit: Optional[DimensionUnitType] = None

class TruckWeightTypeDef(BaseModel):
    Total: Optional[float] = None
    Unit: Optional[VehicleWeightUnitType] = None

class CircleExtraOutputTypeDef(BaseModel):
    Center: List[float]
    Radius: float

class CircleOutputTypeDef(BaseModel):
    Center: List[float]
    Radius: float

class CircleTypeDef(BaseModel):
    Center: Sequence[float]
    Radius: float

class CreateGeofenceCollectionRequestRequestTypeDef(BaseModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyId: Optional[str] = None

class MapConfigurationTypeDef(BaseModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[Sequence[str]] = None

class DataSourceConfigurationTypeDef(BaseModel):
    IntendedUse: Optional[IntendedUseType] = None

class CreateRouteCalculatorRequestRequestTypeDef(BaseModel):
    CalculatorName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateTrackerRequestRequestTypeDef(BaseModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    KmsKeyId: Optional[str] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None

class DeleteGeofenceCollectionRequestRequestTypeDef(BaseModel):
    CollectionName: str

class DeleteKeyRequestRequestTypeDef(BaseModel):
    KeyName: str
    ForceDelete: Optional[bool] = None

class DeleteMapRequestRequestTypeDef(BaseModel):
    MapName: str

class DeletePlaceIndexRequestRequestTypeDef(BaseModel):
    IndexName: str

class DeleteRouteCalculatorRequestRequestTypeDef(BaseModel):
    CalculatorName: str

class DeleteTrackerRequestRequestTypeDef(BaseModel):
    TrackerName: str

class DescribeGeofenceCollectionRequestRequestTypeDef(BaseModel):
    CollectionName: str

class DescribeKeyRequestRequestTypeDef(BaseModel):
    KeyName: str

class DescribeMapRequestRequestTypeDef(BaseModel):
    MapName: str

class MapConfigurationOutputTypeDef(BaseModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[List[str]] = None

class DescribePlaceIndexRequestRequestTypeDef(BaseModel):
    IndexName: str

class DescribeRouteCalculatorRequestRequestTypeDef(BaseModel):
    CalculatorName: str

class DescribeTrackerRequestRequestTypeDef(BaseModel):
    TrackerName: str

class PositionalAccuracyTypeDef(BaseModel):
    Horizontal: float

class WiFiAccessPointTypeDef(BaseModel):
    MacAddress: str
    Rss: int

class DisassociateTrackerConsumerRequestRequestTypeDef(BaseModel):
    TrackerName: str
    ConsumerArn: str

class ForecastGeofenceEventsDeviceStateTypeDef(BaseModel):
    Position: Sequence[float]
    Speed: Optional[float] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ForecastedEventTypeDef(BaseModel):
    EventId: str
    GeofenceId: str
    IsDeviceInGeofence: bool
    NearestDistance: float
    EventType: ForecastedGeofenceEventTypeType
    ForecastedBreachTime: Optional[datetime] = None
    GeofenceProperties: Optional[Dict[str, str]] = None

class GetDevicePositionRequestRequestTypeDef(BaseModel):
    TrackerName: str
    DeviceId: str

class GetGeofenceRequestRequestTypeDef(BaseModel):
    CollectionName: str
    GeofenceId: str

class GetMapGlyphsRequestRequestTypeDef(BaseModel):
    MapName: str
    FontStack: str
    FontUnicodeRange: str
    Key: Optional[str] = None

class GetMapSpritesRequestRequestTypeDef(BaseModel):
    MapName: str
    FileName: str
    Key: Optional[str] = None

class GetMapStyleDescriptorRequestRequestTypeDef(BaseModel):
    MapName: str
    Key: Optional[str] = None

class GetMapTileRequestRequestTypeDef(BaseModel):
    MapName: str
    Z: str
    X: str
    Y: str
    Key: Optional[str] = None

class GetPlaceRequestRequestTypeDef(BaseModel):
    IndexName: str
    PlaceId: str
    Language: Optional[str] = None
    Key: Optional[str] = None

class LegGeometryTypeDef(BaseModel):
    LineString: Optional[List[List[float]]] = None

class StepTypeDef(BaseModel):
    StartPosition: List[float]
    EndPosition: List[float]
    Distance: float
    DurationSeconds: float
    GeometryOffset: Optional[int] = None

class TrackingFilterGeometryTypeDef(BaseModel):
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None

class ListGeofenceCollectionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGeofenceCollectionsResponseEntryTypeDef(BaseModel):
    CollectionName: str
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None

class ListGeofencesRequestRequestTypeDef(BaseModel):
    CollectionName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMapsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMapsResponseEntryTypeDef(BaseModel):
    MapName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None

class ListPlaceIndexesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPlaceIndexesResponseEntryTypeDef(BaseModel):
    IndexName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None

class ListRouteCalculatorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRouteCalculatorsResponseEntryTypeDef(BaseModel):
    CalculatorName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListTrackerConsumersRequestRequestTypeDef(BaseModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTrackersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTrackersResponseEntryTypeDef(BaseModel):
    TrackerName: str
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None

class LteLocalIdTypeDef(BaseModel):
    Earfcn: int
    Pci: int

class LteNetworkMeasurementsTypeDef(BaseModel):
    Earfcn: int
    CellId: int
    Pci: int
    Rsrp: Optional[int] = None
    Rsrq: Optional[float] = None

class MapConfigurationUpdateTypeDef(BaseModel):
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[Sequence[str]] = None

class PlaceGeometryTypeDef(BaseModel):
    Point: Optional[List[float]] = None

class TimeZoneTypeDef(BaseModel):
    Name: str
    Offset: Optional[int] = None

class RouteMatrixEntryErrorTypeDef(BaseModel):
    Code: RouteMatrixErrorCodeType
    Message: Optional[str] = None

class SearchForSuggestionsResultTypeDef(BaseModel):
    Text: str
    PlaceId: Optional[str] = None
    Categories: Optional[List[str]] = None
    SupplementalCategories: Optional[List[str]] = None

class SearchPlaceIndexForPositionRequestRequestTypeDef(BaseModel):
    IndexName: str
    Position: Sequence[float]
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    Key: Optional[str] = None

class SearchPlaceIndexForPositionSummaryTypeDef(BaseModel):
    Position: List[float]
    DataSource: str
    MaxResults: Optional[int] = None
    Language: Optional[str] = None

class SearchPlaceIndexForSuggestionsRequestRequestTypeDef(BaseModel):
    IndexName: str
    Text: str
    BiasPosition: Optional[Sequence[float]] = None
    FilterBBox: Optional[Sequence[float]] = None
    FilterCountries: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[Sequence[str]] = None
    Key: Optional[str] = None

class SearchPlaceIndexForSuggestionsSummaryTypeDef(BaseModel):
    Text: str
    DataSource: str
    BiasPosition: Optional[List[float]] = None
    FilterBBox: Optional[List[float]] = None
    FilterCountries: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[List[str]] = None

class SearchPlaceIndexForTextRequestRequestTypeDef(BaseModel):
    IndexName: str
    Text: str
    BiasPosition: Optional[Sequence[float]] = None
    FilterBBox: Optional[Sequence[float]] = None
    FilterCountries: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[Sequence[str]] = None
    Key: Optional[str] = None

class SearchPlaceIndexForTextSummaryTypeDef(BaseModel):
    Text: str
    DataSource: str
    BiasPosition: Optional[List[float]] = None
    FilterBBox: Optional[List[float]] = None
    FilterCountries: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    ResultBBox: Optional[List[float]] = None
    Language: Optional[str] = None
    FilterCategories: Optional[List[str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateGeofenceCollectionRequestRequestTypeDef(BaseModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None

class UpdateRouteCalculatorRequestRequestTypeDef(BaseModel):
    CalculatorName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None

class UpdateTrackerRequestRequestTypeDef(BaseModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None

class ListKeysRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filter: Optional[ApiKeyFilterTypeDef] = None

class ListKeysResponseEntryTypeDef(BaseModel):
    KeyName: str
    ExpireTime: datetime
    Restrictions: ApiKeyRestrictionsOutputTypeDef
    CreateTime: datetime
    UpdateTime: datetime
    Description: Optional[str] = None

class BatchDeleteDevicePositionHistoryErrorTypeDef(BaseModel):
    DeviceId: str
    Error: BatchItemErrorTypeDef

class BatchDeleteGeofenceErrorTypeDef(BaseModel):
    GeofenceId: str
    Error: BatchItemErrorTypeDef

class BatchEvaluateGeofencesErrorTypeDef(BaseModel):
    DeviceId: str
    SampleTime: datetime
    Error: BatchItemErrorTypeDef

class BatchGetDevicePositionErrorTypeDef(BaseModel):
    DeviceId: str
    Error: BatchItemErrorTypeDef

class BatchPutGeofenceErrorTypeDef(BaseModel):
    GeofenceId: str
    Error: BatchItemErrorTypeDef

class BatchUpdateDevicePositionErrorTypeDef(BaseModel):
    DeviceId: str
    SampleTime: datetime
    Error: BatchItemErrorTypeDef

class CreateGeofenceCollectionResponseTypeDef(BaseModel):
    CollectionName: str
    CollectionArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKeyResponseTypeDef(BaseModel):
    Key: str
    KeyArn: str
    KeyName: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMapResponseTypeDef(BaseModel):
    MapName: str
    MapArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePlaceIndexResponseTypeDef(BaseModel):
    IndexName: str
    IndexArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteCalculatorResponseTypeDef(BaseModel):
    CalculatorName: str
    CalculatorArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrackerResponseTypeDef(BaseModel):
    TrackerName: str
    TrackerArn: str
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGeofenceCollectionResponseTypeDef(BaseModel):
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

class DescribeKeyResponseTypeDef(BaseModel):
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

class DescribeRouteCalculatorResponseTypeDef(BaseModel):
    CalculatorName: str
    CalculatorArn: str
    PricingPlan: PricingPlanType
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    DataSource: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrackerResponseTypeDef(BaseModel):
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

class GetMapGlyphsResponseTypeDef(BaseModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMapSpritesResponseTypeDef(BaseModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMapStyleDescriptorResponseTypeDef(BaseModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMapTileResponseTypeDef(BaseModel):
    Blob: StreamingBody
    ContentType: str
    CacheControl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrackerConsumersResponseTypeDef(BaseModel):
    ConsumerArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutGeofenceResponseTypeDef(BaseModel):
    GeofenceId: str
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeofenceCollectionResponseTypeDef(BaseModel):
    CollectionName: str
    CollectionArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKeyResponseTypeDef(BaseModel):
    KeyArn: str
    KeyName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMapResponseTypeDef(BaseModel):
    MapName: str
    MapArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePlaceIndexResponseTypeDef(BaseModel):
    IndexName: str
    IndexArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouteCalculatorResponseTypeDef(BaseModel):
    CalculatorName: str
    CalculatorArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrackerResponseTypeDef(BaseModel):
    TrackerName: str
    TrackerArn: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKeyRequestRequestTypeDef(BaseModel):
    KeyName: str
    Restrictions: ApiKeyRestrictionsTypeDef
    Description: Optional[str] = None
    ExpireTime: Optional[TimestampTypeDef] = None
    NoExpiry: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None

class GetDevicePositionHistoryRequestRequestTypeDef(BaseModel):
    TrackerName: str
    DeviceId: str
    NextToken: Optional[str] = None
    StartTimeInclusive: Optional[TimestampTypeDef] = None
    EndTimeExclusive: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None

class UpdateKeyRequestRequestTypeDef(BaseModel):
    KeyName: str
    Description: Optional[str] = None
    ExpireTime: Optional[TimestampTypeDef] = None
    NoExpiry: Optional[bool] = None
    ForceUpdate: Optional[bool] = None
    Restrictions: Optional[ApiKeyRestrictionsTypeDef] = None

class CalculateRouteTruckModeOptionsTypeDef(BaseModel):
    AvoidFerries: Optional[bool] = None
    AvoidTolls: Optional[bool] = None
    Dimensions: Optional[TruckDimensionsTypeDef] = None
    Weight: Optional[TruckWeightTypeDef] = None

class GeofenceGeometryExtraOutputTypeDef(BaseModel):
    Polygon: Optional[List[List[List[float]]]] = None
    Circle: Optional[CircleExtraOutputTypeDef] = None
    Geobuf: Optional[bytes] = None

class GeofenceGeometryOutputTypeDef(BaseModel):
    Polygon: Optional[List[List[List[float]]]] = None
    Circle: Optional[CircleOutputTypeDef] = None
    Geobuf: Optional[bytes] = None

class GeofenceGeometryTypeDef(BaseModel):
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None
    Circle: Optional[CircleTypeDef] = None
    Geobuf: Optional[BlobTypeDef] = None

class CreateMapRequestRequestTypeDef(BaseModel):
    MapName: str
    Configuration: MapConfigurationTypeDef
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreatePlaceIndexRequestRequestTypeDef(BaseModel):
    IndexName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class DescribePlaceIndexResponseTypeDef(BaseModel):
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

class UpdatePlaceIndexRequestRequestTypeDef(BaseModel):
    IndexName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    DataSourceConfiguration: Optional[DataSourceConfigurationTypeDef] = None

class DescribeMapResponseTypeDef(BaseModel):
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

class DevicePositionTypeDef(BaseModel):
    SampleTime: datetime
    ReceivedTime: datetime
    Position: List[float]
    DeviceId: Optional[str] = None
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    PositionProperties: Optional[Dict[str, str]] = None

class DevicePositionUpdateTypeDef(BaseModel):
    DeviceId: str
    SampleTime: TimestampTypeDef
    Position: Sequence[float]
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    PositionProperties: Optional[Mapping[str, str]] = None

class GetDevicePositionResponseTypeDef(BaseModel):
    DeviceId: str
    SampleTime: datetime
    ReceivedTime: datetime
    Position: List[float]
    Accuracy: PositionalAccuracyTypeDef
    PositionProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class InferredStateTypeDef(BaseModel):
    ProxyDetected: bool
    Position: Optional[List[float]] = None
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    DeviationDistance: Optional[float] = None

class ListDevicePositionsResponseEntryTypeDef(BaseModel):
    DeviceId: str
    SampleTime: datetime
    Position: List[float]
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    PositionProperties: Optional[Dict[str, str]] = None

class ForecastGeofenceEventsRequestRequestTypeDef(BaseModel):
    CollectionName: str
    DeviceState: ForecastGeofenceEventsDeviceStateTypeDef
    TimeHorizonMinutes: Optional[float] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    SpeedUnit: Optional[SpeedUnitType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ForecastGeofenceEventsRequestForecastGeofenceEventsPaginateTypeDef(BaseModel):
    CollectionName: str
    DeviceState: ForecastGeofenceEventsDeviceStateTypeDef
    TimeHorizonMinutes: Optional[float] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    SpeedUnit: Optional[SpeedUnitType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef(BaseModel):
    TrackerName: str
    DeviceId: str
    StartTimeInclusive: Optional[TimestampTypeDef] = None
    EndTimeExclusive: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGeofencesRequestListGeofencesPaginateTypeDef(BaseModel):
    CollectionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeysRequestListKeysPaginateTypeDef(BaseModel):
    Filter: Optional[ApiKeyFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMapsRequestListMapsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef(BaseModel):
    TrackerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrackersRequestListTrackersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ForecastGeofenceEventsResponseTypeDef(BaseModel):
    ForecastedEvents: List[ForecastedEventTypeDef]
    DistanceUnit: DistanceUnitType
    SpeedUnit: SpeedUnitType
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LegTypeDef(BaseModel):
    StartPosition: List[float]
    EndPosition: List[float]
    Distance: float
    DurationSeconds: float
    Steps: List[StepTypeDef]
    Geometry: Optional[LegGeometryTypeDef] = None

class ListDevicePositionsRequestListDevicePositionsPaginateTypeDef(BaseModel):
    TrackerName: str
    FilterGeometry: Optional[TrackingFilterGeometryTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicePositionsRequestRequestTypeDef(BaseModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FilterGeometry: Optional[TrackingFilterGeometryTypeDef] = None

class ListGeofenceCollectionsResponseTypeDef(BaseModel):
    Entries: List[ListGeofenceCollectionsResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMapsResponseTypeDef(BaseModel):
    Entries: List[ListMapsResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPlaceIndexesResponseTypeDef(BaseModel):
    Entries: List[ListPlaceIndexesResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRouteCalculatorsResponseTypeDef(BaseModel):
    Entries: List[ListRouteCalculatorsResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrackersResponseTypeDef(BaseModel):
    Entries: List[ListTrackersResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LteCellDetailsTypeDef(BaseModel):
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

class UpdateMapRequestRequestTypeDef(BaseModel):
    MapName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    ConfigurationUpdate: Optional[MapConfigurationUpdateTypeDef] = None

class PlaceTypeDef(BaseModel):
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

class RouteMatrixEntryTypeDef(BaseModel):
    Distance: Optional[float] = None
    DurationSeconds: Optional[float] = None
    Error: Optional[RouteMatrixEntryErrorTypeDef] = None

class SearchPlaceIndexForSuggestionsResponseTypeDef(BaseModel):
    Summary: SearchPlaceIndexForSuggestionsSummaryTypeDef
    Results: List[SearchForSuggestionsResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeysResponseTypeDef(BaseModel):
    Entries: List[ListKeysResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchDeleteDevicePositionHistoryResponseTypeDef(BaseModel):
    Errors: List[BatchDeleteDevicePositionHistoryErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteGeofenceResponseTypeDef(BaseModel):
    Errors: List[BatchDeleteGeofenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEvaluateGeofencesResponseTypeDef(BaseModel):
    Errors: List[BatchEvaluateGeofencesErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutGeofenceResponseTypeDef(BaseModel):
    Successes: List[BatchPutGeofenceSuccessTypeDef]
    Errors: List[BatchPutGeofenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateDevicePositionResponseTypeDef(BaseModel):
    Errors: List[BatchUpdateDevicePositionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CalculateRouteMatrixRequestRequestTypeDef(BaseModel):
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

class CalculateRouteRequestRequestTypeDef(BaseModel):
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

class GetGeofenceResponseTypeDef(BaseModel):
    GeofenceId: str
    Geometry: GeofenceGeometryOutputTypeDef
    Status: str
    CreateTime: datetime
    UpdateTime: datetime
    GeofenceProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGeofenceResponseEntryTypeDef(BaseModel):
    GeofenceId: str
    Geometry: GeofenceGeometryOutputTypeDef
    Status: str
    CreateTime: datetime
    UpdateTime: datetime
    GeofenceProperties: Optional[Dict[str, str]] = None

class BatchPutGeofenceRequestEntryTypeDef(BaseModel):
    GeofenceId: str
    Geometry: GeofenceGeometryTypeDef
    GeofenceProperties: Optional[Mapping[str, str]] = None

class PutGeofenceRequestRequestTypeDef(BaseModel):
    CollectionName: str
    GeofenceId: str
    Geometry: GeofenceGeometryTypeDef
    GeofenceProperties: Optional[Mapping[str, str]] = None

class BatchGetDevicePositionResponseTypeDef(BaseModel):
    Errors: List[BatchGetDevicePositionErrorTypeDef]
    DevicePositions: List[DevicePositionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicePositionHistoryResponseTypeDef(BaseModel):
    DevicePositions: List[DevicePositionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchEvaluateGeofencesRequestRequestTypeDef(BaseModel):
    CollectionName: str
    DevicePositionUpdates: Sequence[DevicePositionUpdateTypeDef]

class BatchUpdateDevicePositionRequestRequestTypeDef(BaseModel):
    TrackerName: str
    Updates: Sequence[DevicePositionUpdateTypeDef]

class VerifyDevicePositionResponseTypeDef(BaseModel):
    InferredState: InferredStateTypeDef
    DeviceId: str
    SampleTime: datetime
    ReceivedTime: datetime
    DistanceUnit: DistanceUnitType
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicePositionsResponseTypeDef(BaseModel):
    Entries: List[ListDevicePositionsResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CalculateRouteResponseTypeDef(BaseModel):
    Legs: List[LegTypeDef]
    Summary: CalculateRouteSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CellSignalsTypeDef(BaseModel):
    LteCellDetails: Sequence[LteCellDetailsTypeDef]

class GetPlaceResponseTypeDef(BaseModel):
    Place: PlaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchForPositionResultTypeDef(BaseModel):
    Place: PlaceTypeDef
    Distance: float
    PlaceId: Optional[str] = None

class SearchForTextResultTypeDef(BaseModel):
    Place: PlaceTypeDef
    Distance: Optional[float] = None
    Relevance: Optional[float] = None
    PlaceId: Optional[str] = None

class CalculateRouteMatrixResponseTypeDef(BaseModel):
    RouteMatrix: List[List[RouteMatrixEntryTypeDef]]
    SnappedDeparturePositions: List[List[float]]
    SnappedDestinationPositions: List[List[float]]
    Summary: CalculateRouteMatrixSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGeofencesResponseTypeDef(BaseModel):
    Entries: List[ListGeofenceResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchPutGeofenceRequestRequestTypeDef(BaseModel):
    CollectionName: str
    Entries: Sequence[BatchPutGeofenceRequestEntryTypeDef]

class DeviceStateTypeDef(BaseModel):
    DeviceId: str
    SampleTime: TimestampTypeDef
    Position: Sequence[float]
    Accuracy: Optional[PositionalAccuracyTypeDef] = None
    Ipv4Address: Optional[str] = None
    WiFiAccessPoints: Optional[Sequence[WiFiAccessPointTypeDef]] = None
    CellSignals: Optional[CellSignalsTypeDef] = None

class SearchPlaceIndexForPositionResponseTypeDef(BaseModel):
    Summary: SearchPlaceIndexForPositionSummaryTypeDef
    Results: List[SearchForPositionResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchPlaceIndexForTextResponseTypeDef(BaseModel):
    Summary: SearchPlaceIndexForTextSummaryTypeDef
    Results: List[SearchForTextResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDevicePositionRequestRequestTypeDef(BaseModel):
    TrackerName: str
    DeviceState: DeviceStateTypeDef
    DistanceUnit: Optional[DistanceUnitType] = None

