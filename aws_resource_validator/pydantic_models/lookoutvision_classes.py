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
from aws_resource_validator.pydantic_models.lookoutvision_constants import *

class PixelAnomalyTypeDef(BaseValidatorModel):
    TotalPercentageArea: Optional[float] = None
    Color: Optional[str] = None


class DatasetMetadataTypeDef(BaseValidatorModel):
    DatasetType: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CreateProjectRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ClientToken: Optional[str] = None


class ProjectMetadataTypeDef(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    ProjectName: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None


class DatasetImageStatsTypeDef(BaseValidatorModel):
    Total: Optional[int] = None
    Labeled: Optional[int] = None
    Normal: Optional[int] = None
    Anomaly: Optional[int] = None


class InputS3ObjectTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    ClientToken: Optional[str] = None


class DeleteModelRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None


class DeleteProjectRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ClientToken: Optional[str] = None


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str


class DescribeModelPackagingJobRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    JobName: str


class DescribeModelRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str


class DescribeProjectRequestTypeDef(BaseValidatorModel):
    ProjectName: str


class S3LocationTypeDef(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class TargetPlatformTypeDef(BaseValidatorModel):
    Os: Literal["LINUX"]
    Arch: TargetPlatformArchType
    Accelerator: Optional[Literal["NVIDIA"]] = None


class GreengrassOutputDetailsTypeDef(BaseValidatorModel):
    ComponentVersionArn: Optional[str] = None
    ComponentName: Optional[str] = None
    ComponentVersion: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListModelPackagingJobsRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ModelPackagingJobMetadataTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    ProjectName: Optional[str] = None
    ModelVersion: Optional[str] = None
    ModelPackagingJobDescription: Optional[str] = None
    ModelPackagingMethod: Optional[str] = None
    Status: Optional[ModelPackagingJobStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class ListModelsRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProjectsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ModelPerformanceTypeDef(BaseValidatorModel):
    F1Score: Optional[float] = None
    Recall: Optional[float] = None
    Precision: Optional[float] = None


class OutputS3ObjectTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str


class StartModelRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    MinInferenceUnits: int
    ClientToken: Optional[str] = None
    MaxInferenceUnits: Optional[int] = None


class StopModelRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class AnomalyTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    PixelAnomaly: Optional[PixelAnomalyTypeDef] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class DetectAnomaliesRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    Body: BlobTypeDef
    ContentType: str


class UpdateDatasetEntriesRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    Changes: BlobTypeDef
    ClientToken: Optional[str] = None


class ProjectDescriptionTypeDef(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    ProjectName: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Datasets: Optional[List[DatasetMetadataTypeDef]] = None


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    DatasetMetadata: DatasetMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteModelResponseTypeDef(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProjectResponseTypeDef(BaseValidatorModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListDatasetEntriesResponseTypeDef(BaseValidatorModel):
    DatasetEntries: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartModelPackagingJobResponseTypeDef(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartModelResponseTypeDef(BaseValidatorModel):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StopModelResponseTypeDef(BaseValidatorModel):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDatasetEntriesResponseTypeDef(BaseValidatorModel):
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateProjectResponseTypeDef(BaseValidatorModel):
    ProjectMetadata: ProjectMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListProjectsResponseTypeDef(BaseValidatorModel):
    Projects: List[ProjectMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DatasetDescriptionTypeDef(BaseValidatorModel):
    ProjectName: Optional[str] = None
    DatasetType: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    ImageStats: Optional[DatasetImageStatsTypeDef] = None


class DatasetGroundTruthManifestTypeDef(BaseValidatorModel):
    S3Object: Optional[InputS3ObjectTypeDef] = None


class OutputConfigTypeDef(BaseValidatorModel):
    S3Location: S3LocationTypeDef


class GreengrassConfigurationOutputTypeDef(BaseValidatorModel):
    S3OutputLocation: S3LocationTypeDef
    ComponentName: str
    CompilerOptions: Optional[str] = None
    TargetDevice: Optional[Literal["jetson_xavier"]] = None
    TargetPlatform: Optional[TargetPlatformTypeDef] = None
    ComponentVersion: Optional[str] = None
    ComponentDescription: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class GreengrassConfigurationTypeDef(BaseValidatorModel):
    S3OutputLocation: S3LocationTypeDef
    ComponentName: str
    CompilerOptions: Optional[str] = None
    TargetDevice: Optional[Literal["jetson_xavier"]] = None
    TargetPlatform: Optional[TargetPlatformTypeDef] = None
    ComponentVersion: Optional[str] = None
    ComponentDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ModelPackagingOutputDetailsTypeDef(BaseValidatorModel):
    Greengrass: Optional[GreengrassOutputDetailsTypeDef] = None


class ListModelPackagingJobsRequestPaginateTypeDef(BaseValidatorModel):
    ProjectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListModelsRequestPaginateTypeDef(BaseValidatorModel):
    ProjectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListDatasetEntriesRequestPaginateTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    Labeled: Optional[bool] = None
    AnomalyClass: Optional[str] = None
    BeforeCreationDate: Optional[TimestampTypeDef] = None
    AfterCreationDate: Optional[TimestampTypeDef] = None
    SourceRefContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetEntriesRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    Labeled: Optional[bool] = None
    AnomalyClass: Optional[str] = None
    BeforeCreationDate: Optional[TimestampTypeDef] = None
    AfterCreationDate: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SourceRefContains: Optional[str] = None


class ListModelPackagingJobsResponseTypeDef(BaseValidatorModel):
    ModelPackagingJobs: List[ModelPackagingJobMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ModelMetadataTypeDef(BaseValidatorModel):
    CreationTimestamp: Optional[datetime] = None
    ModelVersion: Optional[str] = None
    ModelArn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[ModelStatusType] = None
    StatusMessage: Optional[str] = None
    Performance: Optional[ModelPerformanceTypeDef] = None


class ImageSourceTypeDef(BaseValidatorModel):
    pass


class DetectAnomalyResultTypeDef(BaseValidatorModel):
    Source: Optional[ImageSourceTypeDef] = None
    IsAnomalous: Optional[bool] = None
    Confidence: Optional[float] = None
    Anomalies: Optional[List[AnomalyTypeDef]] = None
    AnomalyMask: Optional[bytes] = None


class DescribeProjectResponseTypeDef(BaseValidatorModel):
    ProjectDescription: ProjectDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    DatasetDescription: DatasetDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DatasetSourceTypeDef(BaseValidatorModel):
    GroundTruthManifest: Optional[DatasetGroundTruthManifestTypeDef] = None


class CreateModelRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    OutputConfig: OutputConfigTypeDef
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ModelDescriptionTypeDef(BaseValidatorModel):
    ModelVersion: Optional[str] = None
    ModelArn: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Description: Optional[str] = None
    Status: Optional[ModelStatusType] = None
    StatusMessage: Optional[str] = None
    Performance: Optional[ModelPerformanceTypeDef] = None
    OutputConfig: Optional[OutputConfigTypeDef] = None
    EvaluationManifest: Optional[OutputS3ObjectTypeDef] = None
    EvaluationResult: Optional[OutputS3ObjectTypeDef] = None
    EvaluationEndTimestamp: Optional[datetime] = None
    KmsKeyId: Optional[str] = None
    MinInferenceUnits: Optional[int] = None
    MaxInferenceUnits: Optional[int] = None


class ModelPackagingConfigurationOutputTypeDef(BaseValidatorModel):
    Greengrass: GreengrassConfigurationOutputTypeDef


class ModelPackagingConfigurationTypeDef(BaseValidatorModel):
    Greengrass: GreengrassConfigurationTypeDef


class CreateModelResponseTypeDef(BaseValidatorModel):
    ModelMetadata: ModelMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListModelsResponseTypeDef(BaseValidatorModel):
    Models: List[ModelMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DetectAnomaliesResponseTypeDef(BaseValidatorModel):
    DetectAnomalyResult: DetectAnomalyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    DatasetSource: Optional[DatasetSourceTypeDef] = None
    ClientToken: Optional[str] = None


class DescribeModelResponseTypeDef(BaseValidatorModel):
    ModelDescription: ModelDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModelPackagingDescriptionTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    ProjectName: Optional[str] = None
    ModelVersion: Optional[str] = None
    ModelPackagingConfiguration: Optional[ModelPackagingConfigurationOutputTypeDef] = None
    ModelPackagingJobDescription: Optional[str] = None
    ModelPackagingMethod: Optional[str] = None
    ModelPackagingOutputDetails: Optional[ModelPackagingOutputDetailsTypeDef] = None
    Status: Optional[ModelPackagingJobStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class DescribeModelPackagingJobResponseTypeDef(BaseValidatorModel):
    ModelPackagingDescription: ModelPackagingDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModelPackagingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class StartModelPackagingJobRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    Configuration: ModelPackagingConfigurationUnionTypeDef
    JobName: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None


