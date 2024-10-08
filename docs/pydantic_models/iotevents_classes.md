# Pydantic Models in iotevents_classes

# AcknowledgeFlowTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# ActionTypeDef

### setVariable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SetVariableActionTypeDef]

### sns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SNSTopicPublishActionTypeDef]

### iotTopicPublish
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotTopicPublishActionTypeDef]

### setTimer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SetTimerActionTypeDef]

### clearTimer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.ClearTimerActionTypeDef]

### resetTimer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.ResetTimerActionTypeDef]

### iotEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotEventsActionTypeDef]

### sqs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SqsActionTypeDef]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.FirehoseActionTypeDef]

### dynamoDB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DynamoDBActionTypeDef]

### dynamoDBv2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DynamoDBv2ActionTypeDef]

### iotSiteWise
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotSiteWiseActionTypeDef]


# AlarmActionTypeDef

### sns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SNSTopicPublishActionTypeDef]

### iotTopicPublish
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotTopicPublishActionTypeDef]

### iotEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotEventsActionTypeDef]

### sqs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SqsActionTypeDef]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.FirehoseActionTypeDef]

### dynamoDB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DynamoDBActionTypeDef]

### dynamoDBv2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DynamoDBv2ActionTypeDef]

### iotSiteWise
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.IotSiteWiseActionTypeDef]


# AlarmCapabilitiesTypeDef

### initializationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.InitializationConfigurationTypeDef]

### acknowledgeFlow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AcknowledgeFlowTypeDef]


# AlarmEventActionsTypeDef

### alarmActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.AlarmActionTypeDef]]


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


# AlarmNotificationTypeDef

### notificationActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.NotificationActionTypeDef]]


# AlarmRuleTypeDef

### simpleRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.SimpleRuleTypeDef]


# AnalysisResultLocationTypeDef

### path
- **Type**: typing.Optional[str]


# AnalysisResultTypeDef

### type
- **Type**: typing.Optional[str]

### level
- **Type**: typing.Optional[typing.Literal['ERROR', 'INFO', 'WARNING']]

### message
- **Type**: typing.Optional[str]

### locations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AnalysisResultLocationTypeDef]]


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


# CreateAlarmModelRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationTypeDef]

### alarmEventActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsTypeDef]

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


# CreateDetectorModelRequestRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionTypeDef'>
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


# CreateInputRequestRequestTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### inputDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionTypeDef'>
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


# DeleteAlarmModelRequestRequestTypeDef

### alarmModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorModelRequestRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInputRequestRequestTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlarmModelRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationTypeDef'>
- **Required**: Yes

### alarmEventActions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsTypeDef'>
- **Required**: Yes

### alarmCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.AlarmCapabilitiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDetectorModelAnalysisRequestRequestTypeDef

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


# DescribeDetectorModelRequestRequestTypeDef

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


# DescribeInputRequestRequestTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInputResponseTypeDef

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoggingOptionsResponseTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.LoggingOptionsTypeDef'>
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


# DetectorModelDefinitionTypeDef

### states
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.StateTypeDef]
- **Required**: Yes

### initialStateName
- **Type**: <class 'str'>
- **Required**: Yes


# DetectorModelSummaryTypeDef

### detectorModelName
- **Type**: typing.Optional[str]

### detectorModelDescription
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]


# DetectorModelTypeDef

### detectorModelDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionTypeDef]

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


# EmailConfigurationTypeDef

### recipients
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.EmailRecipientsTypeDef'>
- **Required**: Yes

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.EmailContentTypeDef]


# EmailContentTypeDef

### subject
- **Type**: typing.Optional[str]

### additionalMessage
- **Type**: typing.Optional[str]


# EmailRecipientsTypeDef

### to
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.RecipientDetailTypeDef]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# GetDetectorModelAnalysisResultsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# InputDefinitionTypeDef

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.AttributeTypeDef]
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionTypeDef]


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


# ListAlarmModelVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAlarmModelsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAlarmModelsResponseTypeDef

### alarmModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.AlarmModelSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDetectorModelVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDetectorModelsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDetectorModelsResponseTypeDef

### detectorModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInputRoutingsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInputsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListInputsResponseTypeDef

### inputSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotevents_classes.InputSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotevents_classes.DetectorDebugOptionTypeDef]]


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


# OnEnterLifecycleTypeDef

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.EventTypeDef]]


# OnExitLifecycleTypeDef

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.EventTypeDef]]


# OnInputLifecycleTypeDef

### events
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.EventTypeDef]]

### transitionEvents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotevents_classes.TransitionEventTypeDef]]


# PayloadTypeDef

### contentExpression
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['JSON', 'STRING']
- **Required**: Yes


# PutLoggingOptionsRequestRequestTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.LoggingOptionsTypeDef'>
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

### HostId
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


# RoutedResourceTypeDef

### name
- **Type**: typing.Optional[str]

### arn
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


# StartDetectorModelAnalysisRequestRequestTypeDef

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionTypeDef'>
- **Required**: Yes


# StartDetectorModelAnalysisResponseTypeDef

### analysisId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAlarmModelRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmNotificationTypeDef]

### alarmEventActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotevents_classes.AlarmEventActionsTypeDef]

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


# UpdateDetectorModelRequestRequestTypeDef

### detectorModelName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorModelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.DetectorModelDefinitionTypeDef'>
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


# UpdateInputRequestRequestTypeDef

### inputName
- **Type**: <class 'str'>
- **Required**: Yes

### inputDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotevents_classes.InputDefinitionTypeDef'>
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


