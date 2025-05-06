from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sagemaker_geospatial.sagemaker_geospatial_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class MultiPolygonGeometryInputOutput(BaseValidatorModel):
    Coordinates: List[List[List[List[float]]]]


class PolygonGeometryInputOutput(BaseValidatorModel):
    Coordinates: List[List[List[float]]]


class AssetValue(BaseValidatorModel):
    Href: Optional[str] = None


class CloudRemovalConfigInputOutput(BaseValidatorModel):
    AlgorithmName: Optional[Literal['INTERPOLATION']] = None
    InterpolationValue: Optional[str] = None
    TargetBands: Optional[List[str]] = None


class CloudRemovalConfigInput(BaseValidatorModel):
    AlgorithmName: Optional[Literal['INTERPOLATION']] = None
    InterpolationValue: Optional[str] = None
    TargetBands: Optional[List[str]] = None


class Operation(BaseValidatorModel):
    Equation: str
    Name: str
    OutputType: Optional[OutputTypeType] = None


class DeleteEarthObservationJobInput(BaseValidatorModel):
    Arn: str


class DeleteVectorEnrichmentJobInput(BaseValidatorModel):
    Arn: str


class EarthObservationJobErrorDetails(BaseValidatorModel):
    Message: Optional[str] = None
    Type: Optional[EarthObservationJobErrorTypeType] = None


