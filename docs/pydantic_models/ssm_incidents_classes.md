# Ssm Incidents Classes

# Action

### ssmAutomation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.SsmAutomationUnion]


# ActionOutput

### ssmAutomation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.SsmAutomationOutput]


# ActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddRegionAction

### regionName
- **Type**: <class 'str'>
- **Required**: Yes

### sseKmsKeyId
- **Type**: typing.Optional[str]


# AttributeValueList

### integerValues
- **Type**: typing.Optional[typing.Sequence[int]]

### stringValues
- **Type**: typing.Optional[typing.Sequence[str]]


# AutomationExecution

### ssmExecutionArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetIncidentFindingsError

### code
- **Type**: <class 'str'>
- **Required**: Yes

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetIncidentFindingsInput

### findingIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetIncidentFindingsOutput

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.BatchGetIncidentFindingsError]
- **Required**: Yes

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.Finding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# ChatChannel

### chatbotSns
- **Type**: typing.Optional[typing.Sequence[str]]

### empty
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ChatChannelOutput

### chatbotSns
- **Type**: typing.Optional[typing.List[str]]

### empty
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ChatChannelUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudFormationStackUpdate

### stackArn
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[datetime.datetime]


# CodeDeployDeployment

### deploymentGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[datetime.datetime]


# Condition

### after
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.Timestamp]

### before
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.Timestamp]

### equals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.AttributeValueList]


# CreateReplicationSetInput

### regions
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_incidents_classes.RegionMapInputValue]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateReplicationSetOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResponsePlanInput

### incidentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentTemplateUnion'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.ActionUnion]]

### chatChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelUnion]

### clientToken
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### engagements
- **Type**: typing.Optional[typing.Sequence[str]]

### integrations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.Integration]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateResponsePlanOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTimelineEventInput

### eventData
- **Type**: <class 'str'>
- **Required**: Yes

### eventTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.Timestamp'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### eventReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventReference]]


# CreateTimelineEventOutput

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIncidentRecordInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegionAction

### regionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationSetInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyInput

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResponsePlanInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTimelineEventInput

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes


# DynamicSsmParameterValue

### variable
- **Type**: typing.Optional[typing.Literal['INCIDENT_RECORD_ARN', 'INVOLVED_RESOURCES']]


# EventReference

### relatedItemId
- **Type**: typing.Optional[str]

### resource
- **Type**: typing.Optional[str]


# EventSummary

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### eventUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### eventReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventReference]]


# Filter

### condition
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.Condition'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# Finding

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FindingDetails

### cloudFormationStackUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.CloudFormationStackUpdate]

### codeDeployDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.CodeDeployDeployment]


# FindingSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetIncidentRecordInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIncidentRecordOutput

### incidentRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentRecord'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# GetReplicationSetInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetReplicationSetInputWait

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetReplicationSetInputWaitExtra

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetReplicationSetOutput

### replicationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ReplicationSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePoliciesInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetResourcePoliciesInputPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfig]


# GetResourcePoliciesOutput

### resourcePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.ResourcePolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResponsePlanInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResponsePlanOutput

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.ActionOutput]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### chatChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelOutput'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### engagements
- **Type**: typing.List[str]
- **Required**: Yes

### incidentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentTemplateOutput'>
- **Required**: Yes

### integrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.Integration]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# GetTimelineEventInput

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTimelineEventOutput

### event
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.TimelineEvent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# IncidentRecord

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dedupeString
- **Type**: <class 'str'>
- **Required**: Yes

### impact
- **Type**: <class 'int'>
- **Required**: Yes

### incidentRecordSource
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentRecordSource'>
- **Required**: Yes

### lastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['OPEN', 'RESOLVED']
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### automationExecutions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.AutomationExecution]]

### chatChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelOutput]

### notificationTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItem]]

### resolvedTime
- **Type**: typing.Optional[datetime.datetime]

### summary
- **Type**: typing.Optional[str]


# IncidentRecordSource

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### invokedBy
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]


# IncidentRecordSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### impact
- **Type**: <class 'int'>
- **Required**: Yes

### incidentRecordSource
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentRecordSource'>
- **Required**: Yes

### status
- **Type**: typing.Literal['OPEN', 'RESOLVED']
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### resolvedTime
- **Type**: typing.Optional[datetime.datetime]


# IncidentTemplate

### impact
- **Type**: <class 'int'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### dedupeString
- **Type**: typing.Optional[str]

### incidentTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### notificationTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItem]]

### summary
- **Type**: typing.Optional[str]


# IncidentTemplateOutput

### impact
- **Type**: <class 'int'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### dedupeString
- **Type**: typing.Optional[str]

### incidentTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### notificationTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItem]]

### summary
- **Type**: typing.Optional[str]


# IncidentTemplateUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Integration

### pagerDutyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PagerDutyConfiguration]


# ItemIdentifier

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ItemValue

