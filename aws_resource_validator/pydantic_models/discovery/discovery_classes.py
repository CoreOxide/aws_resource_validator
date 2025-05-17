from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.discovery.discovery_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AgentConfigurationStatus(BaseValidatorModel):
    agentId: Optional[str] = None
    operationSucceeded: Optional[bool] = None
    description: Optional[str] = None


class AgentNetworkInfo(BaseValidatorModel):
    ipAddress: Optional[str] = None
    macAddress: Optional[str] = None


class AssociateConfigurationItemsToApplicationRequest(BaseValidatorModel):
    applicationConfigurationId: str
    configurationIds: List[str]


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


# This class is the input for the 'batch_delete_import_data' function.
class BatchDeleteImportDataRequest(BaseValidatorModel):
    importTaskIds: List[str]
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
    dataSource: Optional[Literal['AGENT']] = None
    schemaStorageConfig: Optional[Dict[str, str]] = None


# This class is the input for the 'create_application' function.
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
    configurationIds: List[str]


class Filter(BaseValidatorModel):
    name: str
    values: List[str]
    condition: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_batch_delete_configuration_task' function.
class DescribeBatchDeleteConfigurationTaskRequest(BaseValidatorModel):
    taskId: str


# This class is the input for the 'describe_configurations' function.
class DescribeConfigurationsRequest(BaseValidatorModel):
    configurationIds: List[str]


# This class is the input for the 'describe_continuous_exports' function.
class DescribeContinuousExportsRequest(BaseValidatorModel):
    exportIds: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'describe_export_configurations' function.
class DescribeExportConfigurationsRequest(BaseValidatorModel):
    exportIds: Optional[List[str]] = None
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
    values: List[str]
    condition: str


class ImportTaskFilter(BaseValidatorModel):
    name: Optional[ImportTaskFilterNameType] = None
    values: Optional[List[str]] = None


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
    values: List[str]


class DisassociateConfigurationItemsFromApplicationRequest(BaseValidatorModel):
    applicationConfigurationId: str
    configurationIds: List[str]


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


# This class is the input for the 'list_server_neighbors' function.
class ListServerNeighborsRequest(BaseValidatorModel):
    configurationId: str
    portInformationNeeded: Optional[bool] = None
    neighborConfigurationIds: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NeighborConnectionDetail(BaseValidatorModel):
    sourceServerId: str
    destinationServerId: str
    connectionsCount: int
    destinationPort: Optional[int] = None
    transportProtocol: Optional[str] = None


# This class is the input for the 'start_batch_delete_configuration_task' function.
class StartBatchDeleteConfigurationTaskRequest(BaseValidatorModel):
    configurationType: Literal['SERVER']
    configurationIds: List[str]


# This class is the input for the 'start_data_collection_by_agent_ids' function.
class StartDataCollectionByAgentIdsRequest(BaseValidatorModel):
    agentIds: List[str]

Timestamp = Union[datetime, str]


# This class is the input for the 'start_import_task' function.
class StartImportTaskRequest(BaseValidatorModel):
    name: str
    importUrl: str
    clientRequestToken: Optional[str] = None


# This class is the input for the 'stop_continuous_export' function.
class StopContinuousExportRequest(BaseValidatorModel):
    exportId: str


# This class is the input for the 'stop_data_collection_by_agent_ids' function.
class StopDataCollectionByAgentIdsRequest(BaseValidatorModel):
    agentIds: List[str]


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


# This class is the input for the 'batch_delete_agents' function.
class BatchDeleteAgentsRequest(BaseValidatorModel):
    deleteAgents: List[DeleteAgent]


