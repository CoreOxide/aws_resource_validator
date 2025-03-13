# Finspace Data Classes

# AssociateUserToPermissionGroupRequestTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AssociateUserToPermissionGroupResponseTypeDef

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AwsCredentialsTypeDef

### accessKeyId
- **Type**: typing.Optional[str]

### secretAccessKey
- **Type**: typing.Optional[str]

### sessionToken
- **Type**: typing.Optional[str]

### expiration
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChangesetErrorInfoTypeDef

### errorMessage
- **Type**: typing.Optional[str]

### errorCategory
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'CANCELLED', 'INTERNAL_SERVICE_EXCEPTION', 'RESOURCE_NOT_FOUND', 'SERVICE_QUOTA_EXCEEDED', 'THROTTLING', 'USER_RECOVERABLE', 'VALIDATION']]


# ChangesetSummaryTypeDef

### changesetId
- **Type**: typing.Optional[str]

### changesetArn
- **Type**: typing.Optional[str]

### datasetId
- **Type**: typing.Optional[str]

### changeType
- **Type**: typing.Optional[typing.Literal['APPEND', 'MODIFY', 'REPLACE']]

### sourceParams
- **Type**: typing.Optional[typing.Dict[str, str]]

### formatParams
- **Type**: typing.Optional[typing.Dict[str, str]]

### createTime
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'RUNNING', 'STOP_REQUESTED', 'SUCCESS']]

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.ChangesetErrorInfoTypeDef]

### activeUntilTimestamp
- **Type**: typing.Optional[int]

### activeFromTimestamp
- **Type**: typing.Optional[int]

### updatesChangesetId
- **Type**: typing.Optional[str]

### updatedByChangesetId
- **Type**: typing.Optional[str]


# ColumnDefinitionTypeDef

### dataType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BINARY', 'BOOLEAN', 'CHAR', 'DATE', 'DATETIME', 'DOUBLE', 'FLOAT', 'INTEGER', 'SMALLINT', 'STRING', 'TINYINT']]

### columnName
- **Type**: typing.Optional[str]

### columnDescription
- **Type**: typing.Optional[str]


# CreateChangesetRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### changeType
- **Type**: typing.Literal['APPEND', 'MODIFY', 'REPLACE']
- **Required**: Yes

### sourceParams
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### formatParams
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateChangesetResponseTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataViewRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### destinationTypeParams
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.DataViewDestinationTypeParamsUnionTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### autoUpdate
- **Type**: typing.Optional[bool]

### sortColumns
- **Type**: typing.Optional[typing.Sequence[str]]

### partitionColumns
- **Type**: typing.Optional[typing.Sequence[str]]

### asOfTimestamp
- **Type**: typing.Optional[int]


# CreateDataViewResponseTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### dataViewId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetRequestTypeDef

### datasetTitle
- **Type**: <class 'str'>
- **Required**: Yes

### kind
- **Type**: typing.Literal['NON_TABULAR', 'TABULAR']
- **Required**: Yes

### permissionGroupParams
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.PermissionGroupParamsTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### datasetDescription
- **Type**: typing.Optional[str]

### ownerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.DatasetOwnerInfoTypeDef]

### alias
- **Type**: typing.Optional[str]

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionUnionTypeDef]


# CreateDatasetResponseTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePermissionGroupRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### applicationPermissions
- **Type**: typing.Sequence[typing.Literal['AccessNotebooks', 'CreateDataset', 'GetTemporaryCredentials', 'ManageAttributeSets', 'ManageClusters', 'ManageUsersAndGroups', 'ViewAuditData']]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# CreatePermissionGroupResponseTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserResponseTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CredentialsTypeDef

### accessKeyId
- **Type**: typing.Optional[str]

### secretAccessKey
- **Type**: typing.Optional[str]

### sessionToken
- **Type**: typing.Optional[str]


# DataViewDestinationTypeParamsOutputTypeDef

### destinationType
- **Type**: <class 'str'>
- **Required**: Yes

### s3DestinationExportFileFormat
- **Type**: typing.Optional[typing.Literal['DELIMITED_TEXT', 'PARQUET']]

### s3DestinationExportFileFormatOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataViewDestinationTypeParamsTypeDef

### destinationType
- **Type**: <class 'str'>
- **Required**: Yes

### s3DestinationExportFileFormat
- **Type**: typing.Optional[typing.Literal['DELIMITED_TEXT', 'PARQUET']]

### s3DestinationExportFileFormatOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DataViewDestinationTypeParamsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataViewErrorInfoTypeDef

### errorMessage
- **Type**: typing.Optional[str]

### errorCategory
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'CANCELLED', 'INTERNAL_SERVICE_EXCEPTION', 'RESOURCE_NOT_FOUND', 'SERVICE_QUOTA_EXCEEDED', 'THROTTLING', 'USER_RECOVERABLE', 'VALIDATION']]


# DataViewSummaryTypeDef

### dataViewId
- **Type**: typing.Optional[str]

### dataViewArn
- **Type**: typing.Optional[str]

### datasetId
- **Type**: typing.Optional[str]

### asOfTimestamp
- **Type**: typing.Optional[int]

### partitionColumns
- **Type**: typing.Optional[typing.List[str]]

### sortColumns
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FAILED_CLEANUP_FAILED', 'PENDING', 'RUNNING', 'STARTING', 'SUCCESS', 'TIMEOUT']]

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.DataViewErrorInfoTypeDef]

### destinationTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.DataViewDestinationTypeParamsOutputTypeDef]

### autoUpdate
- **Type**: typing.Optional[bool]

### createTime
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]


# DatasetOwnerInfoTypeDef

### name
- **Type**: typing.Optional[str]

### phoneNumber
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]


# DatasetTypeDef

### datasetId
- **Type**: typing.Optional[str]

### datasetArn
- **Type**: typing.Optional[str]

### datasetTitle
- **Type**: typing.Optional[str]

### kind
- **Type**: typing.Optional[typing.Literal['NON_TABULAR', 'TABULAR']]

### datasetDescription
- **Type**: typing.Optional[str]

### ownerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.DatasetOwnerInfoTypeDef]

### createTime
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionOutputTypeDef]

### alias
- **Type**: typing.Optional[str]


# DeleteDatasetRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteDatasetResponseTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePermissionGroupRequestTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePermissionGroupResponseTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableUserRequestTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DisableUserResponseTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateUserFromPermissionGroupRequestTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DisassociateUserFromPermissionGroupResponseTypeDef

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableUserRequestTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# EnableUserResponseTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChangesetRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetChangesetResponseTypeDef

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetArn
- **Type**: <class 'str'>
- **Required**: Yes

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### changeType
- **Type**: typing.Literal['APPEND', 'MODIFY', 'REPLACE']
- **Required**: Yes

### sourceParams
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### formatParams
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### createTime
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'PENDING', 'RUNNING', 'STOP_REQUESTED', 'SUCCESS']
- **Required**: Yes

### errorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ChangesetErrorInfoTypeDef'>
- **Required**: Yes

### activeUntilTimestamp
- **Type**: <class 'int'>
- **Required**: Yes

### activeFromTimestamp
- **Type**: <class 'int'>
- **Required**: Yes

### updatesChangesetId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedByChangesetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataViewRequestTypeDef

### dataViewId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataViewResponseTypeDef

### autoUpdate
- **Type**: <class 'bool'>
- **Required**: Yes

### partitionColumns
- **Type**: typing.List[str]
- **Required**: Yes

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### asOfTimestamp
- **Type**: <class 'int'>
- **Required**: Yes

### errorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.DataViewErrorInfoTypeDef'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### createTime
- **Type**: <class 'int'>
- **Required**: Yes

### sortColumns
- **Type**: typing.List[str]
- **Required**: Yes

### dataViewId
- **Type**: <class 'str'>
- **Required**: Yes

### dataViewArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationTypeParams
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.DataViewDestinationTypeParamsOutputTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'FAILED_CLEANUP_FAILED', 'PENDING', 'RUNNING', 'STARTING', 'SUCCESS', 'TIMEOUT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDatasetRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDatasetResponseTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### datasetTitle
- **Type**: <class 'str'>
- **Required**: Yes

### kind
- **Type**: typing.Literal['NON_TABULAR', 'TABULAR']
- **Required**: Yes

