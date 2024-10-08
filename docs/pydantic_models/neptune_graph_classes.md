# Pydantic Models in neptune_graph_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelImportTaskInputRequestTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelImportTaskOutputTypeDef

### graphId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'OPEN_CYPHER']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelQueryInputRequestTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGraphInputRequestTypeDef

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


# CreateGraphOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'IMPORTING', 'RESETTING', 'SNAPSHOTTING', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### provisionedMemory
- **Type**: <class 'int'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: <class 'bool'>
- **Required**: Yes

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.VectorSearchConfigurationTypeDef'>
- **Required**: Yes

### replicaCount
- **Type**: <class 'int'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### buildNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGraphSnapshotInputRequestTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateGraphSnapshotOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceGraphId
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotCreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGraphUsingImportTaskInputRequestTypeDef

### graphName
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
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

### importOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.ImportOptionsTypeDef]

### maxProvisionedMemory
- **Type**: typing.Optional[int]

### minProvisionedMemory
- **Type**: typing.Optional[int]

### failOnError
- **Type**: typing.Optional[bool]

### format
- **Type**: typing.Optional[typing.Literal['CSV', 'OPEN_CYPHER']]


# CreateGraphUsingImportTaskOutputTypeDef

### graphId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'OPEN_CYPHER']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### importOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ImportOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePrivateGraphEndpointInputRequestTypeDef

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


# DeleteGraphInputRequestTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipSnapshot
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteGraphOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'IMPORTING', 'RESETTING', 'SNAPSHOTTING', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### provisionedMemory
- **Type**: <class 'int'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: <class 'bool'>
- **Required**: Yes

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.VectorSearchConfigurationTypeDef'>
- **Required**: Yes

### replicaCount
- **Type**: <class 'int'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### buildNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGraphSnapshotInputRequestTypeDef

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGraphSnapshotOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceGraphId
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotCreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePrivateGraphEndpointInputRequestTypeDef

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


# ExecuteQueryInputRequestTypeDef

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


# GetGraphInputGraphAvailableWaitTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphInputGraphDeletedWaitTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphInputRequestTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'IMPORTING', 'RESETTING', 'SNAPSHOTTING', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### provisionedMemory
- **Type**: <class 'int'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: <class 'bool'>
- **Required**: Yes

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.VectorSearchConfigurationTypeDef'>
- **Required**: Yes

### replicaCount
- **Type**: <class 'int'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### buildNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGraphSnapshotInputGraphSnapshotAvailableWaitTypeDef

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphSnapshotInputGraphSnapshotDeletedWaitTypeDef

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetGraphSnapshotInputRequestTypeDef

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphSnapshotOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceGraphId
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotCreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGraphSummaryInputRequestTypeDef

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


# GetImportTaskInputImportTaskCancelledWaitTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetImportTaskInputImportTaskSuccessfulWaitTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetImportTaskInputRequestTypeDef

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportTaskOutputTypeDef

### graphId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'OPEN_CYPHER']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### importOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ImportOptionsTypeDef'>
- **Required**: Yes

### importTaskDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ImportTaskDetailsTypeDef'>
- **Required**: Yes

### attemptNumber
- **Type**: <class 'int'>
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPrivateGraphEndpointInputPrivateGraphEndpointAvailableWaitTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetPrivateGraphEndpointInputPrivateGraphEndpointDeletedWaitTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.WaiterConfigTypeDef]


# GetPrivateGraphEndpointInputRequestTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes


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


# GetQueryInputRequestTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### waited
- **Type**: <class 'int'>
- **Required**: Yes

### elapsed
- **Type**: <class 'int'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CANCELLING', 'RUNNING', 'WAITING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceGraphId
- **Type**: typing.Optional[str]

### snapshotCreateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED']]

### kmsKeyIdentifier
- **Type**: typing.Optional[str]


# GraphSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'IMPORTING', 'RESETTING', 'SNAPSHOTTING', 'UPDATING']]

### provisionedMemory
- **Type**: typing.Optional[int]

### publicConnectivity
- **Type**: typing.Optional[bool]

### endpoint
- **Type**: typing.Optional[str]

### replicaCount
- **Type**: typing.Optional[int]

### kmsKeyIdentifier
- **Type**: typing.Optional[str]

### deletionProtection
- **Type**: typing.Optional[bool]


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

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### graphId
- **Type**: typing.Optional[str]

### format
- **Type**: typing.Optional[typing.Literal['CSV', 'OPEN_CYPHER']]


# ListGraphSnapshotsInputListGraphSnapshotsPaginateTypeDef

### graphIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListGraphSnapshotsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGraphsInputListGraphsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListGraphsInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGraphsOutputTypeDef

### graphs
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.GraphSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImportTasksInputListImportTasksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListImportTasksInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListImportTasksOutputTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph_classes.ImportTaskSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPrivateGraphEndpointsInputListPrivateGraphEndpointsPaginateTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.PaginatorConfigTypeDef]


# ListPrivateGraphEndpointsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQueriesInputRequestTypeDef

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


# ListTagsForResourceInputRequestTypeDef

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

### id
- **Type**: typing.Optional[str]

### queryString
- **Type**: typing.Optional[str]

### waited
- **Type**: typing.Optional[int]

### elapsed
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[typing.Literal['CANCELLING', 'RUNNING', 'WAITING']]


# ResetGraphInputRequestTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipSnapshot
- **Type**: <class 'bool'>
- **Required**: Yes


# ResetGraphOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'IMPORTING', 'RESETTING', 'SNAPSHOTTING', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### provisionedMemory
- **Type**: <class 'int'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: <class 'bool'>
- **Required**: Yes

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.VectorSearchConfigurationTypeDef'>
- **Required**: Yes

### replicaCount
- **Type**: <class 'int'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### buildNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
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


# RestoreGraphFromSnapshotInputRequestTypeDef

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


# RestoreGraphFromSnapshotOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'IMPORTING', 'RESETTING', 'SNAPSHOTTING', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### provisionedMemory
- **Type**: <class 'int'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: <class 'bool'>
- **Required**: Yes

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.VectorSearchConfigurationTypeDef'>
- **Required**: Yes

### replicaCount
- **Type**: <class 'int'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### buildNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartImportTaskInputRequestTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### importOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph_classes.ImportOptionsTypeDef]

### failOnError
- **Type**: typing.Optional[bool]

### format
- **Type**: typing.Optional[typing.Literal['CSV', 'OPEN_CYPHER']]


# StartImportTaskOutputTypeDef

### graphId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'OPEN_CYPHER']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### importOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ImportOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGraphInputRequestTypeDef

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: typing.Optional[bool]

### provisionedMemory
- **Type**: typing.Optional[int]

### deletionProtection
- **Type**: typing.Optional[bool]


# UpdateGraphOutputTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'IMPORTING', 'RESETTING', 'SNAPSHOTTING', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### provisionedMemory
- **Type**: <class 'int'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### publicConnectivity
- **Type**: <class 'bool'>
- **Required**: Yes

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.VectorSearchConfigurationTypeDef'>
- **Required**: Yes

### replicaCount
- **Type**: <class 'int'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtection
- **Type**: <class 'bool'>
- **Required**: Yes

### buildNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VectorSearchConfigurationTypeDef

### dimension
- **Type**: <class 'int'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


