from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CategoricalValues(BaseValidatorModel):
    Status: StatisticalIssueStatusType
    NumberOfCategory: Optional[int] = None


class CountPercent(BaseValidatorModel):
    Count: int
    Percentage: float


class DatasetSchema(BaseValidatorModel):
    InlineDataSchema: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Timestamp = Union[datetime, str]


class DataPreProcessingConfiguration(BaseValidatorModel):
    TargetSamplingRate: Optional[TargetSamplingRateType] = None


class DuplicateTimestamps(BaseValidatorModel):
    TotalNumberOfDuplicateTimestamps: int


class InvalidSensorData(BaseValidatorModel):
    AffectedSensorCount: int
    TotalNumberOfInvalidValues: int


class MissingSensorData(BaseValidatorModel):
    AffectedSensorCount: int
    TotalNumberOfMissingValues: int


class UnsupportedTimestamps(BaseValidatorModel):
    TotalNumberOfUnsupportedTimestamps: int


class DatasetSummary(BaseValidatorModel):
    DatasetName: Optional[str] = None
    DatasetArn: Optional[str] = None
    Status: Optional[DatasetStatusType] = None
    CreatedAt: Optional[datetime] = None


# This class is the input for the 'delete_dataset' function.
class DeleteDatasetRequest(BaseValidatorModel):
    DatasetName: str


# This class is the input for the 'delete_inference_scheduler' function.
class DeleteInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str


# This class is the input for the 'delete_label_group' function.
class DeleteLabelGroupRequest(BaseValidatorModel):
    LabelGroupName: str


# This class is the input for the 'delete_label' function.
class DeleteLabelRequest(BaseValidatorModel):
    LabelGroupName: str
    LabelId: str


# This class is the input for the 'delete_model' function.
class DeleteModelRequest(BaseValidatorModel):
    ModelName: str


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'delete_retraining_scheduler' function.
class DeleteRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str


# This class is the input for the 'describe_data_ingestion_job' function.
class DescribeDataIngestionJobRequest(BaseValidatorModel):
    JobId: str


# This class is the input for the 'describe_dataset' function.
class DescribeDatasetRequest(BaseValidatorModel):
    DatasetName: str


# This class is the input for the 'describe_inference_scheduler' function.
class DescribeInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str


# This class is the input for the 'describe_label_group' function.
class DescribeLabelGroupRequest(BaseValidatorModel):
    LabelGroupName: str


# This class is the input for the 'describe_label' function.
class DescribeLabelRequest(BaseValidatorModel):
    LabelGroupName: str
    LabelId: str


# This class is the input for the 'describe_model' function.
class DescribeModelRequest(BaseValidatorModel):
    ModelName: str


# This class is the input for the 'describe_model_version' function.
class DescribeModelVersionRequest(BaseValidatorModel):
    ModelName: str
    ModelVersion: int


class S3Object(BaseValidatorModel):
    Bucket: str
    Key: str


# This class is the input for the 'describe_resource_policy' function.
class DescribeResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'describe_retraining_scheduler' function.
class DescribeRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str


class InferenceEventSummary(BaseValidatorModel):
    InferenceSchedulerArn: Optional[str] = None
    InferenceSchedulerName: Optional[str] = None
    EventStartTime: Optional[datetime] = None
    EventEndTime: Optional[datetime] = None
    Diagnostics: Optional[str] = None
    EventDurationInSeconds: Optional[int] = None


class InferenceInputNameConfiguration(BaseValidatorModel):
    TimestampFormat: Optional[str] = None
    ComponentTimestampDelimiter: Optional[str] = None


