# Pydantic Models in finspace_data_classes

# AssociateUserToPermissionGroupRequestRequestTypeDef

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


# CreateChangesetRequestRequestTypeDef

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


# CreateDataViewRequestRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### destinationTypeParams
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.DataViewDestinationTypeParamsTypeDef'>
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


# CreateDatasetRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionTypeDef]


# CreateDatasetResponseTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePermissionGroupRequestRequestTypeDef

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


# CreateUserRequestRequestTypeDef

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['APP_USER', 'SUPER_USER']
- **Required**: Yes

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### apiAccess
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### apiAccessPrincipalArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


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


# DataViewDestinationTypeParamsPaginatorTypeDef

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


# DataViewErrorInfoTypeDef

### errorMessage
- **Type**: typing.Optional[str]

### errorCategory
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'CANCELLED', 'INTERNAL_SERVICE_EXCEPTION', 'RESOURCE_NOT_FOUND', 'SERVICE_QUOTA_EXCEEDED', 'THROTTLING', 'USER_RECOVERABLE', 'VALIDATION']]


# DataViewSummaryPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.DataViewDestinationTypeParamsPaginatorTypeDef]

### autoUpdate
- **Type**: typing.Optional[bool]

### createTime
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.DataViewDestinationTypeParamsTypeDef]

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


# DatasetPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionPaginatorTypeDef]

### alias
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionTypeDef]

### alias
- **Type**: typing.Optional[str]


# DeleteDatasetRequestRequestTypeDef

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


# DeletePermissionGroupRequestRequestTypeDef

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


# DisableUserRequestRequestTypeDef

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


# DisassociateUserFromPermissionGroupRequestRequestTypeDef

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


# EnableUserRequestRequestTypeDef

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


# GetChangesetRequestRequestTypeDef

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


# GetDataViewRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.DataViewDestinationTypeParamsTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'FAILED_CLEANUP_FAILED', 'PENDING', 'RUNNING', 'STARTING', 'SUCCESS', 'TIMEOUT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDatasetRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionTypeDef'>
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


# GetExternalDataViewAccessDetailsRequestRequestTypeDef

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


# GetPermissionGroupRequestRequestTypeDef

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


# GetProgrammaticAccessCredentialsRequestRequestTypeDef

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


# GetUserRequestRequestTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserResponseTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATING', 'DISABLED', 'ENABLED']
- **Required**: Yes

### firstName
- **Type**: <class 'str'>
- **Required**: Yes

### lastName
- **Type**: <class 'str'>
- **Required**: Yes

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['APP_USER', 'SUPER_USER']
- **Required**: Yes

### apiAccess
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### apiAccessPrincipalArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'int'>
- **Required**: Yes

### lastEnabledTime
- **Type**: <class 'int'>
- **Required**: Yes

### lastDisabledTime
- **Type**: <class 'int'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### lastLoginTime
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkingLocationRequestRequestTypeDef

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


# ListChangesetsRequestListChangesetsPaginateTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListChangesetsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataViewsRequestListDataViewsPaginateTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListDataViewsRequestRequestTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataViewsResponsePaginatorTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### dataViews
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.DataViewSummaryPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataViewsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### dataViews
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.DataViewSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetsRequestListDatasetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListDatasetsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponsePaginatorTypeDef

### datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.DatasetPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetsResponseTypeDef

### datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.DatasetTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPermissionGroupsByUserRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPermissionGroupsRequestListPermissionGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListPermissionGroupsRequestRequestTypeDef

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsResponseTypeDef

### permissionGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.PermissionGroupTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersByPermissionGroupRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersRequestListUsersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.PaginatorConfigTypeDef]


# ListUsersRequestRequestTypeDef

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersResponseTypeDef

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.UserTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ResetUserPasswordRequestRequestTypeDef

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


# S3LocationTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaDefinitionPaginatorTypeDef

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_data_classes.ColumnDefinitionTypeDef]]

### primaryKeyColumns
- **Type**: typing.Optional[typing.List[str]]


# SchemaDefinitionTypeDef

### columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.finspace_data_classes.ColumnDefinitionTypeDef]]

### primaryKeyColumns
- **Type**: typing.Optional[typing.Sequence[str]]


# SchemaUnionPaginatorTypeDef

### tabularSchemaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaDefinitionPaginatorTypeDef]


# SchemaUnionTypeDef

### tabularSchemaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaDefinitionTypeDef]


# UpdateChangesetRequestRequestTypeDef

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


# UpdateDatasetRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data_classes.SchemaUnionTypeDef]


# UpdateDatasetResponseTypeDef

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePermissionGroupRequestRequestTypeDef

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


# UpdateUserRequestRequestTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['APP_USER', 'SUPER_USER']]

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### apiAccess
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### apiAccessPrincipalArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateUserResponseTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserByPermissionGroupTypeDef

### userId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DISABLED', 'ENABLED']]

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APP_USER', 'SUPER_USER']]

### apiAccess
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### apiAccessPrincipalArn
- **Type**: typing.Optional[str]

### membershipStatus
- **Type**: typing.Optional[typing.Literal['ADDITION_IN_PROGRESS', 'ADDITION_SUCCESS', 'REMOVAL_IN_PROGRESS']]


# UserTypeDef

### userId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DISABLED', 'ENABLED']]

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['APP_USER', 'SUPER_USER']]

### apiAccess
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### apiAccessPrincipalArn
- **Type**: typing.Optional[str]

### createTime
- **Type**: typing.Optional[int]

### lastEnabledTime
- **Type**: typing.Optional[int]

### lastDisabledTime
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]

### lastLoginTime
- **Type**: typing.Optional[int]


