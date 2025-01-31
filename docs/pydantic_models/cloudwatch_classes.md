# Cloudwatch Classes

# AlarmHistoryItemTypeDef

### AlarmName
- **Type**: typing.Optional[str]

### AlarmType
- **Type**: typing.Optional[typing.Literal['CompositeAlarm', 'MetricAlarm']]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### HistoryItemType
- **Type**: typing.Optional[typing.Literal['Action', 'ConfigurationUpdate', 'StateUpdate']]

### HistorySummary
- **Type**: typing.Optional[str]

### HistoryData
- **Type**: typing.Optional[str]


# AnomalyDetectorConfigurationTypeDef

### ExcludedTimeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.RangeTypeDef]]

### MetricTimezone
- **Type**: typing.Optional[str]


# AnomalyDetectorPaginatorTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Stat
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.AnomalyDetectorConfigurationTypeDef]

### StateValue
- **Type**: typing.Optional[typing.Literal['PENDING_TRAINING', 'TRAINED', 'TRAINED_INSUFFICIENT_DATA']]

### MetricCharacteristics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricCharacteristicsTypeDef]

### SingleMetricAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.SingleMetricAnomalyDetectorPaginatorTypeDef]

### MetricMathAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricMathAnomalyDetectorPaginatorTypeDef]


# AnomalyDetectorTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Stat
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.AnomalyDetectorConfigurationTypeDef]

### StateValue
- **Type**: typing.Optional[typing.Literal['PENDING_TRAINING', 'TRAINED', 'TRAINED_INSUFFICIENT_DATA']]

### MetricCharacteristics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricCharacteristicsTypeDef]

### SingleMetricAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.SingleMetricAnomalyDetectorTypeDef]

### MetricMathAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricMathAnomalyDetectorTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudwatchEventDetailConfigurationTypeDef

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.CloudwatchEventMetricTypeDef]]

### actionsSuppressor
- **Type**: typing.Optional[str]

### actionsSuppressorWaitPeriod
- **Type**: typing.Optional[int]

### actionsSuppressorExtensionPeriod
- **Type**: typing.Optional[int]

### threshold
- **Type**: typing.Optional[int]

### evaluationPeriods
- **Type**: typing.Optional[int]

### alarmRule
- **Type**: typing.Optional[str]

### alarmName
- **Type**: typing.Optional[str]

### treatMissingData
- **Type**: typing.Optional[str]

### comparisonOperator
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[str]

### actionsEnabled
- **Type**: typing.Optional[bool]

### okActions
- **Type**: typing.Optional[typing.List[str]]

### alarmActions
- **Type**: typing.Optional[typing.List[str]]

### insufficientDataActions
- **Type**: typing.Optional[typing.List[str]]


# CloudwatchEventDetailTypeDef

### alarmName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.CloudwatchEventStateTypeDef'>
- **Required**: Yes

### operation
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.CloudwatchEventDetailConfigurationTypeDef]

### previousConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.CloudwatchEventDetailConfigurationTypeDef]

### previousState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.CloudwatchEventStateTypeDef]


# CloudwatchEventMetricStatsMetricTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### dimensions
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# CloudwatchEventMetricStatsTypeDef

### period
- **Type**: <class 'str'>
- **Required**: Yes

### stat
- **Type**: <class 'str'>
- **Required**: Yes

### metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.CloudwatchEventMetricStatsMetricTypeDef]


# CloudwatchEventMetricTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### returnData
- **Type**: <class 'bool'>
- **Required**: Yes

### metricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.CloudwatchEventMetricStatsTypeDef]

### expression
- **Type**: typing.Optional[str]

### label
- **Type**: typing.Optional[str]

### period
- **Type**: typing.Optional[int]


# CloudwatchEventStateTypeDef

### timestamp
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### reasonData
- **Type**: typing.Optional[str]

### actionsSuppressedBy
- **Type**: typing.Optional[str]

### actionsSuppressedReason
- **Type**: typing.Optional[str]


