# Docdb Elastic Classes

# ApplyPendingMaintenanceActionInputTypeDef

### applyAction
- **Type**: <class 'str'>
- **Required**: Yes

### optInType
- **Type**: typing.Literal['APPLY_ON', 'IMMEDIATE', 'NEXT_MAINTENANCE', 'UNDO_OPT_IN']
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### applyOn
- **Type**: typing.Optional[str]


# ApplyPendingMaintenanceActionOutputTypeDef

### resourcePendingMaintenanceAction
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResourcePendingMaintenanceActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClusterInListTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COPYING', 'CREATING', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE', 'INACCESSIBLE_ENCRYPTION_CREDS', 'INACCESSIBLE_SECRET_ARN', 'INACCESSIBLE_VPC_ENDPOINT', 'INCOMPATIBLE_NETWORK', 'INVALID_SECURITY_GROUP_ID', 'INVALID_SUBNET_ID', 'IP_ADDRESS_LIMIT_EXCEEDED', 'MAINTENANCE', 'MERGING', 'MODIFYING', 'SPLITTING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING', 'VPC_ENDPOINT_LIMIT_EXCEEDED']
- **Required**: Yes


# ClusterSnapshotInListTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotArn
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotCreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COPYING', 'CREATING', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE', 'INACCESSIBLE_ENCRYPTION_CREDS', 'INACCESSIBLE_SECRET_ARN', 'INACCESSIBLE_VPC_ENDPOINT', 'INCOMPATIBLE_NETWORK', 'INVALID_SECURITY_GROUP_ID', 'INVALID_SUBNET_ID', 'IP_ADDRESS_LIMIT_EXCEEDED', 'MAINTENANCE', 'MERGING', 'MODIFYING', 'SPLITTING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING', 'VPC_ENDPOINT_LIMIT_EXCEEDED']
- **Required**: Yes


# ClusterSnapshotTypeDef

### adminUserName
- **Type**: <class 'str'>
- **Required**: Yes

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### clusterCreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotArn
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotCreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COPYING', 'CREATING', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE', 'INACCESSIBLE_ENCRYPTION_CREDS', 'INACCESSIBLE_SECRET_ARN', 'INACCESSIBLE_VPC_ENDPOINT', 'INCOMPATIBLE_NETWORK', 'INVALID_SECURITY_GROUP_ID', 'INVALID_SUBNET_ID', 'IP_ADDRESS_LIMIT_EXCEEDED', 'MAINTENANCE', 'MERGING', 'MODIFYING', 'SPLITTING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING', 'VPC_ENDPOINT_LIMIT_EXCEEDED']
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### snapshotType
- **Type**: typing.Optional[typing.Literal['AUTOMATED', 'MANUAL']]


# ClusterTypeDef

### adminUserName
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['PLAIN_TEXT', 'SECRET_ARN']
- **Required**: Yes

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### clusterEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### preferredMaintenanceWindow
- **Type**: <class 'str'>
- **Required**: Yes

### shardCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### shardCount
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COPYING', 'CREATING', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE', 'INACCESSIBLE_ENCRYPTION_CREDS', 'INACCESSIBLE_SECRET_ARN', 'INACCESSIBLE_VPC_ENDPOINT', 'INCOMPATIBLE_NETWORK', 'INVALID_SECURITY_GROUP_ID', 'INVALID_SUBNET_ID', 'IP_ADDRESS_LIMIT_EXCEEDED', 'MAINTENANCE', 'MERGING', 'MODIFYING', 'SPLITTING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING', 'VPC_ENDPOINT_LIMIT_EXCEEDED']
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### backupRetentionPeriod
- **Type**: typing.Optional[int]

### preferredBackupWindow
- **Type**: typing.Optional[str]

### shardInstanceCount
- **Type**: typing.Optional[int]

### shards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_elastic_classes.ShardTypeDef]]


# CopyClusterSnapshotInputTypeDef

### snapshotArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### copyTags
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CopyClusterSnapshotOutputTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterInputTypeDef

