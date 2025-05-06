# Discovery Classes

# AgentConfigurationStatus

### agentId
- **Type**: typing.Optional[str]

### operationSucceeded
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# AgentInfo

### agentId
- **Type**: typing.Optional[str]

### hostName
- **Type**: typing.Optional[str]

### agentNetworkInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.AgentNetworkInfo]]

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


# AgentNetworkInfo

### ipAddress
- **Type**: typing.Optional[str]

### macAddress
- **Type**: typing.Optional[str]


# AssociateConfigurationItemsToApplicationRequest

### applicationConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### configurationIds
- **Type**: typing.List[str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteAgentError

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### errorCode
- **Type**: typing.Literal['AGENT_IN_USE', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND']
- **Required**: Yes


# BatchDeleteAgentsRequest

### deleteAgents
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.DeleteAgent]
- **Required**: Yes


# BatchDeleteAgentsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.BatchDeleteAgentError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteConfigurationTask

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.FailedConfiguration]]

### deletionWarnings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.DeletionWarning]]


# BatchDeleteImportDataError

### importTaskId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['INTERNAL_SERVER_ERROR', 'NOT_FOUND', 'OVER_LIMIT']]

### errorDescription
- **Type**: typing.Optional[str]


# BatchDeleteImportDataRequest

### importTaskIds
- **Type**: typing.List[str]
- **Required**: Yes

### deleteHistory
- **Type**: typing.Optional[bool]


# BatchDeleteImportDataResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.BatchDeleteImportDataError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigurationTag

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


# ContinuousExportDescription

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


# CreateApplicationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### wave
- **Type**: typing.Optional[str]


# CreateApplicationResponse

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTagsRequest

### configurationIds
- **Type**: typing.List[str]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.Tag]
- **Required**: Yes


# CustomerAgentInfo

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


# CustomerAgentlessCollectorInfo

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


# CustomerConnectorInfo

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


# CustomerMeCollectorInfo

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


# DeleteAgent

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteApplicationsRequest

### configurationIds
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteTagsRequest

### configurationIds
- **Type**: typing.List[str]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.Tag]]


# DeletionWarning

### configurationId
- **Type**: typing.Optional[str]

### warningCode
- **Type**: typing.Optional[int]

### warningText
- **Type**: typing.Optional[str]


# DescribeAgentsRequest

### agentIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeAgentsRequestPaginate

### agentIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.PaginatorConfig]


# DescribeAgentsResponse

### agentsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.AgentInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeBatchDeleteConfigurationTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchDeleteConfigurationTaskResponse

### task
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.BatchDeleteConfigurationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConfigurationsRequest

### configurationIds
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeConfigurationsResponse

### configurations
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContinuousExportsRequest

### exportIds
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeContinuousExportsRequestPaginate

### exportIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.PaginatorConfig]


# DescribeContinuousExportsResponse

### descriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ContinuousExportDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeExportConfigurationsRequest

### exportIds
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeExportConfigurationsRequestPaginate

### exportIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.PaginatorConfig]


# DescribeExportConfigurationsResponse

### exportsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ExportInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeExportTasksRequest

### exportIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ExportFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeExportTasksRequestPaginate

### exportIds
- **Type**: typing.Optional[typing.List[str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ExportFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.PaginatorConfig]


# DescribeExportTasksResponse

### exportsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ExportInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeImportTasksRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ImportTaskFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeImportTasksRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ImportTaskFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.PaginatorConfig]


# DescribeImportTasksResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ImportTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeTagsRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.TagFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeTagsRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.TagFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.PaginatorConfig]


# DescribeTagsResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ConfigurationTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DisassociateConfigurationItemsFromApplicationRequest

### applicationConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### configurationIds
- **Type**: typing.List[str]
- **Required**: Yes


# Ec2RecommendationsExportPreferences

### enabled
- **Type**: typing.Optional[bool]

### cpuPerformanceMetricBasis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.UsageMetricBasis]

### ramPerformanceMetricBasis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.UsageMetricBasis]

### tenancy
- **Type**: typing.Optional[typing.Literal['DEDICATED', 'SHARED']]

### excludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### preferredRegion
- **Type**: typing.Optional[str]

### reservedInstanceOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.ReservedInstanceOptions]


# ExportConfigurationsResponse

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# ExportFilter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### condition
- **Type**: <class 'str'>
- **Required**: Yes


# ExportInfo

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


# ExportPreferences

### ec2RecommendationsPreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.Ec2RecommendationsExportPreferences]


# FailedConfiguration

### configurationId
- **Type**: typing.Optional[str]

### errorStatusCode
- **Type**: typing.Optional[int]

### errorMessage
- **Type**: typing.Optional[str]


# Filter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### condition
- **Type**: <class 'str'>
- **Required**: Yes


# GetDiscoverySummaryResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.CustomerAgentInfo'>
- **Required**: Yes

### connectorSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.CustomerConnectorInfo'>
- **Required**: Yes

### meCollectorSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.CustomerMeCollectorInfo'>
- **Required**: Yes

### agentlessCollectorSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.CustomerAgentlessCollectorInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# ImportTask

### importTaskId
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### importUrl
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_FAILED_LIMIT_EXCEEDED', 'DELETE_IN_PROGRESS', 'IMPORT_COMPLETE', 'IMPORT_COMPLETE_WITH_ERRORS', 'IMPORT_FAILED', 'IMPORT_FAILED_RECORD_LIMIT_EXCEEDED', 'IMPORT_FAILED_SERVER_LIMIT_EXCEEDED', 'IMPORT_FAILED_UNSUPPORTED_FILE_TYPE', 'IMPORT_IN_PROGRESS', 'INTERNAL_ERROR']]

### importRequestTime
- **Type**: typing.Optional[datetime.datetime]

### importCompletionTime
- **Type**: typing.Optional[datetime.datetime]

### importDeletedTime
- **Type**: typing.Optional[datetime.datetime]

### fileClassification
- **Type**: typing.Optional[typing.Literal['IMPORT_TEMPLATE', 'MODELIZEIT_EXPORT', 'RVTOOLS_EXPORT', 'VMWARE_NSX_EXPORT']]

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


# ImportTaskFilter

### name
- **Type**: typing.Optional[typing.Literal['FILE_CLASSIFICATION', 'IMPORT_TASK_ID', 'NAME', 'STATUS']]

### values
- **Type**: typing.Optional[typing.List[str]]


# ListConfigurationsRequest

### configurationType
- **Type**: typing.Literal['APPLICATION', 'CONNECTION', 'PROCESS', 'SERVER']
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.OrderByElement]]


# ListConfigurationsRequestPaginate

### configurationType
- **Type**: typing.Literal['APPLICATION', 'CONNECTION', 'PROCESS', 'SERVER']
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.Filter]]

### orderBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.OrderByElement]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.PaginatorConfig]


# ListConfigurationsResponse

### configurations
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServerNeighborsRequest

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### portInformationNeeded
- **Type**: typing.Optional[bool]

### neighborConfigurationIds
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListServerNeighborsResponse

### neighbors
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.NeighborConnectionDetail]
- **Required**: Yes

### knownDependencyCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NeighborConnectionDetail

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


# OrderByElement

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ReservedInstanceOptions

### purchasingOption
- **Type**: typing.Literal['ALL_UPFRONT', 'NO_UPFRONT', 'PARTIAL_UPFRONT']
- **Required**: Yes

### offeringClass
- **Type**: typing.Literal['CONVERTIBLE', 'STANDARD']
- **Required**: Yes

### termLength
- **Type**: typing.Literal['ONE_YEAR', 'THREE_YEAR']
- **Required**: Yes


# ResponseMetadata

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


# StartBatchDeleteConfigurationTaskRequest

### configurationType
- **Type**: typing.Literal['SERVER']
- **Required**: Yes

### configurationIds
- **Type**: typing.List[str]
- **Required**: Yes


# StartBatchDeleteConfigurationTaskResponse

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# StartContinuousExportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# StartDataCollectionByAgentIdsRequest

### agentIds
- **Type**: typing.List[str]
- **Required**: Yes


# StartDataCollectionByAgentIdsResponse

### agentsConfigurationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.AgentConfigurationStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# StartExportTaskRequest

### exportDataFormat
- **Type**: typing.Optional[typing.List[typing.Literal['CSV']]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.ExportFilter]]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### preferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.discovery.discovery_classes.ExportPreferences]


# StartExportTaskResponse

### exportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# StartImportTaskRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### importUrl
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# StartImportTaskResponse

### task
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ImportTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# StopContinuousExportRequest

### exportId
- **Type**: <class 'str'>
- **Required**: Yes


# StopContinuousExportResponse

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# StopDataCollectionByAgentIdsRequest

### agentIds
- **Type**: typing.List[str]
- **Required**: Yes


# StopDataCollectionByAgentIdsResponse

### agentsConfigurationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.discovery.discovery_classes.AgentConfigurationStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.discovery.discovery_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagFilter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApplicationRequest

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### wave
- **Type**: typing.Optional[str]


# UsageMetricBasis

### name
- **Type**: typing.Optional[str]

### percentageAdjust
- **Type**: typing.Optional[float]


