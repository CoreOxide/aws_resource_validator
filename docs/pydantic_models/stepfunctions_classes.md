# Stepfunctions Classes

# ActivityFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ActivityListItemTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ActivityScheduleFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ActivityStartedEventDetailsTypeDef

### workerName
- **Type**: typing.Optional[str]


# ActivitySucceededEventDetailsTypeDef

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# ActivityTimedOutEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# AssignedVariablesDetailsTypeDef

### truncated
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillingDetailsTypeDef

### billedMemoryUsedInMB
- **Type**: typing.Optional[int]

### billedDurationInMilliseconds
- **Type**: typing.Optional[int]


# CloudWatchEventsExecutionDataDetailsTypeDef

### included
- **Type**: typing.Optional[bool]


# CloudWatchLogsLogGroupTypeDef

### logGroupArn
- **Type**: typing.Optional[str]


# CreateActivityInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.TagTypeDef]]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.EncryptionConfigurationTypeDef]


# CreateActivityOutputTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStateMachineAliasInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItemTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateStateMachineAliasOutputTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStateMachineOutputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteActivityInputTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineAliasInputTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineInputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineVersionInputTypeDef

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActivityInputTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActivityOutputTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### encryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.EncryptionConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExecutionInputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[typing.Literal['ALL_DATA', 'METADATA_ONLY']]


# DescribeMapRunInputTypeDef

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMapRunOutputTypeDef

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ABORTED', 'FAILED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### maxConcurrency
- **Type**: <class 'int'>
- **Required**: Yes

### toleratedFailurePercentage
- **Type**: <class 'float'>
- **Required**: Yes

### toleratedFailureCount
- **Type**: <class 'int'>
- **Required**: Yes

### itemCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunItemCountsTypeDef'>
- **Required**: Yes

### executionCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunExecutionCountsTypeDef'>
- **Required**: Yes

### redriveCount
- **Type**: <class 'int'>
- **Required**: Yes

### redriveDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStateMachineAliasInputTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStateMachineAliasOutputTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItemTypeDef]
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStateMachineForExecutionInputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[typing.Literal['ALL_DATA', 'METADATA_ONLY']]


# DescribeStateMachineForExecutionOutputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### loggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### tracingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.TracingConfigurationTypeDef'>
- **Required**: Yes

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### label
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.EncryptionConfigurationTypeDef'>
- **Required**: Yes

### variableReferences
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStateMachineInputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[typing.Literal['ALL_DATA', 'METADATA_ONLY']]


# EncryptionConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFailedEventDetailsTypeDef

### state
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[str]


# ExecutionAbortedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ExecutionFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ExecutionListItemTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ABORTED', 'FAILED', 'PENDING_REDRIVE', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopDate
- **Type**: typing.Optional[datetime.datetime]

### mapRunArn
- **Type**: typing.Optional[str]

### itemCount
- **Type**: typing.Optional[int]

### stateMachineVersionArn
- **Type**: typing.Optional[str]

### stateMachineAliasArn
- **Type**: typing.Optional[str]

### redriveCount
- **Type**: typing.Optional[int]

### redriveDate
- **Type**: typing.Optional[datetime.datetime]


# ExecutionRedrivenEventDetailsTypeDef

### redriveCount
- **Type**: typing.Optional[int]


# ExecutionSucceededEventDetailsTypeDef

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# ExecutionTimedOutEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# GetActivityTaskInputTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### workerName
- **Type**: typing.Optional[str]


# GetExecutionHistoryInputPaginateTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### reverseOrder
- **Type**: typing.Optional[bool]

### includeExecutionData
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# GetExecutionHistoryInputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### includeExecutionData
- **Type**: typing.Optional[bool]


# GetExecutionHistoryOutputTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# HistoryEventExecutionDataDetailsTypeDef

### truncated
- **Type**: typing.Optional[bool]


# HistoryEventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InspectionDataRequestTypeDef

### protocol
- **Type**: typing.Optional[str]

### method
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]


# InspectionDataResponseTypeDef

### protocol
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]


# InspectionDataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LambdaFunctionFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionScheduleFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionStartFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionSucceededEventDetailsTypeDef

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# LambdaFunctionTimedOutEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ListActivitiesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# ListActivitiesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActivitiesOutputTypeDef

### activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivityListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExecutionsInputPaginateTypeDef

### stateMachineArn
- **Type**: typing.Optional[str]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'PENDING_REDRIVE', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']]

### mapRunArn
- **Type**: typing.Optional[str]

