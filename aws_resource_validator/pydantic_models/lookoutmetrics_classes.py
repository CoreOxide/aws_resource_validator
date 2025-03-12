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

class LambdaConfigurationTypeDef(BaseValidatorModel):
    RoleArn: str
    LambdaArn: str


class SNSConfigurationTypeDef(BaseValidatorModel):
    RoleArn: str
    SnsTopicArn: str
    SnsFormat: Optional[SnsFormatType] = None


class ActivateAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str


class DimensionFilterOutputTypeDef(BaseValidatorModel):
    DimensionName: Optional[str] = None
    DimensionValueList: Optional[List[str]] = None


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


class BackTestAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MetricTypeDef(BaseValidatorModel):
    MetricName: str
    AggregationFunction: AggregationFunctionType
    Namespace: Optional[str] = None


class TimestampColumnTypeDef(BaseValidatorModel):
    ColumnName: Optional[str] = None
    ColumnFormat: Optional[str] = None


class CsvFormatDescriptorOutputTypeDef(BaseValidatorModel):
    FileCompression: Optional[CSVFileCompressionType] = None
    Charset: Optional[str] = None
    ContainsHeader: Optional[bool] = None
    Delimiter: Optional[str] = None
    HeaderList: Optional[List[str]] = None
    QuoteSymbol: Optional[str] = None


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


class DeactivateAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str


class DeleteAlertRequestTypeDef(BaseValidatorModel):
    AlertArn: str


class DeleteAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str


class DescribeAlertRequestTypeDef(BaseValidatorModel):
    AlertArn: str


class DescribeAnomalyDetectionExecutionsRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    Timestamp: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ExecutionStatusTypeDef(BaseValidatorModel):
    Timestamp: Optional[str] = None
    Status: Optional[AnomalyDetectionTaskStatusType] = None
    FailureReason: Optional[str] = None


class DescribeAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str


class DescribeMetricSetRequestTypeDef(BaseValidatorModel):
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


class GetAnomalyGroupRequestTypeDef(BaseValidatorModel):
    AnomalyGroupId: str
    AnomalyDetectorArn: str


class GetDataQualityMetricsRequestTypeDef(BaseValidatorModel):
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


class ListAlertsRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAnomalyDetectorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAnomalyGroupRelatedMetricsRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    RelationshipTypeFilter: Optional[RelationshipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAnomalyGroupSummariesRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    SensitivityThreshold: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAnomalyGroupTimeSeriesRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupId: str
    MetricName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMetricSetsRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class VpcConfigurationOutputTypeDef(BaseValidatorModel):
    SubnetIdList: List[str]
    SecurityGroupIdList: List[str]


class VpcConfigurationTypeDef(BaseValidatorModel):
    SubnetIdList: Sequence[str]
    SecurityGroupIdList: Sequence[str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class ActionTypeDef(BaseValidatorModel):
    SNSConfiguration: Optional[SNSConfigurationTypeDef] = None
    LambdaConfiguration: Optional[LambdaConfigurationTypeDef] = None


class AlertFiltersOutputTypeDef(BaseValidatorModel):
    MetricList: Optional[List[str]] = None
    DimensionFilterList: Optional[List[DimensionFilterOutputTypeDef]] = None


class AlertFiltersTypeDef(BaseValidatorModel):
    MetricList: Optional[Sequence[str]] = None
    DimensionFilterList: Optional[Sequence[DimensionFilterTypeDef]] = None


class CreateAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorName: str
    AnomalyDetectorConfig: AnomalyDetectorConfigTypeDef
    AnomalyDetectorDescription: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    KmsKeyArn: Optional[str] = None
    AnomalyDetectorDescription: Optional[str] = None
    AnomalyDetectorConfig: Optional[AnomalyDetectorConfigTypeDef] = None


class AnomalyGroupStatisticsTypeDef(BaseValidatorModel):
    EvaluationStartDate: Optional[str] = None
    TotalCount: Optional[int] = None
    ItemizedMetricStatsList: Optional[List[ItemizedMetricStatsTypeDef]] = None


class PutFeedbackRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesFeedbackTypeDef


class GetFeedbackRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAnomalyDetectorsResponseTypeDef(BaseValidatorModel):
    AnomalyDetectorSummaryList: List[AnomalyDetectorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DimensionContributionTypeDef(BaseValidatorModel):
    DimensionName: Optional[str] = None
    DimensionValueContributionList: Optional[List[DimensionValueContributionTypeDef]] = None


class TimeSeriesTypeDef(BaseValidatorModel):
    TimeSeriesId: str
    DimensionList: List[DimensionNameValueTypeDef]
    MetricValueList: List[float]


class FileFormatDescriptorOutputTypeDef(BaseValidatorModel):
    CsvFormatDescriptor: Optional[CsvFormatDescriptorOutputTypeDef] = None
    JsonFormatDescriptor: Optional[JsonFormatDescriptorTypeDef] = None


class MetricSetDimensionFilterOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    FilterList: Optional[List[FilterTypeDef]] = None


class MetricSetDimensionFilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    FilterList: Optional[Sequence[FilterTypeDef]] = None


class GetFeedbackResponseTypeDef(BaseValidatorModel):
    AnomalyGroupTimeSeriesFeedback: List[TimeSeriesFeedbackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAnomalyGroupRelatedMetricsResponseTypeDef(BaseValidatorModel):
    InterMetricImpactList: List[InterMetricImpactDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMetricSetsResponseTypeDef(BaseValidatorModel):
    MetricSetSummaryList: List[MetricSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RDSSourceConfigOutputTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationOutputTypeDef] = None


class RedshiftSourceConfigOutputTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    DatabaseHost: Optional[str] = None
    DatabasePort: Optional[int] = None
    SecretManagerArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    RoleArn: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationOutputTypeDef] = None


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
    AlertFilters: Optional[AlertFiltersOutputTypeDef] = None


class ListAnomalyGroupSummariesResponseTypeDef(BaseValidatorModel):
    AnomalyGroupSummaryList: List[AnomalyGroupSummaryTypeDef]
    AnomalyGroupStatistics: AnomalyGroupStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class DetectMetricSetConfigRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    AutoDetectionMetricSource: AutoDetectionMetricSourceTypeDef


class CsvFormatDescriptorUnionTypeDef(BaseValidatorModel):
    pass


class FileFormatDescriptorTypeDef(BaseValidatorModel):
    CsvFormatDescriptor: Optional[CsvFormatDescriptorUnionTypeDef] = None
    JsonFormatDescriptor: Optional[JsonFormatDescriptorTypeDef] = None


class AnomalyDetectorDataQualityMetricTypeDef(BaseValidatorModel):
    StartTimestamp: Optional[datetime] = None
    MetricSetDataQualityMetricList: Optional[List[MetricSetDataQualityMetricTypeDef]] = None


class ContributionMatrixTypeDef(BaseValidatorModel):
    DimensionContributionList: Optional[List[DimensionContributionTypeDef]] = None


class ListAnomalyGroupTimeSeriesResponseTypeDef(BaseValidatorModel):
    AnomalyGroupId: str
    MetricName: str
    TimestampList: List[str]
    TimeSeriesList: List[TimeSeriesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class S3SourceConfigOutputTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    TemplatedPathList: Optional[List[str]] = None
    HistoricalDataPathList: Optional[List[str]] = None
    FileFormatDescriptor: Optional[FileFormatDescriptorOutputTypeDef] = None


class DescribeAlertResponseTypeDef(BaseValidatorModel):
    Alert: AlertTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AlertFiltersUnionTypeDef(BaseValidatorModel):
    pass


class CreateAlertRequestTypeDef(BaseValidatorModel):
    AlertName: str
    AnomalyDetectorArn: str
    Action: ActionTypeDef
    AlertSensitivityThreshold: Optional[int] = None
    AlertDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    AlertFilters: Optional[AlertFiltersUnionTypeDef] = None


class UpdateAlertRequestTypeDef(BaseValidatorModel):
    AlertArn: str
    AlertDescription: Optional[str] = None
    AlertSensitivityThreshold: Optional[int] = None
    Action: Optional[ActionTypeDef] = None
    AlertFilters: Optional[AlertFiltersUnionTypeDef] = None


class DetectedFileFormatDescriptorTypeDef(BaseValidatorModel):
    CsvFormatDescriptor: Optional[DetectedCsvFormatDescriptorTypeDef] = None
    JsonFormatDescriptor: Optional[DetectedJsonFormatDescriptorTypeDef] = None


class S3SourceConfigTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None
    FileFormatDescriptor: Optional[FileFormatDescriptorTypeDef] = None


class GetDataQualityMetricsResponseTypeDef(BaseValidatorModel):
    AnomalyDetectorDataQualityMetricList: List[AnomalyDetectorDataQualityMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class MetricLevelImpactTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    NumTimeSeries: Optional[int] = None
    ContributionMatrix: Optional[ContributionMatrixTypeDef] = None


class MetricSourceOutputTypeDef(BaseValidatorModel):
    S3SourceConfig: Optional[S3SourceConfigOutputTypeDef] = None
    AppFlowConfig: Optional[AppFlowConfigTypeDef] = None
    CloudWatchConfig: Optional[CloudWatchConfigTypeDef] = None
    RDSSourceConfig: Optional[RDSSourceConfigOutputTypeDef] = None
    RedshiftSourceConfig: Optional[RedshiftSourceConfigOutputTypeDef] = None
    AthenaSourceConfig: Optional[AthenaSourceConfigTypeDef] = None


class DetectedS3SourceConfigTypeDef(BaseValidatorModel):
    FileFormatDescriptor: Optional[DetectedFileFormatDescriptorTypeDef] = None


class FileFormatDescriptorUnionTypeDef(BaseValidatorModel):
    pass


class SampleDataS3SourceConfigTypeDef(BaseValidatorModel):
    RoleArn: str
    FileFormatDescriptor: FileFormatDescriptorUnionTypeDef
    TemplatedPathList: Optional[Sequence[str]] = None
    HistoricalDataPathList: Optional[Sequence[str]] = None


class MetricSourceTypeDef(BaseValidatorModel):
    S3SourceConfig: Optional[S3SourceConfigTypeDef] = None
    AppFlowConfig: Optional[AppFlowConfigTypeDef] = None
    CloudWatchConfig: Optional[CloudWatchConfigTypeDef] = None
    RDSSourceConfig: Optional[RDSSourceConfigTypeDef] = None
    RedshiftSourceConfig: Optional[RedshiftSourceConfigTypeDef] = None
    AthenaSourceConfig: Optional[AthenaSourceConfigTypeDef] = None


class AnomalyGroupTypeDef(BaseValidatorModel):
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    AnomalyGroupId: Optional[str] = None
    AnomalyGroupScore: Optional[float] = None
    PrimaryMetricName: Optional[str] = None
    MetricLevelImpactList: Optional[List[MetricLevelImpactTypeDef]] = None


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
    MetricSource: MetricSourceOutputTypeDef
    DimensionFilterList: List[MetricSetDimensionFilterOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DetectedMetricSourceTypeDef(BaseValidatorModel):
    S3SourceConfig: Optional[DetectedS3SourceConfigTypeDef] = None


class GetSampleDataRequestTypeDef(BaseValidatorModel):
    S3SourceConfig: Optional[SampleDataS3SourceConfigTypeDef] = None


class GetAnomalyGroupResponseTypeDef(BaseValidatorModel):
    AnomalyGroup: AnomalyGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DetectedMetricSetConfigTypeDef(BaseValidatorModel):
    Offset: Optional[DetectedFieldTypeDef] = None
    MetricSetFrequency: Optional[DetectedFieldTypeDef] = None
    MetricSource: Optional[DetectedMetricSourceTypeDef] = None


class MetricSourceUnionTypeDef(BaseValidatorModel):
    pass


class MetricSetDimensionFilterUnionTypeDef(BaseValidatorModel):
    pass


class CreateMetricSetRequestTypeDef(BaseValidatorModel):
    AnomalyDetectorArn: str
    MetricSetName: str
    MetricList: Sequence[MetricTypeDef]
    MetricSource: MetricSourceUnionTypeDef
    MetricSetDescription: Optional[str] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumnTypeDef] = None
    DimensionList: Optional[Sequence[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    Timezone: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    DimensionFilterList: Optional[Sequence[MetricSetDimensionFilterUnionTypeDef]] = None


class UpdateMetricSetRequestTypeDef(BaseValidatorModel):
    MetricSetArn: str
    MetricSetDescription: Optional[str] = None
    MetricList: Optional[Sequence[MetricTypeDef]] = None
    Offset: Optional[int] = None
    TimestampColumn: Optional[TimestampColumnTypeDef] = None
    DimensionList: Optional[Sequence[str]] = None
    MetricSetFrequency: Optional[FrequencyType] = None
    MetricSource: Optional[MetricSourceUnionTypeDef] = None
    DimensionFilterList: Optional[Sequence[MetricSetDimensionFilterUnionTypeDef]] = None


class DetectMetricSetConfigResponseTypeDef(BaseValidatorModel):
    DetectedMetricSetConfig: DetectedMetricSetConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


