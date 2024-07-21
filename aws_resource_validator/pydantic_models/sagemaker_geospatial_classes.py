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
from aws_resource_validator.pydantic_models.sagemaker_geospatial_constants import *

class MultiPolygonGeometryInputTypeDef(BaseModel):
    Coordinates: List[List[List[List[float]]]]

class PolygonGeometryInputTypeDef(BaseModel):
    Coordinates: List[List[List[float]]]

class AssetValueTypeDef(BaseModel):
    Href: Optional[str] = None

class CloudRemovalConfigInputTypeDef(BaseModel):
    AlgorithmName: Optional[Literal["INTERPOLATION"]] = None
    InterpolationValue: Optional[str] = None
    TargetBands: Optional[List[str]] = None

class OperationTypeDef(BaseModel):
    Equation: str
    Name: str
    OutputType: Optional[OutputTypeType] = None

class DeleteEarthObservationJobInputRequestTypeDef(BaseModel):
    Arn: str

class DeleteVectorEnrichmentJobInputRequestTypeDef(BaseModel):
    Arn: str

class EarthObservationJobErrorDetailsTypeDef(BaseModel):
    Message: Optional[str] = None
    Type: Optional[EarthObservationJobErrorTypeType] = None

class EoCloudCoverInputTypeDef(BaseModel):
    LowerBound: float
    UpperBound: float

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ExportErrorDetailsOutputTypeDef(BaseModel):
    Message: Optional[str] = None
    Type: Optional[ExportErrorTypeType] = None

