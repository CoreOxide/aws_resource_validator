from datetime import datetime
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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteDatasetRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    ClientToken: Optional[str] = None

class DeleteModelRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ClientToken: Optional[str] = None

class DescribeDatasetRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str

class DescribeModelPackagingJobRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    JobName: str

class DescribeModelRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str

class DescribeProjectRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str

class ImageSourceTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

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

class ListModelPackagingJobsRequestRequestTypeDef(BaseValidatorModel):
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

class ListModelsRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ModelPerformanceTypeDef(BaseValidatorModel):
    F1Score: Optional[float] = None
    Recall: Optional[float] = None
    Precision: Optional[float] = None

class OutputS3ObjectTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str

class StartModelRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    MinInferenceUnits: int
    ClientToken: Optional[str] = None
    MaxInferenceUnits: Optional[int] = None

class StopModelRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AnomalyTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    PixelAnomaly: Optional[PixelAnomalyTypeDef] = None

class DetectAnomaliesRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    Body: BlobTypeDef
    ContentType: str

class UpdateDatasetEntriesRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateProjectResponseTypeDef(BaseValidatorModel):
    ProjectMetadata: ProjectMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResponseTypeDef(BaseValidatorModel):
    Projects: List[ProjectMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class GreengrassConfigurationTypeDef(BaseValidatorModel):
    S3OutputLocation: S3LocationTypeDef
    ComponentName: str
    CompilerOptions: Optional[str] = None
    TargetDevice: Optional[Literal["jetson_xavier"]] = None
    TargetPlatform: Optional[TargetPlatformTypeDef] = None
    ComponentVersion: Optional[str] = None
    ComponentDescription: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ModelPackagingOutputDetailsTypeDef(BaseValidatorModel):
    Greengrass: Optional[GreengrassOutputDetailsTypeDef] = None

class ListModelPackagingJobsRequestListModelPackagingJobsPaginateTypeDef(BaseValidatorModel):
    ProjectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelsRequestListModelsPaginateTypeDef(BaseValidatorModel):
    ProjectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    Labeled: Optional[bool] = None
    AnomalyClass: Optional[str] = None
    BeforeCreationDate: Optional[TimestampTypeDef] = None
    AfterCreationDate: Optional[TimestampTypeDef] = None
    SourceRefContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetEntriesRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModelMetadataTypeDef(BaseValidatorModel):
    CreationTimestamp: Optional[datetime] = None
    ModelVersion: Optional[str] = None
    ModelArn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[ModelStatusType] = None
    StatusMessage: Optional[str] = None
    Performance: Optional[ModelPerformanceTypeDef] = None

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

class CreateModelRequestRequestTypeDef(BaseValidatorModel):
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

class ModelPackagingConfigurationTypeDef(BaseValidatorModel):
    Greengrass: GreengrassConfigurationTypeDef

class CreateModelResponseTypeDef(BaseValidatorModel):
    ModelMetadata: ModelMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListModelsResponseTypeDef(BaseValidatorModel):
    Models: List[ModelMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectAnomaliesResponseTypeDef(BaseValidatorModel):
    DetectAnomalyResult: DetectAnomalyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetRequestRequestTypeDef(BaseValidatorModel):
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
    ModelPackagingConfiguration: Optional[ModelPackagingConfigurationTypeDef] = None
    ModelPackagingJobDescription: Optional[str] = None
    ModelPackagingMethod: Optional[str] = None
    ModelPackagingOutputDetails: Optional[ModelPackagingOutputDetailsTypeDef] = None
    Status: Optional[ModelPackagingJobStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class StartModelPackagingJobRequestRequestTypeDef(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    Configuration: ModelPackagingConfigurationTypeDef
    JobName: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None

class DescribeModelPackagingJobResponseTypeDef(BaseValidatorModel):
    ModelPackagingDescription: ModelPackagingDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

