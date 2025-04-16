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
from aws_resource_validator.pydantic_models.lookoutequipment_constants import *

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


class DeleteDatasetRequest(BaseValidatorModel):
    DatasetName: str


class DeleteInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str


class DeleteLabelGroupRequest(BaseValidatorModel):
    LabelGroupName: str


class DeleteLabelRequest(BaseValidatorModel):
    LabelGroupName: str
    LabelId: str


class DeleteModelRequest(BaseValidatorModel):
    ModelName: str


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DeleteRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str


class DescribeDataIngestionJobRequest(BaseValidatorModel):
    JobId: str


class DescribeDatasetRequest(BaseValidatorModel):
    DatasetName: str


class DescribeInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str


class DescribeLabelGroupRequest(BaseValidatorModel):
    LabelGroupName: str


class DescribeLabelRequest(BaseValidatorModel):
    LabelGroupName: str
    LabelId: str


class DescribeModelRequest(BaseValidatorModel):
    ModelName: str


class DescribeModelVersionRequest(BaseValidatorModel):
    ModelName: str
    ModelVersion: int


class S3Object(BaseValidatorModel):
    Bucket: str
    Key: str


class DescribeResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


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


class ListDataIngestionJobsRequest(BaseValidatorModel):
    DatasetName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[IngestionJobStatusType] = None


class ListDatasetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DatasetNameBeginsWith: Optional[str] = None


class ListInferenceSchedulersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InferenceSchedulerNameBeginsWith: Optional[str] = None
    ModelName: Optional[str] = None
    Status: Optional[InferenceSchedulerStatusType] = None


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


class ListModelsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ModelStatusType] = None
    ModelNameBeginsWith: Optional[str] = None
    DatasetNameBeginsWith: Optional[str] = None


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


class ListSensorStatisticsRequest(BaseValidatorModel):
    DatasetName: str
    IngestionJobId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


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


class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    ClientToken: str
    PolicyRevisionId: Optional[str] = None


class StartInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str


class StartRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str


class StopInferenceSchedulerRequest(BaseValidatorModel):
    InferenceSchedulerName: str


class StopRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateActiveModelVersionRequest(BaseValidatorModel):
    ModelName: str
    ModelVersion: int


class UpdateLabelGroupRequest(BaseValidatorModel):
    LabelGroupName: str
    FaultCodes: Optional[Sequence[str]] = None


class CreateDatasetRequest(BaseValidatorModel):
    DatasetName: str
    ClientToken: str
    DatasetSchema: Optional[DatasetSchema] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateLabelGroupRequest(BaseValidatorModel):
    LabelGroupName: str
    ClientToken: str
    FaultCodes: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None


class ImportDatasetRequest(BaseValidatorModel):
    SourceDatasetArn: str
    ClientToken: str
    DatasetName: Optional[str] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class CreateDatasetResponse(BaseValidatorModel):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadata


class CreateInferenceSchedulerResponse(BaseValidatorModel):
    InferenceSchedulerArn: str
    InferenceSchedulerName: str
    Status: InferenceSchedulerStatusType
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadata


class CreateLabelGroupResponse(BaseValidatorModel):
    LabelGroupName: str
    LabelGroupArn: str
    ResponseMetadata: ResponseMetadata


class CreateLabelResponse(BaseValidatorModel):
    LabelId: str
    ResponseMetadata: ResponseMetadata


class CreateModelResponse(BaseValidatorModel):
    ModelArn: str
    Status: ModelStatusType
    ResponseMetadata: ResponseMetadata


class CreateRetrainingSchedulerResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadata


class DescribeLabelGroupResponse(BaseValidatorModel):
    LabelGroupName: str
    LabelGroupArn: str
    FaultCodes: List[str]
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


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


class DescribeResourcePolicyResponse(BaseValidatorModel):
    PolicyRevisionId: str
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


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


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ImportDatasetResponse(BaseValidatorModel):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    JobId: str
    ResponseMetadata: ResponseMetadata


class ImportModelVersionResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    ModelVersionArn: str
    ModelVersion: int
    Status: ModelVersionStatusType
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadata


class StartDataIngestionJobResponse(BaseValidatorModel):
    JobId: str
    Status: IngestionJobStatusType
    ResponseMetadata: ResponseMetadata


