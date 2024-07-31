from datetime import datetime
from pydantic import BaseModel
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

class AcknowledgeActionConfigurationTypeDef(BaseModel):
    note: Optional[str] = None

class AcknowledgeAlarmActionRequestTypeDef(BaseModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None

class AlarmSummaryTypeDef(BaseModel):
    alarmModelName: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    keyValue: Optional[str] = None
    stateName: Optional[AlarmStateNameType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class BatchAlarmActionErrorEntryTypeDef(BaseModel):
    requestId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDeleteDetectorErrorEntryTypeDef(BaseModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class DeleteDetectorRequestTypeDef(BaseModel):
    messageId: str
    detectorModelName: str
    keyValue: Optional[str] = None

class DisableAlarmActionRequestTypeDef(BaseModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None

class EnableAlarmActionRequestTypeDef(BaseModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None

class BatchPutMessageErrorEntryTypeDef(BaseModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class ResetAlarmActionRequestTypeDef(BaseModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None

class SnoozeAlarmActionRequestTypeDef(BaseModel):
    requestId: str
    alarmModelName: str
    snoozeDuration: int
    keyValue: Optional[str] = None
    note: Optional[str] = None

class BatchUpdateDetectorErrorEntryTypeDef(BaseModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class DisableActionConfigurationTypeDef(BaseModel):
    note: Optional[str] = None

class EnableActionConfigurationTypeDef(BaseModel):
    note: Optional[str] = None

class ResetActionConfigurationTypeDef(BaseModel):
    note: Optional[str] = None

class SnoozeActionConfigurationTypeDef(BaseModel):
    snoozeDuration: Optional[int] = None
    note: Optional[str] = None

class DescribeAlarmRequestRequestTypeDef(BaseModel):
    alarmModelName: str
    keyValue: Optional[str] = None

class DescribeDetectorRequestRequestTypeDef(BaseModel):
    detectorModelName: str
    keyValue: Optional[str] = None

class TimerDefinitionTypeDef(BaseModel):
    name: str
    seconds: int

class VariableDefinitionTypeDef(BaseModel):
    name: str
    value: str

class DetectorStateSummaryTypeDef(BaseModel):
    stateName: Optional[str] = None

class TimerTypeDef(BaseModel):
    name: str
    timestamp: datetime

class VariableTypeDef(BaseModel):
    name: str
    value: str

class ListAlarmsRequestRequestTypeDef(BaseModel):
    alarmModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDetectorsRequestRequestTypeDef(BaseModel):
    detectorModelName: str
    stateName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TimestampValueTypeDef(BaseModel):
    timeInMillis: Optional[int] = None

class SimpleRuleEvaluationTypeDef(BaseModel):
    inputPropertyValue: Optional[str] = None
    operator: Optional[ComparisonOperatorType] = None
    thresholdValue: Optional[str] = None

class StateChangeConfigurationTypeDef(BaseModel):
    triggerType: Optional[Literal["SNOOZE_TIMEOUT"]] = None

class BatchAcknowledgeAlarmRequestRequestTypeDef(BaseModel):
    acknowledgeActionRequests: Sequence[AcknowledgeAlarmActionRequestTypeDef]

class BatchAcknowledgeAlarmResponseTypeDef(BaseModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisableAlarmResponseTypeDef(BaseModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableAlarmResponseTypeDef(BaseModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchResetAlarmResponseTypeDef(BaseModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchSnoozeAlarmResponseTypeDef(BaseModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlarmsResponseTypeDef(BaseModel):
    alarmSummaries: List[AlarmSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteDetectorResponseTypeDef(BaseModel):
    batchDeleteDetectorErrorEntries: List[BatchDeleteDetectorErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteDetectorRequestRequestTypeDef(BaseModel):
    detectors: Sequence[DeleteDetectorRequestTypeDef]

class BatchDisableAlarmRequestRequestTypeDef(BaseModel):
    disableActionRequests: Sequence[DisableAlarmActionRequestTypeDef]

class BatchEnableAlarmRequestRequestTypeDef(BaseModel):
    enableActionRequests: Sequence[EnableAlarmActionRequestTypeDef]

class BatchPutMessageResponseTypeDef(BaseModel):
    BatchPutMessageErrorEntries: List[BatchPutMessageErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchResetAlarmRequestRequestTypeDef(BaseModel):
    resetActionRequests: Sequence[ResetAlarmActionRequestTypeDef]

class BatchSnoozeAlarmRequestRequestTypeDef(BaseModel):
    snoozeActionRequests: Sequence[SnoozeAlarmActionRequestTypeDef]

class BatchUpdateDetectorResponseTypeDef(BaseModel):
    batchUpdateDetectorErrorEntries: List[BatchUpdateDetectorErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerActionTypeDef(BaseModel):
    actionName: Optional[CustomerActionNameType] = None
    snoozeActionConfiguration: Optional[SnoozeActionConfigurationTypeDef] = None
    enableActionConfiguration: Optional[EnableActionConfigurationTypeDef] = None
    disableActionConfiguration: Optional[DisableActionConfigurationTypeDef] = None
    acknowledgeActionConfiguration: Optional[AcknowledgeActionConfigurationTypeDef] = None
    resetActionConfiguration: Optional[ResetActionConfigurationTypeDef] = None

class DetectorStateDefinitionTypeDef(BaseModel):
    stateName: str
    variables: Sequence[VariableDefinitionTypeDef]
    timers: Sequence[TimerDefinitionTypeDef]

class DetectorSummaryTypeDef(BaseModel):
    detectorModelName: Optional[str] = None
    keyValue: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    state: Optional[DetectorStateSummaryTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class DetectorStateTypeDef(BaseModel):
    stateName: str
    variables: List[VariableTypeDef]
    timers: List[TimerTypeDef]

class MessageTypeDef(BaseModel):
    messageId: str
    inputName: str
    payload: BlobTypeDef
    timestamp: Optional[TimestampValueTypeDef] = None

class RuleEvaluationTypeDef(BaseModel):
    simpleRuleEvaluation: Optional[SimpleRuleEvaluationTypeDef] = None

class SystemEventTypeDef(BaseModel):
    eventType: Optional[Literal["STATE_CHANGE"]] = None
    stateChangeConfiguration: Optional[StateChangeConfigurationTypeDef] = None

class UpdateDetectorRequestTypeDef(BaseModel):
    messageId: str
    detectorModelName: str
    state: DetectorStateDefinitionTypeDef
    keyValue: Optional[str] = None

class ListDetectorsResponseTypeDef(BaseModel):
    detectorSummaries: List[DetectorSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectorTypeDef(BaseModel):
    detectorModelName: Optional[str] = None
    keyValue: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    state: Optional[DetectorStateTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class BatchPutMessageRequestRequestTypeDef(BaseModel):
    messages: Sequence[MessageTypeDef]

class AlarmStateTypeDef(BaseModel):
    stateName: Optional[AlarmStateNameType] = None
    ruleEvaluation: Optional[RuleEvaluationTypeDef] = None
    customerAction: Optional[CustomerActionTypeDef] = None
    systemEvent: Optional[SystemEventTypeDef] = None

class BatchUpdateDetectorRequestRequestTypeDef(BaseModel):
    detectors: Sequence[UpdateDetectorRequestTypeDef]

class DescribeDetectorResponseTypeDef(BaseModel):
    detector: DetectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AlarmTypeDef(BaseModel):
    alarmModelName: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    keyValue: Optional[str] = None
    alarmState: Optional[AlarmStateTypeDef] = None
    severity: Optional[int] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class DescribeAlarmResponseTypeDef(BaseModel):
    alarm: AlarmTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

