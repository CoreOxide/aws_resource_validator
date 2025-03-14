# Application Signals Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetServiceLevelObjectiveBudgetReportInputTypeDef

### Timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### SloIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelObjectiveBudgetReportTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelObjectiveBudgetReportErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BurnRateConfigurationTypeDef

### LookBackWindowMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# CalendarIntervalOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationUnit
- **Type**: typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH']
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# CalendarIntervalTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### DurationUnit
- **Type**: typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH']
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# CreateServiceLevelObjectiveInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorConfigTypeDef]

### RequestBasedSliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.RequestBasedServiceLevelIndicatorConfigTypeDef]

### Goal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.GoalUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.TagTypeDef]]

### BurnRateConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.BurnRateConfigurationTypeDef]]


# CreateServiceLevelObjectiveOutputTypeDef

### Slo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelObjectiveTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceLevelObjectiveInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInputTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# GetServiceLevelObjectiveInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceLevelObjectiveOutputTypeDef

### Slo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelObjectiveTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceOutputTypeDef

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LogGroupReferences
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GoalOutputTypeDef

### Interval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.IntervalOutputTypeDef]

### AttainmentGoal
- **Type**: typing.Optional[float]

### WarningThreshold
- **Type**: typing.Optional[float]


# GoalTypeDef

### Interval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.IntervalTypeDef]

### AttainmentGoal
- **Type**: typing.Optional[float]

### WarningThreshold
- **Type**: typing.Optional[float]


# GoalUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntervalOutputTypeDef

### RollingInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.RollingIntervalTypeDef]

### CalendarInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.CalendarIntervalOutputTypeDef]


# IntervalTypeDef

### RollingInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.RollingIntervalTypeDef]

### CalendarInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.CalendarIntervalTypeDef]


# ListServiceDependenciesInputPaginateTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServiceDependenciesInputTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServiceDependenciesOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceDependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.ServiceDependencyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceDependentsInputPaginateTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServiceDependentsInputTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServiceDependentsOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceDependents
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.ServiceDependentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceLevelObjectivesInputPaginateTypeDef

### KeyAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### SloOwnerAwsAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServiceLevelObjectivesInputTypeDef

### KeyAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### SloOwnerAwsAccountId
- **Type**: typing.Optional[str]


# ListServiceLevelObjectivesOutputTypeDef

### SloSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelObjectiveSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceOperationsInputPaginateTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServiceOperationsInputTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServiceOperationsOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.ServiceOperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesInputPaginateTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### AwsAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServicesInputTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.TimestampTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### AwsAccountId
- **Type**: typing.Optional[str]


# ListServicesOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.ServiceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricDataQueryOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.MetricStatOutputTypeDef]

### Expression
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]

### Period
- **Type**: typing.Optional[int]

### AccountId
- **Type**: typing.Optional[str]


# MetricDataQueryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.MetricStatUnionTypeDef]

### Expression
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### ReturnData
- **Type**: typing.Optional[bool]

### Period
- **Type**: typing.Optional[int]

### AccountId
- **Type**: typing.Optional[str]


# MetricDataQueryUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetricOutputTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals_classes.DimensionTypeDef]]


# MetricReferenceTypeDef

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricType
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals_classes.DimensionTypeDef]]

### AccountId
- **Type**: typing.Optional[str]


# MetricStatOutputTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.MetricOutputTypeDef'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricStatTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.MetricUnionTypeDef'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricStatUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetricTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.DimensionTypeDef]]


# MetricUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MonitoredRequestCountMetricDataQueriesOutputTypeDef

### GoodCountMetric
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryOutputTypeDef]]

### BadCountMetric
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryOutputTypeDef]]


# MonitoredRequestCountMetricDataQueriesTypeDef

### GoodCountMetric
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryUnionTypeDef]]

### BadCountMetric
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryTypeDef]]


# MonitoredRequestCountMetricDataQueriesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RequestBasedServiceLevelIndicatorConfigTypeDef

### RequestBasedSliMetricConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.RequestBasedServiceLevelIndicatorMetricConfigTypeDef'>
- **Required**: Yes

### MetricThreshold
- **Type**: typing.Optional[float]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo']]


# RequestBasedServiceLevelIndicatorMetricConfigTypeDef

### KeyAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MetricType
- **Type**: typing.Optional[typing.Literal['AVAILABILITY', 'LATENCY']]