class StartInferenceSchedulerResponse(BaseValidatorModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadata


class StartRetrainingSchedulerResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadata


class StopInferenceSchedulerResponse(BaseValidatorModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadata


class StopRetrainingSchedulerResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadata


class UpdateActiveModelVersionResponse(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    CurrentActiveVersion: int
    PreviousActiveVersion: int
    CurrentActiveVersionArn: str
    PreviousActiveVersionArn: str
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class CreateLabelRequest(BaseValidatorModel):
    LabelGroupName: str
    StartTime: Timestamp
    EndTime: Timestamp
    Rating: LabelRatingType
    ClientToken: str
    FaultCode: Optional[str] = None
    Notes: Optional[str] = None
    Equipment: Optional[str] = None


class CreateRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str
    RetrainingFrequency: str
    LookbackWindow: str
    ClientToken: str
    RetrainingStartDate: Optional[Timestamp] = None
    PromoteMode: Optional[ModelPromoteModeType] = None


class ListInferenceEventsRequest(BaseValidatorModel):
    InferenceSchedulerName: str
    IntervalStartTime: Timestamp
    IntervalEndTime: Timestamp
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInferenceExecutionsRequest(BaseValidatorModel):
    InferenceSchedulerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DataStartTimeAfter: Optional[Timestamp] = None
    DataEndTimeBefore: Optional[Timestamp] = None
    Status: Optional[InferenceExecutionStatusType] = None


class ListLabelsRequest(BaseValidatorModel):
    LabelGroupName: str
    IntervalStartTime: Optional[Timestamp] = None
    IntervalEndTime: Optional[Timestamp] = None
    FaultCode: Optional[str] = None
    Equipment: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


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


class UpdateRetrainingSchedulerRequest(BaseValidatorModel):
    ModelName: str
    RetrainingStartDate: Optional[Timestamp] = None
    RetrainingFrequency: Optional[str] = None
    LookbackWindow: Optional[str] = None
    PromoteMode: Optional[ModelPromoteModeType] = None


class ListDatasetsResponse(BaseValidatorModel):
    DatasetSummaries: List[DatasetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IngestedFilesSummary(BaseValidatorModel):
    TotalNumberOfFiles: int
    IngestedNumberOfFiles: int
    DiscardedFiles: Optional[List[S3Object]] = None


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


class ListInferenceSchedulersResponse(BaseValidatorModel):
    InferenceSchedulerSummaries: List[InferenceSchedulerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IngestionInputConfiguration(BaseValidatorModel):
    S3InputConfiguration: IngestionS3InputConfiguration


class InsufficientSensorData(BaseValidatorModel):
    MissingCompleteSensorData: MissingCompleteSensorData
    SensorsWithShortDateRange: SensorsWithShortDateRange


class ListLabelGroupsResponse(BaseValidatorModel):
    LabelGroupSummaries: List[LabelGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLabelsResponse(BaseValidatorModel):
    LabelSummaries: List[LabelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LabelsInputConfiguration(BaseValidatorModel):
    S3InputConfiguration: Optional[LabelsS3InputConfiguration] = None
    LabelGroupName: Optional[str] = None


class ListModelVersionsResponse(BaseValidatorModel):
    ModelVersionSummaries: List[ModelVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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
    Tags: Optional[Sequence[Tag]] = None


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


class ImportModelVersionRequest(BaseValidatorModel):
    SourceModelVersionArn: str
    DatasetName: str
    ClientToken: str
    ModelName: Optional[str] = None
    LabelsInputConfiguration: Optional[LabelsInputConfiguration] = None
    RoleArn: Optional[str] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    InferenceDataImportStrategy: Optional[InferenceDataImportStrategyType] = None


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
    Tags: Optional[Sequence[Tag]] = None
    OffCondition: Optional[str] = None
    ModelDiagnosticsOutputConfiguration: Optional[ModelDiagnosticsOutputConfiguration] = None


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


class UpdateModelRequest(BaseValidatorModel):
    ModelName: str
    LabelsInputConfiguration: Optional[LabelsInputConfiguration] = None
    RoleArn: Optional[str] = None
    ModelDiagnosticsOutputConfiguration: Optional[ModelDiagnosticsOutputConfiguration] = None


class ListSensorStatisticsResponse(BaseValidatorModel):
    SensorStatisticsSummaries: List[SensorStatisticsSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListInferenceExecutionsResponse(BaseValidatorModel):
    InferenceExecutionSummaries: List[InferenceExecutionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDataIngestionJobsResponse(BaseValidatorModel):
    DataIngestionJobSummaries: List[DataIngestionJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class ListModelsResponse(BaseValidatorModel):
    ModelSummaries: List[ModelSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


