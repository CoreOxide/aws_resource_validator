# Lakeformation Classes

# AddLFTagsToResourceRequest

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]
- **Required**: Yes

### LFTags
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPair, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# AddLFTagsToResourceResponse

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# AddObjectInput

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### PartitionValues
- **Type**: typing.Optional[typing.List[str]]


# AssumeDecoratedRoleWithSAMLRequest

### SAMLAssertion
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalArn
- **Type**: <class 'str'>
- **Required**: Yes

### DurationSeconds
- **Type**: typing.Optional[int]


# AssumeDecoratedRoleWithSAMLResponse

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### SessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# AuditContext

### AdditionalAuditContext
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGrantPermissionsRequest

### Entries
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.BatchPermissionsRequestEntry, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.BatchPermissionsRequestEntryOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchGrantPermissionsResponse

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.BatchPermissionsFailureEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPermissionsFailureEntry

### RequestEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.BatchPermissionsRequestEntryOutput]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ErrorDetail]


# BatchPermissionsRequestEntry

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput, NoneType]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# BatchPermissionsRequestEntryOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# BatchRevokePermissionsRequest

### Entries
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.BatchPermissionsRequestEntry, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.BatchPermissionsRequestEntryOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchRevokePermissionsResponse

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.BatchPermissionsFailureEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# CancelTransactionRequest

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes


# CatalogResource

### Id
- **Type**: typing.Optional[str]


# ColumnLFTag

### Name
- **Type**: typing.Optional[str]

### LFTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]]


# ColumnWildcard

### ExcludedColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnWildcardOutput

### ExcludedColumnNames
- **Type**: typing.Optional[typing.List[str]]


# CommitTransactionRequest

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes


# CommitTransactionResponse

### TransactionStatus
- **Type**: typing.Literal['ABORTED', 'ACTIVE', 'COMMITTED', 'COMMIT_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# Condition

### Expression
- **Type**: typing.Optional[str]


# CreateDataCellsFilterRequest

### TableData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataCellsFilter, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataCellsFilterOutput]
- **Required**: Yes


# CreateLFTagExpressionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTag, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]


# CreateLFTagRequest

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreateLakeFormationIdentityCenterConfigurationRequest

### CatalogId
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### ExternalFiltering
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ExternalFilteringConfiguration, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ExternalFilteringConfigurationOutput, NoneType]

### ShareRecipients
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]]


# CreateLakeFormationIdentityCenterConfigurationResponse

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLakeFormationOptInRequest

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal'>
- **Required**: Yes

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]
- **Required**: Yes


# DataCellsFilter

### TableCatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RowFilter
- **Type**: <class 'NoneType'>

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]

### ColumnWildcard
- **Type**: <class 'NoneType'>

### VersionId
- **Type**: typing.Optional[str]


# DataCellsFilterOutput

### TableCatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RowFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.RowFilterOutput]

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]

### ColumnWildcard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ColumnWildcardOutput]

### VersionId
- **Type**: typing.Optional[str]


# DataCellsFilterResource

### TableCatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DataLakePrincipal

### DataLakePrincipalIdentifier
- **Type**: typing.Optional[str]


# DataLakeSettings

### DataLakeAdmins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]]

### ReadOnlyAdmins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]]

### CreateDatabaseDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PrincipalPermissions]]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PrincipalPermissions]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TrustedResourceOwners
- **Type**: typing.Optional[typing.List[str]]

### AllowExternalDataFiltering
- **Type**: typing.Optional[bool]

### AllowFullTableExternalDataAccess
- **Type**: typing.Optional[bool]

### ExternalDataFilteringAllowList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]]

### AuthorizedSessionTagValueList
- **Type**: typing.Optional[typing.List[str]]


# DataLakeSettingsOutput

### DataLakeAdmins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]]

### ReadOnlyAdmins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]]

### CreateDatabaseDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PrincipalPermissionsOutput]]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PrincipalPermissionsOutput]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TrustedResourceOwners
- **Type**: typing.Optional[typing.List[str]]

### AllowExternalDataFiltering
- **Type**: typing.Optional[bool]

### AllowFullTableExternalDataAccess
- **Type**: typing.Optional[bool]

### ExternalDataFilteringAllowList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]]

### AuthorizedSessionTagValueList
- **Type**: typing.Optional[typing.List[str]]


# DataLocationResource

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DatabaseResource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteDataCellsFilterRequest

### TableCatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DeleteLFTagExpressionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteLFTagRequest

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteLakeFormationIdentityCenterConfigurationRequest

### CatalogId
- **Type**: typing.Optional[str]


# DeleteLakeFormationOptInRequest

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal'>
- **Required**: Yes

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]
- **Required**: Yes


# DeleteObjectInput

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]

