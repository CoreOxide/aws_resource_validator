# Finspace Data Finspace Data Classes

# AssociateUserToPermissionGroupRequest

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AssociateUserToPermissionGroupResponse

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# AwsCredentials

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

# ChangesetErrorInfo

### errorMessage
- **Type**: typing.Optional[str]

### errorCategory
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'CANCELLED', 'INTERNAL_SERVICE_EXCEPTION', 'RESOURCE_NOT_FOUND', 'SERVICE_QUOTA_EXCEEDED', 'THROTTLING', 'USER_RECOVERABLE', 'VALIDATION']]


# ChangesetSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ChangesetErrorInfo]

### activeUntilTimestamp
- **Type**: typing.Optional[int]

### activeFromTimestamp
- **Type**: typing.Optional[int]

### updatesChangesetId
- **Type**: typing.Optional[str]

### updatedByChangesetId
- **Type**: typing.Optional[str]


# ColumnDefinition

### dataType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BINARY', 'BOOLEAN', 'CHAR', 'DATE', 'DATETIME', 'DOUBLE', 'FLOAT', 'INTEGER', 'SMALLINT', 'STRING', 'TINYINT']]

### columnName
- **Type**: typing.Optional[str]

### columnDescription
- **Type**: typing.Optional[str]


# CreateChangesetRequest

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

### clientToken
- **Type**: typing.Optional[str]


# CreateChangesetResponse

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataViewRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### destinationTypeParams
- **Type**: typing.Union[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DataViewDestinationTypeParams, aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DataViewDestinationTypeParamsOutput]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### autoUpdate
- **Type**: typing.Optional[bool]

### sortColumns
- **Type**: typing.Optional[typing.List[str]]

### partitionColumns
- **Type**: typing.Optional[typing.List[str]]

### asOfTimestamp
- **Type**: typing.Optional[int]


# CreateDataViewResponse

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### dataViewId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetRequest

### datasetTitle
- **Type**: <class 'str'>
- **Required**: Yes

### kind
- **Type**: typing.Literal['NON_TABULAR', 'TABULAR']
- **Required**: Yes

### permissionGroupParams
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PermissionGroupParams'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### datasetDescription
- **Type**: typing.Optional[str]

### ownerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DatasetOwnerInfo]

### alias
- **Type**: typing.Optional[str]

### schemaDefinition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.SchemaUnion, aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.SchemaUnionOutput, NoneType]


# CreateDatasetResponse

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePermissionGroupRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### applicationPermissions
- **Type**: typing.List[typing.Literal['AccessNotebooks', 'CreateDataset', 'GetTemporaryCredentials', 'ManageAttributeSets', 'ManageClusters', 'ManageUsersAndGroups', 'ViewAuditData']]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# CreatePermissionGroupResponse

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

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


# CreateUserResponse

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# Credentials

### accessKeyId
- **Type**: typing.Optional[str]

### secretAccessKey
- **Type**: typing.Optional[str]

### sessionToken
- **Type**: typing.Optional[str]


# DataViewDestinationTypeParams

### destinationType
- **Type**: <class 'str'>
- **Required**: Yes

### s3DestinationExportFileFormat
- **Type**: typing.Optional[typing.Literal['DELIMITED_TEXT', 'PARQUET']]

### s3DestinationExportFileFormatOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataViewDestinationTypeParamsOutput

### destinationType
- **Type**: <class 'str'>
- **Required**: Yes

### s3DestinationExportFileFormat
- **Type**: typing.Optional[typing.Literal['DELIMITED_TEXT', 'PARQUET']]

### s3DestinationExportFileFormatOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataViewErrorInfo

### errorMessage
- **Type**: typing.Optional[str]

### errorCategory
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'CANCELLED', 'INTERNAL_SERVICE_EXCEPTION', 'RESOURCE_NOT_FOUND', 'SERVICE_QUOTA_EXCEEDED', 'THROTTLING', 'USER_RECOVERABLE', 'VALIDATION']]


# DataViewSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DataViewErrorInfo]

### destinationTypeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DataViewDestinationTypeParamsOutput]

### autoUpdate
- **Type**: typing.Optional[bool]

### createTime
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]


# Dataset

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DatasetOwnerInfo]

### createTime
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]

### schemaDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.SchemaUnionOutput]

