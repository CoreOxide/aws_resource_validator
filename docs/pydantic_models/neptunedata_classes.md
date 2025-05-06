# Neptunedata Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelGremlinQueryInput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelGremlinQueryOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# CancelLoaderJobInput

### loadId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelLoaderJobOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# CancelMLDataProcessingJobInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### clean
- **Type**: typing.Optional[bool]


# CancelMLDataProcessingJobOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# CancelMLModelTrainingJobInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### clean
- **Type**: typing.Optional[bool]


# CancelMLModelTrainingJobOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# CancelMLModelTransformJobInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### clean
- **Type**: typing.Optional[bool]


# CancelMLModelTransformJobOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# CancelOpenCypherQueryInput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### silent
- **Type**: typing.Optional[bool]


# CancelOpenCypherQueryOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMLEndpointInput

### id
- **Type**: typing.Optional[str]

### mlModelTrainingJobId
- **Type**: typing.Optional[str]

### mlModelTransformJobId
- **Type**: typing.Optional[str]

### update
- **Type**: typing.Optional[bool]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### modelName
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### instanceCount
- **Type**: typing.Optional[int]

### volumeEncryptionKMSKey
- **Type**: typing.Optional[str]


# CreateMLEndpointOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimeInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# CustomModelTrainingParameters

### sourceS3DirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### trainingEntryPointScript
- **Type**: typing.Optional[str]

### transformEntryPointScript
- **Type**: typing.Optional[str]


# CustomModelTransformParameters

### sourceS3DirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### transformEntryPointScript
- **Type**: typing.Optional[str]


# DeleteMLEndpointInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### clean
- **Type**: typing.Optional[bool]


# DeleteMLEndpointOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePropertygraphStatisticsOutput

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.DeleteStatisticsValueMap'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSparqlStatisticsOutput

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.DeleteStatisticsValueMap'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteStatisticsValueMap

### active
- **Type**: typing.Optional[bool]

### statisticsId
- **Type**: typing.Optional[str]


# EdgeStructure

### count
- **Type**: typing.Optional[int]

### edgeProperties
- **Type**: typing.Optional[typing.List[str]]


# ExecuteFastResetInput

### action
- **Type**: typing.Literal['initiateDatabaseReset', 'performDatabaseReset']
- **Required**: Yes

### token
- **Type**: typing.Optional[str]


# ExecuteFastResetOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.FastResetToken'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteGremlinExplainQueryInput

### gremlinQuery
- **Type**: <class 'str'>
- **Required**: Yes


# ExecuteGremlinExplainQueryOutput

### output
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteGremlinProfileQueryInput

### gremlinQuery
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.Optional[bool]

### chop
- **Type**: typing.Optional[int]

### serializer
- **Type**: typing.Optional[str]

### indexOps
- **Type**: typing.Optional[bool]


# ExecuteGremlinProfileQueryOutput

### output
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteGremlinQueryInput

### gremlinQuery
- **Type**: <class 'str'>
- **Required**: Yes

### serializer
- **Type**: typing.Optional[str]


# ExecuteGremlinQueryOutput

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.GremlinQueryStatusAttributes'>
- **Required**: Yes

### result
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### meta
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteOpenCypherExplainQueryInput

### openCypherQuery
- **Type**: <class 'str'>
- **Required**: Yes

### explainMode
- **Type**: typing.Literal['details', 'dynamic', 'static']
- **Required**: Yes

### parameters
- **Type**: typing.Optional[str]


# ExecuteOpenCypherExplainQueryOutput

### results
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteOpenCypherQueryInput

### openCypherQuery
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[str]


# ExecuteOpenCypherQueryOutput

### results
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# FastResetToken

### token
- **Type**: typing.Optional[str]


# GetEngineStatusOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### dbEngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### role
- **Type**: <class 'str'>
- **Required**: Yes

### dfeQueryEngine
- **Type**: <class 'str'>
- **Required**: Yes

### gremlin
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.QueryLanguageVersion'>
- **Required**: Yes

### sparql
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.QueryLanguageVersion'>
- **Required**: Yes

### opencypher
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.QueryLanguageVersion'>
- **Required**: Yes

