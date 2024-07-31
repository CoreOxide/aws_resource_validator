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
from aws_resource_validator.pydantic_models.discovery_constants import *

class AgentConfigurationStatusTypeDef(BaseModel):
    agentId: Optional[str] = None
    operationSucceeded: Optional[bool] = None
    description: Optional[str] = None

class AgentNetworkInfoTypeDef(BaseModel):
    ipAddress: Optional[str] = None
    macAddress: Optional[str] = None

class AssociateConfigurationItemsToApplicationRequestRequestTypeDef(BaseModel):
    applicationConfigurationId: str
    configurationIds: Sequence[str]

class BatchDeleteAgentErrorTypeDef(BaseModel):
    agentId: str
    errorMessage: str
    errorCode: DeleteAgentErrorCodeType

class DeleteAgentTypeDef(BaseModel):
    agentId: str
    force: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeletionWarningTypeDef(BaseModel):
    configurationId: Optional[str] = None
    warningCode: Optional[int] = None
    warningText: Optional[str] = None

class FailedConfigurationTypeDef(BaseModel):
    configurationId: Optional[str] = None
    errorStatusCode: Optional[int] = None
    errorMessage: Optional[str] = None

class BatchDeleteImportDataErrorTypeDef(BaseModel):
    importTaskId: Optional[str] = None
    errorCode: Optional[BatchDeleteImportDataErrorCodeType] = None
    errorDescription: Optional[str] = None

class BatchDeleteImportDataRequestRequestTypeDef(BaseModel):
    importTaskIds: Sequence[str]
    deleteHistory: Optional[bool] = None

class ConfigurationTagTypeDef(BaseModel):
    configurationType: Optional[ConfigurationItemTypeType] = None
    configurationId: Optional[str] = None
    key: Optional[str] = None
    value: Optional[str] = None
    timeOfCreation: Optional[datetime] = None

class ContinuousExportDescriptionTypeDef(BaseModel):
    exportId: Optional[str] = None
    status: Optional[ContinuousExportStatusType] = None
    statusDetail: Optional[str] = None
    s3Bucket: Optional[str] = None
    startTime: Optional[datetime] = None
    stopTime: Optional[datetime] = None
    dataSource: Optional[Literal["AGENT"]] = None
    schemaStorageConfig: Optional[Dict[str, str]] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None

class TagTypeDef(BaseModel):
    key: str
    value: str

class CustomerAgentInfoTypeDef(BaseModel):
    activeAgents: int
    healthyAgents: int
    blackListedAgents: int
    shutdownAgents: int
    unhealthyAgents: int
    totalAgents: int
    unknownAgents: int

class CustomerAgentlessCollectorInfoTypeDef(BaseModel):
    activeAgentlessCollectors: int
    healthyAgentlessCollectors: int
    denyListedAgentlessCollectors: int
    shutdownAgentlessCollectors: int
    unhealthyAgentlessCollectors: int
    totalAgentlessCollectors: int
    unknownAgentlessCollectors: int

class CustomerConnectorInfoTypeDef(BaseModel):
    activeConnectors: int
    healthyConnectors: int
    blackListedConnectors: int
    shutdownConnectors: int
    unhealthyConnectors: int
    totalConnectors: int
    unknownConnectors: int

class CustomerMeCollectorInfoTypeDef(BaseModel):
    activeMeCollectors: int
    healthyMeCollectors: int
    denyListedMeCollectors: int
    shutdownMeCollectors: int
    unhealthyMeCollectors: int
    totalMeCollectors: int
    unknownMeCollectors: int

class DeleteApplicationsRequestRequestTypeDef(BaseModel):
    configurationIds: Sequence[str]

class FilterTypeDef(BaseModel):
    name: str
    values: Sequence[str]
    condition: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeBatchDeleteConfigurationTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class DescribeConfigurationsRequestRequestTypeDef(BaseModel):
    configurationIds: Sequence[str]

class DescribeContinuousExportsRequestRequestTypeDef(BaseModel):
    exportIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeExportConfigurationsRequestRequestTypeDef(BaseModel):
    exportIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ExportInfoTypeDef(BaseModel):
    exportId: str
    exportStatus: ExportStatusType
    statusMessage: str
    exportRequestTime: datetime
    configurationsDownloadUrl: Optional[str] = None
    isTruncated: Optional[bool] = None
    requestedStartTime: Optional[datetime] = None
    requestedEndTime: Optional[datetime] = None

