# inspector_classes

# AddAttributesToFindingsRequestRequestTypeDef

### findingArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]
- **Required**: Yes


# AddAttributesToFindingsResponseTypeDef

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AgentFilterTypeDef

### agentHealths
- **Type**: typing.Sequence[typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]
- **Required**: Yes

### agentHealthCodes
- **Type**: typing.Sequence[typing.Literal['IDLE', 'RUNNING', 'SHUTDOWN', 'THROTTLED', 'UNHEALTHY', 'UNKNOWN']]
- **Required**: Yes


# AgentPreviewTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### hostname
- **Type**: typing.Optional[str]

### autoScalingGroup
- **Type**: typing.Optional[str]

### agentHealth
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]

### agentVersion
- **Type**: typing.Optional[str]

### operatingSystem
- **Type**: typing.Optional[str]

### kernelVersion
- **Type**: typing.Optional[str]

### ipv4Address
- **Type**: typing.Optional[str]


# AssessmentRunAgentTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### agentHealth
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']
- **Required**: Yes

### agentHealthCode
- **Type**: typing.Literal['IDLE', 'RUNNING', 'SHUTDOWN', 'THROTTLED', 'UNHEALTHY', 'UNKNOWN']
- **Required**: Yes

### telemetryMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.TelemetryMetadataTypeDef]
- **Required**: Yes

### agentHealthDetails
- **Type**: typing.Optional[str]

### autoScalingGroup
- **Type**: typing.Optional[str]


# AssessmentRunFilterTypeDef

### namePattern
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELED', 'COLLECTING_DATA', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'CREATED', 'DATA_COLLECTED', 'ERROR', 'EVALUATING_RULES', 'FAILED', 'START_DATA_COLLECTION_IN_PROGRESS', 'START_DATA_COLLECTION_PENDING', 'START_EVALUATING_RULES_PENDING', 'STOP_DATA_COLLECTION_PENDING']]]

### durationRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.DurationRangeTypeDef]

### rulesPackageArns
- **Type**: typing.Optional[typing.Sequence[str]]

### startTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.TimestampRangeTypeDef]

### completionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.TimestampRangeTypeDef]

### stateChangeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.TimestampRangeTypeDef]


# AssessmentRunNotificationTypeDef

### date
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### event
- **Type**: typing.Literal['ASSESSMENT_RUN_COMPLETED', 'ASSESSMENT_RUN_STARTED', 'ASSESSMENT_RUN_STATE_CHANGED', 'FINDING_REPORTED', 'OTHER']
- **Required**: Yes

### error
- **Type**: <class 'bool'>
- **Required**: Yes

### message
- **Type**: typing.Optional[str]

### snsTopicArn
- **Type**: typing.Optional[str]

### snsPublishStatusCode
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'INTERNAL_ERROR', 'SUCCESS', 'TOPIC_DOES_NOT_EXIST']]


# AssessmentRunStateChangeTypeDef

### stateChangedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CANCELED', 'COLLECTING_DATA', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'CREATED', 'DATA_COLLECTED', 'ERROR', 'EVALUATING_RULES', 'FAILED', 'START_DATA_COLLECTION_IN_PROGRESS', 'START_DATA_COLLECTION_PENDING', 'START_EVALUATING_RULES_PENDING', 'STOP_DATA_COLLECTION_PENDING']
- **Required**: Yes


# AssessmentRunTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CANCELED', 'COLLECTING_DATA', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'CREATED', 'DATA_COLLECTED', 'ERROR', 'EVALUATING_RULES', 'FAILED', 'START_DATA_COLLECTION_IN_PROGRESS', 'START_DATA_COLLECTION_PENDING', 'START_EVALUATING_RULES_PENDING', 'STOP_DATA_COLLECTION_PENDING']
- **Required**: Yes

### durationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### rulesPackageArns
- **Type**: typing.List[str]
- **Required**: Yes

### userAttributesForFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stateChangedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataCollected
- **Type**: <class 'bool'>
- **Required**: Yes

### stateChanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AssessmentRunStateChangeTypeDef]
- **Required**: Yes

### notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AssessmentRunNotificationTypeDef]
- **Required**: Yes

### findingCounts
- **Type**: typing.Dict[typing.Literal['High', 'Informational', 'Low', 'Medium', 'Undefined'], int]
- **Required**: Yes

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### completedAt
- **Type**: typing.Optional[datetime.datetime]


# AssessmentTargetFilterTypeDef

### assessmentTargetNamePattern
- **Type**: typing.Optional[str]


# AssessmentTargetTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### resourceGroupArn
- **Type**: typing.Optional[str]


# AssessmentTemplateFilterTypeDef

### namePattern
- **Type**: typing.Optional[str]

### durationRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.DurationRangeTypeDef]

### rulesPackageArns
- **Type**: typing.Optional[typing.Sequence[str]]


# AssessmentTemplateTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### durationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### rulesPackageArns
- **Type**: typing.List[str]
- **Required**: Yes

### userAttributesForFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]
- **Required**: Yes

### assessmentRunCount
- **Type**: <class 'int'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastAssessmentRunArn
- **Type**: typing.Optional[str]


# AssetAttributesTypeDef

### schemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### agentId
- **Type**: typing.Optional[str]

### autoScalingGroup
- **Type**: typing.Optional[str]

### amiId
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]

### ipv4Addresses
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector_classes.TagTypeDef]]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector_classes.NetworkInterfaceTypeDef]]


# AttributeTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAssessmentTargetRequestRequestTypeDef

### assessmentTargetName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceGroupArn
- **Type**: typing.Optional[str]


# CreateAssessmentTargetResponseTypeDef

### assessmentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssessmentTemplateRequestRequestTypeDef

### assessmentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### durationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### rulesPackageArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### userAttributesForFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]]


# CreateAssessmentTemplateResponseTypeDef

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExclusionsPreviewRequestRequestTypeDef

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateExclusionsPreviewResponseTypeDef

### previewToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceGroupRequestRequestTypeDef

### resourceGroupTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.inspector_classes.ResourceGroupTagTypeDef]
- **Required**: Yes


# CreateResourceGroupResponseTypeDef

### resourceGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAssessmentRunRequestRequestTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssessmentTargetRequestRequestTypeDef

### assessmentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssessmentTemplateRequestRequestTypeDef

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssessmentRunsRequestRequestTypeDef

### assessmentRunArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeAssessmentRunsResponseTypeDef

### assessmentRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AssessmentRunTypeDef]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssessmentTargetsRequestRequestTypeDef

### assessmentTargetArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeAssessmentTargetsResponseTypeDef

### assessmentTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AssessmentTargetTypeDef]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssessmentTemplatesRequestRequestTypeDef

### assessmentTemplateArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeAssessmentTemplatesResponseTypeDef

### assessmentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AssessmentTemplateTypeDef]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCrossAccountAccessRoleResponseTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### valid
- **Type**: <class 'bool'>
- **Required**: Yes

### registeredAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExclusionsRequestRequestTypeDef

### exclusionArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['EN_US']]


# DescribeExclusionsResponseTypeDef

### exclusions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.ExclusionTypeDef]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFindingsRequestRequestTypeDef

### findingArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['EN_US']]


# DescribeFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.FindingTypeDef]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourceGroupsRequestRequestTypeDef

### resourceGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeResourceGroupsResponseTypeDef

### resourceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.ResourceGroupTypeDef]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRulesPackagesRequestRequestTypeDef

### rulesPackageArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['EN_US']]


# DescribeRulesPackagesResponseTypeDef

### rulesPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.RulesPackageTypeDef]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DurationRangeTypeDef

### minSeconds
- **Type**: typing.Optional[int]

### maxSeconds
- **Type**: typing.Optional[int]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventSubscriptionTypeDef

### event
- **Type**: typing.Literal['ASSESSMENT_RUN_COMPLETED', 'ASSESSMENT_RUN_STARTED', 'ASSESSMENT_RUN_STATE_CHANGED', 'FINDING_REPORTED', 'OTHER']
- **Required**: Yes

### subscribedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ExclusionPreviewTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### recommendation
- **Type**: <class 'str'>
- **Required**: Yes

### scopes
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.ScopeTypeDef]
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]]


# ExclusionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### recommendation
- **Type**: <class 'str'>
- **Required**: Yes

### scopes
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.ScopeTypeDef]
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]]


# FailedItemDetailsTypeDef

### failureCode
- **Type**: typing.Literal['ACCESS_DENIED', 'DUPLICATE_ARN', 'INTERNAL_ERROR', 'INVALID_ARN', 'ITEM_DOES_NOT_EXIST', 'LIMIT_EXCEEDED']
- **Required**: Yes

### retryable
- **Type**: <class 'bool'>
- **Required**: Yes


# FindingFilterTypeDef

### agentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### autoScalingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### ruleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### severities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['High', 'Informational', 'Low', 'Medium', 'Undefined']]]

### rulesPackageArns
- **Type**: typing.Optional[typing.Sequence[str]]

### attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]]

### userAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]]

### creationTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.TimestampRangeTypeDef]


# FindingTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]
- **Required**: Yes

### userAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AttributeTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### schemaVersion
- **Type**: typing.Optional[int]

### service
- **Type**: typing.Optional[str]

### serviceAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.InspectorServiceAttributesTypeDef]

### assetType
- **Type**: typing.Optional[typing.Literal['ec2-instance']]

### assetAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AssetAttributesTypeDef]

### id
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### recommendation
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[typing.Literal['High', 'Informational', 'Low', 'Medium', 'Undefined']]

### numericSeverity
- **Type**: typing.Optional[float]

### confidence
- **Type**: typing.Optional[int]

### indicatorOfCompromise
- **Type**: typing.Optional[bool]


# GetAssessmentReportRequestRequestTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### reportFileFormat
- **Type**: typing.Literal['HTML', 'PDF']
- **Required**: Yes

### reportType
- **Type**: typing.Literal['FINDING', 'FULL']
- **Required**: Yes


# GetAssessmentReportResponseTypeDef

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'WORK_IN_PROGRESS']
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExclusionsPreviewRequestRequestTypeDef

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### previewToken
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### locale
- **Type**: typing.Optional[typing.Literal['EN_US']]


# GetExclusionsPreviewResponseTypeDef

### previewStatus
- **Type**: typing.Literal['COMPLETED', 'WORK_IN_PROGRESS']
- **Required**: Yes

### exclusionPreviews
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.ExclusionPreviewTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTelemetryMetadataRequestRequestTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTelemetryMetadataResponseTypeDef

### telemetryMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.TelemetryMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InspectorServiceAttributesTypeDef

### schemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### assessmentRunArn
- **Type**: typing.Optional[str]

### rulesPackageArn
- **Type**: typing.Optional[str]


# ListAssessmentRunAgentsRequestListAssessmentRunAgentsPaginateTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AgentFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# ListAssessmentRunAgentsRequestRequestTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AgentFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentRunAgentsResponseTypeDef

### assessmentRunAgents
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AssessmentRunAgentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssessmentRunsRequestListAssessmentRunsPaginateTypeDef

### assessmentTemplateArns
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AssessmentRunFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# ListAssessmentRunsRequestRequestTypeDef

### assessmentTemplateArns
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AssessmentRunFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentRunsResponseTypeDef

### assessmentRunArns
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssessmentTargetsRequestListAssessmentTargetsPaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AssessmentTargetFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# ListAssessmentTargetsRequestRequestTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AssessmentTargetFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentTargetsResponseTypeDef

### assessmentTargetArns
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssessmentTemplatesRequestListAssessmentTemplatesPaginateTypeDef

### assessmentTargetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AssessmentTemplateFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# ListAssessmentTemplatesRequestRequestTypeDef

### assessmentTargetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.AssessmentTemplateFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentTemplatesResponseTypeDef

### assessmentTemplateArns
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEventSubscriptionsRequestListEventSubscriptionsPaginateTypeDef

### resourceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# ListEventSubscriptionsRequestRequestTypeDef

### resourceArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEventSubscriptionsResponseTypeDef

### subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.SubscriptionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExclusionsRequestListExclusionsPaginateTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# ListExclusionsRequestRequestTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListExclusionsResponseTypeDef

### exclusionArns
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingsRequestListFindingsPaginateTypeDef

### assessmentRunArns
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.FindingFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# ListFindingsRequestRequestTypeDef

### assessmentRunArns
- **Type**: typing.Optional[typing.Sequence[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.FindingFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFindingsResponseTypeDef

### findingArns
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRulesPackagesRequestListRulesPackagesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# ListRulesPackagesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRulesPackagesResponseTypeDef

### rulesPackageArns
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NetworkInterfaceTypeDef

### networkInterfaceId
- **Type**: typing.Optional[str]

### subnetId
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]

### privateDnsName
- **Type**: typing.Optional[str]

### privateIpAddress
- **Type**: typing.Optional[str]

### privateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector_classes.PrivateIpTypeDef]]

### publicDnsName
- **Type**: typing.Optional[str]

### publicIp
- **Type**: typing.Optional[str]

### ipv6Addresses
- **Type**: typing.Optional[typing.List[str]]

### securityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector_classes.SecurityGroupTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PreviewAgentsRequestPreviewAgentsPaginateTypeDef

### previewAgentsArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector_classes.PaginatorConfigTypeDef]


# PreviewAgentsRequestRequestTypeDef

### previewAgentsArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# PreviewAgentsResponseTypeDef

### agentPreviews
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.AgentPreviewTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PrivateIpTypeDef

### privateDnsName
- **Type**: typing.Optional[str]

### privateIpAddress
- **Type**: typing.Optional[str]


# RegisterCrossAccountAccessRoleRequestRequestTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveAttributesFromFindingsRequestRequestTypeDef

### findingArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### attributeKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveAttributesFromFindingsResponseTypeDef

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector_classes.FailedItemDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceGroupTagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# ResourceGroupTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.ResourceGroupTagTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
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


# RulesPackageTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ScopeTypeDef

### key
- **Type**: typing.Optional[typing.Literal['INSTANCE_ID', 'RULES_PACKAGE_ARN']]

### value
- **Type**: typing.Optional[str]


# SecurityGroupTypeDef

### groupName
- **Type**: typing.Optional[str]

### groupId
- **Type**: typing.Optional[str]


# SetTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.inspector_classes.TagTypeDef]]


# StartAssessmentRunRequestRequestTypeDef

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentRunName
- **Type**: typing.Optional[str]


# StartAssessmentRunResponseTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopAssessmentRunRequestRequestTypeDef

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### stopAction
- **Type**: typing.Optional[typing.Literal['SKIP_EVALUATION', 'START_EVALUATION']]


# SubscribeToEventRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### event
- **Type**: typing.Literal['ASSESSMENT_RUN_COMPLETED', 'ASSESSMENT_RUN_STARTED', 'ASSESSMENT_RUN_STATE_CHANGED', 'FINDING_REPORTED', 'OTHER']
- **Required**: Yes

### topicArn
- **Type**: <class 'str'>
- **Required**: Yes


# SubscriptionTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### topicArn
- **Type**: <class 'str'>
- **Required**: Yes

### eventSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector_classes.EventSubscriptionTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# TelemetryMetadataTypeDef

### messageType
- **Type**: <class 'str'>
- **Required**: Yes

### count
- **Type**: <class 'int'>
- **Required**: Yes

### dataSize
- **Type**: typing.Optional[int]


# TimestampRangeTypeDef

### beginDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UnsubscribeFromEventRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### event
- **Type**: typing.Literal['ASSESSMENT_RUN_COMPLETED', 'ASSESSMENT_RUN_STARTED', 'ASSESSMENT_RUN_STATE_CHANGED', 'FINDING_REPORTED', 'OTHER']
- **Required**: Yes

### topicArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAssessmentTargetRequestRequestTypeDef

### assessmentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentTargetName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceGroupArn
- **Type**: typing.Optional[str]


