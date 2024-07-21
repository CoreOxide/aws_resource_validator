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
from aws_resource_validator.pydantic_models.iotevents_constants import *

class AcknowledgeFlowTypeDef(BaseModel):
    enabled: bool

class ClearTimerActionTypeDef(BaseModel):
    timerName: str

class ResetTimerActionTypeDef(BaseModel):
    timerName: str

class SetTimerActionTypeDef(BaseModel):
    timerName: str
    seconds: Optional[int] = None
    durationExpression: Optional[str] = None

class SetVariableActionTypeDef(BaseModel):
    variableName: str
    value: str

class InitializationConfigurationTypeDef(BaseModel):
    disabledOnInitialization: bool

class AlarmModelSummaryTypeDef(BaseModel):
    creationTime: Optional[datetime] = None
    alarmModelDescription: Optional[str] = None
    alarmModelName: Optional[str] = None

class AlarmModelVersionSummaryTypeDef(BaseModel):
    alarmModelName: Optional[str] = None
    alarmModelArn: Optional[str] = None
    alarmModelVersion: Optional[str] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[AlarmModelVersionStatusType] = None
    statusMessage: Optional[str] = None

class SimpleRuleTypeDef(BaseModel):
    inputProperty: str
    comparisonOperator: ComparisonOperatorType
    threshold: str

class AnalysisResultLocationTypeDef(BaseModel):
    path: Optional[str] = None

class AssetPropertyTimestampTypeDef(BaseModel):
    timeInSeconds: str
    offsetInNanos: Optional[str] = None

class AssetPropertyVariantTypeDef(BaseModel):
    stringValue: Optional[str] = None
    integerValue: Optional[str] = None
    doubleValue: Optional[str] = None
    booleanValue: Optional[str] = None

class AttributeTypeDef(BaseModel):
    jsonPath: str

