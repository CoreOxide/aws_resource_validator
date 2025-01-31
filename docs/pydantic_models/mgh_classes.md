# Mgh Classes

# ApplicationStateTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ApplicationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# AssociateCreatedArtifactRequestRequestTypeDef

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


# AssociateDiscoveredResourceRequestRequestTypeDef

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateProgressUpdateStreamRequestRequestTypeDef

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


# DeleteProgressUpdateStreamRequestRequestTypeDef

### ProgressUpdateStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# DescribeApplicationStateRequestRequestTypeDef

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


# DescribeMigrationTaskRequestRequestTypeDef

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


# DisassociateCreatedArtifactRequestRequestTypeDef

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


# DisassociateDiscoveredResourceRequestRequestTypeDef

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


# DiscoveredResourceTypeDef

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ImportMigrationTaskRequestRequestTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### DryRun
- **Type**: typing.Optional[bool]


# ListApplicationStatesRequestListApplicationStatesPaginateTypeDef

### ApplicationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListApplicationStatesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListCreatedArtifactsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedArtifactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.CreatedArtifactTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef

### ProgressUpdateStream
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListDiscoveredResourcesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveredResourceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.DiscoveredResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMigrationTasksRequestListMigrationTasksPaginateTypeDef

### ResourceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListMigrationTasksRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ResourceName
- **Type**: typing.Optional[str]


# ListMigrationTasksResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationTaskSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.MigrationTaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgh_classes.PaginatorConfigTypeDef]


# ListProgressUpdateStreamsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProgressUpdateStreamsResultTypeDef

### ProgressUpdateStreamSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgh_classes.ProgressUpdateStreamSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# NotifyApplicationStateRequestRequestTypeDef

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


# NotifyMigrationTaskStateRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str]
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


# PutResourceAttributesRequestRequestTypeDef

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

### Type
- **Type**: typing.Literal['BIOS_ID', 'FQDN', 'IPV4_ADDRESS', 'IPV6_ADDRESS', 'MAC_ADDRESS', 'MOTHERBOARD_SERIAL_NUMBER', 'VM_MANAGED_OBJECT_REFERENCE', 'VM_MANAGER_ID', 'VM_NAME', 'VM_PATH']
- **Required**: Yes

### Value
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


# TaskTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED']
- **Required**: Yes

### StatusDetail
- **Type**: typing.Optional[str]

### ProgressPercent
- **Type**: typing.Optional[int]


