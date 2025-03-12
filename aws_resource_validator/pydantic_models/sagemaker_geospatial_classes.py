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
from aws_resource_validator.pydantic_models.sagemaker_geospatial_constants import *

class MultiPolygonGeometryInputOutputTypeDef(BaseValidatorModel):
    Coordinates: List[List[List[List[float]]]]


class PolygonGeometryInputOutputTypeDef(BaseValidatorModel):
    Coordinates: List[List[List[float]]]


class AssetValueTypeDef(BaseValidatorModel):
    Href: Optional[str] = None


class CloudRemovalConfigInputOutputTypeDef(BaseValidatorModel):
    AlgorithmName: Optional[Literal["INTERPOLATION"]] = None
    InterpolationValue: Optional[str] = None
    TargetBands: Optional[List[str]] = None


class CloudRemovalConfigInputTypeDef(BaseValidatorModel):
    AlgorithmName: Optional[Literal["INTERPOLATION"]] = None
    InterpolationValue: Optional[str] = None
    TargetBands: Optional[Sequence[str]] = None


class OperationTypeDef(BaseValidatorModel):
    Equation: str
    Name: str
    OutputType: Optional[OutputTypeType] = None


class DeleteEarthObservationJobInputTypeDef(BaseValidatorModel):
    Arn: str


class DeleteVectorEnrichmentJobInputTypeDef(BaseValidatorModel):
    Arn: str