class EoCloudCoverInput(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ExportErrorDetailsOutput(BaseValidatorModel):
    Message: Optional[str] = None
    Type: Optional[ExportErrorTypeType] = None


class ExportS3DataInput(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class VectorEnrichmentJobS3Data(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: str
    Type: str
    Maximum: Optional[float] = None
    Minimum: Optional[float] = None


class GeoMosaicConfigInputOutput(BaseValidatorModel):
    AlgorithmName: Optional[AlgorithmNameGeoMosaicType] = None
    TargetBands: Optional[List[str]] = None


class GeoMosaicConfigInput(BaseValidatorModel):
    AlgorithmName: Optional[AlgorithmNameGeoMosaicType] = None
    TargetBands: Optional[List[str]] = None


class Geometry(BaseValidatorModel):
    Coordinates: List[List[List[float]]]
    Type: str


class GetEarthObservationJobInput(BaseValidatorModel):
    Arn: str


class OutputBand(BaseValidatorModel):
    BandName: str
    OutputDataType: OutputTypeType


class GetRasterDataCollectionInput(BaseValidatorModel):
    Arn: str


class GetTileInput(BaseValidatorModel):
    Arn: str
    ImageAssets: List[str]
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


class GetVectorEnrichmentJobInput(BaseValidatorModel):
    Arn: str


class VectorEnrichmentJobErrorDetails(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[VectorEnrichmentJobErrorTypeType] = None


class VectorEnrichmentJobExportErrorDetails(BaseValidatorModel):
    Message: Optional[str] = None
    Type: Optional[VectorEnrichmentJobExportErrorTypeType] = None


class Properties(BaseValidatorModel):
    EoCloudCover: Optional[float] = None
    LandsatCloudCoverLand: Optional[float] = None
    Platform: Optional[str] = None
    ViewOffNadir: Optional[float] = None
    ViewSunAzimuth: Optional[float] = None
    ViewSunElevation: Optional[float] = None


class TemporalStatisticsConfigInputOutput(BaseValidatorModel):
    Statistics: List[TemporalStatisticsType]
    GroupBy: Optional[GroupByType] = None
    TargetBands: Optional[List[str]] = None


class ZonalStatisticsConfigInputOutput(BaseValidatorModel):
    Statistics: List[ZonalStatisticsType]
    ZoneS3Path: str
    TargetBands: Optional[List[str]] = None
    ZoneS3PathKmsKeyId: Optional[str] = None


class TemporalStatisticsConfigInput(BaseValidatorModel):
    Statistics: List[TemporalStatisticsType]
    GroupBy: Optional[GroupByType] = None
    TargetBands: Optional[List[str]] = None


class ZonalStatisticsConfigInput(BaseValidatorModel):
    Statistics: List[ZonalStatisticsType]
    ZoneS3Path: str
    TargetBands: Optional[List[str]] = None
    ZoneS3PathKmsKeyId: Optional[str] = None


class LandsatCloudCoverLandInput(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEarthObservationJobInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[EarthObservationJobStatusType] = None


class ListEarthObservationJobOutputConfig(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    Name: str
    OperationType: str
    Status: EarthObservationJobStatusType
    Tags: Optional[Dict[str, str]] = None


class ListRasterDataCollectionsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListVectorEnrichmentJobInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[str] = None


class ListVectorEnrichmentJobOutputConfig(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    Name: str
    Status: VectorEnrichmentJobStatusType
    Type: VectorEnrichmentJobTypeType
    Tags: Optional[Dict[str, str]] = None


class MapMatchingConfig(BaseValidatorModel):
    IdAttributeName: str
    TimestampAttributeName: str
    XAttributeName: str
    YAttributeName: str


class MultiPolygonGeometryInput(BaseValidatorModel):
    Coordinates: List[List[List[List[float]]]]


class UserDefined(BaseValidatorModel):
    Unit: Literal['METERS']
    Value: float


class PlatformInput(BaseValidatorModel):
    Value: str
    ComparisonOperator: Optional[ComparisonOperatorType] = None


class PolygonGeometryInput(BaseValidatorModel):
    Coordinates: List[List[List[float]]]


class ViewOffNadirInput(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class ViewSunAzimuthInput(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class ViewSunElevationInput(BaseValidatorModel):
    LowerBound: float
    UpperBound: float


class TimeRangeFilterOutput(BaseValidatorModel):
    EndTime: datetime
    StartTime: datetime


class ReverseGeocodingConfig(BaseValidatorModel):
    XAttributeName: str
    YAttributeName: str


class StopEarthObservationJobInput(BaseValidatorModel):
    Arn: str


class StopVectorEnrichmentJobInput(BaseValidatorModel):
    Arn: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]

Timestamp = Union[datetime, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class AreaOfInterestGeometryOutput(BaseValidatorModel):
    MultiPolygonGeometry: Optional[MultiPolygonGeometryInputOutput] = None
    PolygonGeometry: Optional[PolygonGeometryInputOutput] = None


class CustomIndicesInputOutput(BaseValidatorModel):
    Operations: Optional[List[Operation]] = None


class CustomIndicesInput(BaseValidatorModel):
    Operations: Optional[List[Operation]] = None


class GetTileOutput(BaseValidatorModel):
    BinaryFile: StreamingBody
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ExportErrorDetails(BaseValidatorModel):
    ExportResults: Optional[ExportErrorDetailsOutput] = None
    ExportSourceImages: Optional[ExportErrorDetailsOutput] = None


class OutputConfigInput(BaseValidatorModel):
    S3Data: ExportS3DataInput


class ExportVectorEnrichmentJobOutputConfig(BaseValidatorModel):
    S3Data: VectorEnrichmentJobS3Data


class VectorEnrichmentJobDataSourceConfigInput(BaseValidatorModel):
    S3Data: Optional[VectorEnrichmentJobS3Data] = None


class GetRasterDataCollectionOutput(BaseValidatorModel):
    Arn: str
    Description: str
    DescriptionPageUrl: str
    ImageSourceBands: List[str]
    Name: str
    SupportedFilters: List[Filter]
    Tags: Dict[str, str]
    Type: DataCollectionTypeType
    ResponseMetadata: ResponseMetadata


class RasterDataCollectionMetadata(BaseValidatorModel):
    Arn: str
    Description: str
    Name: str
    SupportedFilters: List[Filter]
    Type: DataCollectionTypeType
    DescriptionPageUrl: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ItemSource(BaseValidatorModel):
    DateTime: datetime
    Geometry: Geometry
    Id: str
    Assets: Optional[Dict[str, AssetValue]] = None
    Properties: Optional[Properties] = None


class ListEarthObservationJobInputPaginate(BaseValidatorModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[EarthObservationJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRasterDataCollectionsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVectorEnrichmentJobInputPaginate(BaseValidatorModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEarthObservationJobOutput(BaseValidatorModel):
    EarthObservationJobSummaries: List[ListEarthObservationJobOutputConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListVectorEnrichmentJobOutput(BaseValidatorModel):
    VectorEnrichmentJobSummaries: List[ListVectorEnrichmentJobOutputConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

MultiPolygonGeometryInputUnion = Union[MultiPolygonGeometryInput, MultiPolygonGeometryInputOutput]


class OutputResolutionResamplingInput(BaseValidatorModel):
    UserDefined: UserDefined


class OutputResolutionStackInput(BaseValidatorModel):
    Predefined: Optional[PredefinedResolutionType] = None
    UserDefined: Optional[UserDefined] = None

PolygonGeometryInputUnion = Union[PolygonGeometryInput, PolygonGeometryInputOutput]


class Property(BaseValidatorModel):
    EoCloudCover: Optional[EoCloudCoverInput] = None
    LandsatCloudCoverLand: Optional[LandsatCloudCoverLandInput] = None
    Platform: Optional[PlatformInput] = None
    ViewOffNadir: Optional[ViewOffNadirInput] = None
    ViewSunAzimuth: Optional[ViewSunAzimuthInput] = None
    ViewSunElevation: Optional[ViewSunElevationInput] = None


class VectorEnrichmentJobConfig(BaseValidatorModel):
    MapMatchingConfig: Optional[MapMatchingConfig] = None
    ReverseGeocodingConfig: Optional[ReverseGeocodingConfig] = None


class TimeRangeFilterInput(BaseValidatorModel):
    EndTime: Timestamp
    StartTime: Timestamp


class AreaOfInterestOutput(BaseValidatorModel):
    AreaOfInterestGeometry: Optional[AreaOfInterestGeometryOutput] = None


class BandMathConfigInputOutput(BaseValidatorModel):
    CustomIndices: Optional[CustomIndicesInputOutput] = None
    PredefinedIndices: Optional[List[str]] = None


class BandMathConfigInput(BaseValidatorModel):
    CustomIndices: Optional[CustomIndicesInput] = None
    PredefinedIndices: Optional[List[str]] = None


class ExportEarthObservationJobInput(BaseValidatorModel):
    Arn: str
    ExecutionRoleArn: str
    OutputConfig: OutputConfigInput
    ClientToken: Optional[str] = None
    ExportSourceImages: Optional[bool] = None


class ExportEarthObservationJobOutput(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    ExecutionRoleArn: str
    ExportSourceImages: bool
    ExportStatus: EarthObservationJobExportStatusType
    OutputConfig: OutputConfigInput
    ResponseMetadata: ResponseMetadata


class ExportVectorEnrichmentJobInput(BaseValidatorModel):
    Arn: str
    ExecutionRoleArn: str
    OutputConfig: ExportVectorEnrichmentJobOutputConfig
    ClientToken: Optional[str] = None


class ExportVectorEnrichmentJobOutput(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    ExecutionRoleArn: str
    ExportStatus: VectorEnrichmentJobExportStatusType
    OutputConfig: ExportVectorEnrichmentJobOutputConfig
    ResponseMetadata: ResponseMetadata


class VectorEnrichmentJobInputConfig(BaseValidatorModel):
    DataSourceConfig: VectorEnrichmentJobDataSourceConfigInput
    DocumentType: Literal['CSV']


class ListRasterDataCollectionsOutput(BaseValidatorModel):
    RasterDataCollectionSummaries: List[RasterDataCollectionMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchRasterDataCollectionOutput(BaseValidatorModel):
    ApproximateResultCount: int
    Items: List[ItemSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResamplingConfigInputOutput(BaseValidatorModel):
    OutputResolution: OutputResolutionResamplingInput
    AlgorithmName: Optional[AlgorithmNameResamplingType] = None
    TargetBands: Optional[List[str]] = None


class ResamplingConfigInput(BaseValidatorModel):
    OutputResolution: OutputResolutionResamplingInput
    AlgorithmName: Optional[AlgorithmNameResamplingType] = None
    TargetBands: Optional[List[str]] = None


class StackConfigInputOutput(BaseValidatorModel):
    OutputResolution: Optional[OutputResolutionStackInput] = None
    TargetBands: Optional[List[str]] = None


class StackConfigInput(BaseValidatorModel):
    OutputResolution: Optional[OutputResolutionStackInput] = None
    TargetBands: Optional[List[str]] = None


class AreaOfInterestGeometry(BaseValidatorModel):
    MultiPolygonGeometry: Optional[MultiPolygonGeometryInputUnion] = None
    PolygonGeometry: Optional[PolygonGeometryInputUnion] = None


class PropertyFilter(BaseValidatorModel):
    Property: Property


class GetVectorEnrichmentJobOutput(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ErrorDetails: VectorEnrichmentJobErrorDetails
    ExecutionRoleArn: str
    ExportErrorDetails: VectorEnrichmentJobExportErrorDetails
    ExportStatus: VectorEnrichmentJobExportStatusType
    InputConfig: VectorEnrichmentJobInputConfig
    JobConfig: VectorEnrichmentJobConfig
    KmsKeyId: str
    Name: str
    Status: VectorEnrichmentJobStatusType
    Tags: Dict[str, str]
    Type: VectorEnrichmentJobTypeType
    ResponseMetadata: ResponseMetadata


class StartVectorEnrichmentJobInput(BaseValidatorModel):
    ExecutionRoleArn: str
    InputConfig: VectorEnrichmentJobInputConfig
    JobConfig: VectorEnrichmentJobConfig
    Name: str
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class StartVectorEnrichmentJobOutput(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ExecutionRoleArn: str
    InputConfig: VectorEnrichmentJobInputConfig
    JobConfig: VectorEnrichmentJobConfig
    KmsKeyId: str
    Name: str
    Status: VectorEnrichmentJobStatusType
    Tags: Dict[str, str]
    Type: VectorEnrichmentJobTypeType
    ResponseMetadata: ResponseMetadata


class JobConfigInputOutput(BaseValidatorModel):
    BandMathConfig: Optional[BandMathConfigInputOutput] = None
    CloudMaskingConfig: Optional[Dict[str, Any]] = None
    CloudRemovalConfig: Optional[CloudRemovalConfigInputOutput] = None
    GeoMosaicConfig: Optional[GeoMosaicConfigInputOutput] = None
    LandCoverSegmentationConfig: Optional[Dict[str, Any]] = None
    ResamplingConfig: Optional[ResamplingConfigInputOutput] = None
    StackConfig: Optional[StackConfigInputOutput] = None
    TemporalStatisticsConfig: Optional[TemporalStatisticsConfigInputOutput] = None
    ZonalStatisticsConfig: Optional[ZonalStatisticsConfigInputOutput] = None


class JobConfigInput(BaseValidatorModel):
    BandMathConfig: Optional[BandMathConfigInput] = None
    CloudMaskingConfig: Optional[Dict[str, Any]] = None
    CloudRemovalConfig: Optional[CloudRemovalConfigInput] = None
    GeoMosaicConfig: Optional[GeoMosaicConfigInput] = None
    LandCoverSegmentationConfig: Optional[Dict[str, Any]] = None
    ResamplingConfig: Optional[ResamplingConfigInput] = None
    StackConfig: Optional[StackConfigInput] = None
    TemporalStatisticsConfig: Optional[TemporalStatisticsConfigInput] = None
    ZonalStatisticsConfig: Optional[ZonalStatisticsConfigInput] = None

AreaOfInterestGeometryUnion = Union[AreaOfInterestGeometry, AreaOfInterestGeometryOutput]


class PropertyFiltersOutput(BaseValidatorModel):
    LogicalOperator: Optional[Literal['AND']] = None
    Properties: Optional[List[PropertyFilter]] = None


class PropertyFilters(BaseValidatorModel):
    LogicalOperator: Optional[Literal['AND']] = None
    Properties: Optional[List[PropertyFilter]] = None

JobConfigInputUnion = Union[JobConfigInput, JobConfigInputOutput]


class AreaOfInterest(BaseValidatorModel):
    AreaOfInterestGeometry: Optional[AreaOfInterestGeometryUnion] = None


class RasterDataCollectionQueryOutput(BaseValidatorModel):
    RasterDataCollectionArn: str
    RasterDataCollectionName: str
    TimeRangeFilter: TimeRangeFilterOutput
    AreaOfInterest: Optional[AreaOfInterestOutput] = None
    PropertyFilters: Optional[PropertyFiltersOutput] = None

PropertyFiltersUnion = Union[PropertyFilters, PropertyFiltersOutput]

AreaOfInterestUnion = Union[AreaOfInterest, AreaOfInterestOutput]


class InputConfigOutput(BaseValidatorModel):
    PreviousEarthObservationJobArn: Optional[str] = None
    RasterDataCollectionQuery: Optional[RasterDataCollectionQueryOutput] = None


class RasterDataCollectionQueryInput(BaseValidatorModel):
    RasterDataCollectionArn: str
    TimeRangeFilter: TimeRangeFilterInput
    AreaOfInterest: Optional[AreaOfInterestUnion] = None
    PropertyFilters: Optional[PropertyFiltersUnion] = None


class RasterDataCollectionQueryWithBandFilterInput(BaseValidatorModel):
    TimeRangeFilter: TimeRangeFilterInput
    AreaOfInterest: Optional[AreaOfInterestUnion] = None
    BandFilter: Optional[List[str]] = None
    PropertyFilters: Optional[PropertyFiltersUnion] = None


class GetEarthObservationJobOutput(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ErrorDetails: EarthObservationJobErrorDetails
    ExecutionRoleArn: str
    ExportErrorDetails: ExportErrorDetails
    ExportStatus: EarthObservationJobExportStatusType
    InputConfig: InputConfigOutput
    JobConfig: JobConfigInputOutput
    KmsKeyId: str
    Name: str
    OutputBands: List[OutputBand]
    Status: EarthObservationJobStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartEarthObservationJobOutput(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    ExecutionRoleArn: str
    InputConfig: InputConfigOutput
    JobConfig: JobConfigInputOutput
    KmsKeyId: str
    Name: str
    Status: EarthObservationJobStatusType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class InputConfigInput(BaseValidatorModel):
    PreviousEarthObservationJobArn: Optional[str] = None
    RasterDataCollectionQuery: Optional[RasterDataCollectionQueryInput] = None


class SearchRasterDataCollectionInput(BaseValidatorModel):
    Arn: str
    RasterDataCollectionQuery: RasterDataCollectionQueryWithBandFilterInput
    NextToken: Optional[str] = None


class StartEarthObservationJobInput(BaseValidatorModel):
    ExecutionRoleArn: str
    InputConfig: InputConfigInput
    JobConfig: JobConfigInputUnion
    Name: str
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None