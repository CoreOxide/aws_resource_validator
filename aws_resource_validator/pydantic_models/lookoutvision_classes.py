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
from aws_resource_validator.pydantic_models.lookoutvision_constants import *

class PixelAnomalyTypeDef(BaseModel):
    TotalPercentageArea: Optional[float] = None
    Color: Optional[str] = None

class DatasetMetadataTypeDef(BaseModel):
    DatasetType: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateProjectRequestRequestTypeDef(BaseModel):
    ProjectName: str
    ClientToken: Optional[str] = None

class ProjectMetadataTypeDef(BaseModel):
    ProjectArn: Optional[str] = None
    ProjectName: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None

class DatasetImageStatsTypeDef(BaseModel):
    Total: Optional[int] = None
    Labeled: Optional[int] = None
    Normal: Optional[int] = None
    Anomaly: Optional[int] = None

class InputS3ObjectTypeDef(BaseModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    ProjectName: str
    DatasetType: str
    ClientToken: Optional[str] = None

class DeleteModelRequestRequestTypeDef(BaseModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None

class DeleteProjectRequestRequestTypeDef(BaseModel):
    ProjectName: str
    ClientToken: Optional[str] = None

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    ProjectName: str
    DatasetType: str

class DescribeModelPackagingJobRequestRequestTypeDef(BaseModel):
    ProjectName: str
    JobName: str

class DescribeModelRequestRequestTypeDef(BaseModel):
    ProjectName: str
    ModelVersion: str

class DescribeProjectRequestRequestTypeDef(BaseModel):
    ProjectName: str

class ImageSourceTypeDef(BaseModel):
    Type: Optional[str] = None

class S3LocationTypeDef(BaseModel):
    Bucket: str
    Prefix: Optional[str] = None

class TargetPlatformTypeDef(BaseModel):
    Os: Literal["LINUX"]
    Arch: TargetPlatformArchType
    Accelerator: Optional[Literal["NVIDIA"]] = None

class GreengrassOutputDetailsTypeDef(BaseModel):
    ComponentVersionArn: Optional[str] = None
    ComponentName: Optional[str] = None
    ComponentVersion: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListModelPackagingJobsRequestRequestTypeDef(BaseModel):
    ProjectName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ModelPackagingJobMetadataTypeDef(BaseModel):
    JobName: Optional[str] = None
    ProjectName: Optional[str] = None
    ModelVersion: Optional[str] = None
    ModelPackagingJobDescription: Optional[str] = None
    ModelPackagingMethod: Optional[str] = None
    Status: Optional[ModelPackagingJobStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class ListModelsRequestRequestTypeDef(BaseModel):
    ProjectName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProjectsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ModelPerformanceTypeDef(BaseModel):
    F1Score: Optional[float] = None
    Recall: Optional[float] = None
    Precision: Optional[float] = None

class OutputS3ObjectTypeDef(BaseModel):
    Bucket: str
    Key: str

class StartModelRequestRequestTypeDef(BaseModel):
    ProjectName: str
    ModelVersion: str
    MinInferenceUnits: int
    ClientToken: Optional[str] = None
    MaxInferenceUnits: Optional[int] = None

class StopModelRequestRequestTypeDef(BaseModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AnomalyTypeDef(BaseModel):
    Name: Optional[str] = None
    PixelAnomaly: Optional[PixelAnomalyTypeDef] = None

class DetectAnomaliesRequestRequestTypeDef(BaseModel):
    ProjectName: str
    ModelVersion: str
    Body: BlobTypeDef
    ContentType: str

class UpdateDatasetEntriesRequestRequestTypeDef(BaseModel):
    ProjectName: str
    DatasetType: str
    Changes: BlobTypeDef
    ClientToken: Optional[str] = None

class ProjectDescriptionTypeDef(BaseModel):
    ProjectArn: Optional[str] = None
    ProjectName: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Datasets: Optional[List[DatasetMetadataTypeDef]] = None

class CreateDatasetResponseTypeDef(BaseModel):
    DatasetMetadata: DatasetMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteModelResponseTypeDef(BaseModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResponseTypeDef(BaseModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetEntriesResponseTypeDef(BaseModel):
    DatasetEntries: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartModelPackagingJobResponseTypeDef(BaseModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartModelResponseTypeDef(BaseModel):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopModelResponseTypeDef(BaseModel):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetEntriesResponseTypeDef(BaseModel):
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateProjectResponseTypeDef(BaseModel):
    ProjectMetadata: ProjectMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResponseTypeDef(BaseModel):
    Projects: List[ProjectMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetDescriptionTypeDef(BaseModel):
    ProjectName: Optional[str] = None
    DatasetType: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    ImageStats: Optional[DatasetImageStatsTypeDef] = None

class DatasetGroundTruthManifestTypeDef(BaseModel):
    S3Object: Optional[InputS3ObjectTypeDef] = None

class OutputConfigTypeDef(BaseModel):
    S3Location: S3LocationTypeDef

class GreengrassConfigurationTypeDef(BaseModel):
    S3OutputLocation: S3LocationTypeDef
    ComponentName: str
    CompilerOptions: Optional[str] = None
    TargetDevice: Optional[Literal["jetson_xavier"]] = None
    TargetPlatform: Optional[TargetPlatformTypeDef] = None
    ComponentVersion: Optional[str] = None
    ComponentDescription: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ModelPackagingOutputDetailsTypeDef(BaseModel):
    Greengrass: Optional[GreengrassOutputDetailsTypeDef] = None

class ListModelPackagingJobsRequestListModelPackagingJobsPaginateTypeDef(BaseModel):
    ProjectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelsRequestListModelsPaginateTypeDef(BaseModel):
    ProjectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef(BaseModel):
    ProjectName: str
    DatasetType: str
    Labeled: Optional[bool] = None
    AnomalyClass: Optional[str] = None
    BeforeCreationDate: Optional[TimestampTypeDef] = None
    AfterCreationDate: Optional[TimestampTypeDef] = None
    SourceRefContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetEntriesRequestRequestTypeDef(BaseModel):
    ProjectName: str
    DatasetType: str
    Labeled: Optional[bool] = None
    AnomalyClass: Optional[str] = None
    BeforeCreationDate: Optional[TimestampTypeDef] = None
    AfterCreationDate: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SourceRefContains: Optional[str] = None

class ListModelPackagingJobsResponseTypeDef(BaseModel):
    ModelPackagingJobs: List[ModelPackagingJobMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModelMetadataTypeDef(BaseModel):
    CreationTimestamp: Optional[datetime] = None
    ModelVersion: Optional[str] = None
    ModelArn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[ModelStatusType] = None
    StatusMessage: Optional[str] = None
    Performance: Optional[ModelPerformanceTypeDef] = None

class DetectAnomalyResultTypeDef(BaseModel):
    Source: Optional[ImageSourceTypeDef] = None
    IsAnomalous: Optional[bool] = None
    Confidence: Optional[float] = None
    Anomalies: Optional[List[AnomalyTypeDef]] = None
    AnomalyMask: Optional[bytes] = None

class DescribeProjectResponseTypeDef(BaseModel):
    ProjectDescription: ProjectDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetResponseTypeDef(BaseModel):
    DatasetDescription: DatasetDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetSourceTypeDef(BaseModel):
    GroundTruthManifest: Optional[DatasetGroundTruthManifestTypeDef] = None

class CreateModelRequestRequestTypeDef(BaseModel):
    ProjectName: str
    OutputConfig: OutputConfigTypeDef
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ModelDescriptionTypeDef(BaseModel):
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

class ModelPackagingConfigurationTypeDef(BaseModel):
    Greengrass: GreengrassConfigurationTypeDef

class CreateModelResponseTypeDef(BaseModel):
    ModelMetadata: ModelMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListModelsResponseTypeDef(BaseModel):
    Models: List[ModelMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectAnomaliesResponseTypeDef(BaseModel):
    DetectAnomalyResult: DetectAnomalyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetRequestRequestTypeDef(BaseModel):
    ProjectName: str
    DatasetType: str
    DatasetSource: Optional[DatasetSourceTypeDef] = None
    ClientToken: Optional[str] = None

class DescribeModelResponseTypeDef(BaseModel):
    ModelDescription: ModelDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModelPackagingDescriptionTypeDef(BaseModel):
    JobName: Optional[str] = None
    ProjectName: Optional[str] = None
    ModelVersion: Optional[str] = None
    ModelPackagingConfiguration: Optional[ModelPackagingConfigurationTypeDef] = None
    ModelPackagingJobDescription: Optional[str] = None
    ModelPackagingMethod: Optional[str] = None
    ModelPackagingOutputDetails: Optional[ModelPackagingOutputDetailsTypeDef] = None
    Status: Optional[ModelPackagingJobStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class StartModelPackagingJobRequestRequestTypeDef(BaseModel):
    ProjectName: str
    ModelVersion: str
    Configuration: ModelPackagingConfigurationTypeDef
    JobName: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None

class DescribeModelPackagingJobResponseTypeDef(BaseModel):
    ModelPackagingDescription: ModelPackagingDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

