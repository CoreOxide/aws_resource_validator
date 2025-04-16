from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.iotevents_data_constants import *

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


class DisableActionConfiguration(BaseValidatorModel):
    note: Optional[str] = None


class EnableActionConfiguration(BaseValidatorModel):
    note: Optional[str] = None


class ResetActionConfiguration(BaseValidatorModel):
    note: Optional[str] = None


class SnoozeActionConfiguration(BaseValidatorModel):
    snoozeDuration: Optional[int] = None
    note: Optional[str] = None


class DescribeAlarmRequest(BaseValidatorModel):
    alarmModelName: str
    keyValue: Optional[str] = None


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


class ListAlarmsRequest(BaseValidatorModel):
    alarmModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDetectorsRequest(BaseValidatorModel):
    detectorModelName: str
    stateName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TimestampValue(BaseValidatorModel):
    timeInMillis: Optional[int] = None


class StateChangeConfiguration(BaseValidatorModel):
    triggerType: Optional[Literal["SNOOZE_TIMEOUT"]] = None


class BatchAcknowledgeAlarmRequest(BaseValidatorModel):
    acknowledgeActionRequests: Sequence[AcknowledgeAlarmActionRequest]


class BatchAcknowledgeAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


class BatchDisableAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


class BatchEnableAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


class BatchResetAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


class BatchSnoozeAlarmResponse(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntry]
    ResponseMetadata: ResponseMetadata


class ListAlarmsResponse(BaseValidatorModel):
    alarmSummaries: List[AlarmSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchDeleteDetectorResponse(BaseValidatorModel):
    batchDeleteDetectorErrorEntries: List[BatchDeleteDetectorErrorEntry]
    ResponseMetadata: ResponseMetadata


class BatchDeleteDetectorRequest(BaseValidatorModel):
    detectors: Sequence[DeleteDetectorRequest]


class BatchDisableAlarmRequest(BaseValidatorModel):
    disableActionRequests: Sequence[DisableAlarmActionRequest]


class BatchEnableAlarmRequest(BaseValidatorModel):
    enableActionRequests: Sequence[EnableAlarmActionRequest]


class BatchPutMessageResponse(BaseValidatorModel):
    BatchPutMessageErrorEntries: List[BatchPutMessageErrorEntry]
    ResponseMetadata: ResponseMetadata


class BatchResetAlarmRequest(BaseValidatorModel):
    resetActionRequests: Sequence[ResetAlarmActionRequest]


class BatchSnoozeAlarmRequest(BaseValidatorModel):
    snoozeActionRequests: Sequence[SnoozeAlarmActionRequest]


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
    variables: Sequence[VariableDefinition]
    timers: Sequence[TimerDefinition]


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


class Blob(BaseValidatorModel):
    pass


class Message(BaseValidatorModel):
    messageId: str
    inputName: str
    payload: Blob
    timestamp: Optional[TimestampValue] = None


class SimpleRuleEvaluation(BaseValidatorModel):
    pass


class RuleEvaluation(BaseValidatorModel):
    simpleRuleEvaluation: Optional[SimpleRuleEvaluation] = None


class SystemEvent(BaseValidatorModel):
    eventType: Optional[Literal["STATE_CHANGE"]] = None
    stateChangeConfiguration: Optional[StateChangeConfiguration] = None


class UpdateDetectorRequest(BaseValidatorModel):
    messageId: str
    detectorModelName: str
    state: DetectorStateDefinition
    keyValue: Optional[str] = None


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


class BatchPutMessageRequest(BaseValidatorModel):
    messages: Sequence[Message]


class AlarmState(BaseValidatorModel):
    stateName: Optional[AlarmStateNameType] = None
    ruleEvaluation: Optional[RuleEvaluation] = None
    customerAction: Optional[CustomerAction] = None
    systemEvent: Optional[SystemEvent] = None


class BatchUpdateDetectorRequest(BaseValidatorModel):
    detectors: Sequence[UpdateDetectorRequest]


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


class DescribeAlarmResponse(BaseValidatorModel):
    alarm: Alarm
    ResponseMetadata: ResponseMetadata


