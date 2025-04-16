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
from aws_resource_validator.pydantic_models.lookoutmetrics_constants import *

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
    DimensionValueList: Optional[Sequence[str]] = None


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
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None


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
    HeaderList: Optional[Sequence[str]] = None
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


class DescribeAlertRequest(BaseValidatorModel):
    AlertArn: str


class DescribeAnomalyDetectionExecutionsRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    Timestamp: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ExecutionStatus(BaseValidatorModel):
    Timestamp: Optional[str] = None
    Status: Optional[AnomalyDetectionTaskStatusType] = None
    FailureReason: Optional[str] = None


class DescribeAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorArn: str


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
    FilterOperation: Optional[Literal["EQUALS"]] = None


class GetAnomalyGroupRequest(BaseValidatorModel):
    AnomalyGroupId: str
    AnomalyDetectorArn: str


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


class ListAlertsRequest(BaseValidatorModel):
    AnomalyDetectorArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAnomalyDetectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAnomalyGroupRelatedMetricsRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    RelationshipTypeFilter: Optional[RelationshipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAnomalyGroupSummariesRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    SensitivityThreshold: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAnomalyGroupTimeSeriesRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    MetricName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class VpcConfigurationOutput(BaseValidatorModel):
    SubnetIdList: List[str]
    SecurityGroupIdList: List[str]


class VpcConfiguration(BaseValidatorModel):
    SubnetIdList: Sequence[str]
    SecurityGroupIdList: Sequence[str]


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class Action(BaseValidatorModel):
    SNSConfiguration: Optional[SNSConfiguration] = None
    LambdaConfiguration: Optional[LambdaConfiguration] = None


class AlertFiltersOutput(BaseValidatorModel):
    MetricList: Optional[List[str]] = None
    DimensionFilterList: Optional[List[DimensionFilterOutput]] = None


class AlertFilters(BaseValidatorModel):
    MetricList: Optional[Sequence[str]] = None
    DimensionFilterList: Optional[Sequence[DimensionFilter]] = None


class CreateAnomalyDetectorRequest(BaseValidatorModel):
    AnomalyDetectorName: str
    AnomalyDetectorConfig: AnomalyDetectorConfig
    AnomalyDetectorDescription: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


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


class CreateAlertResponse(BaseValidatorModel):
    AlertArn: str
    ResponseMetadata: ResponseMetadata


class CreateAnomalyDetectorResponse(BaseValidatorModel):
    AnomalyDetectorArn: str
    ResponseMetadata: ResponseMetadata


class CreateMetricSetResponse(BaseValidatorModel):
    MetricSetArn: str
    ResponseMetadata: ResponseMetadata


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


class GetSampleDataResponse(BaseValidatorModel):
    HeaderValues: List[str]
    SampleRows: List[List[str]]
    ResponseMetadata: ResponseMetadata


class ListAlertsResponse(BaseValidatorModel):
    AlertSummaryList: List[AlertSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAnomalyDetectorsResponse(BaseValidatorModel):
    AnomalyDetectorSummaryList: List[AnomalyDetectorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateAlertResponse(BaseValidatorModel):
    AlertArn: str
    ResponseMetadata: ResponseMetadata


class UpdateAnomalyDetectorResponse(BaseValidatorModel):
    AnomalyDetectorArn: str
    ResponseMetadata: ResponseMetadata


class UpdateMetricSetResponse(BaseValidatorModel):
    MetricSetArn: str
    ResponseMetadata: ResponseMetadata


class MetricSetDataQualityMetric(BaseValidatorModel):
    MetricSetArn: Optional[str] = None
    DataQualityMetricList: Optional[List[DataQualityMetric]] = None


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
    FilterList: Optional[Sequence[Filter]] = None


class GetFeedbackResponse(BaseValidatorModel):
    AnomalyGroupTimeSeriesFeedback: List[TimeSeriesFeedback]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAnomalyGroupRelatedMetricsResponse(BaseValidatorModel):
    InterMetricImpactList: List[InterMetricImpactDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class DetectMetricSetConfigRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    AutoDetectionMetricSource: AutoDetectionMetricSource


class CsvFormatDescriptorUnion(BaseValidatorModel):
    pass


class FileFormatDescriptor(BaseValidatorModel):
    CsvFormatDescriptor: Optional[CsvFormatDescriptorUnion] = None
    JsonFormatDescriptor: Optional[JsonFormatDescriptor] = None


class AnomalyDetectorDataQualityMetric(BaseValidatorModel):
    StartTimestamp: Optional[datetime] = None
    MetricSetDataQualityMetricList: Optional[List[MetricSetDataQualityMetric]] = None


class ContributionMatrix(BaseValidatorModel):
    DimensionContributionList: Optional[List[DimensionContribution]] = None


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


class DescribeAlertResponse(BaseValidatorModel):
    Alert: Alert
    ResponseMetadata: ResponseMetadata


class AlertFiltersUnion(BaseValidatorModel):
    pass


class CreateAlertRequest(BaseValidatorModel):
    AlertName: str
    AnomalyDetectorArn: str
    Action: Action
    AlertSensitivityThreshold: Optional[int] = None
    AlertDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    AlertFilters: Optional[AlertFiltersUnion] = None


class UpdateAlertRequest(BaseValidatorModel):
    AlertArn: str
    AlertDescription: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    Action: Optional[Action] = None
    AlertFilters: Optional[AlertFiltersUnion] = None


class DetectedFileFormatDescriptor(BaseValidatorModel):
    CsvFormatDescriptor: Optional[DetectedCsvFormatDescriptor] = None
    JsonFormatDescriptor: Optional[DetectedJsonFormatDescriptor] = None


class S3SourceConfig(BaseValidatorModel):
    RoleArn: Optional[str] = None
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None
    FileFormatDescriptor: Optional[FileFormatDescriptor] = None


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


class FileFormatDescriptorUnion(BaseValidatorModel):
    pass


class SampleDataS3SourceConfig(BaseValidatorModel):
    RoleArn: str
    FileFormatDescriptor: FileFormatDescriptorUnion
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None


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


class GetSampleDataRequest(BaseValidatorModel):
    S3SourceConfig: Optional[SampleDataS3SourceConfig] = None


class GetAnomalyGroupResponse(BaseValidatorModel):
    AnomalyGroup: AnomalyGroup
    ResponseMetadata: ResponseMetadata


class DetectedMetricSetConfig(BaseValidatorModel):
    Offset: Optional[DetectedField] = None
    MetricSetFrequency: Optional[DetectedField] = None
    MetricSource: Optional[DetectedMetricSource] = None


class MetricSourceUnion(BaseValidatorModel):
    pass


class MetricSetDimensionFilterUnion(BaseValidatorModel):
    pass


class CreateMetricSetRequest(BaseValidatorModel):
    AnomalyDetectorArn: str
    MetricSetName: str
    MetricList: Sequence[Metric]
    MetricSource: MetricSourceUnion
    MetricSetDescription: Optional[str] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumn] = None
    DimensionList: Optional[Sequence[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    Timezone: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    DimensionFilterList: Optional[Sequence[MetricSetDimensionFilterUnion]] = None


class UpdateMetricSetRequest(BaseValidatorModel):
    MetricSetArn: str
    MetricSetDescription: Optional[str] = None
    MetricList: Optional[Sequence[Metric]] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumn] = None
    DimensionList: Optional[Sequence[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    MetricSource: Optional[MetricSourceUnion] = None
    DimensionFilterList: Optional[Sequence[MetricSetDimensionFilterUnion]] = None


class DetectMetricSetConfigResponse(BaseValidatorModel):
    DetectedMetricSetConfig: DetectedMetricSetConfig
    ResponseMetadata: ResponseMetadata


