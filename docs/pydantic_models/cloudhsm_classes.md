# Cloudhsm Classes

# AddTagsToResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudhsm_classes.TagTypeDef]
- **Required**: Yes


# AddTagsToResourceResponseTypeDef

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateHapgRequestTypeDef

### Label
- **Type**: <class 'str'>
- **Required**: Yes


# CreateHapgResponseTypeDef

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHsmRequestTypeDef

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### SshKey
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionType
- **Type**: typing.Literal['PRODUCTION']
- **Required**: Yes

### EniIp
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### SyslogIp
- **Type**: typing.Optional[str]


# CreateHsmResponseTypeDef

### HsmArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLunaClientRequestTypeDef

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]


# CreateLunaClientResponseTypeDef

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteHapgRequestTypeDef

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHapgResponseTypeDef

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteHsmRequestTypeDef

### HsmArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHsmResponseTypeDef

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLunaClientRequestTypeDef

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLunaClientResponseTypeDef

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHapgRequestTypeDef

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHapgResponseTypeDef

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes

### HapgSerial
- **Type**: <class 'str'>
- **Required**: Yes

### HsmsLastActionFailed
- **Type**: typing.List[str]
- **Required**: Yes

### HsmsPendingDeletion
- **Type**: typing.List[str]
- **Required**: Yes

### HsmsPendingRegistration
- **Type**: typing.List[str]
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionSerialList
- **Type**: typing.List[str]
- **Required**: Yes

### State
- **Type**: typing.Literal['DEGRADED', 'READY', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHsmRequestTypeDef

### HsmArn
- **Type**: typing.Optional[str]

### HsmSerialNumber
- **Type**: typing.Optional[str]


# DescribeHsmResponseTypeDef

### HsmArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DEGRADED', 'PENDING', 'RUNNING', 'SUSPENDED', 'TERMINATED', 'TERMINATING', 'UPDATING']
- **Required**: Yes

### StatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### EniId
- **Type**: <class 'str'>
- **Required**: Yes

### EniIp
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionType
- **Type**: typing.Literal['PRODUCTION']
- **Required**: Yes

### SubscriptionStartDate
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionEndDate
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### HsmType
- **Type**: <class 'str'>
- **Required**: Yes

### SoftwareVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKey
- **Type**: <class 'str'>
- **Required**: Yes

### SshKeyLastUpdated
- **Type**: <class 'str'>
- **Required**: Yes

### ServerCertUri
- **Type**: <class 'str'>
- **Required**: Yes

### ServerCertLastUpdated
- **Type**: <class 'str'>
- **Required**: Yes

### Partitions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLunaClientRequestTypeDef

### ClientArn
- **Type**: typing.Optional[str]

### CertificateFingerprint
- **Type**: typing.Optional[str]


# DescribeLunaClientResponseTypeDef

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateFingerprint
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigRequestTypeDef

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientVersion
- **Type**: typing.Literal['5.1', '5.3']
- **Required**: Yes

### HapgList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetConfigResponseTypeDef

### ConfigType
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigFile
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigCred
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAvailableZonesResponseTypeDef

### AZList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListHapgsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsm_classes.PaginatorConfigTypeDef]


# ListHapgsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListHapgsResponseTypeDef

### HapgList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHsmsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsm_classes.PaginatorConfigTypeDef]


# ListHsmsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListHsmsResponseTypeDef

### HsmList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLunaClientsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsm_classes.PaginatorConfigTypeDef]


# ListLunaClientsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListLunaClientsResponseTypeDef

### ClientList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsm_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyHapgRequestTypeDef

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]

### PartitionSerialList
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyHapgResponseTypeDef

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyHsmRequestTypeDef

### HsmArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: typing.Optional[str]

### EniIp
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]

### SyslogIp
- **Type**: typing.Optional[str]


# ModifyHsmResponseTypeDef

### HsmArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyLunaClientRequestTypeDef

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyLunaClientResponseTypeDef

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RemoveTagsFromResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveTagsFromResourceResponseTypeDef

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm_classes.ResponseMetadataTypeDef'>
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


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


