# Iotevents Classes

# AcknowledgeFlowTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ActionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmActionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmCapabilitiesTypeDef

### initializationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.InitializationConfigurationTypeDef]

### acknowledgeFlow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AcknowledgeFlowTypeDef]


# AlarmEventActionsOutputTypeDef

### alarmActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AlarmActionTypeDef]]


# AlarmEventActionsTypeDef

### alarmActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.AlarmActionTypeDef]]


# AlarmEventActionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmModelSummaryTypeDef

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### alarmModelDescription
- **Type**: typing.Optional[str]

### alarmModelName
- **Type**: typing.Optional[str]


# AlarmModelVersionSummaryTypeDef

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


# AlarmNotificationOutputTypeDef

### notificationActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.NotificationActionOutputTypeDef]]


# AlarmNotificationTypeDef

### notificationActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.NotificationActionTypeDef]]


# AlarmNotificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmRuleTypeDef

### simpleRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SimpleRuleTypeDef]


# AnalysisResultLocationTypeDef

### path
- **Type**: typing.Optional[str]


# AnalysisResultTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetPropertyTimestampTypeDef

### timeInSeconds
- **Type**: <class 'str'>
- **Required**: Yes

### offsetInNanos
- **Type**: typing.Optional[str]


# AssetPropertyValueTypeDef

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AssetPropertyVariantTypeDef]

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AssetPropertyTimestampTypeDef]

### quality
- **Type**: typing.Optional[str]


# AssetPropertyVariantTypeDef

### stringValue
- **Type**: typing.Optional[str]

### integerValue
- **Type**: typing.Optional[str]

### doubleValue
- **Type**: typing.Optional[str]

### booleanValue
- **Type**: typing.Optional[str]


# AttributeTypeDef

### jsonPath
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClearTimerActionTypeDef

### timerName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAlarmModelRequestTypeDef

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### alarmRule
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmRuleTypeDef'>
- **Required**: Yes

### alarmModelDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.TagTypeDef]]

### key
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[int]

### alarmNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationUnionTypeDef]

### alarmEventActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsUnionTypeDef]

### alarmCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmCapabilitiesTypeDef]


# CreateAlarmModelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDetectorModelRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionUnionTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDescription
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.TagTypeDef]]

### evaluationMethod
- **Type**: typing.Optional[typing.Literal['BATCH', 'SERIAL']]


# CreateDetectorModelResponseTypeDef

### detectorModelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInputRequestTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### inputDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionUnionTypeDef'>
- **Required**: Yes

### inputDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.TagTypeDef]]


# CreateInputResponseTypeDef

### inputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAlarmModelRequestTypeDef

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorModelRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputRequestTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlarmModelRequestTypeDef

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### alarmModelVersion
- **Type**: typing.Optional[str]


# DescribeAlarmModelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmRuleTypeDef'>
- **Required**: Yes

### alarmNotification
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationOutputTypeDef'>
- **Required**: Yes

### alarmEventActions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsOutputTypeDef'>
- **Required**: Yes

### alarmCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmCapabilitiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDetectorModelAnalysisRequestTypeDef

### analysisId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDetectorModelAnalysisResponseTypeDef

### status
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'RUNNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDetectorModelRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelVersion
- **Type**: typing.Optional[str]


# DescribeDetectorModelResponseTypeDef

### detectorModel
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInputRequestTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoggingOptionsResponseTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.LoggingOptionsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectorDebugOptionTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### keyValue
- **Type**: typing.Optional[str]


# DetectorModelConfigurationTypeDef

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


# DetectorModelDefinitionOutputTypeDef

### states
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.StateOutputTypeDef]
- **Required**: Yes

### initialStateName
- **Type**: <class 'str'>
- **Required**: Yes


# DetectorModelDefinitionTypeDef

### states
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.StateTypeDef]
- **Required**: Yes

### initialStateName
- **Type**: <class 'str'>
- **Required**: Yes


# DetectorModelDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DetectorModelSummaryTypeDef