# This class is the output for the 'batch_delete_agents' function.
class BatchDeleteAgentsResponse(BaseValidatorModel):
    errors: List[BatchDeleteAgentError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_application' function.
class CreateApplicationResponse(BaseValidatorModel):
    configurationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_configurations' function.
class DescribeConfigurationsResponse(BaseValidatorModel):
    configurations: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata


class ExportConfigurationsResponse(BaseValidatorModel):
    exportId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_configurations' function.
class ListConfigurationsResponse(BaseValidatorModel):
    configurations: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_batch_delete_configuration_task' function.
class StartBatchDeleteConfigurationTaskResponse(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


class StartContinuousExportResponse(BaseValidatorModel):
    exportId: str
    s3Bucket: str
    startTime: datetime
    dataSource: Literal['AGENT']
    schemaStorageConfig: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_data_collection_by_agent_ids' function.
class StartDataCollectionByAgentIdsResponse(BaseValidatorModel):
    agentsConfigurationStatus: List[AgentConfigurationStatus]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_export_task' function.
class StartExportTaskResponse(BaseValidatorModel):
    exportId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_continuous_export' function.
class StopContinuousExportResponse(BaseValidatorModel):
    startTime: datetime
    stopTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_data_collection_by_agent_ids' function.
class StopDataCollectionByAgentIdsResponse(BaseValidatorModel):
    agentsConfigurationStatus: List[AgentConfigurationStatus]
    ResponseMetadata: ResponseMetadata


class BatchDeleteConfigurationTask(BaseValidatorModel):
    taskId: Optional[str] = None
    status: Optional[BatchDeleteConfigurationTaskStatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    configurationType: Optional[Literal['SERVER']] = None
    requestedConfigurations: Optional[List[str]] = None
    deletedConfigurations: Optional[List[str]] = None
    failedConfigurations: Optional[List[FailedConfiguration]] = None
    deletionWarnings: Optional[List[DeletionWarning]] = None


# This class is the output for the 'batch_delete_import_data' function.
class BatchDeleteImportDataResponse(BaseValidatorModel):
    errors: List[BatchDeleteImportDataError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_tags' function.
class DescribeTagsResponse(BaseValidatorModel):
    tags: List[ConfigurationTag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_continuous_exports' function.
class DescribeContinuousExportsResponse(BaseValidatorModel):
    descriptions: List[ContinuousExportDescription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateTagsRequest(BaseValidatorModel):
    configurationIds: List[str]
    tags: List[Tag]


class DeleteTagsRequest(BaseValidatorModel):
    configurationIds: List[str]
    tags: Optional[List[Tag]] = None


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


# This class is the input for the 'describe_agents' function.
class DescribeAgentsRequest(BaseValidatorModel):
    agentIds: Optional[List[str]] = None
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeAgentsRequestPaginate(BaseValidatorModel):
    agentIds: Optional[List[str]] = None
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeContinuousExportsRequestPaginate(BaseValidatorModel):
    exportIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeExportConfigurationsRequestPaginate(BaseValidatorModel):
    exportIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_export_configurations' function.
class DescribeExportConfigurationsResponse(BaseValidatorModel):
    exportsInfo: List[ExportInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_export_tasks' function.
class DescribeExportTasksResponse(BaseValidatorModel):
    exportsInfo: List[ExportInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeExportTasksRequestPaginate(BaseValidatorModel):
    exportIds: Optional[List[str]] = None
    filters: Optional[List[ExportFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_export_tasks' function.
class DescribeExportTasksRequest(BaseValidatorModel):
    exportIds: Optional[List[str]] = None
    filters: Optional[List[ExportFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeImportTasksRequestPaginate(BaseValidatorModel):
    filters: Optional[List[ImportTaskFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_import_tasks' function.
class DescribeImportTasksRequest(BaseValidatorModel):
    filters: Optional[List[ImportTaskFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'describe_import_tasks' function.
class DescribeImportTasksResponse(BaseValidatorModel):
    tasks: List[ImportTask]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_import_task' function.
class StartImportTaskResponse(BaseValidatorModel):
    task: ImportTask
    ResponseMetadata: ResponseMetadata


class DescribeTagsRequestPaginate(BaseValidatorModel):
    filters: Optional[List[TagFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsRequest(BaseValidatorModel):
    filters: Optional[List[TagFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class Ec2RecommendationsExportPreferences(BaseValidatorModel):
    enabled: Optional[bool] = None
    cpuPerformanceMetricBasis: Optional[UsageMetricBasis] = None
    ramPerformanceMetricBasis: Optional[UsageMetricBasis] = None
    tenancy: Optional[TenancyType] = None
    excludedInstanceTypes: Optional[List[str]] = None
    preferredRegion: Optional[str] = None
    reservedInstanceOptions: Optional[ReservedInstanceOptions] = None


class ListConfigurationsRequestPaginate(BaseValidatorModel):
    configurationType: ConfigurationItemTypeType
    filters: Optional[List[Filter]] = None
    orderBy: Optional[List[OrderByElement]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_configurations' function.
class ListConfigurationsRequest(BaseValidatorModel):
    configurationType: ConfigurationItemTypeType
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    orderBy: Optional[List[OrderByElement]] = None


# This class is the output for the 'list_server_neighbors' function.
class ListServerNeighborsResponse(BaseValidatorModel):
    neighbors: List[NeighborConnectionDetail]
    knownDependencyCount: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_agents' function.
class DescribeAgentsResponse(BaseValidatorModel):
    agentsInfo: List[AgentInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_batch_delete_configuration_task' function.
class DescribeBatchDeleteConfigurationTaskResponse(BaseValidatorModel):
    task: BatchDeleteConfigurationTask
    ResponseMetadata: ResponseMetadata


class ExportPreferences(BaseValidatorModel):
    ec2RecommendationsPreferences: Optional[Ec2RecommendationsExportPreferences] = None


# This class is the input for the 'start_export_task' function.
class StartExportTaskRequest(BaseValidatorModel):
    exportDataFormat: Optional[List[Literal['CSV']]] = None
    filters: Optional[List[ExportFilter]] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    preferences: Optional[ExportPreferences] = None