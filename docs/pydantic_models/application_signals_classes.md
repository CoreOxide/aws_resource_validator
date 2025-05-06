# Application Signals Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetServiceLevelObjectiveBudgetReportInput

### Timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### SloIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetServiceLevelObjectiveBudgetReportOutput

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelObjectiveBudgetReport]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelObjectiveBudgetReportError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes


# BurnRateConfiguration

### LookBackWindowMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# CalendarInterval

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### DurationUnit
- **Type**: typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH']
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# CalendarIntervalOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationUnit
- **Type**: typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH']
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# CreateServiceLevelObjectiveInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelIndicatorConfig]

### RequestBasedSliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.RequestBasedServiceLevelIndicatorConfig]

### Goal
- **Type**: typing.Union[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Goal, aws_resource_validator.pydantic_models.application_signals.application_signals_classes.GoalOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Tag]]

### BurnRateConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.BurnRateConfiguration]]


# CreateServiceLevelObjectiveOutput

### Slo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelObjective'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceLevelObjectiveInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# Dimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceInput

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# GetServiceLevelObjectiveInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceLevelObjectiveOutput

### Slo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelObjective'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceOutput

### Service
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Service'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes


# Goal

### Interval
- **Type**: <class 'NoneType'>

### AttainmentGoal
- **Type**: typing.Optional[float]

### WarningThreshold
- **Type**: typing.Optional[float]


# GoalOutput

### Interval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.IntervalOutput]

### AttainmentGoal
- **Type**: typing.Optional[float]

### WarningThreshold
- **Type**: typing.Optional[float]


# Interval

### RollingInterval
- **Type**: <class 'NoneType'>

### CalendarInterval
- **Type**: <class 'NoneType'>


# IntervalOutput

### RollingInterval
- **Type**: <class 'NoneType'>

### CalendarInterval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.CalendarIntervalOutput]


# ListServiceDependenciesInput

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServiceDependenciesInputPaginate

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.PaginatorConfig]


# ListServiceDependenciesOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceDependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceDependency]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceDependentsInput

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServiceDependentsInputPaginate

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.PaginatorConfig]


# ListServiceDependentsOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceDependents
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceDependent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceLevelObjectivesInput

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

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


# ListServiceLevelObjectivesInputPaginate

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### SloOwnerAwsAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.PaginatorConfig]


# ListServiceLevelObjectivesOutput

### SloSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelObjectiveSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceOperationsInput

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServiceOperationsInputPaginate

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.PaginatorConfig]


# ListServiceOperationsOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceOperation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesInput

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### AwsAccountId
- **Type**: typing.Optional[str]


# ListServicesInputPaginate

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### AwsAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.PaginatorConfig]


# ListServicesOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes


# Metric

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Dimension]]


# MetricDataQuery

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Union[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricStat, aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricStatOutput, NoneType]

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


# MetricDataQueryOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricStatOutput]

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


# MetricOutput

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Dimension]]


# MetricReference

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Dimension]]

### AccountId
- **Type**: typing.Optional[str]


# MetricStat

### Metric
- **Type**: typing.Union[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Metric, aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricOutput]
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricStatOutput

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricOutput'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MonitoredRequestCountMetricDataQueries

### GoodCountMetric
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQuery, aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQueryOutput]]]

### BadCountMetric
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQuery]]


# MonitoredRequestCountMetricDataQueriesOutput

### GoodCountMetric
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQueryOutput]]

### BadCountMetric
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQueryOutput]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RequestBasedServiceLevelIndicator

### RequestBasedSliMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.RequestBasedServiceLevelIndicatorMetric'>
- **Required**: Yes

### MetricThreshold
- **Type**: typing.Optional[float]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo']]


# RequestBasedServiceLevelIndicatorConfig

### RequestBasedSliMetricConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.RequestBasedServiceLevelIndicatorMetricConfig'>
- **Required**: Yes

### MetricThreshold
- **Type**: typing.Optional[float]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo']]


# RequestBasedServiceLevelIndicatorMetric

### TotalRequestCountMetric
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQueryOutput]
- **Required**: Yes

### MonitoredRequestCountMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MonitoredRequestCountMetricDataQueriesOutput'>
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MetricType
- **Type**: typing.Optional[typing.Literal['AVAILABILITY', 'LATENCY']]


# RequestBasedServiceLevelIndicatorMetricConfig

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MetricType
- **Type**: typing.Optional[typing.Literal['AVAILABILITY', 'LATENCY']]

### TotalRequestCountMetric
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQuery, aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQueryOutput]]]

### MonitoredRequestCountMetric
- **Type**: typing.Union[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MonitoredRequestCountMetricDataQueries, aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MonitoredRequestCountMetricDataQueriesOutput, NoneType]


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


# RollingInterval

### DurationUnit
- **Type**: typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH']
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# Service

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricReference]
- **Required**: Yes

### AttributeMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]

### LogGroupReferences
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]


# ServiceDependency

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricReference]
- **Required**: Yes


# ServiceDependent

### DependentKeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricReference]
- **Required**: Yes

### OperationName
- **Type**: typing.Optional[str]

### DependentOperationName
- **Type**: typing.Optional[str]


# ServiceLevelIndicator

### SliMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelIndicatorMetric'>
- **Required**: Yes

### MetricThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo']
- **Required**: Yes


# ServiceLevelIndicatorConfig

### SliMetricConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelIndicatorMetricConfig'>
- **Required**: Yes

### MetricThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThan', 'GreaterThanOrEqualTo', 'LessThan', 'LessThanOrEqualTo']
- **Required**: Yes


# ServiceLevelIndicatorMetric

### MetricDataQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQueryOutput]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MetricType
- **Type**: typing.Optional[typing.Literal['AVAILABILITY', 'LATENCY']]


# ServiceLevelIndicatorMetricConfig

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MetricType
- **Type**: typing.Optional[typing.Literal['AVAILABILITY', 'LATENCY']]

### Statistic
- **Type**: typing.Optional[str]

### PeriodSeconds
- **Type**: typing.Optional[int]

### MetricDataQueries
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQuery, aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricDataQueryOutput]]]


# ServiceLevelObjective

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
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.GoalOutput'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Sli
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelIndicator]

### RequestBasedSli
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.RequestBasedServiceLevelIndicator]

### EvaluationType
- **Type**: typing.Optional[typing.Literal['PeriodBased', 'RequestBased']]

### BurnRateConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.BurnRateConfiguration]]


# ServiceLevelObjectiveBudgetReport

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelIndicator]

### RequestBasedSli
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.RequestBasedServiceLevelIndicator]

### Goal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.GoalOutput]


# ServiceLevelObjectiveBudgetReportError

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


# ServiceLevelObjectiveSummary

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


# ServiceOperation

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricReference]
- **Required**: Yes


# ServiceSummary

### KeyAttributes
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MetricReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.MetricReference]
- **Required**: Yes

### AttributeMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateServiceLevelObjectiveInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelIndicatorConfig]

### RequestBasedSliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.RequestBasedServiceLevelIndicatorConfig]

### Goal
- **Type**: typing.Union[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.Goal, aws_resource_validator.pydantic_models.application_signals.application_signals_classes.GoalOutput, NoneType]

### BurnRateConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_signals.application_signals_classes.BurnRateConfiguration]]


# UpdateServiceLevelObjectiveOutput

### Slo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ServiceLevelObjective'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals.application_signals_classes.ResponseMetadata'>
- **Required**: Yes


