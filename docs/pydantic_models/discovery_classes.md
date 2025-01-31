# discovery_classes

# AgentConfigurationStatusTypeDef

### agentId
- **Type**: typing.Optional[str]

### operationSucceeded
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# AgentInfoTypeDef

### agentId
- **Type**: typing.Optional[str]

### hostName
- **Type**: typing.Optional[str]

### agentNetworkInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery_classes.AgentNetworkInfoTypeDef]]

### connectorId
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### health
- **Type**: typing.Optional[typing.Literal['BLACKLISTED', 'HEALTHY', 'RUNNING', 'SHUTDOWN', 'UNHEALTHY', 'UNKNOWN']]

### lastHealthPingTime
- **Type**: typing.Optional[str]

### collectionStatus
- **Type**: typing.Optional[str]

### agentType
- **Type**: typing.Optional[str]

### registeredTime
- **Type**: typing.Optional[str]


# AgentNetworkInfoTypeDef

### ipAddress
- **Type**: typing.Optional[str]

### macAddress
- **Type**: typing.Optional[str]


# AssociateConfigurationItemsToApplicationRequestRequestTypeDef

### applicationConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### configurationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteAgentErrorTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### errorCode
- **Type**: typing.Literal['AGENT_IN_USE', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND']
- **Required**: Yes


# BatchDeleteAgentsRequestRequestTypeDef

### deleteAgents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.DeleteAgentTypeDef]
- **Required**: Yes


# BatchDeleteAgentsResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.BatchDeleteAgentErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteConfigurationTaskTypeDef

### taskId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETING', 'FAILED', 'INITIALIZING', 'VALIDATING']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### configurationType
- **Type**: typing.Optional[typing.Literal['SERVER']]

### requestedConfigurations
- **Type**: typing.Optional[typing.List[str]]

### deletedConfigurations
- **Type**: typing.Optional[typing.List[str]]

### failedConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery_classes.FailedConfigurationTypeDef]]

### deletionWarnings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery_classes.DeletionWarningTypeDef]]


# BatchDeleteImportDataErrorTypeDef

### importTaskId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['INTERNAL_SERVER_ERROR', 'NOT_FOUND', 'OVER_LIMIT']]

### errorDescription
- **Type**: typing.Optional[str]


# BatchDeleteImportDataRequestRequestTypeDef

### importTaskIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### deleteHistory
- **Type**: typing.Optional[bool]


# BatchDeleteImportDataResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.BatchDeleteImportDataErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigurationTagTypeDef

### configurationType
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'CONNECTION', 'PROCESS', 'SERVER']]

### configurationId
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### timeOfCreation
- **Type**: typing.Optional[datetime.datetime]


# ContinuousExportDescriptionTypeDef

### exportId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'START_FAILED', 'START_IN_PROGRESS', 'STOP_FAILED', 'STOP_IN_PROGRESS']]

### statusDetail
- **Type**: typing.Optional[str]

### s3Bucket
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### stopTime
- **Type**: typing.Optional[datetime.datetime]

### dataSource
- **Type**: typing.Optional[typing.Literal['AGENT']]

### schemaStorageConfig
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateApplicationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateApplicationResponseTypeDef

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTagsRequestRequestTypeDef

### configurationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.TagTypeDef]
- **Required**: Yes


# CustomerAgentInfoTypeDef

### activeAgents
- **Type**: <class 'int'>
- **Required**: Yes

### healthyAgents
- **Type**: <class 'int'>
- **Required**: Yes

### blackListedAgents
- **Type**: <class 'int'>
- **Required**: Yes

### shutdownAgents
- **Type**: <class 'int'>
- **Required**: Yes

### unhealthyAgents
- **Type**: <class 'int'>
- **Required**: Yes

### totalAgents
- **Type**: <class 'int'>
- **Required**: Yes

### unknownAgents
- **Type**: <class 'int'>
- **Required**: Yes


# CustomerAgentlessCollectorInfoTypeDef

### activeAgentlessCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### healthyAgentlessCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### denyListedAgentlessCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### shutdownAgentlessCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### unhealthyAgentlessCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### totalAgentlessCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### unknownAgentlessCollectors
- **Type**: <class 'int'>
- **Required**: Yes


# CustomerConnectorInfoTypeDef

### activeConnectors
- **Type**: <class 'int'>
- **Required**: Yes

### healthyConnectors
- **Type**: <class 'int'>
- **Required**: Yes

### blackListedConnectors
- **Type**: <class 'int'>
- **Required**: Yes

