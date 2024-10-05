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
from aws_resource_validator.pydantic_models.sagemaker_geospatial_constants import *

class MultiPolygonGeometryInputTypeDef(BaseValidatorModel):
    Coordinates: List[List[List[List[float]]]]

class PolygonGeometryInputTypeDef(BaseValidatorModel):
    Coordinates: List[List[List[float]]]

class AssetValueTypeDef(BaseValidatorModel):
    Href: Optional[str] = None

class CloudRemovalConfigInputTypeDef(BaseValidatorModel):
    AlgorithmName: Optional[Literal["INTERPOLATION"]] = None
    InterpolationValue: Optional[str] = None
    TargetBands: Optional[List[str]] = None

class OperationTypeDef(BaseValidatorModel):
    Equation: str
    Name: str
    OutputType: Optional[OutputTypeType] = None

class DeleteEarthObservationJobInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class DeleteVectorEnrichmentJobInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class EarthObservationJobErrorDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Type: Optional[EarthObservationJobErrorTypeType] = None

class EoCloudCoverInputTypeDef(BaseValidatorModel):
    LowerBound: float
    UpperBound: float

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ExportErrorDetailsOutputTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Type: Optional[ExportErrorTypeType] = None

class ExportS3DataInputTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class VectorEnrichmentJobS3DataTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    Name: str
    Type: str
    Maximum: Optional[float] = None
    Minimum: Optional[float] = None

class GeoMosaicConfigInputTypeDef(BaseValidatorModel):
    AlgorithmName: Optional[AlgorithmNameGeoMosaicType] = None
    TargetBands: Optional[List[str]] = None

class GeometryTypeDef(BaseValidatorModel):
    Coordinates: List[List[List[float]]]
    Type: str

class GetEarthObservationJobInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class OutputBandTypeDef(BaseValidatorModel):
    BandName: str
    OutputDataType: OutputTypeType

class GetRasterDataCollectionInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class GetTileInputRequestTypeDef(BaseValidatorModel):
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

class GetVectorEnrichmentJobInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class VectorEnrichmentJobErrorDetailsTypeDef(BaseValidatorModel):
    ErrorMessage: Optional[str] = None
    ErrorType: Optional[VectorEnrichmentJobErrorTypeType] = None

class VectorEnrichmentJobExportErrorDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Type: Optional[VectorEnrichmentJobExportErrorTypeType] = None

class PropertiesTypeDef(BaseValidatorModel):
    EoCloudCover: Optional[float] = None
    LandsatCloudCoverLand: Optional[float] = None
    Platform: Optional[str] = None
    ViewOffNadir: Optional[float] = None
    ViewSunAzimuth: Optional[float] = None
    ViewSunElevation: Optional[float] = None

class TemporalStatisticsConfigInputTypeDef(BaseValidatorModel):
    Statistics: List[TemporalStatisticsType]
    GroupBy: Optional[GroupByType] = None
    TargetBands: Optional[List[str]] = None

class ZonalStatisticsConfigInputTypeDef(BaseValidatorModel):
    Statistics: List[ZonalStatisticsType]
    ZoneS3Path: str
    TargetBands: Optional[List[str]] = None
    ZoneS3PathKmsKeyId: Optional[str] = None

class LandsatCloudCoverLandInputTypeDef(BaseValidatorModel):
    LowerBound: float
    UpperBound: float

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEarthObservationJobInputRequestTypeDef(BaseValidatorModel):
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

class ListRasterDataCollectionsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListVectorEnrichmentJobInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[str] = None

class ListVectorEnrichmentJobOutputConfigTypeDef(BaseValidatorModel):
    Arn: str
    CreationTime: datetime
    DurationInSeconds: int
    Name: str
    Status: VectorEnrichmentJobStatusType
    Type: VectorEnrichmentJobTypeType
    Tags: Optional[Dict[str, str]] = None

class MapMatchingConfigTypeDef(BaseValidatorModel):
    IdAttributeName: str
    TimestampAttributeName: str
    XAttributeName: str
    YAttributeName: str

