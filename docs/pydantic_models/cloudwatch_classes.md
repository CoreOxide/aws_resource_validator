# Cloudwatch Classes

# AlarmHistoryItem

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


# AnomalyDetector

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Stat
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.AnomalyDetectorConfigurationOutput]

### StateValue
- **Type**: typing.Optional[typing.Literal['PENDING_TRAINING', 'TRAINED', 'TRAINED_INSUFFICIENT_DATA']]

### MetricCharacteristics
- **Type**: <class 'NoneType'>

### SingleMetricAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.SingleMetricAnomalyDetectorOutput]

### MetricMathAnomalyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricMathAnomalyDetectorOutput]


# AnomalyDetectorConfiguration

### ExcludedTimeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Range]]

### MetricTimezone
- **Type**: typing.Optional[str]


# AnomalyDetectorConfigurationOutput

### ExcludedTimeRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.RangeOutput]]

### MetricTimezone
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudwatchEvent

### version
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### detail_type
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CloudwatchEventDetail'>
- **Required**: Yes


# CloudwatchEventDetail

### alarmName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CloudwatchEventState'>
- **Required**: Yes

### operation
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CloudwatchEventDetailConfiguration]

### previousConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CloudwatchEventDetailConfiguration]

### previousState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CloudwatchEventState]


# CloudwatchEventDetailConfiguration

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CloudwatchEventMetric]]

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


# CloudwatchEventMetric

### id
- **Type**: <class 'str'>
- **Required**: Yes

### returnData
- **Type**: <class 'bool'>
- **Required**: Yes

### metricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CloudwatchEventMetricStats]

### expression
- **Type**: typing.Optional[str]

### label
- **Type**: typing.Optional[str]

### period
- **Type**: typing.Optional[int]


# CloudwatchEventMetricStats

### period
- **Type**: <class 'str'>
- **Required**: Yes

### stat
- **Type**: <class 'str'>
- **Required**: Yes

### metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CloudwatchEventMetricStatsMetric]


# CloudwatchEventMetricStatsMetric

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### dimensions
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# CloudwatchEventState

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


# CompositeAlarm

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


# DashboardEntry

### DashboardName
- **Type**: typing.Optional[str]

### DashboardArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### Size
- **Type**: typing.Optional[int]


# DashboardValidationMessage

### DataPath
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# Datapoint

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


# DeleteAlarmsInput

### AlarmNames
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteAnomalyDetectorInput

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Stat
- **Type**: typing.Optional[str]

### SingleMetricAnomalyDetector
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.SingleMetricAnomalyDetector, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.SingleMetricAnomalyDetectorOutput, NoneType]

### MetricMathAnomalyDetector
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricMathAnomalyDetector, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricMathAnomalyDetectorOutput, NoneType]


# DeleteDashboardsInput

### DashboardNames
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteInsightRulesInput

### RuleNames
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteInsightRulesOutput

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PartialFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMetricStreamInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlarmHistoryInput

### AlarmName
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

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


# DescribeAlarmHistoryInputAlarmDescribeHistory

### AlarmTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

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


# DescribeAlarmHistoryInputPaginate

### AlarmName
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### HistoryItemType
- **Type**: typing.Optional[typing.Literal['Action', 'ConfigurationUpdate', 'StateUpdate']]

### StartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ScanBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PaginatorConfig]


# DescribeAlarmHistoryOutput

### AlarmHistoryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.AlarmHistoryItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAlarmsForMetricInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Period
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# DescribeAlarmsForMetricOutput

### MetricAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricAlarm]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAlarmsInput

### AlarmNames
- **Type**: typing.Optional[typing.List[str]]

### AlarmNamePrefix
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

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


# DescribeAlarmsInputPaginate

### AlarmNames
- **Type**: typing.Optional[typing.List[str]]

### AlarmNamePrefix
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

### ChildrenOfAlarmName
- **Type**: typing.Optional[str]

### ParentsOfAlarmName
- **Type**: typing.Optional[str]

### StateValue
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### ActionPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PaginatorConfig]


# DescribeAlarmsInputWait

### AlarmNames
- **Type**: typing.Optional[typing.List[str]]

### AlarmNamePrefix
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

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
- **Type**: <class 'NoneType'>


# DescribeAlarmsInputWaitExtra

### AlarmNames
- **Type**: typing.Optional[typing.List[str]]

### AlarmNamePrefix
- **Type**: typing.Optional[str]

### AlarmTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CompositeAlarm', 'MetricAlarm']]]

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
- **Type**: <class 'NoneType'>


# DescribeAlarmsOutput

### CompositeAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.CompositeAlarm]
- **Required**: Yes

### MetricAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricAlarm]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAnomalyDetectorsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### AnomalyDetectorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['METRIC_MATH', 'SINGLE_METRIC']]]


# DescribeAnomalyDetectorsInputPaginate

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### AnomalyDetectorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['METRIC_MATH', 'SINGLE_METRIC']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PaginatorConfig]


# DescribeAnomalyDetectorsOutput

### AnomalyDetectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.AnomalyDetector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInsightRulesInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInsightRulesOutput

### InsightRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.InsightRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Dimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DimensionFilter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# DisableAlarmActionsInput

### AlarmNames
- **Type**: typing.List[str]
- **Required**: Yes


# DisableInsightRulesInput

### RuleNames
- **Type**: typing.List[str]
- **Required**: Yes


# DisableInsightRulesOutput

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PartialFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# EnableAlarmActionsInput

### AlarmNames
- **Type**: typing.List[str]
- **Required**: Yes


# EnableInsightRulesInput

### RuleNames
- **Type**: typing.List[str]
- **Required**: Yes


# EnableInsightRulesOutput

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PartialFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# Entity

### KeyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# EntityMetricData

### Entity
- **Type**: <class 'NoneType'>

### MetricData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDatum]]


# GetDashboardInput

### DashboardName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDashboardOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# GetInsightRuleReportInput

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
- **Type**: typing.Optional[typing.List[str]]

### OrderBy
- **Type**: typing.Optional[str]


# GetInsightRuleReportOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.InsightRuleContributor]
- **Required**: Yes

### MetricDatapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.InsightRuleMetricDatapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetricDataInput

### MetricDataQueries
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQuery, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQueryOutput]]
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
- **Type**: <class 'NoneType'>


# GetMetricDataInputPaginate

### MetricDataQueries
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQuery, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQueryOutput]]
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
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PaginatorConfig]


# GetMetricDataOutput

### MetricDataResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataResult]
- **Required**: Yes

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MessageData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMetricStatisticsInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Statistics
- **Type**: typing.Optional[typing.List[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]]

### ExtendedStatistics
- **Type**: typing.Optional[typing.List[str]]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# GetMetricStatisticsInputMetricGetStatistics

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Statistics
- **Type**: typing.Optional[typing.List[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]]

### ExtendedStatistics
- **Type**: typing.Optional[typing.List[str]]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# GetMetricStatisticsOutput

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### Datapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Datapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetricStreamInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetricStreamOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamFilterOutput]
- **Required**: Yes

### ExcludeFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamFilterOutput]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamStatisticsConfigurationOutput]
- **Required**: Yes

### IncludeLinkedAccountsMetrics
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetricWidgetImageInput

### MetricWidget
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Optional[str]


# GetMetricWidgetImageOutput

### MetricWidgetImage
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# InsightRule

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


# InsightRuleContributor

### Keys
- **Type**: typing.List[str]
- **Required**: Yes

### ApproximateAggregateValue
- **Type**: <class 'float'>
- **Required**: Yes

### Datapoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.InsightRuleContributorDatapoint]
- **Required**: Yes


# InsightRuleContributorDatapoint

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ApproximateValue
- **Type**: <class 'float'>
- **Required**: Yes


# InsightRuleMetricDatapoint

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


# LabelOptions

### Timezone
- **Type**: typing.Optional[str]


# ListDashboardsInput

### DashboardNamePrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListDashboardsInputPaginate

### DashboardNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PaginatorConfig]


# ListDashboardsOutput

### DashboardEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.DashboardEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedInsightRulesInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListManagedInsightRulesOutput

### ManagedRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ManagedRuleDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMetricStreamsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMetricStreamsOutput

### Entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMetricsInput

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.DimensionFilter]]

### NextToken
- **Type**: typing.Optional[str]

### RecentlyActive
- **Type**: typing.Optional[typing.Literal['PT3H']]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### OwningAccount
- **Type**: typing.Optional[str]


# ListMetricsInputPaginate

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.DimensionFilter]]

### RecentlyActive
- **Type**: typing.Optional[typing.Literal['PT3H']]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### OwningAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PaginatorConfig]


# ListMetricsOutput

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricOutput]
- **Required**: Yes

### OwningAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# ManagedRule

### TemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Tag]]


# ManagedRuleDescription

### TemplateName
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### RuleState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ManagedRuleState]


# ManagedRuleState

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes


# MessageData

### Code
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# Metric

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]


# MetricAlarm

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQueryOutput]]

### ThresholdMetricId
- **Type**: typing.Optional[str]

### EvaluationState
- **Type**: typing.Optional[typing.Literal['PARTIAL_DATA']]

### StateTransitionedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MetricCharacteristics

### PeriodicSpikes
- **Type**: typing.Optional[bool]


# MetricDataQuery

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStat, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStatOutput, NoneType]

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


# MetricDataQueryAlarm

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MetricStat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStatAlarm]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStatOutput]

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


# MetricDataResult

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MessageData]]


# MetricDatum

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Timestamp
- **Type**: <class 'NoneType'>

### Value
- **Type**: typing.Optional[float]

### StatisticValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.StatisticSet]

### Values
- **Type**: typing.Optional[typing.List[float]]

### Counts
- **Type**: typing.Optional[typing.List[float]]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### StorageResolution
- **Type**: typing.Optional[int]


# MetricMathAnomalyDetector

### MetricDataQueries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQuery]]


