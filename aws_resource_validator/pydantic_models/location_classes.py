from datetime import datetime

from botocore.response import StreamingBody

from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ApiKeyRestrictionsExtraOutputTypeDef(BaseValidatorModel):
    AllowActions: List[str]
    AllowResources: List[str]
    AllowReferers: Optional[List[str]] = None

class ApiKeyRestrictionsOutputTypeDef(BaseValidatorModel):
    AllowActions: List[str]
    AllowResources: List[str]
    AllowReferers: Optional[List[str]] = None

class ApiKeyRestrictionsTypeDef(BaseValidatorModel):
    AllowActions: Sequence[str]
    AllowResources: Sequence[str]
    AllowReferers: Optional[Sequence[str]] = None

class AssociateTrackerConsumerRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    ConsumerArn: str

class BatchItemErrorTypeDef(BaseValidatorModel):
    Code: Optional[BatchItemErrorCodeType] = None
    Message: Optional[str] = None

class BatchDeleteDevicePositionHistoryRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceIds: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchDeleteGeofenceRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    GeofenceIds: Sequence[str]

class BatchGetDevicePositionRequestRequestTypeDef(BaseValidatorModel):
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

class CircleExtraOutputTypeDef(BaseValidatorModel):
    Center: List[float]
    Radius: float

class CircleOutputTypeDef(BaseValidatorModel):
    Center: List[float]
    Radius: float

class CircleTypeDef(BaseValidatorModel):
    Center: Sequence[float]
    Radius: float

class CreateGeofenceCollectionRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyId: Optional[str] = None

