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
from aws_resource_validator.pydantic_models.lookoutmetrics_constants import *

class LambdaConfigurationTypeDef(BaseValidatorModel):
    RoleArn: str
    LambdaArn: str

class SNSConfigurationTypeDef(BaseValidatorModel):
    RoleArn: str
    SnsTopicArn: str
    SnsFormat: Optional[SnsFormatType] = None

class ActivateAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str

class DimensionFilterTypeDef(BaseValidatorModel):
    DimensionName: Optional[str] = None
    DimensionValueList: Optional[Sequence[str]] = None

class AlertSummaryTypeDef(BaseValidatorModel):
    AlertArn: Optional[str] = None
    AnomalyDetectorArn: Optional[str] = None
    AlertName: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    AlertType: Optional[AlertTypeType] = None
    AlertStatus: Optional[AlertStatusType] = None
    LastModificationTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class AnomalyDetectorConfigSummaryTypeDef(BaseValidatorModel):
    AnomalyDetectorFrequency: Optional[FrequencyType] = None

class AnomalyDetectorConfigTypeDef(BaseValidatorModel):
    AnomalyDetectorFrequency: Optional[FrequencyType] = None

class AnomalyDetectorSummaryTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: Optional[str] = None
    AnomalyDetectorName: Optional[str] = None
    AnomalyDetectorDescription: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    Status: Optional[AnomalyDetectorStatusType] = None
    Tags: Optional[Dict[str, str]] = None

class ItemizedMetricStatsTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    OccurrenceCount: Optional[int] = None