### redriveFilter
- **Type**: typing.Optional[typing.Literal['NOT_REDRIVEN', 'REDRIVEN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# ListExecutionsInputTypeDef

### stateMachineArn
- **Type**: typing.Optional[str]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'PENDING_REDRIVE', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### mapRunArn
- **Type**: typing.Optional[str]

### redriveFilter
- **Type**: typing.Optional[typing.Literal['NOT_REDRIVEN', 'REDRIVEN']]


# ListExecutionsOutputTypeDef

### executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMapRunsInputPaginateTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# ListMapRunsInputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMapRunsOutputTypeDef

### mapRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachineAliasesInputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStateMachineAliasesOutputTypeDef

### stateMachineAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineAliasListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachineVersionsInputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStateMachineVersionsOutputTypeDef

### stateMachineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineVersionListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachinesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# ListStateMachinesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachinesOutputTypeDef

### stateMachines
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogDestinationTypeDef

### cloudWatchLogsLogGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.CloudWatchLogsLogGroupTypeDef]


# LoggingConfigurationOutputTypeDef

### level
- **Type**: typing.Optional[typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']]

### includeExecutionData
- **Type**: typing.Optional[bool]

### destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.LogDestinationTypeDef]]


# LoggingConfigurationTypeDef

### level
- **Type**: typing.Optional[typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']]

### includeExecutionData
- **Type**: typing.Optional[bool]

### destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.LogDestinationTypeDef]]


# LoggingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MapIterationEventDetailsTypeDef

### name
- **Type**: typing.Optional[str]

### index
- **Type**: typing.Optional[int]


# MapRunExecutionCountsTypeDef

### pending
- **Type**: <class 'int'>
- **Required**: Yes

### running
- **Type**: <class 'int'>
- **Required**: Yes

### succeeded
- **Type**: <class 'int'>
- **Required**: Yes

### failed
- **Type**: <class 'int'>
- **Required**: Yes

### timedOut
- **Type**: <class 'int'>
- **Required**: Yes

### aborted
- **Type**: <class 'int'>
- **Required**: Yes

### total
- **Type**: <class 'int'>
- **Required**: Yes

### resultsWritten
- **Type**: <class 'int'>
- **Required**: Yes

### failuresNotRedrivable
- **Type**: typing.Optional[int]

### pendingRedrive
- **Type**: typing.Optional[int]


# MapRunFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# MapRunItemCountsTypeDef

### pending
- **Type**: <class 'int'>
- **Required**: Yes

### running
- **Type**: <class 'int'>
- **Required**: Yes

### succeeded
- **Type**: <class 'int'>
- **Required**: Yes

### failed
- **Type**: <class 'int'>
- **Required**: Yes

### timedOut
- **Type**: <class 'int'>
- **Required**: Yes

### aborted
- **Type**: <class 'int'>
- **Required**: Yes

### total
- **Type**: <class 'int'>
- **Required**: Yes

### resultsWritten
- **Type**: <class 'int'>
- **Required**: Yes

### failuresNotRedrivable
- **Type**: typing.Optional[int]

### pendingRedrive
- **Type**: typing.Optional[int]


# MapRunListItemTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopDate
- **Type**: typing.Optional[datetime.datetime]


# MapRunRedrivenEventDetailsTypeDef

### mapRunArn
- **Type**: typing.Optional[str]

### redriveCount
- **Type**: typing.Optional[int]


# MapRunStartedEventDetailsTypeDef

### mapRunArn
- **Type**: typing.Optional[str]


# MapStateStartedEventDetailsTypeDef

### length
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishStateMachineVersionInputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# PublishStateMachineVersionOutputTypeDef

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RedriveExecutionInputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# RedriveExecutionOutputTypeDef

### redriveDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
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


# RoutingConfigurationListItemTypeDef

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: <class 'int'>
- **Required**: Yes


# SendTaskFailureInputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# SendTaskHeartbeatInputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes


# SendTaskSuccessInputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# StartExecutionOutputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StateExitedEventDetailsTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]

### assignedVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### assignedVariablesDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.AssignedVariablesDetailsTypeDef]


# StateMachineAliasListItemTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# StateMachineListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StateMachineVersionListItemTypeDef

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# StopExecutionInputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# StopExecutionOutputTypeDef

### stopDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TaskCredentialsTypeDef

### roleArn
- **Type**: typing.Optional[str]


# TaskFailedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# TaskScheduledEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'str'>
- **Required**: Yes

### timeoutInSeconds
- **Type**: typing.Optional[int]

### heartbeatInSeconds
- **Type**: typing.Optional[int]

### taskCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskCredentialsTypeDef]


# TaskStartFailedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# TaskStartedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes


# TaskSubmitFailedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# TaskSubmittedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# TaskSucceededEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# TaskTimedOutEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# TestStateOutputTypeDef

### output
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: <class 'str'>
- **Required**: Yes

### inspectionData
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.InspectionDataTypeDef'>
- **Required**: Yes

### nextState
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CAUGHT_ERROR', 'FAILED', 'RETRIABLE', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TracingConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMapRunInputTypeDef

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxConcurrency
- **Type**: typing.Optional[int]

### toleratedFailurePercentage
- **Type**: typing.Optional[float]

### toleratedFailureCount
- **Type**: typing.Optional[int]


# UpdateStateMachineAliasInputTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### routingConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItemTypeDef]]


# UpdateStateMachineAliasOutputTypeDef

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStateMachineInputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### loggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LoggingConfigurationUnionTypeDef]

### tracingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TracingConfigurationTypeDef]

### publish
- **Type**: typing.Optional[bool]

### versionDescription
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.EncryptionConfigurationTypeDef]


# UpdateStateMachineOutputTypeDef

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateStateMachineDefinitionDiagnosticTypeDef

### severity
- **Type**: typing.Literal['ERROR', 'WARNING']
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]


# ValidateStateMachineDefinitionOutputTypeDef

### result
- **Type**: typing.Literal['FAIL', 'OK']
- **Required**: Yes

### diagnostics
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ValidateStateMachineDefinitionDiagnosticTypeDef]
- **Required**: Yes

### truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


