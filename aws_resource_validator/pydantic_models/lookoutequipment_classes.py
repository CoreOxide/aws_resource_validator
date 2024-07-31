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
from aws_resource_validator.pydantic_models.lookoutequipment_constants import *

class CategoricalValuesTypeDef(BaseModel):
    Status: StatisticalIssueStatusType
    NumberOfCategory: Optional[int] = None

class CountPercentTypeDef(BaseModel):
    Count: int
    Percentage: float

class DatasetSchemaTypeDef(BaseModel):
    InlineDataSchema: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DataPreProcessingConfigurationTypeDef(BaseModel):
    TargetSamplingRate: Optional[TargetSamplingRateType] = None

class DuplicateTimestampsTypeDef(BaseModel):
    TotalNumberOfDuplicateTimestamps: int

class InvalidSensorDataTypeDef(BaseModel):
    AffectedSensorCount: int
    TotalNumberOfInvalidValues: int

class MissingSensorDataTypeDef(BaseModel):
    AffectedSensorCount: int
    TotalNumberOfMissingValues: int

class UnsupportedTimestampsTypeDef(BaseModel):
    TotalNumberOfUnsupportedTimestamps: int

class DatasetSummaryTypeDef(BaseModel):
    DatasetName: Optional[str] = None
    DatasetArn: Optional[str] = None
    Status: Optional[DatasetStatusType] = None
    CreatedAt: Optional[datetime] = None

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    DatasetName: str

class DeleteInferenceSchedulerRequestRequestTypeDef(BaseModel):
    InferenceSchedulerName: str

class DeleteLabelGroupRequestRequestTypeDef(BaseModel):
    LabelGroupName: str

class DeleteLabelRequestRequestTypeDef(BaseModel):
    LabelGroupName: str
    LabelId: str

class DeleteModelRequestRequestTypeDef(BaseModel):
    ModelName: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DeleteRetrainingSchedulerRequestRequestTypeDef(BaseModel):
    ModelName: str

class DescribeDataIngestionJobRequestRequestTypeDef(BaseModel):
    JobId: str

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    DatasetName: str

class DescribeInferenceSchedulerRequestRequestTypeDef(BaseModel):
    InferenceSchedulerName: str

class DescribeLabelGroupRequestRequestTypeDef(BaseModel):
    LabelGroupName: str

class DescribeLabelRequestRequestTypeDef(BaseModel):
    LabelGroupName: str
    LabelId: str

class DescribeModelRequestRequestTypeDef(BaseModel):
    ModelName: str

class DescribeModelVersionRequestRequestTypeDef(BaseModel):
    ModelName: str
    ModelVersion: int

class S3ObjectTypeDef(BaseModel):
    Bucket: str
    Key: str

class DescribeResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DescribeRetrainingSchedulerRequestRequestTypeDef(BaseModel):
    ModelName: str

class InferenceEventSummaryTypeDef(BaseModel):
    InferenceSchedulerArn: Optional[str] = None
    InferenceSchedulerName: Optional[str] = None
    EventStartTime: Optional[datetime] = None
    EventEndTime: Optional[datetime] = None
    Diagnostics: Optional[str] = None
    EventDurationInSeconds: Optional[int] = None

class InferenceInputNameConfigurationTypeDef(BaseModel):
    TimestampFormat: Optional[str] = None
    ComponentTimestampDelimiter: Optional[str] = None

class InferenceS3InputConfigurationTypeDef(BaseModel):
    Bucket: str
    Prefix: Optional[str] = None

class InferenceS3OutputConfigurationTypeDef(BaseModel):
    Bucket: str
    Prefix: Optional[str] = None