class UserDefinedTypeDef(BaseValidatorModel):
    Unit: Literal["METERS"]
    Value: float

class PlatformInputTypeDef(BaseValidatorModel):
    Value: str
    ComparisonOperator: Optional[ComparisonOperatorType] = None

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

class StopEarthObservationJobInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class StopVectorEnrichmentJobInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AreaOfInterestGeometryTypeDef(BaseValidatorModel):
    MultiPolygonGeometry: Optional[MultiPolygonGeometryInputTypeDef] = None
    PolygonGeometry: Optional[PolygonGeometryInputTypeDef] = None

class CustomIndicesInputTypeDef(BaseValidatorModel):
    Operations: Optional[List[OperationTypeDef]] = None

class GetTileOutputTypeDef(BaseValidatorModel):
    BinaryFile: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportErrorDetailsTypeDef(BaseValidatorModel):
    ExportResults: Optional[ExportErrorDetailsOutputTypeDef] = None
    ExportSourceImages: Optional[ExportErrorDetailsOutputTypeDef] = None

class OutputConfigInputTypeDef(BaseValidatorModel):
    S3Data: ExportS3DataInputTypeDef

class ExportVectorEnrichmentJobOutputConfigTypeDef(BaseValidatorModel):
    S3Data: VectorEnrichmentJobS3DataTypeDef

class VectorEnrichmentJobDataSourceConfigInputTypeDef(BaseValidatorModel):
    S3Data: Optional[VectorEnrichmentJobS3DataTypeDef] = None

class GetRasterDataCollectionOutputTypeDef(BaseValidatorModel):
    Arn: str
    Description: str
    DescriptionPageUrl: str
    ImageSourceBands: List[str]
    Name: str
    SupportedFilters: List[FilterTypeDef]
    Tags: Dict[str, str]
    Type: DataCollectionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class RasterDataCollectionMetadataTypeDef(BaseValidatorModel):
    Arn: str
    Description: str
    Name: str
    SupportedFilters: List[FilterTypeDef]
    Type: DataCollectionTypeType
    DescriptionPageUrl: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ItemSourceTypeDef(BaseValidatorModel):
    DateTime: datetime
    Geometry: GeometryTypeDef
    Id: str
    Assets: Optional[Dict[str, AssetValueTypeDef]] = None
    Properties: Optional[PropertiesTypeDef] = None

