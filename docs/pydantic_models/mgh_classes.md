# Mgh Classes

# ApplicationState

### ApplicationId
- **Type**: typing.Optional[str]

### ApplicationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# AssociateCreatedArtifactRequest

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedArtifact
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.CreatedArtifact'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# AssociateDiscoveredResourceRequest

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveredResource
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.DiscoveredResource'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# AssociateSourceResourceRequest

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceResource
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.SourceResource'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateProgressUpdateStreamRequest

### ProgressUpdateStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# CreatedArtifact

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# DeleteProgressUpdateStreamRequest

### ProgressUpdateStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# DescribeApplicationStateRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationStateResult

### ApplicationStatus
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMigrationTaskRequest

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMigrationTaskResult

### MigrationTask
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.MigrationTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateCreatedArtifactRequest

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


# DisassociateDiscoveredResourceRequest

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


# DisassociateSourceResourceRequest

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


# DiscoveredResource

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ImportMigrationTaskRequest

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# ListApplicationStatesRequest

### ApplicationIds
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApplicationStatesRequestPaginate

### ApplicationIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh.mgh_classes.PaginatorConfig]


# ListApplicationStatesResult

### ApplicationStateList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.ApplicationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCreatedArtifactsRequest

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


# ListCreatedArtifactsRequestPaginate

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh.mgh_classes.PaginatorConfig]


# ListCreatedArtifactsResult

### CreatedArtifactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.CreatedArtifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesRequest

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


# ListDiscoveredResourcesRequestPaginate

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh.mgh_classes.PaginatorConfig]


# ListDiscoveredResourcesResult

### DiscoveredResourceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.DiscoveredResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMigrationTaskUpdatesRequest

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


# ListMigrationTaskUpdatesRequestPaginate

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh.mgh_classes.PaginatorConfig]


# ListMigrationTaskUpdatesResult

### MigrationTaskUpdateList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.MigrationTaskUpdate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMigrationTasksRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceName
- **Type**: typing.Optional[str]


# ListMigrationTasksRequestPaginate

### ResourceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh.mgh_classes.PaginatorConfig]


# ListMigrationTasksResult

### MigrationTaskSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.MigrationTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProgressUpdateStreamsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProgressUpdateStreamsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh.mgh_classes.PaginatorConfig]


# ListProgressUpdateStreamsResult

### ProgressUpdateStreamSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.ProgressUpdateStreamSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSourceResourcesRequest

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


# ListSourceResourcesRequestPaginate

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh.mgh_classes.PaginatorConfig]


# ListSourceResourcesResult

### SourceResourceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.SourceResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MigrationTask

### ProgressUpdateStream
- **Type**: typing.Optional[str]

### MigrationTaskName
- **Type**: typing.Optional[str]

### Task
- **Type**: <class 'NoneType'>

### UpdateDateTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceAttributeList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.ResourceAttribute]]


# MigrationTaskSummary

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


# MigrationTaskUpdate

### UpdateDateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdateType
- **Type**: typing.Optional[typing.Literal['MIGRATION_TASK_STATE_UPDATED']]

### MigrationTaskState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh.mgh_classes.Task]


# NotifyApplicationStateRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### UpdateDateTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DryRun
- **Type**: typing.Optional[bool]


# NotifyMigrationTaskStateRequest

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### Task
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh.mgh_classes.Task'>
- **Required**: Yes

### UpdateDateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### NextUpdateSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProgressUpdateStreamSummary

### ProgressUpdateStreamName
- **Type**: typing.Optional[str]


# PutResourceAttributesRequest

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAttributeList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh.mgh_classes.ResourceAttribute]
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# ResourceAttribute

### Type
- **Type**: typing.Literal['BIOS_ID', 'FQDN', 'IPV4_ADDRESS', 'IPV6_ADDRESS', 'MAC_ADDRESS', 'MOTHERBOARD_SERIAL_NUMBER', 'VM_MANAGED_OBJECT_REFERENCE', 'VM_MANAGER_ID', 'VM_NAME', 'VM_PATH']
- **Required**: Yes

### Value
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


# SourceResource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### StatusDetail
- **Type**: typing.Optional[str]


# Task

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### StatusDetail
- **Type**: typing.Optional[str]

### ProgressPercent
- **Type**: typing.Optional[int]