class MapConfigurationTypeDef(BaseValidatorModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[Sequence[str]] = None

class DataSourceConfigurationTypeDef(BaseValidatorModel):
    IntendedUse: Optional[IntendedUseType] = None

class CreateRouteCalculatorRequestRequestTypeDef(BaseValidatorModel):
    CalculatorName: str
    DataSource: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateTrackerRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    KmsKeyId: Optional[str] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None

class DeleteGeofenceCollectionRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str

class DeleteKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyName: str
    ForceDelete: Optional[bool] = None

class DeleteMapRequestRequestTypeDef(BaseValidatorModel):
    MapName: str

class DeletePlaceIndexRequestRequestTypeDef(BaseValidatorModel):
    IndexName: str

class DeleteRouteCalculatorRequestRequestTypeDef(BaseValidatorModel):
    CalculatorName: str

class DeleteTrackerRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str

class DescribeGeofenceCollectionRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str

class DescribeKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyName: str

class DescribeMapRequestRequestTypeDef(BaseValidatorModel):
    MapName: str

class MapConfigurationOutputTypeDef(BaseValidatorModel):
    Style: str
    PoliticalView: Optional[str] = None
    CustomLayers: Optional[List[str]] = None

class DescribePlaceIndexRequestRequestTypeDef(BaseValidatorModel):
    IndexName: str

class DescribeRouteCalculatorRequestRequestTypeDef(BaseValidatorModel):
    CalculatorName: str

class DescribeTrackerRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str

class PositionalAccuracyTypeDef(BaseValidatorModel):
    Horizontal: float

class WiFiAccessPointTypeDef(BaseValidatorModel):
    MacAddress: str
    Rss: int

class DisassociateTrackerConsumerRequestRequestTypeDef(BaseValidatorModel):
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

class GetDevicePositionRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceId: str

class GetGeofenceRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    GeofenceId: str

class GetMapGlyphsRequestRequestTypeDef(BaseValidatorModel):
    MapName: str
    FontStack: str
    FontUnicodeRange: str
    Key: Optional[str] = None

class GetMapSpritesRequestRequestTypeDef(BaseValidatorModel):
    MapName: str
    FileName: str
    Key: Optional[str] = None

class GetMapStyleDescriptorRequestRequestTypeDef(BaseValidatorModel):
    MapName: str
    Key: Optional[str] = None

class GetMapTileRequestRequestTypeDef(BaseValidatorModel):
    MapName: str
    Z: str
    X: str
    Y: str
    Key: Optional[str] = None

class GetPlaceRequestRequestTypeDef(BaseValidatorModel):
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

class ListGeofenceCollectionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGeofenceCollectionsResponseEntryTypeDef(BaseValidatorModel):
    CollectionName: str
    Description: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None

class ListGeofencesRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMapsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMapsResponseEntryTypeDef(BaseValidatorModel):
    MapName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None

class ListPlaceIndexesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPlaceIndexesResponseEntryTypeDef(BaseValidatorModel):
    IndexName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None

class ListRouteCalculatorsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRouteCalculatorsResponseEntryTypeDef(BaseValidatorModel):
    CalculatorName: str
    Description: str
    DataSource: str
    CreateTime: datetime
    UpdateTime: datetime
    PricingPlan: Optional[PricingPlanType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListTrackerConsumersRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTrackersRequestRequestTypeDef(BaseValidatorModel):
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

class SearchForSuggestionsResultTypeDef(BaseValidatorModel):
    Text: str
    PlaceId: Optional[str] = None
    Categories: Optional[List[str]] = None
    SupplementalCategories: Optional[List[str]] = None

class SearchPlaceIndexForPositionRequestRequestTypeDef(BaseValidatorModel):
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

class SearchPlaceIndexForSuggestionsRequestRequestTypeDef(BaseValidatorModel):
    IndexName: str
    Text: str
    BiasPosition: Optional[Sequence[float]] = None
    FilterBBox: Optional[Sequence[float]] = None
    FilterCountries: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[Sequence[str]] = None
    Key: Optional[str] = None

class SearchPlaceIndexForSuggestionsSummaryTypeDef(BaseValidatorModel):
    Text: str
    DataSource: str
    BiasPosition: Optional[List[float]] = None
    FilterBBox: Optional[List[float]] = None
    FilterCountries: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[List[str]] = None

class SearchPlaceIndexForTextRequestRequestTypeDef(BaseValidatorModel):
    IndexName: str
    Text: str
    BiasPosition: Optional[Sequence[float]] = None
    FilterBBox: Optional[Sequence[float]] = None
    FilterCountries: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    Language: Optional[str] = None
    FilterCategories: Optional[Sequence[str]] = None
    Key: Optional[str] = None

class SearchPlaceIndexForTextSummaryTypeDef(BaseValidatorModel):
    Text: str
    DataSource: str
    BiasPosition: Optional[List[float]] = None
    FilterBBox: Optional[List[float]] = None
    FilterCountries: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    ResultBBox: Optional[List[float]] = None
    Language: Optional[str] = None
    FilterCategories: Optional[List[str]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateGeofenceCollectionRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None

class UpdateRouteCalculatorRequestRequestTypeDef(BaseValidatorModel):
    CalculatorName: str
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None

class UpdateTrackerRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    PricingPlan: Optional[PricingPlanType] = None
    PricingPlanDataSource: Optional[str] = None
    Description: Optional[str] = None
    PositionFiltering: Optional[PositionFilteringType] = None
    EventBridgeEnabled: Optional[bool] = None
    KmsKeyEnableGeospatialQueries: Optional[bool] = None

class ListKeysRequestRequestTypeDef(BaseValidatorModel):
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

class CreateKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyName: str
    Restrictions: ApiKeyRestrictionsTypeDef
    Description: Optional[str] = None
    ExpireTime: Optional[TimestampTypeDef] = None
    NoExpiry: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None

class GetDevicePositionHistoryRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceId: str
    NextToken: Optional[str] = None
    StartTimeInclusive: Optional[TimestampTypeDef] = None
    EndTimeExclusive: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None

class UpdateKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyName: str
    Description: Optional[str] = None
    ExpireTime: Optional[TimestampTypeDef] = None
    NoExpiry: Optional[bool] = None
    ForceUpdate: Optional[bool] = None
    Restrictions: Optional[ApiKeyRestrictionsTypeDef] = None

class CalculateRouteTruckModeOptionsTypeDef(BaseValidatorModel):
    AvoidFerries: Optional[bool] = None
    AvoidTolls: Optional[bool] = None
    Dimensions: Optional[TruckDimensionsTypeDef] = None
    Weight: Optional[TruckWeightTypeDef] = None

class GeofenceGeometryExtraOutputTypeDef(BaseValidatorModel):
    Polygon: Optional[List[List[List[float]]]] = None
    Circle: Optional[CircleExtraOutputTypeDef] = None
    Geobuf: Optional[bytes] = None

class GeofenceGeometryOutputTypeDef(BaseValidatorModel):
    Polygon: Optional[List[List[List[float]]]] = None
    Circle: Optional[CircleOutputTypeDef] = None
    Geobuf: Optional[bytes] = None

class GeofenceGeometryTypeDef(BaseValidatorModel):
    Polygon: Optional[Sequence[Sequence[Sequence[float]]]] = None
    Circle: Optional[CircleTypeDef] = None
    Geobuf: Optional[BlobTypeDef] = None

class CreateMapRequestRequestTypeDef(BaseValidatorModel):
    MapName: str
    Configuration: MapConfigurationTypeDef
    PricingPlan: Optional[PricingPlanType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreatePlaceIndexRequestRequestTypeDef(BaseValidatorModel):
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

class UpdatePlaceIndexRequestRequestTypeDef(BaseValidatorModel):
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

class ForecastGeofenceEventsRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    DeviceState: ForecastGeofenceEventsDeviceStateTypeDef
    TimeHorizonMinutes: Optional[float] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    SpeedUnit: Optional[SpeedUnitType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ForecastGeofenceEventsRequestForecastGeofenceEventsPaginateTypeDef(BaseValidatorModel):
    CollectionName: str
    DeviceState: ForecastGeofenceEventsDeviceStateTypeDef
    TimeHorizonMinutes: Optional[float] = None
    DistanceUnit: Optional[DistanceUnitType] = None
    SpeedUnit: Optional[SpeedUnitType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceId: str
    StartTimeInclusive: Optional[TimestampTypeDef] = None
    EndTimeExclusive: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGeofencesRequestListGeofencesPaginateTypeDef(BaseValidatorModel):
    CollectionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeysRequestListKeysPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[ApiKeyFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMapsRequestListMapsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef(BaseValidatorModel):
    TrackerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrackersRequestListTrackersPaginateTypeDef(BaseValidatorModel):
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

class ListDevicePositionsRequestListDevicePositionsPaginateTypeDef(BaseValidatorModel):
    TrackerName: str
    FilterGeometry: Optional[TrackingFilterGeometryTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicePositionsRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateMapRequestRequestTypeDef(BaseValidatorModel):
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

class SearchPlaceIndexForSuggestionsResponseTypeDef(BaseValidatorModel):
    Summary: SearchPlaceIndexForSuggestionsSummaryTypeDef
    Results: List[SearchForSuggestionsResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeysResponseTypeDef(BaseValidatorModel):
    Entries: List[ListKeysResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

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

class CalculateRouteMatrixRequestRequestTypeDef(BaseValidatorModel):
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

class CalculateRouteRequestRequestTypeDef(BaseValidatorModel):
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

class BatchPutGeofenceRequestEntryTypeDef(BaseValidatorModel):
    GeofenceId: str
    Geometry: GeofenceGeometryTypeDef
    GeofenceProperties: Optional[Mapping[str, str]] = None

class PutGeofenceRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    GeofenceId: str
    Geometry: GeofenceGeometryTypeDef
    GeofenceProperties: Optional[Mapping[str, str]] = None

class BatchGetDevicePositionResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchGetDevicePositionErrorTypeDef]
    DevicePositions: List[DevicePositionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicePositionHistoryResponseTypeDef(BaseValidatorModel):
    DevicePositions: List[DevicePositionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchEvaluateGeofencesRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    DevicePositionUpdates: Sequence[DevicePositionUpdateTypeDef]

class BatchUpdateDevicePositionRequestRequestTypeDef(BaseValidatorModel):
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

class BatchPutGeofenceRequestRequestTypeDef(BaseValidatorModel):
    CollectionName: str
    Entries: Sequence[BatchPutGeofenceRequestEntryTypeDef]

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

class SearchPlaceIndexForTextResponseTypeDef(BaseValidatorModel):
    Summary: SearchPlaceIndexForTextSummaryTypeDef
    Results: List[SearchForTextResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDevicePositionRequestRequestTypeDef(BaseValidatorModel):
    TrackerName: str
    DeviceState: DeviceStateTypeDef
    DistanceUnit: Optional[DistanceUnitType] = None