### shutdownConnectors
- **Type**: <class 'int'>
- **Required**: Yes

### unhealthyConnectors
- **Type**: <class 'int'>
- **Required**: Yes

### totalConnectors
- **Type**: <class 'int'>
- **Required**: Yes

### unknownConnectors
- **Type**: <class 'int'>
- **Required**: Yes


# CustomerMeCollectorInfoTypeDef

### activeMeCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### healthyMeCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### denyListedMeCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### shutdownMeCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### unhealthyMeCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### totalMeCollectors
- **Type**: <class 'int'>
- **Required**: Yes

### unknownMeCollectors
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteAgentTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteApplicationsRequestRequestTypeDef

### configurationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteTagsRequestRequestTypeDef

### configurationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.TagTypeDef]]


# DeletionWarningTypeDef

### configurationId
- **Type**: typing.Optional[str]

### warningCode
- **Type**: typing.Optional[int]

### warningText
- **Type**: typing.Optional[str]


# DescribeAgentsRequestDescribeAgentsPaginateTypeDef

### agentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.PaginatorConfigTypeDef]


# DescribeAgentsRequestRequestTypeDef

### agentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeAgentsResponseTypeDef

### agentsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.AgentInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBatchDeleteConfigurationTaskRequestRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchDeleteConfigurationTaskResponseTypeDef

### task
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.BatchDeleteConfigurationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConfigurationsRequestRequestTypeDef

### configurationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeConfigurationsResponseTypeDef

### configurations
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeContinuousExportsRequestDescribeContinuousExportsPaginateTypeDef

### exportIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.PaginatorConfigTypeDef]


# DescribeContinuousExportsRequestRequestTypeDef

### exportIds
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeContinuousExportsResponseTypeDef

### descriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.ContinuousExportDescriptionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateTypeDef

### exportIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.PaginatorConfigTypeDef]


# DescribeExportConfigurationsRequestRequestTypeDef

### exportIds
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeExportConfigurationsResponseTypeDef

### exportsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.ExportInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef

### exportIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.ExportFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.PaginatorConfigTypeDef]


# DescribeExportTasksRequestRequestTypeDef

### exportIds
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.ExportFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeExportTasksResponseTypeDef

### exportsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.ExportInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImportTasksRequestDescribeImportTasksPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.ImportTaskFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.PaginatorConfigTypeDef]


# DescribeImportTasksRequestRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.ImportTaskFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeImportTasksResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.ImportTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTagsRequestDescribeTagsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.TagFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.PaginatorConfigTypeDef]


# DescribeTagsRequestRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.TagFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeTagsResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.ConfigurationTagTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef

### applicationConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### configurationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# Ec2RecommendationsExportPreferencesTypeDef

### enabled
- **Type**: typing.Optional[bool]

### cpuPerformanceMetricBasis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.UsageMetricBasisTypeDef]

### ramPerformanceMetricBasis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.UsageMetricBasisTypeDef]

### tenancy
- **Type**: typing.Optional[typing.Literal['DEDICATED', 'SHARED']]

### excludedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### preferredRegion
- **Type**: typing.Optional[str]

### reservedInstanceOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.ReservedInstanceOptionsTypeDef]


# ExportConfigurationsResponseTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportFilterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### condition
- **Type**: <class 'str'>
- **Required**: Yes


# ExportInfoTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### exportStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### exportRequestTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configurationsDownloadUrl
- **Type**: typing.Optional[str]

### isTruncated
- **Type**: typing.Optional[bool]

### requestedStartTime
- **Type**: typing.Optional[datetime.datetime]

### requestedEndTime
- **Type**: typing.Optional[datetime.datetime]


# ExportPreferencesTypeDef

### ec2RecommendationsPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.Ec2RecommendationsExportPreferencesTypeDef]


# FailedConfigurationTypeDef

### configurationId
- **Type**: typing.Optional[str]

### errorStatusCode
- **Type**: typing.Optional[int]

### errorMessage
- **Type**: typing.Optional[str]


# FilterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### condition
- **Type**: <class 'str'>
- **Required**: Yes


# GetDiscoverySummaryResponseTypeDef

### servers
- **Type**: <class 'int'>
- **Required**: Yes

### applications
- **Type**: <class 'int'>
- **Required**: Yes

### serversMappedToApplications
- **Type**: <class 'int'>
- **Required**: Yes

### serversMappedtoTags
- **Type**: <class 'int'>
- **Required**: Yes

### agentSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.CustomerAgentInfoTypeDef'>
- **Required**: Yes

### connectorSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.CustomerConnectorInfoTypeDef'>
- **Required**: Yes

### meCollectorSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.CustomerMeCollectorInfoTypeDef'>
- **Required**: Yes

### agentlessCollectorSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.CustomerAgentlessCollectorInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportTaskFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['IMPORT_TASK_ID', 'NAME', 'STATUS']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# ImportTaskTypeDef

### importTaskId
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### importUrl
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_FAILED_LIMIT_EXCEEDED', 'DELETE_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_COMPLETE_WITH_ERRORS', 'IMPORT_FAILED', 'IMPORT_FAILED_RECORD_LIMIT_EXCEEDED', 'IMPORT_FAILED_SERVER_LIMIT_EXCEEDED', 'IMPORT_IN_PROGRESS', 'INTERNAL_ERROR']]

### importRequestTime
- **Type**: typing.Optional[datetime.datetime]

### importCompletionTime
- **Type**: typing.Optional[datetime.datetime]

### importDeletedTime
- **Type**: typing.Optional[datetime.datetime]

### serverImportSuccess
- **Type**: typing.Optional[int]

### serverImportFailure
- **Type**: typing.Optional[int]

### applicationImportSuccess
- **Type**: typing.Optional[int]

### applicationImportFailure
- **Type**: typing.Optional[int]

### errorsAndFailedEntriesZip
- **Type**: typing.Optional[str]


# ListConfigurationsRequestListConfigurationsPaginateTypeDef

### configurationType
- **Type**: typing.Literal['APPLICATION', 'CONNECTION', 'PROCESS', 'SERVER']
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.FilterTypeDef]]

### orderBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.OrderByElementTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.PaginatorConfigTypeDef]


# ListConfigurationsRequestRequestTypeDef

### configurationType
- **Type**: typing.Literal['APPLICATION', 'CONNECTION', 'PROCESS', 'SERVER']
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.OrderByElementTypeDef]]


# ListConfigurationsResponseTypeDef

### configurations
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServerNeighborsRequestRequestTypeDef

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### portInformationNeeded
- **Type**: typing.Optional[bool]

### neighborConfigurationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServerNeighborsResponseTypeDef

### neighbors
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.NeighborConnectionDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### knownDependencyCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NeighborConnectionDetailTypeDef

### sourceServerId
- **Type**: <class 'str'>
- **Required**: Yes

### destinationServerId
- **Type**: <class 'str'>
- **Required**: Yes

### connectionsCount
- **Type**: <class 'int'>
- **Required**: Yes

### destinationPort
- **Type**: typing.Optional[int]

### transportProtocol
- **Type**: typing.Optional[str]


# OrderByElementTypeDef

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ReservedInstanceOptionsTypeDef

### purchasingOption
- **Type**: typing.Literal['ALL_UPFRONT', 'NO_UPFRONT', 'PARTIAL_UPFRONT']
- **Required**: Yes

### offeringClass
- **Type**: typing.Literal['CONVERTIBLE', 'STANDARD']
- **Required**: Yes

### termLength
- **Type**: typing.Literal['ONE_YEAR', 'THREE_YEAR']
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# StartBatchDeleteConfigurationTaskRequestRequestTypeDef

### configurationType
- **Type**: typing.Literal['SERVER']
- **Required**: Yes

### configurationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StartBatchDeleteConfigurationTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartContinuousExportResponseTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataSource
- **Type**: typing.Literal['AGENT']
- **Required**: Yes

### schemaStorageConfig
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDataCollectionByAgentIdsRequestRequestTypeDef

### agentIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StartDataCollectionByAgentIdsResponseTypeDef

### agentsConfigurationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.AgentConfigurationStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartExportTaskRequestRequestTypeDef

### exportDataFormat
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CSV']]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.discovery_classes.ExportFilterTypeDef]]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### preferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery_classes.ExportPreferencesTypeDef]


# StartExportTaskResponseTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartImportTaskRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### importUrl
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# StartImportTaskResponseTypeDef

### task
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ImportTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopContinuousExportRequestRequestTypeDef

### exportId
- **Type**: <class 'str'>
- **Required**: Yes


# StopContinuousExportResponseTypeDef

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDataCollectionByAgentIdsRequestRequestTypeDef

### agentIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StopDataCollectionByAgentIdsResponseTypeDef

### agentsConfigurationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery_classes.AgentConfigurationStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagFilterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UsageMetricBasisTypeDef

### name
- **Type**: typing.Optional[str]

### percentageAdjust
- **Type**: typing.Optional[float]