### labMode
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### rollingBackTrxCount
- **Type**: <class 'int'>
- **Required**: Yes

### rollingBackTrxEarliestStartTime
- **Type**: <class 'str'>
- **Required**: Yes

### features
- **Type**: typing.Dict[str, typing.Dict[str, typing.Any]]
- **Required**: Yes

### settings
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetGremlinQueryStatusInput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGremlinQueryStatusOutput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryEvalStats
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.QueryEvalStats'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoaderJobStatusInput

### loadId
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[bool]

### errors
- **Type**: typing.Optional[bool]

### page
- **Type**: typing.Optional[int]

### errorsPerPage
- **Type**: typing.Optional[int]


# GetLoaderJobStatusOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLDataProcessingJobInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# GetMLDataProcessingJobOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### processingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlResourceDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLEndpointInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# GetMLEndpointOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlResourceDefinition'>
- **Required**: Yes

### endpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlConfigDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLModelTrainingJobInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# GetMLModelTrainingJobOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### processingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlResourceDefinition'>
- **Required**: Yes

### hpoJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlResourceDefinition'>
- **Required**: Yes

### modelTransformJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlResourceDefinition'>
- **Required**: Yes

### mlModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlConfigDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLModelTransformJobInput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# GetMLModelTransformJobOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### baseProcessingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlResourceDefinition'>
- **Required**: Yes

### remoteModelTransformJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlResourceDefinition'>
- **Required**: Yes

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.MlConfigDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetOpenCypherQueryStatusInput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOpenCypherQueryStatusOutput

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryEvalStats
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.QueryEvalStats'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetPropertygraphStatisticsOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.Statistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetPropertygraphStreamInput

### limit
- **Type**: typing.Optional[int]

### iteratorType
- **Type**: typing.Optional[typing.Literal['AFTER_SEQUENCE_NUMBER', 'AT_SEQUENCE_NUMBER', 'LATEST', 'TRIM_HORIZON']]

### commitNum
- **Type**: typing.Optional[int]

### opNum
- **Type**: typing.Optional[int]

### encoding
- **Type**: typing.Optional[typing.Literal['gzip']]


# GetPropertygraphStreamOutput

### lastEventId
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### lastTrxTimestampInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### format
- **Type**: <class 'str'>
- **Required**: Yes

### records
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.PropertygraphRecord]
- **Required**: Yes

### totalRecords
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetPropertygraphSummaryInput

### mode
- **Type**: typing.Optional[typing.Literal['basic', 'detailed']]


# GetPropertygraphSummaryOutput

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.PropertygraphSummaryValueMap'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetRDFGraphSummaryInput

### mode
- **Type**: typing.Optional[typing.Literal['basic', 'detailed']]


# GetRDFGraphSummaryOutput

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.RDFGraphSummaryValueMap'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetSparqlStatisticsOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.Statistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GetSparqlStreamInput

### limit
- **Type**: typing.Optional[int]

### iteratorType
- **Type**: typing.Optional[typing.Literal['AFTER_SEQUENCE_NUMBER', 'AT_SEQUENCE_NUMBER', 'LATEST', 'TRIM_HORIZON']]

### commitNum
- **Type**: typing.Optional[int]

### opNum
- **Type**: typing.Optional[int]

### encoding
- **Type**: typing.Optional[typing.Literal['gzip']]


# GetSparqlStreamOutput

### lastEventId
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### lastTrxTimestampInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### format
- **Type**: <class 'str'>
- **Required**: Yes

### records
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.SparqlRecord]
- **Required**: Yes

### totalRecords
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# GremlinQueryStatus

### queryId
- **Type**: typing.Optional[str]

### queryString
- **Type**: typing.Optional[str]

### queryEvalStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.QueryEvalStats]


# GremlinQueryStatusAttributes

### message
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[int]

### attributes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ListGremlinQueriesInput

### includeWaiting
- **Type**: typing.Optional[bool]


# ListGremlinQueriesOutput

### acceptedQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### runningQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.GremlinQueryStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ListLoaderJobsInput

### limit
- **Type**: typing.Optional[int]

