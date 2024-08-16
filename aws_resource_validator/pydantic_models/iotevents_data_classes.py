from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AcknowledgeActionConfigurationTypeDef(BaseValidatorModel):
    note: Optional[str] = None

class AcknowledgeAlarmActionRequestTypeDef(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None

class AlarmSummaryTypeDef(BaseValidatorModel):
    alarmModelName: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    keyValue: Optional[str] = None
    stateName: Optional[AlarmStateNameType] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class BatchAlarmActionErrorEntryTypeDef(BaseValidatorModel):
    requestId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDeleteDetectorErrorEntryTypeDef(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class DeleteDetectorRequestTypeDef(BaseValidatorModel):
    messageId: str
    detectorModelName: str
    keyValue: Optional[str] = None

class DisableAlarmActionRequestTypeDef(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None

class EnableAlarmActionRequestTypeDef(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None

class BatchPutMessageErrorEntryTypeDef(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class ResetAlarmActionRequestTypeDef(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    keyValue: Optional[str] = None
    note: Optional[str] = None

class SnoozeAlarmActionRequestTypeDef(BaseValidatorModel):
    requestId: str
    alarmModelName: str
    snoozeDuration: int
    keyValue: Optional[str] = None
    note: Optional[str] = None

class BatchUpdateDetectorErrorEntryTypeDef(BaseValidatorModel):
    messageId: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None

class DisableActionConfigurationTypeDef(BaseValidatorModel):
    note: Optional[str] = None

class EnableActionConfigurationTypeDef(BaseValidatorModel):
    note: Optional[str] = None

class ResetActionConfigurationTypeDef(BaseValidatorModel):
    note: Optional[str] = None

class SnoozeActionConfigurationTypeDef(BaseValidatorModel):
    snoozeDuration: Optional[int] = None
    note: Optional[str] = None

class DescribeAlarmRequestRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    keyValue: Optional[str] = None

class DescribeDetectorRequestRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    keyValue: Optional[str] = None

class TimerDefinitionTypeDef(BaseValidatorModel):
    name: str
    seconds: int

class VariableDefinitionTypeDef(BaseValidatorModel):
    name: str
    value: str

class DetectorStateSummaryTypeDef(BaseValidatorModel):
    stateName: Optional[str] = None

class TimerTypeDef(BaseValidatorModel):
    name: str
    timestamp: datetime

class VariableTypeDef(BaseValidatorModel):
    name: str
    value: str

class ListAlarmsRequestRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDetectorsRequestRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    stateName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TimestampValueTypeDef(BaseValidatorModel):
    timeInMillis: Optional[int] = None

class SimpleRuleEvaluationTypeDef(BaseValidatorModel):
    inputPropertyValue: Optional[str] = None
    operator: Optional[ComparisonOperatorType] = None
    thresholdValue: Optional[str] = None

class StateChangeConfigurationTypeDef(BaseValidatorModel):
    triggerType: Optional[Literal["SNOOZE_TIMEOUT"]] = None

class BatchAcknowledgeAlarmRequestRequestTypeDef(BaseValidatorModel):
    acknowledgeActionRequests: Sequence[AcknowledgeAlarmActionRequestTypeDef]

class BatchAcknowledgeAlarmResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisableAlarmResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableAlarmResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchResetAlarmResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchSnoozeAlarmResponseTypeDef(BaseValidatorModel):
    errorEntries: List[BatchAlarmActionErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlarmsResponseTypeDef(BaseValidatorModel):
    alarmSummaries: List[AlarmSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteDetectorResponseTypeDef(BaseValidatorModel):
    batchDeleteDetectorErrorEntries: List[BatchDeleteDetectorErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteDetectorRequestRequestTypeDef(BaseValidatorModel):
    detectors: Sequence[DeleteDetectorRequestTypeDef]

class BatchDisableAlarmRequestRequestTypeDef(BaseValidatorModel):
    disableActionRequests: Sequence[DisableAlarmActionRequestTypeDef]

class BatchEnableAlarmRequestRequestTypeDef(BaseValidatorModel):
    enableActionRequests: Sequence[EnableAlarmActionRequestTypeDef]

class BatchPutMessageResponseTypeDef(BaseValidatorModel):
    BatchPutMessageErrorEntries: List[BatchPutMessageErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchResetAlarmRequestRequestTypeDef(BaseValidatorModel):
    resetActionRequests: Sequence[ResetAlarmActionRequestTypeDef]

class BatchSnoozeAlarmRequestRequestTypeDef(BaseValidatorModel):
    snoozeActionRequests: Sequence[SnoozeAlarmActionRequestTypeDef]

class BatchUpdateDetectorResponseTypeDef(BaseValidatorModel):
    batchUpdateDetectorErrorEntries: List[BatchUpdateDetectorErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerActionTypeDef(BaseValidatorModel):
    actionName: Optional[CustomerActionNameType] = None
    snoozeActionConfiguration: Optional[SnoozeActionConfigurationTypeDef] = None
    enableActionConfiguration: Optional[EnableActionConfigurationTypeDef] = None
    disableActionConfiguration: Optional[DisableActionConfigurationTypeDef] = None
    acknowledgeActionConfiguration: Optional[AcknowledgeActionConfigurationTypeDef] = None
    resetActionConfiguration: Optional[ResetActionConfigurationTypeDef] = None

class DetectorStateDefinitionTypeDef(BaseValidatorModel):
    stateName: str
    variables: Sequence[VariableDefinitionTypeDef]
    timers: Sequence[TimerDefinitionTypeDef]

class DetectorSummaryTypeDef(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    keyValue: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    state: Optional[DetectorStateSummaryTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class DetectorStateTypeDef(BaseValidatorModel):
    stateName: str
    variables: List[VariableTypeDef]
    timers: List[TimerTypeDef]

class MessageTypeDef(BaseValidatorModel):
    messageId: str
    inputName: str
    payload: BlobTypeDef
    timestamp: Optional[TimestampValueTypeDef] = None

class RuleEvaluationTypeDef(BaseValidatorModel):
    simpleRuleEvaluation: Optional[SimpleRuleEvaluationTypeDef] = None

class SystemEventTypeDef(BaseValidatorModel):
    eventType: Optional[Literal["STATE_CHANGE"]] = None
    stateChangeConfiguration: Optional[StateChangeConfigurationTypeDef] = None

class UpdateDetectorRequestTypeDef(BaseValidatorModel):
    messageId: str
    detectorModelName: str
    state: DetectorStateDefinitionTypeDef
    keyValue: Optional[str] = None

class ListDetectorsResponseTypeDef(BaseValidatorModel):
    detectorSummaries: List[DetectorSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectorTypeDef(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    keyValue: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    state: Optional[DetectorStateTypeDef] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class BatchPutMessageRequestRequestTypeDef(BaseValidatorModel):
    messages: Sequence[MessageTypeDef]

class AlarmStateTypeDef(BaseValidatorModel):
    stateName: Optional[AlarmStateNameType] = None
    ruleEvaluation: Optional[RuleEvaluationTypeDef] = None
    customerAction: Optional[CustomerActionTypeDef] = None
    systemEvent: Optional[SystemEventTypeDef] = None

class BatchUpdateDetectorRequestRequestTypeDef(BaseValidatorModel):
    detectors: Sequence[UpdateDetectorRequestTypeDef]

class DescribeDetectorResponseTypeDef(BaseValidatorModel):
    detector: DetectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AlarmTypeDef(BaseValidatorModel):
    alarmModelName: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    keyValue: Optional[str] = None
    alarmState: Optional[AlarmStateTypeDef] = None
    severity: Optional[int] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class DescribeAlarmResponseTypeDef(BaseValidatorModel):
    alarm: AlarmTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