# MetricMathAnomalyDetectorOutput

### MetricDataQueries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQueryOutput]]


# MetricOutput

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]


# MetricStat

### Metric
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Metric, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricOutput]
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricStatAlarm

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricAlarm'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricOutput'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Stat
- **Type**: <class 'str'>
- **Required**: Yes

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricStreamEntry

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


# MetricStreamFilter

### Namespace
- **Type**: typing.Optional[str]

### MetricNames
- **Type**: typing.Optional[typing.List[str]]


# MetricStreamFilterOutput

### Namespace
- **Type**: typing.Optional[str]

### MetricNames
- **Type**: typing.Optional[typing.List[str]]


# MetricStreamStatisticsConfiguration

### IncludeMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamStatisticsMetric]
- **Required**: Yes

### AdditionalStatistics
- **Type**: typing.List[str]
- **Required**: Yes


# MetricStreamStatisticsConfigurationOutput

### IncludeMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamStatisticsMetric]
- **Required**: Yes

### AdditionalStatistics
- **Type**: typing.List[str]
- **Required**: Yes


# MetricStreamStatisticsMetric

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartialFailure

### FailureResource
- **Type**: typing.Optional[str]

### ExceptionType
- **Type**: typing.Optional[str]

### FailureCode
- **Type**: typing.Optional[str]

### FailureDescription
- **Type**: typing.Optional[str]


# PutAnomalyDetectorInput

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Stat
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.AnomalyDetectorConfiguration, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.AnomalyDetectorConfigurationOutput, NoneType]

### MetricCharacteristics
- **Type**: <class 'NoneType'>

### SingleMetricAnomalyDetector
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.SingleMetricAnomalyDetector, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.SingleMetricAnomalyDetectorOutput, NoneType]

### MetricMathAnomalyDetector
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricMathAnomalyDetector, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricMathAnomalyDetectorOutput, NoneType]


# PutCompositeAlarmInput

### AlarmName
- **Type**: <class 'str'>
- **Required**: Yes

### AlarmRule
- **Type**: <class 'str'>
- **Required**: Yes

### ActionsEnabled
- **Type**: typing.Optional[bool]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### AlarmDescription
- **Type**: typing.Optional[str]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### OKActions
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Tag]]

### ActionsSuppressor
- **Type**: typing.Optional[str]

### ActionsSuppressorWaitPeriod
- **Type**: typing.Optional[int]

### ActionsSuppressorExtensionPeriod
- **Type**: typing.Optional[int]


# PutDashboardInput

### DashboardName
- **Type**: <class 'str'>
- **Required**: Yes

### DashboardBody
- **Type**: <class 'str'>
- **Required**: Yes


# PutDashboardOutput

### DashboardValidationMessages
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.DashboardValidationMessage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# PutInsightRuleInput

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### RuleState
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Tag]]


# PutManagedInsightRulesInput

### ManagedRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ManagedRule]
- **Required**: Yes


# PutManagedInsightRulesOutput

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.PartialFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# PutMetricAlarmInput

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
- **Type**: typing.Optional[typing.List[str]]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQuery, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQueryOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Tag]]

### ThresholdMetricId
- **Type**: typing.Optional[str]


# PutMetricAlarmInputMetricPutAlarm

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
- **Type**: typing.Optional[typing.List[str]]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQuery, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDataQueryOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Tag]]

### ThresholdMetricId
- **Type**: typing.Optional[str]


# PutMetricDataInput

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### MetricData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricDatum]]

### EntityMetricData
- **Type**: typing.Optional[typing.List[NoneType]]

### StrictEntityValidation
- **Type**: typing.Optional[bool]


# PutMetricDataInputMetricPutData

### EntityMetricData
- **Type**: typing.Optional[typing.List[NoneType]]

### StrictEntityValidation
- **Type**: typing.Optional[bool]


# PutMetricStreamInput

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamFilter, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamFilterOutput]]]

### ExcludeFilters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamFilter, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamFilterOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Tag]]

### StatisticsConfigurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamStatisticsConfiguration, aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.MetricStreamStatisticsConfigurationOutput]]]

### IncludeLinkedAccountsMetrics
- **Type**: typing.Optional[bool]


# PutMetricStreamOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.ResponseMetadata'>
- **Required**: Yes


# Range

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# RangeOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
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


# SetAlarmStateInput

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


# SetAlarmStateInputAlarmSetState

### StateValue
- **Type**: typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### StateReasonData
- **Type**: typing.Optional[str]


# SingleMetricAnomalyDetector

### AccountId
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Stat
- **Type**: typing.Optional[str]


# SingleMetricAnomalyDetectorOutput

### AccountId
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Dimension]]

### Stat
- **Type**: typing.Optional[str]


# StartMetricStreamsInput

### Names
- **Type**: typing.List[str]
- **Required**: Yes


# StatisticSet

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


# StopMetricStreamsInput

### Names
- **Type**: typing.List[str]
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudwatch.cloudwatch_classes.Tag]
- **Required**: Yes


# UntagResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