### TotalRequestCountMetric
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryUnionTypeDef]]

### MonitoredRequestCountMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.MonitoredRequestCountMetricDataQueriesUnionTypeDef]


# RequestBasedServiceLevelIndicatorMetricTypeDef

### TotalRequestCountMetric
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryOutputTypeDef]
- **Required**: Yes

### MonitoredRequestCountMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.MonitoredRequestCountMetricDataQueriesOutputTypeDef'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MetricType
- **Type**: typing.Optional[typing.Literal['AVAILABILITY', 'LATENCY']]


# RequestBasedServiceLevelIndicatorTypeDef

### RequestBasedSliMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.RequestBasedServiceLevelIndicatorMetricTypeDef'>
- **Required**: Yes

### MetricThreshold
- **Type**: typing.Optional[float]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo']]


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


# RollingIntervalTypeDef

### DurationUnit
- **Type**: typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH']
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# ServiceDependencyTypeDef

### OperationName
- **Type**: <class 'str'>
- **Required**: Yes

### DependencyKeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### DependencyOperationName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricReferenceTypeDef]
- **Required**: Yes


# ServiceDependentTypeDef

### DependentKeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricReferenceTypeDef]
- **Required**: Yes

### OperationName
- **Type**: typing.Optional[str]

### DependentOperationName
- **Type**: typing.Optional[str]


# ServiceLevelIndicatorConfigTypeDef

### SliMetricConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorMetricConfigTypeDef'>
- **Required**: Yes

### MetricThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo']
- **Required**: Yes


# ServiceLevelIndicatorMetricConfigTypeDef

### KeyAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MetricType
- **Type**: typing.Optional[typing.Literal['AVAILABILITY', 'LATENCY']]

### Statistic
- **Type**: typing.Optional[str]

### PeriodSeconds
- **Type**: typing.Optional[int]

### MetricDataQueries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryUnionTypeDef]]


# ServiceLevelIndicatorMetricTypeDef

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryOutputTypeDef]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MetricType
- **Type**: typing.Optional[typing.Literal['AVAILABILITY', 'LATENCY']]


# ServiceLevelIndicatorTypeDef

### SliMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorMetricTypeDef'>
- **Required**: Yes

### MetricThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo']
- **Required**: Yes


# ServiceLevelObjectiveBudgetReportErrorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceLevelObjectiveBudgetReportTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### BudgetStatus
- **Type**: typing.Literal['BREACHED', 'INSUFFICIENT_DATA', 'OK', 'WARNING']
- **Required**: Yes

### EvaluationType
- **Type**: typing.Optional[typing.Literal['PeriodBased', 'RequestBased']]

### Attainment
- **Type**: typing.Optional[float]

### TotalBudgetSeconds
- **Type**: typing.Optional[int]

### BudgetSecondsRemaining
- **Type**: typing.Optional[int]

### TotalBudgetRequests
- **Type**: typing.Optional[int]

### BudgetRequestsRemaining
- **Type**: typing.Optional[int]

### Sli
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorTypeDef]

### RequestBasedSli
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.RequestBasedServiceLevelIndicatorTypeDef]

### Goal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.GoalOutputTypeDef]


# ServiceLevelObjectiveSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# ServiceLevelObjectiveTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Goal
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.GoalOutputTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Sli
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorTypeDef]

### RequestBasedSli
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.RequestBasedServiceLevelIndicatorTypeDef]

### EvaluationType
- **Type**: typing.Optional[typing.Literal['PeriodBased', 'RequestBased']]

### BurnRateConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals_classes.BurnRateConfigurationTypeDef]]


# ServiceOperationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricReferenceTypeDef]
- **Required**: Yes


# ServiceSummaryTypeDef

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricReferenceTypeDef]
- **Required**: Yes

### AttributeMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]


# ServiceTypeDef

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals_classes.MetricReferenceTypeDef]
- **Required**: Yes

### AttributeMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]

### LogGroupReferences
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateServiceLevelObjectiveInputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorConfigTypeDef]

### RequestBasedSliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.RequestBasedServiceLevelIndicatorConfigTypeDef]

### Goal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.GoalUnionTypeDef]

### BurnRateConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.BurnRateConfigurationTypeDef]]


# UpdateServiceLevelObjectiveOutputTypeDef

### Slo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelObjectiveTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