### detectorModelName
- **Type**: typing.Optional[str]

### detectorModelDescription
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]


# DetectorModelTypeDef

### detectorModelDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionOutputTypeDef]

### detectorModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelConfigurationTypeDef]


# DetectorModelVersionSummaryTypeDef

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


# DynamoDBActionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.PayloadTypeDef]


# DynamoDBv2ActionTypeDef

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.PayloadTypeDef]


# EmailConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmailConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmailContentTypeDef

### subject
- **Type**: typing.Optional[str]

### additionalMessage
- **Type**: typing.Optional[str]


# EmailRecipientsOutputTypeDef

### to
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetailTypeDef]]


# EmailRecipientsTypeDef

### to
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetailTypeDef]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventOutputTypeDef

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Optional[str]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.ActionTypeDef]]


# EventTypeDef

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Optional[str]

### actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.ActionTypeDef]]


# FirehoseActionTypeDef

### deliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### separator
- **Type**: typing.Optional[str]

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.PayloadTypeDef]


# GetDetectorModelAnalysisResultsRequestTypeDef

### analysisId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetDetectorModelAnalysisResultsResponseTypeDef

### analysisResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AnalysisResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# InitializationConfigurationTypeDef

### disabledOnInitialization
- **Type**: <class 'bool'>
- **Required**: Yes


# InputConfigurationTypeDef

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


# InputDefinitionOutputTypeDef

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AttributeTypeDef]
- **Required**: Yes


# InputDefinitionTypeDef

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.AttributeTypeDef]
- **Required**: Yes


# InputDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputIdentifierTypeDef

### iotEventsInputIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotEventsInputIdentifierTypeDef]

### iotSiteWiseInputIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotSiteWiseInputIdentifierTypeDef]


# InputSummaryTypeDef

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


# InputTypeDef

### inputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.InputConfigurationTypeDef]

### inputDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionOutputTypeDef]


# IotEventsActionTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.PayloadTypeDef]


# IotEventsInputIdentifierTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes


# IotSiteWiseActionTypeDef

### entryId
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### propertyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AssetPropertyValueTypeDef]


# IotSiteWiseAssetModelPropertyIdentifierTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyId
- **Type**: <class 'str'>
- **Required**: Yes


# IotSiteWiseInputIdentifierTypeDef

### iotSiteWiseAssetModelPropertyIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotSiteWiseAssetModelPropertyIdentifierTypeDef]


# IotTopicPublishActionTypeDef

### mqttTopic
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.PayloadTypeDef]


# LambdaActionTypeDef

### functionArn
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.PayloadTypeDef]


# ListAlarmModelVersionsRequestTypeDef

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAlarmModelVersionsResponseTypeDef

### alarmModelVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AlarmModelVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAlarmModelsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAlarmModelsResponseTypeDef

### alarmModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AlarmModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectorModelVersionsRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDetectorModelVersionsResponseTypeDef

### detectorModelVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDetectorModelsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDetectorModelsResponseTypeDef

### detectorModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInputRoutingsRequestTypeDef

### inputIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputIdentifierTypeDef'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInputRoutingsResponseTypeDef

### routedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.RoutedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInputsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListInputsResponseTypeDef

### inputSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.InputSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingOptionsOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.DetectorDebugOptionTypeDef]]


# LoggingOptionsTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.DetectorDebugOptionTypeDef]]


# LoggingOptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotificationActionOutputTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.NotificationTargetActionsTypeDef'>
- **Required**: Yes

### smsConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.SMSConfigurationOutputTypeDef]]

### emailConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.EmailConfigurationOutputTypeDef]]


# NotificationActionTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.NotificationTargetActionsTypeDef'>
- **Required**: Yes

### smsConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.SMSConfigurationTypeDef]]

### emailConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.EmailConfigurationTypeDef]]


# NotificationTargetActionsTypeDef

### lambdaAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.LambdaActionTypeDef]


# OnEnterLifecycleOutputTypeDef

