from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class LambdaConfiguration(BaseValidatorModel):
    RoleArn: str
    LambdaArn: str


class SNSConfiguration(BaseValidatorModel):
    RoleArn: str
    SnsTopicArn: str
    SnsFormat: Optional[SnsFormatType] = None


class ActivateAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorArn: str


class DimensionFilterOutput(BaseValidatorModel):
    DimensionName: Optional[str] = None
    DimensionValueList: Optional[List[str]] = None


class DimensionFilter(BaseValidatorModel):
    DimensionName: Optional[str] = None
    DimensionValueList: Optional[List[str]] = None


class AlertSummary(BaseValidatorModel):
    AlertArn: Optional[str] = None
    AnomalyDetectorArn: Optional[str] = None
    AlertName: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    AlertType: Optional[AlertTypeType] = None
    AlertStatus: Optional[AlertStatusType] = None
    LastModificationTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class AnomalyDetectorConfigSummary(BaseValidatorModel):
    AnomalyDetectorFrequency: Optional[FrequencyType] = None


class AnomalyDetectorConfig(BaseValidatorModel):
    AnomalyDetectorFrequency: Optional[FrequencyType] = None


class AnomalyDetectorSummary(BaseValidatorModel):
    AnomalyDetectorArn: Optional[str] = None
    AnomalyDetectorName: Optional[str] = None
    AnomalyDetectorDescription: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    Status: Optional[AnomalyDetectorStatusType] = None
    Tags: Optional[Dict[str, str]] = None


class ItemizedMetricStats(BaseValidatorModel):
    MetricName: Optional[str] = None
    OccurrenceCount: Optional[int] = None


