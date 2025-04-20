# Cloudhsmv2 Cloudhsmv2 Classes

# Backup

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupArn
- **Type**: typing.Optional[str]

### BackupState
- **Type**: typing.Optional[typing.Literal['CREATE_IN_PROGRESS', 'DELETED', 'PENDING_DELETION', 'READY']]

### ClusterId
- **Type**: typing.Optional[str]

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CopyTimestamp
- **Type**: typing.Optional[datetime.datetime]

### NeverExpires
- **Type**: typing.Optional[bool]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceBackup
- **Type**: typing.Optional[str]

### SourceCluster
- **Type**: typing.Optional[str]

### DeleteTimestamp
- **Type**: typing.Optional[datetime.datetime]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Tag]]

### HsmType
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['FIPS', 'NON_FIPS']]


# BackupRetentionPolicy

### Type
- **Type**: typing.Optional[typing.Literal['DAYS']]

### Value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Certificates

### ClusterCsr
- **Type**: typing.Optional[str]

### HsmCertificate
- **Type**: typing.Optional[str]

### AwsHardwareCertificate
- **Type**: typing.Optional[str]

### ManufacturerHardwareCertificate
- **Type**: typing.Optional[str]

### ClusterCertificate
- **Type**: typing.Optional[str]


# Cluster

### BackupPolicy
- **Type**: typing.Optional[typing.Literal['DEFAULT']]

### BackupRetentionPolicy
- **Type**: <class 'NoneType'>

### ClusterId
- **Type**: typing.Optional[str]

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Hsms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Hsm]]

### HsmType
- **Type**: typing.Optional[str]

### HsmTypeRollbackExpiration
- **Type**: typing.Optional[datetime.datetime]

### PreCoPassword
- **Type**: typing.Optional[str]

### SecurityGroup
- **Type**: typing.Optional[str]

### SourceBackupId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'DEGRADED', 'DELETED', 'DELETE_IN_PROGRESS', 'INITIALIZED', 'INITIALIZE_IN_PROGRESS', 'MODIFY_IN_PROGRESS', 'ROLLBACK_IN_PROGRESS', 'UNINITIALIZED', 'UPDATE_IN_PROGRESS']]

### StateMessage
- **Type**: typing.Optional[str]

### SubnetMapping
- **Type**: typing.Optional[typing.Dict[str, str]]

### VpcId
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4']]

### Certificates
- **Type**: <class 'NoneType'>

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Tag]]

### Mode
- **Type**: typing.Optional[typing.Literal['FIPS', 'NON_FIPS']]


# CopyBackupToRegionRequest

### DestinationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Tag]]


# CopyBackupToRegionResponse

### DestinationBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.DestinationBackup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterRequest

### HsmType
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### BackupRetentionPolicy
- **Type**: <class 'NoneType'>

### SourceBackupId
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[typing.Literal['DUALSTACK', 'IPV4']]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Tag]]

### Mode
- **Type**: typing.Optional[typing.Literal['FIPS', 'NON_FIPS']]


# CreateClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHsmRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: typing.Optional[str]


# CreateHsmResponse

### Hsm
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Hsm'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBackupRequest

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupResponse

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Backup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteHsmRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### HsmId
- **Type**: typing.Optional[str]

### EniId
- **Type**: typing.Optional[str]

### EniIp
- **Type**: typing.Optional[str]


# DeleteHsmResponse

### HsmId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: typing.Optional[str]


# DeleteResourcePolicyResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBackupsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Shared
- **Type**: typing.Optional[bool]

### SortAscending
- **Type**: typing.Optional[bool]


# DescribeBackupsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Shared
- **Type**: typing.Optional[bool]

### SortAscending
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.PaginatorConfig]


# DescribeBackupsResponse

### Backups
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Backup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeClustersRequest

### Filters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeClustersRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.PaginatorConfig]


# DescribeClustersResponse

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Cluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DestinationBackup

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceBackup
- **Type**: typing.Optional[str]

### SourceCluster
- **Type**: typing.Optional[str]


# GetResourcePolicyRequest

### ResourceArn
- **Type**: typing.Optional[str]


# GetResourcePolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# Hsm

### HsmId
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### EniId
- **Type**: typing.Optional[str]

### EniIp
- **Type**: typing.Optional[str]

### EniIpV6
- **Type**: typing.Optional[str]

### HsmType
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'DEGRADED', 'DELETED', 'DELETE_IN_PROGRESS']]

### StateMessage
- **Type**: typing.Optional[str]


# InitializeClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### SignedCert
- **Type**: <class 'str'>
- **Required**: Yes

### TrustAnchor
- **Type**: <class 'str'>
- **Required**: Yes


# InitializeClusterResponse

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'DEGRADED', 'DELETED', 'DELETE_IN_PROGRESS', 'INITIALIZED', 'INITIALIZE_IN_PROGRESS', 'MODIFY_IN_PROGRESS', 'ROLLBACK_IN_PROGRESS', 'UNINITIALIZED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### StateMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsRequestPaginate

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.PaginatorConfig]


# ListTagsResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ModifyBackupAttributesRequest

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### NeverExpires
- **Type**: <class 'bool'>
- **Required**: Yes


# ModifyBackupAttributesResponse

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Backup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### HsmType
- **Type**: typing.Optional[str]

### BackupRetentionPolicy
- **Type**: <class 'NoneType'>


# ModifyClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequest

### ResourceArn
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Optional[str]


# PutResourcePolicyResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


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


# RestoreBackupRequest

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreBackupResponse

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Backup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsmv2.cloudhsmv2_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.List[str]
- **Required**: Yes


