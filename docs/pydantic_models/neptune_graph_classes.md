# Neptune Graph Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelExportTaskInput

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelImportTaskInput

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelQueryInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGraphInput

### graphName
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedMemory
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### publicConnectivity
- **Type**: typing.Optional[bool]

### kmsKeyIdentifier
- **Type**: typing.Optional[str]

### vectorSearchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.VectorSearchConfiguration]

### replicaCount
- **Type**: typing.Optional[int]

### deletionProtection
- **Type**: typing.Optional[bool]


# CreateGraphSnapshotInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePrivateGraphEndpointInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: typing.Optional[str]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CreatePrivateGraphEndpointOutput

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### vpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGraphInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipSnapshot
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteGraphSnapshotInput

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrivateGraphEndpointInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrivateGraphEndpointOutput

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### vpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# EdgeStructure

### count
- **Type**: typing.Optional[int]

### edgeProperties
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteQueryInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### language
- **Type**: typing.Literal['OPEN_CYPHER']
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### planCache
- **Type**: typing.Optional[typing.Literal['AUTO', 'DISABLED', 'ENABLED']]

### explainMode
- **Type**: typing.Optional[typing.Literal['DETAILS', 'STATIC']]

### queryTimeoutMilliseconds
- **Type**: typing.Optional[int]


# ExecuteQueryOutput

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# ExportFilter

### vertexFilter
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterElement]]

### edgeFilter
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterElement]]


# ExportFilterElement

### properties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterPropertyAttributes]]


# ExportFilterElementOutput

### properties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterPropertyAttributes]]


# ExportFilterOutput

### vertexFilter
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterElementOutput]]

### edgeFilter
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterElementOutput]]


# ExportFilterPropertyAttributes

### outputType
- **Type**: typing.Optional[str]

### sourcePropertyName
- **Type**: typing.Optional[str]

### multiValueHandling
- **Type**: typing.Optional[typing.Literal['PICK_FIRST', 'TO_LIST']]


# ExportTaskDetails

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### timeElapsedSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### progressPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### numVerticesWritten
- **Type**: typing.Optional[int]

### numEdgesWritten
- **Type**: typing.Optional[int]


# ExportTaskSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetExportTaskInput

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportTaskInputWait

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetExportTaskInputWaitExtra

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetGraphInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphInputWait

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetGraphInputWaitExtra

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetGraphSnapshotInput

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphSnapshotInputWait

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetGraphSnapshotInputWaitExtra

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetGraphSummaryInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### mode
- **Type**: typing.Optional[typing.Literal['BASIC', 'DETAILED']]


# GetGraphSummaryOutput

### version
- **Type**: <class 'str'>
- **Required**: Yes

### lastStatisticsComputationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### graphSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.GraphDataSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportTaskInput

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportTaskInputWait

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetImportTaskInputWaitExtra

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetPrivateGraphEndpointInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrivateGraphEndpointInputWait

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetPrivateGraphEndpointInputWaitExtra

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetPrivateGraphEndpointOutput

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### vpcEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GraphDataSummary

### numNodes
- **Type**: typing.Optional[int]

### numEdges
- **Type**: typing.Optional[int]

### numNodeLabels
- **Type**: typing.Optional[int]

### numEdgeLabels
- **Type**: typing.Optional[int]

### nodeLabels
- **Type**: typing.Optional[typing.List[str]]

### edgeLabels
- **Type**: typing.Optional[typing.List[str]]

### numNodeProperties
- **Type**: typing.Optional[int]

### numEdgeProperties
- **Type**: typing.Optional[int]

### nodeProperties
- **Type**: typing.Optional[typing.List[typing.Dict[str, int]]]

### edgeProperties
- **Type**: typing.Optional[typing.List[typing.Dict[str, int]]]

### totalNodePropertyValues
- **Type**: typing.Optional[int]

### totalEdgePropertyValues
- **Type**: typing.Optional[int]

### nodeStructures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.NodeStructure]]

### edgeStructures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.EdgeStructure]]


# GraphSnapshotSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GraphSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportOptions

### neptune
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.NeptuneImportOptions]


# ImportTaskDetails

### status
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### timeElapsedSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### progressPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### errorCount
- **Type**: <class 'int'>
- **Required**: Yes

### statementCount
- **Type**: <class 'int'>
- **Required**: Yes

### dictionaryEntryCount
- **Type**: <class 'int'>
- **Required**: Yes

### errorDetails
- **Type**: typing.Optional[str]


# ImportTaskSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListExportTasksInput

### graphIdentifier
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListExportTasksInputPaginate

### graphIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfig]


# ListExportTasksOutput

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.ExportTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGraphSnapshotsInput

### graphIdentifier
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGraphSnapshotsInputPaginate

### graphIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfig]


# ListGraphSnapshotsOutput

### graphSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.GraphSnapshotSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGraphsInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGraphsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfig]


# ListGraphsOutput

### graphs
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.GraphSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportTasksInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListImportTasksInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfig]


# ListImportTasksOutput

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.ImportTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrivateGraphEndpointsInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrivateGraphEndpointsInputPaginate

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfig]


# ListPrivateGraphEndpointsOutput

### privateGraphEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.PrivateGraphEndpointSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueriesInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['ALL', 'CANCELLING', 'RUNNING', 'WAITING']]


# ListQueriesOutput

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.QuerySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# NeptuneImportOptions

### s3ExportPath
- **Type**: <class 'str'>
- **Required**: Yes

### s3ExportKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### preserveDefaultVertexLabels
- **Type**: typing.Optional[bool]

### preserveEdgeIds
- **Type**: typing.Optional[bool]


# NodeStructure

### count
- **Type**: typing.Optional[int]

### nodeProperties
- **Type**: typing.Optional[typing.List[str]]

### distinctOutgoingEdgeLabels
- **Type**: typing.Optional[typing.List[str]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrivateGraphEndpointSummary

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### vpcEndpointId
- **Type**: typing.Optional[str]


# QuerySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResetGraphInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipSnapshot
- **Type**: <class 'bool'>
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


# RestoreGraphFromSnapshotInput

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### graphName
- **Type**: <class 'str'>
- **Required**: Yes

### provisionedMemory
- **Type**: typing.Optional[int]

### deletionProtection
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### replicaCount
- **Type**: typing.Optional[int]

### publicConnectivity
- **Type**: typing.Optional[bool]


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGraphInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: typing.Optional[bool]

### provisionedMemory
- **Type**: typing.Optional[int]

### deletionProtection
- **Type**: typing.Optional[bool]


# VectorSearchConfiguration

### dimension
- **Type**: <class 'int'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