# CloudwatchEventTypeDef

### version
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### account
- **Type**: <class 'str'>
- **Required**: Yes

### time
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### resources
- **Type**: typing.List[str]
- **Required**: Yes

### detail
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.CloudwatchEventDetailTypeDef'>
- **Required**: Yes


# CompositeAlarmTypeDef

### ActionsEnabled
- **Type**: typing.Optional[bool]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### AlarmArn
- **Type**: typing.Optional[str]

### AlarmConfigurationUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### AlarmDescription
- **Type**: typing.Optional[str]

### AlarmName
- **Type**: typing.Optional[str]

### AlarmRule
- **Type**: typing.Optional[str]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### OKActions
- **Type**: typing.Optional[typing.List[str]]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonData
- **Type**: typing.Optional[str]

### StateUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### StateValue
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### StateTransitionedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ActionsSuppressedBy
- **Type**: typing.Optional[typing.Literal['Alarm', 'ExtensionPeriod', 'WaitPeriod']]

### ActionsSuppressedReason
- **Type**: typing.Optional[str]

### ActionsSuppressor
- **Type**: typing.Optional[str]

### ActionsSuppressorWaitPeriod
- **Type**: typing.Optional[int]

### ActionsSuppressorExtensionPeriod
- **Type**: typing.Optional[int]


# DashboardEntryTypeDef

### DashboardName
- **Type**: typing.Optional[str]

### DashboardArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### Size
- **Type**: typing.Optional[int]


# DashboardValidationMessageTypeDef

### DataPath
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# DatapointTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### SampleCount
- **Type**: typing.Optional[float]

### Average
- **Type**: typing.Optional[float]

### Sum
- **Type**: typing.Optional[float]

### Minimum
- **Type**: typing.Optional[float]

### Maximum
- **Type**: typing.Optional[float]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### ExtendedStatistics
- **Type**: typing.Optional[typing.Dict[str, float]]


# DeleteAlarmsInputRequestTypeDef

### AlarmNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteAnomalyDetectorInputRequestTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Stat
- **Type**: typing.Optional[str]

### SingleMetricAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.SingleMetricAnomalyDetectorTypeDef]

### MetricMathAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricMathAnomalyDetectorTypeDef]


# DeleteDashboardsInputRequestTypeDef

### DashboardNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteInsightRulesInputRequestTypeDef

### RuleNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteInsightRulesOutputTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.PartialFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMetricStreamInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef

### AlarmTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### HistoryItemType
- **Type**: typing.Optional[typing.Literal['Action', 'ConfigurationUpdate', 'StateUpdate']]

### StartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ScanBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]


# DescribeAlarmHistoryInputDescribeAlarmHistoryPaginateTypeDef

### AlarmName
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### HistoryItemType
- **Type**: typing.Optional[typing.Literal['Action', 'ConfigurationUpdate', 'StateUpdate']]

### StartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ScanBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.PaginatorConfigTypeDef]


# DescribeAlarmHistoryInputRequestTypeDef

### AlarmName
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### HistoryItemType
- **Type**: typing.Optional[typing.Literal['Action', 'ConfigurationUpdate', 'StateUpdate']]

### StartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ScanBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]


# DescribeAlarmHistoryOutputTypeDef

### AlarmHistoryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.AlarmHistoryItemTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAlarmsForMetricInputRequestTypeDef

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Period
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# DescribeAlarmsForMetricOutputTypeDef

### MetricAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricAlarmTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAlarmsInputAlarmExistsWaitTypeDef

### AlarmNames
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmNamePrefix
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### ChildrenOfAlarmName
- **Type**: typing.Optional[str]

### ParentsOfAlarmName
- **Type**: typing.Optional[str]

### StateValue
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### ActionPrefix
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.WaiterConfigTypeDef]


# DescribeAlarmsInputCompositeAlarmExistsWaitTypeDef

### AlarmNames
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmNamePrefix
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### ChildrenOfAlarmName
- **Type**: typing.Optional[str]