### datasetDescription
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'int'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### schemaDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionOutputTypeDef'>
- **Required**: Yes

### alias
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'PENDING', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExternalDataViewAccessDetailsRequestTypeDef

### dataViewId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExternalDataViewAccessDetailsResponseTypeDef

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.S3LocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPermissionGroupRequestTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPermissionGroupResponseTypeDef

### permissionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.PermissionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProgrammaticAccessCredentialsRequestTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### durationInMinutes
- **Type**: typing.Optional[int]


# GetProgrammaticAccessCredentialsResponseTypeDef

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.CredentialsTypeDef'>
- **Required**: Yes

### durationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserRequestTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkingLocationRequestTypeDef

### locationType
- **Type**: typing.Optional[typing.Literal['INGESTION', 'SAGEMAKER']]


# GetWorkingLocationResponseTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### s3Path
- **Type**: <class 'str'>
- **Required**: Yes

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChangesetsRequestPaginateTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListChangesetsRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListChangesetsResponseTypeDef

### changesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.ChangesetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataViewsRequestPaginateTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListDataViewsRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataViewsResponseTypeDef

### dataViews
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.DataViewSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListDatasetsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponseTypeDef

### datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.DatasetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsByUserRequestTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsByUserResponseTypeDef

### permissionGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.PermissionGroupByUserTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListPermissionGroupsRequestTypeDef

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsResponseTypeDef

### permissionGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.PermissionGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersByPermissionGroupRequestTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersByPermissionGroupResponseTypeDef

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.UserByPermissionGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListUsersRequestTypeDef

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersResponseTypeDef

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.UserTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionGroupByUserTypeDef

### permissionGroupId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### membershipStatus
- **Type**: typing.Optional[typing.Literal['ADDITION_IN_PROGRESS', 'ADDITION_SUCCESS', 'REMOVAL_IN_PROGRESS']]


# PermissionGroupParamsTypeDef

### permissionGroupId
- **Type**: typing.Optional[str]

### datasetPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_data_classes.ResourcePermissionTypeDef]]


# PermissionGroupTypeDef

### permissionGroupId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### applicationPermissions
- **Type**: typing.Optional[typing.List[typing.Literal['AccessNotebooks', 'CreateDataset', 'GetTemporaryCredentials', 'ManageAttributeSets', 'ManageClusters', 'ManageUsersAndGroups', 'ViewAuditData']]]

### createTime
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]

### membershipStatus
- **Type**: typing.Optional[typing.Literal['ADDITION_IN_PROGRESS', 'ADDITION_SUCCESS', 'REMOVAL_IN_PROGRESS']]


# ResetUserPasswordRequestTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ResetUserPasswordResponseTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### temporaryPassword
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourcePermissionTypeDef

### permission
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


# S3LocationTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaDefinitionOutputTypeDef

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.ColumnDefinitionTypeDef]]

### primaryKeyColumns
- **Type**: typing.Optional[typing.List[str]]


# SchemaDefinitionTypeDef

### columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_data_classes.ColumnDefinitionTypeDef]]

### primaryKeyColumns
- **Type**: typing.Optional[typing.Sequence[str]]


# SchemaUnionOutputTypeDef

### tabularSchemaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaDefinitionOutputTypeDef]


# SchemaUnionTypeDef

### tabularSchemaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaDefinitionTypeDef]


# SchemaUnionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateChangesetRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceParams
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### formatParams
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateChangesetResponseTypeDef

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDatasetRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetTitle
- **Type**: <class 'str'>
- **Required**: Yes

### kind
- **Type**: typing.Literal['NON_TABULAR', 'TABULAR']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### datasetDescription
- **Type**: typing.Optional[str]

### alias
- **Type**: typing.Optional[str]

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionUnionTypeDef]


# UpdateDatasetResponseTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePermissionGroupRequestTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### applicationPermissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AccessNotebooks', 'CreateDataset', 'GetTemporaryCredentials', 'ManageAttributeSets', 'ManageClusters', 'ManageUsersAndGroups', 'ViewAuditData']]]

### clientToken
- **Type**: typing.Optional[str]


# UpdatePermissionGroupResponseTypeDef

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserResponseTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserByPermissionGroupTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UserTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