class InferenceSchedulerSummaryTypeDef(BaseModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    InferenceSchedulerName: Optional[str] = None
    InferenceSchedulerArn: Optional[str] = None
    Status: Optional[InferenceSchedulerStatusType] = None
    DataDelayOffsetInMinutes: Optional[int] = None
    DataUploadFrequency: Optional[DataUploadFrequencyType] = None
    LatestInferenceResult: Optional[LatestInferenceResultType] = None

class IngestionS3InputConfigurationTypeDef(BaseModel):
    Bucket: str
    Prefix: Optional[str] = None
    KeyPattern: Optional[str] = None

class MissingCompleteSensorDataTypeDef(BaseModel):
    AffectedSensorCount: int

class SensorsWithShortDateRangeTypeDef(BaseModel):
    AffectedSensorCount: int

class LabelGroupSummaryTypeDef(BaseModel):
    LabelGroupName: Optional[str] = None
    LabelGroupArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class LabelSummaryTypeDef(BaseModel):
    LabelGroupName: Optional[str] = None
    LabelId: Optional[str] = None
    LabelGroupArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Rating: Optional[LabelRatingType] = None
    FaultCode: Optional[str] = None
    Equipment: Optional[str] = None
    CreatedAt: Optional[datetime] = None

class LabelsS3InputConfigurationTypeDef(BaseModel):
    Bucket: str
    Prefix: Optional[str] = None

class LargeTimestampGapsTypeDef(BaseModel):
    Status: StatisticalIssueStatusType
    NumberOfLargeTimestampGaps: Optional[int] = None
    MaxTimestampGapInDays: Optional[int] = None

class ListDataIngestionJobsRequestRequestTypeDef(BaseModel):
    DatasetName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[IngestionJobStatusType] = None

class ListDatasetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DatasetNameBeginsWith: Optional[str] = None

class ListInferenceSchedulersRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InferenceSchedulerNameBeginsWith: Optional[str] = None
    ModelName: Optional[str] = None
    Status: Optional[InferenceSchedulerStatusType] = None

class ListLabelGroupsRequestRequestTypeDef(BaseModel):
    LabelGroupNameBeginsWith: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ModelVersionSummaryTypeDef(BaseModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    ModelVersion: Optional[int] = None
    ModelVersionArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Status: Optional[ModelVersionStatusType] = None
    SourceType: Optional[ModelVersionSourceTypeType] = None
    ModelQuality: Optional[ModelQualityType] = None

class ListModelsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ModelStatusType] = None
    ModelNameBeginsWith: Optional[str] = None
    DatasetNameBeginsWith: Optional[str] = None

class ListRetrainingSchedulersRequestRequestTypeDef(BaseModel):
    ModelNameBeginsWith: Optional[str] = None
    Status: Optional[RetrainingSchedulerStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RetrainingSchedulerSummaryTypeDef(BaseModel):
    ModelName: Optional[str] = None
    ModelArn: Optional[str] = None
    Status: Optional[RetrainingSchedulerStatusType] = None
    RetrainingStartDate: Optional[datetime] = None
    RetrainingFrequency: Optional[str] = None
    LookbackWindow: Optional[str] = None

class ListSensorStatisticsRequestRequestTypeDef(BaseModel):
    DatasetName: str
    IngestionJobId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ModelDiagnosticsS3OutputConfigurationTypeDef(BaseModel):
    Bucket: str
    Prefix: Optional[str] = None

class MonotonicValuesTypeDef(BaseModel):
    Status: StatisticalIssueStatusType
    Monotonicity: Optional[MonotonicityType] = None

class MultipleOperatingModesTypeDef(BaseModel):
    Status: StatisticalIssueStatusType

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    ResourcePolicy: str
    ClientToken: str
    PolicyRevisionId: Optional[str] = None

class StartInferenceSchedulerRequestRequestTypeDef(BaseModel):
    InferenceSchedulerName: str

class StartRetrainingSchedulerRequestRequestTypeDef(BaseModel):
    ModelName: str

class StopInferenceSchedulerRequestRequestTypeDef(BaseModel):
    InferenceSchedulerName: str

class StopRetrainingSchedulerRequestRequestTypeDef(BaseModel):
    ModelName: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateActiveModelVersionRequestRequestTypeDef(BaseModel):
    ModelName: str
    ModelVersion: int

class UpdateLabelGroupRequestRequestTypeDef(BaseModel):
    LabelGroupName: str
    FaultCodes: Optional[Sequence[str]] = None

class CreateDatasetRequestRequestTypeDef(BaseModel):
    DatasetName: str
    ClientToken: str
    DatasetSchema: Optional[DatasetSchemaTypeDef] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateLabelGroupRequestRequestTypeDef(BaseModel):
    LabelGroupName: str
    ClientToken: str
    FaultCodes: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ImportDatasetRequestRequestTypeDef(BaseModel):
    SourceDatasetArn: str
    ClientToken: str
    DatasetName: Optional[str] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateDatasetResponseTypeDef(BaseModel):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInferenceSchedulerResponseTypeDef(BaseModel):
    InferenceSchedulerArn: str
    InferenceSchedulerName: str
    Status: InferenceSchedulerStatusType
    ModelQuality: ModelQualityType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelGroupResponseTypeDef(BaseModel):
    LabelGroupName: str
    LabelGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelResponseTypeDef(BaseModel):
    LabelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelResponseTypeDef(BaseModel):
    ModelArn: str
    Status: ModelStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRetrainingSchedulerResponseTypeDef(BaseModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLabelGroupResponseTypeDef(BaseModel):
    LabelGroupName: str
    LabelGroupArn: str
    FaultCodes: List[str]
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLabelResponseTypeDef(BaseModel):
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

class DescribeResourcePolicyResponseTypeDef(BaseModel):
    PolicyRevisionId: str
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRetrainingSchedulerResponseTypeDef(BaseModel):
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

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ImportDatasetResponseTypeDef(BaseModel):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatusType
    JobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportModelVersionResponseTypeDef(BaseModel):
    ModelName: str
    ModelArn: str
    ModelVersionArn: str
    ModelVersion: int
    Status: ModelVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseModel):
    ResourceArn: str
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataIngestionJobResponseTypeDef(BaseModel):
    JobId: str
    Status: IngestionJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartInferenceSchedulerResponseTypeDef(BaseModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartRetrainingSchedulerResponseTypeDef(BaseModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopInferenceSchedulerResponseTypeDef(BaseModel):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopRetrainingSchedulerResponseTypeDef(BaseModel):
    ModelName: str
    ModelArn: str
    Status: RetrainingSchedulerStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActiveModelVersionResponseTypeDef(BaseModel):
    ModelName: str
    ModelArn: str
    CurrentActiveVersion: int
    PreviousActiveVersion: int
    CurrentActiveVersionArn: str
    PreviousActiveVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLabelRequestRequestTypeDef(BaseModel):
    LabelGroupName: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Rating: LabelRatingType
    ClientToken: str
    FaultCode: Optional[str] = None
    Notes: Optional[str] = None
    Equipment: Optional[str] = None

class CreateRetrainingSchedulerRequestRequestTypeDef(BaseModel):
    ModelName: str
    RetrainingFrequency: str
    LookbackWindow: str
    ClientToken: str
    RetrainingStartDate: Optional[TimestampTypeDef] = None
    PromoteMode: Optional[ModelPromoteModeType] = None

class ListInferenceEventsRequestRequestTypeDef(BaseModel):
    InferenceSchedulerName: str
    IntervalStartTime: TimestampTypeDef
    IntervalEndTime: TimestampTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInferenceExecutionsRequestRequestTypeDef(BaseModel):
    InferenceSchedulerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DataStartTimeAfter: Optional[TimestampTypeDef] = None
    DataEndTimeBefore: Optional[TimestampTypeDef] = None
    Status: Optional[InferenceExecutionStatusType] = None

class ListLabelsRequestRequestTypeDef(BaseModel):
    LabelGroupName: str
    IntervalStartTime: Optional[TimestampTypeDef] = None
    IntervalEndTime: Optional[TimestampTypeDef] = None
    FaultCode: Optional[str] = None
    Equipment: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListModelVersionsRequestRequestTypeDef(BaseModel):
    ModelName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[ModelVersionStatusType] = None
    SourceType: Optional[ModelVersionSourceTypeType] = None
    CreatedAtEndTime: Optional[TimestampTypeDef] = None
    CreatedAtStartTime: Optional[TimestampTypeDef] = None
    MaxModelVersion: Optional[int] = None
    MinModelVersion: Optional[int] = None

class UpdateRetrainingSchedulerRequestRequestTypeDef(BaseModel):
    ModelName: str
    RetrainingStartDate: Optional[TimestampTypeDef] = None
    RetrainingFrequency: Optional[str] = None
    LookbackWindow: Optional[str] = None
    PromoteMode: Optional[ModelPromoteModeType] = None

class ListDatasetsResponseTypeDef(BaseModel):
    NextToken: str
    DatasetSummaries: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IngestedFilesSummaryTypeDef(BaseModel):
    TotalNumberOfFiles: int
    IngestedNumberOfFiles: int
    DiscardedFiles: Optional[List[S3ObjectTypeDef]] = None

class ListInferenceEventsResponseTypeDef(BaseModel):
    NextToken: str
    InferenceEventSummaries: List[InferenceEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InferenceInputConfigurationTypeDef(BaseModel):
    S3InputConfiguration: Optional[InferenceS3InputConfigurationTypeDef] = None
    InputTimeZoneOffset: Optional[str] = None
    InferenceInputNameConfiguration: Optional[InferenceInputNameConfigurationTypeDef] = None

class InferenceOutputConfigurationTypeDef(BaseModel):
    S3OutputConfiguration: InferenceS3OutputConfigurationTypeDef
    KmsKeyId: Optional[str] = None

class ListInferenceSchedulersResponseTypeDef(BaseModel):
    NextToken: str
    InferenceSchedulerSummaries: List[InferenceSchedulerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IngestionInputConfigurationTypeDef(BaseModel):
    S3InputConfiguration: IngestionS3InputConfigurationTypeDef

class InsufficientSensorDataTypeDef(BaseModel):
    MissingCompleteSensorData: MissingCompleteSensorDataTypeDef
    SensorsWithShortDateRange: SensorsWithShortDateRangeTypeDef

class ListLabelGroupsResponseTypeDef(BaseModel):
    NextToken: str
    LabelGroupSummaries: List[LabelGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLabelsResponseTypeDef(BaseModel):
    NextToken: str
    LabelSummaries: List[LabelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LabelsInputConfigurationTypeDef(BaseModel):
    S3InputConfiguration: Optional[LabelsS3InputConfigurationTypeDef] = None
    LabelGroupName: Optional[str] = None

class ListModelVersionsResponseTypeDef(BaseModel):
    NextToken: str
    ModelVersionSummaries: List[ModelVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRetrainingSchedulersResponseTypeDef(BaseModel):
    RetrainingSchedulerSummaries: List[RetrainingSchedulerSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModelDiagnosticsOutputConfigurationTypeDef(BaseModel):
    S3OutputConfiguration: ModelDiagnosticsS3OutputConfigurationTypeDef
    KmsKeyId: Optional[str] = None

class SensorStatisticsSummaryTypeDef(BaseModel):
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

class CreateInferenceSchedulerRequestRequestTypeDef(BaseModel):
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

class DescribeInferenceSchedulerResponseTypeDef(BaseModel):
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

class InferenceExecutionSummaryTypeDef(BaseModel):
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

class UpdateInferenceSchedulerRequestRequestTypeDef(BaseModel):
    InferenceSchedulerName: str
    DataDelayOffsetInMinutes: Optional[int] = None
    DataUploadFrequency: Optional[DataUploadFrequencyType] = None
    DataInputConfiguration: Optional[InferenceInputConfigurationTypeDef] = None
    DataOutputConfiguration: Optional[InferenceOutputConfigurationTypeDef] = None
    RoleArn: Optional[str] = None

class DataIngestionJobSummaryTypeDef(BaseModel):
    JobId: Optional[str] = None
    DatasetName: Optional[str] = None
    DatasetArn: Optional[str] = None
    IngestionInputConfiguration: Optional[IngestionInputConfigurationTypeDef] = None
    Status: Optional[IngestionJobStatusType] = None

class StartDataIngestionJobRequestRequestTypeDef(BaseModel):
    DatasetName: str
    IngestionInputConfiguration: IngestionInputConfigurationTypeDef
    RoleArn: str
    ClientToken: str

class DataQualitySummaryTypeDef(BaseModel):
    InsufficientSensorData: InsufficientSensorDataTypeDef
    MissingSensorData: MissingSensorDataTypeDef
    InvalidSensorData: InvalidSensorDataTypeDef
    UnsupportedTimestamps: UnsupportedTimestampsTypeDef
    DuplicateTimestamps: DuplicateTimestampsTypeDef

class ImportModelVersionRequestRequestTypeDef(BaseModel):
    SourceModelVersionArn: str
    DatasetName: str
    ClientToken: str
    ModelName: Optional[str] = None
    LabelsInputConfiguration: Optional[LabelsInputConfigurationTypeDef] = None
    RoleArn: Optional[str] = None
    ServerSideKmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    InferenceDataImportStrategy: Optional[InferenceDataImportStrategyType] = None

class CreateModelRequestRequestTypeDef(BaseModel):
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
    ModelDiagnosticsOutputConfiguration: Optional[       ModelDiagnosticsOutputConfigurationTypeDef     ] = None

class DescribeModelResponseTypeDef(BaseModel):
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

class DescribeModelVersionResponseTypeDef(BaseModel):
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

class ModelSummaryTypeDef(BaseModel):
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
    ModelDiagnosticsOutputConfiguration: Optional[       ModelDiagnosticsOutputConfigurationTypeDef     ] = None
    ModelQuality: Optional[ModelQualityType] = None

class UpdateModelRequestRequestTypeDef(BaseModel):
    ModelName: str
    LabelsInputConfiguration: Optional[LabelsInputConfigurationTypeDef] = None
    RoleArn: Optional[str] = None
    ModelDiagnosticsOutputConfiguration: Optional[       ModelDiagnosticsOutputConfigurationTypeDef     ] = None

class ListSensorStatisticsResponseTypeDef(BaseModel):
    SensorStatisticsSummaries: List[SensorStatisticsSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInferenceExecutionsResponseTypeDef(BaseModel):
    NextToken: str
    InferenceExecutionSummaries: List[InferenceExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataIngestionJobsResponseTypeDef(BaseModel):
    NextToken: str
    DataIngestionJobSummaries: List[DataIngestionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataIngestionJobResponseTypeDef(BaseModel):
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

class DescribeDatasetResponseTypeDef(BaseModel):
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

class ListModelsResponseTypeDef(BaseModel):
    NextToken: str
    ModelSummaries: List[ModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

