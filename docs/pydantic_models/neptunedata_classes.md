# Neptunedata Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelGremlinQueryInputRequestTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelGremlinQueryOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelLoaderJobInputRequestTypeDef

### loadId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelLoaderJobOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelMLDataProcessingJobInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### clean
- **Type**: typing.Optional[bool]


# CancelMLDataProcessingJobOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelMLModelTrainingJobInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### clean
- **Type**: typing.Optional[bool]


# CancelMLModelTrainingJobOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelMLModelTransformJobInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### clean
- **Type**: typing.Optional[bool]


# CancelMLModelTransformJobOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelOpenCypherQueryInputRequestTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### silent
- **Type**: typing.Optional[bool]


# CancelOpenCypherQueryOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMLEndpointInputRequestTypeDef

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


# CreateMLEndpointOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomModelTrainingParametersTypeDef

### sourceS3DirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### trainingEntryPointScript
- **Type**: typing.Optional[str]

### transformEntryPointScript
- **Type**: typing.Optional[str]


# CustomModelTransformParametersTypeDef

### sourceS3DirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### transformEntryPointScript
- **Type**: typing.Optional[str]


# DeleteMLEndpointInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]

### clean
- **Type**: typing.Optional[bool]


# DeleteMLEndpointOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePropertygraphStatisticsOutputTypeDef

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.DeleteStatisticsValueMapTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSparqlStatisticsOutputTypeDef

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.DeleteStatisticsValueMapTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStatisticsValueMapTypeDef

### active
- **Type**: typing.Optional[bool]

### statisticsId
- **Type**: typing.Optional[str]


# EdgeStructureTypeDef

### count
- **Type**: typing.Optional[int]

### edgeProperties
- **Type**: typing.Optional[typing.List[str]]


# ExecuteFastResetInputRequestTypeDef

### action
- **Type**: typing.Literal['initiateDatabaseReset', 'performDatabaseReset']
- **Required**: Yes

### token
- **Type**: typing.Optional[str]


# ExecuteFastResetOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.FastResetTokenTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteGremlinExplainQueryInputRequestTypeDef

### gremlinQuery
- **Type**: <class 'str'>
- **Required**: Yes


# ExecuteGremlinExplainQueryOutputTypeDef

### output
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteGremlinProfileQueryInputRequestTypeDef

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


# ExecuteGremlinProfileQueryOutputTypeDef

### output
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteGremlinQueryInputRequestTypeDef

### gremlinQuery
- **Type**: <class 'str'>
- **Required**: Yes

### serializer
- **Type**: typing.Optional[str]


# ExecuteGremlinQueryOutputTypeDef

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.GremlinQueryStatusAttributesTypeDef'>
- **Required**: Yes

### result
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### meta
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteOpenCypherExplainQueryInputRequestTypeDef

### openCypherQuery
- **Type**: <class 'str'>
- **Required**: Yes

### explainMode
- **Type**: typing.Literal['details', 'dynamic', 'static']
- **Required**: Yes

### parameters
- **Type**: typing.Optional[str]


# ExecuteOpenCypherExplainQueryOutputTypeDef

### results
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteOpenCypherQueryInputRequestTypeDef

### openCypherQuery
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[str]


# ExecuteOpenCypherQueryOutputTypeDef

### results
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FastResetTokenTypeDef

### token
- **Type**: typing.Optional[str]


# GetEngineStatusOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.QueryLanguageVersionTypeDef'>
- **Required**: Yes

### sparql
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.QueryLanguageVersionTypeDef'>
- **Required**: Yes

### opencypher
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.QueryLanguageVersionTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGremlinQueryStatusInputRequestTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGremlinQueryStatusOutputTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryEvalStats
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.QueryEvalStatsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoaderJobStatusInputRequestTypeDef

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


# GetLoaderJobStatusOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLDataProcessingJobInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# GetMLDataProcessingJobOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### processingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.MlResourceDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLEndpointInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# GetMLEndpointOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.MlResourceDefinitionTypeDef'>
- **Required**: Yes

### endpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.MlConfigDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLModelTrainingJobInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# GetMLModelTrainingJobOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### processingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.MlResourceDefinitionTypeDef'>
- **Required**: Yes

### hpoJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.MlResourceDefinitionTypeDef'>
- **Required**: Yes

### modelTransformJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.MlResourceDefinitionTypeDef'>
- **Required**: Yes

### mlModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.MlConfigDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLModelTransformJobInputRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# GetMLModelTransformJobOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### baseProcessingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.MlResourceDefinitionTypeDef'>
- **Required**: Yes

### remoteModelTransformJob
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.MlResourceDefinitionTypeDef'>
- **Required**: Yes

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.MlConfigDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOpenCypherQueryStatusInputRequestTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOpenCypherQueryStatusOutputTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryEvalStats
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.QueryEvalStatsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPropertygraphStatisticsOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.StatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPropertygraphStreamInputRequestTypeDef

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


# GetPropertygraphStreamOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.PropertygraphRecordTypeDef]
- **Required**: Yes

### totalRecords
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPropertygraphSummaryInputRequestTypeDef

### mode
- **Type**: typing.Optional[typing.Literal['basic', 'detailed']]


# GetPropertygraphSummaryOutputTypeDef

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.PropertygraphSummaryValueMapTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRDFGraphSummaryInputRequestTypeDef

### mode
- **Type**: typing.Optional[typing.Literal['basic', 'detailed']]


# GetRDFGraphSummaryOutputTypeDef

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.RDFGraphSummaryValueMapTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSparqlStatisticsOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.StatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSparqlStreamInputRequestTypeDef

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


# GetSparqlStreamOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.SparqlRecordTypeDef]
- **Required**: Yes

### totalRecords
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GremlinQueryStatusAttributesTypeDef

### message
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[int]

### attributes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# GremlinQueryStatusTypeDef

### queryId
- **Type**: typing.Optional[str]

### queryString
- **Type**: typing.Optional[str]

### queryEvalStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata_classes.QueryEvalStatsTypeDef]


# ListGremlinQueriesInputRequestTypeDef

### includeWaiting
- **Type**: typing.Optional[bool]


# ListGremlinQueriesOutputTypeDef

### acceptedQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### runningQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.GremlinQueryStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLoaderJobsInputRequestTypeDef

### limit
- **Type**: typing.Optional[int]

### includeQueuedLoads
- **Type**: typing.Optional[bool]


# ListLoaderJobsOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.LoaderIdResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMLDataProcessingJobsInputRequestTypeDef

### maxItems
- **Type**: typing.Optional[int]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# ListMLDataProcessingJobsOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMLEndpointsInputRequestTypeDef

### maxItems
- **Type**: typing.Optional[int]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# ListMLEndpointsOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMLModelTrainingJobsInputRequestTypeDef

### maxItems
- **Type**: typing.Optional[int]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# ListMLModelTrainingJobsOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMLModelTransformJobsInputRequestTypeDef

### maxItems
- **Type**: typing.Optional[int]

### neptuneIamRoleArn
- **Type**: typing.Optional[str]


# ListMLModelTransformJobsOutputTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOpenCypherQueriesInputRequestTypeDef

### includeWaiting
- **Type**: typing.Optional[bool]


# ListOpenCypherQueriesOutputTypeDef

### acceptedQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### runningQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.GremlinQueryStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoaderIdResultTypeDef

### loadIds
- **Type**: typing.Optional[typing.List[str]]


# ManagePropertygraphStatisticsInputRequestTypeDef

### mode
- **Type**: typing.Optional[typing.Literal['disableAutoCompute', 'enableAutoCompute', 'refresh']]


# ManagePropertygraphStatisticsOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.RefreshStatisticsIdMapTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManageSparqlStatisticsInputRequestTypeDef

### mode
- **Type**: typing.Optional[typing.Literal['disableAutoCompute', 'enableAutoCompute', 'refresh']]


# ManageSparqlStatisticsOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.RefreshStatisticsIdMapTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MlConfigDefinitionTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# MlResourceDefinitionTypeDef

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