### events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.EventOutputTypeDef]]


# OnEnterLifecycleTypeDef

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.EventTypeDef]]


# OnExitLifecycleOutputTypeDef

### events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.EventOutputTypeDef]]


# OnExitLifecycleTypeDef

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.EventTypeDef]]


# OnInputLifecycleOutputTypeDef

### events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.EventOutputTypeDef]]

### transitionEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.TransitionEventOutputTypeDef]]


# OnInputLifecycleTypeDef

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.EventTypeDef]]

### transitionEvents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.TransitionEventTypeDef]]


# PayloadTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutLoggingOptionsRequestTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.LoggingOptionsUnionTypeDef'>
- **Required**: Yes


# RecipientDetailTypeDef

### ssoIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SSOIdentityTypeDef]


# ResetTimerActionTypeDef

### timerName
- **Type**: <class 'str'>
- **Required**: Yes


# ResponseMetadataTypeDef

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


# RoutedResourceTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# SMSConfigurationOutputTypeDef

### recipients
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetailTypeDef]
- **Required**: Yes

### senderId
- **Type**: typing.Optional[str]

### additionalMessage
- **Type**: typing.Optional[str]


# SMSConfigurationTypeDef

### recipients
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetailTypeDef]
- **Required**: Yes

### senderId
- **Type**: typing.Optional[str]

### additionalMessage
- **Type**: typing.Optional[str]


# SNSTopicPublishActionTypeDef

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.PayloadTypeDef]


# SSOIdentityTypeDef

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: typing.Optional[str]


# SetTimerActionTypeDef

### timerName
- **Type**: <class 'str'>
- **Required**: Yes

### seconds
- **Type**: typing.Optional[int]

### durationExpression
- **Type**: typing.Optional[str]


# SetVariableActionTypeDef

### variableName
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SimpleRuleTypeDef

### inputProperty
- **Type**: <class 'str'>
- **Required**: Yes

### comparisonOperator
- **Type**: typing.Literal['EQUAL', 'GREATER', 'GREATER_OR_EQUAL', 'LESS', 'LESS_OR_EQUAL', 'NOT_EQUAL']
- **Required**: Yes

### threshold
- **Type**: <class 'str'>
- **Required**: Yes


# SqsActionTypeDef

### queueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### useBase64
- **Type**: typing.Optional[bool]

### payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.PayloadTypeDef]


# StartDetectorModelAnalysisRequestTypeDef

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionUnionTypeDef'>
- **Required**: Yes


# StartDetectorModelAnalysisResponseTypeDef

### analysisId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StateOutputTypeDef

### stateName
- **Type**: <class 'str'>
- **Required**: Yes

### onInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnInputLifecycleOutputTypeDef]

### onEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnEnterLifecycleOutputTypeDef]

### onExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnExitLifecycleOutputTypeDef]


# StateTypeDef

### stateName
- **Type**: <class 'str'>
- **Required**: Yes

### onInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnInputLifecycleTypeDef]

### onEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnEnterLifecycleTypeDef]

### onExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.OnExitLifecycleTypeDef]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TransitionEventOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.ActionTypeDef]]


# TransitionEventTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.ActionTypeDef]]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAlarmModelRequestTypeDef

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### alarmRule
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmRuleTypeDef'>
- **Required**: Yes

### alarmModelDescription
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[int]

### alarmNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationUnionTypeDef]

### alarmEventActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsUnionTypeDef]

### alarmCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmCapabilitiesTypeDef]


# UpdateAlarmModelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDetectorModelRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionUnionTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDescription
- **Type**: typing.Optional[str]

### evaluationMethod
- **Type**: typing.Optional[typing.Literal['BATCH', 'SERIAL']]


# UpdateDetectorModelResponseTypeDef

### detectorModelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInputRequestTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### inputDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionUnionTypeDef'>
- **Required**: Yes

### inputDescription
- **Type**: typing.Optional[str]


# UpdateInputResponseTypeDef

### inputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