class AnomalyGroupSummary(BaseValidatorModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    AnomalyGroupScore: Optional[float] = None
    PrimaryMetricName: Optional[str] = None


class AnomalyGroupTimeSeriesFeedback(BaseValidatorModel):
    AnomalyGroupId: str
    TimeSeriesId: str
    IsAnomaly: bool


class AnomalyGroupTimeSeries(BaseValidatorModel):
    AnomalyGroupId: str
    TimeSeriesId: Optional[str] = None


class AppFlowConfig(BaseValidatorModel):
    RoleArn: Optional[str] = None
    FlowName: Optional[str] = None


class BackTestConfiguration(BaseValidatorModel):
    RunBackTestMode: bool


class AttributeValue(BaseValidatorModel):
    S: Optional[str] = None
    N: Optional[str] = None
    B: Optional[str] = None
    SS: Optional[List[str]] = None
    NS: Optional[List[str]] = None
    BS: Optional[List[str]] = None


class AutoDetectionS3SourceConfig(BaseValidatorModel):
    TemplatedPathList: Optional[List[str]] = None
    HistoricalDataPathList: Optional[List[str]] = None


class BackTestAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Metric(BaseValidatorModel):
    MetricName: str
    AggregationFunction: AggregationFunctionType
    Namespace: Optional[str] = None


class TimestampColumn(BaseValidatorModel):
    ColumnName: Optional[str] = None
    ColumnFormat: Optional[str] = None


class CsvFormatDescriptorOutput(BaseValidatorModel):
    FileCompression: Optional[CSVFileCompressionType] = None
    Charset: Optional[str] = None
    ContainsHeader: Optional[bool] = None
    Delimiter: Optional[str] = None
    HeaderList: Optional[List[str]] = None
    QuoteSymbol: Optional[str] = None


class CsvFormatDescriptor(BaseValidatorModel):
    FileCompression: Optional[CSVFileCompressionType] = None
    Charset: Optional[str] = None
    ContainsHeader: Optional[bool] = None
    Delimiter: Optional[str] = None
    HeaderList: Optional[List[str]] = None
    QuoteSymbol: Optional[str] = None


class DataQualityMetric(BaseValidatorModel):
    MetricType: Optional[DataQualityMetricTypeType] = None
    MetricDescription: Optional[str] = None
    RelatedColumnName: Optional[str] = None
    MetricValue: Optional[float] = None


class DeactivateAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorArn: str


class DeleteAlertRequest(BaseValidatorModel):
    AlertArn: str


class DeleteAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorArn: str


# This class is the input for the 'describe_alert' function.
class DescribeAlertRequest(BaseValidatorModel):
    AlertArn: str


# This class is the input for the 'describe_anomaly_detection_executions' function.
class DescribeAnomalyDetectionExecutionsRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    Timestamp: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ExecutionStatus(BaseValidatorModel):
    Timestamp: Optional[str] = None
    Status: Optional[AnomalyDetectionTaskStatusType] = None
    FailureReason: Optional[str] = None


# This class is the input for the 'describe_anomaly_detector' function.
class DescribeAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorArn: str


# This class is the input for the 'describe_metric_set' function.
class DescribeMetricSetRequest(BaseValidatorModel):
    MetricSetArn: str


class DimensionValueContribution(BaseValidatorModel):
    DimensionValue: Optional[str] = None
    ContributionScore: Optional[float] = None


class DimensionNameValue(BaseValidatorModel):
    DimensionName: str
    DimensionValue: str


class JsonFormatDescriptor(BaseValidatorModel):
    FileCompression: Optional[JsonFileCompressionType] = None
    Charset: Optional[str] = None


class Filter(BaseValidatorModel):
    DimensionValue: Optional[str] = None
    FilterOperation: Optional[Literal['EQUALS']] = None


# This class is the input for the 'get_anomaly_group' function.
class GetAnomalyGroupRequest(BaseValidatorModel):
    AnomalyGroupId: str
    AnomalyDetectorArn: str


# This class is the input for the 'get_data_quality_metrics' function.
class GetDataQualityMetricsRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    MetricSetArn: Optional[str] = None


class TimeSeriesFeedback(BaseValidatorModel):
    TimeSeriesId: Optional[str] = None
    IsAnomaly: Optional[bool] = None


class InterMetricImpactDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    RelationshipType: Optional[RelationshipTypeType] = None
    ContributionPercentage: Optional[float] = None


# This class is the input for the 'list_alerts' function.
class ListAlertsRequest(BaseValidatorModel):
    AnomalyDetectorArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_anomaly_detectors' function.
class ListAnomalyDetectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_anomaly_group_related_metrics' function.
class ListAnomalyGroupRelatedMetricsRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    RelationshipTypeFilter: Optional[RelationshipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_anomaly_group_summaries' function.
class ListAnomalyGroupSummariesRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    SensitivityThreshold: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_anomaly_group_time_series' function.
class ListAnomalyGroupTimeSeriesRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    MetricName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_metric_sets' function.
class ListMetricSetsRequest(BaseValidatorModel):
    AnomalyDetectorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MetricSetSummary(BaseValidatorModel):
    MetricSetArn: Optional[str] = None
    AnomalyDetectorArn: Optional[str] = None
    MetricSetDescription: Optional[str] = None
    MetricSetName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class VpcConfigurationOutput(BaseValidatorModel):
    SubnetIdList: List[str]
    SecurityGroupIdList: List[str]


class VpcConfiguration(BaseValidatorModel):
    SubnetIdList: List[str]
    SecurityGroupIdList: List[str]


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class Action(BaseValidatorModel):
    SNSConfiguration: Optional[SNSConfiguration] = None
    LambdaConfiguration: Optional[LambdaConfiguration] = None


class AlertFiltersOutput(BaseValidatorModel):
    MetricList: Optional[List[str]] = None
    DimensionFilterList: Optional[List[DimensionFilterOutput]] = None


class AlertFilters(BaseValidatorModel):
    MetricList: Optional[List[str]] = None
    DimensionFilterList: Optional[List[DimensionFilter]] = None


# This class is the input for the 'create_anomaly_detector' function.
class CreateAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorName: str
    AnomalyDetectorConfig: AnomalyDetectorConfig
    AnomalyDetectorDescription: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_anomaly_detector' function.
class UpdateAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    KmsKeyArn: Optional[str] = None
    AnomalyDetectorDescription: Optional[str] = None
    AnomalyDetectorConfig: Optional[AnomalyDetectorConfig] = None


class AnomalyGroupStatistics(BaseValidatorModel):
    EvaluationStartDate: Optional[str] = None
    TotalCount: Optional[int] = None
    ItemizedMetricStatsList: Optional[List[ItemizedMetricStats]] = None


class PutFeedbackRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesFeedback


# This class is the input for the 'get_feedback' function.
class GetFeedbackRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeries
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class AthenaSourceConfig(BaseValidatorModel):
    RoleArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    DataCatalog: Optional[str] = None
    TableName: Optional[str] = None
    WorkGroupName: Optional[str] = None
    S3ResultsPath: Optional[str] = None
    BackTestConfiguration: Optional[BackTestConfiguration] = None


class CloudWatchConfig(BaseValidatorModel):
    RoleArn: Optional[str] = None
    BackTestConfiguration: Optional[BackTestConfiguration] = None


class DetectedField(BaseValidatorModel):
    Value: Optional[AttributeValue] = None
    Confidence: Optional[ConfidenceType] = None
    Message: Optional[str] = None


class AutoDetectionMetricSource(BaseValidatorModel):
    S3SourceConfig: Optional[AutoDetectionS3SourceConfig] = None


# This class is the output for the 'create_alert' function.
class CreateAlertResponse(BaseValidatorModel):
    AlertArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_anomaly_detector' function.
class CreateAnomalyDetectorResponse(BaseValidatorModel):
    AnomalyDetectorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_metric_set' function.
class CreateMetricSetResponse(BaseValidatorModel):
    MetricSetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_anomaly_detector' function.
class DescribeAnomalyDetectorResponse(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyDetectorName: str
    AnomalyDetectorDescription: str
    AnomalyDetectorConfig: AnomalyDetectorConfigSummary
    CreationTime: datetime
    LastModificationTime: datetime
    Status: AnomalyDetectorStatusType
    FailureReason: str
    KmsKeyArn: str
    FailureType: AnomalyDetectorFailureTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sample_data' function.
class GetSampleDataResponse(BaseValidatorModel):
    HeaderValues: List[str]
    SampleRows: List[List[str]]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_alerts' function.
class ListAlertsResponse(BaseValidatorModel):
    AlertSummaryList: List[AlertSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_anomaly_detectors' function.
class ListAnomalyDetectorsResponse(BaseValidatorModel):
    AnomalyDetectorSummaryList: List[AnomalyDetectorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_alert' function.
class UpdateAlertResponse(BaseValidatorModel):
    AlertArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_anomaly_detector' function.
class UpdateAnomalyDetectorResponse(BaseValidatorModel):
    AnomalyDetectorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_metric_set' function.
class UpdateMetricSetResponse(BaseValidatorModel):
    MetricSetArn: str
    ResponseMetadata: ResponseMetadata

CsvFormatDescriptorUnion = Union[CsvFormatDescriptor, CsvFormatDescriptorOutput]


class MetricSetDataQualityMetric(BaseValidatorModel):
    MetricSetArn: Optional[str] = None
    DataQualityMetricList: Optional[List[DataQualityMetric]] = None


# This class is the output for the 'describe_anomaly_detection_executions' function.
class DescribeAnomalyDetectionExecutionsResponse(BaseValidatorModel):
    ExecutionList: List[ExecutionStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DimensionContribution(BaseValidatorModel):
    DimensionName: Optional[str] = None
    DimensionValueContributionList: Optional[List[DimensionValueContribution]] = None


class TimeSeries(BaseValidatorModel):
    TimeSeriesId: str
    DimensionList: List[DimensionNameValue]
    MetricValueList: List[float]


class FileFormatDescriptorOutput(BaseValidatorModel):
    CsvFormatDescriptor: Optional[CsvFormatDescriptorOutput] = None
    JsonFormatDescriptor: Optional[JsonFormatDescriptor] = None


class MetricSetDimensionFilterOutput(BaseValidatorModel):
    Name: Optional[str] = None
    FilterList: Optional[List[Filter]] = None


class MetricSetDimensionFilter(BaseValidatorModel):
    Name: Optional[str] = None
    FilterList: Optional[List[Filter]] = None


# This class is the output for the 'get_feedback' function.
class GetFeedbackResponse(BaseValidatorModel):
    AnomalyGroupTimeSeriesFeedback: List[TimeSeriesFeedback]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_anomaly_group_related_metrics' function.
class ListAnomalyGroupRelatedMetricsResponse(BaseValidatorModel):
    InterMetricImpactList: List[InterMetricImpactDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_metric_sets' function.
class ListMetricSetsResponse(BaseValidatorModel):
    MetricSetSummaryList: List[MetricSetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RDSSourceConfigOutput(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationOutput] = None


class RedshiftSourceConfigOutput(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationOutput] = None


class RDSSourceConfig(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfiguration] = None


class RedshiftSourceConfig(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfiguration] = None


class Alert(BaseValidatorModel):
    Action: Optional[Action] = None
    AlertDescription: Optional[str] = None
    AlertArn: Optional[str] = None
    AnomalyDetectorArn: Optional[str] = None
    AlertName: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    AlertType: Optional[AlertTypeType] = None
    AlertStatus: Optional[AlertStatusType] = None
    LastModificationTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    AlertFilters: Optional[AlertFiltersOutput] = None

AlertFiltersUnion = Union[AlertFilters, AlertFiltersOutput]


# This class is the output for the 'list_anomaly_group_summaries' function.
class ListAnomalyGroupSummariesResponse(BaseValidatorModel):
    AnomalyGroupSummaryList: List[AnomalyGroupSummary]
    AnomalyGroupStatistics: AnomalyGroupStatistics
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DetectedCsvFormatDescriptor(BaseValidatorModel):
    FileCompression: Optional[DetectedField] = None
    Charset: Optional[DetectedField] = None
    ContainsHeader: Optional[DetectedField] = None
    Delimiter: Optional[DetectedField] = None
    HeaderList: Optional[DetectedField] = None
    QuoteSymbol: Optional[DetectedField] = None


class DetectedJsonFormatDescriptor(BaseValidatorModel):
    FileCompression: Optional[DetectedField] = None
    Charset: Optional[DetectedField] = None


# This class is the input for the 'detect_metric_set_config' function.
class DetectMetricSetConfigRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    AutoDetectionMetricSource: AutoDetectionMetricSource


class FileFormatDescriptor(BaseValidatorModel):
    CsvFormatDescriptor: Optional[CsvFormatDescriptorUnion] = None
    JsonFormatDescriptor: Optional[JsonFormatDescriptor] = None


class AnomalyDetectorDataQualityMetric(BaseValidatorModel):
    StartTimestamp: Optional[datetime] = None
    MetricSetDataQualityMetricList: Optional[List[MetricSetDataQualityMetric]] = None


class ContributionMatrix(BaseValidatorModel):
    DimensionContributionList: Optional[List[DimensionContribution]] = None


# This class is the output for the 'list_anomaly_group_time_series' function.
class ListAnomalyGroupTimeSeriesResponse(BaseValidatorModel):
    AnomalyGroupId: str
    MetricName: str
    TimestampList: List[str]
    TimeSeriesList: List[TimeSeries]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class S3SourceConfigOutput(BaseValidatorModel):
    RoleArn: Optional[str] = None
    TemplatedPathList: Optional[List[str]] = None
    HistoricalDataPathList: Optional[List[str]] = None
    FileFormatDescriptor: Optional[FileFormatDescriptorOutput] = None

MetricSetDimensionFilterUnion = Union[MetricSetDimensionFilter, MetricSetDimensionFilterOutput]


# This class is the output for the 'describe_alert' function.
class DescribeAlertResponse(BaseValidatorModel):
    Alert: Alert
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_alert' function.
class CreateAlertRequest(BaseValidatorModel):
    AlertName: str
    AnomalyDetectorArn: str
    Action: Action
    AlertSensitivityThreshold: Optional[int] = None
    AlertDescription: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    AlertFilters: Optional[AlertFiltersUnion] = None


# This class is the input for the 'update_alert' function.
class UpdateAlertRequest(BaseValidatorModel):
    AlertArn: str
    AlertDescription: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    Action: Optional[Action] = None
    AlertFilters: Optional[AlertFiltersUnion] = None


class DetectedFileFormatDescriptor(BaseValidatorModel):
    CsvFormatDescriptor: Optional[DetectedCsvFormatDescriptor] = None
    JsonFormatDescriptor: Optional[DetectedJsonFormatDescriptor] = None

FileFormatDescriptorUnion = Union[FileFormatDescriptor, FileFormatDescriptorOutput]


class S3SourceConfig(BaseValidatorModel):
    RoleArn: Optional[str] = None
    TemplatedPathList: Optional[List[str]] = None
    HistoricalDataPathList: Optional[List[str]] = None
    FileFormatDescriptor: Optional[FileFormatDescriptor] = None


# This class is the output for the 'get_data_quality_metrics' function.
class GetDataQualityMetricsResponse(BaseValidatorModel):
    AnomalyDetectorDataQualityMetricList: List[AnomalyDetectorDataQualityMetric]
    ResponseMetadata: ResponseMetadata


class MetricLevelImpact(BaseValidatorModel):
    MetricName: Optional[str] = None
    NumTimeSeries: Optional[int] = None
    ContributionMatrix: Optional[ContributionMatrix] = None


class MetricSourceOutput(BaseValidatorModel):
    S3SourceConfig: Optional[S3SourceConfigOutput] = None
    AppFlowConfig: Optional[AppFlowConfig] = None
    CloudWatchConfig: Optional[CloudWatchConfig] = None
    RDSSourceConfig: Optional[RDSSourceConfigOutput] = None
    RedshiftSourceConfig: Optional[RedshiftSourceConfigOutput] = None
    AthenaSourceConfig: Optional[AthenaSourceConfig] = None


class DetectedS3SourceConfig(BaseValidatorModel):
    FileFormatDescriptor: Optional[DetectedFileFormatDescriptor] = None


class SampleDataS3SourceConfig(BaseValidatorModel):
    RoleArn: str
    FileFormatDescriptor: FileFormatDescriptorUnion
    TemplatedPathList: Optional[List[str]] = None
    HistoricalDataPathList: Optional[List[str]] = None


class MetricSource(BaseValidatorModel):
    S3SourceConfig: Optional[S3SourceConfig] = None
    AppFlowConfig: Optional[AppFlowConfig] = None
    CloudWatchConfig: Optional[CloudWatchConfig] = None
    RDSSourceConfig: Optional[RDSSourceConfig] = None
    RedshiftSourceConfig: Optional[RedshiftSourceConfig] = None
    AthenaSourceConfig: Optional[AthenaSourceConfig] = None


class AnomalyGroup(BaseValidatorModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    AnomalyGroupScore: Optional[float] = None
    PrimaryMetricName: Optional[str] = None
    MetricLevelImpactList: Optional[List[MetricLevelImpact]] = None


# This class is the output for the 'describe_metric_set' function.
class DescribeMetricSetResponse(BaseValidatorModel):
    MetricSetArn: str
    AnomalyDetectorArn: str
    MetricSetName: str
    MetricSetDescription: str
    CreationTime: datetime
    LastModificationTime: datetime
    Offset: int
    MetricList: List[Metric]
    TimestampColumn: TimestampColumn
    DimensionList: List[str]
    MetricSetFrequency: FrequencyType
    Timezone: str
    MetricSource: MetricSourceOutput
    DimensionFilterList: List[MetricSetDimensionFilterOutput]
    ResponseMetadata: ResponseMetadata


class DetectedMetricSource(BaseValidatorModel):
    S3SourceConfig: Optional[DetectedS3SourceConfig] = None


# This class is the input for the 'get_sample_data' function.
class GetSampleDataRequest(BaseValidatorModel):
    S3SourceConfig: Optional[SampleDataS3SourceConfig] = None

MetricSourceUnion = Union[MetricSource, MetricSourceOutput]


# This class is the output for the 'get_anomaly_group' function.
class GetAnomalyGroupResponse(BaseValidatorModel):
    AnomalyGroup: AnomalyGroup
    ResponseMetadata: ResponseMetadata


class DetectedMetricSetConfig(BaseValidatorModel):
    Offset: Optional[DetectedField] = None
    MetricSetFrequency: Optional[DetectedField] = None
    MetricSource: Optional[DetectedMetricSource] = None


# This class is the input for the 'create_metric_set' function.
class CreateMetricSetRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    MetricSetName: str
    MetricList: List[Metric]
    MetricSource: MetricSourceUnion
    MetricSetDescription: Optional[str] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumn] = None
    DimensionList: Optional[List[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    Timezone: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DimensionFilterList: Optional[List[MetricSetDimensionFilterUnion]] = None


# This class is the input for the 'update_metric_set' function.
class UpdateMetricSetRequest(BaseValidatorModel):
    MetricSetArn: str
    MetricSetDescription: Optional[str] = None
    MetricList: Optional[List[Metric]] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumn] = None
    DimensionList: Optional[List[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    MetricSource: Optional[MetricSourceUnion] = None
    DimensionFilterList: Optional[List[MetricSetDimensionFilterUnion]] = None


# This class is the output for the 'detect_metric_set_config' function.
class DetectMetricSetConfigResponse(BaseValidatorModel):
    DetectedMetricSetConfig: DetectedMetricSetConfig
    ResponseMetadata: ResponseMetadata