# NodeStructureTypeDef

### count
- **Type**: typing.Optional[int]

### nodeProperties
- **Type**: typing.Optional[typing.List[str]]

### distinctOutgoingEdgeLabels
- **Type**: typing.Optional[typing.List[str]]


# PropertygraphDataTypeDef

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

### to
- **Type**: typing.Optional[str]


# PropertygraphRecordTypeDef

### commitTimestampInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### eventId
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.PropertygraphDataTypeDef'>
- **Required**: Yes

### op
- **Type**: <class 'str'>
- **Required**: Yes

### isLastOp
- **Type**: typing.Optional[bool]


# PropertygraphSummaryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.NodeStructureTypeDef]]

### edgeStructures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.EdgeStructureTypeDef]]


# PropertygraphSummaryValueMapTypeDef

### version
- **Type**: typing.Optional[str]

### lastStatisticsComputationTime
- **Type**: typing.Optional[datetime.datetime]

### graphSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata_classes.PropertygraphSummaryTypeDef]


# QueryEvalStatsTypeDef

### waited
- **Type**: typing.Optional[int]

### elapsed
- **Type**: typing.Optional[int]

### cancelled
- **Type**: typing.Optional[bool]

### subqueries
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# QueryLanguageVersionTypeDef

### version
- **Type**: <class 'str'>
- **Required**: Yes


# RDFGraphSummaryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.neptunedata_classes.SubjectStructureTypeDef]]


# RDFGraphSummaryValueMapTypeDef

### version
- **Type**: typing.Optional[str]

### lastStatisticsComputationTime
- **Type**: typing.Optional[datetime.datetime]

### graphSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata_classes.RDFGraphSummaryTypeDef]


# RefreshStatisticsIdMapTypeDef

### statisticsId
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# SparqlDataTypeDef

### stmt
- **Type**: <class 'str'>
- **Required**: Yes


# SparqlRecordTypeDef

### commitTimestampInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### eventId
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.SparqlDataTypeDef'>
- **Required**: Yes

### op
- **Type**: <class 'str'>
- **Required**: Yes

### isLastOp
- **Type**: typing.Optional[bool]


# StartLoaderJobInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### updateSingleCardinalityProperties
- **Type**: typing.Optional[bool]

### queueRequest
- **Type**: typing.Optional[bool]

### dependencies
- **Type**: typing.Optional[typing.Sequence[str]]

### userProvidedEdgeIds
- **Type**: typing.Optional[bool]


# StartLoaderJobOutputTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMLDataProcessingJobInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### volumeEncryptionKMSKey
- **Type**: typing.Optional[str]

### s3OutputEncryptionKMSKey
- **Type**: typing.Optional[str]


# StartMLDataProcessingJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMLModelTrainingJobInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### volumeEncryptionKMSKey
- **Type**: typing.Optional[str]

### s3OutputEncryptionKMSKey
- **Type**: typing.Optional[str]

### enableManagedSpotTraining
- **Type**: typing.Optional[bool]

### customModelTrainingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata_classes.CustomModelTrainingParametersTypeDef]


# StartMLModelTrainingJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMLModelTransformJobInputRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata_classes.CustomModelTransformParametersTypeDef]

### baseProcessingInstanceType
- **Type**: typing.Optional[str]

### baseProcessingInstanceVolumeSizeInGB
- **Type**: typing.Optional[int]

### subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### volumeEncryptionKMSKey
- **Type**: typing.Optional[str]

### s3OutputEncryptionKMSKey
- **Type**: typing.Optional[str]


# StartMLModelTransformJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.neptunedata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatisticsSummaryTypeDef

### signatureCount
- **Type**: typing.Optional[int]

### instanceCount
- **Type**: typing.Optional[int]

### predicateCount
- **Type**: typing.Optional[int]


# StatisticsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.neptunedata_classes.StatisticsSummaryTypeDef]


# SubjectStructureTypeDef

### count
- **Type**: typing.Optional[int]

### predicates
- **Type**: typing.Optional[typing.List[str]]


