# Lakeformation Classes

# AddLFTagsToResourceRequestTypeDef

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef'>
- **Required**: Yes

### LFTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairUnionTypeDef]
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


# AssumeDecoratedRoleWithSAMLRequestTypeDef

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

# BatchGrantPermissionsRequestTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsRequestEntryUnionTypeDef]
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
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# BatchPermissionsRequestEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef]

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# BatchPermissionsRequestEntryUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchRevokePermissionsRequestTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.BatchPermissionsRequestEntryUnionTypeDef]
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


# CancelTransactionRequestTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes


# CatalogResourceTypeDef

### Id
- **Type**: typing.Optional[str]


# ColumnLFTagTypeDef

### Name
- **Type**: typing.Optional[str]

### LFTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]]


# ColumnWildcardOutputTypeDef

### ExcludedColumnNames
- **Type**: typing.Optional[typing.List[str]]


# ColumnWildcardTypeDef

### ExcludedColumnNames
- **Type**: typing.Optional[typing.Sequence[str]]


# ColumnWildcardUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommitTransactionRequestTypeDef

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


# ConditionTypeDef

### Expression
- **Type**: typing.Optional[str]


# CreateDataCellsFilterRequestTypeDef

### TableData
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterUnionTypeDef'>
- **Required**: Yes


# CreateLFTagExpressionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagUnionTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]


# CreateLFTagRequestTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# CreateLakeFormationIdentityCenterConfigurationRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### ExternalFiltering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ExternalFilteringConfigurationUnionTypeDef]

### ShareRecipients
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]


# CreateLakeFormationIdentityCenterConfigurationResponseTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLakeFormationOptInRequestTypeDef

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef'>
- **Required**: Yes


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


# DataCellsFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# DataLakeSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# DeleteDataCellsFilterRequestTypeDef

### TableCatalogId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# DeleteLFTagExpressionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteLFTagRequestTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# DeleteLakeFormationIdentityCenterConfigurationRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]


# DeleteLakeFormationOptInRequestTypeDef

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef'>
- **Required**: Yes


# DeleteObjectInputTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]

### PartitionValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DeleteObjectsOnCancelRequestTypeDef

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


# DeregisterResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLakeFormationIdentityCenterConfigurationRequestTypeDef

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


# DescribeResourceRequestTypeDef

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


# DescribeTransactionRequestTypeDef

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


# ExtendTransactionRequestTypeDef

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


# ExternalFilteringConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterConditionTypeDef

### Field
- **Type**: typing.Optional[typing.Literal['LAST_MODIFIED', 'RESOURCE_ARN', 'ROLE_ARN']]

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'EQ', 'GE', 'GT', 'IN', 'LE', 'LT', 'NE', 'NOT_CONTAINS']]

### StringValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# GetDataCellsFilterRequestTypeDef

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


# GetDataLakeSettingsRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]


# GetDataLakeSettingsResponseTypeDef

### DataLakeSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakeSettingsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEffectivePermissionsForPathRequestTypeDef

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


# GetLFTagExpressionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# GetLFTagExpressionResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLFTagRequestTypeDef

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


# GetQueryStateRequestTypeDef

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


# GetQueryStatisticsRequestTypeDef

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


# GetResourceLFTagsRequestTypeDef

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef'>
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


# GetTableObjectsRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TimestampTypeDef]

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


# GetTemporaryGluePartitionCredentialsRequestTypeDef

### TableArn
- **Type**: <class 'str'>
- **Required**: Yes

### Partition
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.PartitionValueListTypeDef'>
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

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


# GetTemporaryGlueTableCredentialsRequestTypeDef

### TableArn
- **Type**: <class 'str'>
- **Required**: Yes

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

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


# GetWorkUnitResultsRequestTypeDef

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


# GetWorkUnitsRequestPaginateTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# GetWorkUnitsRequestTypeDef

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


# GrantPermissionsRequestTypeDef

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef'>
- **Required**: Yes

### Permissions
- **Type**: typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# LFTagErrorTypeDef

### LFTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairOutputTypeDef]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ErrorDetailTypeDef]


# LFTagExpressionResourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]


# LFTagExpressionTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagOutputTypeDef]]


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


# LFTagKeyResourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LFTagOutputTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


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


# LFTagPairUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LFTagPolicyResourceOutputTypeDef

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagOutputTypeDef]]

### ExpressionName
- **Type**: typing.Optional[str]


# LFTagPolicyResourceTypeDef

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagUnionTypeDef]]

### ExpressionName
- **Type**: typing.Optional[str]


# LFTagPolicyResourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LFTagTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# LFTagUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LakeFormationOptInsInfoTypeDef

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceOutputTypeDef]

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ConditionTypeDef]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedBy
- **Type**: typing.Optional[str]


# ListDataCellsFilterRequestPaginateTypeDef

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableResourceUnionTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# ListDataCellsFilterRequestTypeDef

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableResourceUnionTypeDef]

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


# ListLFTagExpressionsRequestPaginateTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# ListLFTagExpressionsRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLFTagExpressionsResponseTypeDef

### LFTagExpressions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagExpressionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLFTagsRequestPaginateTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### ResourceShareType
- **Type**: typing.Optional[typing.Literal['ALL', 'FOREIGN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# ListLFTagsRequestTypeDef

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


# ListLakeFormationOptInsRequestTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef]

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


# ListPermissionsRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### ResourceType
- **Type**: typing.Optional[typing.Literal['CATALOG', 'DATABASE', 'DATA_LOCATION', 'LF_NAMED_TAG_EXPRESSION', 'LF_TAG', 'LF_TAG_POLICY', 'LF_TAG_POLICY_DATABASE', 'LF_TAG_POLICY_TABLE', 'TABLE']]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef]

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


# ListResourcesRequestTypeDef

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


# ListTableStorageOptimizersRequestTypeDef

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


# ListTransactionsRequestTypeDef

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
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# PrincipalPermissionsTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


# PrincipalResourcePermissionsTypeDef

### Principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ResourceOutputTypeDef]

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ConditionTypeDef]

### Permissions
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]

### AdditionalDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DetailsMapTypeDef]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedBy
- **Type**: typing.Optional[str]


# PutDataLakeSettingsRequestTypeDef

### DataLakeSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakeSettingsUnionTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TimestampTypeDef]

### QueryParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TransactionId
- **Type**: typing.Optional[str]


# QuerySessionContextTypeDef

### QueryId
- **Type**: typing.Optional[str]

### QueryStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TimestampTypeDef]

### ClusterId
- **Type**: typing.Optional[str]

### QueryAuthorizationId
- **Type**: typing.Optional[str]

### AdditionalContext
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterResourceRequestTypeDef

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


# RemoveLFTagsFromResourceRequestTypeDef

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef'>
- **Required**: Yes

### LFTags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPairUnionTypeDef]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.CatalogResourceTypeDef]

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

### LFTagExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagExpressionResourceTypeDef]


# ResourceTypeDef

### Catalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.CatalogResourceTypeDef]

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DatabaseResourceTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableResourceUnionTypeDef]

### TableWithColumns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.TableWithColumnsResourceUnionTypeDef]

### DataLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataLocationResourceTypeDef]

### DataCellsFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterResourceTypeDef]

### LFTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagKeyResourceUnionTypeDef]

### LFTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagPolicyResourceUnionTypeDef]

### LFTagExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagExpressionResourceTypeDef]


# ResourceUnionTypeDef

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


# RevokePermissionsRequestTypeDef

### Principal
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef'>
- **Required**: Yes

### Resource
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResourceUnionTypeDef'>
- **Required**: Yes

### Permissions
- **Type**: typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PermissionsWithGrantOption
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'ALTER', 'ASSOCIATE', 'CREATE_CATALOG', 'CREATE_DATABASE', 'CREATE_LF_TAG', 'CREATE_LF_TAG_EXPRESSION', 'CREATE_TABLE', 'DATA_LOCATION_ACCESS', 'DELETE', 'DESCRIBE', 'DROP', 'GRANT_WITH_LF_TAG_EXPRESSION', 'INSERT', 'SELECT', 'SUPER_USER']]]


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


# SearchDatabasesByLFTagsRequestPaginateTypeDef

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagUnionTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# SearchDatabasesByLFTagsRequestTypeDef

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagUnionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CatalogId
- **Type**: typing.Optional[str]


# SearchDatabasesByLFTagsResponseTypeDef

### DatabaseList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.TaggedDatabaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchTablesByLFTagsRequestPaginateTypeDef

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagUnionTypeDef]
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.PaginatorConfigTypeDef]


# SearchTablesByLFTagsRequestTypeDef

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagUnionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CatalogId
- **Type**: typing.Optional[str]


# SearchTablesByLFTagsResponseTypeDef

### TableList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lakeformation_classes.TaggedTableTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StartQueryPlanningRequestTypeDef

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


# StartTransactionRequestTypeDef

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


# TableResourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ColumnWildcardUnionTypeDef]


# TableWithColumnsResourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransactionDescriptionTypeDef

### TransactionId
- **Type**: typing.Optional[str]

### TransactionStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ACTIVE', 'COMMITTED', 'COMMIT_IN_PROGRESS']]

### TransactionStartTime
- **Type**: typing.Optional[datetime.datetime]

### TransactionEndTime
- **Type**: typing.Optional[datetime.datetime]


# UpdateDataCellsFilterRequestTypeDef

### TableData
- **Type**: <class 'aws_resource_validator.pydantic_models.lakeformation_classes.DataCellsFilterUnionTypeDef'>
- **Required**: Yes


# UpdateLFTagExpressionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.LFTagUnionTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CatalogId
- **Type**: typing.Optional[str]


# UpdateLFTagRequestTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### CatalogId
- **Type**: typing.Optional[str]

### TagValuesToDelete
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValuesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLakeFormationIdentityCenterConfigurationRequestTypeDef

### CatalogId
- **Type**: typing.Optional[str]

### ShareRecipients
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lakeformation_classes.DataLakePrincipalTypeDef]]

### ApplicationStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ExternalFiltering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lakeformation_classes.ExternalFilteringConfigurationUnionTypeDef]


# UpdateResourceRequestTypeDef

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


# UpdateTableObjectsRequestTypeDef

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


# UpdateTableStorageOptimizerRequestTypeDef

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


