# Neptune Graph Neptune Graph Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelExportTaskInput

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelExportTaskOutput

### graphId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'INITIALIZING', 'SUCCEEDED']
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parquetType
- **Type**: typing.Literal['COLUMNAR']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# CancelImportTaskInput

### taskIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelImportTaskOutput

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
- **Type**: typing.Literal['CSV', 'NTRIPLES', 'OPEN_CYPHER', 'PARQUET']
- **Required**: Yes

### parquetType
- **Type**: typing.Literal['COLUMNAR']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]

### publicConnectivity
- **Type**: typing.Optional[bool]

### kmsKeyIdentifier
- **Type**: typing.Optional[str]

### vectorSearchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.VectorSearchConfiguration]

### replicaCount
- **Type**: typing.Optional[int]

### deletionProtection
- **Type**: typing.Optional[bool]


# CreateGraphOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.VectorSearchConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGraphSnapshotInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateGraphSnapshotOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGraphUsingImportTaskInput

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### publicConnectivity
- **Type**: typing.Optional[bool]

### kmsKeyIdentifier
- **Type**: typing.Optional[str]

### vectorSearchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.VectorSearchConfiguration]

### replicaCount
- **Type**: typing.Optional[int]

### deletionProtection
- **Type**: typing.Optional[bool]

### importOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ImportOptions]

### maxProvisionedMemory
- **Type**: typing.Optional[int]

### minProvisionedMemory
- **Type**: typing.Optional[int]

### failOnError
- **Type**: typing.Optional[bool]

### format
- **Type**: typing.Optional[typing.Literal['CSV', 'NTRIPLES', 'OPEN_CYPHER', 'PARQUET']]

### parquetType
- **Type**: typing.Optional[typing.Literal['COLUMNAR']]

### blankNodeHandling
- **Type**: typing.Optional[typing.Literal['convertToIri']]


# CreateGraphUsingImportTaskOutput

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
- **Type**: typing.Literal['CSV', 'NTRIPLES', 'OPEN_CYPHER', 'PARQUET']
- **Required**: Yes

### parquetType
- **Type**: typing.Literal['COLUMNAR']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### importOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ImportOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePrivateGraphEndpointInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: typing.Optional[str]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGraphInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipSnapshot
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteGraphOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.VectorSearchConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGraphSnapshotInput

### snapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGraphSnapshotOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# EdgeStructure

### count
- **Type**: typing.Optional[int]

### edgeProperties
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# ExportFilter

### vertexFilter
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterElement]]

### edgeFilter
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterElement]]


# ExportFilterElement

### properties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterPropertyAttributes]]


# ExportFilterElementOutput

### properties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterPropertyAttributes]]


# ExportFilterOutput

### vertexFilter
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterElementOutput]]

### edgeFilter
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterElementOutput]]


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

### graphId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'INITIALIZING', 'SUCCEEDED']
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parquetType
- **Type**: typing.Optional[typing.Literal['COLUMNAR']]

### statusReason
- **Type**: typing.Optional[str]


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


# GetExportTaskOutput

### graphId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'INITIALIZING', 'SUCCEEDED']
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parquetType
- **Type**: typing.Literal['COLUMNAR']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### exportTaskDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportTaskDetails'>
- **Required**: Yes

### exportFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


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


# GetGraphOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.VectorSearchConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


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


# GetGraphSnapshotOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.GraphDataSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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


# GetImportTaskOutput

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
- **Type**: typing.Literal['CSV', 'NTRIPLES', 'OPEN_CYPHER', 'PARQUET']
- **Required**: Yes

### parquetType
- **Type**: typing.Literal['COLUMNAR']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### importOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ImportOptions'>
- **Required**: Yes

### importTaskDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ImportTaskDetails'>
- **Required**: Yes

### attemptNumber
- **Type**: <class 'int'>
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.NodeStructure]]

### edgeStructures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.EdgeStructure]]


# GraphSnapshotSummary

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


# GraphSummary

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


# ImportOptions

### neptune
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.NeptuneImportOptions]


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
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### graphId
- **Type**: typing.Optional[str]

### format
- **Type**: typing.Optional[typing.Literal['CSV', 'NTRIPLES', 'OPEN_CYPHER', 'PARQUET']]

### parquetType
- **Type**: typing.Optional[typing.Literal['COLUMNAR']]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.PaginatorConfig]


# ListExportTasksOutput

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.PaginatorConfig]


# ListGraphSnapshotsOutput

### graphSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.GraphSnapshotSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.PaginatorConfig]


# ListGraphsOutput

### graphs
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.GraphSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.PaginatorConfig]


# ListImportTasksOutput

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ImportTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.PaginatorConfig]


# ListPrivateGraphEndpointsOutput

### privateGraphEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.PrivateGraphEndpointSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.QuerySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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


# ResetGraphInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipSnapshot
- **Type**: <class 'bool'>
- **Required**: Yes


# ResetGraphOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.VectorSearchConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]

### replicaCount
- **Type**: typing.Optional[int]

### publicConnectivity
- **Type**: typing.Optional[bool]


# RestoreGraphFromSnapshotOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.VectorSearchConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# StartExportTaskInput

### graphIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parquetType
- **Type**: typing.Optional[typing.Literal['COLUMNAR']]

### exportFilter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilter, aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartExportTaskOutput

### graphId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'INITIALIZING', 'SUCCEEDED']
- **Required**: Yes

### format
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### parquetType
- **Type**: typing.Literal['COLUMNAR']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### exportFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ExportFilterOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# StartImportTaskInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ImportOptions]

### failOnError
- **Type**: typing.Optional[bool]

### format
- **Type**: typing.Optional[typing.Literal['CSV', 'NTRIPLES', 'OPEN_CYPHER', 'PARQUET']]

### parquetType
- **Type**: typing.Optional[typing.Literal['COLUMNAR']]

### blankNodeHandling
- **Type**: typing.Optional[typing.Literal['convertToIri']]


# StartImportTaskOutput

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
- **Type**: typing.Literal['CSV', 'NTRIPLES', 'OPEN_CYPHER', 'PARQUET']
- **Required**: Yes

### parquetType
- **Type**: typing.Literal['COLUMNAR']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ANALYZING_DATA', 'CANCELLED', 'CANCELLING', 'DELETED', 'EXPORTING', 'FAILED', 'IMPORTING', 'INITIALIZING', 'REPROVISIONING', 'ROLLING_BACK', 'SUCCEEDED']
- **Required**: Yes

### importOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ImportOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
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


# UpdateGraphOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.VectorSearchConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptune_graph.neptune_graph_classes.ResponseMetadata'>
- **Required**: Yes


# VectorSearchConfiguration

### dimension
- **Type**: <class 'int'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


