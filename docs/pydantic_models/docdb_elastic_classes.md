# Docdb Elastic Classes

# ApplyPendingMaintenanceActionInput

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


# ApplyPendingMaintenanceActionOutput

### resourcePendingMaintenanceAction
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResourcePendingMaintenanceAction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Cluster

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.Shard]]


# ClusterInList

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COPYING', 'CREATING', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE', 'INACCESSIBLE_ENCRYPTION_CREDS', 'INACCESSIBLE_SECRET_ARN', 'INACCESSIBLE_VPC_ENDPOINT', 'INCOMPATIBLE_NETWORK', 'INVALID_SECURITY_GROUP_ID', 'INVALID_SUBNET_ID', 'IP_ADDRESS_LIMIT_EXCEEDED', 'MAINTENANCE', 'MERGING', 'MODIFYING', 'SPLITTING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING', 'VPC_ENDPOINT_LIMIT_EXCEEDED']
- **Required**: Yes


# ClusterSnapshot

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


# ClusterSnapshotInList

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


# CopyClusterSnapshotInput

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CopyClusterSnapshotOutput

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterInput

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
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# CreateClusterOutput

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterSnapshotInput

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateClusterSnapshotOutput

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterInput

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterOutput

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterSnapshotInput

### snapshotArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterSnapshotOutput

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# GetClusterInput

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetClusterOutput

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# GetClusterSnapshotInput

### snapshotArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetClusterSnapshotOutput

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ClusterSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# GetPendingMaintenanceActionInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPendingMaintenanceActionOutput

### resourcePendingMaintenanceAction
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResourcePendingMaintenanceAction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# ListClusterSnapshotsInput

### clusterArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### snapshotType
- **Type**: typing.Optional[str]


# ListClusterSnapshotsInputPaginate

### clusterArn
- **Type**: typing.Optional[str]

### snapshotType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.PaginatorConfig]


# ListClusterSnapshotsOutput

### snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ClusterSnapshotInList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListClustersInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListClustersInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.PaginatorConfig]


# ListClustersOutput

### clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ClusterInList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPendingMaintenanceActionsInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPendingMaintenanceActionsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.PaginatorConfig]


# ListPendingMaintenanceActionsOutput

### resourcePendingMaintenanceActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResourcePendingMaintenanceAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingMaintenanceActionDetails

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


# ResourcePendingMaintenanceAction

### pendingMaintenanceActionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.PendingMaintenanceActionDetails]]

### resourceArn
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


# RestoreClusterFromSnapshotInput

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
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# RestoreClusterFromSnapshotOutput

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# Shard

### createTime
- **Type**: <class 'str'>
- **Required**: Yes

### shardId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'COPYING', 'CREATING', 'DELETING', 'INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE', 'INACCESSIBLE_ENCRYPTION_CREDS', 'INACCESSIBLE_SECRET_ARN', 'INACCESSIBLE_VPC_ENDPOINT', 'INCOMPATIBLE_NETWORK', 'INVALID_SECURITY_GROUP_ID', 'INVALID_SUBNET_ID', 'IP_ADDRESS_LIMIT_EXCEEDED', 'MAINTENANCE', 'MERGING', 'MODIFYING', 'SPLITTING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING', 'VPC_ENDPOINT_LIMIT_EXCEEDED']
- **Required**: Yes


# StartClusterInput

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartClusterOutput

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# StopClusterInput

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopClusterOutput

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateClusterInput

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
- **Type**: typing.Optional[typing.List[str]]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# UpdateClusterOutput

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.docdb_elastic.docdb_elastic_classes.ResponseMetadata'>
- **Required**: Yes