### PartitionValues
- **Type**: typing.Optional[typing.List[str]]


# DeleteObjectsOnCancelRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### Objects
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.VirtualObject]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeregisterResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLakeFormationIdentityCenterConfigurationRequest

### CatalogId
- **Type**: typing.Optional[str]


# DescribeLakeFormationIdentityCenterConfigurationResponse

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalFiltering
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ExternalFilteringConfigurationOutput'>
- **Required**: Yes

### ShareRecipients
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]
- **Required**: Yes

### ResourceShare
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourceResponse

### ResourceInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTransactionRequest

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTransactionResponse

### TransactionDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TransactionDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# DetailsMap

### ResourceShare
- **Type**: typing.Optional[typing.List[str]]


# ErrorDetail

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# ExecutionStatistics

### AverageExecutionTimeMillis
- **Type**: typing.Optional[int]

### DataScannedBytes
- **Type**: typing.Optional[int]

### WorkUnitsExecutedCount
- **Type**: typing.Optional[int]


# ExtendTransactionRequest

### TransactionId
- **Type**: typing.Optional[str]


# ExternalFilteringConfiguration

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.List[str]
- **Required**: Yes


# ExternalFilteringConfigurationOutput

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.List[str]
- **Required**: Yes


# FilterCondition

### Field
- **Type**: typing.Optional[typing.Literal['LAST_MODIFIED', 'RESOURCE_ARN', 'ROLE_ARN']]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'EQ', 'GE', 'GT', 'IN', 'LE', 'LT', 'NE', 'NOT_CONTAINS']]

### StringValueList
- **Type**: typing.Optional[typing.List[str]]


# GetDataCellsFilterRequest

### TableCatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataCellsFilterResponse

### DataCellsFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataCellsFilterOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataLakePrincipalResponse

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataLakeSettingsRequest

### CatalogId
- **Type**: typing.Optional[str]


# GetDataLakeSettingsResponse

### DataLakeSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakeSettingsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetEffectivePermissionsForPathRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetEffectivePermissionsForPathResponse

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PrincipalResourcePermissions]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLFTagExpressionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetLFTagExpressionResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetLFTagRequest

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetLFTagResponse

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryStateRequest

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStateResponse

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ERROR', 'EXPIRED', 'FINISHED', 'PENDING', 'WORKUNITS_AVAILABLE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryStatisticsRequest

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStatisticsResponse

### ExecutionStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ExecutionStatistics'>
- **Required**: Yes

### PlanningStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PlanningStatistics'>
- **Required**: Yes

### QuerySubmissionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceLFTagsRequest

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### ShowAssignedLFTags
- **Type**: typing.Optional[bool]


# GetResourceLFTagsResponse

### LFTagOnDatabase
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]
- **Required**: Yes

### LFTagsOnTable
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]
- **Required**: Yes

### LFTagsOnColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ColumnLFTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableObjectsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PartitionPredicate
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetTableObjectsResponse

### Objects
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PartitionObjects]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTemporaryGluePartitionCredentialsRequest

### TableArn
- **Type**: <class 'str'>
- **Required**: Yes

### Partition
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PartitionValueList'>
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### DurationSeconds
- **Type**: typing.Optional[int]

### AuditContext
- **Type**: <class 'NoneType'>

### SupportedPermissionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]]


# GetTemporaryGluePartitionCredentialsResponse

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### SessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemporaryGlueTableCredentialsRequest

### TableArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### DurationSeconds
- **Type**: typing.Optional[int]

### AuditContext
- **Type**: <class 'NoneType'>

### SupportedPermissionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]]

### S3Path
- **Type**: typing.Optional[str]

### QuerySessionContext
- **Type**: <class 'NoneType'>


# GetTemporaryGlueTableCredentialsResponse

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### SessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VendedS3Path
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkUnitResultsRequest

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkUnitId
- **Type**: <class 'int'>
- **Required**: Yes

### WorkUnitToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkUnitResultsResponse

### ResultStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkUnitsRequest

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# GetWorkUnitsRequestPaginate

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PaginatorConfig]


# GetWorkUnitsResponse

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkUnitRanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.WorkUnitRange]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GrantPermissionsRequest

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal'>
- **Required**: Yes

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# LFTag

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# LFTagError

### LFTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ErrorDetail]


# LFTagExpression

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]


# LFTagExpressionResource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagKeyResource

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagKeyResourceOutput

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagOutput

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# LFTagPair

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagPairOutput

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagPolicyResource

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTag, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]]

### ExpressionName
- **Type**: typing.Optional[str]


# LFTagPolicyResourceOutput

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]

### ExpressionName
- **Type**: typing.Optional[str]


# LakeFormationOptInsInfo

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]

