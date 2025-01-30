# ssm_incidents_classes

# ActionTypeDef

### ssmAutomation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.SsmAutomationTypeDef]


# AddRegionActionTypeDef

### regionName
- **Type**: <class 'str'>
- **Required**: Yes

### sseKmsKeyId
- **Type**: typing.Optional[str]


# AttributeValueListTypeDef

### integerValues
- **Type**: typing.Optional[typing.Sequence[int]]

### stringValues
- **Type**: typing.Optional[typing.Sequence[str]]


# AutomationExecutionTypeDef

### ssmExecutionArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetIncidentFindingsErrorTypeDef

### code
- **Type**: <class 'str'>
- **Required**: Yes

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetIncidentFindingsInputRequestTypeDef

### findingIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetIncidentFindingsOutputTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.BatchGetIncidentFindingsErrorTypeDef]
- **Required**: Yes

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.FindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChatChannelTypeDef

### chatbotSns
- **Type**: typing.Optional[typing.Sequence[str]]

### empty
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# CloudFormationStackUpdateTypeDef

### stackArn
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[datetime.datetime]


# CodeDeployDeploymentTypeDef

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


# ConditionTypeDef

### after
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### before
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### equals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.AttributeValueListTypeDef]


# CreateReplicationSetInputRequestTypeDef

### regions
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_incidents_classes.RegionMapInputValueTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateReplicationSetOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResponsePlanInputRequestTypeDef

### incidentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentTemplateTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.ActionTypeDef]]

### chatChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### engagements
- **Type**: typing.Optional[typing.Sequence[str]]

### integrations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.IntegrationTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateResponsePlanOutputTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTimelineEventInputRequestTypeDef

### eventData
- **Type**: <class 'str'>
- **Required**: Yes

### eventTime
- **Type**: typing.Union[datetime.datetime, str]
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventReferenceTypeDef]]


# CreateTimelineEventOutputTypeDef

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIncidentRecordInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegionActionTypeDef

### regionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationSetInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyInputRequestTypeDef

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResponsePlanInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTimelineEventInputRequestTypeDef

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes


# DynamicSsmParameterValueTypeDef

### variable
- **Type**: typing.Optional[typing.Literal['INCIDENT_RECORD_ARN', 'INVOLVED_RESOURCES']]


# EventReferenceTypeDef

### relatedItemId
- **Type**: typing.Optional[str]

### resource
- **Type**: typing.Optional[str]


# EventSummaryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventReferenceTypeDef]]


# FilterTypeDef

### condition
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ConditionTypeDef'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# FindingDetailsTypeDef

### cloudFormationStackUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.CloudFormationStackUpdateTypeDef]

### codeDeployDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.CodeDeployDeploymentTypeDef]


# FindingSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FindingTypeDef

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.FindingDetailsTypeDef]


# GetIncidentRecordInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIncidentRecordOutputTypeDef

### incidentRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentRecordTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReplicationSetInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetReplicationSetInputWaitForReplicationSetActiveWaitTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.WaiterConfigTypeDef]


# GetReplicationSetInputWaitForReplicationSetDeletedWaitTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.WaiterConfigTypeDef]


# GetReplicationSetOutputTypeDef

### replicationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ReplicationSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePoliciesInputGetResourcePoliciesPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfigTypeDef]


# GetResourcePoliciesInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetResourcePoliciesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### resourcePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.ResourcePolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResponsePlanInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResponsePlanOutputTypeDef

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.ActionTypeDef]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### chatChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelTypeDef'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### engagements
- **Type**: typing.List[str]
- **Required**: Yes

### incidentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentTemplateTypeDef'>
- **Required**: Yes

### integrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.IntegrationTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTimelineEventInputRequestTypeDef

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTimelineEventOutputTypeDef

### event
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.TimelineEventTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IncidentRecordSourceTypeDef

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


# IncidentRecordSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentRecordSourceTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['OPEN', 'RESOLVED']
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### resolvedTime
- **Type**: typing.Optional[datetime.datetime]


# IncidentRecordTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentRecordSourceTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.AutomationExecutionTypeDef]]

### chatChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelTypeDef]

### notificationTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItemTypeDef]]

### resolvedTime
- **Type**: typing.Optional[datetime.datetime]

### summary
- **Type**: typing.Optional[str]


# IncidentTemplateTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItemTypeDef]]

### summary
- **Type**: typing.Optional[str]


# IntegrationTypeDef

### pagerDutyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PagerDutyConfigurationTypeDef]


# ItemIdentifierTypeDef

### type
- **Type**: typing.Literal['ANALYSIS', 'ATTACHMENT', 'AUTOMATION', 'INCIDENT', 'INVOLVED_RESOURCE', 'METRIC', 'OTHER', 'PARENT', 'TASK']
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ItemValueTypeDef'>
- **Required**: Yes


