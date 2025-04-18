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
from aws_resource_validator.pydantic_models.discovery_constants import *

class AgentConfigurationStatus(BaseValidatorModel):
    agentId: Optional[str] = None
    operationSucceeded: Optional[bool] = None
    description: Optional[str] = None


class AgentNetworkInfo(BaseValidatorModel):
    ipAddress: Optional[str] = None
    macAddress: Optional[str] = None


class AssociateConfigurationItemsToApplicationRequest(BaseValidatorModel):
    applicationConfigurationId: str
    configurationIds: Sequence[str]


class BatchDeleteAgentError(BaseValidatorModel):
    agentId: str
    errorMessage: str
    errorCode: DeleteAgentErrorCodeType


class DeleteAgent(BaseValidatorModel):
    agentId: str
    force: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeletionWarning(BaseValidatorModel):
    configurationId: Optional[str] = None
    warningCode: Optional[int] = None
    warningText: Optional[str] = None


class FailedConfiguration(BaseValidatorModel):
    configurationId: Optional[str] = None
    errorStatusCode: Optional[int] = None
    errorMessage: Optional[str] = None


class BatchDeleteImportDataError(BaseValidatorModel):
    importTaskId: Optional[str] = None
    errorCode: Optional[BatchDeleteImportDataErrorCodeType] = None
    errorDescription: Optional[str] = None


class BatchDeleteImportDataRequest(BaseValidatorModel):
    importTaskIds: Sequence[str]
    deleteHistory: Optional[bool] = None


class ConfigurationTag(BaseValidatorModel):
    configurationType: Optional[ConfigurationItemTypeType] = None
    configurationId: Optional[str] = None
    key: Optional[str] = None
    value: Optional[str] = None
    timeOfCreation: Optional[datetime] = None


class ContinuousExportDescription(BaseValidatorModel):
    exportId: Optional[str] = None
    status: Optional[ContinuousExportStatusType] = None
    statusDetail: Optional[str] = None
    s3Bucket: Optional[str] = None
    startTime: Optional[datetime] = None
    stopTime: Optional[datetime] = None
    dataSource: Optional[Literal["AGENT"]] = None
    schemaStorageConfig: Optional[Dict[str, str]] = None


class CreateApplicationRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    wave: Optional[str] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class CustomerAgentInfo(BaseValidatorModel):
    activeAgents: int
    healthyAgents: int
    blackListedAgents: int
    shutdownAgents: int
    unhealthyAgents: int
    totalAgents: int
    unknownAgents: int


class CustomerAgentlessCollectorInfo(BaseValidatorModel):
    activeAgentlessCollectors: int
    healthyAgentlessCollectors: int
    denyListedAgentlessCollectors: int
    shutdownAgentlessCollectors: int
    unhealthyAgentlessCollectors: int
    totalAgentlessCollectors: int
    unknownAgentlessCollectors: int


class CustomerConnectorInfo(BaseValidatorModel):
    activeConnectors: int
    healthyConnectors: int
    blackListedConnectors: int
    shutdownConnectors: int
    unhealthyConnectors: int
    totalConnectors: int
    unknownConnectors: int


class CustomerMeCollectorInfo(BaseValidatorModel):
    activeMeCollectors: int
    healthyMeCollectors: int
    denyListedMeCollectors: int
    shutdownMeCollectors: int
    unhealthyMeCollectors: int
    totalMeCollectors: int
    unknownMeCollectors: int


class DeleteApplicationsRequest(BaseValidatorModel):
    configurationIds: Sequence[str]


class Filter(BaseValidatorModel):
    name: str
    values: Sequence[str]
    condition: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBatchDeleteConfigurationTaskRequest(BaseValidatorModel):
    taskId: str


class DescribeConfigurationsRequest(BaseValidatorModel):
    configurationIds: Sequence[str]


