# Iotevents Classes

# AcknowledgeFlow

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# Action

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmAction

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmCapabilities

### initializationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.InitializationConfiguration]

### acknowledgeFlow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AcknowledgeFlow]


# AlarmEventActions

### alarmActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.AlarmAction]]


# AlarmEventActionsOutput

### alarmActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AlarmAction]]


# AlarmEventActionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmModelSummary

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### alarmModelDescription
- **Type**: typing.Optional[str]

### alarmModelName
- **Type**: typing.Optional[str]


# AlarmModelVersionSummary

### alarmModelName
- **Type**: typing.Optional[str]

### alarmModelArn
- **Type**: typing.Optional[str]

### alarmModelVersion
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'FAILED', 'INACTIVE']]

### statusMessage
- **Type**: typing.Optional[str]


# AlarmNotification

### notificationActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.NotificationAction]]


# AlarmNotificationOutput

### notificationActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.NotificationActionOutput]]


# AlarmNotificationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmRule

### simpleRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SimpleRule]


# AnalysisResult

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalysisResultLocation

### path
- **Type**: typing.Optional[str]


# AssetPropertyTimestamp

### timeInSeconds
- **Type**: <class 'str'>
- **Required**: Yes

### offsetInNanos
- **Type**: typing.Optional[str]


# AssetPropertyValue

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AssetPropertyVariant]

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AssetPropertyTimestamp]

### quality
- **Type**: typing.Optional[str]


# AssetPropertyVariant

### stringValue
- **Type**: typing.Optional[str]

### integerValue
- **Type**: typing.Optional[str]

### doubleValue
- **Type**: typing.Optional[str]

### booleanValue
- **Type**: typing.Optional[str]


# Attribute

### jsonPath
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClearTimerAction

### timerName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAlarmModelRequest

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### alarmRule
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmRule'>
- **Required**: Yes

### alarmModelDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Tag]]

### key
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[int]

### alarmNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationUnion]

### alarmEventActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsUnion]

### alarmCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmCapabilities]


# CreateAlarmModelResponse

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### alarmModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'FAILED', 'INACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDetectorModelRequest

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionUnion'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDescription
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Tag]]

### evaluationMethod
- **Type**: typing.Optional[typing.Literal['BATCH', 'SERIAL']]


# CreateDetectorModelResponse

### detectorModelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInputRequest

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### inputDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionUnion'>
- **Required**: Yes

### inputDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Tag]]


# CreateInputResponse

### inputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAlarmModelRequest

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorModelRequest

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputRequest

### inputName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlarmModelRequest

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelVersion
- **Type**: typing.Optional[str]


# DescribeAlarmModelResponse

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### alarmModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'FAILED', 'INACTIVE']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelDescription
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### severity
- **Type**: <class 'int'>
- **Required**: Yes

### alarmRule
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmRule'>
- **Required**: Yes

### alarmNotification
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationOutput'>
- **Required**: Yes

### alarmEventActions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsOutput'>
- **Required**: Yes

### alarmCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmCapabilities'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDetectorModelAnalysisRequest

### analysisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDetectorModelAnalysisResponse

### status
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'RUNNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDetectorModelRequest

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelVersion
- **Type**: typing.Optional[str]


# DescribeDetectorModelResponse

### detectorModel
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInputRequest

### inputName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoggingOptionsResponse

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.LoggingOptionsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# DetectorDebugOption

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# DetectorModel

### detectorModelDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionOutput]

### detectorModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelConfiguration]


# DetectorModelConfiguration

### detectorModelName
- **Type**: typing.Optional[str]

### detectorModelVersion
- **Type**: typing.Optional[str]

### detectorModelDescription
- **Type**: typing.Optional[str]

### detectorModelArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'DEPRECATED', 'DRAFT', 'FAILED', 'INACTIVE', 'PAUSED']]

### key
- **Type**: typing.Optional[str]

### evaluationMethod
- **Type**: typing.Optional[typing.Literal['BATCH', 'SERIAL']]


# DetectorModelDefinition

### states
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.State]
- **Required**: Yes