### includeQueuedLoads
- **Type**: typing.Optional[bool]


# ListLoaderJobsOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.LoaderIdResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ListMLDataProcessingJobsInput

### maxItems
- **Type**: typing.Optional[int]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# ListMLDataProcessingJobsOutput

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ListMLEndpointsInput

### maxItems
- **Type**: typing.Optional[int]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# ListMLEndpointsOutput

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ListMLModelTrainingJobsInput

### maxItems
- **Type**: typing.Optional[int]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# ListMLModelTrainingJobsOutput

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ListMLModelTransformJobsInput

### maxItems
- **Type**: typing.Optional[int]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# ListMLModelTransformJobsOutput

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ListOpenCypherQueriesInput

### includeWaiting
- **Type**: typing.Optional[bool]


# ListOpenCypherQueriesOutput

### acceptedQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### runningQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.GremlinQueryStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# LoaderIdResult

### loadIds
- **Type**: typing.Optional[typing.List[str]]


# ManagePropertygraphStatisticsInput

### mode
- **Type**: typing.Optional[typing.Literal['disableAutoCompute', 'enableAutoCompute', 'refresh']]


# ManagePropertygraphStatisticsOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.RefreshStatisticsIdMap'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# ManageSparqlStatisticsInput

### mode
- **Type**: typing.Optional[typing.Literal['disableAutoCompute', 'enableAutoCompute', 'refresh']]


# ManageSparqlStatisticsOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.RefreshStatisticsIdMap'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# MlConfigDefinition

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# MlResourceDefinition

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### outputLocation
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### cloudwatchLogUrl
- **Type**: typing.Optional[str]


# NodeStructure

### count
- **Type**: typing.Optional[int]

### nodeProperties
- **Type**: typing.Optional[typing.List[str]]

### distinctOutgoingEdgeLabels
- **Type**: typing.Optional[typing.List[str]]


# PropertygraphData

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### from_
- **Type**: typing.Optional[str]

### to
- **Type**: typing.Optional[str]


# PropertygraphRecord

### commitTimestampInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### eventId
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.PropertygraphData'>
- **Required**: Yes

### op
- **Type**: <class 'str'>
- **Required**: Yes

### isLastOp
- **Type**: typing.Optional[bool]


# PropertygraphSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.NodeStructure]]

### edgeStructures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.EdgeStructure]]


# PropertygraphSummaryValueMap

### version
- **Type**: typing.Optional[str]

### lastStatisticsComputationTime
- **Type**: typing.Optional[datetime.datetime]

### graphSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.PropertygraphSummary]


# QueryEvalStats

### waited
- **Type**: typing.Optional[int]

### elapsed
- **Type**: typing.Optional[int]

### cancelled
- **Type**: typing.Optional[bool]

### subqueries
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# QueryLanguageVersion

### version
- **Type**: <class 'str'>
- **Required**: Yes


# RDFGraphSummary

### numDistinctSubjects
- **Type**: typing.Optional[int]

### numDistinctPredicates
- **Type**: typing.Optional[int]

### numQuads
- **Type**: typing.Optional[int]

### numClasses
- **Type**: typing.Optional[int]

### classes
- **Type**: typing.Optional[typing.List[str]]

### predicates
- **Type**: typing.Optional[typing.List[typing.Dict[str, int]]]

### subjectStructures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.SubjectStructure]]


# RDFGraphSummaryValueMap

### version
- **Type**: typing.Optional[str]

### lastStatisticsComputationTime
- **Type**: typing.Optional[datetime.datetime]

### graphSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.RDFGraphSummary]


# RefreshStatisticsIdMap

### statisticsId
- **Type**: typing.Optional[str]


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


# SparqlData

### stmt
- **Type**: <class 'str'>
- **Required**: Yes


# SparqlRecord

### commitTimestampInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### eventId
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.SparqlData'>
- **Required**: Yes

### op
- **Type**: <class 'str'>
- **Required**: Yes

### isLastOp
- **Type**: typing.Optional[bool]


# StartLoaderJobInput

### source
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['csv', 'nquads', 'ntriples', 'opencypher', 'rdfxml', 'turtle']
- **Required**: Yes

