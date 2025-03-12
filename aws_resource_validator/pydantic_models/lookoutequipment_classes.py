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

class CategoricalValuesTypeDef(BaseValidatorModel):
    Status: StatisticalIssueStatusType
    NumberOfCategory: Optional[int] = None


class CountPercentTypeDef(BaseValidatorModel):
    Count: int
    Percentage: float


class DatasetSchemaTypeDef(BaseValidatorModel):
    InlineDataSchema: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DataPreProcessingConfigurationTypeDef(BaseValidatorModel):
    TargetSamplingRate: Optional[TargetSamplingRateType] = None


class DuplicateTimestampsTypeDef(BaseValidatorModel):
    TotalNumberOfDuplicateTimestamps: int


class InvalidSensorDataTypeDef(BaseValidatorModel):
    AffectedSensorCount: int
    TotalNumberOfInvalidValues: int


class MissingSensorDataTypeDef(BaseValidatorModel):
    AffectedSensorCount: int
    TotalNumberOfMissingValues: int


class UnsupportedTimestampsTypeDef(BaseValidatorModel):
    TotalNumberOfUnsupportedTimestamps: int


class DatasetSummaryTypeDef(BaseValidatorModel):
    DatasetName: Optional[str] = None
    DatasetArn: Optional[str] = None
    Status: Optional[DatasetStatusType] = None
    CreatedAt: Optional[datetime] = None


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    DatasetName: str


class DeleteInferenceSchedulerRequestTypeDef(BaseValidatorModel):
    InferenceSchedulerName: str


class DeleteLabelGroupRequestTypeDef(BaseValidatorModel):
    LabelGroupName: str


class DeleteLabelRequestTypeDef(BaseValidatorModel):
    LabelGroupName: str
    LabelId: str


class DeleteModelRequestTypeDef(BaseValidatorModel):
    ModelName: str


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DeleteRetrainingSchedulerRequestTypeDef(BaseValidatorModel):
    ModelName: str


class DescribeDataIngestionJobRequestTypeDef(BaseValidatorModel):
    JobId: str


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    DatasetName: str


class DescribeInferenceSchedulerRequestTypeDef(BaseValidatorModel):
    InferenceSchedulerName: str


class DescribeLabelGroupRequestTypeDef(BaseValidatorModel):
    LabelGroupName: str


class DescribeLabelRequestTypeDef(BaseValidatorModel):
    LabelGroupName: str
    LabelId: str


class DescribeModelRequestTypeDef(BaseValidatorModel):
    ModelName: str


class DescribeModelVersionRequestTypeDef(BaseValidatorModel):
    ModelName: str
    ModelVersion: int


class S3ObjectTypeDef(BaseValidatorModel):
    Bucket: str
    Key: str


class DescribeResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DescribeRetrainingSchedulerRequestTypeDef(BaseValidatorModel):
    ModelName: str


class InferenceEventSummaryTypeDef(BaseValidatorModel):
    InferenceSchedulerArn: Optional[str] = None
    InferenceSchedulerName: Optional[str] = None
    EventStartTime: Optional[datetime] = None
    EventEndTime: Optional[datetime] = None
    Diagnostics: Optional[str] = None
    EventDurationInSeconds: Optional[int] = None


class InferenceInputNameConfigurationTypeDef(BaseValidatorModel):
    TimestampFormat: Optional[str] = None
    ComponentTimestampDelimiter: Optional[str] = None