class InferenceS3InputConfiguration(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class InferenceS3OutputConfiguration(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class InferenceSchedulerSummary(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    InferenceSchedulerName: Optional[str] = None
    InferenceSchedulerArn: Optional[str] = None
    Status: Optional[InferenceSchedulerStatusType] = None
    DataDelayOffsetInMinutes: Optional[int] = None
    DataUploadFrequency: Optional[DataUploadFrequencyType] = None
    LatestInferenceResult: Optional[LatestInferenceResultType] = None


class IngestionS3InputConfiguration(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None
    KeyPattern: Optional[str] = None


class MissingCompleteSensorData(BaseValidatorModel):
    AffectedSensorCount: int


class SensorsWithShortDateRange(BaseValidatorModel):
    AffectedSensorCount: int


class LabelGroupSummary(BaseValidatorModel):
    LabelGroupName: Optional[str] = None
    LabelGroupArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class LabelSummary(BaseValidatorModel):
    LabelGroupName: Optional[str] = None
    LabelId: Optional[str] = None
    LabelGroupArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Rating: Optional[LabelRatingType] = None
    FaultCode: Optional[str] = None
    Equipment: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class LabelsS3InputConfiguration(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class LargeTimestampGaps(BaseValidatorModel):
    Status: StatisticalIssueStatusType
    NumberOfLargeTimestampGaps: Optional[int] = None
    MaxTimestampGapInDays: Optional[int] = None


# This class is the input for the 'list_data_ingestion_jobs' function.
class ListDataIngestionJobsRequest(BaseValidatorModel):
    DatasetName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[IngestionJobStatusType] = None


# This class is the input for the 'list_datasets' function.
class ListDatasetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DatasetNameBeginsWith: Optional[str] = None


# This class is the input for the 'list_inference_schedulers' function.
class ListInferenceSchedulersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InferenceSchedulerNameBeginsWith: Optional[str] = None
    ModelName: Optional[str] = None
    Status: Optional[InferenceSchedulerStatusType] = None


# This class is the input for the 'list_label_groups' function.
class ListLabelGroupsRequest(BaseValidatorModel):
    LabelGroupNameBeginsWith: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ModelVersionSummary(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    ModelVersion: Optional[int] = None
    ModelVersionArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Status: Optional[ModelVersionStatusType] = None
    SourceType: Optional[ModelVersionSourceTypeType] = None
    ModelQuality: Optional[ModelQualityType] = None


# This class is the input for the 'list_models' function.
class ListModelsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ModelStatusType] = None
    ModelNameBeginsWith: Optional[str] = None
    DatasetNameBeginsWith: Optional[str] = None


# This class is the input for the 'list_retraining_schedulers' function.
class ListRetrainingSchedulersRequest(BaseValidatorModel):
    ModelNameBeginsWith: Optional[str] = None
    Status: Optional[RetrainingSchedulerStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RetrainingSchedulerSummary(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    Status: Optional[RetrainingSchedulerStatusType] = None
    RetrainingStartDate: Optional[datetime] = None
    RetrainingFrequency: Optional[str] = None
    LookbackWindow: Optional[str] = None


# This class is the input for the 'list_sensor_statistics' function.
class ListSensorStatisticsRequest(BaseValidatorModel):
    DatasetName: str
    IngestionJobId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ModelDiagnosticsS3OutputConfiguration(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class MonotonicValues(BaseValidatorModel):
    Status: StatisticalIssueStatusType
    Monotonicity: Optional[MonotonicityType] = None


class MultipleOperatingModes(BaseValidatorModel):
    Status: StatisticalIssueStatusType


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    ClientToken: str
    PolicyRevisionId: Optional[str] = None


# This class is the input for the 'start_inference_scheduler' function.
class StartInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str


# This class is the input for the 'start_retraining_scheduler' function.
class StartRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str


# This class is the input for the 'stop_inference_scheduler' function.
class StopInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str


# This class is the input for the 'stop_retraining_scheduler' function.
class StopRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_active_model_version' function.
class UpdateActiveModelVersionRequest(BaseValidatorModel):
    ModelName: str
    ModelVersion: int


# This class is the input for the 'update_label_group' function.
class UpdateLabelGroupRequest(BaseValidatorModel):
    LabelGroupName: str
    FaultCodes: Optional[List[str]] = None


# This class is the input for the 'create_dataset' function.
class CreateDatasetRequest(BaseValidatorModel):
    DatasetName: str
    ClientToken: str
    DatasetSchema: Optional[DatasetSchema] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_label_group' function.
class CreateLabelGroupRequest(BaseValidatorModel):
    LabelGroupName: str
    ClientToken: str
    FaultCodes: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'import_dataset' function.
class ImportDatasetRequest(BaseValidatorModel):
    SourceDatasetArn: str
    ClientToken: str
    DatasetName: Optional[str] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the output for the 'create_dataset' function.
class CreateDatasetResponse(BaseValidatorModel):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_inference_scheduler' function.
class CreateInferenceSchedulerResponse(BaseValidatorModel):
    InferenceSchedulerArn: str
    InferenceSchedulerName: str
    Status: InferenceSchedulerStatusType
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_label_group' function.
class CreateLabelGroupResponse(BaseValidatorModel):
    LabelGroupName: str
    LabelGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_label' function.
class CreateLabelResponse(BaseValidatorModel):
    LabelId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model' function.
class CreateModelResponse(BaseValidatorModel):
    ModelArn: str
    Status: ModelStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_retraining_scheduler' function.
class CreateRetrainingSchedulerResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_label_group' function.
class DescribeLabelGroupResponse(BaseValidatorModel):
    LabelGroupName: str
    LabelGroupArn: str
    FaultCodes: List[str]
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_label' function.
class DescribeLabelResponse(BaseValidatorModel):
    LabelGroupName: str
    LabelGroupArn: str
    LabelId: str
    StartTime: datetime
    EndTime: datetime
    Rating: LabelRatingType
    FaultCode: str
    Notes: str
    Equipment: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resource_policy' function.
class DescribeResourcePolicyResponse(BaseValidatorModel):
    PolicyRevisionId: str
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_retraining_scheduler' function.
class DescribeRetrainingSchedulerResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    RetrainingStartDate: datetime
    RetrainingFrequency: str
    LookbackWindow: str
    Status: RetrainingSchedulerStatusType
    PromoteMode: ModelPromoteModeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_retraining_scheduler' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_dataset' function.
class ImportDatasetResponse(BaseValidatorModel):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    JobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_model_version' function.
class ImportModelVersionResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    ModelVersionArn: str
    ModelVersion: int
    Status: ModelVersionStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_data_ingestion_job' function.
class StartDataIngestionJobResponse(BaseValidatorModel):
    JobId: str
    Status: IngestionJobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_inference_scheduler' function.
class StartInferenceSchedulerResponse(BaseValidatorModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_retraining_scheduler' function.
class StartRetrainingSchedulerResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_inference_scheduler' function.
class StopInferenceSchedulerResponse(BaseValidatorModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_retraining_scheduler' function.
class StopRetrainingSchedulerResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_active_model_version' function.
class UpdateActiveModelVersionResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    CurrentActiveVersion: int
    PreviousActiveVersion: int
    CurrentActiveVersionArn: str
    PreviousActiveVersionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_label' function.
class CreateLabelRequest(BaseValidatorModel):
    LabelGroupName: str
    StartTime: Timestamp
    EndTime: Timestamp
    Rating: LabelRatingType
    ClientToken: str
    FaultCode: Optional[str] = None
    Notes: Optional[str] = None
    Equipment: Optional[str] = None


# This class is the input for the 'create_retraining_scheduler' function.
class CreateRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str
    RetrainingFrequency: str
    LookbackWindow: str
    ClientToken: str
    RetrainingStartDate: Optional[Timestamp] = None
    PromoteMode: Optional[ModelPromoteModeType] = None


# This class is the input for the 'list_inference_events' function.
class ListInferenceEventsRequest(BaseValidatorModel):
    InferenceSchedulerName: str
    IntervalStartTime: Timestamp
    IntervalEndTime: Timestamp
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_inference_executions' function.
class ListInferenceExecutionsRequest(BaseValidatorModel):
    InferenceSchedulerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DataStartTimeAfter: Optional[Timestamp] = None
    DataEndTimeBefore: Optional[Timestamp] = None
    Status: Optional[InferenceExecutionStatusType] = None


# This class is the input for the 'list_labels' function.
class ListLabelsRequest(BaseValidatorModel):
    LabelGroupName: str
    IntervalStartTime: Optional[Timestamp] = None
    IntervalEndTime: Optional[Timestamp] = None
    FaultCode: Optional[str] = None
    Equipment: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_model_versions' function.
class ListModelVersionsRequest(BaseValidatorModel):
    ModelName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ModelVersionStatusType] = None
    SourceType: Optional[ModelVersionSourceTypeType] = None
    CreatedAtEndTime: Optional[Timestamp] = None
    CreatedAtStartTime: Optional[Timestamp] = None
    MaxModelVersion: Optional[int] = None
    MinModelVersion: Optional[int] = None


# This class is the input for the 'update_retraining_scheduler' function.
class UpdateRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str
    RetrainingStartDate: Optional[Timestamp] = None
    RetrainingFrequency: Optional[str] = None
    LookbackWindow: Optional[str] = None
    PromoteMode: Optional[ModelPromoteModeType] = None


# This class is the output for the 'list_datasets' function.
class ListDatasetsResponse(BaseValidatorModel):
    DatasetSummaries: List[DatasetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IngestedFilesSummary(BaseValidatorModel):
    TotalNumberOfFiles: int
    IngestedNumberOfFiles: int
    DiscardedFiles: Optional[List[S3Object]] = None


# This class is the output for the 'list_inference_events' function.
class ListInferenceEventsResponse(BaseValidatorModel):
    InferenceEventSummaries: List[InferenceEventSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InferenceInputConfiguration(BaseValidatorModel):
    S3InputConfiguration: Optional[InferenceS3InputConfiguration] = None
    InputTimeZoneOffset: Optional[str] = None
    InferenceInputNameConfiguration: Optional[InferenceInputNameConfiguration] = None


class InferenceOutputConfiguration(BaseValidatorModel):
    S3OutputConfiguration: InferenceS3OutputConfiguration
    KmsKeyId: Optional[str] = None


# This class is the output for the 'list_inference_schedulers' function.
class ListInferenceSchedulersResponse(BaseValidatorModel):
    InferenceSchedulerSummaries: List[InferenceSchedulerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IngestionInputConfiguration(BaseValidatorModel):
    S3InputConfiguration: IngestionS3InputConfiguration


class InsufficientSensorData(BaseValidatorModel):
    MissingCompleteSensorData: MissingCompleteSensorData
    SensorsWithShortDateRange: SensorsWithShortDateRange


# This class is the output for the 'list_label_groups' function.
class ListLabelGroupsResponse(BaseValidatorModel):
    LabelGroupSummaries: List[LabelGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_labels' function.
class ListLabelsResponse(BaseValidatorModel):
    LabelSummaries: List[LabelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LabelsInputConfiguration(BaseValidatorModel):
    S3InputConfiguration: Optional[LabelsS3InputConfiguration] = None
    LabelGroupName: Optional[str] = None


# This class is the output for the 'list_model_versions' function.
class ListModelVersionsResponse(BaseValidatorModel):
    ModelVersionSummaries: List[ModelVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_retraining_schedulers' function.
class ListRetrainingSchedulersResponse(BaseValidatorModel):
    RetrainingSchedulerSummaries: List[RetrainingSchedulerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModelDiagnosticsOutputConfiguration(BaseValidatorModel):
    S3OutputConfiguration: ModelDiagnosticsS3OutputConfiguration
    KmsKeyId: Optional[str] = None


class SensorStatisticsSummary(BaseValidatorModel):
    ComponentName: Optional[str] = None
    SensorName: Optional[str] = None
    DataExists: Optional[bool] = None
    MissingValues: Optional[CountPercent] = None
    InvalidValues: Optional[CountPercent] = None
    InvalidDateEntries: Optional[CountPercent] = None
    DuplicateTimestamps: Optional[CountPercent] = None
    CategoricalValues: Optional[CategoricalValues] = None
    MultipleOperatingModes: Optional[MultipleOperatingModes] = None
    LargeTimestampGaps: Optional[LargeTimestampGaps] = None
    MonotonicValues: Optional[MonotonicValues] = None
    DataStartTime: Optional[datetime] = None
    DataEndTime: Optional[datetime] = None


# This class is the input for the 'create_inference_scheduler' function.
class CreateInferenceSchedulerRequest(BaseValidatorModel):
    ModelName: str
    InferenceSchedulerName: str
    DataUploadFrequency: DataUploadFrequencyType
    DataInputConfiguration: InferenceInputConfiguration
    DataOutputConfiguration: InferenceOutputConfiguration
    RoleArn: str
    ClientToken: str
    DataDelayOffsetInMinutes: Optional[int] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_inference_scheduler' function.
class DescribeInferenceSchedulerResponse(BaseValidatorModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    DataDelayOffsetInMinutes: int
    DataUploadFrequency: DataUploadFrequencyType
    CreatedAt: datetime
    UpdatedAt: datetime
    DataInputConfiguration: InferenceInputConfiguration
    DataOutputConfiguration: InferenceOutputConfiguration
    RoleArn: str
    ServerSideKmsKeyId: str
    LatestInferenceResult: LatestInferenceResultType
    ResponseMetadata: ResponseMetadata


class InferenceExecutionSummary(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    InferenceSchedulerName: Optional[str] = None
    InferenceSchedulerArn: Optional[str] = None
    ScheduledStartTime: Optional[datetime] = None
    DataStartTime: Optional[datetime] = None
    DataEndTime: Optional[datetime] = None
    DataInputConfiguration: Optional[InferenceInputConfiguration] = None
    DataOutputConfiguration: Optional[InferenceOutputConfiguration] = None
    CustomerResultObject: Optional[S3Object] = None
    Status: Optional[InferenceExecutionStatusType] = None
    FailedReason: Optional[str] = None
    ModelVersion: Optional[int] = None
    ModelVersionArn: Optional[str] = None


# This class is the input for the 'update_inference_scheduler' function.
class UpdateInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str
    DataDelayOffsetInMinutes: Optional[int] = None
    DataUploadFrequency: Optional[DataUploadFrequencyType] = None
    DataInputConfiguration: Optional[InferenceInputConfiguration] = None
    DataOutputConfiguration: Optional[InferenceOutputConfiguration] = None
    RoleArn: Optional[str] = None


class DataIngestionJobSummary(BaseValidatorModel):
    JobId: Optional[str] = None
    DatasetName: Optional[str] = None
    DatasetArn: Optional[str] = None
    IngestionInputConfiguration: Optional[IngestionInputConfiguration] = None
    Status: Optional[IngestionJobStatusType] = None


# This class is the input for the 'start_data_ingestion_job' function.
class StartDataIngestionJobRequest(BaseValidatorModel):
    DatasetName: str
    IngestionInputConfiguration: IngestionInputConfiguration
    RoleArn: str
    ClientToken: str


class DataQualitySummary(BaseValidatorModel):
    InsufficientSensorData: InsufficientSensorData
    MissingSensorData: MissingSensorData
    InvalidSensorData: InvalidSensorData
    UnsupportedTimestamps: UnsupportedTimestamps
    DuplicateTimestamps: DuplicateTimestamps


# This class is the input for the 'import_model_version' function.
class ImportModelVersionRequest(BaseValidatorModel):
    SourceModelVersionArn: str
    DatasetName: str
    ClientToken: str
    ModelName: Optional[str] = None
    LabelsInputConfiguration: Optional[LabelsInputConfiguration] = None
    RoleArn: Optional[str] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    InferenceDataImportStrategy: Optional[InferenceDataImportStrategyType] = None


# This class is the input for the 'create_model' function.
class CreateModelRequest(BaseValidatorModel):
    ModelName: str
    DatasetName: str
    ClientToken: str
    DatasetSchema: Optional[DatasetSchema] = None
    LabelsInputConfiguration: Optional[LabelsInputConfiguration] = None
    TrainingDataStartTime: Optional[Timestamp] = None
    TrainingDataEndTime: Optional[Timestamp] = None
    EvaluationDataStartTime: Optional[Timestamp] = None
    EvaluationDataEndTime: Optional[Timestamp] = None
    RoleArn: Optional[str] = None
    DataPreProcessingConfiguration: Optional[DataPreProcessingConfiguration] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    OffCondition: Optional[str] = None
    ModelDiagnosticsOutputConfiguration: Optional[ModelDiagnosticsOutputConfiguration] = None


# This class is the output for the 'describe_model' function.
class DescribeModelResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    DatasetName: str
    DatasetArn: str
    Schema: str
    LabelsInputConfiguration: LabelsInputConfiguration
    TrainingDataStartTime: datetime
    TrainingDataEndTime: datetime
    EvaluationDataStartTime: datetime
    EvaluationDataEndTime: datetime
    RoleArn: str
    DataPreProcessingConfiguration: DataPreProcessingConfiguration
    Status: ModelStatusType
    TrainingExecutionStartTime: datetime
    TrainingExecutionEndTime: datetime
    FailedReason: str
    ModelMetrics: str
    LastUpdatedTime: datetime
    CreatedAt: datetime
    ServerSideKmsKeyId: str
    OffCondition: str
    SourceModelVersionArn: str
    ImportJobStartTime: datetime
    ImportJobEndTime: datetime
    ActiveModelVersion: int
    ActiveModelVersionArn: str
    ModelVersionActivatedAt: datetime
    PreviousActiveModelVersion: int
    PreviousActiveModelVersionArn: str
    PreviousModelVersionActivatedAt: datetime
    PriorModelMetrics: str
    LatestScheduledRetrainingFailedReason: str
    LatestScheduledRetrainingStatus: ModelVersionStatusType
    LatestScheduledRetrainingModelVersion: int
    LatestScheduledRetrainingStartTime: datetime
    LatestScheduledRetrainingAvailableDataInDays: int
    NextScheduledRetrainingStartDate: datetime
    AccumulatedInferenceDataStartTime: datetime
    AccumulatedInferenceDataEndTime: datetime
    RetrainingSchedulerStatus: RetrainingSchedulerStatusType
    ModelDiagnosticsOutputConfiguration: ModelDiagnosticsOutputConfiguration
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_model_version' function.
class DescribeModelVersionResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    ModelVersion: int
    ModelVersionArn: str
    Status: ModelVersionStatusType
    SourceType: ModelVersionSourceTypeType
    DatasetName: str
    DatasetArn: str
    Schema: str
    LabelsInputConfiguration: LabelsInputConfiguration
    TrainingDataStartTime: datetime
    TrainingDataEndTime: datetime
    EvaluationDataStartTime: datetime
    EvaluationDataEndTime: datetime
    RoleArn: str
    DataPreProcessingConfiguration: DataPreProcessingConfiguration
    TrainingExecutionStartTime: datetime
    TrainingExecutionEndTime: datetime
    FailedReason: str
    ModelMetrics: str
    LastUpdatedTime: datetime
    CreatedAt: datetime
    ServerSideKmsKeyId: str
    OffCondition: str
    SourceModelVersionArn: str
    ImportJobStartTime: datetime
    ImportJobEndTime: datetime
    ImportedDataSizeInBytes: int
    PriorModelMetrics: str
    RetrainingAvailableDataInDays: int
    AutoPromotionResult: AutoPromotionResultType
    AutoPromotionResultReason: str
    ModelDiagnosticsOutputConfiguration: ModelDiagnosticsOutputConfiguration
    ModelDiagnosticsResultsObject: S3Object
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadata


class ModelSummary(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    DatasetName: Optional[str] = None
    DatasetArn: Optional[str] = None
    Status: Optional[ModelStatusType] = None
    CreatedAt: Optional[datetime] = None
    ActiveModelVersion: Optional[int] = None
    ActiveModelVersionArn: Optional[str] = None
    LatestScheduledRetrainingStatus: Optional[ModelVersionStatusType] = None
    LatestScheduledRetrainingModelVersion: Optional[int] = None
    LatestScheduledRetrainingStartTime: Optional[datetime] = None
    NextScheduledRetrainingStartDate: Optional[datetime] = None
    RetrainingSchedulerStatus: Optional[RetrainingSchedulerStatusType] = None
    ModelDiagnosticsOutputConfiguration: Optional[ModelDiagnosticsOutputConfiguration] = None
    ModelQuality: Optional[ModelQualityType] = None


# This class is the input for the 'update_model' function.
class UpdateModelRequest(BaseValidatorModel):
    ModelName: str
    LabelsInputConfiguration: Optional[LabelsInputConfiguration] = None
    RoleArn: Optional[str] = None
    ModelDiagnosticsOutputConfiguration: Optional[ModelDiagnosticsOutputConfiguration] = None


# This class is the output for the 'list_sensor_statistics' function.
class ListSensorStatisticsResponse(BaseValidatorModel):
    SensorStatisticsSummaries: List[SensorStatisticsSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_inference_executions' function.
class ListInferenceExecutionsResponse(BaseValidatorModel):
    InferenceExecutionSummaries: List[InferenceExecutionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_data_ingestion_jobs' function.
class ListDataIngestionJobsResponse(BaseValidatorModel):
    DataIngestionJobSummaries: List[DataIngestionJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_data_ingestion_job' function.
class DescribeDataIngestionJobResponse(BaseValidatorModel):
    JobId: str
    DatasetArn: str
    IngestionInputConfiguration: IngestionInputConfiguration
    RoleArn: str
    CreatedAt: datetime
    Status: IngestionJobStatusType
    FailedReason: str
    DataQualitySummary: DataQualitySummary
    IngestedFilesSummary: IngestedFilesSummary
    StatusDetail: str
    IngestedDataSize: int
    DataStartTime: datetime
    DataEndTime: datetime
    SourceDatasetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_dataset' function.
class DescribeDatasetResponse(BaseValidatorModel):
    DatasetName: str
    DatasetArn: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Status: DatasetStatusType
    Schema: str
    ServerSideKmsKeyId: str
    IngestionInputConfiguration: IngestionInputConfiguration
    DataQualitySummary: DataQualitySummary
    IngestedFilesSummary: IngestedFilesSummary
    RoleArn: str
    DataStartTime: datetime
    DataEndTime: datetime
    SourceDatasetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_models' function.
class ListModelsResponse(BaseValidatorModel):
    ModelSummaries: List[ModelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None