class ListEarthObservationJobInputListEarthObservationJobsPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[EarthObservationJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRasterDataCollectionsInputListRasterDataCollectionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVectorEnrichmentJobInputListVectorEnrichmentJobsPaginateTypeDef(BaseValidatorModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None
    StatusEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEarthObservationJobOutputTypeDef(BaseValidatorModel):
    EarthObservationJobSummaries: List[ListEarthObservationJobOutputConfigTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVectorEnrichmentJobOutputTypeDef(BaseValidatorModel):
    NextToken: str
    VectorEnrichmentJobSummaries: List[ListVectorEnrichmentJobOutputConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class TimeRangeFilterInputTypeDef(BaseValidatorModel):
    EndTime: TimestampTypeDef
    StartTime: TimestampTypeDef

class AreaOfInterestTypeDef(BaseValidatorModel):
    AreaOfInterestGeometry: Optional[AreaOfInterestGeometryTypeDef] = None

class BandMathConfigInputTypeDef(BaseValidatorModel):
    CustomIndices: Optional[CustomIndicesInputTypeDef] = None
    PredefinedIndices: Optional[List[str]] = None

class ExportEarthObservationJobInputRequestTypeDef(BaseValidatorModel):
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

class ExportVectorEnrichmentJobInputRequestTypeDef(BaseValidatorModel):
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

class ListRasterDataCollectionsOutputTypeDef(BaseValidatorModel):
    NextToken: str
    RasterDataCollectionSummaries: List[RasterDataCollectionMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchRasterDataCollectionOutputTypeDef(BaseValidatorModel):
    ApproximateResultCount: int
    Items: List[ItemSourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResamplingConfigInputTypeDef(BaseValidatorModel):
    OutputResolution: OutputResolutionResamplingInputTypeDef
    AlgorithmName: Optional[AlgorithmNameResamplingType] = None
    TargetBands: Optional[List[str]] = None

class StackConfigInputTypeDef(BaseValidatorModel):
    OutputResolution: Optional[OutputResolutionStackInputTypeDef] = None
    TargetBands: Optional[List[str]] = None

class PropertyFilterTypeDef(BaseValidatorModel):
    Property: PropertyTypeDef

class GetVectorEnrichmentJobOutputTypeDef(BaseValidatorModel):
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

class StartVectorEnrichmentJobInputRequestTypeDef(BaseValidatorModel):
    ExecutionRoleArn: str
    InputConfig: VectorEnrichmentJobInputConfigTypeDef
    JobConfig: VectorEnrichmentJobConfigTypeDef
    Name: str
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class StartVectorEnrichmentJobOutputTypeDef(BaseValidatorModel):
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

class JobConfigInputTypeDef(BaseValidatorModel):
    BandMathConfig: Optional[BandMathConfigInputTypeDef] = None
    CloudMaskingConfig: Optional[Dict[str, Any]] = None
    CloudRemovalConfig: Optional[CloudRemovalConfigInputTypeDef] = None
    GeoMosaicConfig: Optional[GeoMosaicConfigInputTypeDef] = None
    LandCoverSegmentationConfig: Optional[Dict[str, Any]] = None
    ResamplingConfig: Optional[ResamplingConfigInputTypeDef] = None
    StackConfig: Optional[StackConfigInputTypeDef] = None
    TemporalStatisticsConfig: Optional[TemporalStatisticsConfigInputTypeDef] = None
    ZonalStatisticsConfig: Optional[ZonalStatisticsConfigInputTypeDef] = None

class PropertyFiltersTypeDef(BaseValidatorModel):
    LogicalOperator: Optional[Literal["AND"]] = None
    Properties: Optional[List[PropertyFilterTypeDef]] = None

class RasterDataCollectionQueryInputTypeDef(BaseValidatorModel):
    RasterDataCollectionArn: str
    TimeRangeFilter: TimeRangeFilterInputTypeDef
    AreaOfInterest: Optional[AreaOfInterestTypeDef] = None
    PropertyFilters: Optional[PropertyFiltersTypeDef] = None

class RasterDataCollectionQueryOutputTypeDef(BaseValidatorModel):
    RasterDataCollectionArn: str
    RasterDataCollectionName: str
    TimeRangeFilter: TimeRangeFilterOutputTypeDef
    AreaOfInterest: Optional[AreaOfInterestTypeDef] = None
    PropertyFilters: Optional[PropertyFiltersTypeDef] = None

class RasterDataCollectionQueryWithBandFilterInputTypeDef(BaseValidatorModel):
    TimeRangeFilter: TimeRangeFilterInputTypeDef
    AreaOfInterest: Optional[AreaOfInterestTypeDef] = None
    BandFilter: Optional[Sequence[str]] = None
    PropertyFilters: Optional[PropertyFiltersTypeDef] = None

class InputConfigInputTypeDef(BaseValidatorModel):
    PreviousEarthObservationJobArn: Optional[str] = None
    RasterDataCollectionQuery: Optional[RasterDataCollectionQueryInputTypeDef] = None

class InputConfigOutputTypeDef(BaseValidatorModel):
    PreviousEarthObservationJobArn: Optional[str] = None
    RasterDataCollectionQuery: Optional[RasterDataCollectionQueryOutputTypeDef] = None

class SearchRasterDataCollectionInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    RasterDataCollectionQuery: RasterDataCollectionQueryWithBandFilterInputTypeDef
    NextToken: Optional[str] = None

class StartEarthObservationJobInputRequestTypeDef(BaseValidatorModel):
    ExecutionRoleArn: str
    InputConfig: InputConfigInputTypeDef
    JobConfig: JobConfigInputTypeDef
    Name: str
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class GetEarthObservationJobOutputTypeDef(BaseValidatorModel):
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

class StartEarthObservationJobOutputTypeDef(BaseValidatorModel):
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

