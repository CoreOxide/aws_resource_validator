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

class AgentConfigurationStatusTypeDef(BaseValidatorModel):
    agentId: Optional[str] = None
    operationSucceeded: Optional[bool] = None
    description: Optional[str] = None


class AgentNetworkInfoTypeDef(BaseValidatorModel):
    ipAddress: Optional[str] = None
    macAddress: Optional[str] = None


class AssociateConfigurationItemsToApplicationRequestTypeDef(BaseValidatorModel):
    applicationConfigurationId: str
    configurationIds: Sequence[str]


class BatchDeleteAgentErrorTypeDef(BaseValidatorModel):
    agentId: str
    errorMessage: str
    errorCode: DeleteAgentErrorCodeType


class DeleteAgentTypeDef(BaseValidatorModel):
    agentId: str
    force: Optional[bool] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeletionWarningTypeDef(BaseValidatorModel):
    configurationId: Optional[str] = None
    warningCode: Optional[int] = None
    warningText: Optional[str] = None


class FailedConfigurationTypeDef(BaseValidatorModel):
    configurationId: Optional[str] = None
    errorStatusCode: Optional[int] = None
    errorMessage: Optional[str] = None


class BatchDeleteImportDataErrorTypeDef(BaseValidatorModel):
    importTaskId: Optional[str] = None
    errorCode: Optional[BatchDeleteImportDataErrorCodeType] = None
    errorDescription: Optional[str] = None


class BatchDeleteImportDataRequestTypeDef(BaseValidatorModel):
    importTaskIds: Sequence[str]
    deleteHistory: Optional[bool] = None


class ConfigurationTagTypeDef(BaseValidatorModel):
    configurationType: Optional[ConfigurationItemTypeType] = None
    configurationId: Optional[str] = None
    key: Optional[str] = None
    value: Optional[str] = None
    timeOfCreation: Optional[datetime] = None


class ContinuousExportDescriptionTypeDef(BaseValidatorModel):
    exportId: Optional[str] = None
    status: Optional[ContinuousExportStatusType] = None
    statusDetail: Optional[str] = None
    s3Bucket: Optional[str] = None
    startTime: Optional[datetime] = None
    stopTime: Optional[datetime] = None
    dataSource: Optional[Literal["AGENT"]] = None
    schemaStorageConfig: Optional[Dict[str, str]] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    wave: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class CustomerAgentInfoTypeDef(BaseValidatorModel):
    activeAgents: int
    healthyAgents: int
    blackListedAgents: int
    shutdownAgents: int
    unhealthyAgents: int
    totalAgents: int
    unknownAgents: int


class CustomerAgentlessCollectorInfoTypeDef(BaseValidatorModel):
    activeAgentlessCollectors: int
    healthyAgentlessCollectors: int
    denyListedAgentlessCollectors: int
    shutdownAgentlessCollectors: int
    unhealthyAgentlessCollectors: int
    totalAgentlessCollectors: int
    unknownAgentlessCollectors: int


class CustomerConnectorInfoTypeDef(BaseValidatorModel):
    activeConnectors: int
    healthyConnectors: int
    blackListedConnectors: int
    shutdownConnectors: int
    unhealthyConnectors: int
    totalConnectors: int
    unknownConnectors: int


class CustomerMeCollectorInfoTypeDef(BaseValidatorModel):
    activeMeCollectors: int
    healthyMeCollectors: int
    denyListedMeCollectors: int
    shutdownMeCollectors: int
    unhealthyMeCollectors: int
    totalMeCollectors: int
    unknownMeCollectors: int


class DeleteApplicationsRequestTypeDef(BaseValidatorModel):
    configurationIds: Sequence[str]


class FilterTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[str]
    condition: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBatchDeleteConfigurationTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class DescribeConfigurationsRequestTypeDef(BaseValidatorModel):
    configurationIds: Sequence[str]