class TagTypeDef(BaseModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DetectorModelConfigurationTypeDef(BaseModel):
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

class InputConfigurationTypeDef(BaseModel):
    inputName: str
    inputArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    status: InputStatusType
    inputDescription: Optional[str] = None

class DeleteAlarmModelRequestRequestTypeDef(BaseModel):
    alarmModelName: str

class DeleteDetectorModelRequestRequestTypeDef(BaseModel):
    detectorModelName: str

class DeleteInputRequestRequestTypeDef(BaseModel):
    inputName: str

class DescribeAlarmModelRequestRequestTypeDef(BaseModel):
    alarmModelName: str
    alarmModelVersion: Optional[str] = None

class DescribeDetectorModelAnalysisRequestRequestTypeDef(BaseModel):
    analysisId: str

class DescribeDetectorModelRequestRequestTypeDef(BaseModel):
    detectorModelName: str
    detectorModelVersion: Optional[str] = None

class DescribeInputRequestRequestTypeDef(BaseModel):
    inputName: str

class DetectorDebugOptionTypeDef(BaseModel):
    detectorModelName: str
    keyValue: Optional[str] = None

class DetectorModelSummaryTypeDef(BaseModel):
    detectorModelName: Optional[str] = None
    detectorModelDescription: Optional[str] = None
    creationTime: Optional[datetime] = None

class DetectorModelVersionSummaryTypeDef(BaseModel):
    detectorModelName: Optional[str] = None
    detectorModelVersion: Optional[str] = None
    detectorModelArn: Optional[str] = None
    roleArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[DetectorModelVersionStatusType] = None
    evaluationMethod: Optional[EvaluationMethodType] = None

class PayloadTypeDef(BaseModel):
    contentExpression: str
    type: PayloadTypeType

class EmailContentTypeDef(BaseModel):
    subject: Optional[str] = None
    additionalMessage: Optional[str] = None

class GetDetectorModelAnalysisResultsRequestRequestTypeDef(BaseModel):
    analysisId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class IotEventsInputIdentifierTypeDef(BaseModel):
    inputName: str

class InputSummaryTypeDef(BaseModel):
    inputName: Optional[str] = None
    inputDescription: Optional[str] = None
    inputArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    status: Optional[InputStatusType] = None

class IotSiteWiseAssetModelPropertyIdentifierTypeDef(BaseModel):
    assetModelId: str
    propertyId: str

class ListAlarmModelVersionsRequestRequestTypeDef(BaseModel):
    alarmModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAlarmModelsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDetectorModelVersionsRequestRequestTypeDef(BaseModel):
    detectorModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDetectorModelsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RoutedResourceTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None

class ListInputsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class SSOIdentityTypeDef(BaseModel):
    identityStoreId: str
    userId: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AlarmCapabilitiesTypeDef(BaseModel):
    initializationConfiguration: Optional[InitializationConfigurationTypeDef] = None
    acknowledgeFlow: Optional[AcknowledgeFlowTypeDef] = None

class AlarmRuleTypeDef(BaseModel):
    simpleRule: Optional[SimpleRuleTypeDef] = None

class AnalysisResultTypeDef(BaseModel):
    type: Optional[str] = None
    level: Optional[AnalysisResultLevelType] = None
    message: Optional[str] = None
    locations: Optional[List[AnalysisResultLocationTypeDef]] = None

class AssetPropertyValueTypeDef(BaseModel):
    value: Optional[AssetPropertyVariantTypeDef] = None
    timestamp: Optional[AssetPropertyTimestampTypeDef] = None
    quality: Optional[str] = None

class InputDefinitionTypeDef(BaseModel):
    attributes: Sequence[AttributeTypeDef]

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateAlarmModelResponseTypeDef(BaseModel):
    creationTime: datetime
    alarmModelArn: str
    alarmModelVersion: str
    lastUpdateTime: datetime
    status: AlarmModelVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDetectorModelAnalysisResponseTypeDef(BaseModel):
    status: AnalysisStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlarmModelVersionsResponseTypeDef(BaseModel):
    alarmModelVersionSummaries: List[AlarmModelVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlarmModelsResponseTypeDef(BaseModel):
    alarmModelSummaries: List[AlarmModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDetectorModelAnalysisResponseTypeDef(BaseModel):
    analysisId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAlarmModelResponseTypeDef(BaseModel):
    creationTime: datetime
    alarmModelArn: str
    alarmModelVersion: str
    lastUpdateTime: datetime
    status: AlarmModelVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDetectorModelResponseTypeDef(BaseModel):
    detectorModelConfiguration: DetectorModelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDetectorModelResponseTypeDef(BaseModel):
    detectorModelConfiguration: DetectorModelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInputResponseTypeDef(BaseModel):
    inputConfiguration: InputConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInputResponseTypeDef(BaseModel):
    inputConfiguration: InputConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingOptionsTypeDef(BaseModel):
    roleArn: str
    level: LoggingLevelType
    enabled: bool
    detectorDebugOptions: Optional[List[DetectorDebugOptionTypeDef]] = None

class ListDetectorModelsResponseTypeDef(BaseModel):
    detectorModelSummaries: List[DetectorModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDetectorModelVersionsResponseTypeDef(BaseModel):
    detectorModelVersionSummaries: List[DetectorModelVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DynamoDBActionTypeDef(BaseModel):
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

class DynamoDBv2ActionTypeDef(BaseModel):
    tableName: str
    payload: Optional[PayloadTypeDef] = None

class FirehoseActionTypeDef(BaseModel):
    deliveryStreamName: str
    separator: Optional[str] = None
    payload: Optional[PayloadTypeDef] = None

class IotEventsActionTypeDef(BaseModel):
    inputName: str
    payload: Optional[PayloadTypeDef] = None

class IotTopicPublishActionTypeDef(BaseModel):
    mqttTopic: str
    payload: Optional[PayloadTypeDef] = None

class LambdaActionTypeDef(BaseModel):
    functionArn: str
    payload: Optional[PayloadTypeDef] = None

class SNSTopicPublishActionTypeDef(BaseModel):
    targetArn: str
    payload: Optional[PayloadTypeDef] = None

class SqsActionTypeDef(BaseModel):
    queueUrl: str
    useBase64: Optional[bool] = None
    payload: Optional[PayloadTypeDef] = None

class ListInputsResponseTypeDef(BaseModel):
    inputSummaries: List[InputSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IotSiteWiseInputIdentifierTypeDef(BaseModel):
    iotSiteWiseAssetModelPropertyIdentifier: Optional[       IotSiteWiseAssetModelPropertyIdentifierTypeDef     ] = None

class ListInputRoutingsResponseTypeDef(BaseModel):
    routedResources: List[RoutedResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecipientDetailTypeDef(BaseModel):
    ssoIdentity: Optional[SSOIdentityTypeDef] = None

class GetDetectorModelAnalysisResultsResponseTypeDef(BaseModel):
    analysisResults: List[AnalysisResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IotSiteWiseActionTypeDef(BaseModel):
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    propertyValue: Optional[AssetPropertyValueTypeDef] = None

class CreateInputRequestRequestTypeDef(BaseModel):
    inputName: str
    inputDefinition: InputDefinitionTypeDef
    inputDescription: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class InputTypeDef(BaseModel):
    inputConfiguration: Optional[InputConfigurationTypeDef] = None
    inputDefinition: Optional[InputDefinitionTypeDef] = None

class UpdateInputRequestRequestTypeDef(BaseModel):
    inputName: str
    inputDefinition: InputDefinitionTypeDef
    inputDescription: Optional[str] = None

class DescribeLoggingOptionsResponseTypeDef(BaseModel):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestRequestTypeDef(BaseModel):
    loggingOptions: LoggingOptionsTypeDef

class NotificationTargetActionsTypeDef(BaseModel):
    lambdaAction: Optional[LambdaActionTypeDef] = None

class InputIdentifierTypeDef(BaseModel):
    iotEventsInputIdentifier: Optional[IotEventsInputIdentifierTypeDef] = None
    iotSiteWiseInputIdentifier: Optional[IotSiteWiseInputIdentifierTypeDef] = None

class EmailRecipientsTypeDef(BaseModel):
    to: Optional[Sequence[RecipientDetailTypeDef]] = None

class SMSConfigurationTypeDef(BaseModel):
    recipients: Sequence[RecipientDetailTypeDef]
    senderId: Optional[str] = None
    additionalMessage: Optional[str] = None

class ActionTypeDef(BaseModel):
    setVariable: Optional[SetVariableActionTypeDef] = None
    sns: Optional[SNSTopicPublishActionTypeDef] = None
    iotTopicPublish: Optional[IotTopicPublishActionTypeDef] = None
    setTimer: Optional[SetTimerActionTypeDef] = None
    clearTimer: Optional[ClearTimerActionTypeDef] = None
    resetTimer: Optional[ResetTimerActionTypeDef] = None
    lambda: Optional[LambdaActionTypeDef] = None
    iotEvents: Optional[IotEventsActionTypeDef] = None
    sqs: Optional[SqsActionTypeDef] = None
    firehose: Optional[FirehoseActionTypeDef] = None
    dynamoDB: Optional[DynamoDBActionTypeDef] = None
    dynamoDBv2: Optional[DynamoDBv2ActionTypeDef] = None
    iotSiteWise: Optional[IotSiteWiseActionTypeDef] = None

class AlarmActionTypeDef(BaseModel):
    sns: Optional[SNSTopicPublishActionTypeDef] = None
    iotTopicPublish: Optional[IotTopicPublishActionTypeDef] = None
    lambda: Optional[LambdaActionTypeDef] = None
    iotEvents: Optional[IotEventsActionTypeDef] = None
    sqs: Optional[SqsActionTypeDef] = None
    firehose: Optional[FirehoseActionTypeDef] = None
    dynamoDB: Optional[DynamoDBActionTypeDef] = None
    dynamoDBv2: Optional[DynamoDBv2ActionTypeDef] = None
    iotSiteWise: Optional[IotSiteWiseActionTypeDef] = None

class DescribeInputResponseTypeDef(BaseModel):
    input: InputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInputRoutingsRequestRequestTypeDef(BaseModel):
    inputIdentifier: InputIdentifierTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class EmailConfigurationTypeDef(BaseModel):
    from: str
    recipients: EmailRecipientsTypeDef
    content: Optional[EmailContentTypeDef] = None

class EventTypeDef(BaseModel):
    eventName: str
    condition: Optional[str] = None
    actions: Optional[Sequence[ActionTypeDef]] = None

class TransitionEventTypeDef(BaseModel):
    eventName: str
    condition: str
    nextState: str
    actions: Optional[Sequence[ActionTypeDef]] = None

class AlarmEventActionsTypeDef(BaseModel):
    alarmActions: Optional[Sequence[AlarmActionTypeDef]] = None

class NotificationActionTypeDef(BaseModel):
    action: NotificationTargetActionsTypeDef
    smsConfigurations: Optional[Sequence[SMSConfigurationTypeDef]] = None
    emailConfigurations: Optional[Sequence[EmailConfigurationTypeDef]] = None

class OnEnterLifecycleTypeDef(BaseModel):
    events: Optional[Sequence[EventTypeDef]] = None

class OnExitLifecycleTypeDef(BaseModel):
    events: Optional[Sequence[EventTypeDef]] = None

class OnInputLifecycleTypeDef(BaseModel):
    events: Optional[Sequence[EventTypeDef]] = None
    transitionEvents: Optional[Sequence[TransitionEventTypeDef]] = None

class AlarmNotificationTypeDef(BaseModel):
    notificationActions: Optional[Sequence[NotificationActionTypeDef]] = None

class StateTypeDef(BaseModel):
    stateName: str
    onInput: Optional[OnInputLifecycleTypeDef] = None
    onEnter: Optional[OnEnterLifecycleTypeDef] = None
    onExit: Optional[OnExitLifecycleTypeDef] = None

class CreateAlarmModelRequestRequestTypeDef(BaseModel):
    alarmModelName: str
    roleArn: str
    alarmRule: AlarmRuleTypeDef
    alarmModelDescription: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    key: Optional[str] = None
    severity: Optional[int] = None
    alarmNotification: Optional[AlarmNotificationTypeDef] = None
    alarmEventActions: Optional[AlarmEventActionsTypeDef] = None
    alarmCapabilities: Optional[AlarmCapabilitiesTypeDef] = None

class DescribeAlarmModelResponseTypeDef(BaseModel):
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
    alarmNotification: AlarmNotificationTypeDef
    alarmEventActions: AlarmEventActionsTypeDef
    alarmCapabilities: AlarmCapabilitiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAlarmModelRequestRequestTypeDef(BaseModel):
    alarmModelName: str
    roleArn: str
    alarmRule: AlarmRuleTypeDef
    alarmModelDescription: Optional[str] = None
    severity: Optional[int] = None
    alarmNotification: Optional[AlarmNotificationTypeDef] = None
    alarmEventActions: Optional[AlarmEventActionsTypeDef] = None
    alarmCapabilities: Optional[AlarmCapabilitiesTypeDef] = None

class DetectorModelDefinitionTypeDef(BaseModel):
    states: Sequence[StateTypeDef]
    initialStateName: str

class CreateDetectorModelRequestRequestTypeDef(BaseModel):
    detectorModelName: str
    detectorModelDefinition: DetectorModelDefinitionTypeDef
    roleArn: str
    detectorModelDescription: Optional[str] = None
    key: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    evaluationMethod: Optional[EvaluationMethodType] = None

class DetectorModelTypeDef(BaseModel):
    detectorModelDefinition: Optional[DetectorModelDefinitionTypeDef] = None
    detectorModelConfiguration: Optional[DetectorModelConfigurationTypeDef] = None

class StartDetectorModelAnalysisRequestRequestTypeDef(BaseModel):
    detectorModelDefinition: DetectorModelDefinitionTypeDef

class UpdateDetectorModelRequestRequestTypeDef(BaseModel):
    detectorModelName: str
    detectorModelDefinition: DetectorModelDefinitionTypeDef
    roleArn: str
    detectorModelDescription: Optional[str] = None
    evaluationMethod: Optional[EvaluationMethodType] = None

class DescribeDetectorModelResponseTypeDef(BaseModel):
    detectorModel: DetectorModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