### ParentsOfAlarmName
- **Type**: typing.Optional[str]

### StateValue
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### ActionPrefix
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.WaiterConfigTypeDef]


# DescribeAlarmsInputDescribeAlarmsPaginateTypeDef

### AlarmNames
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmNamePrefix
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### ChildrenOfAlarmName
- **Type**: typing.Optional[str]

### ParentsOfAlarmName
- **Type**: typing.Optional[str]

### StateValue
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### ActionPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.PaginatorConfigTypeDef]


# DescribeAlarmsInputRequestTypeDef

### AlarmNames
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmNamePrefix
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### ChildrenOfAlarmName
- **Type**: typing.Optional[str]

### ParentsOfAlarmName
- **Type**: typing.Optional[str]

### StateValue
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### ActionPrefix
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAlarmsOutputPaginatorTypeDef

### CompositeAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.CompositeAlarmTypeDef]
- **Required**: Yes

### MetricAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricAlarmPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAlarmsOutputTypeDef

### CompositeAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.CompositeAlarmTypeDef]
- **Required**: Yes

### MetricAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricAlarmTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnomalyDetectorsInputDescribeAnomalyDetectorsPaginateTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### AnomalyDetectorTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['METRIC_MATH', 'SINGLE_METRIC']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.PaginatorConfigTypeDef]


# DescribeAnomalyDetectorsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### AnomalyDetectorTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['METRIC_MATH', 'SINGLE_METRIC']]]


# DescribeAnomalyDetectorsOutputPaginatorTypeDef

### AnomalyDetectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.AnomalyDetectorPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnomalyDetectorsOutputTypeDef

### AnomalyDetectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.AnomalyDetectorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInsightRulesInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInsightRulesOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### InsightRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.InsightRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DimensionFilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# DimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DisableAlarmActionsInputRequestTypeDef

### AlarmNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisableInsightRulesInputRequestTypeDef

### RuleNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisableInsightRulesOutputTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.PartialFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableAlarmActionsInputRequestTypeDef

### AlarmNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EnableInsightRulesInputRequestTypeDef

### RuleNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EnableInsightRulesOutputTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.PartialFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDashboardInputRequestTypeDef

### DashboardName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDashboardOutputTypeDef

### DashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardBody
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightRuleReportInputRequestTypeDef

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### MaxContributorCount
- **Type**: typing.Optional[int]

### Metrics
- **Type**: typing.Optional[typing.Sequence[str]]

### OrderBy
- **Type**: typing.Optional[str]


# GetInsightRuleReportOutputTypeDef

### KeyLabels
- **Type**: typing.List[str]
- **Required**: Yes

### AggregationStatistic
- **Type**: <class 'str'>
- **Required**: Yes

### AggregateValue
- **Type**: <class 'float'>
- **Required**: Yes

### ApproximateUniqueCount
- **Type**: <class 'int'>
- **Required**: Yes

### Contributors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.InsightRuleContributorTypeDef]
- **Required**: Yes

### MetricDatapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.InsightRuleMetricDatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetricDataInputGetMetricDataPaginateTypeDef

### MetricDataQueries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataQueryPaginatorTypeDef]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ScanBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]

### LabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.LabelOptionsTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.PaginatorConfigTypeDef]


# GetMetricDataInputRequestTypeDef

### MetricDataQueries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataQueryTypeDef]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### ScanBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]

### MaxDatapoints
- **Type**: typing.Optional[int]

### LabelOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.LabelOptionsTypeDef]


# GetMetricDataOutputTypeDef

### MetricDataResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataResultTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MessageDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetricStatisticsInputMetricGetStatisticsTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Statistics
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]]

### ExtendedStatistics
- **Type**: typing.Optional[typing.Sequence[str]]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# GetMetricStatisticsInputRequestTypeDef

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Statistics
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]]

### ExtendedStatistics
- **Type**: typing.Optional[typing.Sequence[str]]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# GetMetricStatisticsOutputTypeDef

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### Datapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetricStreamInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetricStreamOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStreamFilterTypeDef]
- **Required**: Yes

### ExcludeFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStreamFilterTypeDef]
- **Required**: Yes

### FirehoseArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Literal['json', 'opentelemetry0.7', 'opentelemetry1.0']
- **Required**: Yes

### StatisticsConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStreamStatisticsConfigurationTypeDef]
- **Required**: Yes

### IncludeLinkedAccountsMetrics
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetricWidgetImageInputRequestTypeDef

### MetricWidget
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Optional[str]


# GetMetricWidgetImageOutputTypeDef

### MetricWidgetImage
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InsightRuleContributorDatapointTypeDef

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ApproximateValue
- **Type**: <class 'float'>
- **Required**: Yes


# InsightRuleContributorTypeDef

### Keys
- **Type**: typing.List[str]
- **Required**: Yes

### ApproximateAggregateValue
- **Type**: <class 'float'>
- **Required**: Yes

### Datapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.InsightRuleContributorDatapointTypeDef]
- **Required**: Yes


# InsightRuleMetricDatapointTypeDef

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UniqueContributors
- **Type**: typing.Optional[float]

### MaxContributorValue
- **Type**: typing.Optional[float]

### SampleCount
- **Type**: typing.Optional[float]

### Average
- **Type**: typing.Optional[float]

### Sum
- **Type**: typing.Optional[float]

### Minimum
- **Type**: typing.Optional[float]

### Maximum
- **Type**: typing.Optional[float]


# InsightRuleTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### Definition
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedRule
- **Type**: typing.Optional[bool]


# LabelOptionsTypeDef

### Timezone
- **Type**: typing.Optional[str]


# ListDashboardsInputListDashboardsPaginateTypeDef

### DashboardNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.PaginatorConfigTypeDef]


# ListDashboardsInputRequestTypeDef

### DashboardNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDashboardsOutputTypeDef

### DashboardEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DashboardEntryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListManagedInsightRulesInputRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListManagedInsightRulesOutputTypeDef

### ManagedRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.ManagedRuleDescriptionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetricStreamsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMetricStreamsOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStreamEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetricsInputListMetricsPaginateTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionFilterTypeDef]]

### RecentlyActive
- **Type**: typing.Optional[typing.Literal['PT3H']]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### OwningAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.PaginatorConfigTypeDef]


# ListMetricsInputRequestTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### RecentlyActive
- **Type**: typing.Optional[typing.Literal['PT3H']]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### OwningAccount
- **Type**: typing.Optional[str]


# ListMetricsOutputPaginatorTypeDef

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### OwningAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetricsOutputTypeDef

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### OwningAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagedRuleDescriptionTypeDef

### TemplateName
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### RuleState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.ManagedRuleStateTypeDef]


# ManagedRuleStateTypeDef

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes


# ManagedRuleTypeDef

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.TagTypeDef]]


# MessageDataTypeDef

### Code
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# MetricAlarmPaginatorTypeDef

### AlarmName
- **Type**: typing.Optional[str]

### AlarmArn
- **Type**: typing.Optional[str]

### AlarmDescription
- **Type**: typing.Optional[str]

### AlarmConfigurationUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ActionsEnabled
- **Type**: typing.Optional[bool]

### OKActions
- **Type**: typing.Optional[typing.List[str]]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### StateValue
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonData
- **Type**: typing.Optional[str]

### StateUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Period
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Threshold
- **Type**: typing.Optional[float]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'GreaterThanUpperThreshold', 'LessThanLowerOrGreaterThanUpperThreshold', 'LessThanLowerThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']]

### TreatMissingData
- **Type**: typing.Optional[str]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataQueryPaginatorTypeDef]]

### ThresholdMetricId
- **Type**: typing.Optional[str]

### EvaluationState
- **Type**: typing.Optional[typing.Literal['PARTIAL_DATA']]

### StateTransitionedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MetricAlarmTypeDef

### AlarmName
- **Type**: typing.Optional[str]