class ExportFilterTypeDef(BaseModel):
    name: str
    values: Sequence[str]
    condition: str

class ImportTaskFilterTypeDef(BaseModel):
    name: Optional[ImportTaskFilterNameType] = None
    values: Optional[Sequence[str]] = None

class ImportTaskTypeDef(BaseModel):
    importTaskId: Optional[str] = None
    clientRequestToken: Optional[str] = None
    name: Optional[str] = None
    importUrl: Optional[str] = None
    status: Optional[ImportStatusType] = None
    importRequestTime: Optional[datetime] = None
    importCompletionTime: Optional[datetime] = None
    importDeletedTime: Optional[datetime] = None
    serverImportSuccess: Optional[int] = None
    serverImportFailure: Optional[int] = None
    applicationImportSuccess: Optional[int] = None
    applicationImportFailure: Optional[int] = None
    errorsAndFailedEntriesZip: Optional[str] = None

class TagFilterTypeDef(BaseModel):
    name: str
    values: Sequence[str]

class DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef(BaseModel):
    applicationConfigurationId: str
    configurationIds: Sequence[str]

class ReservedInstanceOptionsTypeDef(BaseModel):
    purchasingOption: PurchasingOptionType
    offeringClass: OfferingClassType
    termLength: TermLengthType

class UsageMetricBasisTypeDef(BaseModel):
    name: Optional[str] = None
    percentageAdjust: Optional[float] = None

class OrderByElementTypeDef(BaseModel):
    fieldName: str
    sortOrder: Optional[OrderStringType] = None

class ListServerNeighborsRequestRequestTypeDef(BaseModel):
    configurationId: str
    portInformationNeeded: Optional[bool] = None
    neighborConfigurationIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NeighborConnectionDetailTypeDef(BaseModel):
    sourceServerId: str
    destinationServerId: str
    connectionsCount: int
    destinationPort: Optional[int] = None
    transportProtocol: Optional[str] = None

class StartBatchDeleteConfigurationTaskRequestRequestTypeDef(BaseModel):
    configurationType: Literal["SERVER"]
    configurationIds: Sequence[str]

class StartDataCollectionByAgentIdsRequestRequestTypeDef(BaseModel):
    agentIds: Sequence[str]

class StartImportTaskRequestRequestTypeDef(BaseModel):
    name: str
    importUrl: str
    clientRequestToken: Optional[str] = None

class StopContinuousExportRequestRequestTypeDef(BaseModel):
    exportId: str

class StopDataCollectionByAgentIdsRequestRequestTypeDef(BaseModel):
    agentIds: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    configurationId: str
    name: Optional[str] = None
    description: Optional[str] = None

class AgentInfoTypeDef(BaseModel):
    agentId: Optional[str] = None
    hostName: Optional[str] = None
    agentNetworkInfoList: Optional[List[AgentNetworkInfoTypeDef]] = None
    connectorId: Optional[str] = None
    version: Optional[str] = None
    health: Optional[AgentStatusType] = None
    lastHealthPingTime: Optional[str] = None
    collectionStatus: Optional[str] = None
    agentType: Optional[str] = None
    registeredTime: Optional[str] = None

class BatchDeleteAgentsRequestRequestTypeDef(BaseModel):
    deleteAgents: Sequence[DeleteAgentTypeDef]

