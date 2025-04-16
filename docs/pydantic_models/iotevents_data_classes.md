# Iotevents Data Classes

# AcknowledgeActionConfiguration

### note
- **Type**: typing.Optional[str]


# AcknowledgeAlarmActionRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]

### note
- **Type**: typing.Optional[str]


# Alarm

### alarmModelName
- **Type**: typing.Optional[str]

### alarmModelVersion
- **Type**: typing.Optional[str]

### keyValue
- **Type**: typing.Optional[str]

### alarmState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.AlarmState]

### severity
- **Type**: typing.Optional[int]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# AlarmState

### stateName
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGED', 'ACTIVE', 'DISABLED', 'LATCHED', 'NORMAL', 'SNOOZE_DISABLED']]

### ruleEvaluation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.RuleEvaluation]

### customerAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.CustomerAction]

### systemEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.SystemEvent]


# AlarmSummary

### alarmModelName
- **Type**: typing.Optional[str]

### alarmModelVersion
- **Type**: typing.Optional[str]

### keyValue
- **Type**: typing.Optional[str]

### stateName
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGED', 'ACTIVE', 'DISABLED', 'LATCHED', 'NORMAL', 'SNOOZE_DISABLED']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAcknowledgeAlarmRequest

### acknowledgeActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.AcknowledgeAlarmActionRequest]
- **Required**: Yes


# BatchAcknowledgeAlarmResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# BatchAlarmActionErrorEntry

### requestId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalFailureException', 'InvalidRequestException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDeleteDetectorErrorEntry

### messageId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalFailureException', 'InvalidRequestException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDeleteDetectorRequest

### detectors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.DeleteDetectorRequest]
- **Required**: Yes


# BatchDeleteDetectorResponse

### batchDeleteDetectorErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchDeleteDetectorErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisableAlarmRequest

### disableActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.DisableAlarmActionRequest]
- **Required**: Yes


# BatchDisableAlarmResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# BatchEnableAlarmRequest

### enableActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.EnableAlarmActionRequest]
- **Required**: Yes


# BatchEnableAlarmResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutMessageErrorEntry

### messageId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalFailureException', 'InvalidRequestException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchPutMessageRequest

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.Message]
- **Required**: Yes


# BatchPutMessageResponse

### BatchPutMessageErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchPutMessageErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# BatchResetAlarmRequest

### resetActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.ResetAlarmActionRequest]
- **Required**: Yes


# BatchResetAlarmResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# BatchSnoozeAlarmRequest

### snoozeActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.SnoozeAlarmActionRequest]
- **Required**: Yes


# BatchSnoozeAlarmResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateDetectorErrorEntry

### messageId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalFailureException', 'InvalidRequestException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchUpdateDetectorRequest

### detectors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.UpdateDetectorRequest]
- **Required**: Yes


# BatchUpdateDetectorResponse

### batchUpdateDetectorErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchUpdateDetectorErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomerAction

### actionName
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGE', 'DISABLE', 'ENABLE', 'RESET', 'SNOOZE']]

### snoozeActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.SnoozeActionConfiguration]

### enableActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.EnableActionConfiguration]

### disableActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.DisableActionConfiguration]

### acknowledgeActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.AcknowledgeActionConfiguration]

### resetActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.ResetActionConfiguration]


# DeleteDetectorRequest

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# DescribeAlarmRequest

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# DescribeAlarmResponse

### alarm
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.Alarm'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDetectorRequest

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# DescribeDetectorResponse

### detector
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.Detector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes


# Detector

### detectorModelName
- **Type**: typing.Optional[str]

### keyValue
- **Type**: typing.Optional[str]

### detectorModelVersion
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorState]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# DetectorState

### stateName
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.Variable]
- **Required**: Yes

### timers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.Timer]
- **Required**: Yes


# DetectorStateDefinition

### stateName
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.VariableDefinition]
- **Required**: Yes

### timers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.TimerDefinition]
- **Required**: Yes


# DetectorStateSummary

### stateName
- **Type**: typing.Optional[str]


# DetectorSummary

### detectorModelName
- **Type**: typing.Optional[str]

### keyValue
- **Type**: typing.Optional[str]

### detectorModelVersion
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorStateSummary]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# DisableActionConfiguration

### note
- **Type**: typing.Optional[str]


# DisableAlarmActionRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]

### note
- **Type**: typing.Optional[str]


# EnableActionConfiguration

### note
- **Type**: typing.Optional[str]


# EnableAlarmActionRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]

### note
- **Type**: typing.Optional[str]


# ListAlarmsRequest

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAlarmsResponse

### alarmSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.AlarmSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectorsRequest

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### stateName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDetectorsResponse

### detectorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Message

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.Blob'>
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.TimestampValue]


# ResetActionConfiguration

### note
- **Type**: typing.Optional[str]


# ResetAlarmActionRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]

### note
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


# RuleEvaluation

### simpleRuleEvaluation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.SimpleRuleEvaluation]


# SimpleRuleEvaluation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnoozeActionConfiguration

### snoozeDuration
- **Type**: typing.Optional[int]

### note
- **Type**: typing.Optional[str]


# SnoozeAlarmActionRequest

### requestId
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### snoozeDuration
- **Type**: <class 'int'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]

### note
- **Type**: typing.Optional[str]


# StateChangeConfiguration

### triggerType
- **Type**: typing.Optional[typing.Literal['SNOOZE_TIMEOUT']]


# SystemEvent

### eventType
- **Type**: typing.Optional[typing.Literal['STATE_CHANGE']]

### stateChangeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.StateChangeConfiguration]


# Timer

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TimerDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### seconds
- **Type**: <class 'int'>
- **Required**: Yes


# TimestampValue

### timeInMillis
- **Type**: typing.Optional[int]


# UpdateDetectorRequest

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorStateDefinition'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# Variable

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# VariableDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


