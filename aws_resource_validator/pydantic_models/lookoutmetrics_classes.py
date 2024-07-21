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
from aws_resource_validator.pydantic_models.lookoutmetrics_constants import *

class LambdaConfigurationTypeDef(BaseModel):
    RoleArn: str
    LambdaArn: str

class SNSConfigurationTypeDef(BaseModel):
    RoleArn: str
    SnsTopicArn: str
    SnsFormat: Optional[SnsFormatType] = None

class ActivateAnomalyDetectorRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str

class DimensionFilterTypeDef(BaseModel):
    DimensionName: Optional[str] = None
    DimensionValueList: Optional[Sequence[str]] = None

class AlertSummaryTypeDef(BaseModel):
    AlertArn: Optional[str] = None
    AnomalyDetectorArn: Optional[str] = None
    AlertName: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    AlertType: Optional[AlertTypeType] = None
    AlertStatus: Optional[AlertStatusType] = None
    LastModificationTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class AnomalyDetectorConfigSummaryTypeDef(BaseModel):
    AnomalyDetectorFrequency: Optional[FrequencyType] = None

class AnomalyDetectorConfigTypeDef(BaseModel):
    AnomalyDetectorFrequency: Optional[FrequencyType] = None

class AnomalyDetectorSummaryTypeDef(BaseModel):
    AnomalyDetectorArn: Optional[str] = None
    AnomalyDetectorName: Optional[str] = None
    AnomalyDetectorDescription: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    Status: Optional[AnomalyDetectorStatusType] = None
    Tags: Optional[Dict[str, str]] = None

class ItemizedMetricStatsTypeDef(BaseModel):
    MetricName: Optional[str] = None
    OccurrenceCount: Optional[int] = None