### alias
- **Type**: typing.Optional[str]


# DatasetOwnerInfo

### name
- **Type**: typing.Optional[str]

### phoneNumber
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]


# DeleteDatasetRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteDatasetResponse

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePermissionGroupRequest

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePermissionGroupResponse

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# DisableUserRequest

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DisableUserResponse

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateUserFromPermissionGroupRequest

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DisassociateUserFromPermissionGroupResponse

### statusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# EnableUserRequest

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# EnableUserResponse

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetChangesetRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetChangesetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ChangesetErrorInfo'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataViewRequest

### dataViewId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataViewResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DataViewErrorInfo'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DataViewDestinationTypeParamsOutput'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'FAILED_CLEANUP_FAILED', 'PENDING', 'RUNNING', 'STARTING', 'SUCCESS', 'TIMEOUT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetDatasetRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDatasetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.SchemaUnionOutput'>
- **Required**: Yes

### alias
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'PENDING', 'RUNNING', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetExternalDataViewAccessDetailsRequest

### dataViewId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExternalDataViewAccessDetailsResponse

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.AwsCredentials'>
- **Required**: Yes

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.S3Location'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetPermissionGroupRequest

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPermissionGroupResponse

### permissionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PermissionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetProgrammaticAccessCredentialsRequest

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### durationInMinutes
- **Type**: typing.Optional[int]


# GetProgrammaticAccessCredentialsResponse

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.Credentials'>
- **Required**: Yes

### durationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserRequest

### userId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkingLocationRequest

### locationType
- **Type**: typing.Optional[typing.Literal['INGESTION', 'SAGEMAKER']]


# GetWorkingLocationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# ListChangesetsRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListChangesetsRequestPaginate

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PaginatorConfig]


# ListChangesetsResponse

### changesets
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ChangesetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataViewsRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataViewsRequestPaginate

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PaginatorConfig]


# ListDataViewsResponse

### dataViews
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.DataViewSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PaginatorConfig]


# ListDatasetsResponse

### datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.Dataset]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsByUserRequest

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsByUserResponse

### permissionGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PermissionGroupByUser]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsRequest

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PaginatorConfig]


# ListPermissionGroupsResponse

### permissionGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PermissionGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersByPermissionGroupRequest

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersByPermissionGroupResponse

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.UserByPermissionGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersRequest

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.PaginatorConfig]


# ListUsersResponse

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.User]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionGroup

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


# PermissionGroupByUser

### permissionGroupId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### membershipStatus
- **Type**: typing.Optional[typing.Literal['ADDITION_IN_PROGRESS', 'ADDITION_SUCCESS', 'REMOVAL_IN_PROGRESS']]


# PermissionGroupParams

### permissionGroupId
- **Type**: typing.Optional[str]

### datasetPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResourcePermission]]


# ResetUserPasswordRequest

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ResetUserPasswordResponse

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### temporaryPassword
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# ResourcePermission

### permission
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


# S3Location

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaDefinition

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ColumnDefinition]]

### primaryKeyColumns
- **Type**: typing.Optional[typing.List[str]]


# SchemaDefinitionOutput

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ColumnDefinition]]

### primaryKeyColumns
- **Type**: typing.Optional[typing.List[str]]


# SchemaUnion

### tabularSchemaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.SchemaDefinition]


# SchemaUnionOutput

### tabularSchemaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.SchemaDefinitionOutput]


# UpdateChangesetRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceParams
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### formatParams
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateChangesetResponse

### changesetId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDatasetRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.SchemaUnion, aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.SchemaUnionOutput, NoneType]


# UpdateDatasetResponse

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePermissionGroupRequest

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### applicationPermissions
- **Type**: typing.Optional[typing.List[typing.Literal['AccessNotebooks', 'CreateDataset', 'GetTemporaryCredentials', 'ManageAttributeSets', 'ManageClusters', 'ManageUsersAndGroups', 'ViewAuditData']]]

### clientToken
- **Type**: typing.Optional[str]


# UpdatePermissionGroupResponse

### permissionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserRequest

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


# UpdateUserResponse

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.finspace_data.finspace_data_classes.ResponseMetadata'>
- **Required**: Yes


# User

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


# UserByPermissionGroup

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


