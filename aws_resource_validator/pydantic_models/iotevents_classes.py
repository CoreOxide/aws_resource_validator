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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class DeleteAlarmModelRequestRequestTypeDef(BaseValidatorModel):
    alarmModelName: str

class DeleteDetectorModelRequestRequestTypeDef(BaseValidatorModel):
    detectorModelName: str

class DeleteInputRequestRequestTypeDef(BaseValidatorModel):
    inputName: str

class DescribeAlarmModelRequestRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    alarmModelVersion: Optional[str] = None

class DescribeDetectorModelAnalysisRequestRequestTypeDef(BaseValidatorModel):
    analysisId: str

class DescribeDetectorModelRequestRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    detectorModelVersion: Optional[str] = None

class DescribeInputRequestRequestTypeDef(BaseValidatorModel):
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

class PayloadTypeDef(BaseValidatorModel):
    contentExpression: str
    type: PayloadTypeType

class EmailContentTypeDef(BaseValidatorModel):
    subject: Optional[str] = None
    additionalMessage: Optional[str] = None

class GetDetectorModelAnalysisResultsRequestRequestTypeDef(BaseValidatorModel):
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

class ListAlarmModelVersionsRequestRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAlarmModelsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDetectorModelVersionsRequestRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDetectorModelsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RoutedResourceTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None

class ListInputsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class SSOIdentityTypeDef(BaseValidatorModel):
    identityStoreId: str
    userId: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AlarmCapabilitiesTypeDef(BaseValidatorModel):
    initializationConfiguration: Optional[InitializationConfigurationTypeDef] = None
    acknowledgeFlow: Optional[AcknowledgeFlowTypeDef] = None

class AlarmRuleTypeDef(BaseValidatorModel):
    simpleRule: Optional[SimpleRuleTypeDef] = None

class AnalysisResultTypeDef(BaseValidatorModel):
    type: Optional[str] = None
    level: Optional[AnalysisResultLevelType] = None
    message: Optional[str] = None
    locations: Optional[List[AnalysisResultLocationTypeDef]] = None

class AssetPropertyValueTypeDef(BaseValidatorModel):
    value: Optional[AssetPropertyVariantTypeDef] = None
    timestamp: Optional[AssetPropertyTimestampTypeDef] = None
    quality: Optional[str] = None

