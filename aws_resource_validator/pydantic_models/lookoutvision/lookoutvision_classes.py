from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lookoutvision.lookoutvision_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class PixelAnomaly(BaseValidatorModel):
    TotalPercentageArea: Optional[float] = None
    Color: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


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


# This class is the input for the 'create_project' function.
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


# This class is the input for the 'delete_model' function.
class DeleteModelRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None


# This class is the input for the 'delete_project' function.
class DeleteProjectRequest(BaseValidatorModel):
    ProjectName: str
    ClientToken: Optional[str] = None


# This class is the input for the 'describe_dataset' function.
class DescribeDatasetRequest(BaseValidatorModel):
    ProjectName: str
    DatasetType: str


# This class is the input for the 'describe_model_packaging_job' function.
class DescribeModelPackagingJobRequest(BaseValidatorModel):
    ProjectName: str
    JobName: str


# This class is the input for the 'describe_model' function.
class DescribeModelRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str


# This class is the input for the 'describe_project' function.
class DescribeProjectRequest(BaseValidatorModel):
    ProjectName: str


class ImageSource(BaseValidatorModel):
    Type: Optional[str] = None


class S3Location(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class TargetPlatform(BaseValidatorModel):
    Os: Literal['LINUX']
    Arch: TargetPlatformArchType
    Accelerator: Optional[Literal['NVIDIA']] = None


class GreengrassOutputDetails(BaseValidatorModel):
    ComponentVersionArn: Optional[str] = None
    ComponentName: Optional[str] = None
    ComponentVersion: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'list_model_packaging_jobs' function.
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


# This class is the input for the 'list_models' function.
class ListModelsRequest(BaseValidatorModel):
    ProjectName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_projects' function.
class ListProjectsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ModelPerformance(BaseValidatorModel):
    F1Score: Optional[float] = None
    Recall: Optional[float] = None
    Precision: Optional[float] = None


class OutputS3Object(BaseValidatorModel):
    Bucket: str
    Key: str


# This class is the input for the 'start_model' function.
class StartModelRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    MinInferenceUnits: int
    ClientToken: Optional[str] = None
    MaxInferenceUnits: Optional[int] = None


# This class is the input for the 'stop_model' function.
class StopModelRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    ClientToken: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class Anomaly(BaseValidatorModel):
    Name: Optional[str] = None
    PixelAnomaly: Optional[PixelAnomaly] = None


# This class is the input for the 'detect_anomalies' function.
class DetectAnomaliesRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    Body: Blob
    ContentType: str


# This class is the input for the 'update_dataset_entries' function.
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


# This class is the output for the 'create_dataset' function.
class CreateDatasetResponse(BaseValidatorModel):
    DatasetMetadata: DatasetMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_model' function.
class DeleteModelResponse(BaseValidatorModel):
    ModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_project' function.
class DeleteProjectResponse(BaseValidatorModel):
    ProjectArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_dataset_entries' function.
class ListDatasetEntriesResponse(BaseValidatorModel):
    DatasetEntries: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_model_packaging_job' function.
class StartModelPackagingJobResponse(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_model' function.
class StartModelResponse(BaseValidatorModel):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_model' function.
class StopModelResponse(BaseValidatorModel):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_dataset_entries' function.
class UpdateDatasetEntriesResponse(BaseValidatorModel):
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the output for the 'create_project' function.
class CreateProjectResponse(BaseValidatorModel):
    ProjectMetadata: ProjectMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_projects' function.
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
    TargetDevice: Optional[Literal['jetson_xavier']] = None
    TargetPlatform: Optional[TargetPlatform] = None
    ComponentVersion: Optional[str] = None
    ComponentDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class GreengrassConfiguration(BaseValidatorModel):
    S3OutputLocation: S3Location
    ComponentName: str
    CompilerOptions: Optional[str] = None
    TargetDevice: Optional[Literal['jetson_xavier']] = None
    TargetPlatform: Optional[TargetPlatform] = None
    ComponentVersion: Optional[str] = None
    ComponentDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None


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


class ListDatasetEntriesRequestPaginate(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    Labeled: Optional[bool] = None
    AnomalyClass: Optional[str] = None
    BeforeCreationDate: Optional[Timestamp] = None
    AfterCreationDate: Optional[Timestamp] = None
    SourceRefContains: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_dataset_entries' function.
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


# This class is the output for the 'list_model_packaging_jobs' function.
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


class DetectAnomalyResult(BaseValidatorModel):
    Source: Optional[ImageSource] = None
    IsAnomalous: Optional[bool] = None
    Confidence: Optional[float] = None
    Anomalies: Optional[List[Anomaly]] = None
    AnomalyMask: Optional[bytes] = None


# This class is the output for the 'describe_project' function.
class DescribeProjectResponse(BaseValidatorModel):
    ProjectDescription: ProjectDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_dataset' function.
class DescribeDatasetResponse(BaseValidatorModel):
    DatasetDescription: DatasetDescription
    ResponseMetadata: ResponseMetadata


class DatasetSource(BaseValidatorModel):
    GroundTruthManifest: Optional[DatasetGroundTruthManifest] = None


# This class is the input for the 'create_model' function.
class CreateModelRequest(BaseValidatorModel):
    ProjectName: str
    OutputConfig: OutputConfig
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


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


# This class is the output for the 'create_model' function.
class CreateModelResponse(BaseValidatorModel):
    ModelMetadata: ModelMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_models' function.
class ListModelsResponse(BaseValidatorModel):
    Models: List[ModelMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'detect_anomalies' function.
class DetectAnomaliesResponse(BaseValidatorModel):
    DetectAnomalyResult: DetectAnomalyResult
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_dataset' function.
class CreateDatasetRequest(BaseValidatorModel):
    ProjectName: str
    DatasetType: str
    DatasetSource: Optional[DatasetSource] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'describe_model' function.
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

ModelPackagingConfigurationUnion = Union[ModelPackagingConfiguration, ModelPackagingConfigurationOutput]


# This class is the output for the 'describe_model_packaging_job' function.
class DescribeModelPackagingJobResponse(BaseValidatorModel):
    ModelPackagingDescription: ModelPackagingDescription
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_model_packaging_job' function.
class StartModelPackagingJobRequest(BaseValidatorModel):
    ProjectName: str
    ModelVersion: str
    Configuration: ModelPackagingConfigurationUnion
    JobName: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None