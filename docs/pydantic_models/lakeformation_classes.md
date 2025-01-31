# Lakeformation Classes

# AddLFTagsToResourceRequestRequestTypeDef

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef'>
- **Required**: Yes

### LFTags
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairTypeDef, aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairExtraOutputTypeDef]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# AddLFTagsToResourceResponseTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddObjectInputTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]


# AssumeDecoratedRoleWithSAMLRequestRequestTypeDef

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


# AssumeDecoratedRoleWithSAMLResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuditContextTypeDef

### AdditionalAuditContext
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGrantPermissionsRequestRequestTypeDef

### Entries
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsRequestEntryTypeDef, aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsRequestEntryOutputTypeDef]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchGrantPermissionsResponseTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsFailureEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPermissionsFailureEntryTypeDef

### RequestEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsRequestEntryOutputTypeDef]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ErrorDetailTypeDef]


# BatchPermissionsRequestEntryOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceOutputTypeDef]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]


# BatchPermissionsRequestEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef]

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]


# BatchRevokePermissionsRequestRequestTypeDef

### Entries
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsRequestEntryTypeDef, aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsRequestEntryOutputTypeDef]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# BatchRevokePermissionsResponseTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsFailureEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelTransactionRequestRequestTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes


# ColumnLFTagTypeDef

### Name
- **Type**: typing.Optional[str]

### LFTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]]


# ColumnWildcardExtraOutputTypeDef

### ExcludedColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnWildcardOutputTypeDef

### ExcludedColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnWildcardTypeDef

### ExcludedColumnNames
- **Type**: typing.Optional[typing.Sequence[str]]


# CommitTransactionRequestRequestTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes


# CommitTransactionResponseTypeDef

### TransactionStatus
- **Type**: typing.Literal['ABORTED', 'ACTIVE', 'COMMITTED', 'COMMIT_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataCellsFilterRequestRequestTypeDef

### TableData
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterTypeDef'>
- **Required**: Yes


# CreateLFTagRequestRequestTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### ExternalFiltering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ExternalFilteringConfigurationTypeDef]

### ShareRecipients
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]


# CreateLakeFormationIdentityCenterConfigurationResponseTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLakeFormationOptInRequestRequestTypeDef

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef'>
- **Required**: Yes


# DataCellsFilterExtraOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.RowFilterExtraOutputTypeDef]

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]

### ColumnWildcard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ColumnWildcardExtraOutputTypeDef]

### VersionId
- **Type**: typing.Optional[str]


# DataCellsFilterOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.RowFilterOutputTypeDef]

### ColumnNames
- **Type**: typing.Optional[typing.List[str]]

### ColumnWildcard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ColumnWildcardOutputTypeDef]

### VersionId
- **Type**: typing.Optional[str]


# DataCellsFilterResourceTypeDef

### TableCatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DataCellsFilterTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.RowFilterTypeDef]

### ColumnNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ColumnWildcard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ColumnWildcardTypeDef]

### VersionId
- **Type**: typing.Optional[str]


# DataLakePrincipalTypeDef

### DataLakePrincipalIdentifier
- **Type**: typing.Optional[str]


# DataLakeSettingsOutputTypeDef

### DataLakeAdmins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]

### ReadOnlyAdmins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]

### CreateDatabaseDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.PrincipalPermissionsOutputTypeDef]]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.PrincipalPermissionsOutputTypeDef]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TrustedResourceOwners
- **Type**: typing.Optional[typing.List[str]]

### AllowExternalDataFiltering
- **Type**: typing.Optional[bool]

### AllowFullTableExternalDataAccess
- **Type**: typing.Optional[bool]

### ExternalDataFilteringAllowList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]

### AuthorizedSessionTagValueList
- **Type**: typing.Optional[typing.List[str]]


# DataLakeSettingsTypeDef

### DataLakeAdmins
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]

### ReadOnlyAdmins
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]

### CreateDatabaseDefaultPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.PrincipalPermissionsTypeDef]]

### CreateTableDefaultPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.PrincipalPermissionsTypeDef]]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TrustedResourceOwners
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowExternalDataFiltering
- **Type**: typing.Optional[bool]

### AllowFullTableExternalDataAccess
- **Type**: typing.Optional[bool]

### ExternalDataFilteringAllowList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]

### AuthorizedSessionTagValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# DataLocationResourceTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DatabaseResourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteDataCellsFilterRequestRequestTypeDef

### TableCatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DeleteLFTagRequestRequestTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]


# DeleteLakeFormationOptInRequestRequestTypeDef

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef'>
- **Required**: Yes


# DeleteObjectInputTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]

### PartitionValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DeleteObjectsOnCancelRequestRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.VirtualObjectTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeregisterResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]


# DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ExternalFilteringConfigurationOutputTypeDef'>
- **Required**: Yes

### ShareRecipients
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]
- **Required**: Yes

### ResourceShare
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourceResponseTypeDef

### ResourceInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTransactionRequestRequestTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTransactionResponseTypeDef

### TransactionDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.TransactionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetailsMapTypeDef

### ResourceShare
- **Type**: typing.Optional[typing.List[str]]


# ErrorDetailTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# ExecutionStatisticsTypeDef

### AverageExecutionTimeMillis
- **Type**: typing.Optional[int]

### DataScannedBytes
- **Type**: typing.Optional[int]

### WorkUnitsExecutedCount
- **Type**: typing.Optional[int]


# ExtendTransactionRequestRequestTypeDef

### TransactionId
- **Type**: typing.Optional[str]


# ExternalFilteringConfigurationOutputTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.List[str]
- **Required**: Yes


# ExternalFilteringConfigurationTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FilterConditionTypeDef

### Field
- **Type**: typing.Optional[typing.Literal['LAST_MODIFIED', 'RESOURCE_ARN', 'ROLE_ARN']]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'EQ', 'GE', 'GT', 'IN', 'LE', 'LT', 'NE', 'NOT_CONTAINS']]

### StringValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# GetDataCellsFilterRequestRequestTypeDef

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


# GetDataCellsFilterResponseTypeDef

### DataCellsFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataLakePrincipalResponseTypeDef

### Identity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataLakeSettingsRequestRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]


# GetDataLakeSettingsResponseTypeDef

### DataLakeSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakeSettingsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEffectivePermissionsForPathRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetEffectivePermissionsForPathResponseTypeDef

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.PrincipalResourcePermissionsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLFTagRequestRequestTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetLFTagResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryStateRequestRequestTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStateResponseTypeDef

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ERROR', 'EXPIRED', 'FINISHED', 'PENDING', 'WORKUNITS_AVAILABLE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryStatisticsRequestRequestTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStatisticsResponseTypeDef

### ExecutionStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ExecutionStatisticsTypeDef'>
- **Required**: Yes

### PlanningStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.PlanningStatisticsTypeDef'>
- **Required**: Yes

### QuerySubmissionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceLFTagsRequestRequestTypeDef

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### ShowAssignedLFTags
- **Type**: typing.Optional[bool]


# GetResourceLFTagsResponseTypeDef

### LFTagOnDatabase
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]
- **Required**: Yes

### LFTagsOnTable
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]
- **Required**: Yes

### LFTagsOnColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.ColumnLFTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableObjectsRequestRequestTypeDef

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


# GetTableObjectsResponseTypeDef

### Objects
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.PartitionObjectsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTemporaryGluePartitionCredentialsRequestRequestTypeDef

### TableArn
- **Type**: <class 'str'>
- **Required**: Yes

### Partition
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.PartitionValueListTypeDef'>
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]

### DurationSeconds
- **Type**: typing.Optional[int]

### AuditContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.AuditContextTypeDef]

### SupportedPermissionTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]]


# GetTemporaryGluePartitionCredentialsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemporaryGlueTableCredentialsRequestRequestTypeDef

### TableArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]

### DurationSeconds
- **Type**: typing.Optional[int]

### AuditContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.AuditContextTypeDef]

### SupportedPermissionTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CELL_FILTER_PERMISSION', 'COLUMN_PERMISSION', 'NESTED_CELL_PERMISSION', 'NESTED_PERMISSION']]]

### S3Path
- **Type**: typing.Optional[str]

### QuerySessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.QuerySessionContextTypeDef]


# GetTemporaryGlueTableCredentialsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkUnitResultsRequestRequestTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkUnitId
- **Type**: <class 'int'>
- **Required**: Yes

### WorkUnitToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkUnitResultsResponseTypeDef

### ResultStream
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# GetWorkUnitsRequestRequestTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# GetWorkUnitsResponseTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkUnitRanges
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.WorkUnitRangeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GrantPermissionsRequestRequestTypeDef

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef'>
- **Required**: Yes