### AlarmArn
- **Type**: typing.Optional[str]

### AlarmDescription
- **Type**: typing.Optional[str]

### AlarmConfigurationUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ActionsEnabled
- **Type**: typing.Optional[bool]

### OKActions
- **Type**: typing.Optional[typing.List[str]]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### StateValue
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonData
- **Type**: typing.Optional[str]

### StateUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Period
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Threshold
- **Type**: typing.Optional[float]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'GreaterThanUpperThreshold', 'LessThanLowerOrGreaterThanUpperThreshold', 'LessThanLowerThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']]

### TreatMissingData
- **Type**: typing.Optional[str]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataQueryTypeDef]]

### ThresholdMetricId
- **Type**: typing.Optional[str]

### EvaluationState
- **Type**: typing.Optional[typing.Literal['PARTIAL_DATA']]

### StateTransitionedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MetricCharacteristicsTypeDef

### PeriodicSpikes
- **Type**: typing.Optional[bool]


# MetricDataQueryAlarmTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStatAlarmTypeDef]

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


# MetricDataQueryPaginatorTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStatPaginatorTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStatTypeDef]

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


# MetricDataResultTypeDef

### Id
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### Timestamps
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### Values
- **Type**: typing.Optional[typing.List[float]]

### StatusCode
- **Type**: typing.Optional[typing.Literal['Complete', 'Forbidden', 'InternalError', 'PartialData']]

### Messages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MessageDataTypeDef]]


# MetricDatumTypeDef

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Timestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Value
- **Type**: typing.Optional[float]

### StatisticValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.StatisticSetTypeDef]

### Values
- **Type**: typing.Optional[typing.Sequence[float]]

### Counts
- **Type**: typing.Optional[typing.Sequence[float]]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### StorageResolution
- **Type**: typing.Optional[int]


# MetricMathAnomalyDetectorPaginatorTypeDef

### MetricDataQueries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataQueryPaginatorTypeDef]]


# MetricMathAnomalyDetectorTypeDef

### MetricDataQueries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataQueryTypeDef]]


# MetricPaginatorTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]


# MetricStatAlarmTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.MetricAlarmTypeDef'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricStatPaginatorTypeDef

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.MetricPaginatorTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.MetricTypeDef'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricStreamEntryTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateDate
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### FirehoseArn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### OutputFormat
- **Type**: typing.Optional[typing.Literal['json', 'opentelemetry0.7', 'opentelemetry1.0']]


# MetricStreamFilterTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricNames
- **Type**: typing.Optional[typing.List[str]]


# MetricStreamStatisticsConfigurationTypeDef

### IncludeMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStreamStatisticsMetricTypeDef]
- **Required**: Yes

### AdditionalStatistics
- **Type**: typing.List[str]
- **Required**: Yes


# MetricStreamStatisticsMetricTypeDef

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes


# MetricTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartialFailureTypeDef

### FailureResource
- **Type**: typing.Optional[str]

### ExceptionType
- **Type**: typing.Optional[str]

### FailureCode
- **Type**: typing.Optional[str]

### FailureDescription
- **Type**: typing.Optional[str]


# PutAnomalyDetectorInputRequestTypeDef

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Stat
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.AnomalyDetectorConfigurationTypeDef]

### MetricCharacteristics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricCharacteristicsTypeDef]

### SingleMetricAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.SingleMetricAnomalyDetectorTypeDef]

### MetricMathAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricMathAnomalyDetectorTypeDef]


# PutCompositeAlarmInputRequestTypeDef

### AlarmName
- **Type**: <class 'str'>
- **Required**: Yes

### AlarmRule
- **Type**: <class 'str'>
- **Required**: Yes

### ActionsEnabled
- **Type**: typing.Optional[bool]

### AlarmActions
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmDescription
- **Type**: typing.Optional[str]

### InsufficientDataActions
- **Type**: typing.Optional[typing.Sequence[str]]

### OKActions
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.TagTypeDef]]

### ActionsSuppressor
- **Type**: typing.Optional[str]

