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

class PixelAnomaly(BaseValidatorModel):
    TotalPercentageArea: Optional[float] = None
    Color: Optional[str] = None


class DatasetMetadata(BaseValidatorModel):
    DatasetType: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CreateProjectRequest(BaseValidatorModel):
    ProjectName: str
    ClientToken: Optional[str] = None


class ProjectMetadata(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    ProjectName: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None


class DatasetImageStats(BaseValidatorModel):
    Total: Optional[int] = None
    Labeled: Optional[int] = None
    Normal: Optional[int] = None
    Anomaly: Optional[int] = None


class InputS3Object(BaseValidatorModel):
    Bucket: str
    Key: str
    VersionId: Optional[str] = None


class DeleteDatasetRequest(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    ClientToken: Optional[str] = None


class DeleteModelRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None


class DeleteProjectRequest(BaseValidatorModel):
    ProjectName: str
    ClientToken: Optional[str] = None


class DescribeDatasetRequest(BaseValidatorModel):
    ProjectName: str
    DatasetType: str


class DescribeModelPackagingJobRequest(BaseValidatorModel):
    ProjectName: str
    JobName: str


class DescribeModelRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str


class DescribeProjectRequest(BaseValidatorModel):
    ProjectName: str


class S3Location(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class TargetPlatform(BaseValidatorModel):
    Os: Literal["LINUX"]
    Arch: TargetPlatformArchType
    Accelerator: Optional[Literal["NVIDIA"]] = None


class GreengrassOutputDetails(BaseValidatorModel):
    ComponentVersionArn: Optional[str] = None
    ComponentName: Optional[str] = None
    ComponentVersion: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListModelPackagingJobsRequest(BaseValidatorModel):
    ProjectName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ModelPackagingJobMetadata(BaseValidatorModel):
    JobName: Optional[str] = None
    ProjectName: Optional[str] = None
    ModelVersion: Optional[str] = None
    ModelPackagingJobDescription: Optional[str] = None
    ModelPackagingMethod: Optional[str] = None
    Status: Optional[ModelPackagingJobStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class ListModelsRequest(BaseValidatorModel):
    ProjectName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProjectsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ModelPerformance(BaseValidatorModel):
    F1Score: Optional[float] = None
    Recall: Optional[float] = None
    Precision: Optional[float] = None


class OutputS3Object(BaseValidatorModel):
    Bucket: str
    Key: str


class StartModelRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    MinInferenceUnits: int
    ClientToken: Optional[str] = None
    MaxInferenceUnits: Optional[int] = None


class StopModelRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class Anomaly(BaseValidatorModel):
    Name: Optional[str] = None
    PixelAnomaly: Optional[PixelAnomaly] = None


class Blob(BaseValidatorModel):
    pass


class DetectAnomaliesRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    Body: Blob
    ContentType: str


class UpdateDatasetEntriesRequest(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    Changes: Blob
    ClientToken: Optional[str] = None


class ProjectDescription(BaseValidatorModel):
    ProjectArn: Optional[str] = None
    ProjectName: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Datasets: Optional[List[DatasetMetadata]] = None


class CreateDatasetResponse(BaseValidatorModel):
    DatasetMetadata: DatasetMetadata
    ResponseMetadata: ResponseMetadata


class DeleteModelResponse(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadata


class DeleteProjectResponse(BaseValidatorModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadata


class ListDatasetEntriesResponse(BaseValidatorModel):
    DatasetEntries: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartModelPackagingJobResponse(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadata


class StartModelResponse(BaseValidatorModel):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadata


class StopModelResponse(BaseValidatorModel):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadata


class UpdateDatasetEntriesResponse(BaseValidatorModel):
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class CreateProjectResponse(BaseValidatorModel):
    ProjectMetadata: ProjectMetadata
    ResponseMetadata: ResponseMetadata


class ListProjectsResponse(BaseValidatorModel):
    Projects: List[ProjectMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DatasetDescription(BaseValidatorModel):
    ProjectName: Optional[str] = None
    DatasetType: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Status: Optional[DatasetStatusType] = None
    StatusMessage: Optional[str] = None
    ImageStats: Optional[DatasetImageStats] = None


class DatasetGroundTruthManifest(BaseValidatorModel):
    S3Object: Optional[InputS3Object] = None


class OutputConfig(BaseValidatorModel):
    S3Location: S3Location


class GreengrassConfigurationOutput(BaseValidatorModel):
    S3OutputLocation: S3Location
    ComponentName: str
    CompilerOptions: Optional[str] = None
    TargetDevice: Optional[Literal["jetson_xavier"]] = None
    TargetPlatform: Optional[TargetPlatform] = None
    ComponentVersion: Optional[str] = None
    ComponentDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class GreengrassConfiguration(BaseValidatorModel):
    S3OutputLocation: S3Location
    ComponentName: str
    CompilerOptions: Optional[str] = None
    TargetDevice: Optional[Literal["jetson_xavier"]] = None
    TargetPlatform: Optional[TargetPlatform] = None
    ComponentVersion: Optional[str] = None
    ComponentDescription: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class ModelPackagingOutputDetails(BaseValidatorModel):
    Greengrass: Optional[GreengrassOutputDetails] = None


class ListModelPackagingJobsRequestPaginate(BaseValidatorModel):
    ProjectName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelsRequestPaginate(BaseValidatorModel):
    ProjectName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class ListDatasetEntriesRequestPaginate(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    Labeled: Optional[bool] = None
    AnomalyClass: Optional[str] = None
    BeforeCreationDate: Optional[Timestamp] = None
    AfterCreationDate: Optional[Timestamp] = None
    SourceRefContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetEntriesRequest(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    Labeled: Optional[bool] = None
    AnomalyClass: Optional[str] = None
    BeforeCreationDate: Optional[Timestamp] = None
    AfterCreationDate: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SourceRefContains: Optional[str] = None


class ListModelPackagingJobsResponse(BaseValidatorModel):
    ModelPackagingJobs: List[ModelPackagingJobMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModelMetadata(BaseValidatorModel):
    CreationTimestamp: Optional[datetime] = None
    ModelVersion: Optional[str] = None
    ModelArn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[ModelStatusType] = None
    StatusMessage: Optional[str] = None
    Performance: Optional[ModelPerformance] = None


class ImageSource(BaseValidatorModel):
    pass


class DetectAnomalyResult(BaseValidatorModel):
    Source: Optional[ImageSource] = None
    IsAnomalous: Optional[bool] = None
    Confidence: Optional[float] = None
    Anomalies: Optional[List[Anomaly]] = None
    AnomalyMask: Optional[bytes] = None


class DescribeProjectResponse(BaseValidatorModel):
    ProjectDescription: ProjectDescription
    ResponseMetadata: ResponseMetadata


class DescribeDatasetResponse(BaseValidatorModel):
    DatasetDescription: DatasetDescription
    ResponseMetadata: ResponseMetadata


class DatasetSource(BaseValidatorModel):
    GroundTruthManifest: Optional[DatasetGroundTruthManifest] = None


class CreateModelRequest(BaseValidatorModel):
    ProjectName: str
    OutputConfig: OutputConfig
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class ModelDescription(BaseValidatorModel):
    ModelVersion: Optional[str] = None
    ModelArn: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    Description: Optional[str] = None
    Status: Optional[ModelStatusType] = None
    StatusMessage: Optional[str] = None
    Performance: Optional[ModelPerformance] = None
    OutputConfig: Optional[OutputConfig] = None
    EvaluationManifest: Optional[OutputS3Object] = None
    EvaluationResult: Optional[OutputS3Object] = None
    EvaluationEndTimestamp: Optional[datetime] = None
    KmsKeyId: Optional[str] = None
    MinInferenceUnits: Optional[int] = None
    MaxInferenceUnits: Optional[int] = None


class ModelPackagingConfigurationOutput(BaseValidatorModel):
    Greengrass: GreengrassConfigurationOutput


class ModelPackagingConfiguration(BaseValidatorModel):
    Greengrass: GreengrassConfiguration


class CreateModelResponse(BaseValidatorModel):
    ModelMetadata: ModelMetadata
    ResponseMetadata: ResponseMetadata


class ListModelsResponse(BaseValidatorModel):
    Models: List[ModelMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DetectAnomaliesResponse(BaseValidatorModel):
    DetectAnomalyResult: DetectAnomalyResult
    ResponseMetadata: ResponseMetadata


class CreateDatasetRequest(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    DatasetSource: Optional[DatasetSource] = None
    ClientToken: Optional[str] = None


class DescribeModelResponse(BaseValidatorModel):
    ModelDescription: ModelDescription
    ResponseMetadata: ResponseMetadata


class ModelPackagingDescription(BaseValidatorModel):
    JobName: Optional[str] = None
    ProjectName: Optional[str] = None
    ModelVersion: Optional[str] = None
    ModelPackagingConfiguration: Optional[ModelPackagingConfigurationOutput] = None
    ModelPackagingJobDescription: Optional[str] = None
    ModelPackagingMethod: Optional[str] = None
    ModelPackagingOutputDetails: Optional[ModelPackagingOutputDetails] = None
    Status: Optional[ModelPackagingJobStatusType] = None
    StatusMessage: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None


class DescribeModelPackagingJobResponse(BaseValidatorModel):
    ModelPackagingDescription: ModelPackagingDescription
    ResponseMetadata: ResponseMetadata


class ModelPackagingConfigurationUnion(BaseValidatorModel):
    pass


class StartModelPackagingJobRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    Configuration: ModelPackagingConfigurationUnion
    JobName: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None


