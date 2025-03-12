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
from aws_resource_validator.pydantic_models.iotevents_constants import *

class AcknowledgeFlowTypeDef(BaseValidatorModel):
    enabled: bool


class ClearTimerActionTypeDef(BaseValidatorModel):
    timerName: str


class ResetTimerActionTypeDef(BaseValidatorModel):
    timerName: str


class SetTimerActionTypeDef(BaseValidatorModel):
    timerName: str
    seconds: Optional[int] = None
    durationExpression: Optional[str] = None


class SetVariableActionTypeDef(BaseValidatorModel):
    variableName: str
    value: str


class InitializationConfigurationTypeDef(BaseValidatorModel):
    disabledOnInitialization: bool


class AlarmModelSummaryTypeDef(BaseValidatorModel):
    creationTime: Optional[datetime] = None
    alarmModelDescription: Optional[str] = None
    alarmModelName: Optional[str] = None


class AlarmModelVersionSummaryTypeDef(BaseValidatorModel):
    alarmModelName: Optional[str] = None
    alarmModelArn: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[AlarmModelVersionStatusType] = None
    statusMessage: Optional[str] = None


class SimpleRuleTypeDef(BaseValidatorModel):
    inputProperty: str
    comparisonOperator: ComparisonOperatorType
    threshold: str


class AnalysisResultLocationTypeDef(BaseValidatorModel):
    path: Optional[str] = None


class AssetPropertyTimestampTypeDef(BaseValidatorModel):
    timeInSeconds: str
    offsetInNanos: Optional[str] = None


class AssetPropertyVariantTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    integerValue: Optional[str] = None
    doubleValue: Optional[str] = None
    booleanValue: Optional[str] = None


class AttributeTypeDef(BaseValidatorModel):
    jsonPath: str


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DetectorModelConfigurationTypeDef(BaseValidatorModel):
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


class InputConfigurationTypeDef(BaseValidatorModel):
    inputName: str
    inputArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    status: InputStatusType
    inputDescription: Optional[str] = None


class DeleteAlarmModelRequestTypeDef(BaseValidatorModel):
    alarmModelName: str


class DeleteDetectorModelRequestTypeDef(BaseValidatorModel):
    detectorModelName: str


class DeleteInputRequestTypeDef(BaseValidatorModel):
    inputName: str


class DescribeAlarmModelRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    alarmModelVersion: Optional[str] = None


class DescribeDetectorModelAnalysisRequestTypeDef(BaseValidatorModel):
    analysisId: str


class DescribeDetectorModelRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    detectorModelVersion: Optional[str] = None


class DescribeInputRequestTypeDef(BaseValidatorModel):
    inputName: str


class DetectorDebugOptionTypeDef(BaseValidatorModel):
    detectorModelName: str
    keyValue: Optional[str] = None


