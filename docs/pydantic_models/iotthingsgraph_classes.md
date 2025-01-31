# Iotthingsgraph Classes

# AssociateEntityToThingRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceVersion
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateFlowTemplateRequestRequestTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef'>
- **Required**: Yes

### compatibleNamespaceVersion
- **Type**: typing.Optional[int]


# CreateFlowTemplateResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSystemInstanceRequestRequestTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef'>
- **Required**: Yes

### target
- **Type**: typing.Literal['CLOUD', 'GREENGRASS']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.TagTypeDef]]

### greengrassGroupName
- **Type**: typing.Optional[str]

### s3BucketName
- **Type**: typing.Optional[str]

### metricsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.MetricsConfigurationTypeDef]

### flowActionsRoleArn
- **Type**: typing.Optional[str]


# CreateSystemInstanceResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSystemTemplateRequestRequestTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef'>
- **Required**: Yes

### compatibleNamespaceVersion
- **Type**: typing.Optional[int]


# CreateSystemTemplateResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefinitionDocumentTypeDef

### language
- **Type**: typing.Literal['GRAPHQL']
- **Required**: Yes

### text
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNamespaceResponseTypeDef

### namespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSystemInstanceRequestRequestTypeDef

### id
- **Type**: typing.Optional[str]


# DeleteSystemTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DependencyRevisionTypeDef

### id
- **Type**: typing.Optional[str]

### revisionNumber
- **Type**: typing.Optional[int]


# DeploySystemInstanceRequestRequestTypeDef

### id
- **Type**: typing.Optional[str]


# DeploySystemInstanceResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceSummaryTypeDef'>
- **Required**: Yes

### greengrassDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeprecateFlowTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecateSystemTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNamespaceRequestRequestTypeDef

### namespaceName
- **Type**: typing.Optional[str]


# DescribeNamespaceResponseTypeDef

### namespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### trackingNamespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### trackingNamespaceVersion
- **Type**: <class 'int'>
- **Required**: Yes

### namespaceVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DissociateEntityFromThingRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']
- **Required**: Yes


# EntityDescriptionTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef]


# EntityFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['NAME', 'NAMESPACE', 'REFERENCED_ENTITY_ID', 'SEMANTIC_TYPE_PATH']]

### value
- **Type**: typing.Optional[typing.Sequence[str]]


# FlowExecutionMessageTypeDef

### messageId
- **Type**: typing.Optional[str]

### eventType
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGE_TASK_MESSAGE', 'ACTIVITY_FAILED', 'ACTIVITY_SCHEDULED', 'ACTIVITY_STARTED', 'ACTIVITY_SUCCEEDED', 'EXECUTION_ABORTED', 'EXECUTION_FAILED', 'EXECUTION_STARTED', 'EXECUTION_SUCCEEDED', 'SCHEDULE_NEXT_READY_STEPS_TASK', 'START_FLOW_EXECUTION_TASK', 'STEP_FAILED', 'STEP_STARTED', 'STEP_SUCCEEDED', 'THING_ACTION_TASK', 'THING_ACTION_TASK_FAILED', 'THING_ACTION_TASK_SUCCEEDED']]

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### payload
- **Type**: typing.Optional[str]


# FlowExecutionSummaryTypeDef

### flowExecutionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'RUNNING', 'SUCCEEDED']]

### systemInstanceId
- **Type**: typing.Optional[str]

### flowTemplateId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# FlowTemplateDescriptionTypeDef

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateSummaryTypeDef]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef]

### validatedNamespaceVersion
- **Type**: typing.Optional[int]


# FlowTemplateFilterTypeDef

### name
- **Type**: typing.Literal['DEVICE_MODEL_ID']
- **Required**: Yes

### value
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FlowTemplateSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### revisionNumber
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# GetEntitiesRequestRequestTypeDef

### ids
- **Type**: typing.Sequence[str]
- **Required**: Yes

### namespaceVersion
- **Type**: typing.Optional[int]


# GetEntitiesResponseTypeDef

### descriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.EntityDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFlowTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### revisionNumber
- **Type**: typing.Optional[int]


# GetFlowTemplateResponseTypeDef

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFlowTemplateRevisionsRequestGetFlowTemplateRevisionsPaginateTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# GetFlowTemplateRevisionsRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetFlowTemplateRevisionsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNamespaceDeletionStatusResponseTypeDef

### namespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### errorCode
- **Type**: typing.Literal['VALIDATION_FAILED']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSystemInstanceRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSystemInstanceResponseTypeDef

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSystemTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### revisionNumber
- **Type**: typing.Optional[int]


