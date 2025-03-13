# Mgh Classes

# ApplicationStateTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ApplicationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# AssociateCreatedArtifactRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedArtifact
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.CreatedArtifactTypeDef'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# AssociateDiscoveredResourceRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveredResource
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.DiscoveredResourceTypeDef'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# AssociateSourceResourceRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceResource
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.SourceResourceTypeDef'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateProgressUpdateStreamRequestTypeDef

### ProgressUpdateStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# CreatedArtifactTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# DeleteProgressUpdateStreamRequestTypeDef

### ProgressUpdateStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# DescribeApplicationStateRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationStateResultTypeDef

### ApplicationStatus
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMigrationTaskRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMigrationTaskResultTypeDef

### MigrationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.MigrationTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateCreatedArtifactRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedArtifactName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# DisassociateDiscoveredResourceRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# DisassociateSourceResourceRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# DiscoveredResourceTypeDef

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ImportMigrationTaskRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# ListApplicationStatesRequestPaginateTypeDef

### ApplicationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListApplicationStatesRequestTypeDef

### ApplicationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApplicationStatesResultTypeDef

### ApplicationStateList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.ApplicationStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCreatedArtifactsRequestPaginateTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListCreatedArtifactsRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCreatedArtifactsResultTypeDef

### CreatedArtifactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.CreatedArtifactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesRequestPaginateTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListDiscoveredResourcesRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDiscoveredResourcesResultTypeDef

### DiscoveredResourceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.DiscoveredResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMigrationTaskUpdatesRequestPaginateTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListMigrationTaskUpdatesRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMigrationTaskUpdatesResultTypeDef

### MigrationTaskUpdateList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.MigrationTaskUpdateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMigrationTasksRequestPaginateTypeDef

### ResourceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListMigrationTasksRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceName
- **Type**: typing.Optional[str]


# ListMigrationTasksResultTypeDef

### MigrationTaskSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.MigrationTaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProgressUpdateStreamsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListProgressUpdateStreamsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProgressUpdateStreamsResultTypeDef

### ProgressUpdateStreamSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.ProgressUpdateStreamSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSourceResourcesRequestPaginateTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListSourceResourcesRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSourceResourcesResultTypeDef

### SourceResourceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.SourceResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MigrationTaskSummaryTypeDef

### ProgressUpdateStream
- **Type**: typing.Optional[str]

### MigrationTaskName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED']]

### ProgressPercent
- **Type**: typing.Optional[int]

### StatusDetail
- **Type**: typing.Optional[str]

### UpdateDateTime
- **Type**: typing.Optional[datetime.datetime]


# MigrationTaskTypeDef

### ProgressUpdateStream
- **Type**: typing.Optional[str]

### MigrationTaskName
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.TaskTypeDef]

### UpdateDateTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceAttributeList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgh_classes.ResourceAttributeTypeDef]]


# MigrationTaskUpdateTypeDef

### UpdateDateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateType
- **Type**: typing.Optional[typing.Literal['MIGRATION_TASK_STATE_UPDATED']]

### MigrationTaskState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.TaskTypeDef]


# NotifyApplicationStateRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### UpdateDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.TimestampTypeDef]

### DryRun
- **Type**: typing.Optional[bool]


# NotifyMigrationTaskStateRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### Task
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.TaskTypeDef'>
- **Required**: Yes

### UpdateDateTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.TimestampTypeDef'>
- **Required**: Yes

### NextUpdateSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProgressUpdateStreamSummaryTypeDef

### ProgressUpdateStreamName
- **Type**: typing.Optional[str]


# PutResourceAttributesRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAttributeList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mgh_classes.ResourceAttributeTypeDef]
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# ResourceAttributeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SourceResourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### StatusDetail
- **Type**: typing.Optional[str]


# TaskTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### StatusDetail
- **Type**: typing.Optional[str]

### ProgressPercent
- **Type**: typing.Optional[int]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

