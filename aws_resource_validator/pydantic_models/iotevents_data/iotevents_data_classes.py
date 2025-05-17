from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iotevents_data.iotevents_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcknowledgeActionConfiguration(BaseValidatorModel):
    note: Optional[str] = None


class AcknowledgeAlarmActionRequest(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None


class AlarmSummary(BaseValidatorModel):
    alarmModelName: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    keyValue: Optional[str] = None
    stateName: Optional[AlarmStateNameType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


class BatchAlarmActionErrorEntry(BaseValidatorModel):
    requestId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteDetectorErrorEntry(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None


class DeleteDetectorRequest(BaseValidatorModel):
    messageId: str
    detectorModelName: str
    keyValue: Optional[str] = None


class DisableAlarmActionRequest(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None


class EnableAlarmActionRequest(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None


class BatchPutMessageErrorEntry(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None


class ResetAlarmActionRequest(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None


class SnoozeAlarmActionRequest(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    snoozeDuration: int
    keyValue: Optional[str] = None
    note: Optional[str] = None


class BatchUpdateDetectorErrorEntry(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class DisableActionConfiguration(BaseValidatorModel):
    note: Optional[str] = None


class EnableActionConfiguration(BaseValidatorModel):
    note: Optional[str] = None


class ResetActionConfiguration(BaseValidatorModel):
    note: Optional[str] = None


class SnoozeActionConfiguration(BaseValidatorModel):
    snoozeDuration: Optional[int] = None
    note: Optional[str] = None


# This class is the input for the 'describe_alarm' function.
class DescribeAlarmRequest(BaseValidatorModel):
    alarmModelName: str
    keyValue: Optional[str] = None


# This class is the input for the 'describe_detector' function.
class DescribeDetectorRequest(BaseValidatorModel):
    detectorModelName: str
    keyValue: Optional[str] = None


class TimerDefinition(BaseValidatorModel):
    name: str
    seconds: int


class VariableDefinition(BaseValidatorModel):
    name: str
    value: str


class DetectorStateSummary(BaseValidatorModel):
    stateName: Optional[str] = None


class Timer(BaseValidatorModel):
    name: str
    timestamp: datetime


class Variable(BaseValidatorModel):
    name: str
    value: str


# This class is the input for the 'list_alarms' function.
class ListAlarmsRequest(BaseValidatorModel):
    alarmModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_detectors' function.
class ListDetectorsRequest(BaseValidatorModel):
    detectorModelName: str
    stateName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TimestampValue(BaseValidatorModel):
    timeInMillis: Optional[int] = None


class SimpleRuleEvaluation(BaseValidatorModel):
    inputPropertyValue: Optional[str] = None
    operator: Optional[ComparisonOperatorType] = None
    thresholdValue: Optional[str] = None


class StateChangeConfiguration(BaseValidatorModel):
    triggerType: Optional[Literal['SNOOZE_TIMEOUT']] = None


# This class is the input for the 'batch_acknowledge_alarm' function.
class BatchAcknowledgeAlarmRequest(BaseValidatorModel):
    acknowledgeActionRequests: List[AcknowledgeAlarmActionRequest]


# This class is the output for the 'batch_acknowledge_alarm' function.
class BatchAcknowledgeAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_disable_alarm' function.
class BatchDisableAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_enable_alarm' function.
class BatchEnableAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_reset_alarm' function.
class BatchResetAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_snooze_alarm' function.
class BatchSnoozeAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_alarms' function.
class ListAlarmsResponse(BaseValidatorModel):
    alarmSummaries: List[AlarmSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_delete_detector' function.
class BatchDeleteDetectorResponse(BaseValidatorModel):
    batchDeleteDetectorErrorEntries: List[BatchDeleteDetectorErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_delete_detector' function.
class BatchDeleteDetectorRequest(BaseValidatorModel):
    detectors: List[DeleteDetectorRequest]


# This class is the input for the 'batch_disable_alarm' function.
class BatchDisableAlarmRequest(BaseValidatorModel):
    disableActionRequests: List[DisableAlarmActionRequest]


# This class is the input for the 'batch_enable_alarm' function.
class BatchEnableAlarmRequest(BaseValidatorModel):
    enableActionRequests: List[EnableAlarmActionRequest]


# This class is the output for the 'batch_put_message' function.
class BatchPutMessageResponse(BaseValidatorModel):
    BatchPutMessageErrorEntries: List[BatchPutMessageErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_reset_alarm' function.
class BatchResetAlarmRequest(BaseValidatorModel):
    resetActionRequests: List[ResetAlarmActionRequest]


# This class is the input for the 'batch_snooze_alarm' function.
class BatchSnoozeAlarmRequest(BaseValidatorModel):
    snoozeActionRequests: List[SnoozeAlarmActionRequest]


# This class is the output for the 'batch_update_detector' function.
class BatchUpdateDetectorResponse(BaseValidatorModel):
    batchUpdateDetectorErrorEntries: List[BatchUpdateDetectorErrorEntry]
    ResponseMetadata: ResponseMetadata


class CustomerAction(BaseValidatorModel):
    actionName: Optional[CustomerActionNameType] = None
    snoozeActionConfiguration: Optional[SnoozeActionConfiguration] = None
    enableActionConfiguration: Optional[EnableActionConfiguration] = None
    disableActionConfiguration: Optional[DisableActionConfiguration] = None
    acknowledgeActionConfiguration: Optional[AcknowledgeActionConfiguration] = None
    resetActionConfiguration: Optional[ResetActionConfiguration] = None


class DetectorStateDefinition(BaseValidatorModel):
    stateName: str
    variables: List[VariableDefinition]
    timers: List[TimerDefinition]


class DetectorSummary(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    keyValue: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    state: Optional[DetectorStateSummary] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


class DetectorState(BaseValidatorModel):
    stateName: str
    variables: List[Variable]
    timers: List[Timer]


class Message(BaseValidatorModel):
    messageId: str
    inputName: str
    payload: Blob
    timestamp: Optional[TimestampValue] = None


class RuleEvaluation(BaseValidatorModel):
    simpleRuleEvaluation: Optional[SimpleRuleEvaluation] = None


class SystemEvent(BaseValidatorModel):
    eventType: Optional[Literal['STATE_CHANGE']] = None
    stateChangeConfiguration: Optional[StateChangeConfiguration] = None


class UpdateDetectorRequest(BaseValidatorModel):
    messageId: str
    detectorModelName: str
    state: DetectorStateDefinition
    keyValue: Optional[str] = None


# This class is the output for the 'list_detectors' function.
class ListDetectorsResponse(BaseValidatorModel):
    detectorSummaries: List[DetectorSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Detector(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    keyValue: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    state: Optional[DetectorState] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


# This class is the input for the 'batch_put_message' function.
class BatchPutMessageRequest(BaseValidatorModel):
    messages: List[Message]


class AlarmState(BaseValidatorModel):
    stateName: Optional[AlarmStateNameType] = None
    ruleEvaluation: Optional[RuleEvaluation] = None
    customerAction: Optional[CustomerAction] = None
    systemEvent: Optional[SystemEvent] = None


# This class is the input for the 'batch_update_detector' function.
class BatchUpdateDetectorRequest(BaseValidatorModel):
    detectors: List[UpdateDetectorRequest]


# This class is the output for the 'describe_detector' function.
class DescribeDetectorResponse(BaseValidatorModel):
    detector: Detector
    ResponseMetadata: ResponseMetadata


class Alarm(BaseValidatorModel):
    alarmModelName: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    keyValue: Optional[str] = None
    alarmState: Optional[AlarmState] = None
    severity: Optional[int] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


# This class is the output for the 'describe_alarm' function.
class DescribeAlarmResponse(BaseValidatorModel):
    alarm: Alarm
    ResponseMetadata: ResponseMetadata