### adminUserName
- **Type**: <class 'str'>
- **Required**: Yes

### adminUserPassword
- **Type**: <class 'str'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['PLAIN_TEXT', 'SECRET_ARN']
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### shardCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### shardCount
- **Type**: <class 'int'>
- **Required**: Yes

### backupRetentionPeriod
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### preferredBackupWindow
- **Type**: typing.Optional[str]

### preferredMaintenanceWindow
- **Type**: typing.Optional[str]

### shardInstanceCount
- **Type**: typing.Optional[int]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateClusterOutputTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterSnapshotInputTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateClusterSnapshotOutputTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterInputTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterOutputTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterSnapshotInputTypeDef

### snapshotArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterSnapshotOutputTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetClusterInputTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetClusterOutputTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetClusterSnapshotInputTypeDef

### snapshotArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetClusterSnapshotOutputTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPendingMaintenanceActionInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPendingMaintenanceActionOutputTypeDef

### resourcePendingMaintenanceAction
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResourcePendingMaintenanceActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListClusterSnapshotsInputPaginateTypeDef

### clusterArn
- **Type**: typing.Optional[str]

### snapshotType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_elastic_classes.PaginatorConfigTypeDef]


# ListClusterSnapshotsInputTypeDef

### clusterArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### snapshotType
- **Type**: typing.Optional[str]


# ListClusterSnapshotsOutputTypeDef

### snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterSnapshotInListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListClustersInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_elastic_classes.PaginatorConfigTypeDef]


# ListClustersInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListClustersOutputTypeDef

### clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterInListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPendingMaintenanceActionsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_elastic_classes.PaginatorConfigTypeDef]


# ListPendingMaintenanceActionsInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPendingMaintenanceActionsOutputTypeDef

### resourcePendingMaintenanceActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_elastic_classes.ResourcePendingMaintenanceActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingMaintenanceActionDetailsTypeDef

### action
- **Type**: <class 'str'>
- **Required**: Yes

### autoAppliedAfterDate
- **Type**: typing.Optional[str]

### currentApplyDate
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### forcedApplyDate
- **Type**: typing.Optional[str]

### optInStatus
- **Type**: typing.Optional[str]


# ResourcePendingMaintenanceActionTypeDef

### pendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_elastic_classes.PendingMaintenanceActionDetailsTypeDef]]

### resourceArn
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


# RestoreClusterFromSnapshotInputTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotArn
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]

### shardCapacity
- **Type**: typing.Optional[int]

### shardInstanceCount
- **Type**: typing.Optional[int]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# RestoreClusterFromSnapshotOutputTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ShardTypeDef

### createTime
- **Type**: <class 'str'>
- **Required**: Yes

### shardId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COPYING', 'CREATING', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE', 'INACCESSIBLE_ENCRYPTION_CREDS', 'INACCESSIBLE_SECRET_ARN', 'INACCESSIBLE_VPC_ENDPOINT', 'INCOMPATIBLE_NETWORK', 'INVALID_SECURITY_GROUP_ID', 'INVALID_SUBNET_ID', 'IP_ADDRESS_LIMIT_EXCEEDED', 'MAINTENANCE', 'MERGING', 'MODIFYING', 'SPLITTING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING', 'VPC_ENDPOINT_LIMIT_EXCEEDED']
- **Required**: Yes


# StartClusterInputTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartClusterOutputTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopClusterInputTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopClusterOutputTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateClusterInputTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### adminUserPassword
- **Type**: typing.Optional[str]

### authType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT', 'SECRET_ARN']]

### backupRetentionPeriod
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]

### preferredBackupWindow
- **Type**: typing.Optional[str]

### preferredMaintenanceWindow
- **Type**: typing.Optional[str]

### shardCapacity
- **Type**: typing.Optional[int]

### shardCount
- **Type**: typing.Optional[int]

### shardInstanceCount
- **Type**: typing.Optional[int]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateClusterOutputTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