class DescribeContinuousExportsRequestTypeDef(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeExportConfigurationsRequestTypeDef(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ExportInfoTypeDef(BaseValidatorModel):
    exportId: str
    exportStatus: ExportStatusType
    statusMessage: str
    exportRequestTime: datetime
    configurationsDownloadUrl: Optional[str] = None
    isTruncated: Optional[bool] = None
    requestedStartTime: Optional[datetime] = None
    requestedEndTime: Optional[datetime] = None


class ExportFilterTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[str]
    condition: str


class ImportTaskFilterTypeDef(BaseValidatorModel):
    name: Optional[ImportTaskFilterNameType] = None
    values: Optional[Sequence[str]] = None


class ImportTaskTypeDef(BaseValidatorModel):
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


class TagFilterTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[str]


class DisassociateConfigurationItemsFromApplicationRequestTypeDef(BaseValidatorModel):
    applicationConfigurationId: str
    configurationIds: Sequence[str]


class ReservedInstanceOptionsTypeDef(BaseValidatorModel):
    purchasingOption: PurchasingOptionType
    offeringClass: OfferingClassType
    termLength: TermLengthType


class UsageMetricBasisTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    percentageAdjust: Optional[float] = None


class OrderByElementTypeDef(BaseValidatorModel):
    fieldName: str
    sortOrder: Optional[OrderStringType] = None


class ListServerNeighborsRequestTypeDef(BaseValidatorModel):
    configurationId: str
    portInformationNeeded: Optional[bool] = None
    neighborConfigurationIds: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NeighborConnectionDetailTypeDef(BaseValidatorModel):
    sourceServerId: str
    destinationServerId: str
    connectionsCount: int
    destinationPort: Optional[int] = None
    transportProtocol: Optional[str] = None


class StartBatchDeleteConfigurationTaskRequestTypeDef(BaseValidatorModel):
    configurationType: Literal["SERVER"]
    configurationIds: Sequence[str]


class StartDataCollectionByAgentIdsRequestTypeDef(BaseValidatorModel):
    agentIds: Sequence[str]


class StartImportTaskRequestTypeDef(BaseValidatorModel):
    name: str
    importUrl: str
    clientRequestToken: Optional[str] = None


class StopContinuousExportRequestTypeDef(BaseValidatorModel):
    exportId: str


class StopDataCollectionByAgentIdsRequestTypeDef(BaseValidatorModel):
    agentIds: Sequence[str]


class UpdateApplicationRequestTypeDef(BaseValidatorModel):
    configurationId: str
    name: Optional[str] = None
    description: Optional[str] = None
    wave: Optional[str] = None


class AgentInfoTypeDef(BaseValidatorModel):
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


class BatchDeleteAgentsRequestTypeDef(BaseValidatorModel):
    deleteAgents: Sequence[DeleteAgentTypeDef]


class BatchDeleteAgentsResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteAgentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateApplicationResponseTypeDef(BaseValidatorModel):
    configurationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConfigurationsResponseTypeDef(BaseValidatorModel):
    configurations: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef


class ExportConfigurationsResponseTypeDef(BaseValidatorModel):
    exportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigurationsResponseTypeDef(BaseValidatorModel):
    configurations: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartBatchDeleteConfigurationTaskResponseTypeDef(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartContinuousExportResponseTypeDef(BaseValidatorModel):
    exportId: str
    s3Bucket: str
    startTime: datetime
    dataSource: Literal["AGENT"]
    schemaStorageConfig: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartDataCollectionByAgentIdsResponseTypeDef(BaseValidatorModel):
    agentsConfigurationStatus: List[AgentConfigurationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartExportTaskResponseTypeDef(BaseValidatorModel):
    exportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StopContinuousExportResponseTypeDef(BaseValidatorModel):
    startTime: datetime
    stopTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class StopDataCollectionByAgentIdsResponseTypeDef(BaseValidatorModel):
    agentsConfigurationStatus: List[AgentConfigurationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteConfigurationTaskTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    status: Optional[BatchDeleteConfigurationTaskStatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    configurationType: Optional[Literal["SERVER"]] = None
    requestedConfigurations: Optional[List[str]] = None
    deletedConfigurations: Optional[List[str]] = None
    failedConfigurations: Optional[List[FailedConfigurationTypeDef]] = None
    deletionWarnings: Optional[List[DeletionWarningTypeDef]] = None


class BatchDeleteImportDataResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteImportDataErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTagsResponseTypeDef(BaseValidatorModel):
    tags: List[ConfigurationTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeContinuousExportsResponseTypeDef(BaseValidatorModel):
    descriptions: List[ContinuousExportDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateTagsRequestTypeDef(BaseValidatorModel):
    configurationIds: Sequence[str]
    tags: Sequence[TagTypeDef]


class DeleteTagsRequestTypeDef(BaseValidatorModel):
    configurationIds: Sequence[str]
    tags: Optional[Sequence[TagTypeDef]] = None


class GetDiscoverySummaryResponseTypeDef(BaseValidatorModel):
    servers: int
    applications: int
    serversMappedToApplications: int
    serversMappedtoTags: int
    agentSummary: CustomerAgentInfoTypeDef
    connectorSummary: CustomerConnectorInfoTypeDef
    meCollectorSummary: CustomerMeCollectorInfoTypeDef
    agentlessCollectorSummary: CustomerAgentlessCollectorInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAgentsRequestTypeDef(BaseValidatorModel):
    agentIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeAgentsRequestPaginateTypeDef(BaseValidatorModel):
    agentIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeContinuousExportsRequestPaginateTypeDef(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeExportConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeExportConfigurationsResponseTypeDef(BaseValidatorModel):
    exportsInfo: List[ExportInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeExportTasksResponseTypeDef(BaseValidatorModel):
    exportsInfo: List[ExportInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeExportTasksRequestPaginateTypeDef(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[ExportFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeExportTasksRequestTypeDef(BaseValidatorModel):
    exportIds: Optional[Sequence[str]] = None
    filters: Optional[Sequence[ExportFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeImportTasksRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ImportTaskFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeImportTasksRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ImportTaskFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeImportTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[ImportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartImportTaskResponseTypeDef(BaseValidatorModel):
    task: ImportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTagsRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[TagFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTagsRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[TagFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class Ec2RecommendationsExportPreferencesTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    cpuPerformanceMetricBasis: Optional[UsageMetricBasisTypeDef] = None
    ramPerformanceMetricBasis: Optional[UsageMetricBasisTypeDef] = None
    tenancy: Optional[TenancyType] = None
    excludedInstanceTypes: Optional[Sequence[str]] = None
    preferredRegion: Optional[str] = None
    reservedInstanceOptions: Optional[ReservedInstanceOptionsTypeDef] = None


class ListConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    configurationType: ConfigurationItemTypeType
    filters: Optional[Sequence[FilterTypeDef]] = None
    orderBy: Optional[Sequence[OrderByElementTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfigurationsRequestTypeDef(BaseValidatorModel):
    configurationType: ConfigurationItemTypeType
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    orderBy: Optional[Sequence[OrderByElementTypeDef]] = None


class ListServerNeighborsResponseTypeDef(BaseValidatorModel):
    neighbors: List[NeighborConnectionDetailTypeDef]
    knownDependencyCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeAgentsResponseTypeDef(BaseValidatorModel):
    agentsInfo: List[AgentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeBatchDeleteConfigurationTaskResponseTypeDef(BaseValidatorModel):
    task: BatchDeleteConfigurationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportPreferencesTypeDef(BaseValidatorModel):
    ec2RecommendationsPreferences: Optional[Ec2RecommendationsExportPreferencesTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class StartExportTaskRequestTypeDef(BaseValidatorModel):
    exportDataFormat: Optional[Sequence[Literal["CSV"]]] = None
    filters: Optional[Sequence[ExportFilterTypeDef]] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    preferences: Optional[ExportPreferencesTypeDef] = None