class AnomalyGroupSummaryTypeDef(BaseValidatorModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    AnomalyGroupScore: Optional[float] = None
    PrimaryMetricName: Optional[str] = None

class AnomalyGroupTimeSeriesFeedbackTypeDef(BaseValidatorModel):
    AnomalyGroupId: str
    TimeSeriesId: str
    IsAnomaly: bool

class AnomalyGroupTimeSeriesTypeDef(BaseValidatorModel):
    AnomalyGroupId: str
    TimeSeriesId: Optional[str] = None

class AppFlowConfigTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    FlowName: Optional[str] = None

class BackTestConfigurationTypeDef(BaseValidatorModel):
    RunBackTestMode: bool

class AttributeValueTypeDef(BaseValidatorModel):
    S: Optional[str] = None
    N: Optional[str] = None
    B: Optional[str] = None
    SS: Optional[List[str]] = None
    NS: Optional[List[str]] = None
    BS: Optional[List[str]] = None

class AutoDetectionS3SourceConfigTypeDef(BaseValidatorModel):
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None

class BackTestAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class MetricTypeDef(BaseValidatorModel):
    MetricName: str
    AggregationFunction: AggregationFunctionType
    Namespace: Optional[str] = None

class TimestampColumnTypeDef(BaseValidatorModel):
    ColumnName: Optional[str] = None
    ColumnFormat: Optional[str] = None

class CsvFormatDescriptorTypeDef(BaseValidatorModel):
    FileCompression: Optional[CSVFileCompressionType] = None
    Charset: Optional[str] = None
    ContainsHeader: Optional[bool] = None
    Delimiter: Optional[str] = None
    HeaderList: Optional[Sequence[str]] = None
    QuoteSymbol: Optional[str] = None

class DataQualityMetricTypeDef(BaseValidatorModel):
    MetricType: Optional[DataQualityMetricTypeType] = None
    MetricDescription: Optional[str] = None
    RelatedColumnName: Optional[str] = None
    MetricValue: Optional[float] = None

class DeactivateAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str

class DeleteAlertRequestRequestTypeDef(BaseValidatorModel):
    AlertArn: str

class DeleteAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str

class DescribeAlertRequestRequestTypeDef(BaseValidatorModel):
    AlertArn: str

class DescribeAnomalyDetectionExecutionsRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    Timestamp: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ExecutionStatusTypeDef(BaseValidatorModel):
    Timestamp: Optional[str] = None
    Status: Optional[AnomalyDetectionTaskStatusType] = None
    FailureReason: Optional[str] = None

class DescribeAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str

class DescribeMetricSetRequestRequestTypeDef(BaseValidatorModel):
    MetricSetArn: str

class DimensionValueContributionTypeDef(BaseValidatorModel):
    DimensionValue: Optional[str] = None
    ContributionScore: Optional[float] = None

class DimensionNameValueTypeDef(BaseValidatorModel):
    DimensionName: str
    DimensionValue: str

class JsonFormatDescriptorTypeDef(BaseValidatorModel):
    FileCompression: Optional[JsonFileCompressionType] = None
    Charset: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    DimensionValue: Optional[str] = None
    FilterOperation: Optional[Literal["EQUALS"]] = None

class GetAnomalyGroupRequestRequestTypeDef(BaseValidatorModel):
    AnomalyGroupId: str
    AnomalyDetectorArn: str

class GetDataQualityMetricsRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    MetricSetArn: Optional[str] = None

class TimeSeriesFeedbackTypeDef(BaseValidatorModel):
    TimeSeriesId: Optional[str] = None
    IsAnomaly: Optional[bool] = None

class InterMetricImpactDetailsTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    RelationshipType: Optional[RelationshipTypeType] = None
    ContributionPercentage: Optional[float] = None

class ListAlertsRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAnomalyDetectorsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAnomalyGroupRelatedMetricsRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    RelationshipTypeFilter: Optional[RelationshipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAnomalyGroupSummariesRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    SensitivityThreshold: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAnomalyGroupTimeSeriesRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    MetricName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMetricSetsRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MetricSetSummaryTypeDef(BaseValidatorModel):
    MetricSetArn: Optional[str] = None
    AnomalyDetectorArn: Optional[str] = None
    MetricSetDescription: Optional[str] = None
    MetricSetName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class VpcConfigurationTypeDef(BaseValidatorModel):
    SubnetIdList: Sequence[str]
    SecurityGroupIdList: Sequence[str]

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class ActionTypeDef(BaseValidatorModel):
    SNSConfiguration: Optional[SNSConfigurationTypeDef] = None
    LambdaConfiguration: Optional[LambdaConfigurationTypeDef] = None

class AlertFiltersTypeDef(BaseValidatorModel):
    MetricList: Optional[Sequence[str]] = None
    DimensionFilterList: Optional[Sequence[DimensionFilterTypeDef]] = None

class CreateAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorName: str
    AnomalyDetectorConfig: AnomalyDetectorConfigTypeDef
    AnomalyDetectorDescription: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    KmsKeyArn: Optional[str] = None
    AnomalyDetectorDescription: Optional[str] = None
    AnomalyDetectorConfig: Optional[AnomalyDetectorConfigTypeDef] = None

class AnomalyGroupStatisticsTypeDef(BaseValidatorModel):
    EvaluationStartDate: Optional[str] = None
    TotalCount: Optional[int] = None
    ItemizedMetricStatsList: Optional[List[ItemizedMetricStatsTypeDef]] = None

class PutFeedbackRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesFeedbackTypeDef

class GetFeedbackRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class AthenaSourceConfigTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    DataCatalog: Optional[str] = None
    TableName: Optional[str] = None
    WorkGroupName: Optional[str] = None
    S3ResultsPath: Optional[str] = None
    BackTestConfiguration: Optional[BackTestConfigurationTypeDef] = None

class CloudWatchConfigTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    BackTestConfiguration: Optional[BackTestConfigurationTypeDef] = None

class DetectedFieldTypeDef(BaseValidatorModel):
    Value: Optional[AttributeValueTypeDef] = None
    Confidence: Optional[ConfidenceType] = None
    Message: Optional[str] = None

class AutoDetectionMetricSourceTypeDef(BaseValidatorModel):
    S3SourceConfig: Optional[AutoDetectionS3SourceConfigTypeDef] = None

class CreateAlertResponseTypeDef(BaseValidatorModel):
    AlertArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnomalyDetectorResponseTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMetricSetResponseTypeDef(BaseValidatorModel):
    MetricSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAnomalyDetectorResponseTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyDetectorName: str
    AnomalyDetectorDescription: str
    AnomalyDetectorConfig: AnomalyDetectorConfigSummaryTypeDef
    CreationTime: datetime
    LastModificationTime: datetime
    Status: AnomalyDetectorStatusType
    FailureReason: str
    KmsKeyArn: str
    FailureType: AnomalyDetectorFailureTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetSampleDataResponseTypeDef(BaseValidatorModel):
    HeaderValues: List[str]
    SampleRows: List[List[str]]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlertsResponseTypeDef(BaseValidatorModel):
    AlertSummaryList: List[AlertSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnomalyDetectorsResponseTypeDef(BaseValidatorModel):
    AnomalyDetectorSummaryList: List[AnomalyDetectorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAlertResponseTypeDef(BaseValidatorModel):
    AlertArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnomalyDetectorResponseTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMetricSetResponseTypeDef(BaseValidatorModel):
    MetricSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricSetDataQualityMetricTypeDef(BaseValidatorModel):
    MetricSetArn: Optional[str] = None
    DataQualityMetricList: Optional[List[DataQualityMetricTypeDef]] = None

class DescribeAnomalyDetectionExecutionsResponseTypeDef(BaseValidatorModel):
    ExecutionList: List[ExecutionStatusTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DimensionContributionTypeDef(BaseValidatorModel):
    DimensionName: Optional[str] = None
    DimensionValueContributionList: Optional[List[DimensionValueContributionTypeDef]] = None

class TimeSeriesTypeDef(BaseValidatorModel):
    TimeSeriesId: str
    DimensionList: List[DimensionNameValueTypeDef]
    MetricValueList: List[float]

class FileFormatDescriptorTypeDef(BaseValidatorModel):
    CsvFormatDescriptor: Optional[CsvFormatDescriptorTypeDef] = None
    JsonFormatDescriptor: Optional[JsonFormatDescriptorTypeDef] = None

class MetricSetDimensionFilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    FilterList: Optional[Sequence[FilterTypeDef]] = None

class GetFeedbackResponseTypeDef(BaseValidatorModel):
    AnomalyGroupTimeSeriesFeedback: List[TimeSeriesFeedbackTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnomalyGroupRelatedMetricsResponseTypeDef(BaseValidatorModel):
    InterMetricImpactList: List[InterMetricImpactDetailsTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetricSetsResponseTypeDef(BaseValidatorModel):
    MetricSetSummaryList: List[MetricSetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RDSSourceConfigTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None

class RedshiftSourceConfigTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None

class AlertTypeDef(BaseValidatorModel):
    Action: Optional[ActionTypeDef] = None
    AlertDescription: Optional[str] = None
    AlertArn: Optional[str] = None
    AnomalyDetectorArn: Optional[str] = None
    AlertName: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    AlertType: Optional[AlertTypeType] = None
    AlertStatus: Optional[AlertStatusType] = None
    LastModificationTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    AlertFilters: Optional[AlertFiltersTypeDef] = None

class CreateAlertRequestRequestTypeDef(BaseValidatorModel):
    AlertName: str
    AnomalyDetectorArn: str
    Action: ActionTypeDef
    AlertSensitivityThreshold: Optional[int] = None
    AlertDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    AlertFilters: Optional[AlertFiltersTypeDef] = None

class UpdateAlertRequestRequestTypeDef(BaseValidatorModel):
    AlertArn: str
    AlertDescription: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    Action: Optional[ActionTypeDef] = None
    AlertFilters: Optional[AlertFiltersTypeDef] = None

class ListAnomalyGroupSummariesResponseTypeDef(BaseValidatorModel):
    AnomalyGroupSummaryList: List[AnomalyGroupSummaryTypeDef]
    AnomalyGroupStatistics: AnomalyGroupStatisticsTypeDef
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectedCsvFormatDescriptorTypeDef(BaseValidatorModel):
    FileCompression: Optional[DetectedFieldTypeDef] = None
    Charset: Optional[DetectedFieldTypeDef] = None
    ContainsHeader: Optional[DetectedFieldTypeDef] = None
    Delimiter: Optional[DetectedFieldTypeDef] = None
    HeaderList: Optional[DetectedFieldTypeDef] = None
    QuoteSymbol: Optional[DetectedFieldTypeDef] = None

class DetectedJsonFormatDescriptorTypeDef(BaseValidatorModel):
    FileCompression: Optional[DetectedFieldTypeDef] = None
    Charset: Optional[DetectedFieldTypeDef] = None

class DetectMetricSetConfigRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AutoDetectionMetricSource: AutoDetectionMetricSourceTypeDef

class AnomalyDetectorDataQualityMetricTypeDef(BaseValidatorModel):
    StartTimestamp: Optional[datetime] = None
    MetricSetDataQualityMetricList: Optional[List[MetricSetDataQualityMetricTypeDef]] = None

class ContributionMatrixTypeDef(BaseValidatorModel):
    DimensionContributionList: Optional[List[DimensionContributionTypeDef]] = None

class ListAnomalyGroupTimeSeriesResponseTypeDef(BaseValidatorModel):
    AnomalyGroupId: str
    MetricName: str
    TimestampList: List[str]
    NextToken: str
    TimeSeriesList: List[TimeSeriesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class S3SourceConfigTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None
    FileFormatDescriptor: Optional[FileFormatDescriptorTypeDef] = None

class SampleDataS3SourceConfigTypeDef(BaseValidatorModel):
    RoleArn: str
    FileFormatDescriptor: FileFormatDescriptorTypeDef
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None

class DescribeAlertResponseTypeDef(BaseValidatorModel):
    Alert: AlertTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DetectedFileFormatDescriptorTypeDef(BaseValidatorModel):
    CsvFormatDescriptor: Optional[DetectedCsvFormatDescriptorTypeDef] = None
    JsonFormatDescriptor: Optional[DetectedJsonFormatDescriptorTypeDef] = None

class GetDataQualityMetricsResponseTypeDef(BaseValidatorModel):
    AnomalyDetectorDataQualityMetricList: List[AnomalyDetectorDataQualityMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricLevelImpactTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    NumTimeSeries: Optional[int] = None
    ContributionMatrix: Optional[ContributionMatrixTypeDef] = None

class MetricSourceTypeDef(BaseValidatorModel):
    S3SourceConfig: Optional[S3SourceConfigTypeDef] = None
    AppFlowConfig: Optional[AppFlowConfigTypeDef] = None
    CloudWatchConfig: Optional[CloudWatchConfigTypeDef] = None
    RDSSourceConfig: Optional[RDSSourceConfigTypeDef] = None
    RedshiftSourceConfig: Optional[RedshiftSourceConfigTypeDef] = None
    AthenaSourceConfig: Optional[AthenaSourceConfigTypeDef] = None

class GetSampleDataRequestRequestTypeDef(BaseValidatorModel):
    S3SourceConfig: Optional[SampleDataS3SourceConfigTypeDef] = None

class DetectedS3SourceConfigTypeDef(BaseValidatorModel):
    FileFormatDescriptor: Optional[DetectedFileFormatDescriptorTypeDef] = None

class AnomalyGroupTypeDef(BaseValidatorModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    AnomalyGroupScore: Optional[float] = None
    PrimaryMetricName: Optional[str] = None
    MetricLevelImpactList: Optional[List[MetricLevelImpactTypeDef]] = None

class CreateMetricSetRequestRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    MetricSetName: str
    MetricList: Sequence[MetricTypeDef]
    MetricSource: MetricSourceTypeDef
    MetricSetDescription: Optional[str] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumnTypeDef] = None
    DimensionList: Optional[Sequence[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    Timezone: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    DimensionFilterList: Optional[Sequence[MetricSetDimensionFilterTypeDef]] = None

class DescribeMetricSetResponseTypeDef(BaseValidatorModel):
    MetricSetArn: str
    AnomalyDetectorArn: str
    MetricSetName: str
    MetricSetDescription: str
    CreationTime: datetime
    LastModificationTime: datetime
    Offset: int
    MetricList: List[MetricTypeDef]
    TimestampColumn: TimestampColumnTypeDef
    DimensionList: List[str]
    MetricSetFrequency: FrequencyType
    Timezone: str
    MetricSource: MetricSourceTypeDef
    DimensionFilterList: List[MetricSetDimensionFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMetricSetRequestRequestTypeDef(BaseValidatorModel):
    MetricSetArn: str
    MetricSetDescription: Optional[str] = None
    MetricList: Optional[Sequence[MetricTypeDef]] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumnTypeDef] = None
    DimensionList: Optional[Sequence[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    MetricSource: Optional[MetricSourceTypeDef] = None
    DimensionFilterList: Optional[Sequence[MetricSetDimensionFilterTypeDef]] = None

class DetectedMetricSourceTypeDef(BaseValidatorModel):
    S3SourceConfig: Optional[DetectedS3SourceConfigTypeDef] = None

class GetAnomalyGroupResponseTypeDef(BaseValidatorModel):
    AnomalyGroup: AnomalyGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DetectedMetricSetConfigTypeDef(BaseValidatorModel):
    Offset: Optional[DetectedFieldTypeDef] = None
    MetricSetFrequency: Optional[DetectedFieldTypeDef] = None
    MetricSource: Optional[DetectedMetricSourceTypeDef] = None

class DetectMetricSetConfigResponseTypeDef(BaseValidatorModel):
    DetectedMetricSetConfig: DetectedMetricSetConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

