# Pydantic Models in iotevents_data_classes

# AcknowledgeActionConfigurationTypeDef

### note
- **Type**: typing.Optional[str]


# AcknowledgeAlarmActionRequestTypeDef

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


# AlarmStateTypeDef

### stateName
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGED', 'ACTIVE', 'DISABLED', 'LATCHED', 'NORMAL', 'SNOOZE_DISABLED']]

### ruleEvaluation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.RuleEvaluationTypeDef]

### customerAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.CustomerActionTypeDef]

### systemEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.SystemEventTypeDef]


# AlarmSummaryTypeDef

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


# AlarmTypeDef

### alarmModelName
- **Type**: typing.Optional[str]

### alarmModelVersion
- **Type**: typing.Optional[str]

### keyValue
- **Type**: typing.Optional[str]

### alarmState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.AlarmStateTypeDef]

### severity
- **Type**: typing.Optional[int]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAcknowledgeAlarmRequestRequestTypeDef

### acknowledgeActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.AcknowledgeAlarmActionRequestTypeDef]
- **Required**: Yes


# BatchAcknowledgeAlarmResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchAlarmActionErrorEntryTypeDef

### requestId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalFailureException', 'InvalidRequestException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDeleteDetectorErrorEntryTypeDef

### messageId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalFailureException', 'InvalidRequestException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDeleteDetectorRequestRequestTypeDef

### detectors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.DeleteDetectorRequestTypeDef]
- **Required**: Yes


# BatchDeleteDetectorResponseTypeDef

### batchDeleteDetectorErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchDeleteDetectorErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisableAlarmRequestRequestTypeDef

### disableActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.DisableAlarmActionRequestTypeDef]
- **Required**: Yes


# BatchDisableAlarmResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchEnableAlarmRequestRequestTypeDef

### enableActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.EnableAlarmActionRequestTypeDef]
- **Required**: Yes


# BatchEnableAlarmResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutMessageErrorEntryTypeDef

### messageId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalFailureException', 'InvalidRequestException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchPutMessageRequestRequestTypeDef

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.MessageTypeDef]
- **Required**: Yes


# BatchPutMessageResponseTypeDef

### BatchPutMessageErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchPutMessageErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchResetAlarmRequestRequestTypeDef

### resetActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.ResetAlarmActionRequestTypeDef]
- **Required**: Yes


# BatchResetAlarmResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchSnoozeAlarmRequestRequestTypeDef

### snoozeActionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.SnoozeAlarmActionRequestTypeDef]
- **Required**: Yes


# BatchSnoozeAlarmResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchAlarmActionErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateDetectorErrorEntryTypeDef

### messageId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['InternalFailureException', 'InvalidRequestException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchUpdateDetectorRequestRequestTypeDef

### detectors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.UpdateDetectorRequestTypeDef]
- **Required**: Yes


# BatchUpdateDetectorResponseTypeDef

### batchUpdateDetectorErrorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.BatchUpdateDetectorErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerActionTypeDef

### actionName
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGE', 'DISABLE', 'ENABLE', 'RESET', 'SNOOZE']]

### snoozeActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.SnoozeActionConfigurationTypeDef]

### enableActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.EnableActionConfigurationTypeDef]

### disableActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.DisableActionConfigurationTypeDef]

### acknowledgeActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.AcknowledgeActionConfigurationTypeDef]

### resetActionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.ResetActionConfigurationTypeDef]


# DeleteDetectorRequestTypeDef

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# DescribeAlarmRequestRequestTypeDef

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# DescribeAlarmResponseTypeDef

### alarm
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.AlarmTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDetectorRequestRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# DescribeDetectorResponseTypeDef

### detector
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectorStateDefinitionTypeDef

### stateName
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.VariableDefinitionTypeDef]
- **Required**: Yes

### timers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_data_classes.TimerDefinitionTypeDef]
- **Required**: Yes


# DetectorStateSummaryTypeDef

### stateName
- **Type**: typing.Optional[str]


# DetectorStateTypeDef

### stateName
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.VariableTypeDef]
- **Required**: Yes

### timers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.TimerTypeDef]
- **Required**: Yes


# DetectorSummaryTypeDef

### detectorModelName
- **Type**: typing.Optional[str]

### keyValue
- **Type**: typing.Optional[str]

### detectorModelVersion
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorStateSummaryTypeDef]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# DetectorTypeDef

### detectorModelName
- **Type**: typing.Optional[str]

### keyValue
- **Type**: typing.Optional[str]

### detectorModelVersion
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorStateTypeDef]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# DisableActionConfigurationTypeDef

### note
- **Type**: typing.Optional[str]


# DisableAlarmActionRequestTypeDef

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


# EnableActionConfigurationTypeDef

### note
- **Type**: typing.Optional[str]


# EnableAlarmActionRequestTypeDef

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


# ListAlarmsRequestRequestTypeDef

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAlarmsResponseTypeDef

### alarmSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.AlarmSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDetectorsRequestRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### stateName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDetectorsResponseTypeDef

### detectorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MessageTypeDef

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.TimestampValueTypeDef]


# ResetActionConfigurationTypeDef

### note
- **Type**: typing.Optional[str]


# ResetAlarmActionRequestTypeDef

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


# RuleEvaluationTypeDef

### simpleRuleEvaluation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.SimpleRuleEvaluationTypeDef]


# SimpleRuleEvaluationTypeDef

### inputPropertyValue
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[typing.Literal['EQUAL', 'GREATER', 'GREATER_OR_EQUAL', 'LESS', 'LESS_OR_EQUAL', 'NOT_EQUAL']]

### thresholdValue
- **Type**: typing.Optional[str]


# SnoozeActionConfigurationTypeDef

### snoozeDuration
- **Type**: typing.Optional[int]

### note
- **Type**: typing.Optional[str]


# SnoozeAlarmActionRequestTypeDef

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


# StateChangeConfigurationTypeDef

### triggerType
- **Type**: typing.Optional[typing.Literal['SNOOZE_TIMEOUT']]


# SystemEventTypeDef

### eventType
- **Type**: typing.Optional[typing.Literal['STATE_CHANGE']]

### stateChangeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_data_classes.StateChangeConfigurationTypeDef]


# TimerDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### seconds
- **Type**: <class 'int'>
- **Required**: Yes


# TimerTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TimestampValueTypeDef

### timeInMillis
- **Type**: typing.Optional[int]


# UpdateDetectorRequestTypeDef

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_data_classes.DetectorStateDefinitionTypeDef'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# VariableDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# VariableTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