### ActionsSuppressorWaitPeriod
- **Type**: typing.Optional[int]

### ActionsSuppressorExtensionPeriod
- **Type**: typing.Optional[int]


# PutDashboardInputRequestTypeDef

### DashboardName
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardBody
- **Type**: <class 'str'>
- **Required**: Yes


# PutDashboardOutputTypeDef

### DashboardValidationMessages
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DashboardValidationMessageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutInsightRuleInputRequestTypeDef

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### RuleState
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.TagTypeDef]]


# PutManagedInsightRulesInputRequestTypeDef

### ManagedRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.ManagedRuleTypeDef]
- **Required**: Yes


# PutManagedInsightRulesOutputTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.PartialFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutMetricAlarmInputMetricPutAlarmTypeDef

### AlarmName
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'GreaterThanUpperThreshold', 'LessThanLowerOrGreaterThanUpperThreshold', 'LessThanLowerThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### AlarmDescription
- **Type**: typing.Optional[str]

### ActionsEnabled
- **Type**: typing.Optional[bool]

### OKActions
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmActions
- **Type**: typing.Optional[typing.Sequence[str]]

### InsufficientDataActions
- **Type**: typing.Optional[typing.Sequence[str]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Period
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Threshold
- **Type**: typing.Optional[float]

### TreatMissingData
- **Type**: typing.Optional[str]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataQueryTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.TagTypeDef]]

### ThresholdMetricId
- **Type**: typing.Optional[str]


# PutMetricAlarmInputRequestTypeDef

### AlarmName
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'GreaterThanUpperThreshold', 'LessThanLowerOrGreaterThanUpperThreshold', 'LessThanLowerThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### AlarmDescription
- **Type**: typing.Optional[str]

### ActionsEnabled
- **Type**: typing.Optional[bool]

### OKActions
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmActions
- **Type**: typing.Optional[typing.Sequence[str]]

### InsufficientDataActions
- **Type**: typing.Optional[typing.Sequence[str]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Period
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Threshold
- **Type**: typing.Optional[float]

### TreatMissingData
- **Type**: typing.Optional[str]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDataQueryTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.TagTypeDef]]

### ThresholdMetricId
- **Type**: typing.Optional[str]


# PutMetricDataInputRequestTypeDef

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricData
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricDatumTypeDef]
- **Required**: Yes


# PutMetricStreamInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FirehoseArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Literal['json', 'opentelemetry0.7', 'opentelemetry1.0']
- **Required**: Yes

### IncludeFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStreamFilterTypeDef]]

### ExcludeFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStreamFilterTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.TagTypeDef]]

### StatisticsConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.MetricStreamStatisticsConfigurationTypeDef]]

### IncludeLinkedAccountsMetrics
- **Type**: typing.Optional[bool]


# PutMetricStreamOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RangeTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
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


# SetAlarmStateInputAlarmSetStateTypeDef

### StateValue
- **Type**: typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### StateReasonData
- **Type**: typing.Optional[str]


# SetAlarmStateInputRequestTypeDef

### AlarmName
- **Type**: <class 'str'>
- **Required**: Yes

### StateValue
- **Type**: typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### StateReasonData
- **Type**: typing.Optional[str]


# SingleMetricAnomalyDetectorPaginatorTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Stat
- **Type**: typing.Optional[str]


# SingleMetricAnomalyDetectorTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.DimensionTypeDef]]

### Stat
- **Type**: typing.Optional[str]


# StartMetricStreamsInputRequestTypeDef

### Names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StatisticSetTypeDef

### SampleCount
- **Type**: <class 'float'>
- **Required**: Yes

### Sum
- **Type**: <class 'float'>
- **Required**: Yes

### Minimum
- **Type**: <class 'float'>
- **Required**: Yes

### Maximum
- **Type**: <class 'float'>
- **Required**: Yes


# StopMetricStreamsInputRequestTypeDef

### Names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TagResourceInputRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudwatch_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