class DescribeContinuousExportsRequest(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeExportConfigurationsRequest(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ExportInfo(BaseValidatorModel):
    exportId: str
    exportStatus: ExportStatusType
    statusMessage: str
    exportRequestTime: datetime
    configurationsDownloadUrl: Optional[str] = None
    isTruncated: Optional[bool] = None
    requestedStartTime: Optional[datetime] = None
    requestedEndTime: Optional[datetime] = None


class ExportFilter(BaseValidatorModel):
    name: str
    values: Sequence[str]
    condition: str


class ImportTaskFilter(BaseValidatorModel):
    name: Optional[ImportTaskFilterNameType] = None
    values: Optional[Sequence[str]] = None


class ImportTask(BaseValidatorModel):
    importTaskId: Optional[str] = None
    clientRequestToken: Optional[str] = None
    name: Optional[str] = None
    importUrl: Optional[str] = None
    status: Optional[ImportStatusType] = None
    importRequestTime: Optional[datetime] = None
    importCompletionTime: Optional[datetime] = None
    importDeletedTime: Optional[datetime] = None
    fileClassification: Optional[FileClassificationType] = None
    serverImportSuccess: Optional[int] = None
    serverImportFailure: Optional[int] = None
    applicationImportSuccess: Optional[int] = None
    applicationImportFailure: Optional[int] = None
    errorsAndFailedEntriesZip: Optional[str] = None


class TagFilter(BaseValidatorModel):
    name: str
    values: Sequence[str]


class DisassociateConfigurationItemsFromApplicationRequest(BaseValidatorModel):
    applicationConfigurationId: str
    configurationIds: Sequence[str]


class ReservedInstanceOptions(BaseValidatorModel):
    purchasingOption: PurchasingOptionType
    offeringClass: OfferingClassType
    termLength: TermLengthType


class UsageMetricBasis(BaseValidatorModel):
    name: Optional[str] = None
    percentageAdjust: Optional[float] = None


class OrderByElement(BaseValidatorModel):
    fieldName: str
    sortOrder: Optional[OrderStringType] = None


class ListServerNeighborsRequest(BaseValidatorModel):
    configurationId: str
    portInformationNeeded: Optional[bool] = None
    neighborConfigurationIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NeighborConnectionDetail(BaseValidatorModel):
    sourceServerId: str
    destinationServerId: str
    connectionsCount: int
    destinationPort: Optional[int] = None
    transportProtocol: Optional[str] = None


class StartBatchDeleteConfigurationTaskRequest(BaseValidatorModel):
    configurationType: Literal["SERVER"]
    configurationIds: Sequence[str]


class StartDataCollectionByAgentIdsRequest(BaseValidatorModel):
    agentIds: Sequence[str]


class StartImportTaskRequest(BaseValidatorModel):
    name: str
    importUrl: str
    clientRequestToken: Optional[str] = None


class StopContinuousExportRequest(BaseValidatorModel):
    exportId: str


class StopDataCollectionByAgentIdsRequest(BaseValidatorModel):
    agentIds: Sequence[str]


class UpdateApplicationRequest(BaseValidatorModel):
    configurationId: str
    name: Optional[str] = None
    description: Optional[str] = None
    wave: Optional[str] = None


class AgentInfo(BaseValidatorModel):
    agentId: Optional[str] = None
    hostName: Optional[str] = None
    agentNetworkInfoList: Optional[List[AgentNetworkInfo]] = None
    connectorId: Optional[str] = None
    version: Optional[str] = None
    health: Optional[AgentStatusType] = None
    lastHealthPingTime: Optional[str] = None
    collectionStatus: Optional[str] = None
    agentType: Optional[str] = None
    registeredTime: Optional[str] = None


class BatchDeleteAgentsRequest(BaseValidatorModel):
    deleteAgents: Sequence[DeleteAgent]


class BatchDeleteAgentsResponse(BaseValidatorModel):
    errors: List[BatchDeleteAgentError]
    ResponseMetadata: ResponseMetadata


class CreateApplicationResponse(BaseValidatorModel):
    configurationId: str
    ResponseMetadata: ResponseMetadata


class DescribeConfigurationsResponse(BaseValidatorModel):
    configurations: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata


class ExportConfigurationsResponse(BaseValidatorModel):
    exportId: str
    ResponseMetadata: ResponseMetadata


class ListConfigurationsResponse(BaseValidatorModel):
    configurations: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartBatchDeleteConfigurationTaskResponse(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


class StartContinuousExportResponse(BaseValidatorModel):
    exportId: str
    s3Bucket: str
    startTime: datetime
    dataSource: Literal["AGENT"]
    schemaStorageConfig: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartDataCollectionByAgentIdsResponse(BaseValidatorModel):
    agentsConfigurationStatus: List[AgentConfigurationStatus]
    ResponseMetadata: ResponseMetadata


class StartExportTaskResponse(BaseValidatorModel):
    exportId: str
    ResponseMetadata: ResponseMetadata


class StopContinuousExportResponse(BaseValidatorModel):
    startTime: datetime
    stopTime: datetime
    ResponseMetadata: ResponseMetadata


class StopDataCollectionByAgentIdsResponse(BaseValidatorModel):
    agentsConfigurationStatus: List[AgentConfigurationStatus]
    ResponseMetadata: ResponseMetadata


class BatchDeleteConfigurationTask(BaseValidatorModel):
    taskId: Optional[str] = None
    status: Optional[BatchDeleteConfigurationTaskStatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    configurationType: Optional[Literal["SERVER"]] = None
    requestedConfigurations: Optional[List[str]] = None
    deletedConfigurations: Optional[List[str]] = None
    failedConfigurations: Optional[List[FailedConfiguration]] = None
    deletionWarnings: Optional[List[DeletionWarning]] = None


class BatchDeleteImportDataResponse(BaseValidatorModel):
    errors: List[BatchDeleteImportDataError]
    ResponseMetadata: ResponseMetadata


class DescribeTagsResponse(BaseValidatorModel):
    tags: List[ConfigurationTag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeContinuousExportsResponse(BaseValidatorModel):
    descriptions: List[ContinuousExportDescription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateTagsRequest(BaseValidatorModel):
    configurationIds: Sequence[str]
    tags: Sequence[Tag]


class DeleteTagsRequest(BaseValidatorModel):
    configurationIds: Sequence[str]
    tags: Optional[Sequence[Tag]] = None


class GetDiscoverySummaryResponse(BaseValidatorModel):
    servers: int
    applications: int
    serversMappedToApplications: int
    serversMappedtoTags: int
    agentSummary: CustomerAgentInfo
    connectorSummary: CustomerConnectorInfo
    meCollectorSummary: CustomerMeCollectorInfo
    agentlessCollectorSummary: CustomerAgentlessCollectorInfo
    ResponseMetadata: ResponseMetadata


class DescribeAgentsRequest(BaseValidatorModel):
    agentIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeAgentsRequestPaginate(BaseValidatorModel):
    agentIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeContinuousExportsRequestPaginate(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeExportConfigurationsRequestPaginate(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeExportConfigurationsResponse(BaseValidatorModel):
    exportsInfo: List[ExportInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeExportTasksResponse(BaseValidatorModel):
    exportsInfo: List[ExportInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeExportTasksRequestPaginate(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[ExportFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeExportTasksRequest(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[ExportFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeImportTasksRequestPaginate(BaseValidatorModel):
    filters: Optional[Sequence[ImportTaskFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeImportTasksRequest(BaseValidatorModel):
    filters: Optional[Sequence[ImportTaskFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeImportTasksResponse(BaseValidatorModel):
    tasks: List[ImportTask]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartImportTaskResponse(BaseValidatorModel):
    task: ImportTask
    ResponseMetadata: ResponseMetadata


class DescribeTagsRequestPaginate(BaseValidatorModel):
    filters: Optional[Sequence[TagFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTagsRequest(BaseValidatorModel):
    filters: Optional[Sequence[TagFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class Ec2RecommendationsExportPreferences(BaseValidatorModel):
    enabled: Optional[bool] = None
    cpuPerformanceMetricBasis: Optional[UsageMetricBasis] = None
    ramPerformanceMetricBasis: Optional[UsageMetricBasis] = None
    tenancy: Optional[TenancyType] = None
    excludedInstanceTypes: Optional[Sequence[str]] = None
    preferredRegion: Optional[str] = None
    reservedInstanceOptions: Optional[ReservedInstanceOptions] = None


class ListConfigurationsRequestPaginate(BaseValidatorModel):
    configurationType: ConfigurationItemTypeType
    filters: Optional[Sequence[Filter]] = None
    orderBy: Optional[Sequence[OrderByElement]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationsRequest(BaseValidatorModel):
    configurationType: ConfigurationItemTypeType
    filters: Optional[Sequence[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    orderBy: Optional[Sequence[OrderByElement]] = None


class ListServerNeighborsResponse(BaseValidatorModel):
    neighbors: List[NeighborConnectionDetail]
    knownDependencyCount: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeAgentsResponse(BaseValidatorModel):
    agentsInfo: List[AgentInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeBatchDeleteConfigurationTaskResponse(BaseValidatorModel):
    task: BatchDeleteConfigurationTask
    ResponseMetadata: ResponseMetadata


class ExportPreferences(BaseValidatorModel):
    ec2RecommendationsPreferences: Optional[Ec2RecommendationsExportPreferences] = None


class Timestamp(BaseValidatorModel):
    pass


class StartExportTaskRequest(BaseValidatorModel):
    exportDataFormat: Optional[Sequence[Literal["CSV"]]] = None
    filters: Optional[Sequence[ExportFilter]] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    preferences: Optional[ExportPreferences] = None