class BatchDeleteAgentsResponseTypeDef(BaseModel):
    errors: List[BatchDeleteAgentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResponseTypeDef(BaseModel):
    configurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationsResponseTypeDef(BaseModel):
    configurations: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportConfigurationsResponseTypeDef(BaseModel):
    exportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationsResponseTypeDef(BaseModel):
    configurations: List[Dict[str, str]]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartBatchDeleteConfigurationTaskResponseTypeDef(BaseModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContinuousExportResponseTypeDef(BaseModel):
    exportId: str
    s3Bucket: str
    startTime: datetime
    dataSource: Literal["AGENT"]
    schemaStorageConfig: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataCollectionByAgentIdsResponseTypeDef(BaseModel):
    agentsConfigurationStatus: List[AgentConfigurationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartExportTaskResponseTypeDef(BaseModel):
    exportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopContinuousExportResponseTypeDef(BaseModel):
    startTime: datetime
    stopTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopDataCollectionByAgentIdsResponseTypeDef(BaseModel):
    agentsConfigurationStatus: List[AgentConfigurationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteConfigurationTaskTypeDef(BaseModel):
    taskId: Optional[str] = None
    status: Optional[BatchDeleteConfigurationTaskStatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    configurationType: Optional[Literal["SERVER"]] = None
    requestedConfigurations: Optional[List[str]] = None
    deletedConfigurations: Optional[List[str]] = None
    failedConfigurations: Optional[List[FailedConfigurationTypeDef]] = None
    deletionWarnings: Optional[List[DeletionWarningTypeDef]] = None

class BatchDeleteImportDataResponseTypeDef(BaseModel):
    errors: List[BatchDeleteImportDataErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTagsResponseTypeDef(BaseModel):
    tags: List[ConfigurationTagTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContinuousExportsResponseTypeDef(BaseModel):
    descriptions: List[ContinuousExportDescriptionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTagsRequestRequestTypeDef(BaseModel):
    configurationIds: Sequence[str]
    tags: Sequence[TagTypeDef]

class DeleteTagsRequestRequestTypeDef(BaseModel):
    configurationIds: Sequence[str]
    tags: Optional[Sequence[TagTypeDef]] = None

class GetDiscoverySummaryResponseTypeDef(BaseModel):
    servers: int
    applications: int
    serversMappedToApplications: int
    serversMappedtoTags: int
    agentSummary: CustomerAgentInfoTypeDef
    connectorSummary: CustomerConnectorInfoTypeDef
    meCollectorSummary: CustomerMeCollectorInfoTypeDef
    agentlessCollectorSummary: CustomerAgentlessCollectorInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAgentsRequestRequestTypeDef(BaseModel):
    agentIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeAgentsRequestDescribeAgentsPaginateTypeDef(BaseModel):
    agentIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeContinuousExportsRequestDescribeContinuousExportsPaginateTypeDef(BaseModel):
    exportIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateTypeDef(BaseModel):
    exportIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportConfigurationsResponseTypeDef(BaseModel):
    exportsInfo: List[ExportInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportTasksResponseTypeDef(BaseModel):
    exportsInfo: List[ExportInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef(BaseModel):
    exportIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[ExportFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportTasksRequestRequestTypeDef(BaseModel):
    exportIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[ExportFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeImportTasksRequestDescribeImportTasksPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[ImportTaskFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImportTasksRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[ImportTaskFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeImportTasksResponseTypeDef(BaseModel):
    nextToken: str
    tasks: List[ImportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportTaskResponseTypeDef(BaseModel):
    task: ImportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTagsRequestDescribeTagsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[TagFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTagsRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[TagFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class Ec2RecommendationsExportPreferencesTypeDef(BaseModel):
    enabled: Optional[bool] = None
    cpuPerformanceMetricBasis: Optional[UsageMetricBasisTypeDef] = None
    ramPerformanceMetricBasis: Optional[UsageMetricBasisTypeDef] = None
    tenancy: Optional[TenancyType] = None
    excludedInstanceTypes: Optional[Sequence[str]] = None
    preferredRegion: Optional[str] = None
    reservedInstanceOptions: Optional[ReservedInstanceOptionsTypeDef] = None

class ListConfigurationsRequestListConfigurationsPaginateTypeDef(BaseModel):
    configurationType: ConfigurationItemTypeType
    filters: Optional[Sequence[FilterTypeDef]] = None
    orderBy: Optional[Sequence[OrderByElementTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationsRequestRequestTypeDef(BaseModel):
    configurationType: ConfigurationItemTypeType
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    orderBy: Optional[Sequence[OrderByElementTypeDef]] = None

class ListServerNeighborsResponseTypeDef(BaseModel):
    neighbors: List[NeighborConnectionDetailTypeDef]
    nextToken: str
    knownDependencyCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAgentsResponseTypeDef(BaseModel):
    agentsInfo: List[AgentInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBatchDeleteConfigurationTaskResponseTypeDef(BaseModel):
    task: BatchDeleteConfigurationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportPreferencesTypeDef(BaseModel):
    ec2RecommendationsPreferences: Optional[Ec2RecommendationsExportPreferencesTypeDef] = None

class StartExportTaskRequestRequestTypeDef(BaseModel):
    exportDataFormat: Optional[Sequence[Literal["CSV"]]] = None
    filters: Optional[Sequence[ExportFilterTypeDef]] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    preferences: Optional[ExportPreferencesTypeDef] = None

