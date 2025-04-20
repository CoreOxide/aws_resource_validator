# Inspector Inspector Classes

# AddAttributesToFindingsRequest

### findingArns
- **Type**: typing.List[str]
- **Required**: Yes

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]
- **Required**: Yes


# AddAttributesToFindingsResponse

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# AgentFilter

### agentHealths
- **Type**: typing.List[typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]
- **Required**: Yes

### agentHealthCodes
- **Type**: typing.List[typing.Literal['IDLE', 'RUNNING', 'SHUTDOWN', 'THROTTLED', 'UNHEALTHY', 'UNKNOWN']]
- **Required**: Yes


# AgentPreview

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


# AssessmentRun

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentRunStateChange]
- **Required**: Yes

### notifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentRunNotification]
- **Required**: Yes

### findingCounts
- **Type**: typing.Dict[typing.Literal['High', 'Informational', 'Low', 'Medium', 'Undefined'], int]
- **Required**: Yes

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### completedAt
- **Type**: typing.Optional[datetime.datetime]


# AssessmentRunAgent

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.TelemetryMetadata]
- **Required**: Yes

### agentHealthDetails
- **Type**: typing.Optional[str]

### autoScalingGroup
- **Type**: typing.Optional[str]


# AssessmentRunFilter

### namePattern
- **Type**: typing.Optional[str]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELED', 'COLLECTING_DATA', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'CREATED', 'DATA_COLLECTED', 'ERROR', 'EVALUATING_RULES', 'FAILED', 'START_DATA_COLLECTION_IN_PROGRESS', 'START_DATA_COLLECTION_PENDING', 'START_EVALUATING_RULES_PENDING', 'STOP_DATA_COLLECTION_PENDING']]]

### durationRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.DurationRange]

### rulesPackageArns
- **Type**: typing.Optional[typing.List[str]]

### startTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.TimestampRange]

### completionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.TimestampRange]

### stateChangeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.TimestampRange]


# AssessmentRunNotification

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


# AssessmentRunStateChange

### stateChangedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CANCELED', 'COLLECTING_DATA', 'COMPLETED', 'COMPLETED_WITH_ERRORS', 'CREATED', 'DATA_COLLECTED', 'ERROR', 'EVALUATING_RULES', 'FAILED', 'START_DATA_COLLECTION_IN_PROGRESS', 'START_DATA_COLLECTION_PENDING', 'START_EVALUATING_RULES_PENDING', 'STOP_DATA_COLLECTION_PENDING']
- **Required**: Yes


# AssessmentTarget

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


# AssessmentTargetFilter

### assessmentTargetNamePattern
- **Type**: typing.Optional[str]


# AssessmentTemplate

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]
- **Required**: Yes

### assessmentRunCount
- **Type**: <class 'int'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastAssessmentRunArn
- **Type**: typing.Optional[str]


# AssessmentTemplateFilter

### namePattern
- **Type**: typing.Optional[str]

### durationRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.DurationRange]

### rulesPackageArns
- **Type**: typing.Optional[typing.List[str]]


# AssetAttributes

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Tag]]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.NetworkInterface]]


# Attribute

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAssessmentTargetRequest

### assessmentTargetName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceGroupArn
- **Type**: typing.Optional[str]


# CreateAssessmentTargetResponse

### assessmentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssessmentTemplateRequest

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
- **Type**: typing.List[str]
- **Required**: Yes

### userAttributesForFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]]


# CreateAssessmentTemplateResponse

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExclusionsPreviewRequest

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateExclusionsPreviewResponse

### previewToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceGroupRequest

### resourceGroupTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.ResourceGroupTag]
- **Required**: Yes


# CreateResourceGroupResponse

### resourceGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAssessmentRunRequest

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssessmentTargetRequest

### assessmentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssessmentTemplateRequest

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssessmentRunsRequest

### assessmentRunArns
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeAssessmentRunsResponse

### assessmentRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentRun]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssessmentTargetsRequest

### assessmentTargetArns
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeAssessmentTargetsResponse

### assessmentTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentTarget]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssessmentTemplatesRequest

### assessmentTemplateArns
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeAssessmentTemplatesResponse

### assessmentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentTemplate]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCrossAccountAccessRoleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExclusionsRequest

### exclusionArns
- **Type**: typing.List[str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['EN_US']]


# DescribeExclusionsResponse

### exclusions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.Exclusion]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFindingsRequest

### findingArns
- **Type**: typing.List[str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['EN_US']]


# DescribeFindingsResponse

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Finding]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourceGroupsRequest

### resourceGroupArns
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeResourceGroupsResponse

### resourceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.ResourceGroup]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRulesPackagesRequest

### rulesPackageArns
- **Type**: typing.List[str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['EN_US']]


# DescribeRulesPackagesResponse

### rulesPackages
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.RulesPackage]
- **Required**: Yes

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# DurationRange

### minSeconds
- **Type**: typing.Optional[int]

### maxSeconds
- **Type**: typing.Optional[int]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# EventSubscription

### event
- **Type**: typing.Literal['ASSESSMENT_RUN_COMPLETED', 'ASSESSMENT_RUN_STARTED', 'ASSESSMENT_RUN_STATE_CHANGED', 'FINDING_REPORTED', 'OTHER']
- **Required**: Yes

### subscribedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# Exclusion

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Scope]
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]]


# ExclusionPreview

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Scope]
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]]


# FailedItemDetails

### failureCode
- **Type**: typing.Literal['ACCESS_DENIED', 'DUPLICATE_ARN', 'INTERNAL_ERROR', 'INVALID_ARN', 'ITEM_DOES_NOT_EXIST', 'LIMIT_EXCEEDED']
- **Required**: Yes

### retryable
- **Type**: <class 'bool'>
- **Required**: Yes


# Finding

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]
- **Required**: Yes

### userAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.InspectorServiceAttributes]

### assetType
- **Type**: typing.Optional[typing.Literal['ec2-instance']]

### assetAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssetAttributes]

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


# FindingFilter

### agentIds
- **Type**: typing.Optional[typing.List[str]]

### autoScalingGroups
- **Type**: typing.Optional[typing.List[str]]

### ruleNames
- **Type**: typing.Optional[typing.List[str]]

### severities
- **Type**: typing.Optional[typing.List[typing.Literal['High', 'Informational', 'Low', 'Medium', 'Undefined']]]

### rulesPackageArns
- **Type**: typing.Optional[typing.List[str]]

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]]

### userAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Attribute]]

### creationTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.TimestampRange]


# GetAssessmentReportRequest

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### reportFileFormat
- **Type**: typing.Literal['HTML', 'PDF']
- **Required**: Yes

### reportType
- **Type**: typing.Literal['FINDING', 'FULL']
- **Required**: Yes


# GetAssessmentReportResponse

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'WORK_IN_PROGRESS']
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# GetExclusionsPreviewRequest

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


# GetExclusionsPreviewResponse

### previewStatus
- **Type**: typing.Literal['COMPLETED', 'WORK_IN_PROGRESS']
- **Required**: Yes

### exclusionPreviews
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.ExclusionPreview]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetTelemetryMetadataRequest

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTelemetryMetadataResponse

### telemetryMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.TelemetryMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# InspectorServiceAttributes

### schemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### assessmentRunArn
- **Type**: typing.Optional[str]

### rulesPackageArn
- **Type**: typing.Optional[str]


# ListAssessmentRunAgentsRequest

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AgentFilter]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentRunAgentsRequestPaginate

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AgentFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# ListAssessmentRunAgentsResponse

### assessmentRunAgents
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentRunAgent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssessmentRunsRequest

### assessmentTemplateArns
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentRunFilter]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentRunsRequestPaginate

### assessmentTemplateArns
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentRunFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# ListAssessmentRunsResponse

### assessmentRunArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssessmentTargetsRequest

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentTargetFilter]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentTargetsRequestPaginate

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentTargetFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# ListAssessmentTargetsResponse

### assessmentTargetArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssessmentTemplatesRequest

### assessmentTargetArns
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentTemplateFilter]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssessmentTemplatesRequestPaginate

### assessmentTargetArns
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.AssessmentTemplateFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# ListAssessmentTemplatesResponse

### assessmentTemplateArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEventSubscriptionsRequest

### resourceArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEventSubscriptionsRequestPaginate

### resourceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# ListEventSubscriptionsResponse

### subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Subscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExclusionsRequest

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListExclusionsRequestPaginate

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# ListExclusionsResponse

### exclusionArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsRequest

### assessmentRunArns
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.FindingFilter]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFindingsRequestPaginate

### assessmentRunArns
- **Type**: typing.Optional[typing.List[str]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.FindingFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# ListFindingsResponse

### findingArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRulesPackagesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRulesPackagesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# ListRulesPackagesResponse

### rulesPackageArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# NetworkInterface

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.PrivateIp]]

### publicDnsName
- **Type**: typing.Optional[str]

### publicIp
- **Type**: typing.Optional[str]

### ipv6Addresses
- **Type**: typing.Optional[typing.List[str]]

### securityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.SecurityGroup]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PreviewAgentsRequest

### previewAgentsArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# PreviewAgentsRequestPaginate

### previewAgentsArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.inspector.inspector_classes.PaginatorConfig]


# PreviewAgentsResponse

### agentPreviews
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.AgentPreview]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PrivateIp

### privateDnsName
- **Type**: typing.Optional[str]

### privateIpAddress
- **Type**: typing.Optional[str]


# RegisterCrossAccountAccessRoleRequest

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveAttributesFromFindingsRequest

### findingArns
- **Type**: typing.List[str]
- **Required**: Yes

### attributeKeys
- **Type**: typing.List[str]
- **Required**: Yes


# RemoveAttributesFromFindingsResponse

### failedItems
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.inspector.inspector_classes.FailedItemDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceGroup

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.ResourceGroupTag]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ResourceGroupTag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


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


# RulesPackage

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


# Scope

### key
- **Type**: typing.Optional[typing.Literal['INSTANCE_ID', 'RULES_PACKAGE_ARN']]

### value
- **Type**: typing.Optional[str]


# SecurityGroup

### groupName
- **Type**: typing.Optional[str]

### groupId
- **Type**: typing.Optional[str]


# SetTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.Tag]]


# StartAssessmentRunRequest

### assessmentTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentRunName
- **Type**: typing.Optional[str]


# StartAssessmentRunResponse

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.inspector.inspector_classes.ResponseMetadata'>
- **Required**: Yes


# StopAssessmentRunRequest

### assessmentRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### stopAction
- **Type**: typing.Optional[typing.Literal['SKIP_EVALUATION', 'START_EVALUATION']]


# SubscribeToEventRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### event
- **Type**: typing.Literal['ASSESSMENT_RUN_COMPLETED', 'ASSESSMENT_RUN_STARTED', 'ASSESSMENT_RUN_STATE_CHANGED', 'FINDING_REPORTED', 'OTHER']
- **Required**: Yes

### topicArn
- **Type**: <class 'str'>
- **Required**: Yes


# Subscription

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### topicArn
- **Type**: <class 'str'>
- **Required**: Yes

### eventSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.inspector.inspector_classes.EventSubscription]
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# TelemetryMetadata

### messageType
- **Type**: <class 'str'>
- **Required**: Yes

### count
- **Type**: <class 'int'>
- **Required**: Yes

### dataSize
- **Type**: typing.Optional[int]


# TimestampRange

### beginDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UnsubscribeFromEventRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### event
- **Type**: typing.Literal['ASSESSMENT_RUN_COMPLETED', 'ASSESSMENT_RUN_STARTED', 'ASSESSMENT_RUN_STATE_CHANGED', 'FINDING_REPORTED', 'OTHER']
- **Required**: Yes

### topicArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAssessmentTargetRequest

### assessmentTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### assessmentTargetName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceGroupArn
- **Type**: typing.Optional[str]


