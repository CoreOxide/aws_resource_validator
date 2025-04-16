# Stepfunctions Classes

# ActivityFailedEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ActivityListItem

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ActivityScheduleFailedEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ActivityStartedEventDetails

### workerName
- **Type**: typing.Optional[str]


# ActivitySucceededEventDetails

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetails]


# ActivityTimedOutEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# AssignedVariablesDetails

### truncated
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillingDetails

### billedMemoryUsedInMB
- **Type**: typing.Optional[int]

### billedDurationInMilliseconds
- **Type**: typing.Optional[int]


# CloudWatchEventsExecutionDataDetails

### included
- **Type**: typing.Optional[bool]


# CloudWatchLogsLogGroup

### logGroupArn
- **Type**: typing.Optional[str]


# CreateActivityInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.Tag]]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.EncryptionConfiguration]


# CreateActivityOutput

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStateMachineAliasInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItem]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateStateMachineAliasOutput

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStateMachineOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteActivityInput

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineAliasInput

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineInput

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineVersionInput

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActivityInput

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActivityOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.EncryptionConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExecutionInput

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[typing.Literal['ALL_DATA', 'METADATA_ONLY']]


# DescribeMapRunInput

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMapRunOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunItemCounts'>
- **Required**: Yes

### executionCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunExecutionCounts'>
- **Required**: Yes

### redriveCount
- **Type**: <class 'int'>
- **Required**: Yes

### redriveDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStateMachineAliasInput

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStateMachineAliasOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItem]
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStateMachineForExecutionInput

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[typing.Literal['ALL_DATA', 'METADATA_ONLY']]


# DescribeStateMachineForExecutionOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### tracingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.TracingConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.EncryptionConfiguration'>
- **Required**: Yes

### variableReferences
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStateMachineInput

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### includedData
- **Type**: typing.Optional[typing.Literal['ALL_DATA', 'METADATA_ONLY']]


# EncryptionConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationFailedEventDetails

### state
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[str]


# ExecutionAbortedEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ExecutionFailedEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ExecutionListItem

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


# ExecutionRedrivenEventDetails

### redriveCount
- **Type**: typing.Optional[int]


# ExecutionSucceededEventDetails

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetails]


# ExecutionTimedOutEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# GetActivityTaskInput

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### workerName
- **Type**: typing.Optional[str]


# GetExecutionHistoryInput

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


# GetExecutionHistoryInputPaginate

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### reverseOrder
- **Type**: typing.Optional[bool]

### includeExecutionData
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfig]


# GetExecutionHistoryOutput

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# HistoryEvent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HistoryEventExecutionDataDetails

### truncated
- **Type**: typing.Optional[bool]


# InspectionData

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InspectionDataRequest

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


# InspectionDataResponse

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


# LambdaFunctionFailedEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionScheduleFailedEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionStartFailedEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionSucceededEventDetails

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetails]


# LambdaFunctionTimedOutEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ListActivitiesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActivitiesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfig]


# ListActivitiesOutput

### activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivityListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExecutionsInput

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


# ListExecutionsInputPaginate

### stateMachineArn
- **Type**: typing.Optional[str]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'PENDING_REDRIVE', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']]

### mapRunArn
- **Type**: typing.Optional[str]

### redriveFilter
- **Type**: typing.Optional[typing.Literal['NOT_REDRIVEN', 'REDRIVEN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfig]


# ListExecutionsOutput

### executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMapRunsInput

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMapRunsInputPaginate

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfig]


# ListMapRunsOutput

### mapRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachineAliasesInput

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStateMachineAliasesOutput

### stateMachineAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineAliasListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachineVersionsInput

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStateMachineVersionsOutput

### stateMachineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineVersionListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachinesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachinesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfig]


# ListStateMachinesOutput

### stateMachines
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# LogDestination

### cloudWatchLogsLogGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.CloudWatchLogsLogGroup]


# LoggingConfiguration

### level
- **Type**: typing.Optional[typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']]

### includeExecutionData
- **Type**: typing.Optional[bool]

### destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.LogDestination]]


# LoggingConfigurationOutput

### level
- **Type**: typing.Optional[typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']]

### includeExecutionData
- **Type**: typing.Optional[bool]

### destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.LogDestination]]


# LoggingConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MapIterationEventDetails

### name
- **Type**: typing.Optional[str]

### index
- **Type**: typing.Optional[int]


# MapRunExecutionCounts

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


# MapRunFailedEventDetails

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# MapRunItemCounts

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


# MapRunListItem

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


# MapRunRedrivenEventDetails

### mapRunArn
- **Type**: typing.Optional[str]

### redriveCount
- **Type**: typing.Optional[int]


# MapRunStartedEventDetails

### mapRunArn
- **Type**: typing.Optional[str]


# MapStateStartedEventDetails

### length
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishStateMachineVersionInput

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# PublishStateMachineVersionOutput

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# RedriveExecutionInput

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# RedriveExecutionOutput

### redriveDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
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


# RoutingConfigurationListItem

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: <class 'int'>
- **Required**: Yes


# SendTaskFailureInput

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# SendTaskHeartbeatInput

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes


# SendTaskSuccessInput

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# StartExecutionOutput

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# StateExitedEventDetails

### name
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetails]

### assignedVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### assignedVariablesDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.AssignedVariablesDetails]


# StateMachineAliasListItem

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# StateMachineListItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StateMachineVersionListItem

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# StopExecutionInput

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# StopExecutionOutput

### stopDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.Tag]
- **Required**: Yes


# TaskCredentials

### roleArn
- **Type**: typing.Optional[str]


# TaskFailedEventDetails

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


# TaskScheduledEventDetails

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskCredentials]


# TaskStartFailedEventDetails

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


# TaskStartedEventDetails

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes


# TaskSubmitFailedEventDetails

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


# TaskSubmittedEventDetails

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetails]


# TaskSucceededEventDetails

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetails]


# TaskTimedOutEventDetails

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


# TestStateOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.InspectionData'>
- **Required**: Yes

### nextState
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CAUGHT_ERROR', 'FAILED', 'RETRIABLE', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# TracingConfiguration

### enabled
- **Type**: typing.Optional[bool]


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMapRunInput

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxConcurrency
- **Type**: typing.Optional[int]

### toleratedFailurePercentage
- **Type**: typing.Optional[float]

### toleratedFailureCount
- **Type**: typing.Optional[int]


# UpdateStateMachineAliasInput

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### routingConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItem]]


# UpdateStateMachineAliasOutput

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStateMachineInput

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### loggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LoggingConfigurationUnion]

### tracingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TracingConfiguration]

### publish
- **Type**: typing.Optional[bool]

### versionDescription
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.EncryptionConfiguration]


# UpdateStateMachineOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


# ValidateStateMachineDefinitionDiagnostic

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


# ValidateStateMachineDefinitionOutput

### result
- **Type**: typing.Literal['FAIL', 'OK']
- **Required**: Yes

### diagnostics
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ValidateStateMachineDefinitionDiagnostic]
- **Required**: Yes

### truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadata'>
- **Required**: Yes


