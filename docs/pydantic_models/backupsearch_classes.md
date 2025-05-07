# Backupsearch Classes

# BackupCreationTimeFilter

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# BackupCreationTimeFilterOutput

### CreatedAfter
- **Type**: typing.Optional[datetime.datetime]

### CreatedBefore
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CurrentSearchProgress

### RecoveryPointsScannedCount
- **Type**: typing.Optional[int]

### ItemsScannedCount
- **Type**: typing.Optional[int]

### ItemsMatchedCount
- **Type**: typing.Optional[int]


# EBSItemFilter

### FilePaths
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.StringCondition]]

### Sizes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.LongCondition]]

### CreationTimes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.TimeCondition]]

### LastModificationTimes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.TimeCondition]]


# EBSItemFilterOutput

### FilePaths
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.StringCondition]]

### Sizes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.LongCondition]]

### CreationTimes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.TimeConditionOutput]]

### LastModificationTimes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.TimeConditionOutput]]


# EBSResultItem

### BackupResourceArn
- **Type**: typing.Optional[str]

### SourceResourceArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### FileSystemIdentifier
- **Type**: typing.Optional[str]

### FilePath
- **Type**: typing.Optional[str]

### FileSize
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ExportJobSummary

### ExportJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExportJobArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]

### SearchJobArn
- **Type**: typing.Optional[str]


# ExportSpecification

### s3ExportSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.S3ExportSpecification]


# GetSearchJobInput

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSearchJobOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SearchScopeSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.SearchScopeSummary'>
- **Required**: Yes

### CurrentSearchProgress
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.CurrentSearchProgress'>
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### CompletionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### SearchScope
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.SearchScopeOutput'>
- **Required**: Yes

### ItemFilters
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ItemFiltersOutput'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SearchJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes


# GetSearchResultExportJobInput

### ExportJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSearchResultExportJobOutput

### ExportJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'RUNNING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ExportSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ExportSpecification'>
- **Required**: Yes

### SearchJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes


# ItemFilters

### S3ItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.S3ItemFilter]]

### EBSItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.EBSItemFilter]]


# ItemFiltersOutput

### S3ItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.S3ItemFilterOutput]]

### EBSItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.EBSItemFilterOutput]]


# ListSearchJobBackupsInput

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSearchJobBackupsInputPaginate

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.PaginatorConfig]


# ListSearchJobBackupsOutput

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.SearchJobBackupsResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSearchJobResultsInput

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSearchJobResultsInputPaginate

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.PaginatorConfig]


# ListSearchJobResultsOutput

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSearchJobsInput

### ByStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'STOPPED', 'STOPPING']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSearchJobsInputPaginate

### ByStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'STOPPED', 'STOPPING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.PaginatorConfig]


# ListSearchJobsOutput

### SearchJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.SearchJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSearchResultExportJobsInput

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING']]

### SearchJobIdentifier
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSearchResultExportJobsInputPaginate

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING']]

### SearchJobIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.PaginatorConfig]


# ListSearchResultExportJobsOutput

### ExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes


# LongCondition

### Value
- **Type**: <class 'int'>
- **Required**: Yes

### Operator
- **Type**: typing.Optional[typing.Literal['EQUALS_TO', 'GREATER_THAN_EQUAL_TO', 'LESS_THAN_EQUAL_TO', 'NOT_EQUALS_TO']]


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


# ResultItem

### S3ResultItem
- **Type**: <class 'NoneType'>

### EBSResultItem
- **Type**: <class 'NoneType'>


# S3ExportSpecification

### DestinationBucket
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPrefix
- **Type**: typing.Optional[str]


# S3ItemFilter

### ObjectKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.StringCondition]]

### Sizes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.LongCondition]]

### CreationTimes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.TimeCondition]]

### VersionIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.StringCondition]]

### ETags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.StringCondition]]


# S3ItemFilterOutput

### ObjectKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.StringCondition]]

### Sizes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.LongCondition]]

### CreationTimes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.TimeConditionOutput]]

### VersionIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.StringCondition]]

### ETags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.StringCondition]]


# S3ResultItem

### BackupResourceArn
- **Type**: typing.Optional[str]

### SourceResourceArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### ObjectKey
- **Type**: typing.Optional[str]

### ObjectSize
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ETag
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# SearchJobBackupsResult

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'STOPPED', 'STOPPING']]

### StatusMessage
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EBS', 'S3']]

### BackupResourceArn
- **Type**: typing.Optional[str]

### SourceResourceArn
- **Type**: typing.Optional[str]

### IndexCreationTime
- **Type**: typing.Optional[datetime.datetime]

### BackupCreationTime
- **Type**: typing.Optional[datetime.datetime]


# SearchJobSummary

### SearchJobIdentifier
- **Type**: typing.Optional[str]

### SearchJobArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'RUNNING', 'STOPPED', 'STOPPING']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### SearchScopeSummary
- **Type**: <class 'NoneType'>

### StatusMessage
- **Type**: typing.Optional[str]


# SearchScope

### BackupResourceTypes
- **Type**: typing.List[typing.Literal['EBS', 'S3']]
- **Required**: Yes

### BackupResourceCreationTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.BackupCreationTimeFilter]

### SourceResourceArns
- **Type**: typing.Optional[typing.List[str]]

### BackupResourceArns
- **Type**: typing.Optional[typing.List[str]]

### BackupResourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SearchScopeOutput

### BackupResourceTypes
- **Type**: typing.List[typing.Literal['EBS', 'S3']]
- **Required**: Yes

### BackupResourceCreationTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.BackupCreationTimeFilterOutput]

### SourceResourceArns
- **Type**: typing.Optional[typing.List[str]]

### BackupResourceArns
- **Type**: typing.Optional[typing.List[str]]

### BackupResourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SearchScopeSummary

### TotalRecoveryPointsToScanCount
- **Type**: typing.Optional[int]

### TotalItemsToScanCount
- **Type**: typing.Optional[int]


# StartSearchJobInput

### SearchScope
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.SearchScope, aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.SearchScopeOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Name
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### ItemFilters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ItemFilters, aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ItemFiltersOutput, NoneType]


# StartSearchJobOutput

### SearchJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes


# StartSearchResultExportJobInput

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExportSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ExportSpecification'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RoleArn
- **Type**: typing.Optional[str]


# StartSearchResultExportJobOutput

### ExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExportJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backupsearch.backupsearch_classes.ResponseMetadata'>
- **Required**: Yes


# StopSearchJobInput

### SearchJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StringCondition

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'CONTAINS', 'DOES_NOT_BEGIN_WITH', 'DOES_NOT_CONTAIN', 'DOES_NOT_END_WITH', 'ENDS_WITH', 'EQUALS_TO', 'NOT_EQUALS_TO']]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TimeCondition

### Value
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Operator
- **Type**: typing.Optional[typing.Literal['EQUALS_TO', 'GREATER_THAN_EQUAL_TO', 'LESS_THAN_EQUAL_TO', 'NOT_EQUALS_TO']]


# TimeConditionOutput

### Value
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Operator
- **Type**: typing.Optional[typing.Literal['EQUALS_TO', 'GREATER_THAN_EQUAL_TO', 'LESS_THAN_EQUAL_TO', 'NOT_EQUALS_TO']]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