### arn
- **Type**: typing.Optional[str]

### metricDefinition
- **Type**: typing.Optional[str]

### pagerDutyIncidentDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PagerDutyIncidentDetail]

### url
- **Type**: typing.Optional[str]


# ListIncidentFindingsInput

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIncidentFindingsInputPaginate

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfig]


# ListIncidentFindingsOutput

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.FindingSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIncidentRecordsInput

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIncidentRecordsInputPaginate

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfig]


# ListIncidentRecordsOutput

### incidentRecordSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentRecordSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRelatedItemsInput

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRelatedItemsInputPaginate

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfig]


# ListRelatedItemsOutput

### relatedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.RelatedItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReplicationSetsInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListReplicationSetsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfig]


# ListReplicationSetsOutput

### replicationSetArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResponsePlansInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListResponsePlansInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfig]


# ListResponsePlansOutput

### responsePlanSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponsePlanSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# ListTimelineEventsInput

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['EVENT_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListTimelineEventsInputPaginate

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.Filter]]

### sortBy
- **Type**: typing.Optional[typing.Literal['EVENT_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfig]


# ListTimelineEventsOutput

### eventSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NotificationTargetItem

### snsTopicArn
- **Type**: typing.Optional[str]


# PagerDutyConfiguration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pagerDutyIncidentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.PagerDutyIncidentConfiguration'>
- **Required**: Yes

### secretId
- **Type**: <class 'str'>
- **Required**: Yes


# PagerDutyIncidentConfiguration

### serviceId
- **Type**: <class 'str'>
- **Required**: Yes


# PagerDutyIncidentDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyInput

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyOutput

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# RegionInfo

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### statusUpdateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sseKmsKeyId
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]


# RegionMapInputValue

### sseKmsKeyId
- **Type**: typing.Optional[str]


# RelatedItem

### identifier
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ItemIdentifier'>
- **Required**: Yes

### generatedId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]


# RelatedItemsUpdate

### itemToAdd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.RelatedItem]

### itemToRemove
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ItemIdentifier]


# ReplicationSet

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deletionProtected
- **Type**: <class 'bool'>
- **Required**: Yes

### lastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### regionMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ssm_incidents_classes.RegionInfo]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]


# ResourcePolicy

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### ramResourceShareRegion
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


# ResponsePlanSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]


# SsmAutomation

### documentName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### documentVersion
- **Type**: typing.Optional[str]

### dynamicParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_incidents_classes.DynamicSsmParameterValue]]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### targetAccount
- **Type**: typing.Optional[typing.Literal['IMPACTED_ACCOUNT', 'RESPONSE_PLAN_OWNER_ACCOUNT']]


# SsmAutomationOutput

### documentName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### documentVersion
- **Type**: typing.Optional[str]

### dynamicParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm_incidents_classes.DynamicSsmParameterValue]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### targetAccount
- **Type**: typing.Optional[typing.Literal['IMPACTED_ACCOUNT', 'RESPONSE_PLAN_OWNER_ACCOUNT']]


# SsmAutomationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartIncidentInput

### responsePlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### impact
- **Type**: typing.Optional[int]

### relatedItems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.RelatedItem]]

### title
- **Type**: typing.Optional[str]

### triggerDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.TriggerDetails]


# StartIncidentOutput

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimelineEvent

### eventData
- **Type**: <class 'str'>
- **Required**: Yes

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### eventUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### eventReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventReference]]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TriggerDetails

### source
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.Timestamp'>
- **Required**: Yes

### rawData
- **Type**: typing.Optional[str]

### triggerArn
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeletionProtectionInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtected
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateIncidentRecordInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### chatChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelUnion]

### clientToken
- **Type**: typing.Optional[str]

### impact
- **Type**: typing.Optional[int]

### notificationTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItem]]

### status
- **Type**: typing.Optional[typing.Literal['OPEN', 'RESOLVED']]

### summary
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]


# UpdateRelatedItemsInput

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### relatedItemsUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.RelatedItemsUpdate'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateReplicationSetAction

### addRegionAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.AddRegionAction]

### deleteRegionAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.DeleteRegionAction]


# UpdateReplicationSetInput

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.UpdateReplicationSetAction]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateResponsePlanInput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.ActionUnion]]

### chatChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelUnion]

### clientToken
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### engagements
- **Type**: typing.Optional[typing.Sequence[str]]

### incidentTemplateDedupeString
- **Type**: typing.Optional[str]

### incidentTemplateImpact
- **Type**: typing.Optional[int]

### incidentTemplateNotificationTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItem]]

### incidentTemplateSummary
- **Type**: typing.Optional[str]

### incidentTemplateTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### incidentTemplateTitle
- **Type**: typing.Optional[str]

### integrations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.Integration]]


# UpdateTimelineEventInput

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### eventData
- **Type**: typing.Optional[str]

### eventReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventReference]]

### eventTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.Timestamp]

### eventType
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


