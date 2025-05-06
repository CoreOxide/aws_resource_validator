from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iotevents.iotevents_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcknowledgeFlow(BaseValidatorModel):
    enabled: bool


class ClearTimerAction(BaseValidatorModel):
    timerName: str


class ResetTimerAction(BaseValidatorModel):
    timerName: str


class SetTimerAction(BaseValidatorModel):
    timerName: str
    seconds: Optional[int] = None
    durationExpression: Optional[str] = None


class SetVariableAction(BaseValidatorModel):
    variableName: str
    value: str


class InitializationConfiguration(BaseValidatorModel):
    disabledOnInitialization: bool


class AlarmModelSummary(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    alarmModelDescription: Optional[str] = None
    alarmModelName: Optional[str] = None


class AlarmModelVersionSummary(BaseValidatorModel):
    alarmModelName: Optional[str] = None
    alarmModelArn: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[AlarmModelVersionStatusType] = None
    statusMessage: Optional[str] = None


class SimpleRule(BaseValidatorModel):
    inputProperty: str
    comparisonOperator: ComparisonOperatorType
    threshold: str


class AnalysisResultLocation(BaseValidatorModel):
    path: Optional[str] = None


class AssetPropertyTimestamp(BaseValidatorModel):
    timeInSeconds: str
    offsetInNanos: Optional[str] = None


class AssetPropertyVariant(BaseValidatorModel):
    stringValue: Optional[str] = None
    integerValue: Optional[str] = None
    doubleValue: Optional[str] = None
    booleanValue: Optional[str] = None


class Attribute(BaseValidatorModel):
    jsonPath: str


class Tag(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DetectorModelConfiguration(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    detectorModelDescription: Optional[str] = None
    detectorModelArn: Optional[str] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[DetectorModelVersionStatusType] = None
    key: Optional[str] = None
    evaluationMethod: Optional[EvaluationMethodType] = None


class InputConfiguration(BaseValidatorModel):
    inputName: str
    inputArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    status: InputStatusType
    inputDescription: Optional[str] = None


class DeleteAlarmModelRequest(BaseValidatorModel):
    alarmModelName: str


class DeleteDetectorModelRequest(BaseValidatorModel):
    detectorModelName: str


class DeleteInputRequest(BaseValidatorModel):
    inputName: str


class DescribeAlarmModelRequest(BaseValidatorModel):
    alarmModelName: str
    alarmModelVersion: Optional[str] = None


class DescribeDetectorModelAnalysisRequest(BaseValidatorModel):
    analysisId: str


class DescribeDetectorModelRequest(BaseValidatorModel):
    detectorModelName: str
    detectorModelVersion: Optional[str] = None


class DescribeInputRequest(BaseValidatorModel):
    inputName: str


class DetectorDebugOption(BaseValidatorModel):
    detectorModelName: str
    keyValue: Optional[str] = None


class DetectorModelSummary(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    detectorModelDescription: Optional[str] = None
    creationTime: Optional[datetime] = None


class DetectorModelVersionSummary(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    detectorModelArn: Optional[str] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[DetectorModelVersionStatusType] = None
    evaluationMethod: Optional[EvaluationMethodType] = None


class Payload(BaseValidatorModel):
    contentExpression: str
    type: PayloadTypeType


class EmailContent(BaseValidatorModel):
    subject: Optional[str] = None
    additionalMessage: Optional[str] = None


class GetDetectorModelAnalysisResultsRequest(BaseValidatorModel):
    analysisId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class IotEventsInputIdentifier(BaseValidatorModel):
    inputName: str


class InputSummary(BaseValidatorModel):
    inputName: Optional[str] = None
    inputDescription: Optional[str] = None
    inputArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[InputStatusType] = None


class IotSiteWiseAssetModelPropertyIdentifier(BaseValidatorModel):
    assetModelId: str
    propertyId: str


class ListAlarmModelVersionsRequest(BaseValidatorModel):
    alarmModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAlarmModelsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDetectorModelVersionsRequest(BaseValidatorModel):
    detectorModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDetectorModelsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RoutedResource(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


class ListInputsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class SSOIdentity(BaseValidatorModel):
    identityStoreId: str
    userId: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class AlarmCapabilities(BaseValidatorModel):
    initializationConfiguration: Optional[InitializationConfiguration] = None
    acknowledgeFlow: Optional[AcknowledgeFlow] = None


class AlarmRule(BaseValidatorModel):
    simpleRule: Optional[SimpleRule] = None


class AnalysisResult(BaseValidatorModel):
    type: Optional[str] = None
    level: Optional[AnalysisResultLevelType] = None
    message: Optional[str] = None
    locations: Optional[List[AnalysisResultLocation]] = None


class AssetPropertyValue(BaseValidatorModel):
    value: Optional[AssetPropertyVariant] = None
    timestamp: Optional[AssetPropertyTimestamp] = None
    quality: Optional[str] = None


class InputDefinitionOutput(BaseValidatorModel):
    attributes: List[Attribute]


class InputDefinition(BaseValidatorModel):
    attributes: List[Attribute]


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class CreateAlarmModelResponse(BaseValidatorModel):
    creationTime: datetime
    alarmModelArn: str
    alarmModelVersion: str
    lastUpdateTime: datetime
    status: AlarmModelVersionStatusType
    ResponseMetadata: ResponseMetadata


class DescribeDetectorModelAnalysisResponse(BaseValidatorModel):
    status: AnalysisStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListAlarmModelVersionsResponse(BaseValidatorModel):
    alarmModelVersionSummaries: List[AlarmModelVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAlarmModelsResponse(BaseValidatorModel):
    alarmModelSummaries: List[AlarmModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class StartDetectorModelAnalysisResponse(BaseValidatorModel):
    analysisId: str
    ResponseMetadata: ResponseMetadata


class UpdateAlarmModelResponse(BaseValidatorModel):
    creationTime: datetime
    alarmModelArn: str
    alarmModelVersion: str
    lastUpdateTime: datetime
    status: AlarmModelVersionStatusType
    ResponseMetadata: ResponseMetadata


class CreateDetectorModelResponse(BaseValidatorModel):
    detectorModelConfiguration: DetectorModelConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateDetectorModelResponse(BaseValidatorModel):
    detectorModelConfiguration: DetectorModelConfiguration
    ResponseMetadata: ResponseMetadata


class CreateInputResponse(BaseValidatorModel):
    inputConfiguration: InputConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateInputResponse(BaseValidatorModel):
    inputConfiguration: InputConfiguration
    ResponseMetadata: ResponseMetadata


class LoggingOptionsOutput(BaseValidatorModel):
    roleArn: str
    level: LoggingLevelType
    enabled: bool
    detectorDebugOptions: Optional[List[DetectorDebugOption]] = None


class LoggingOptions(BaseValidatorModel):
    roleArn: str
    level: LoggingLevelType
    enabled: bool
    detectorDebugOptions: Optional[List[DetectorDebugOption]] = None


class ListDetectorModelsResponse(BaseValidatorModel):
    detectorModelSummaries: List[DetectorModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDetectorModelVersionsResponse(BaseValidatorModel):
    detectorModelVersionSummaries: List[DetectorModelVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DynamoDBAction(BaseValidatorModel):
    hashKeyField: str
    hashKeyValue: str
    tableName: str
    hashKeyType: Optional[str] = None
    rangeKeyType: Optional[str] = None
    rangeKeyField: Optional[str] = None
    rangeKeyValue: Optional[str] = None
    operation: Optional[str] = None
    payloadField: Optional[str] = None
    payload: Optional[Payload] = None


class DynamoDBv2Action(BaseValidatorModel):
    tableName: str
    payload: Optional[Payload] = None


class FirehoseAction(BaseValidatorModel):
    deliveryStreamName: str
    separator: Optional[str] = None
    payload: Optional[Payload] = None


class IotEventsAction(BaseValidatorModel):
    inputName: str
    payload: Optional[Payload] = None


class IotTopicPublishAction(BaseValidatorModel):
    mqttTopic: str
    payload: Optional[Payload] = None


class LambdaAction(BaseValidatorModel):
    functionArn: str
    payload: Optional[Payload] = None


class SNSTopicPublishAction(BaseValidatorModel):
    targetArn: str
    payload: Optional[Payload] = None


class SqsAction(BaseValidatorModel):
    queueUrl: str
    useBase64: Optional[bool] = None
    payload: Optional[Payload] = None


class ListInputsResponse(BaseValidatorModel):
    inputSummaries: List[InputSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IotSiteWiseInputIdentifier(BaseValidatorModel):
    iotSiteWiseAssetModelPropertyIdentifier: Optional[IotSiteWiseAssetModelPropertyIdentifier] = None


class ListInputRoutingsResponse(BaseValidatorModel):
    routedResources: List[RoutedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RecipientDetail(BaseValidatorModel):
    ssoIdentity: Optional[SSOIdentity] = None


class GetDetectorModelAnalysisResultsResponse(BaseValidatorModel):
    analysisResults: List[AnalysisResult]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IotSiteWiseAction(BaseValidatorModel):
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    propertyValue: Optional[AssetPropertyValue] = None


class Input(BaseValidatorModel):
    inputConfiguration: Optional[InputConfiguration] = None
    inputDefinition: Optional[InputDefinitionOutput] = None

InputDefinitionUnion = Union[InputDefinition, InputDefinitionOutput]


class DescribeLoggingOptionsResponse(BaseValidatorModel):
    loggingOptions: LoggingOptionsOutput
    ResponseMetadata: ResponseMetadata

LoggingOptionsUnion = Union[LoggingOptions, LoggingOptionsOutput]


class NotificationTargetActions(BaseValidatorModel):
    lambdaAction: Optional[LambdaAction] = None


class InputIdentifier(BaseValidatorModel):
    iotEventsInputIdentifier: Optional[IotEventsInputIdentifier] = None
    iotSiteWiseInputIdentifier: Optional[IotSiteWiseInputIdentifier] = None


class EmailRecipientsOutput(BaseValidatorModel):
    to: Optional[List[RecipientDetail]] = None


class EmailRecipients(BaseValidatorModel):
    to: Optional[List[RecipientDetail]] = None


class SMSConfigurationOutput(BaseValidatorModel):
    recipients: List[RecipientDetail]
    senderId: Optional[str] = None
    additionalMessage: Optional[str] = None


class SMSConfiguration(BaseValidatorModel):
    recipients: List[RecipientDetail]
    senderId: Optional[str] = None
    additionalMessage: Optional[str] = None


class Action(BaseValidatorModel):
    setVariable: Optional[SetVariableAction] = None
    sns: Optional[SNSTopicPublishAction] = None
    iotTopicPublish: Optional[IotTopicPublishAction] = None
    setTimer: Optional[SetTimerAction] = None
    clearTimer: Optional[ClearTimerAction] = None
    resetTimer: Optional[ResetTimerAction] = None
    lambda_:Optional[LambdaAction] = None
    iotEvents: Optional[IotEventsAction] = None
    sqs: Optional[SqsAction] = None
    firehose: Optional[FirehoseAction] = None
    dynamoDB: Optional[DynamoDBAction] = None
    dynamoDBv2: Optional[DynamoDBv2Action] = None
    iotSiteWise: Optional[IotSiteWiseAction] = None


class AlarmAction(BaseValidatorModel):
    sns: Optional[SNSTopicPublishAction] = None
    iotTopicPublish: Optional[IotTopicPublishAction] = None
    lambda_:Optional[LambdaAction] = None
    iotEvents: Optional[IotEventsAction] = None
    sqs: Optional[SqsAction] = None
    firehose: Optional[FirehoseAction] = None
    dynamoDB: Optional[DynamoDBAction] = None
    dynamoDBv2: Optional[DynamoDBv2Action] = None
    iotSiteWise: Optional[IotSiteWiseAction] = None


class DescribeInputResponse(BaseValidatorModel):
    input: Input
    ResponseMetadata: ResponseMetadata


class CreateInputRequest(BaseValidatorModel):
    inputName: str
    inputDefinition: InputDefinitionUnion
    inputDescription: Optional[str] = None
    tags: Optional[List[Tag]] = None


class UpdateInputRequest(BaseValidatorModel):
    inputName: str
    inputDefinition: InputDefinitionUnion
    inputDescription: Optional[str] = None


class PutLoggingOptionsRequest(BaseValidatorModel):
    loggingOptions: LoggingOptionsUnion


class ListInputRoutingsRequest(BaseValidatorModel):
    inputIdentifier: InputIdentifier
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class EmailConfigurationOutput(BaseValidatorModel):
    from_: str
    recipients: EmailRecipientsOutput
    content: Optional[EmailContent] = None


class EmailConfiguration(BaseValidatorModel):
    from_: str
    recipients: EmailRecipients
    content: Optional[EmailContent] = None


class EventOutput(BaseValidatorModel):
    eventName: str
    condition: Optional[str] = None
    actions: Optional[List[Action]] = None


class Event(BaseValidatorModel):
    eventName: str
    condition: Optional[str] = None
    actions: Optional[List[Action]] = None


class TransitionEventOutput(BaseValidatorModel):
    eventName: str
    condition: str
    nextState: str
    actions: Optional[List[Action]] = None


class TransitionEvent(BaseValidatorModel):
    eventName: str
    condition: str
    nextState: str
    actions: Optional[List[Action]] = None


class AlarmEventActionsOutput(BaseValidatorModel):
    alarmActions: Optional[List[AlarmAction]] = None


class AlarmEventActions(BaseValidatorModel):
    alarmActions: Optional[List[AlarmAction]] = None


class NotificationActionOutput(BaseValidatorModel):
    action: NotificationTargetActions
    smsConfigurations: Optional[List[SMSConfigurationOutput]] = None
    emailConfigurations: Optional[List[EmailConfigurationOutput]] = None


class NotificationAction(BaseValidatorModel):
    action: NotificationTargetActions
    smsConfigurations: Optional[List[SMSConfiguration]] = None
    emailConfigurations: Optional[List[EmailConfiguration]] = None


class OnEnterLifecycleOutput(BaseValidatorModel):
    events: Optional[List[EventOutput]] = None


class OnExitLifecycleOutput(BaseValidatorModel):
    events: Optional[List[EventOutput]] = None


class OnEnterLifecycle(BaseValidatorModel):
    events: Optional[List[Event]] = None


class OnExitLifecycle(BaseValidatorModel):
    events: Optional[List[Event]] = None


class OnInputLifecycleOutput(BaseValidatorModel):
    events: Optional[List[EventOutput]] = None
    transitionEvents: Optional[List[TransitionEventOutput]] = None


class OnInputLifecycle(BaseValidatorModel):
    events: Optional[List[Event]] = None
    transitionEvents: Optional[List[TransitionEvent]] = None

AlarmEventActionsUnion = Union[AlarmEventActions, AlarmEventActionsOutput]


class AlarmNotificationOutput(BaseValidatorModel):
    notificationActions: Optional[List[NotificationActionOutput]] = None


class AlarmNotification(BaseValidatorModel):
    notificationActions: Optional[List[NotificationAction]] = None


class StateOutput(BaseValidatorModel):
    stateName: str
    onInput: Optional[OnInputLifecycleOutput] = None
    onEnter: Optional[OnEnterLifecycleOutput] = None
    onExit: Optional[OnExitLifecycleOutput] = None


class State(BaseValidatorModel):
    stateName: str
    onInput: Optional[OnInputLifecycle] = None
    onEnter: Optional[OnEnterLifecycle] = None
    onExit: Optional[OnExitLifecycle] = None


class DescribeAlarmModelResponse(BaseValidatorModel):
    creationTime: datetime
    alarmModelArn: str
    alarmModelVersion: str
    lastUpdateTime: datetime
    status: AlarmModelVersionStatusType
    statusMessage: str
    alarmModelName: str
    alarmModelDescription: str
    roleArn: str
    key: str
    severity: int
    alarmRule: AlarmRule
    alarmNotification: AlarmNotificationOutput
    alarmEventActions: AlarmEventActionsOutput
    alarmCapabilities: AlarmCapabilities
    ResponseMetadata: ResponseMetadata

AlarmNotificationUnion = Union[AlarmNotification, AlarmNotificationOutput]


class DetectorModelDefinitionOutput(BaseValidatorModel):
    states: List[StateOutput]
    initialStateName: str


class DetectorModelDefinition(BaseValidatorModel):
    states: List[State]
    initialStateName: str


class CreateAlarmModelRequest(BaseValidatorModel):
    alarmModelName: str
    roleArn: str
    alarmRule: AlarmRule
    alarmModelDescription: Optional[str] = None
    tags: Optional[List[Tag]] = None
    key: Optional[str] = None
    severity: Optional[int] = None
    alarmNotification: Optional[AlarmNotificationUnion] = None
    alarmEventActions: Optional[AlarmEventActionsUnion] = None
    alarmCapabilities: Optional[AlarmCapabilities] = None


class UpdateAlarmModelRequest(BaseValidatorModel):
    alarmModelName: str
    roleArn: str
    alarmRule: AlarmRule
    alarmModelDescription: Optional[str] = None
    severity: Optional[int] = None
    alarmNotification: Optional[AlarmNotificationUnion] = None
    alarmEventActions: Optional[AlarmEventActionsUnion] = None
    alarmCapabilities: Optional[AlarmCapabilities] = None


class DetectorModel(BaseValidatorModel):
    detectorModelDefinition: Optional[DetectorModelDefinitionOutput] = None
    detectorModelConfiguration: Optional[DetectorModelConfiguration] = None

DetectorModelDefinitionUnion = Union[DetectorModelDefinition, DetectorModelDefinitionOutput]


class DescribeDetectorModelResponse(BaseValidatorModel):
    detectorModel: DetectorModel
    ResponseMetadata: ResponseMetadata


class CreateDetectorModelRequest(BaseValidatorModel):
    detectorModelName: str
    detectorModelDefinition: DetectorModelDefinitionUnion
    roleArn: str
    detectorModelDescription: Optional[str] = None
    key: Optional[str] = None
    tags: Optional[List[Tag]] = None
    evaluationMethod: Optional[EvaluationMethodType] = None


class StartDetectorModelAnalysisRequest(BaseValidatorModel):
    detectorModelDefinition: DetectorModelDefinitionUnion


class UpdateDetectorModelRequest(BaseValidatorModel):
    detectorModelName: str
    detectorModelDefinition: DetectorModelDefinitionUnion
    roleArn: str
    detectorModelDescription: Optional[str] = None
    evaluationMethod: Optional[EvaluationMethodType] = None