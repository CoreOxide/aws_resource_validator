# Iotthingsgraph Classes

# AssociateEntityToThingRequest

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

# CreateFlowTemplateRequest

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument'>
- **Required**: Yes

### compatibleNamespaceVersion
- **Type**: typing.Optional[int]


# CreateFlowTemplateResponse

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowTemplateSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSystemInstanceRequest

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument'>
- **Required**: Yes

### target
- **Type**: typing.Literal['CLOUD', 'GREENGRASS']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.Tag]]

### greengrassGroupName
- **Type**: typing.Optional[str]

### s3BucketName
- **Type**: typing.Optional[str]

### metricsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.MetricsConfiguration]

### flowActionsRoleArn
- **Type**: typing.Optional[str]


# CreateSystemInstanceResponse

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemInstanceSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSystemTemplateRequest

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument'>
- **Required**: Yes

### compatibleNamespaceVersion
- **Type**: typing.Optional[int]


# CreateSystemTemplateResponse

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemTemplateSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# DefinitionDocument

### language
- **Type**: typing.Literal['GRAPHQL']
- **Required**: Yes

### text
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNamespaceResponse

### namespaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSystemInstanceRequest

### id
- **Type**: typing.Optional[str]


# DeleteSystemTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DependencyRevision

### id
- **Type**: typing.Optional[str]

### revisionNumber
- **Type**: typing.Optional[int]


# DeploySystemInstanceRequest

### id
- **Type**: typing.Optional[str]


# DeploySystemInstanceResponse

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemInstanceSummary'>
- **Required**: Yes

### greengrassDeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# DeprecateFlowTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecateSystemTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNamespaceRequest

### namespaceName
- **Type**: typing.Optional[str]


# DescribeNamespaceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# DissociateEntityFromThingRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']
- **Required**: Yes


# EntityDescription

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument]


# EntityFilter

### name
- **Type**: typing.Optional[typing.Literal['NAME', 'NAMESPACE', 'REFERENCED_ENTITY_ID', 'SEMANTIC_TYPE_PATH']]

### value
- **Type**: typing.Optional[typing.List[str]]


# FlowExecutionMessage

### messageId
- **Type**: typing.Optional[str]

### eventType
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGE_TASK_MESSAGE', 'ACTIVITY_FAILED', 'ACTIVITY_SCHEDULED', 'ACTIVITY_STARTED', 'ACTIVITY_SUCCEEDED', 'EXECUTION_ABORTED', 'EXECUTION_FAILED', 'EXECUTION_STARTED', 'EXECUTION_SUCCEEDED', 'SCHEDULE_NEXT_READY_STEPS_TASK', 'START_FLOW_EXECUTION_TASK', 'STEP_FAILED', 'STEP_STARTED', 'STEP_SUCCEEDED', 'THING_ACTION_TASK', 'THING_ACTION_TASK_FAILED', 'THING_ACTION_TASK_SUCCEEDED']]

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### payload
- **Type**: typing.Optional[str]


# FlowExecutionSummary

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


# FlowTemplateDescription

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowTemplateSummary]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument]

### validatedNamespaceVersion
- **Type**: typing.Optional[int]


# FlowTemplateFilter

### name
- **Type**: typing.Literal['DEVICE_MODEL_ID']
- **Required**: Yes

### value
- **Type**: typing.List[str]
- **Required**: Yes


# FlowTemplateSummary

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### revisionNumber
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# GetEntitiesRequest

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### namespaceVersion
- **Type**: typing.Optional[int]


# GetEntitiesResponse

### descriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.EntityDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# GetFlowTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### revisionNumber
- **Type**: typing.Optional[int]


# GetFlowTemplateResponse

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowTemplateDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# GetFlowTemplateRevisionsRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetFlowTemplateRevisionsRequestPaginate

### id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# GetFlowTemplateRevisionsResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetNamespaceDeletionStatusResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# GetSystemInstanceRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSystemInstanceResponse

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemInstanceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# GetSystemTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### revisionNumber
- **Type**: typing.Optional[int]