# ItemValueTypeDef

### arn
- **Type**: typing.Optional[str]

### metricDefinition
- **Type**: typing.Optional[str]

### pagerDutyIncidentDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PagerDutyIncidentDetailTypeDef]

### url
- **Type**: typing.Optional[str]


# ListIncidentFindingsInputListIncidentFindingsPaginateTypeDef

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfigTypeDef]


# ListIncidentFindingsInputRequestTypeDef

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIncidentFindingsOutputTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.FindingSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIncidentRecordsInputListIncidentRecordsPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfigTypeDef]


# ListIncidentRecordsInputRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIncidentRecordsOutputTypeDef

### incidentRecordSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.IncidentRecordSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRelatedItemsInputListRelatedItemsPaginateTypeDef

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfigTypeDef]


# ListRelatedItemsInputRequestTypeDef

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRelatedItemsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### relatedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.RelatedItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReplicationSetsInputListReplicationSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfigTypeDef]


# ListReplicationSetsInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListReplicationSetsOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### replicationSetArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResponsePlansInputListResponsePlansPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfigTypeDef]


# ListResponsePlansInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListResponsePlansOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### responsePlanSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponsePlanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTimelineEventsInputListTimelineEventsPaginateTypeDef

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.FilterTypeDef]]

### sortBy
- **Type**: typing.Optional[typing.Literal['EVENT_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.PaginatorConfigTypeDef]


# ListTimelineEventsInputRequestTypeDef

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['EVENT_TIME']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListTimelineEventsOutputTypeDef

### eventSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotificationTargetItemTypeDef

### snsTopicArn
- **Type**: typing.Optional[str]


# PagerDutyConfigurationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pagerDutyIncidentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.PagerDutyIncidentConfigurationTypeDef'>
- **Required**: Yes

### secretId
- **Type**: <class 'str'>
- **Required**: Yes


# PagerDutyIncidentConfigurationTypeDef

### serviceId
- **Type**: <class 'str'>
- **Required**: Yes


# PagerDutyIncidentDetailTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### autoResolve
- **Type**: typing.Optional[bool]

### secretId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyInputRequestTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyOutputTypeDef

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegionInfoTypeDef

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


# RegionMapInputValueTypeDef

### sseKmsKeyId
- **Type**: typing.Optional[str]


# RelatedItemTypeDef

### identifier
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ItemIdentifierTypeDef'>
- **Required**: Yes

### generatedId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]


# RelatedItemsUpdateTypeDef

### itemToAdd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.RelatedItemTypeDef]

### itemToRemove
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ItemIdentifierTypeDef]


# ReplicationSetTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ssm_incidents_classes.RegionInfoTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]


# ResourcePolicyTypeDef

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### ramResourceShareRegion
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


# ResponsePlanSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]


# SsmAutomationTypeDef

### documentName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### documentVersion
- **Type**: typing.Optional[str]

### dynamicParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_incidents_classes.DynamicSsmParameterValueTypeDef]]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### targetAccount
- **Type**: typing.Optional[typing.Literal['IMPACTED_ACCOUNT', 'RESPONSE_PLAN_OWNER_ACCOUNT']]


# StartIncidentInputRequestTypeDef

### responsePlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### impact
- **Type**: typing.Optional[int]

### relatedItems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.RelatedItemTypeDef]]

### title
- **Type**: typing.Optional[str]

### triggerDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.TriggerDetailsTypeDef]


# StartIncidentOutputTypeDef

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimelineEventTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventReferenceTypeDef]]


# TriggerDetailsTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### rawData
- **Type**: typing.Optional[str]

### triggerArn
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeletionProtectionInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### deletionProtected
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateIncidentRecordInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### chatChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### impact
- **Type**: typing.Optional[int]

### notificationTargets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItemTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['OPEN', 'RESOLVED']]

### summary
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]


# UpdateRelatedItemsInputRequestTypeDef

### incidentRecordArn
- **Type**: <class 'str'>
- **Required**: Yes

### relatedItemsUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_incidents_classes.RelatedItemsUpdateTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateReplicationSetActionTypeDef

### addRegionAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.AddRegionActionTypeDef]

### deleteRegionAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.DeleteRegionActionTypeDef]


# UpdateReplicationSetInputRequestTypeDef

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.UpdateReplicationSetActionTypeDef]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateResponsePlanInputRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.ActionTypeDef]]

### chatChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_incidents_classes.ChatChannelTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.NotificationTargetItemTypeDef]]

### incidentTemplateSummary
- **Type**: typing.Optional[str]

### incidentTemplateTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### incidentTemplateTitle
- **Type**: typing.Optional[str]

### integrations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.IntegrationTypeDef]]


# UpdateTimelineEventInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_incidents_classes.EventReferenceTypeDef]]

### eventTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### eventType
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


