# Cloudhsmv2 Classes

# BackupRetentionPolicyTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['DAYS']]

### Value
- **Type**: typing.Optional[str]


# BackupTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudhsmv2_classes.TagTypeDef]]

### HsmType
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['FIPS', 'NON_FIPS']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificatesTypeDef

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


# ClusterTypeDef

### BackupPolicy
- **Type**: typing.Optional[typing.Literal['DEFAULT']]

### BackupRetentionPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2_classes.BackupRetentionPolicyTypeDef]

### ClusterId
- **Type**: typing.Optional[str]

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Hsms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudhsmv2_classes.HsmTypeDef]]

### HsmType
- **Type**: typing.Optional[str]

### PreCoPassword
- **Type**: typing.Optional[str]

### SecurityGroup
- **Type**: typing.Optional[str]

### SourceBackupId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'DEGRADED', 'DELETED', 'DELETE_IN_PROGRESS', 'INITIALIZED', 'INITIALIZE_IN_PROGRESS', 'UNINITIALIZED', 'UPDATE_IN_PROGRESS']]

### StateMessage
- **Type**: typing.Optional[str]

### SubnetMapping
- **Type**: typing.Optional[typing.Dict[str, str]]

### VpcId
- **Type**: typing.Optional[str]

### Certificates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2_classes.CertificatesTypeDef]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudhsmv2_classes.TagTypeDef]]

### Mode
- **Type**: typing.Optional[typing.Literal['FIPS', 'NON_FIPS']]


# CopyBackupToRegionRequestRequestTypeDef

### DestinationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudhsmv2_classes.TagTypeDef]]


# CopyBackupToRegionResponseTypeDef

### DestinationBackup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.DestinationBackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterRequestRequestTypeDef

### HsmType
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### BackupRetentionPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2_classes.BackupRetentionPolicyTypeDef]

### SourceBackupId
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudhsmv2_classes.TagTypeDef]]

### Mode
- **Type**: typing.Optional[typing.Literal['FIPS', 'NON_FIPS']]


# CreateClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHsmRequestRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: typing.Optional[str]


# CreateHsmResponseTypeDef

### Hsm
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.HsmTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBackupRequestRequestTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupResponseTypeDef

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.BackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterRequestRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteHsmRequestRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### HsmId
- **Type**: typing.Optional[str]

### EniId
- **Type**: typing.Optional[str]

### EniIp
- **Type**: typing.Optional[str]


# DeleteHsmResponseTypeDef

### HsmId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestRequestTypeDef

### ResourceArn
- **Type**: typing.Optional[str]


# DeleteResourcePolicyResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBackupsRequestDescribeBackupsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### Shared
- **Type**: typing.Optional[bool]

### SortAscending
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2_classes.PaginatorConfigTypeDef]


# DescribeBackupsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### Shared
- **Type**: typing.Optional[bool]

### SortAscending
- **Type**: typing.Optional[bool]


# DescribeBackupsResponseTypeDef

### Backups
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsmv2_classes.BackupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeClustersRequestDescribeClustersPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2_classes.PaginatorConfigTypeDef]


# DescribeClustersRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeClustersResponseTypeDef

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsmv2_classes.ClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DestinationBackupTypeDef

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceBackup
- **Type**: typing.Optional[str]

### SourceCluster
- **Type**: typing.Optional[str]


# GetResourcePolicyRequestRequestTypeDef

### ResourceArn
- **Type**: typing.Optional[str]


# GetResourcePolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HsmTypeDef

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

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'DEGRADED', 'DELETED', 'DELETE_IN_PROGRESS']]

### StateMessage
- **Type**: typing.Optional[str]


# InitializeClusterRequestRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### SignedCert
- **Type**: <class 'str'>
- **Required**: Yes

### TrustAnchor
- **Type**: <class 'str'>
- **Required**: Yes


# InitializeClusterResponseTypeDef

### State
- **Type**: typing.Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'DEGRADED', 'DELETED', 'DELETE_IN_PROGRESS', 'INITIALIZED', 'INITIALIZE_IN_PROGRESS', 'UNINITIALIZED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### StateMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsRequestListTagsPaginateTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsmv2_classes.PaginatorConfigTypeDef]


# ListTagsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsmv2_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ModifyBackupAttributesRequestRequestTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### NeverExpires
- **Type**: <class 'bool'>
- **Required**: Yes


# ModifyBackupAttributesResponseTypeDef

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.BackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyClusterRequestRequestTypeDef

### BackupRetentionPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.BackupRetentionPolicyTypeDef'>
- **Required**: Yes

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequestRequestTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Optional[str]


# PutResourcePolicyResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RestoreBackupRequestRequestTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreBackupResponseTypeDef

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.BackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsmv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudhsmv2_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.Sequence[str]
- **Required**: Yes