# GetSystemTemplateResponse

### description
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemTemplateDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# GetSystemTemplateRevisionsRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetSystemTemplateRevisionsRequestPaginate

### id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# GetSystemTemplateRevisionsResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetUploadStatusRequest

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUploadStatusResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# ListFlowExecutionMessagesRequest

### flowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFlowExecutionMessagesRequestPaginate

### flowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# ListFlowExecutionMessagesResponse

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowExecutionMessage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MetricsConfiguration

### cloudMetricEnabled
- **Type**: typing.Optional[bool]

### metricRuleRoleArn
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# SearchEntitiesRequest

### entityTypes
- **Type**: typing.List[typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']]
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.EntityFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### namespaceVersion
- **Type**: typing.Optional[int]


# SearchEntitiesRequestPaginate

### entityTypes
- **Type**: typing.List[typing.Literal['ACTION', 'CAPABILITY', 'DEVICE', 'DEVICE_MODEL', 'ENUM', 'EVENT', 'MAPPING', 'PROPERTY', 'SERVICE', 'STATE']]
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.EntityFilter]]

### namespaceVersion
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# SearchEntitiesResponse

### descriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.EntityDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchFlowExecutionsRequest

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


# SearchFlowExecutionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# SearchFlowExecutionsResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchFlowTemplatesRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowTemplateFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchFlowTemplatesRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowTemplateFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# SearchFlowTemplatesResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchSystemInstancesRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemInstanceFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchSystemInstancesRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemInstanceFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# SearchSystemInstancesResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemInstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchSystemTemplatesRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemTemplateFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# SearchSystemTemplatesRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemTemplateFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# SearchSystemTemplatesResponse

### summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchThingsRequest

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### namespaceVersion
- **Type**: typing.Optional[int]


# SearchThingsRequestPaginate

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceVersion
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.PaginatorConfig]


# SearchThingsResponse

### things
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.Thing]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SystemInstanceDescription

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemInstanceSummary]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument]

### s3BucketName
- **Type**: typing.Optional[str]

### metricsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.MetricsConfiguration]

### validatedNamespaceVersion
- **Type**: typing.Optional[int]

### validatedDependencyRevisions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DependencyRevision]]

### flowActionsRoleArn
- **Type**: typing.Optional[str]


# SystemInstanceFilter

### name
- **Type**: typing.Optional[typing.Literal['GREENGRASS_GROUP_NAME', 'STATUS', 'SYSTEM_TEMPLATE_ID']]

### value
- **Type**: typing.Optional[typing.List[str]]


# SystemInstanceSummary

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


# SystemTemplateDescription

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemTemplateSummary]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument]

### validatedNamespaceVersion
- **Type**: typing.Optional[int]


# SystemTemplateFilter

### name
- **Type**: typing.Literal['FLOW_TEMPLATE_ID']
- **Required**: Yes

### value
- **Type**: typing.List[str]
- **Required**: Yes


# SystemTemplateSummary

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### revisionNumber
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.Tag]
- **Required**: Yes


# Thing

### thingArn
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]


# UndeploySystemInstanceRequest

### id
- **Type**: typing.Optional[str]


# UndeploySystemInstanceResponse

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemInstanceSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateFlowTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument'>
- **Required**: Yes

### compatibleNamespaceVersion
- **Type**: typing.Optional[int]


# UpdateFlowTemplateResponse

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.FlowTemplateSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSystemTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument'>
- **Required**: Yes

### compatibleNamespaceVersion
- **Type**: typing.Optional[int]


# UpdateSystemTemplateResponse

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.SystemTemplateSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


# UploadEntityDefinitionsRequest

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.DefinitionDocument]

### syncWithPublicNamespace
- **Type**: typing.Optional[bool]

### deprecateExistingEntities
- **Type**: typing.Optional[bool]


# UploadEntityDefinitionsResponse

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotthingsgraph.iotthingsgraph_classes.ResponseMetadata'>
- **Required**: Yes


