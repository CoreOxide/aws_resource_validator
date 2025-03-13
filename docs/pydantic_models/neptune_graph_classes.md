# Neptune Graph Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelExportTaskInputTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelImportTaskInputTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelQueryInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGraphInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.VectorSearchConfigurationTypeDef]

### replicaCount
- **Type**: typing.Optional[int]

### deletionProtection
- **Type**: typing.Optional[bool]


# CreateGraphSnapshotInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePrivateGraphEndpointInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: typing.Optional[str]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CreatePrivateGraphEndpointOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGraphInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipSnapshot
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteGraphSnapshotInputTypeDef

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrivateGraphEndpointInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrivateGraphEndpointOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EdgeStructureTypeDef

### count
- **Type**: typing.Optional[int]

### edgeProperties
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteQueryInputTypeDef

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


# ExecuteQueryOutputTypeDef

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportFilterElementOutputTypeDef

### properties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterPropertyAttributesTypeDef]]


# ExportFilterElementTypeDef

### properties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterPropertyAttributesTypeDef]]


# ExportFilterOutputTypeDef

### vertexFilter
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterElementOutputTypeDef]]

### edgeFilter
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterElementOutputTypeDef]]


# ExportFilterPropertyAttributesTypeDef

### outputType
- **Type**: typing.Optional[str]

### sourcePropertyName
- **Type**: typing.Optional[str]

### multiValueHandling
- **Type**: typing.Optional[typing.Literal['PICK_FIRST', 'TO_LIST']]


# ExportFilterTypeDef

### vertexFilter
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterElementTypeDef]]

### edgeFilter
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.neptune_graph_classes.ExportFilterElementTypeDef]]


# ExportTaskDetailsTypeDef

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


# ExportTaskSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetExportTaskInputTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetExportTaskInputWaitExtraTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetExportTaskInputWaitTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphInputWaitExtraTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphInputWaitTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphSnapshotInputTypeDef

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphSnapshotInputWaitExtraTypeDef

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphSnapshotInputWaitTypeDef

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphSummaryInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### mode
- **Type**: typing.Optional[typing.Literal['BASIC', 'DETAILED']]


# GetGraphSummaryOutputTypeDef

### version
- **Type**: <class 'str'>
- **Required**: Yes

### lastStatisticsComputationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### graphSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.GraphDataSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportTaskInputTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportTaskInputWaitExtraTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetImportTaskInputWaitTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetPrivateGraphEndpointInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrivateGraphEndpointInputWaitExtraTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetPrivateGraphEndpointInputWaitTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetPrivateGraphEndpointOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GraphDataSummaryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.NodeStructureTypeDef]]

### edgeStructures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.EdgeStructureTypeDef]]


# GraphSnapshotSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GraphSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportOptionsTypeDef

### neptune
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.NeptuneImportOptionsTypeDef]


# ImportTaskDetailsTypeDef

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


# ImportTaskSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListExportTasksInputPaginateTypeDef

### graphIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListExportTasksInputTypeDef

### graphIdentifier
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListExportTasksOutputTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.ExportTaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGraphSnapshotsInputPaginateTypeDef

### graphIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListGraphSnapshotsInputTypeDef

### graphIdentifier
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGraphSnapshotsOutputTypeDef

### graphSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.GraphSnapshotSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGraphsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListGraphsInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGraphsOutputTypeDef

### graphs
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.GraphSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportTasksInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListImportTasksInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListImportTasksOutputTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.ImportTaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrivateGraphEndpointsInputPaginateTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListPrivateGraphEndpointsInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrivateGraphEndpointsOutputTypeDef

### privateGraphEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.PrivateGraphEndpointSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueriesInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['ALL', 'CANCELLING', 'RUNNING', 'WAITING']]


# ListQueriesOutputTypeDef

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.QuerySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NeptuneImportOptionsTypeDef

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


# NodeStructureTypeDef

### count
- **Type**: typing.Optional[int]

### nodeProperties
- **Type**: typing.Optional[typing.List[str]]

### distinctOutgoingEdgeLabels
- **Type**: typing.Optional[typing.List[str]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrivateGraphEndpointSummaryTypeDef

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


# QuerySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResetGraphInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipSnapshot
- **Type**: <class 'bool'>
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


# RestoreGraphFromSnapshotInputTypeDef

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


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGraphInputTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: typing.Optional[bool]

### provisionedMemory
- **Type**: typing.Optional[int]

### deletionProtection
- **Type**: typing.Optional[bool]


# VectorSearchConfigurationTypeDef

### dimension
- **Type**: <class 'int'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