class DetectorModelSummaryTypeDef(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    detectorModelDescription: Optional[str] = None
    creationTime: Optional[datetime] = None


class DetectorModelVersionSummaryTypeDef(BaseValidatorModel):
    detectorModelName: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    detectorModelArn: Optional[str] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[DetectorModelVersionStatusType] = None
    evaluationMethod: Optional[EvaluationMethodType] = None


class EmailContentTypeDef(BaseValidatorModel):
    subject: Optional[str] = None
    additionalMessage: Optional[str] = None


class GetDetectorModelAnalysisResultsRequestTypeDef(BaseValidatorModel):
    analysisId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class IotEventsInputIdentifierTypeDef(BaseValidatorModel):
    inputName: str


class InputSummaryTypeDef(BaseValidatorModel):
    inputName: Optional[str] = None
    inputDescription: Optional[str] = None
    inputArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[InputStatusType] = None


class IotSiteWiseAssetModelPropertyIdentifierTypeDef(BaseValidatorModel):
    assetModelId: str
    propertyId: str


class ListAlarmModelVersionsRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAlarmModelsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDetectorModelVersionsRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDetectorModelsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RoutedResourceTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


class ListInputsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class SSOIdentityTypeDef(BaseValidatorModel):
    identityStoreId: str
    userId: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class AlarmCapabilitiesTypeDef(BaseValidatorModel):
    initializationConfiguration: Optional[InitializationConfigurationTypeDef] = None
    acknowledgeFlow: Optional[AcknowledgeFlowTypeDef] = None


class AlarmRuleTypeDef(BaseValidatorModel):
    simpleRule: Optional[SimpleRuleTypeDef] = None


class AssetPropertyValueTypeDef(BaseValidatorModel):
    value: Optional[AssetPropertyVariantTypeDef] = None
    timestamp: Optional[AssetPropertyTimestampTypeDef] = None
    quality: Optional[str] = None


class InputDefinitionOutputTypeDef(BaseValidatorModel):
    attributes: List[AttributeTypeDef]


class InputDefinitionTypeDef(BaseValidatorModel):
    attributes: Sequence[AttributeTypeDef]


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class CreateAlarmModelResponseTypeDef(BaseValidatorModel):
    creationTime: datetime
    alarmModelArn: str
    alarmModelVersion: str
    lastUpdateTime: datetime
    status: AlarmModelVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDetectorModelAnalysisResponseTypeDef(BaseValidatorModel):
    status: AnalysisStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListAlarmModelVersionsResponseTypeDef(BaseValidatorModel):
    alarmModelVersionSummaries: List[AlarmModelVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAlarmModelsResponseTypeDef(BaseValidatorModel):
    alarmModelSummaries: List[AlarmModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartDetectorModelAnalysisResponseTypeDef(BaseValidatorModel):
    analysisId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAlarmModelResponseTypeDef(BaseValidatorModel):
    creationTime: datetime
    alarmModelArn: str
    alarmModelVersion: str
    lastUpdateTime: datetime
    status: AlarmModelVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDetectorModelResponseTypeDef(BaseValidatorModel):
    detectorModelConfiguration: DetectorModelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDetectorModelResponseTypeDef(BaseValidatorModel):
    detectorModelConfiguration: DetectorModelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInputResponseTypeDef(BaseValidatorModel):
    inputConfiguration: InputConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateInputResponseTypeDef(BaseValidatorModel):
    inputConfiguration: InputConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoggingOptionsOutputTypeDef(BaseValidatorModel):
    roleArn: str
    level: LoggingLevelType
    enabled: bool
    detectorDebugOptions: Optional[List[DetectorDebugOptionTypeDef]] = None


class LoggingOptionsTypeDef(BaseValidatorModel):
    roleArn: str
    level: LoggingLevelType
    enabled: bool
    detectorDebugOptions: Optional[Sequence[DetectorDebugOptionTypeDef]] = None


class ListDetectorModelsResponseTypeDef(BaseValidatorModel):
    detectorModelSummaries: List[DetectorModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDetectorModelVersionsResponseTypeDef(BaseValidatorModel):
    detectorModelVersionSummaries: List[DetectorModelVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PayloadTypeDef(BaseValidatorModel):
    pass


class DynamoDBActionTypeDef(BaseValidatorModel):
    hashKeyField: str
    hashKeyValue: str
    tableName: str
    hashKeyType: Optional[str] = None
    rangeKeyType: Optional[str] = None
    rangeKeyField: Optional[str] = None
    rangeKeyValue: Optional[str] = None
    operation: Optional[str] = None
    payloadField: Optional[str] = None
    payload: Optional[PayloadTypeDef] = None


class DynamoDBv2ActionTypeDef(BaseValidatorModel):
    tableName: str
    payload: Optional[PayloadTypeDef] = None


class FirehoseActionTypeDef(BaseValidatorModel):
    deliveryStreamName: str
    separator: Optional[str] = None
    payload: Optional[PayloadTypeDef] = None


class IotEventsActionTypeDef(BaseValidatorModel):
    inputName: str
    payload: Optional[PayloadTypeDef] = None


class IotTopicPublishActionTypeDef(BaseValidatorModel):
    mqttTopic: str
    payload: Optional[PayloadTypeDef] = None


class LambdaActionTypeDef(BaseValidatorModel):
    functionArn: str
    payload: Optional[PayloadTypeDef] = None


class SNSTopicPublishActionTypeDef(BaseValidatorModel):
    targetArn: str
    payload: Optional[PayloadTypeDef] = None


class SqsActionTypeDef(BaseValidatorModel):
    queueUrl: str
    useBase64: Optional[bool] = None
    payload: Optional[PayloadTypeDef] = None


class ListInputsResponseTypeDef(BaseValidatorModel):
    inputSummaries: List[InputSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IotSiteWiseInputIdentifierTypeDef(BaseValidatorModel):
    iotSiteWiseAssetModelPropertyIdentifier: Optional[ IotSiteWiseAssetModelPropertyIdentifierTypeDef ] = None


class ListInputRoutingsResponseTypeDef(BaseValidatorModel):
    routedResources: List[RoutedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecipientDetailTypeDef(BaseValidatorModel):
    ssoIdentity: Optional[SSOIdentityTypeDef] = None


class AnalysisResultTypeDef(BaseValidatorModel):
    pass


class GetDetectorModelAnalysisResultsResponseTypeDef(BaseValidatorModel):
    analysisResults: List[AnalysisResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IotSiteWiseActionTypeDef(BaseValidatorModel):
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    propertyValue: Optional[AssetPropertyValueTypeDef] = None


class InputTypeDef(BaseValidatorModel):
    inputConfiguration: Optional[InputConfigurationTypeDef] = None
    inputDefinition: Optional[InputDefinitionOutputTypeDef] = None


class DescribeLoggingOptionsResponseTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class NotificationTargetActionsTypeDef(BaseValidatorModel):
    lambdaAction: Optional[LambdaActionTypeDef] = None


class InputIdentifierTypeDef(BaseValidatorModel):
    iotEventsInputIdentifier: Optional[IotEventsInputIdentifierTypeDef] = None
    iotSiteWiseInputIdentifier: Optional[IotSiteWiseInputIdentifierTypeDef] = None


class EmailRecipientsOutputTypeDef(BaseValidatorModel):
    to: Optional[List[RecipientDetailTypeDef]] = None


class EmailRecipientsTypeDef(BaseValidatorModel):
    to: Optional[Sequence[RecipientDetailTypeDef]] = None


class SMSConfigurationOutputTypeDef(BaseValidatorModel):
    recipients: List[RecipientDetailTypeDef]
    senderId: Optional[str] = None
    additionalMessage: Optional[str] = None


class SMSConfigurationTypeDef(BaseValidatorModel):
    recipients: Sequence[RecipientDetailTypeDef]
    senderId: Optional[str] = None
    additionalMessage: Optional[str] = None


class InputDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class CreateInputRequestTypeDef(BaseValidatorModel):
    inputName: str
    inputDefinition: InputDefinitionUnionTypeDef
    inputDescription: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateInputRequestTypeDef(BaseValidatorModel):
    inputName: str
    inputDefinition: InputDefinitionUnionTypeDef
    inputDescription: Optional[str] = None


class LoggingOptionsUnionTypeDef(BaseValidatorModel):
    pass


class PutLoggingOptionsRequestTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsUnionTypeDef


class ListInputRoutingsRequestTypeDef(BaseValidatorModel):
    inputIdentifier: InputIdentifierTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ActionTypeDef(BaseValidatorModel):
    pass


class EventOutputTypeDef(BaseValidatorModel):
    eventName: str
    condition: Optional[str] = None
    actions: Optional[List[ActionTypeDef]] = None


class EventTypeDef(BaseValidatorModel):
    eventName: str
    condition: Optional[str] = None
    actions: Optional[Sequence[ActionTypeDef]] = None


class TransitionEventOutputTypeDef(BaseValidatorModel):
    eventName: str
    condition: str
    nextState: str
    actions: Optional[List[ActionTypeDef]] = None


class TransitionEventTypeDef(BaseValidatorModel):
    eventName: str
    condition: str
    nextState: str
    actions: Optional[Sequence[ActionTypeDef]] = None


class AlarmActionTypeDef(BaseValidatorModel):
    pass


class AlarmEventActionsOutputTypeDef(BaseValidatorModel):
    alarmActions: Optional[List[AlarmActionTypeDef]] = None


class AlarmEventActionsTypeDef(BaseValidatorModel):
    alarmActions: Optional[Sequence[AlarmActionTypeDef]] = None


class EmailConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class NotificationActionOutputTypeDef(BaseValidatorModel):
    action: NotificationTargetActionsTypeDef
    smsConfigurations: Optional[List[SMSConfigurationOutputTypeDef]] = None
    emailConfigurations: Optional[List[EmailConfigurationOutputTypeDef]] = None


class EmailConfigurationTypeDef(BaseValidatorModel):
    pass


class NotificationActionTypeDef(BaseValidatorModel):
    action: NotificationTargetActionsTypeDef
    smsConfigurations: Optional[Sequence[SMSConfigurationTypeDef]] = None
    emailConfigurations: Optional[Sequence[EmailConfigurationTypeDef]] = None


class OnEnterLifecycleOutputTypeDef(BaseValidatorModel):
    events: Optional[List[EventOutputTypeDef]] = None


class OnExitLifecycleOutputTypeDef(BaseValidatorModel):
    events: Optional[List[EventOutputTypeDef]] = None


class OnEnterLifecycleTypeDef(BaseValidatorModel):
    events: Optional[Sequence[EventTypeDef]] = None


class OnExitLifecycleTypeDef(BaseValidatorModel):
    events: Optional[Sequence[EventTypeDef]] = None


class OnInputLifecycleOutputTypeDef(BaseValidatorModel):
    events: Optional[List[EventOutputTypeDef]] = None
    transitionEvents: Optional[List[TransitionEventOutputTypeDef]] = None


class OnInputLifecycleTypeDef(BaseValidatorModel):
    events: Optional[Sequence[EventTypeDef]] = None
    transitionEvents: Optional[Sequence[TransitionEventTypeDef]] = None


class AlarmNotificationOutputTypeDef(BaseValidatorModel):
    notificationActions: Optional[List[NotificationActionOutputTypeDef]] = None


class AlarmNotificationTypeDef(BaseValidatorModel):
    notificationActions: Optional[Sequence[NotificationActionTypeDef]] = None


class StateOutputTypeDef(BaseValidatorModel):
    stateName: str
    onInput: Optional[OnInputLifecycleOutputTypeDef] = None
    onEnter: Optional[OnEnterLifecycleOutputTypeDef] = None
    onExit: Optional[OnExitLifecycleOutputTypeDef] = None


class StateTypeDef(BaseValidatorModel):
    stateName: str
    onInput: Optional[OnInputLifecycleTypeDef] = None
    onEnter: Optional[OnEnterLifecycleTypeDef] = None
    onExit: Optional[OnExitLifecycleTypeDef] = None


class DescribeAlarmModelResponseTypeDef(BaseValidatorModel):
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
    alarmRule: AlarmRuleTypeDef
    alarmNotification: AlarmNotificationOutputTypeDef
    alarmEventActions: AlarmEventActionsOutputTypeDef
    alarmCapabilities: AlarmCapabilitiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DetectorModelDefinitionOutputTypeDef(BaseValidatorModel):
    states: List[StateOutputTypeDef]
    initialStateName: str


class DetectorModelDefinitionTypeDef(BaseValidatorModel):
    states: Sequence[StateTypeDef]
    initialStateName: str


class AlarmNotificationUnionTypeDef(BaseValidatorModel):
    pass


class AlarmEventActionsUnionTypeDef(BaseValidatorModel):
    pass


class CreateAlarmModelRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    roleArn: str
    alarmRule: AlarmRuleTypeDef
    alarmModelDescription: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    key: Optional[str] = None
    severity: Optional[int] = None
    alarmNotification: Optional[AlarmNotificationUnionTypeDef] = None
    alarmEventActions: Optional[AlarmEventActionsUnionTypeDef] = None
    alarmCapabilities: Optional[AlarmCapabilitiesTypeDef] = None


class UpdateAlarmModelRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    roleArn: str
    alarmRule: AlarmRuleTypeDef
    alarmModelDescription: Optional[str] = None
    severity: Optional[int] = None
    alarmNotification: Optional[AlarmNotificationUnionTypeDef] = None
    alarmEventActions: Optional[AlarmEventActionsUnionTypeDef] = None
    alarmCapabilities: Optional[AlarmCapabilitiesTypeDef] = None


class DetectorModelTypeDef(BaseValidatorModel):
    detectorModelDefinition: Optional[DetectorModelDefinitionOutputTypeDef] = None
    detectorModelConfiguration: Optional[DetectorModelConfigurationTypeDef] = None


class DescribeDetectorModelResponseTypeDef(BaseValidatorModel):
    detectorModel: DetectorModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DetectorModelDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class CreateDetectorModelRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    detectorModelDefinition: DetectorModelDefinitionUnionTypeDef
    roleArn: str
    detectorModelDescription: Optional[str] = None
    key: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    evaluationMethod: Optional[EvaluationMethodType] = None


class StartDetectorModelAnalysisRequestTypeDef(BaseValidatorModel):
    detectorModelDefinition: DetectorModelDefinitionUnionTypeDef


class UpdateDetectorModelRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    detectorModelDefinition: DetectorModelDefinitionUnionTypeDef
    roleArn: str
    detectorModelDescription: Optional[str] = None
    evaluationMethod: Optional[EvaluationMethodType] = None