### initialStateName
- **Type**: <class 'str'>
- **Required**: Yes


# DetectorModelDefinitionOutput

### states
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.StateOutput]
- **Required**: Yes

### initialStateName
- **Type**: <class 'str'>
- **Required**: Yes


# DetectorModelDefinitionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DetectorModelSummary

### detectorModelName
- **Type**: typing.Optional[str]

### detectorModelDescription
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]


# DetectorModelVersionSummary

### detectorModelName
- **Type**: typing.Optional[str]

### detectorModelVersion
- **Type**: typing.Optional[str]

### detectorModelArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'DEPRECATED', 'DRAFT', 'FAILED', 'INACTIVE', 'PAUSED']]

### evaluationMethod
- **Type**: typing.Optional[typing.Literal['BATCH', 'SERIAL']]


# DynamoDBAction

### hashKeyField
- **Type**: <class 'str'>
- **Required**: Yes

### hashKeyValue
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### hashKeyType
- **Type**: typing.Optional[str]

### rangeKeyType
- **Type**: typing.Optional[str]

### rangeKeyField
- **Type**: typing.Optional[str]

### rangeKeyValue
- **Type**: typing.Optional[str]

### operation
- **Type**: typing.Optional[str]

### payloadField
- **Type**: typing.Optional[str]

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.Payload]


# DynamoDBv2Action

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.Payload]


# EmailConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmailConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmailContent

### subject
- **Type**: typing.Optional[str]

### additionalMessage
- **Type**: typing.Optional[str]


# EmailRecipients

### to
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetail]]


# EmailRecipientsOutput

### to
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetail]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# Event

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Optional[str]

### actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Action]]


# EventOutput

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Optional[str]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.Action]]


# FirehoseAction

### deliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### separator
- **Type**: typing.Optional[str]

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.Payload]


# GetDetectorModelAnalysisResultsRequest

### analysisId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetDetectorModelAnalysisResultsResponse

### analysisResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AnalysisResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# InitializationConfiguration

### disabledOnInitialization
- **Type**: <class 'bool'>
- **Required**: Yes


# Input

### inputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.InputConfiguration]

### inputDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionOutput]


# InputConfiguration

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### inputArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']
- **Required**: Yes

### inputDescription
- **Type**: typing.Optional[str]


# InputDefinition

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Attribute]
- **Required**: Yes


# InputDefinitionOutput

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.Attribute]
- **Required**: Yes


# InputDefinitionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputIdentifier

### iotEventsInputIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotEventsInputIdentifier]

### iotSiteWiseInputIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotSiteWiseInputIdentifier]


# InputSummary

### inputName
- **Type**: typing.Optional[str]

### inputDescription
- **Type**: typing.Optional[str]

### inputArn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']]


# IotEventsAction

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.Payload]


# IotEventsInputIdentifier

### inputName
- **Type**: <class 'str'>
- **Required**: Yes


# IotSiteWiseAction

### entryId
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### propertyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AssetPropertyValue]


# IotSiteWiseAssetModelPropertyIdentifier

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyId
- **Type**: <class 'str'>
- **Required**: Yes


# IotSiteWiseInputIdentifier

### iotSiteWiseAssetModelPropertyIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotSiteWiseAssetModelPropertyIdentifier]


# IotTopicPublishAction

### mqttTopic
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.Payload]


# LambdaAction

### functionArn
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.Payload]


# ListAlarmModelVersionsRequest

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAlarmModelVersionsResponse

### alarmModelVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AlarmModelVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAlarmModelsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAlarmModelsResponse

### alarmModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AlarmModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectorModelVersionsRequest

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDetectorModelVersionsResponse

### detectorModelVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectorModelsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDetectorModelsResponse

### detectorModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInputRoutingsRequest

### inputIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputIdentifier'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInputRoutingsResponse

### routedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.RoutedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInputsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListInputsResponse

### inputSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.InputSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingOptions

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### level
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO']
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### detectorDebugOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.DetectorDebugOption]]


# LoggingOptionsOutput

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### level
- **Type**: typing.Literal['DEBUG', 'ERROR', 'INFO']
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### detectorDebugOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.DetectorDebugOption]]


# LoggingOptionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotificationAction

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.NotificationTargetActions'>
- **Required**: Yes

### smsConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.SMSConfiguration]]

### emailConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.EmailConfiguration]]


# NotificationActionOutput

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.NotificationTargetActions'>
- **Required**: Yes

### smsConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.SMSConfigurationOutput]]

### emailConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.EmailConfigurationOutput]]


# NotificationTargetActions

### lambdaAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.LambdaAction]


# OnEnterLifecycle

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Event]]


# OnEnterLifecycleOutput

### events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.EventOutput]]


# OnExitLifecycle

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Event]]


# OnExitLifecycleOutput

### events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.EventOutput]]


# OnInputLifecycle

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Event]]

### transitionEvents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.TransitionEvent]]


# OnInputLifecycleOutput

### events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.EventOutput]]

### transitionEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.TransitionEventOutput]]


# Payload

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutLoggingOptionsRequest

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.LoggingOptionsUnion'>
- **Required**: Yes


# RecipientDetail

### ssoIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SSOIdentity]


# ResetTimerAction

### timerName
- **Type**: <class 'str'>
- **Required**: Yes


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


# RoutedResource

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# SMSConfiguration

### recipients
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetail]
- **Required**: Yes

### senderId
- **Type**: typing.Optional[str]

### additionalMessage
- **Type**: typing.Optional[str]


# SMSConfigurationOutput

### recipients
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetail]
- **Required**: Yes

### senderId
- **Type**: typing.Optional[str]

### additionalMessage
- **Type**: typing.Optional[str]


# SNSTopicPublishAction

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.Payload]


# SSOIdentity

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]


# SetTimerAction

### timerName
- **Type**: <class 'str'>
- **Required**: Yes

### seconds
- **Type**: typing.Optional[int]

### durationExpression
- **Type**: typing.Optional[str]


# SetVariableAction

### variableName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SimpleRule

### inputProperty
- **Type**: <class 'str'>
- **Required**: Yes

### comparisonOperator
- **Type**: typing.Literal['EQUAL', 'GREATER', 'GREATER_OR_EQUAL', 'LESS', 'LESS_OR_EQUAL', 'NOT_EQUAL']
- **Required**: Yes

### threshold
- **Type**: <class 'str'>
- **Required**: Yes


# SqsAction

### queueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### useBase64
- **Type**: typing.Optional[bool]

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.Payload]


# StartDetectorModelAnalysisRequest

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionUnion'>
- **Required**: Yes


# StartDetectorModelAnalysisResponse

### analysisId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# State

### stateName
- **Type**: <class 'str'>
- **Required**: Yes

### onInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnInputLifecycle]

### onEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnEnterLifecycle]

### onExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnExitLifecycle]


# StateOutput

### stateName
- **Type**: <class 'str'>
- **Required**: Yes

### onInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnInputLifecycleOutput]

### onEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnEnterLifecycleOutput]

### onExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnExitLifecycleOutput]


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Tag]
- **Required**: Yes


# TransitionEvent

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: <class 'str'>
- **Required**: Yes

### nextState
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.Action]]


# TransitionEventOutput

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: <class 'str'>
- **Required**: Yes

### nextState
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.Action]]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAlarmModelRequest

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### alarmRule
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmRule'>
- **Required**: Yes

### alarmModelDescription
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[int]

### alarmNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationUnion]

### alarmEventActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsUnion]

### alarmCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmCapabilities]


# UpdateAlarmModelResponse

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### alarmModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'FAILED', 'INACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDetectorModelRequest

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionUnion'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDescription
- **Type**: typing.Optional[str]

### evaluationMethod
- **Type**: typing.Optional[typing.Literal['BATCH', 'SERIAL']]


# UpdateDetectorModelResponse

### detectorModelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInputRequest

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### inputDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionUnion'>
- **Required**: Yes

### inputDescription
- **Type**: typing.Optional[str]


# UpdateInputResponse

### inputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadata'>
- **Required**: Yes