class ExportS3DataInputTypeDef(BaseModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class VectorEnrichmentJobS3DataTypeDef(BaseModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class FilterTypeDef(BaseModel):
    Name: str
    Type: str
    Maximum: Optional[float] = None
    Minimum: Optional[float] = None

class GeoMosaicConfigInputTypeDef(BaseModel):
    AlgorithmName: Optional[AlgorithmNameGeoMosaicType] = None
    TargetBands: Optional[List[str]] = None

class GeometryTypeDef(BaseModel):
    Coordinates: List[List[List[float]]]
    Type: str

class GetEarthObservationJobInputRequestTypeDef(BaseModel):
    Arn: str

class OutputBandTypeDef(BaseModel):
    BandName: str
    OutputDataType: OutputTypeType

class GetRasterDataCollectionInputRequestTypeDef(BaseModel):
    Arn: str

class GetTileInputRequestTypeDef(BaseModel):
    Arn: str
    ImageAssets: Sequence[str]
    Target: TargetOptionsType
    x: int
    y: int
    z: int
    ExecutionRoleArn: Optional[str] = None
    ImageMask: Optional[bool] = None
    OutputDataType: Optional[OutputTypeType] = None
    OutputFormat: Optional[str] = None
    PropertyFilters: Optional[str] = None
    TimeRangeFilter: Optional[str] = None

class GetVectorEnrichmentJobInputRequestTypeDef(BaseModel):
    Arn: str

class VectorEnrichmentJobErrorDetailsTypeDef(BaseModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[VectorEnrichmentJobErrorTypeType] = None

class VectorEnrichmentJobExportErrorDetailsTypeDef(BaseModel):
    Message: Optional[str] = None
    Type: Optional[VectorEnrichmentJobExportErrorTypeType] = None

class PropertiesTypeDef(BaseModel):
    EoCloudCover: Optional[float] = None
    LandsatCloudCoverLand: Optional[float] = None
    Platform: Optional[str] = None
    ViewOffNadir: Optional[float] = None
    ViewSunAzimuth: Optional[float] = None
    ViewSunElevation: Optional[float] = None

class TemporalStatisticsConfigInputTypeDef(BaseModel):
    Statistics: List[TemporalStatisticsType]
    GroupBy: Optional[GroupByType] = None
    TargetBands: Optional[List[str]] = None

class ZonalStatisticsConfigInputTypeDef(BaseModel):
    Statistics: List[ZonalStatisticsType]
    ZoneS3Path: str
    TargetBands: Optional[List[str]] = None
    ZoneS3PathKmsKeyId: Optional[str] = None

class LandsatCloudCoverLandInputTypeDef(BaseModel):
    LowerBound: float
    UpperBound: float

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEarthObservationJobInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[EarthObservationJobStatusType] = None

class ListEarthObservationJobOutputConfigTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    Name: str
    OperationType: str
    Status: EarthObservationJobStatusType
    Tags: Optional[Dict[str, str]] = None

class ListRasterDataCollectionsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListVectorEnrichmentJobInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[str] = None

class ListVectorEnrichmentJobOutputConfigTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    Name: str
    Status: VectorEnrichmentJobStatusType
    Type: VectorEnrichmentJobTypeType
    Tags: Optional[Dict[str, str]] = None

class MapMatchingConfigTypeDef(BaseModel):
    IdAttributeName: str
    TimestampAttributeName: str
    XAttributeName: str
    YAttributeName: str

class UserDefinedTypeDef(BaseModel):
    Unit: Literal["METERS"]
    Value: float

class PlatformInputTypeDef(BaseModel):
    Value: str
    ComparisonOperator: Optional[ComparisonOperatorType] = None

class ViewOffNadirInputTypeDef(BaseModel):
    LowerBound: float
    UpperBound: float

class ViewSunAzimuthInputTypeDef(BaseModel):
    LowerBound: float
    UpperBound: float

class ViewSunElevationInputTypeDef(BaseModel):
    LowerBound: float
    UpperBound: float

class TimeRangeFilterOutputTypeDef(BaseModel):
    EndTime: datetime
    StartTime: datetime

class ReverseGeocodingConfigTypeDef(BaseModel):
    XAttributeName: str
    YAttributeName: str

class StopEarthObservationJobInputRequestTypeDef(BaseModel):
    Arn: str

class StopVectorEnrichmentJobInputRequestTypeDef(BaseModel):
    Arn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AreaOfInterestGeometryTypeDef(BaseModel):
    MultiPolygonGeometry: Optional[MultiPolygonGeometryInputTypeDef] = None
    PolygonGeometry: Optional[PolygonGeometryInputTypeDef] = None

class CustomIndicesInputTypeDef(BaseModel):
    Operations: Optional[List[OperationTypeDef]] = None

class GetTileOutputTypeDef(BaseModel):
    BinaryFile: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportErrorDetailsTypeDef(BaseModel):
    ExportResults: Optional[ExportErrorDetailsOutputTypeDef] = None
    ExportSourceImages: Optional[ExportErrorDetailsOutputTypeDef] = None

class OutputConfigInputTypeDef(BaseModel):
    S3Data: ExportS3DataInputTypeDef

class ExportVectorEnrichmentJobOutputConfigTypeDef(BaseModel):
    S3Data: VectorEnrichmentJobS3DataTypeDef

class VectorEnrichmentJobDataSourceConfigInputTypeDef(BaseModel):
    S3Data: Optional[VectorEnrichmentJobS3DataTypeDef] = None

class GetRasterDataCollectionOutputTypeDef(BaseModel):
    Arn: str
    Description: str
    DescriptionPageUrl: str
    ImageSourceBands: List[str]
    Name: str
    SupportedFilters: List[FilterTypeDef]
    Tags: Dict[str, str]
    Type: DataCollectionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class RasterDataCollectionMetadataTypeDef(BaseModel):
    Arn: str
    Description: str
    Name: str
    SupportedFilters: List[FilterTypeDef]
    Type: DataCollectionTypeType
    DescriptionPageUrl: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ItemSourceTypeDef(BaseModel):
    DateTime: datetime
    Geometry: GeometryTypeDef
    Id: str
    Assets: Optional[Dict[str, AssetValueTypeDef]] = None
    Properties: Optional[PropertiesTypeDef] = None

class ListEarthObservationJobInputListEarthObservationJobsPaginateTypeDef(BaseModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[EarthObservationJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRasterDataCollectionsInputListRasterDataCollectionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVectorEnrichmentJobInputListVectorEnrichmentJobsPaginateTypeDef(BaseModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEarthObservationJobOutputTypeDef(BaseModel):
    EarthObservationJobSummaries: List[ListEarthObservationJobOutputConfigTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVectorEnrichmentJobOutputTypeDef(BaseModel):
    NextToken: str
    VectorEnrichmentJobSummaries: List[ListVectorEnrichmentJobOutputConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OutputResolutionResamplingInputTypeDef(BaseModel):
    UserDefined: UserDefinedTypeDef

class OutputResolutionStackInputTypeDef(BaseModel):
    Predefined: Optional[PredefinedResolutionType] = None
    UserDefined: Optional[UserDefinedTypeDef] = None

class PropertyTypeDef(BaseModel):
    EoCloudCover: Optional[EoCloudCoverInputTypeDef] = None
    LandsatCloudCoverLand: Optional[LandsatCloudCoverLandInputTypeDef] = None
    Platform: Optional[PlatformInputTypeDef] = None
    ViewOffNadir: Optional[ViewOffNadirInputTypeDef] = None
    ViewSunAzimuth: Optional[ViewSunAzimuthInputTypeDef] = None
    ViewSunElevation: Optional[ViewSunElevationInputTypeDef] = None

class VectorEnrichmentJobConfigTypeDef(BaseModel):
    MapMatchingConfig: Optional[MapMatchingConfigTypeDef] = None
    ReverseGeocodingConfig: Optional[ReverseGeocodingConfigTypeDef] = None

class TimeRangeFilterInputTypeDef(BaseModel):
    EndTime: TimestampTypeDef
    StartTime: TimestampTypeDef

class AreaOfInterestTypeDef(BaseModel):
    AreaOfInterestGeometry: Optional[AreaOfInterestGeometryTypeDef] = None

class BandMathConfigInputTypeDef(BaseModel):
    CustomIndices: Optional[CustomIndicesInputTypeDef] = None
    PredefinedIndices: Optional[List[str]] = None

class ExportEarthObservationJobInputRequestTypeDef(BaseModel):
    Arn: str
    ExecutionRoleArn: str
    OutputConfig: OutputConfigInputTypeDef
    ClientToken: Optional[str] = None
    ExportSourceImages: Optional[bool] = None

class ExportEarthObservationJobOutputTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    ExecutionRoleArn: str
    ExportSourceImages: bool
    ExportStatus: EarthObservationJobExportStatusType
    OutputConfig: OutputConfigInputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportVectorEnrichmentJobInputRequestTypeDef(BaseModel):
    Arn: str
    ExecutionRoleArn: str
    OutputConfig: ExportVectorEnrichmentJobOutputConfigTypeDef
    ClientToken: Optional[str] = None

class ExportVectorEnrichmentJobOutputTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    ExecutionRoleArn: str
    ExportStatus: VectorEnrichmentJobExportStatusType
    OutputConfig: ExportVectorEnrichmentJobOutputConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VectorEnrichmentJobInputConfigTypeDef(BaseModel):
    DataSourceConfig: VectorEnrichmentJobDataSourceConfigInputTypeDef
    DocumentType: Literal["CSV"]

class ListRasterDataCollectionsOutputTypeDef(BaseModel):
    NextToken: str
    RasterDataCollectionSummaries: List[RasterDataCollectionMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchRasterDataCollectionOutputTypeDef(BaseModel):
    ApproximateResultCount: int
    Items: List[ItemSourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResamplingConfigInputTypeDef(BaseModel):
    OutputResolution: OutputResolutionResamplingInputTypeDef
    AlgorithmName: Optional[AlgorithmNameResamplingType] = None
    TargetBands: Optional[List[str]] = None

class StackConfigInputTypeDef(BaseModel):
    OutputResolution: Optional[OutputResolutionStackInputTypeDef] = None
    TargetBands: Optional[List[str]] = None

class PropertyFilterTypeDef(BaseModel):
    Property: PropertyTypeDef

class GetVectorEnrichmentJobOutputTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ErrorDetails: VectorEnrichmentJobErrorDetailsTypeDef
    ExecutionRoleArn: str
    ExportErrorDetails: VectorEnrichmentJobExportErrorDetailsTypeDef
    ExportStatus: VectorEnrichmentJobExportStatusType
    InputConfig: VectorEnrichmentJobInputConfigTypeDef
    JobConfig: VectorEnrichmentJobConfigTypeDef
    KmsKeyId: str
    Name: str
    Status: VectorEnrichmentJobStatusType
    Tags: Dict[str, str]
    Type: VectorEnrichmentJobTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class StartVectorEnrichmentJobInputRequestTypeDef(BaseModel):
    ExecutionRoleArn: str
    InputConfig: VectorEnrichmentJobInputConfigTypeDef
    JobConfig: VectorEnrichmentJobConfigTypeDef
    Name: str
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class StartVectorEnrichmentJobOutputTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ExecutionRoleArn: str
    InputConfig: VectorEnrichmentJobInputConfigTypeDef
    JobConfig: VectorEnrichmentJobConfigTypeDef
    KmsKeyId: str
    Name: str
    Status: VectorEnrichmentJobStatusType
    Tags: Dict[str, str]
    Type: VectorEnrichmentJobTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class JobConfigInputTypeDef(BaseModel):
    BandMathConfig: Optional[BandMathConfigInputTypeDef] = None
    CloudMaskingConfig: Optional[Dict[str, Any]] = None
    CloudRemovalConfig: Optional[CloudRemovalConfigInputTypeDef] = None
    GeoMosaicConfig: Optional[GeoMosaicConfigInputTypeDef] = None
    LandCoverSegmentationConfig: Optional[Dict[str, Any]] = None
    ResamplingConfig: Optional[ResamplingConfigInputTypeDef] = None
    StackConfig: Optional[StackConfigInputTypeDef] = None
    TemporalStatisticsConfig: Optional[TemporalStatisticsConfigInputTypeDef] = None
    ZonalStatisticsConfig: Optional[ZonalStatisticsConfigInputTypeDef] = None

class PropertyFiltersTypeDef(BaseModel):
    LogicalOperator: Optional[Literal["AND"]] = None
    Properties: Optional[List[PropertyFilterTypeDef]] = None

class RasterDataCollectionQueryInputTypeDef(BaseModel):
    RasterDataCollectionArn: str
    TimeRangeFilter: TimeRangeFilterInputTypeDef
    AreaOfInterest: Optional[AreaOfInterestTypeDef] = None
    PropertyFilters: Optional[PropertyFiltersTypeDef] = None

class RasterDataCollectionQueryOutputTypeDef(BaseModel):
    RasterDataCollectionArn: str
    RasterDataCollectionName: str
    TimeRangeFilter: TimeRangeFilterOutputTypeDef
    AreaOfInterest: Optional[AreaOfInterestTypeDef] = None
    PropertyFilters: Optional[PropertyFiltersTypeDef] = None

class RasterDataCollectionQueryWithBandFilterInputTypeDef(BaseModel):
    TimeRangeFilter: TimeRangeFilterInputTypeDef
    AreaOfInterest: Optional[AreaOfInterestTypeDef] = None
    BandFilter: Optional[Sequence[str]] = None
    PropertyFilters: Optional[PropertyFiltersTypeDef] = None

class InputConfigInputTypeDef(BaseModel):
    PreviousEarthObservationJobArn: Optional[str] = None
    RasterDataCollectionQuery: Optional[RasterDataCollectionQueryInputTypeDef] = None

class InputConfigOutputTypeDef(BaseModel):
    PreviousEarthObservationJobArn: Optional[str] = None
    RasterDataCollectionQuery: Optional[RasterDataCollectionQueryOutputTypeDef] = None

class SearchRasterDataCollectionInputRequestTypeDef(BaseModel):
    Arn: str
    RasterDataCollectionQuery: RasterDataCollectionQueryWithBandFilterInputTypeDef
    NextToken: Optional[str] = None

class StartEarthObservationJobInputRequestTypeDef(BaseModel):
    ExecutionRoleArn: str
    InputConfig: InputConfigInputTypeDef
    JobConfig: JobConfigInputTypeDef
    Name: str
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class GetEarthObservationJobOutputTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ErrorDetails: EarthObservationJobErrorDetailsTypeDef
    ExecutionRoleArn: str
    ExportErrorDetails: ExportErrorDetailsTypeDef
    ExportStatus: EarthObservationJobExportStatusType
    InputConfig: InputConfigOutputTypeDef
    JobConfig: JobConfigInputTypeDef
    KmsKeyId: str
    Name: str
    OutputBands: List[OutputBandTypeDef]
    Status: EarthObservationJobStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartEarthObservationJobOutputTypeDef(BaseModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ExecutionRoleArn: str
    InputConfig: InputConfigOutputTypeDef
    JobConfig: JobConfigInputTypeDef
    KmsKeyId: str
    Name: str
    Status: EarthObservationJobStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

