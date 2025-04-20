# S3Tables S3Tables Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateNamespaceRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.List[str]
- **Required**: Yes


# CreateNamespaceResponse

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTableBucketRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTableBucketResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTableRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['ICEBERG']
- **Required**: Yes

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableMetadata]


# CreateTableResponse

### tableARN
- **Type**: <class 'str'>
- **Required**: Yes

### versionToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNamespaceRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTableBucketPolicyRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTableBucketRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTablePolicyRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTableRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionToken
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetNamespaceRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes


# GetNamespaceResponse

### namespace
- **Type**: typing.List[str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableBucketMaintenanceConfigurationRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableBucketMaintenanceConfigurationResponse

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Dict[typing.Literal['icebergUnreferencedFileRemoval'], aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableBucketMaintenanceConfigurationValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableBucketPolicyRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableBucketPolicyResponse

### resourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableBucketRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableBucketResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableMaintenanceConfigurationRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableMaintenanceConfigurationResponse

### tableARN
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Dict[typing.Literal['icebergCompaction', 'icebergSnapshotManagement'], aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableMaintenanceConfigurationValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableMaintenanceJobStatusRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableMaintenanceJobStatusResponse

### tableARN
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Dict[typing.Literal['icebergCompaction', 'icebergSnapshotManagement', 'icebergUnreferencedFileRemoval'], aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableMaintenanceJobStatusValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableMetadataLocationRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableMetadataLocationResponse

### versionToken
- **Type**: <class 'str'>
- **Required**: Yes

### metadataLocation
- **Type**: <class 'str'>
- **Required**: Yes

### warehouseLocation
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetTablePolicyRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTablePolicyResponse

### resourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['aws', 'customer']
- **Required**: Yes

### tableARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.List[str]
- **Required**: Yes

### versionToken
- **Type**: <class 'str'>
- **Required**: Yes

### metadataLocation
- **Type**: <class 'str'>
- **Required**: Yes

### warehouseLocation
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### managedByService
- **Type**: <class 'str'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['ICEBERG']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# IcebergCompactionSettings

### targetFileSizeMB
- **Type**: typing.Optional[int]


# IcebergMetadata

### schema
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.IcebergSchema'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.IcebergMetadata'>>


# IcebergSchema

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.SchemaField]
- **Required**: Yes


# IcebergSnapshotManagementSettings

### minSnapshotsToKeep
- **Type**: typing.Optional[int]

### maxSnapshotAgeHours
- **Type**: typing.Optional[int]


# IcebergUnreferencedFileRemovalSettings

### unreferencedDays
- **Type**: typing.Optional[int]

### nonCurrentDays
- **Type**: typing.Optional[int]


# ListNamespacesRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]

### continuationToken
- **Type**: typing.Optional[str]

### maxNamespaces
- **Type**: typing.Optional[int]


# ListNamespacesRequestPaginate

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.PaginatorConfig]


# ListNamespacesResponse

### namespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.NamespaceSummary]
- **Required**: Yes

### continuationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# ListTableBucketsRequest

### prefix
- **Type**: typing.Optional[str]

### continuationToken
- **Type**: typing.Optional[str]

### maxBuckets
- **Type**: typing.Optional[int]


# ListTableBucketsRequestPaginate

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.PaginatorConfig]


# ListTableBucketsResponse

### tableBuckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableBucketSummary]
- **Required**: Yes

### continuationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# ListTablesRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### continuationToken
- **Type**: typing.Optional[str]

### maxTables
- **Type**: typing.Optional[int]


# ListTablesRequestPaginate

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.PaginatorConfig]


# ListTablesResponse

### tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableSummary]
- **Required**: Yes

### continuationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


# NamespaceSummary

### namespace
- **Type**: typing.List[str]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutTableBucketMaintenanceConfigurationRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['icebergUnreferencedFileRemoval']
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableBucketMaintenanceConfigurationValue'>
- **Required**: Yes


# PutTableBucketPolicyRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### resourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutTableMaintenanceConfigurationRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['icebergCompaction', 'icebergSnapshotManagement']
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableMaintenanceConfigurationValue'>
- **Required**: Yes


# PutTablePolicyRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# RenameTableRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### newNamespaceName
- **Type**: typing.Optional[str]

### newName
- **Type**: typing.Optional[str]

### versionToken
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


# SchemaField

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]


# TableBucketMaintenanceConfigurationValue

### status
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableBucketMaintenanceSettings]


# TableBucketMaintenanceSettings

### icebergUnreferencedFileRemoval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.IcebergUnreferencedFileRemovalSettings]


# TableBucketSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TableMaintenanceConfigurationValue

### status
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.TableMaintenanceSettings]


# TableMaintenanceJobStatusValue

### status
- **Type**: typing.Literal['Disabled', 'Failed', 'Not_Yet_Run', 'Successful']
- **Required**: Yes

### lastRunTimestamp
- **Type**: typing.Optional[datetime.datetime]

### failureMessage
- **Type**: typing.Optional[str]


# TableMaintenanceSettings

### icebergCompaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.IcebergCompactionSettings]

### icebergSnapshotManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.IcebergSnapshotManagementSettings]


# TableMetadata

### iceberg
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3tables.s3tables_classes.IcebergMetadata]


# TableSummary

### namespace
- **Type**: typing.List[str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['aws', 'customer']
- **Required**: Yes

### tableARN
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# UpdateTableMetadataLocationRequest

### tableBucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionToken
- **Type**: <class 'str'>
- **Required**: Yes

### metadataLocation
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTableMetadataLocationResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tableARN
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.List[str]
- **Required**: Yes

### versionToken
- **Type**: <class 'str'>
- **Required**: Yes

### metadataLocation
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3tables.s3tables_classes.ResponseMetadata'>
- **Required**: Yes