### s3BucketRegion
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-west-1', 'us-west-2']
- **Required**: Yes

### iamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'NEW', 'RESUME']]

### failOnError
- **Type**: typing.Optional[bool]

### parallelism
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'OVERSUBSCRIBE']]

### parserConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### updateSingleCardinalityProperties
- **Type**: typing.Optional[bool]

### queueRequest
- **Type**: typing.Optional[bool]

### dependencies
- **Type**: typing.Optional[typing.List[str]]

### userProvidedEdgeIds
- **Type**: typing.Optional[bool]


# StartLoaderJobOutput

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# StartMLDataProcessingJobInput

### inputDataS3Location
- **Type**: <class 'str'>
- **Required**: Yes

### processedDataS3Location
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### previousDataProcessingJobId
- **Type**: typing.Optional[str]

### sagemakerIamRoleArn
- **Type**: typing.Optional[str]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### processingInstanceType
- **Type**: typing.Optional[str]

### processingInstanceVolumeSizeInGB
- **Type**: typing.Optional[int]

### processingTimeOutInSeconds
- **Type**: typing.Optional[int]

### modelType
- **Type**: typing.Optional[str]

### configFileName
- **Type**: typing.Optional[str]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### volumeEncryptionKMSKey
- **Type**: typing.Optional[str]

### s3OutputEncryptionKMSKey
- **Type**: typing.Optional[str]


# StartMLDataProcessingJobOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimeInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# StartMLModelTrainingJobInput

### dataProcessingJobId
- **Type**: <class 'str'>
- **Required**: Yes

### trainModelS3Location
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### previousModelTrainingJobId
- **Type**: typing.Optional[str]

### sagemakerIamRoleArn
- **Type**: typing.Optional[str]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### baseProcessingInstanceType
- **Type**: typing.Optional[str]

### trainingInstanceType
- **Type**: typing.Optional[str]

### trainingInstanceVolumeSizeInGB
- **Type**: typing.Optional[int]

### trainingTimeOutInSeconds
- **Type**: typing.Optional[int]

### maxHPONumberOfTrainingJobs
- **Type**: typing.Optional[int]

### maxHPOParallelTrainingJobs
- **Type**: typing.Optional[int]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### volumeEncryptionKMSKey
- **Type**: typing.Optional[str]

### s3OutputEncryptionKMSKey
- **Type**: typing.Optional[str]

### enableManagedSpotTraining
- **Type**: typing.Optional[bool]

### customModelTrainingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.CustomModelTrainingParameters]


# StartMLModelTrainingJobOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimeInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# StartMLModelTransformJobInput

### modelTransformOutputS3Location
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### dataProcessingJobId
- **Type**: typing.Optional[str]

### mlModelTrainingJobId
- **Type**: typing.Optional[str]

### trainingJobName
- **Type**: typing.Optional[str]

### sagemakerIamRoleArn
- **Type**: typing.Optional[str]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### customModelTransformParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.CustomModelTransformParameters]

### baseProcessingInstanceType
- **Type**: typing.Optional[str]

### baseProcessingInstanceVolumeSizeInGB
- **Type**: typing.Optional[int]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### volumeEncryptionKMSKey
- **Type**: typing.Optional[str]

### s3OutputEncryptionKMSKey
- **Type**: typing.Optional[str]


# StartMLModelTransformJobOutput

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimeInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.ResponseMetadata'>
- **Required**: Yes


# Statistics

### autoCompute
- **Type**: typing.Optional[bool]

### active
- **Type**: typing.Optional[bool]

### statisticsId
- **Type**: typing.Optional[str]

### date
- **Type**: typing.Optional[datetime.datetime]

### note
- **Type**: typing.Optional[str]

### signatureInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata.neptunedata_classes.StatisticsSummary]


# StatisticsSummary

### signatureCount
- **Type**: typing.Optional[int]

### instanceCount
- **Type**: typing.Optional[int]

### predicateCount
- **Type**: typing.Optional[int]


# SubjectStructure

### count
- **Type**: typing.Optional[int]

### predicates
- **Type**: typing.Optional[typing.List[str]]