class AnomalyGroupSummaryTypeDef(BaseModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    AnomalyGroupScore: Optional[float] = None
    PrimaryMetricName: Optional[str] = None

class AnomalyGroupTimeSeriesFeedbackTypeDef(BaseModel):
    AnomalyGroupId: str
    TimeSeriesId: str
    IsAnomaly: bool

class AnomalyGroupTimeSeriesTypeDef(BaseModel):
    AnomalyGroupId: str
    TimeSeriesId: Optional[str] = None

class AppFlowConfigTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    FlowName: Optional[str] = None

class BackTestConfigurationTypeDef(BaseModel):
    RunBackTestMode: bool

class AttributeValueTypeDef(BaseModel):
    S: Optional[str] = None
    N: Optional[str] = None
    B: Optional[str] = None
    SS: Optional[List[str]] = None
    NS: Optional[List[str]] = None
    BS: Optional[List[str]] = None

class AutoDetectionS3SourceConfigTypeDef(BaseModel):
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None

class BackTestAnomalyDetectorRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class MetricTypeDef(BaseModel):
    MetricName: str
    AggregationFunction: AggregationFunctionType
    Namespace: Optional[str] = None

class TimestampColumnTypeDef(BaseModel):
    ColumnName: Optional[str] = None
    ColumnFormat: Optional[str] = None

class CsvFormatDescriptorTypeDef(BaseModel):
    FileCompression: Optional[CSVFileCompressionType] = None
    Charset: Optional[str] = None
    ContainsHeader: Optional[bool] = None
    Delimiter: Optional[str] = None
    HeaderList: Optional[Sequence[str]] = None
    QuoteSymbol: Optional[str] = None

class DataQualityMetricTypeDef(BaseModel):
    MetricType: Optional[DataQualityMetricTypeType] = None
    MetricDescription: Optional[str] = None
    RelatedColumnName: Optional[str] = None
    MetricValue: Optional[float] = None

class DeactivateAnomalyDetectorRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str

class DeleteAlertRequestRequestTypeDef(BaseModel):
    AlertArn: str

class DeleteAnomalyDetectorRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str

class DescribeAlertRequestRequestTypeDef(BaseModel):
    AlertArn: str

class DescribeAnomalyDetectionExecutionsRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    Timestamp: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ExecutionStatusTypeDef(BaseModel):
    Timestamp: Optional[str] = None
    Status: Optional[AnomalyDetectionTaskStatusType] = None
    FailureReason: Optional[str] = None

class DescribeAnomalyDetectorRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str

class DescribeMetricSetRequestRequestTypeDef(BaseModel):
    MetricSetArn: str

class DimensionValueContributionTypeDef(BaseModel):
    DimensionValue: Optional[str] = None
    ContributionScore: Optional[float] = None

class DimensionNameValueTypeDef(BaseModel):
    DimensionName: str
    DimensionValue: str

class JsonFormatDescriptorTypeDef(BaseModel):
    FileCompression: Optional[JsonFileCompressionType] = None
    Charset: Optional[str] = None

class FilterTypeDef(BaseModel):
    DimensionValue: Optional[str] = None
    FilterOperation: Optional[Literal["EQUALS"]] = None

class GetAnomalyGroupRequestRequestTypeDef(BaseModel):
    AnomalyGroupId: str
    AnomalyDetectorArn: str

class GetDataQualityMetricsRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    MetricSetArn: Optional[str] = None

class TimeSeriesFeedbackTypeDef(BaseModel):
    TimeSeriesId: Optional[str] = None
    IsAnomaly: Optional[bool] = None

class InterMetricImpactDetailsTypeDef(BaseModel):
    MetricName: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    RelationshipType: Optional[RelationshipTypeType] = None
    ContributionPercentage: Optional[float] = None

class ListAlertsRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAnomalyDetectorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAnomalyGroupRelatedMetricsRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    RelationshipTypeFilter: Optional[RelationshipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAnomalyGroupSummariesRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    SensitivityThreshold: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAnomalyGroupTimeSeriesRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    MetricName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMetricSetsRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MetricSetSummaryTypeDef(BaseModel):
    MetricSetArn: Optional[str] = None
    AnomalyDetectorArn: Optional[str] = None
    MetricSetDescription: Optional[str] = None
    MetricSetName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastModificationTime: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class VpcConfigurationTypeDef(BaseModel):
    SubnetIdList: Sequence[str]
    SecurityGroupIdList: Sequence[str]

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class ActionTypeDef(BaseModel):
    SNSConfiguration: Optional[SNSConfigurationTypeDef] = None
    LambdaConfiguration: Optional[LambdaConfigurationTypeDef] = None

class AlertFiltersTypeDef(BaseModel):
    MetricList: Optional[Sequence[str]] = None
    DimensionFilterList: Optional[Sequence[DimensionFilterTypeDef]] = None

class CreateAnomalyDetectorRequestRequestTypeDef(BaseModel):
    AnomalyDetectorName: str
    AnomalyDetectorConfig: AnomalyDetectorConfigTypeDef
    AnomalyDetectorDescription: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateAnomalyDetectorRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    KmsKeyArn: Optional[str] = None
    AnomalyDetectorDescription: Optional[str] = None
    AnomalyDetectorConfig: Optional[AnomalyDetectorConfigTypeDef] = None

class AnomalyGroupStatisticsTypeDef(BaseModel):
    EvaluationStartDate: Optional[str] = None
    TotalCount: Optional[int] = None
    ItemizedMetricStatsList: Optional[List[ItemizedMetricStatsTypeDef]] = None

class PutFeedbackRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesFeedbackTypeDef

class GetFeedbackRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class AthenaSourceConfigTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    DataCatalog: Optional[str] = None
    TableName: Optional[str] = None
    WorkGroupName: Optional[str] = None
    S3ResultsPath: Optional[str] = None
    BackTestConfiguration: Optional[BackTestConfigurationTypeDef] = None

class CloudWatchConfigTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    BackTestConfiguration: Optional[BackTestConfigurationTypeDef] = None

class DetectedFieldTypeDef(BaseModel):
    Value: Optional[AttributeValueTypeDef] = None
    Confidence: Optional[ConfidenceType] = None
    Message: Optional[str] = None

class AutoDetectionMetricSourceTypeDef(BaseModel):
    S3SourceConfig: Optional[AutoDetectionS3SourceConfigTypeDef] = None

class CreateAlertResponseTypeDef(BaseModel):
    AlertArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAnomalyDetectorResponseTypeDef(BaseModel):
    AnomalyDetectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMetricSetResponseTypeDef(BaseModel):
    MetricSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAnomalyDetectorResponseTypeDef(BaseModel):
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

class GetSampleDataResponseTypeDef(BaseModel):
    HeaderValues: List[str]
    SampleRows: List[List[str]]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlertsResponseTypeDef(BaseModel):
    AlertSummaryList: List[AlertSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnomalyDetectorsResponseTypeDef(BaseModel):
    AnomalyDetectorSummaryList: List[AnomalyDetectorSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAlertResponseTypeDef(BaseModel):
    AlertArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnomalyDetectorResponseTypeDef(BaseModel):
    AnomalyDetectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMetricSetResponseTypeDef(BaseModel):
    MetricSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricSetDataQualityMetricTypeDef(BaseModel):
    MetricSetArn: Optional[str] = None
    DataQualityMetricList: Optional[List[DataQualityMetricTypeDef]] = None

class DescribeAnomalyDetectionExecutionsResponseTypeDef(BaseModel):
    ExecutionList: List[ExecutionStatusTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DimensionContributionTypeDef(BaseModel):
    DimensionName: Optional[str] = None
    DimensionValueContributionList: Optional[List[DimensionValueContributionTypeDef]] = None

class TimeSeriesTypeDef(BaseModel):
    TimeSeriesId: str
    DimensionList: List[DimensionNameValueTypeDef]
    MetricValueList: List[float]

class FileFormatDescriptorTypeDef(BaseModel):
    CsvFormatDescriptor: Optional[CsvFormatDescriptorTypeDef] = None
    JsonFormatDescriptor: Optional[JsonFormatDescriptorTypeDef] = None

class MetricSetDimensionFilterTypeDef(BaseModel):
    Name: Optional[str] = None
    FilterList: Optional[Sequence[FilterTypeDef]] = None

class GetFeedbackResponseTypeDef(BaseModel):
    AnomalyGroupTimeSeriesFeedback: List[TimeSeriesFeedbackTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAnomalyGroupRelatedMetricsResponseTypeDef(BaseModel):
    InterMetricImpactList: List[InterMetricImpactDetailsTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetricSetsResponseTypeDef(BaseModel):
    MetricSetSummaryList: List[MetricSetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RDSSourceConfigTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None

class RedshiftSourceConfigTypeDef(BaseModel):
    ClusterIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None

class AlertTypeDef(BaseModel):
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

class CreateAlertRequestRequestTypeDef(BaseModel):
    AlertName: str
    AnomalyDetectorArn: str
    Action: ActionTypeDef
    AlertSensitivityThreshold: Optional[int] = None
    AlertDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    AlertFilters: Optional[AlertFiltersTypeDef] = None

class UpdateAlertRequestRequestTypeDef(BaseModel):
    AlertArn: str
    AlertDescription: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    Action: Optional[ActionTypeDef] = None
    AlertFilters: Optional[AlertFiltersTypeDef] = None

class ListAnomalyGroupSummariesResponseTypeDef(BaseModel):
    AnomalyGroupSummaryList: List[AnomalyGroupSummaryTypeDef]
    AnomalyGroupStatistics: AnomalyGroupStatisticsTypeDef
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectedCsvFormatDescriptorTypeDef(BaseModel):
    FileCompression: Optional[DetectedFieldTypeDef] = None
    Charset: Optional[DetectedFieldTypeDef] = None
    ContainsHeader: Optional[DetectedFieldTypeDef] = None
    Delimiter: Optional[DetectedFieldTypeDef] = None
    HeaderList: Optional[DetectedFieldTypeDef] = None
    QuoteSymbol: Optional[DetectedFieldTypeDef] = None

class DetectedJsonFormatDescriptorTypeDef(BaseModel):
    FileCompression: Optional[DetectedFieldTypeDef] = None
    Charset: Optional[DetectedFieldTypeDef] = None

class DetectMetricSetConfigRequestRequestTypeDef(BaseModel):
    AnomalyDetectorArn: str
    AutoDetectionMetricSource: AutoDetectionMetricSourceTypeDef

class AnomalyDetectorDataQualityMetricTypeDef(BaseModel):
    StartTimestamp: Optional[datetime] = None
    MetricSetDataQualityMetricList: Optional[List[MetricSetDataQualityMetricTypeDef]] = None

class ContributionMatrixTypeDef(BaseModel):
    DimensionContributionList: Optional[List[DimensionContributionTypeDef]] = None

class ListAnomalyGroupTimeSeriesResponseTypeDef(BaseModel):
    AnomalyGroupId: str
    MetricName: str
    TimestampList: List[str]
    NextToken: str
    TimeSeriesList: List[TimeSeriesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class S3SourceConfigTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None
    FileFormatDescriptor: Optional[FileFormatDescriptorTypeDef] = None

class SampleDataS3SourceConfigTypeDef(BaseModel):
    RoleArn: str
    FileFormatDescriptor: FileFormatDescriptorTypeDef
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None

class DescribeAlertResponseTypeDef(BaseModel):
    Alert: AlertTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DetectedFileFormatDescriptorTypeDef(BaseModel):
    CsvFormatDescriptor: Optional[DetectedCsvFormatDescriptorTypeDef] = None
    JsonFormatDescriptor: Optional[DetectedJsonFormatDescriptorTypeDef] = None

class GetDataQualityMetricsResponseTypeDef(BaseModel):
    AnomalyDetectorDataQualityMetricList: List[AnomalyDetectorDataQualityMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricLevelImpactTypeDef(BaseModel):
    MetricName: Optional[str] = None
    NumTimeSeries: Optional[int] = None
    ContributionMatrix: Optional[ContributionMatrixTypeDef] = None

class MetricSourceTypeDef(BaseModel):
    S3SourceConfig: Optional[S3SourceConfigTypeDef] = None
    AppFlowConfig: Optional[AppFlowConfigTypeDef] = None
    CloudWatchConfig: Optional[CloudWatchConfigTypeDef] = None
    RDSSourceConfig: Optional[RDSSourceConfigTypeDef] = None
    RedshiftSourceConfig: Optional[RedshiftSourceConfigTypeDef] = None
    AthenaSourceConfig: Optional[AthenaSourceConfigTypeDef] = None

class GetSampleDataRequestRequestTypeDef(BaseModel):
    S3SourceConfig: Optional[SampleDataS3SourceConfigTypeDef] = None

class DetectedS3SourceConfigTypeDef(BaseModel):
    FileFormatDescriptor: Optional[DetectedFileFormatDescriptorTypeDef] = None

class AnomalyGroupTypeDef(BaseModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    AnomalyGroupScore: Optional[float] = None
    PrimaryMetricName: Optional[str] = None
    MetricLevelImpactList: Optional[List[MetricLevelImpactTypeDef]] = None

class CreateMetricSetRequestRequestTypeDef(BaseModel):
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

class DescribeMetricSetResponseTypeDef(BaseModel):
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

class UpdateMetricSetRequestRequestTypeDef(BaseModel):
    MetricSetArn: str
    MetricSetDescription: Optional[str] = None
    MetricList: Optional[Sequence[MetricTypeDef]] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumnTypeDef] = None
    DimensionList: Optional[Sequence[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    MetricSource: Optional[MetricSourceTypeDef] = None
    DimensionFilterList: Optional[Sequence[MetricSetDimensionFilterTypeDef]] = None

class DetectedMetricSourceTypeDef(BaseModel):
    S3SourceConfig: Optional[DetectedS3SourceConfigTypeDef] = None

class GetAnomalyGroupResponseTypeDef(BaseModel):
    AnomalyGroup: AnomalyGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DetectedMetricSetConfigTypeDef(BaseModel):
    Offset: Optional[DetectedFieldTypeDef] = None
    MetricSetFrequency: Optional[DetectedFieldTypeDef] = None
    MetricSource: Optional[DetectedMetricSourceTypeDef] = None

class DetectMetricSetConfigResponseTypeDef(BaseModel):
    DetectedMetricSetConfig: DetectedMetricSetConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