class EoCloudCoverInputTypeDef(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ExportS3DataInputTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class VectorEnrichmentJobS3DataTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class GeoMosaicConfigInputOutputTypeDef(BaseValidatorModel):
    AlgorithmName: Optional[AlgorithmNameGeoMosaicType] = None
    TargetBands: Optional[List[str]] = None


class GeoMosaicConfigInputTypeDef(BaseValidatorModel):
    AlgorithmName: Optional[AlgorithmNameGeoMosaicType] = None
    TargetBands: Optional[Sequence[str]] = None


class GetEarthObservationJobInputTypeDef(BaseValidatorModel):
    Arn: str


class OutputBandTypeDef(BaseValidatorModel):
    BandName: str
    OutputDataType: OutputTypeType


class GetRasterDataCollectionInputTypeDef(BaseValidatorModel):
    Arn: str


class GetTileInputTypeDef(BaseValidatorModel):
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


class GetVectorEnrichmentJobInputTypeDef(BaseValidatorModel):
    Arn: str


class VectorEnrichmentJobErrorDetailsTypeDef(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[VectorEnrichmentJobErrorTypeType] = None


class PropertiesTypeDef(BaseValidatorModel):
    EoCloudCover: Optional[float] = None
    LandsatCloudCoverLand: Optional[float] = None
    Platform: Optional[str] = None
    ViewOffNadir: Optional[float] = None
    ViewSunAzimuth: Optional[float] = None
    ViewSunElevation: Optional[float] = None


class TemporalStatisticsConfigInputOutputTypeDef(BaseValidatorModel):
    Statistics: List[TemporalStatisticsType]
    GroupBy: Optional[GroupByType] = None
    TargetBands: Optional[List[str]] = None


class ZonalStatisticsConfigInputOutputTypeDef(BaseValidatorModel):
    Statistics: List[ZonalStatisticsType]
    ZoneS3Path: str
    TargetBands: Optional[List[str]] = None
    ZoneS3PathKmsKeyId: Optional[str] = None


class TemporalStatisticsConfigInputTypeDef(BaseValidatorModel):
    Statistics: Sequence[TemporalStatisticsType]
    GroupBy: Optional[GroupByType] = None
    TargetBands: Optional[Sequence[str]] = None


class ZonalStatisticsConfigInputTypeDef(BaseValidatorModel):
    Statistics: Sequence[ZonalStatisticsType]
    ZoneS3Path: str
    TargetBands: Optional[Sequence[str]] = None
    ZoneS3PathKmsKeyId: Optional[str] = None


class LandsatCloudCoverLandInputTypeDef(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEarthObservationJobInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[EarthObservationJobStatusType] = None


class ListEarthObservationJobOutputConfigTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    Name: str
    OperationType: str
    Status: EarthObservationJobStatusType
    Tags: Optional[Dict[str, str]] = None


class ListRasterDataCollectionsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListVectorEnrichmentJobInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[str] = None


class MapMatchingConfigTypeDef(BaseValidatorModel):
    IdAttributeName: str
    TimestampAttributeName: str
    XAttributeName: str
    YAttributeName: str


class MultiPolygonGeometryInputTypeDef(BaseValidatorModel):
    Coordinates: Sequence[Sequence[Sequence[Sequence[float]]]]


class UserDefinedTypeDef(BaseValidatorModel):
    Unit: Literal["METERS"]
    Value: float


class PlatformInputTypeDef(BaseValidatorModel):
    Value: str
    ComparisonOperator: Optional[ComparisonOperatorType] = None


class PolygonGeometryInputTypeDef(BaseValidatorModel):
    Coordinates: Sequence[Sequence[Sequence[float]]]


class ViewOffNadirInputTypeDef(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class ViewSunAzimuthInputTypeDef(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class ViewSunElevationInputTypeDef(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class TimeRangeFilterOutputTypeDef(BaseValidatorModel):
    EndTime: datetime
    StartTime: datetime


class ReverseGeocodingConfigTypeDef(BaseValidatorModel):
    XAttributeName: str
    YAttributeName: str


class StopEarthObservationJobInputTypeDef(BaseValidatorModel):
    Arn: str


class StopVectorEnrichmentJobInputTypeDef(BaseValidatorModel):
    Arn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class AreaOfInterestGeometryOutputTypeDef(BaseValidatorModel):
    MultiPolygonGeometry: Optional[MultiPolygonGeometryInputOutputTypeDef] = None
    PolygonGeometry: Optional[PolygonGeometryInputOutputTypeDef] = None


class CustomIndicesInputOutputTypeDef(BaseValidatorModel):
    Operations: Optional[List[OperationTypeDef]] = None


class CustomIndicesInputTypeDef(BaseValidatorModel):
    Operations: Optional[Sequence[OperationTypeDef]] = None


class GetTileOutputTypeDef(BaseValidatorModel):
    BinaryFile: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ExportErrorDetailsOutputTypeDef(BaseValidatorModel):
    pass


class ExportErrorDetailsTypeDef(BaseValidatorModel):
    ExportResults: Optional[ExportErrorDetailsOutputTypeDef] = None
    ExportSourceImages: Optional[ExportErrorDetailsOutputTypeDef] = None


class OutputConfigInputTypeDef(BaseValidatorModel):
    S3Data: ExportS3DataInputTypeDef


class ExportVectorEnrichmentJobOutputConfigTypeDef(BaseValidatorModel):
    S3Data: VectorEnrichmentJobS3DataTypeDef


class VectorEnrichmentJobDataSourceConfigInputTypeDef(BaseValidatorModel):
    S3Data: Optional[VectorEnrichmentJobS3DataTypeDef] = None


class GeometryTypeDef(BaseValidatorModel):
    pass


class ItemSourceTypeDef(BaseValidatorModel):
    DateTime: datetime
    Geometry: GeometryTypeDef
    Id: str
    Assets: Optional[Dict[str, AssetValueTypeDef]] = None
    Properties: Optional[PropertiesTypeDef] = None


class ListEarthObservationJobInputPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[EarthObservationJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRasterDataCollectionsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVectorEnrichmentJobInputPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEarthObservationJobOutputTypeDef(BaseValidatorModel):
    EarthObservationJobSummaries: List[ListEarthObservationJobOutputConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListVectorEnrichmentJobOutputConfigTypeDef(BaseValidatorModel):
    pass


class ListVectorEnrichmentJobOutputTypeDef(BaseValidatorModel):
    VectorEnrichmentJobSummaries: List[ListVectorEnrichmentJobOutputConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class OutputResolutionResamplingInputTypeDef(BaseValidatorModel):
    UserDefined: UserDefinedTypeDef


class OutputResolutionStackInputTypeDef(BaseValidatorModel):
    Predefined: Optional[PredefinedResolutionType] = None
    UserDefined: Optional[UserDefinedTypeDef] = None


class PropertyTypeDef(BaseValidatorModel):
    EoCloudCover: Optional[EoCloudCoverInputTypeDef] = None
    LandsatCloudCoverLand: Optional[LandsatCloudCoverLandInputTypeDef] = None
    Platform: Optional[PlatformInputTypeDef] = None
    ViewOffNadir: Optional[ViewOffNadirInputTypeDef] = None
    ViewSunAzimuth: Optional[ViewSunAzimuthInputTypeDef] = None
    ViewSunElevation: Optional[ViewSunElevationInputTypeDef] = None


class VectorEnrichmentJobConfigTypeDef(BaseValidatorModel):
    MapMatchingConfig: Optional[MapMatchingConfigTypeDef] = None
    ReverseGeocodingConfig: Optional[ReverseGeocodingConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class TimeRangeFilterInputTypeDef(BaseValidatorModel):
    EndTime: TimestampTypeDef
    StartTime: TimestampTypeDef


class AreaOfInterestOutputTypeDef(BaseValidatorModel):
    AreaOfInterestGeometry: Optional[AreaOfInterestGeometryOutputTypeDef] = None


class BandMathConfigInputOutputTypeDef(BaseValidatorModel):
    CustomIndices: Optional[CustomIndicesInputOutputTypeDef] = None
    PredefinedIndices: Optional[List[str]] = None


class BandMathConfigInputTypeDef(BaseValidatorModel):
    CustomIndices: Optional[CustomIndicesInputTypeDef] = None
    PredefinedIndices: Optional[Sequence[str]] = None


class ExportEarthObservationJobInputTypeDef(BaseValidatorModel):
    Arn: str
    ExecutionRoleArn: str
    OutputConfig: OutputConfigInputTypeDef
    ClientToken: Optional[str] = None
    ExportSourceImages: Optional[bool] = None


class ExportEarthObservationJobOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    ExecutionRoleArn: str
    ExportSourceImages: bool
    ExportStatus: EarthObservationJobExportStatusType
    OutputConfig: OutputConfigInputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportVectorEnrichmentJobInputTypeDef(BaseValidatorModel):
    Arn: str
    ExecutionRoleArn: str
    OutputConfig: ExportVectorEnrichmentJobOutputConfigTypeDef
    ClientToken: Optional[str] = None


class ExportVectorEnrichmentJobOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    ExecutionRoleArn: str
    ExportStatus: VectorEnrichmentJobExportStatusType
    OutputConfig: ExportVectorEnrichmentJobOutputConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class VectorEnrichmentJobInputConfigTypeDef(BaseValidatorModel):
    DataSourceConfig: VectorEnrichmentJobDataSourceConfigInputTypeDef
    DocumentType: Literal["CSV"]


class RasterDataCollectionMetadataTypeDef(BaseValidatorModel):
    pass


class ListRasterDataCollectionsOutputTypeDef(BaseValidatorModel):
    RasterDataCollectionSummaries: List[RasterDataCollectionMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchRasterDataCollectionOutputTypeDef(BaseValidatorModel):
    ApproximateResultCount: int
    Items: List[ItemSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResamplingConfigInputOutputTypeDef(BaseValidatorModel):
    OutputResolution: OutputResolutionResamplingInputTypeDef
    AlgorithmName: Optional[AlgorithmNameResamplingType] = None
    TargetBands: Optional[List[str]] = None


class ResamplingConfigInputTypeDef(BaseValidatorModel):
    OutputResolution: OutputResolutionResamplingInputTypeDef
    AlgorithmName: Optional[AlgorithmNameResamplingType] = None
    TargetBands: Optional[Sequence[str]] = None


class StackConfigInputOutputTypeDef(BaseValidatorModel):
    OutputResolution: Optional[OutputResolutionStackInputTypeDef] = None
    TargetBands: Optional[List[str]] = None


class StackConfigInputTypeDef(BaseValidatorModel):
    OutputResolution: Optional[OutputResolutionStackInputTypeDef] = None
    TargetBands: Optional[Sequence[str]] = None


class MultiPolygonGeometryInputUnionTypeDef(BaseValidatorModel):
    pass


class PolygonGeometryInputUnionTypeDef(BaseValidatorModel):
    pass


class AreaOfInterestGeometryTypeDef(BaseValidatorModel):
    MultiPolygonGeometry: Optional[MultiPolygonGeometryInputUnionTypeDef] = None
    PolygonGeometry: Optional[PolygonGeometryInputUnionTypeDef] = None


class PropertyFilterTypeDef(BaseValidatorModel):
    Property: PropertyTypeDef


class StartVectorEnrichmentJobInputTypeDef(BaseValidatorModel):
    ExecutionRoleArn: str
    InputConfig: VectorEnrichmentJobInputConfigTypeDef
    JobConfig: VectorEnrichmentJobConfigTypeDef
    Name: str
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class JobConfigInputOutputTypeDef(BaseValidatorModel):
    BandMathConfig: Optional[BandMathConfigInputOutputTypeDef] = None
    CloudMaskingConfig: Optional[Dict[str, Any]] = None
    CloudRemovalConfig: Optional[CloudRemovalConfigInputOutputTypeDef] = None
    GeoMosaicConfig: Optional[GeoMosaicConfigInputOutputTypeDef] = None
    LandCoverSegmentationConfig: Optional[Dict[str, Any]] = None
    ResamplingConfig: Optional[ResamplingConfigInputOutputTypeDef] = None
    StackConfig: Optional[StackConfigInputOutputTypeDef] = None
    TemporalStatisticsConfig: Optional[TemporalStatisticsConfigInputOutputTypeDef] = None
    ZonalStatisticsConfig: Optional[ZonalStatisticsConfigInputOutputTypeDef] = None


class JobConfigInputTypeDef(BaseValidatorModel):
    BandMathConfig: Optional[BandMathConfigInputTypeDef] = None
    CloudMaskingConfig: Optional[Mapping[str, Any]] = None
    CloudRemovalConfig: Optional[CloudRemovalConfigInputTypeDef] = None
    GeoMosaicConfig: Optional[GeoMosaicConfigInputTypeDef] = None
    LandCoverSegmentationConfig: Optional[Mapping[str, Any]] = None
    ResamplingConfig: Optional[ResamplingConfigInputTypeDef] = None
    StackConfig: Optional[StackConfigInputTypeDef] = None
    TemporalStatisticsConfig: Optional[TemporalStatisticsConfigInputTypeDef] = None
    ZonalStatisticsConfig: Optional[ZonalStatisticsConfigInputTypeDef] = None


class PropertyFiltersOutputTypeDef(BaseValidatorModel):
    LogicalOperator: Optional[Literal["AND"]] = None
    Properties: Optional[List[PropertyFilterTypeDef]] = None


class PropertyFiltersTypeDef(BaseValidatorModel):
    LogicalOperator: Optional[Literal["AND"]] = None
    Properties: Optional[Sequence[PropertyFilterTypeDef]] = None


class AreaOfInterestGeometryUnionTypeDef(BaseValidatorModel):
    pass


class AreaOfInterestTypeDef(BaseValidatorModel):
    AreaOfInterestGeometry: Optional[AreaOfInterestGeometryUnionTypeDef] = None


class RasterDataCollectionQueryOutputTypeDef(BaseValidatorModel):
    RasterDataCollectionArn: str
    RasterDataCollectionName: str
    TimeRangeFilter: TimeRangeFilterOutputTypeDef
    AreaOfInterest: Optional[AreaOfInterestOutputTypeDef] = None
    PropertyFilters: Optional[PropertyFiltersOutputTypeDef] = None


class InputConfigOutputTypeDef(BaseValidatorModel):
    PreviousEarthObservationJobArn: Optional[str] = None
    RasterDataCollectionQuery: Optional[RasterDataCollectionQueryOutputTypeDef] = None


class PropertyFiltersUnionTypeDef(BaseValidatorModel):
    pass


class AreaOfInterestUnionTypeDef(BaseValidatorModel):
    pass


class RasterDataCollectionQueryInputTypeDef(BaseValidatorModel):
    RasterDataCollectionArn: str
    TimeRangeFilter: TimeRangeFilterInputTypeDef
    AreaOfInterest: Optional[AreaOfInterestUnionTypeDef] = None
    PropertyFilters: Optional[PropertyFiltersUnionTypeDef] = None


class RasterDataCollectionQueryWithBandFilterInputTypeDef(BaseValidatorModel):
    TimeRangeFilter: TimeRangeFilterInputTypeDef
    AreaOfInterest: Optional[AreaOfInterestUnionTypeDef] = None
    BandFilter: Optional[Sequence[str]] = None
    PropertyFilters: Optional[PropertyFiltersUnionTypeDef] = None


class EarthObservationJobErrorDetailsTypeDef(BaseValidatorModel):
    pass


class GetEarthObservationJobOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ErrorDetails: EarthObservationJobErrorDetailsTypeDef
    ExecutionRoleArn: str
    ExportErrorDetails: ExportErrorDetailsTypeDef
    ExportStatus: EarthObservationJobExportStatusType
    InputConfig: InputConfigOutputTypeDef
    JobConfig: JobConfigInputOutputTypeDef
    KmsKeyId: str
    Name: str
    OutputBands: List[OutputBandTypeDef]
    Status: EarthObservationJobStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartEarthObservationJobOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ExecutionRoleArn: str
    InputConfig: InputConfigOutputTypeDef
    JobConfig: JobConfigInputOutputTypeDef
    KmsKeyId: str
    Name: str
    Status: EarthObservationJobStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class InputConfigInputTypeDef(BaseValidatorModel):
    PreviousEarthObservationJobArn: Optional[str] = None
    RasterDataCollectionQuery: Optional[RasterDataCollectionQueryInputTypeDef] = None


class SearchRasterDataCollectionInputTypeDef(BaseValidatorModel):
    Arn: str
    RasterDataCollectionQuery: RasterDataCollectionQueryWithBandFilterInputTypeDef
    NextToken: Optional[str] = None


class JobConfigInputUnionTypeDef(BaseValidatorModel):
    pass


class StartEarthObservationJobInputTypeDef(BaseValidatorModel):
    ExecutionRoleArn: str
    InputConfig: InputConfigInputTypeDef
    JobConfig: JobConfigInputUnionTypeDef
    Name: str
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


