# Cloudhsm Cloudhsm Classes

# AddTagsToResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.Tag]
- **Required**: Yes


# AddTagsToResourceResponse

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateHapgRequest

### Label
- **Type**: <class 'str'>
- **Required**: Yes


# CreateHapgResponse

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHsmRequest

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


# CreateHsmResponse

### HsmArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLunaClientRequest

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]


# CreateLunaClientResponse

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteHapgRequest

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHapgResponse

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteHsmRequest

### HsmArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHsmResponse

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLunaClientRequest

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLunaClientResponse

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHapgRequest

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHapgResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHsmRequest

### HsmArn
- **Type**: typing.Optional[str]

### HsmSerialNumber
- **Type**: typing.Optional[str]


# DescribeHsmResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLunaClientRequest

### ClientArn
- **Type**: typing.Optional[str]

### CertificateFingerprint
- **Type**: typing.Optional[str]


# DescribeLunaClientResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigRequest

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientVersion
- **Type**: typing.Literal['5.1', '5.3']
- **Required**: Yes

### HapgList
- **Type**: typing.List[str]
- **Required**: Yes


# GetConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# ListAvailableZonesResponse

### AZList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# ListHapgsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListHapgsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.PaginatorConfig]


# ListHapgsResponse

### HapgList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHsmsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListHsmsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.PaginatorConfig]


# ListHsmsResponse

### HsmList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLunaClientsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListLunaClientsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.PaginatorConfig]


# ListLunaClientsResponse

### ClientList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyHapgRequest

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes

### Label
- **Type**: typing.Optional[str]

### PartitionSerialList
- **Type**: typing.Optional[typing.List[str]]


# ModifyHapgResponse

### HapgArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyHsmRequest

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


# ModifyHsmResponse

### HsmArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyLunaClientRequest

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyLunaClientResponse

### ClientArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RemoveTagsFromResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.List[str]
- **Required**: Yes


# RemoveTagsFromResourceResponse

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_classes.ResponseMetadata'>
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


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