### Permissions
- **Type**: typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]


# LFTagErrorTypeDef

### LFTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ErrorDetailTypeDef]


# LFTagKeyResourceOutputTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagKeyResourceTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagOutputTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# LFTagPairExtraOutputTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagPairOutputTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagPairTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagPolicyResourceOutputTypeDef

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagOutputTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagPolicyResourceTypeDef

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# LakeFormationOptInsInfoTypeDef

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceOutputTypeDef]

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedBy
- **Type**: typing.Optional[str]


# ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableResourceTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# ListDataCellsFilterRequestRequestTypeDef

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableResourceTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataCellsFilterResponseTypeDef

### DataCellsFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLFTagsRequestListLFTagsPaginateTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FOREIGN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# ListLFTagsRequestRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FOREIGN']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLFTagsResponseTypeDef

### LFTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLakeFormationOptInsRequestRequestTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLakeFormationOptInsResponseTypeDef

### LakeFormationOptInsInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LakeFormationOptInsInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionsRequestRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### ResourceType
- **Type**: typing.Optional[typing.Literal['CATALOG', 'DATABASE', 'DATA_LOCATION', 'LF_TAG', 'LF_TAG_POLICY', 'LF_TAG_POLICY_DATABASE', 'LF_TAG_POLICY_TABLE', 'TABLE']]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeRelated
- **Type**: typing.Optional[str]


# ListPermissionsResponseTypeDef

### PrincipalResourcePermissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.PrincipalResourcePermissionsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesRequestRequestTypeDef

### FilterConditionList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.FilterConditionTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesResponseTypeDef

### ResourceInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTableStorageOptimizersRequestRequestTypeDef

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


# ListTableStorageOptimizersResponseTypeDef

### StorageOptimizerList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.StorageOptimizerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTransactionsRequestRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ACTIVE', 'ALL', 'COMMITTED', 'COMPLETED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTransactionsResponseTypeDef

### Transactions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.TransactionDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartitionObjectsTypeDef

### PartitionValues
- **Type**: typing.Optional[typing.List[str]]

### Objects
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.TableObjectTypeDef]]


# PartitionValueListTypeDef

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PlanningStatisticsTypeDef

### EstimatedDataToScanBytes
- **Type**: typing.Optional[int]

### PlanningTimeMillis
- **Type**: typing.Optional[int]

### QueueTimeMillis
- **Type**: typing.Optional[int]

### WorkUnitsGeneratedCount
- **Type**: typing.Optional[int]


# PrincipalPermissionsOutputTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]


# PrincipalPermissionsTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]


# PrincipalResourcePermissionsTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceOutputTypeDef]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]

### AdditionalDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DetailsMapTypeDef]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedBy
- **Type**: typing.Optional[str]


# PutDataLakeSettingsRequestRequestTypeDef

### DataLakeSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakeSettingsTypeDef'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# QueryPlanningContextTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### QueryAsOfTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### QueryParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TransactionId
- **Type**: typing.Optional[str]


# QuerySessionContextTypeDef

### QueryId
- **Type**: typing.Optional[str]

### QueryStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ClusterId
- **Type**: typing.Optional[str]

### QueryAuthorizationId
- **Type**: typing.Optional[str]

### AdditionalContext
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterResourceRequestRequestTypeDef

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


# RemoveLFTagsFromResourceRequestRequestTypeDef

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef'>
- **Required**: Yes

### LFTags
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairTypeDef, aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairExtraOutputTypeDef]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# RemoveLFTagsFromResourceResponseTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceInfoTypeDef

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


# ResourceOutputTypeDef

### Catalog
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DatabaseResourceTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableResourceOutputTypeDef]

### TableWithColumns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableWithColumnsResourceOutputTypeDef]

### DataLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLocationResourceTypeDef]

### DataCellsFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterResourceTypeDef]

### LFTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagKeyResourceOutputTypeDef]

### LFTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPolicyResourceOutputTypeDef]


# ResourceTypeDef

### Catalog
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DatabaseResourceTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableResourceTypeDef]

### TableWithColumns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableWithColumnsResourceTypeDef]

### DataLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLocationResourceTypeDef]

### DataCellsFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterResourceTypeDef]

### LFTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagKeyResourceTypeDef]

### LFTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPolicyResourceTypeDef]


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


# RevokePermissionsRequestRequestTypeDef

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceTypeDef'>
- **Required**: Yes

### Permissions
- **Type**: typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT']]]


# RowFilterExtraOutputTypeDef

### FilterExpression
- **Type**: typing.Optional[str]

### AllRowsWildcard
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# RowFilterOutputTypeDef

### FilterExpression
- **Type**: typing.Optional[str]

### AllRowsWildcard
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# RowFilterTypeDef

### FilterExpression
- **Type**: typing.Optional[str]

### AllRowsWildcard
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# SearchDatabasesByLFTagsRequestRequestTypeDef

### Expression
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagTypeDef, aws_resource_validator.pydantic_models.lakeformation_classes.LFTagOutputTypeDef]]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CatalogId
- **Type**: typing.Optional[str]


# SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef

### Expression
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagTypeDef, aws_resource_validator.pydantic_models.lakeformation_classes.LFTagOutputTypeDef]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# SearchDatabasesByLFTagsResponseTypeDef

### DatabaseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.TaggedDatabaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchTablesByLFTagsRequestRequestTypeDef

### Expression
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagTypeDef, aws_resource_validator.pydantic_models.lakeformation_classes.LFTagOutputTypeDef]]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CatalogId
- **Type**: typing.Optional[str]


# SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef

### Expression
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagTypeDef, aws_resource_validator.pydantic_models.lakeformation_classes.LFTagOutputTypeDef]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# SearchTablesByLFTagsResponseTypeDef

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.TaggedTableTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StartQueryPlanningRequestRequestTypeDef

### QueryPlanningContext
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.QueryPlanningContextTypeDef'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes


# StartQueryPlanningResponseTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTransactionRequestRequestTypeDef

### TransactionType
- **Type**: typing.Optional[typing.Literal['READ_AND_WRITE', 'READ_ONLY']]


# StartTransactionResponseTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StorageOptimizerTypeDef

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


# TableObjectTypeDef

### Uri
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### Size
- **Type**: typing.Optional[int]


# TableResourceExtraOutputTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### TableWildcard
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TableResourceOutputTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### TableWildcard
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TableResourceTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### TableWildcard
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# TableWithColumnsResourceOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ColumnWildcardOutputTypeDef]


# TableWithColumnsResourceTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### ColumnNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ColumnWildcard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ColumnWildcardTypeDef]


# TaggedDatabaseTypeDef

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DatabaseResourceTypeDef]

### LFTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]]


# TaggedTableTypeDef

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableResourceOutputTypeDef]

### LFTagOnDatabase
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]]

### LFTagsOnTable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]]

### LFTagsOnColumns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.ColumnLFTagTypeDef]]


# TransactionDescriptionTypeDef

### TransactionId
- **Type**: typing.Optional[str]

### TransactionStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ACTIVE', 'COMMITTED', 'COMMIT_IN_PROGRESS']]

### TransactionStartTime
- **Type**: typing.Optional[datetime.datetime]

### TransactionEndTime
- **Type**: typing.Optional[datetime.datetime]


# UpdateDataCellsFilterRequestRequestTypeDef

### TableData
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterTypeDef'>
- **Required**: Yes


# UpdateLFTagRequestRequestTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TagValuesToDelete
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValuesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### ShareRecipients
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]

### ApplicationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ExternalFiltering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ExternalFilteringConfigurationTypeDef]


# UpdateResourceRequestRequestTypeDef

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


# UpdateTableObjectsRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### WriteOperations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.WriteOperationTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TransactionId
- **Type**: typing.Optional[str]


# UpdateTableStorageOptimizerRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### StorageOptimizerConfig
- **Type**: typing.Mapping[typing.Literal['ALL', 'COMPACTION', 'GARBAGE_COLLECTION'], typing.Mapping[str, str]]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# UpdateTableStorageOptimizerResponseTypeDef

### Result
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VirtualObjectTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]


# WorkUnitRangeTypeDef

### WorkUnitIdMax
- **Type**: <class 'int'>
- **Required**: Yes

### WorkUnitIdMin
- **Type**: <class 'int'>
- **Required**: Yes

### WorkUnitToken
- **Type**: <class 'str'>
- **Required**: Yes


# WriteOperationTypeDef

### AddObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.AddObjectInputTypeDef]

### DeleteObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DeleteObjectInputTypeDef]


