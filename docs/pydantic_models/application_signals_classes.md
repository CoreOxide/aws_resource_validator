# application_signals_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef

### Timestamp
- **Type**: typing.Union[datetime.datetime, str]
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


# CalendarIntervalOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationUnit
- **Type**: typing.Literal['DAY', 'MONTH']
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# CalendarIntervalTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### DurationUnit
- **Type**: typing.Literal['DAY', 'MONTH']
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes


# CreateServiceLevelObjectiveInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SliConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Goal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.GoalTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.TagTypeDef]]


# CreateServiceLevelObjectiveOutputTypeDef

### Slo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelObjectiveTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceLevelObjectiveInputRequestTypeDef

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


# GetServiceInputRequestTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# GetServiceLevelObjectiveInputRequestTypeDef

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


# ListServiceDependenciesInputListServiceDependenciesPaginateTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServiceDependenciesInputRequestTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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


# ListServiceDependentsInputListServiceDependentsPaginateTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServiceDependentsInputRequestTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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


# ListServiceLevelObjectivesInputListServiceLevelObjectivesPaginateTypeDef

### KeyAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServiceLevelObjectivesInputRequestTypeDef

### KeyAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OperationName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
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


# ListServiceOperationsInputListServiceOperationsPaginateTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### KeyAttributes
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServiceOperationsInputRequestTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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


# ListServicesInputListServicesPaginateTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.PaginatorConfigTypeDef]


# ListServicesInputRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.MetricStatTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.MetricTypeDef'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.DimensionTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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
- **Type**: typing.Literal['DAY', 'MONTH']
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_signals_classes.MetricDataQueryTypeDef]]


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

### Attainment
- **Type**: typing.Optional[float]

### TotalBudgetSeconds
- **Type**: typing.Optional[int]

### BudgetSecondsRemaining
- **Type**: typing.Optional[int]

### Sli
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorTypeDef]

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

### Sli
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorTypeDef'>
- **Required**: Yes

### Goal
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.GoalOutputTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateServiceLevelObjectiveInputRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SliConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelIndicatorConfigTypeDef]

### Goal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_signals_classes.GoalTypeDef]


# UpdateServiceLevelObjectiveOutputTypeDef

### Slo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ServiceLevelObjectiveTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_signals_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