class InferenceS3InputConfigurationTypeDef(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class InferenceS3OutputConfigurationTypeDef(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class InferenceSchedulerSummaryTypeDef(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    InferenceSchedulerName: Optional[str] = None
    InferenceSchedulerArn: Optional[str] = None
    Status: Optional[InferenceSchedulerStatusType] = None
    DataDelayOffsetInMinutes: Optional[int] = None
    DataUploadFrequency: Optional[DataUploadFrequencyType] = None
    LatestInferenceResult: Optional[LatestInferenceResultType] = None


class IngestionS3InputConfigurationTypeDef(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None
    KeyPattern: Optional[str] = None


class MissingCompleteSensorDataTypeDef(BaseValidatorModel):
    AffectedSensorCount: int


class SensorsWithShortDateRangeTypeDef(BaseValidatorModel):
    AffectedSensorCount: int


class LabelGroupSummaryTypeDef(BaseValidatorModel):
    LabelGroupName: Optional[str] = None
    LabelGroupArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class LabelSummaryTypeDef(BaseValidatorModel):
    LabelGroupName: Optional[str] = None
    LabelId: Optional[str] = None
    LabelGroupArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Rating: Optional[LabelRatingType] = None
    FaultCode: Optional[str] = None
    Equipment: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class LabelsS3InputConfigurationTypeDef(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class LargeTimestampGapsTypeDef(BaseValidatorModel):
    Status: StatisticalIssueStatusType
    NumberOfLargeTimestampGaps: Optional[int] = None
    MaxTimestampGapInDays: Optional[int] = None


class ListDataIngestionJobsRequestTypeDef(BaseValidatorModel):
    DatasetName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[IngestionJobStatusType] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DatasetNameBeginsWith: Optional[str] = None


class ListInferenceSchedulersRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InferenceSchedulerNameBeginsWith: Optional[str] = None
    ModelName: Optional[str] = None
    Status: Optional[InferenceSchedulerStatusType] = None


class ListLabelGroupsRequestTypeDef(BaseValidatorModel):
    LabelGroupNameBeginsWith: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ModelVersionSummaryTypeDef(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    ModelVersion: Optional[int] = None
    ModelVersionArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Status: Optional[ModelVersionStatusType] = None
    SourceType: Optional[ModelVersionSourceTypeType] = None
    ModelQuality: Optional[ModelQualityType] = None


class ListModelsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ModelStatusType] = None
    ModelNameBeginsWith: Optional[str] = None
    DatasetNameBeginsWith: Optional[str] = None


class ListRetrainingSchedulersRequestTypeDef(BaseValidatorModel):
    ModelNameBeginsWith: Optional[str] = None
    Status: Optional[RetrainingSchedulerStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RetrainingSchedulerSummaryTypeDef(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    Status: Optional[RetrainingSchedulerStatusType] = None
    RetrainingStartDate: Optional[datetime] = None
    RetrainingFrequency: Optional[str] = None
    LookbackWindow: Optional[str] = None


class ListSensorStatisticsRequestTypeDef(BaseValidatorModel):
    DatasetName: str
    IngestionJobId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ModelDiagnosticsS3OutputConfigurationTypeDef(BaseValidatorModel):
    Bucket: str
    Prefix: Optional[str] = None


class MonotonicValuesTypeDef(BaseValidatorModel):
    Status: StatisticalIssueStatusType
    Monotonicity: Optional[MonotonicityType] = None


class MultipleOperatingModesTypeDef(BaseValidatorModel):
    Status: StatisticalIssueStatusType


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    ClientToken: str
    PolicyRevisionId: Optional[str] = None


class StartInferenceSchedulerRequestTypeDef(BaseValidatorModel):
    InferenceSchedulerName: str


class StartRetrainingSchedulerRequestTypeDef(BaseValidatorModel):
    ModelName: str


class StopInferenceSchedulerRequestTypeDef(BaseValidatorModel):
    InferenceSchedulerName: str


class StopRetrainingSchedulerRequestTypeDef(BaseValidatorModel):
    ModelName: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateActiveModelVersionRequestTypeDef(BaseValidatorModel):
    ModelName: str
    ModelVersion: int


class UpdateLabelGroupRequestTypeDef(BaseValidatorModel):
    LabelGroupName: str
    FaultCodes: Optional[Sequence[str]] = None


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    DatasetName: str
    ClientToken: str
    DatasetSchema: Optional[DatasetSchemaTypeDef] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateLabelGroupRequestTypeDef(BaseValidatorModel):
    LabelGroupName: str
    ClientToken: str
    FaultCodes: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ImportDatasetRequestTypeDef(BaseValidatorModel):
    SourceDatasetArn: str
    ClientToken: str
    DatasetName: Optional[str] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInferenceSchedulerResponseTypeDef(BaseValidatorModel):
    InferenceSchedulerArn: str
    InferenceSchedulerName: str
    Status: InferenceSchedulerStatusType
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLabelGroupResponseTypeDef(BaseValidatorModel):
    LabelGroupName: str
    LabelGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLabelResponseTypeDef(BaseValidatorModel):
    LabelId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateModelResponseTypeDef(BaseValidatorModel):
    ModelArn: str
    Status: ModelStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRetrainingSchedulerResponseTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLabelGroupResponseTypeDef(BaseValidatorModel):
    LabelGroupName: str
    LabelGroupArn: str
    FaultCodes: List[str]
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLabelResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyRevisionId: str
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRetrainingSchedulerResponseTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    RetrainingStartDate: datetime
    RetrainingFrequency: str
    LookbackWindow: str
    Status: RetrainingSchedulerStatusType
    PromoteMode: ModelPromoteModeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ImportDatasetResponseTypeDef(BaseValidatorModel):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportModelVersionResponseTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    ModelVersionArn: str
    ModelVersion: int
    Status: ModelVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDataIngestionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    Status: IngestionJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StartInferenceSchedulerResponseTypeDef(BaseValidatorModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StartRetrainingSchedulerResponseTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StopInferenceSchedulerResponseTypeDef(BaseValidatorModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StopRetrainingSchedulerResponseTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateActiveModelVersionResponseTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    CurrentActiveVersion: int
    PreviousActiveVersion: int
    CurrentActiveVersionArn: str
    PreviousActiveVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateLabelRequestTypeDef(BaseValidatorModel):
    LabelGroupName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Rating: LabelRatingType
    ClientToken: str
    FaultCode: Optional[str] = None
    Notes: Optional[str] = None
    Equipment: Optional[str] = None


class CreateRetrainingSchedulerRequestTypeDef(BaseValidatorModel):
    ModelName: str
    RetrainingFrequency: str
    LookbackWindow: str
    ClientToken: str
    RetrainingStartDate: Optional[TimestampTypeDef] = None
    PromoteMode: Optional[ModelPromoteModeType] = None


class ListInferenceEventsRequestTypeDef(BaseValidatorModel):
    InferenceSchedulerName: str
    IntervalStartTime: TimestampTypeDef
    IntervalEndTime: TimestampTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInferenceExecutionsRequestTypeDef(BaseValidatorModel):
    InferenceSchedulerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DataStartTimeAfter: Optional[TimestampTypeDef] = None
    DataEndTimeBefore: Optional[TimestampTypeDef] = None
    Status: Optional[InferenceExecutionStatusType] = None


class ListLabelsRequestTypeDef(BaseValidatorModel):
    LabelGroupName: str
    IntervalStartTime: Optional[TimestampTypeDef] = None
    IntervalEndTime: Optional[TimestampTypeDef] = None
    FaultCode: Optional[str] = None
    Equipment: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListModelVersionsRequestTypeDef(BaseValidatorModel):
    ModelName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ModelVersionStatusType] = None
    SourceType: Optional[ModelVersionSourceTypeType] = None
    CreatedAtEndTime: Optional[TimestampTypeDef] = None
    CreatedAtStartTime: Optional[TimestampTypeDef] = None
    MaxModelVersion: Optional[int] = None
    MinModelVersion: Optional[int] = None


class UpdateRetrainingSchedulerRequestTypeDef(BaseValidatorModel):
    ModelName: str
    RetrainingStartDate: Optional[TimestampTypeDef] = None
    RetrainingFrequency: Optional[str] = None
    LookbackWindow: Optional[str] = None
    PromoteMode: Optional[ModelPromoteModeType] = None


class ListDatasetsResponseTypeDef(BaseValidatorModel):
    DatasetSummaries: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IngestedFilesSummaryTypeDef(BaseValidatorModel):
    TotalNumberOfFiles: int
    IngestedNumberOfFiles: int
    DiscardedFiles: Optional[List[S3ObjectTypeDef]] = None


class ListInferenceEventsResponseTypeDef(BaseValidatorModel):
    InferenceEventSummaries: List[InferenceEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InferenceInputConfigurationTypeDef(BaseValidatorModel):
    S3InputConfiguration: Optional[InferenceS3InputConfigurationTypeDef] = None
    InputTimeZoneOffset: Optional[str] = None
    InferenceInputNameConfiguration: Optional[InferenceInputNameConfigurationTypeDef] = None


class InferenceOutputConfigurationTypeDef(BaseValidatorModel):
    S3OutputConfiguration: InferenceS3OutputConfigurationTypeDef
    KmsKeyId: Optional[str] = None


class ListInferenceSchedulersResponseTypeDef(BaseValidatorModel):
    InferenceSchedulerSummaries: List[InferenceSchedulerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IngestionInputConfigurationTypeDef(BaseValidatorModel):
    S3InputConfiguration: IngestionS3InputConfigurationTypeDef


class InsufficientSensorDataTypeDef(BaseValidatorModel):
    MissingCompleteSensorData: MissingCompleteSensorDataTypeDef
    SensorsWithShortDateRange: SensorsWithShortDateRangeTypeDef


class ListLabelGroupsResponseTypeDef(BaseValidatorModel):
    LabelGroupSummaries: List[LabelGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLabelsResponseTypeDef(BaseValidatorModel):
    LabelSummaries: List[LabelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LabelsInputConfigurationTypeDef(BaseValidatorModel):
    S3InputConfiguration: Optional[LabelsS3InputConfigurationTypeDef] = None
    LabelGroupName: Optional[str] = None


class ListModelVersionsResponseTypeDef(BaseValidatorModel):
    ModelVersionSummaries: List[ModelVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRetrainingSchedulersResponseTypeDef(BaseValidatorModel):
    RetrainingSchedulerSummaries: List[RetrainingSchedulerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ModelDiagnosticsOutputConfigurationTypeDef(BaseValidatorModel):
    S3OutputConfiguration: ModelDiagnosticsS3OutputConfigurationTypeDef
    KmsKeyId: Optional[str] = None


class SensorStatisticsSummaryTypeDef(BaseValidatorModel):
    ComponentName: Optional[str] = None
    SensorName: Optional[str] = None
    DataExists: Optional[bool] = None
    MissingValues: Optional[CountPercentTypeDef] = None
    InvalidValues: Optional[CountPercentTypeDef] = None
    InvalidDateEntries: Optional[CountPercentTypeDef] = None
    DuplicateTimestamps: Optional[CountPercentTypeDef] = None
    CategoricalValues: Optional[CategoricalValuesTypeDef] = None
    MultipleOperatingModes: Optional[MultipleOperatingModesTypeDef] = None
    LargeTimestampGaps: Optional[LargeTimestampGapsTypeDef] = None
    MonotonicValues: Optional[MonotonicValuesTypeDef] = None
    DataStartTime: Optional[datetime] = None
    DataEndTime: Optional[datetime] = None


class CreateInferenceSchedulerRequestTypeDef(BaseValidatorModel):
    ModelName: str
    InferenceSchedulerName: str
    DataUploadFrequency: DataUploadFrequencyType
    DataInputConfiguration: InferenceInputConfigurationTypeDef
    DataOutputConfiguration: InferenceOutputConfigurationTypeDef
    RoleArn: str
    ClientToken: str
    DataDelayOffsetInMinutes: Optional[int] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DescribeInferenceSchedulerResponseTypeDef(BaseValidatorModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    DataDelayOffsetInMinutes: int
    DataUploadFrequency: DataUploadFrequencyType
    CreatedAt: datetime
    UpdatedAt: datetime
    DataInputConfiguration: InferenceInputConfigurationTypeDef
    DataOutputConfiguration: InferenceOutputConfigurationTypeDef
    RoleArn: str
    ServerSideKmsKeyId: str
    LatestInferenceResult: LatestInferenceResultType
    ResponseMetadata: ResponseMetadataTypeDef


class InferenceExecutionSummaryTypeDef(BaseValidatorModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    InferenceSchedulerName: Optional[str] = None
    InferenceSchedulerArn: Optional[str] = None
    ScheduledStartTime: Optional[datetime] = None
    DataStartTime: Optional[datetime] = None
    DataEndTime: Optional[datetime] = None
    DataInputConfiguration: Optional[InferenceInputConfigurationTypeDef] = None
    DataOutputConfiguration: Optional[InferenceOutputConfigurationTypeDef] = None
    CustomerResultObject: Optional[S3ObjectTypeDef] = None
    Status: Optional[InferenceExecutionStatusType] = None
    FailedReason: Optional[str] = None
    ModelVersion: Optional[int] = None
    ModelVersionArn: Optional[str] = None


class UpdateInferenceSchedulerRequestTypeDef(BaseValidatorModel):
    InferenceSchedulerName: str
    DataDelayOffsetInMinutes: Optional[int] = None
    DataUploadFrequency: Optional[DataUploadFrequencyType] = None
    DataInputConfiguration: Optional[InferenceInputConfigurationTypeDef] = None
    DataOutputConfiguration: Optional[InferenceOutputConfigurationTypeDef] = None
    RoleArn: Optional[str] = None


class DataIngestionJobSummaryTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    DatasetName: Optional[str] = None
    DatasetArn: Optional[str] = None
    IngestionInputConfiguration: Optional[IngestionInputConfigurationTypeDef] = None
    Status: Optional[IngestionJobStatusType] = None


class StartDataIngestionJobRequestTypeDef(BaseValidatorModel):
    DatasetName: str
    IngestionInputConfiguration: IngestionInputConfigurationTypeDef
    RoleArn: str
    ClientToken: str


class DataQualitySummaryTypeDef(BaseValidatorModel):
    InsufficientSensorData: InsufficientSensorDataTypeDef
    MissingSensorData: MissingSensorDataTypeDef
    InvalidSensorData: InvalidSensorDataTypeDef
    UnsupportedTimestamps: UnsupportedTimestampsTypeDef
    DuplicateTimestamps: DuplicateTimestampsTypeDef


class ImportModelVersionRequestTypeDef(BaseValidatorModel):
    SourceModelVersionArn: str
    DatasetName: str
    ClientToken: str
    ModelName: Optional[str] = None
    LabelsInputConfiguration: Optional[LabelsInputConfigurationTypeDef] = None
    RoleArn: Optional[str] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    InferenceDataImportStrategy: Optional[InferenceDataImportStrategyType] = None


class CreateModelRequestTypeDef(BaseValidatorModel):
    ModelName: str
    DatasetName: str
    ClientToken: str
    DatasetSchema: Optional[DatasetSchemaTypeDef] = None
    LabelsInputConfiguration: Optional[LabelsInputConfigurationTypeDef] = None
    TrainingDataStartTime: Optional[TimestampTypeDef] = None
    TrainingDataEndTime: Optional[TimestampTypeDef] = None
    EvaluationDataStartTime: Optional[TimestampTypeDef] = None
    EvaluationDataEndTime: Optional[TimestampTypeDef] = None
    RoleArn: Optional[str] = None
    DataPreProcessingConfiguration: Optional[DataPreProcessingConfigurationTypeDef] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    OffCondition: Optional[str] = None
    ModelDiagnosticsOutputConfiguration: Optional[ModelDiagnosticsOutputConfigurationTypeDef] = None


class DescribeModelResponseTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    DatasetName: str
    DatasetArn: str
    Schema: str
    LabelsInputConfiguration: LabelsInputConfigurationTypeDef
    TrainingDataStartTime: datetime
    TrainingDataEndTime: datetime
    EvaluationDataStartTime: datetime
    EvaluationDataEndTime: datetime
    RoleArn: str
    DataPreProcessingConfiguration: DataPreProcessingConfigurationTypeDef
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
    ModelDiagnosticsOutputConfiguration: ModelDiagnosticsOutputConfigurationTypeDef
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeModelVersionResponseTypeDef(BaseValidatorModel):
    ModelName: str
    ModelArn: str
    ModelVersion: int
    ModelVersionArn: str
    Status: ModelVersionStatusType
    SourceType: ModelVersionSourceTypeType
    DatasetName: str
    DatasetArn: str
    Schema: str
    LabelsInputConfiguration: LabelsInputConfigurationTypeDef
    TrainingDataStartTime: datetime
    TrainingDataEndTime: datetime
    EvaluationDataStartTime: datetime
    EvaluationDataEndTime: datetime
    RoleArn: str
    DataPreProcessingConfiguration: DataPreProcessingConfigurationTypeDef
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
    ModelDiagnosticsOutputConfiguration: ModelDiagnosticsOutputConfigurationTypeDef
    ModelDiagnosticsResultsObject: S3ObjectTypeDef
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadataTypeDef


class ModelSummaryTypeDef(BaseValidatorModel):
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
    ModelDiagnosticsOutputConfiguration: Optional[ModelDiagnosticsOutputConfigurationTypeDef] = None
    ModelQuality: Optional[ModelQualityType] = None


class UpdateModelRequestTypeDef(BaseValidatorModel):
    ModelName: str
    LabelsInputConfiguration: Optional[LabelsInputConfigurationTypeDef] = None
    RoleArn: Optional[str] = None
    ModelDiagnosticsOutputConfiguration: Optional[ModelDiagnosticsOutputConfigurationTypeDef] = None


class ListSensorStatisticsResponseTypeDef(BaseValidatorModel):
    SensorStatisticsSummaries: List[SensorStatisticsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListInferenceExecutionsResponseTypeDef(BaseValidatorModel):
    InferenceExecutionSummaries: List[InferenceExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDataIngestionJobsResponseTypeDef(BaseValidatorModel):
    DataIngestionJobSummaries: List[DataIngestionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeDataIngestionJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    DatasetArn: str
    IngestionInputConfiguration: IngestionInputConfigurationTypeDef
    RoleArn: str
    CreatedAt: datetime
    Status: IngestionJobStatusType
    FailedReason: str
    DataQualitySummary: DataQualitySummaryTypeDef
    IngestedFilesSummary: IngestedFilesSummaryTypeDef
    StatusDetail: str
    IngestedDataSize: int
    DataStartTime: datetime
    DataEndTime: datetime
    SourceDatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    DatasetName: str
    DatasetArn: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Status: DatasetStatusType
    Schema: str
    ServerSideKmsKeyId: str
    IngestionInputConfiguration: IngestionInputConfigurationTypeDef
    DataQualitySummary: DataQualitySummaryTypeDef
    IngestedFilesSummary: IngestedFilesSummaryTypeDef
    RoleArn: str
    DataStartTime: datetime
    DataEndTime: datetime
    SourceDatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListModelsResponseTypeDef(BaseValidatorModel):
    ModelSummaries: List[ModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