### Condition
- **Type**: <class 'NoneType'>

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedBy
- **Type**: typing.Optional[str]


# ListDataCellsFilterRequest

### Table
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableResource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableResourceOutput, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataCellsFilterRequestPaginate

### Table
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableResource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableResourceOutput, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PaginatorConfig]


# ListDataCellsFilterResponse

### DataCellsFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataCellsFilterOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLFTagExpressionsRequest

### CatalogId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLFTagExpressionsRequestPaginate

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PaginatorConfig]


# ListLFTagExpressionsResponse

### LFTagExpressions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagExpression]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLFTagsRequest

### CatalogId
- **Type**: typing.Optional[str]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FOREIGN']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLFTagsRequestPaginate

### CatalogId
- **Type**: typing.Optional[str]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FOREIGN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PaginatorConfig]


# ListLFTagsResponse

### LFTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLakeFormationOptInsRequest

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLakeFormationOptInsResponse

### LakeFormationOptInsInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LakeFormationOptInsInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionsRequest

### CatalogId
- **Type**: typing.Optional[str]

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]

### ResourceType
- **Type**: typing.Optional[typing.Literal['CATALOG', 'DATABASE', 'DATA_LOCATION', 'LF_NAMED_TAG_EXPRESSION', 'LF_TAG', 'LF_TAG_POLICY', 'LF_TAG_POLICY_DATABASE', 'LF_TAG_POLICY_TABLE', 'TABLE']]

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeRelated
- **Type**: typing.Optional[str]


# ListPermissionsResponse

### PrincipalResourcePermissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PrincipalResourcePermissions]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesRequest

### FilterConditionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.FilterCondition]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesResponse

### ResourceInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTableStorageOptimizersRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### StorageOptimizerType
- **Type**: typing.Optional[typing.Literal['ALL', 'COMPACTION', 'GARBAGE_COLLECTION']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTableStorageOptimizersResponse

### StorageOptimizerList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.StorageOptimizer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTransactionsRequest

### CatalogId
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ACTIVE', 'ALL', 'COMMITTED', 'COMPLETED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTransactionsResponse

### Transactions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TransactionDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartitionObjects

### PartitionValues
- **Type**: typing.Optional[typing.List[str]]

### Objects
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableObject]]


# PartitionValueList

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# PlanningStatistics

### EstimatedDataToScanBytes
- **Type**: typing.Optional[int]

### PlanningTimeMillis
- **Type**: typing.Optional[int]

### QueueTimeMillis
- **Type**: typing.Optional[int]

### WorkUnitsGeneratedCount
- **Type**: typing.Optional[int]


# PrincipalPermissions

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# PrincipalPermissionsOutput

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# PrincipalResourcePermissions

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]

### Condition
- **Type**: <class 'NoneType'>

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### AdditionalDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DetailsMap]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedBy
- **Type**: typing.Optional[str]


# PutDataLakeSettingsRequest

### DataLakeSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakeSettings, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakeSettingsOutput]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# QueryPlanningContext

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### QueryParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TransactionId
- **Type**: typing.Optional[str]


# QuerySessionContext

### QueryId
- **Type**: typing.Optional[str]

### QueryStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ClusterId
- **Type**: typing.Optional[str]

### QueryAuthorizationId
- **Type**: typing.Optional[str]

### AdditionalContext
- **Type**: typing.Optional[typing.Dict[str, str]]


# RegisterResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### UseServiceLinkedRole
- **Type**: typing.Optional[bool]

### RoleArn
- **Type**: typing.Optional[str]

### WithFederation
- **Type**: typing.Optional[bool]

### HybridAccessEnabled
- **Type**: typing.Optional[bool]


# RemoveLFTagsFromResourceRequest

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]
- **Required**: Yes

### LFTags
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPair, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# RemoveLFTagsFromResourceResponse

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# Resource

### Catalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.CatalogResource]

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DatabaseResource]

### Table
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableResource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableResourceOutput, NoneType]

### TableWithColumns
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableWithColumnsResource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableWithColumnsResourceOutput, NoneType]

### DataLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLocationResource]

### DataCellsFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataCellsFilterResource]

### LFTag
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagKeyResource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagKeyResourceOutput, NoneType]

### LFTagPolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPolicyResource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPolicyResourceOutput, NoneType]

### LFTagExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagExpressionResource]


# ResourceInfo

### ResourceArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### WithFederation
- **Type**: typing.Optional[bool]

### HybridAccessEnabled
- **Type**: typing.Optional[bool]


# ResourceOutput

### Catalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.CatalogResource]

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DatabaseResource]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableResourceOutput]

### TableWithColumns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableWithColumnsResourceOutput]

### DataLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLocationResource]

### DataCellsFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataCellsFilterResource]

### LFTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagKeyResourceOutput]

### LFTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPolicyResourceOutput]

### LFTagExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagExpressionResource]


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


# RevokePermissionsRequest

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal'>
- **Required**: Yes

### Resource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.Resource, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResourceOutput]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# RowFilter

### FilterExpression
- **Type**: typing.Optional[str]

### AllRowsWildcard
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# RowFilterOutput

### FilterExpression
- **Type**: typing.Optional[str]

### AllRowsWildcard
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# SearchDatabasesByLFTagsRequest

### Expression
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTag, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CatalogId
- **Type**: typing.Optional[str]


# SearchDatabasesByLFTagsRequestPaginate

### Expression
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTag, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PaginatorConfig]


# SearchDatabasesByLFTagsResponse

### DatabaseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TaggedDatabase]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchTablesByLFTagsRequest

### Expression
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTag, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CatalogId
- **Type**: typing.Optional[str]


# SearchTablesByLFTagsRequestPaginate

### Expression
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTag, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.PaginatorConfig]


# SearchTablesByLFTagsResponse

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TaggedTable]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StartQueryPlanningRequest

### QueryPlanningContext
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.QueryPlanningContext'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes


# StartQueryPlanningResponse

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# StartTransactionRequest

### TransactionType
- **Type**: typing.Optional[typing.Literal['READ_AND_WRITE', 'READ_ONLY']]


# StartTransactionResponse

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# StorageOptimizer

### StorageOptimizerType
- **Type**: typing.Optional[typing.Literal['ALL', 'COMPACTION', 'GARBAGE_COLLECTION']]

### Config
- **Type**: typing.Optional[typing.Dict[str, str]]

### ErrorMessage
- **Type**: typing.Optional[str]

### Warnings
- **Type**: typing.Optional[str]

### LastRunDetails
- **Type**: typing.Optional[str]


# TableObject

### Uri
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### Size
- **Type**: typing.Optional[int]


# TableResource

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### TableWildcard
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TableResourceOutput

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### TableWildcard
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TableWithColumnsResource

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]

### ColumnWildcard
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ColumnWildcard, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ColumnWildcardOutput, NoneType]


# TableWithColumnsResourceOutput

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]

### ColumnWildcard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ColumnWildcardOutput]


# TaggedDatabase

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DatabaseResource]

### LFTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]]


# TaggedTable

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.TableResourceOutput]

### LFTagOnDatabase
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]]

### LFTagsOnTable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagPairOutput]]

### LFTagsOnColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ColumnLFTag]]


# TransactionDescription

### TransactionId
- **Type**: typing.Optional[str]

### TransactionStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ACTIVE', 'COMMITTED', 'COMMIT_IN_PROGRESS']]

### TransactionStartTime
- **Type**: typing.Optional[datetime.datetime]

### TransactionEndTime
- **Type**: typing.Optional[datetime.datetime]


# UpdateDataCellsFilterRequest

### TableData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataCellsFilter, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataCellsFilterOutput]
- **Required**: Yes


# UpdateLFTagExpressionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTag, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.LFTagOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]


# UpdateLFTagRequest

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TagValuesToDelete
- **Type**: typing.Optional[typing.List[str]]

### TagValuesToAdd
- **Type**: typing.Optional[typing.List[str]]


# UpdateLakeFormationIdentityCenterConfigurationRequest

### CatalogId
- **Type**: typing.Optional[str]

### ShareRecipients
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DataLakePrincipal]]

### ApplicationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ExternalFiltering
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ExternalFilteringConfiguration, aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ExternalFilteringConfigurationOutput, NoneType]


# UpdateResourceRequest

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### WithFederation
- **Type**: typing.Optional[bool]

### HybridAccessEnabled
- **Type**: typing.Optional[bool]


# UpdateTableObjectsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### WriteOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.WriteOperation]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]


# UpdateTableStorageOptimizerRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### StorageOptimizerConfig
- **Type**: typing.Dict[typing.Literal['ALL', 'COMPACTION', 'GARBAGE_COLLECTION'], typing.Dict[str, str]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateTableStorageOptimizerResponse

### Result
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.ResponseMetadata'>
- **Required**: Yes


# VirtualObject

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]


# WorkUnitRange

### WorkUnitIdMax
- **Type**: <class 'int'>
- **Required**: Yes

### WorkUnitIdMin
- **Type**: <class 'int'>
- **Required**: Yes

### WorkUnitToken
- **Type**: <class 'str'>
- **Required**: Yes


# WriteOperation

### AddObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.AddObjectInput]

### DeleteObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation.lakeformation_classes.DeleteObjectInput]