class InputDefinitionTypeDef(BaseValidatorModel):
    attributes: Sequence[AttributeTypeDef]

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAlarmModelsResponseTypeDef(BaseValidatorModel):
    alarmModelSummaries: List[AlarmModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class LoggingOptionsTypeDef(BaseValidatorModel):
    roleArn: str
    level: LoggingLevelType
    enabled: bool
    detectorDebugOptions: Optional[List[DetectorDebugOptionTypeDef]] = None

class ListDetectorModelsResponseTypeDef(BaseValidatorModel):
    detectorModelSummaries: List[DetectorModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDetectorModelVersionsResponseTypeDef(BaseValidatorModel):
    detectorModelVersionSummaries: List[DetectorModelVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IotSiteWiseInputIdentifierTypeDef(BaseValidatorModel):
    iotSiteWiseAssetModelPropertyIdentifier: Optional[       IotSiteWiseAssetModelPropertyIdentifierTypeDef     ] = None

class ListInputRoutingsResponseTypeDef(BaseValidatorModel):
    routedResources: List[RoutedResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecipientDetailTypeDef(BaseValidatorModel):
    ssoIdentity: Optional[SSOIdentityTypeDef] = None

class GetDetectorModelAnalysisResultsResponseTypeDef(BaseValidatorModel):
    analysisResults: List[AnalysisResultTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IotSiteWiseActionTypeDef(BaseValidatorModel):
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None
    propertyValue: Optional[AssetPropertyValueTypeDef] = None

class CreateInputRequestRequestTypeDef(BaseValidatorModel):
    inputName: str
    inputDefinition: InputDefinitionTypeDef
    inputDescription: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class InputTypeDef(BaseValidatorModel):
    inputConfiguration: Optional[InputConfigurationTypeDef] = None
    inputDefinition: Optional[InputDefinitionTypeDef] = None

class UpdateInputRequestRequestTypeDef(BaseValidatorModel):
    inputName: str
    inputDefinition: InputDefinitionTypeDef
    inputDescription: Optional[str] = None

class DescribeLoggingOptionsResponseTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestRequestTypeDef(BaseValidatorModel):
    loggingOptions: LoggingOptionsTypeDef

class NotificationTargetActionsTypeDef(BaseValidatorModel):
    lambdaAction: Optional[LambdaActionTypeDef] = None

class InputIdentifierTypeDef(BaseValidatorModel):
    iotEventsInputIdentifier: Optional[IotEventsInputIdentifierTypeDef] = None
    iotSiteWiseInputIdentifier: Optional[IotSiteWiseInputIdentifierTypeDef] = None

class EmailRecipientsTypeDef(BaseValidatorModel):
    to: Optional[Sequence[RecipientDetailTypeDef]] = None

class SMSConfigurationTypeDef(BaseValidatorModel):
    recipients: Sequence[RecipientDetailTypeDef]
    senderId: Optional[str] = None
    additionalMessage: Optional[str] = None

class ActionTypeDef(BaseValidatorModel):
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

class AlarmActionTypeDef(BaseValidatorModel):
    sns: Optional[SNSTopicPublishActionTypeDef] = None
    iotTopicPublish: Optional[IotTopicPublishActionTypeDef] = None
    lambda: Optional[LambdaActionTypeDef] = None
    iotEvents: Optional[IotEventsActionTypeDef] = None
    sqs: Optional[SqsActionTypeDef] = None
    firehose: Optional[FirehoseActionTypeDef] = None
    dynamoDB: Optional[DynamoDBActionTypeDef] = None
    dynamoDBv2: Optional[DynamoDBv2ActionTypeDef] = None
    iotSiteWise: Optional[IotSiteWiseActionTypeDef] = None

class DescribeInputResponseTypeDef(BaseValidatorModel):
    input: InputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInputRoutingsRequestRequestTypeDef(BaseValidatorModel):
    inputIdentifier: InputIdentifierTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class EmailConfigurationTypeDef(BaseValidatorModel):
    from: str
    recipients: EmailRecipientsTypeDef
    content: Optional[EmailContentTypeDef] = None

class EventTypeDef(BaseValidatorModel):
    eventName: str
    condition: Optional[str] = None
    actions: Optional[Sequence[ActionTypeDef]] = None

class TransitionEventTypeDef(BaseValidatorModel):
    eventName: str
    condition: str
    nextState: str
    actions: Optional[Sequence[ActionTypeDef]] = None

class AlarmEventActionsTypeDef(BaseValidatorModel):
    alarmActions: Optional[Sequence[AlarmActionTypeDef]] = None

class NotificationActionTypeDef(BaseValidatorModel):
    action: NotificationTargetActionsTypeDef
    smsConfigurations: Optional[Sequence[SMSConfigurationTypeDef]] = None
    emailConfigurations: Optional[Sequence[EmailConfigurationTypeDef]] = None

class OnEnterLifecycleTypeDef(BaseValidatorModel):
    events: Optional[Sequence[EventTypeDef]] = None

class OnExitLifecycleTypeDef(BaseValidatorModel):
    events: Optional[Sequence[EventTypeDef]] = None

class OnInputLifecycleTypeDef(BaseValidatorModel):
    events: Optional[Sequence[EventTypeDef]] = None
    transitionEvents: Optional[Sequence[TransitionEventTypeDef]] = None

class AlarmNotificationTypeDef(BaseValidatorModel):
    notificationActions: Optional[Sequence[NotificationActionTypeDef]] = None

class StateTypeDef(BaseValidatorModel):
    stateName: str
    onInput: Optional[OnInputLifecycleTypeDef] = None
    onEnter: Optional[OnEnterLifecycleTypeDef] = None
    onExit: Optional[OnExitLifecycleTypeDef] = None

class CreateAlarmModelRequestRequestTypeDef(BaseValidatorModel):
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
    alarmNotification: AlarmNotificationTypeDef
    alarmEventActions: AlarmEventActionsTypeDef
    alarmCapabilities: AlarmCapabilitiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAlarmModelRequestRequestTypeDef(BaseValidatorModel):
    alarmModelName: str
    roleArn: str
    alarmRule: AlarmRuleTypeDef
    alarmModelDescription: Optional[str] = None
    severity: Optional[int] = None
    alarmNotification: Optional[AlarmNotificationTypeDef] = None
    alarmEventActions: Optional[AlarmEventActionsTypeDef] = None
    alarmCapabilities: Optional[AlarmCapabilitiesTypeDef] = None

class DetectorModelDefinitionTypeDef(BaseValidatorModel):
    states: Sequence[StateTypeDef]
    initialStateName: str

class CreateDetectorModelRequestRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    detectorModelDefinition: DetectorModelDefinitionTypeDef
    roleArn: str
    detectorModelDescription: Optional[str] = None
    key: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    evaluationMethod: Optional[EvaluationMethodType] = None

class DetectorModelTypeDef(BaseValidatorModel):
    detectorModelDefinition: Optional[DetectorModelDefinitionTypeDef] = None
    detectorModelConfiguration: Optional[DetectorModelConfigurationTypeDef] = None

class StartDetectorModelAnalysisRequestRequestTypeDef(BaseValidatorModel):
    detectorModelDefinition: DetectorModelDefinitionTypeDef

class UpdateDetectorModelRequestRequestTypeDef(BaseValidatorModel):
    detectorModelName: str
    detectorModelDefinition: DetectorModelDefinitionTypeDef
    roleArn: str
    detectorModelDescription: Optional[str] = None
    evaluationMethod: Optional[EvaluationMethodType] = None

class DescribeDetectorModelResponseTypeDef(BaseValidatorModel):
    detectorModel: DetectorModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