# GetSystemTemplateResponseTypeDef

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSystemTemplateRevisionsRequestGetSystemTemplateRevisionsPaginateTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# GetSystemTemplateRevisionsRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetSystemTemplateRevisionsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUploadStatusRequestRequestTypeDef

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUploadStatusResponseTypeDef

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### namespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceVersion
- **Type**: <class 'int'>
- **Required**: Yes

### failureReason
- **Type**: typing.List[str]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFlowExecutionMessagesRequestListFlowExecutionMessagesPaginateTypeDef

### flowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# ListFlowExecutionMessagesRequestRequestTypeDef

### flowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFlowExecutionMessagesResponseTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowExecutionMessageTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.TagTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricsConfigurationTypeDef

### cloudMetricEnabled
- **Type**: typing.Optional[bool]

### metricRuleRoleArn
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# SearchEntitiesRequestRequestTypeDef

### entityTypes
- **Type**: typing.Sequence[typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']]
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.EntityFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### namespaceVersion
- **Type**: typing.Optional[int]


# SearchEntitiesRequestSearchEntitiesPaginateTypeDef

### entityTypes
- **Type**: typing.Sequence[typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']]
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.EntityFilterTypeDef]]

### namespaceVersion
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchEntitiesResponseTypeDef

### descriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.EntityDescriptionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchFlowExecutionsRequestRequestTypeDef

### systemInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### flowExecutionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchFlowExecutionsRequestSearchFlowExecutionsPaginateTypeDef

### systemInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### flowExecutionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchFlowExecutionsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowExecutionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchFlowTemplatesRequestRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchFlowTemplatesRequestSearchFlowTemplatesPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchFlowTemplatesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchSystemInstancesRequestRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchSystemInstancesRequestSearchSystemInstancesPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchSystemInstancesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchSystemTemplatesRequestRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchSystemTemplatesRequestSearchSystemTemplatesPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchSystemTemplatesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchThingsRequestRequestTypeDef

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### namespaceVersion
- **Type**: typing.Optional[int]


# SearchThingsRequestSearchThingsPaginateTypeDef

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceVersion
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchThingsResponseTypeDef

### things
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.ThingTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SystemInstanceDescriptionTypeDef

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceSummaryTypeDef]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef]

### s3BucketName
- **Type**: typing.Optional[str]

### metricsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.MetricsConfigurationTypeDef]

### validatedNamespaceVersion
- **Type**: typing.Optional[int]

### validatedDependencyRevisions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.DependencyRevisionTypeDef]]

### flowActionsRoleArn
- **Type**: typing.Optional[str]


# SystemInstanceFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['GREENGRASS_GROUP_NAME', 'STATUS', 'SYSTEM_TEMPLATE_ID']]

### value
- **Type**: typing.Optional[typing.Sequence[str]]


# SystemInstanceSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['BOOTSTRAP', 'DELETED_IN_TARGET', 'DEPLOYED_IN_TARGET', 'DEPLOY_IN_PROGRESS', 'FAILED', 'NOT_DEPLOYED', 'PENDING_DELETE', 'UNDEPLOY_IN_PROGRESS']]

### target
- **Type**: typing.Optional[typing.Literal['CLOUD', 'GREENGRASS']]

### greengrassGroupName
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### greengrassGroupId
- **Type**: typing.Optional[str]

### greengrassGroupVersionId
- **Type**: typing.Optional[str]


# SystemTemplateDescriptionTypeDef

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateSummaryTypeDef]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef]

### validatedNamespaceVersion
- **Type**: typing.Optional[int]


# SystemTemplateFilterTypeDef

### name
- **Type**: typing.Literal['FLOW_TEMPLATE_ID']
- **Required**: Yes

### value
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SystemTemplateSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### revisionNumber
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ThingTypeDef

### thingArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]


# UndeploySystemInstanceRequestRequestTypeDef

### id
- **Type**: typing.Optional[str]


# UndeploySystemInstanceResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFlowTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef'>
- **Required**: Yes

### compatibleNamespaceVersion
- **Type**: typing.Optional[int]


# UpdateFlowTemplateResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSystemTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef'>
- **Required**: Yes

### compatibleNamespaceVersion
- **Type**: typing.Optional[int]


# UpdateSystemTemplateResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadEntityDefinitionsRequestRequestTypeDef

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.DefinitionDocumentTypeDef]

### syncWithPublicNamespace
- **Type**: typing.Optional[bool]

### deprecateExistingEntities
- **Type**: typing.Optional[bool]


# UploadEntityDefinitionsResponseTypeDef

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


