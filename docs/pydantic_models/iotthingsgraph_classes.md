# Iotthingsgraph Classes

# AssociateEntityToThingRequestTypeDef

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

# CreateFlowTemplateRequestTypeDef

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


# CreateSystemInstanceRequestTypeDef

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


# CreateSystemTemplateRequestTypeDef

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


# DependencyRevisionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# DescribeNamespaceRequestTypeDef

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


# DissociateEntityFromThingRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']
- **Required**: Yes


# EntityDescriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetEntitiesRequestTypeDef

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


# GetFlowTemplateResponseTypeDef

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFlowTemplateRevisionsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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


# GetSystemInstanceResponseTypeDef

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSystemTemplateResponseTypeDef

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSystemTemplateRevisionsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetUploadStatusRequestTypeDef

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


# ListFlowExecutionMessagesRequestPaginateTypeDef

### flowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# ListFlowExecutionMessagesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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


# SearchEntitiesRequestPaginateTypeDef

### entityTypes
- **Type**: typing.Sequence[typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']]
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.EntityFilterTypeDef]]

### namespaceVersion
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchEntitiesRequestTypeDef

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


# SearchEntitiesResponseTypeDef

### descriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.EntityDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchFlowExecutionsRequestPaginateTypeDef

### systemInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### flowExecutionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchFlowExecutionsRequestTypeDef

### systemInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### flowExecutionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.TimestampTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.TimestampTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchFlowExecutionsResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowExecutionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchFlowTemplatesRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchFlowTemplatesRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchFlowTemplatesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchSystemInstancesRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchSystemInstancesRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchSystemInstancesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchSystemTemplatesRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchSystemTemplatesRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchSystemTemplatesResponseTypeDef

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchThingsRequestPaginateTypeDef

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceVersion
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph_classes.PaginatorConfigTypeDef]


# SearchThingsRequestTypeDef

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### namespaceVersion
- **Type**: typing.Optional[int]


# SearchThingsResponseTypeDef

### things
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph_classes.ThingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

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


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UndeploySystemInstanceResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemInstanceSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFlowTemplateResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.FlowTemplateSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSystemTemplateResponseTypeDef

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.SystemTemplateSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadEntityDefinitionsRequestTypeDef

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


