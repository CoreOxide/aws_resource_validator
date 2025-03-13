# Opsworkscm Classes

# AccountAttributeTypeDef

### Name
- **Type**: typing.Optional[str]

### Maximum
- **Type**: typing.Optional[int]

### Used
- **Type**: typing.Optional[int]


# AssociateNodeRequestTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opsworkscm_classes.EngineAttributeTypeDef]
- **Required**: Yes


# AssociateNodeResponseTypeDef

### NodeAssociationStatusToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BackupTypeDef

### BackupArn
- **Type**: typing.Optional[str]

### BackupId
- **Type**: typing.Optional[str]

### BackupType
- **Type**: typing.Optional[typing.Literal['AUTOMATED', 'MANUAL']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineModel
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### InstanceProfileArn
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### KeyPair
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### S3DataSize
- **Type**: typing.Optional[int]

### S3DataUrl
- **Type**: typing.Optional[str]

### S3LogUrl
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### ServerName
- **Type**: typing.Optional[str]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'IN_PROGRESS', 'OK']]

### StatusDescription
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### ToolsVersion
- **Type**: typing.Optional[str]

### UserArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateBackupRequestTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworkscm_classes.TagTypeDef]]


# CreateBackupResponseTypeDef

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.BackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServerRequestTypeDef

### Engine
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### CustomDomain
- **Type**: typing.Optional[str]

### CustomCertificate
- **Type**: typing.Optional[str]

### CustomPrivateKey
- **Type**: typing.Optional[str]

### DisableAutomatedBackup
- **Type**: typing.Optional[bool]

### EngineModel
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EngineAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworkscm_classes.EngineAttributeTypeDef]]

### BackupRetentionCount
- **Type**: typing.Optional[int]

### KeyPair
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworkscm_classes.TagTypeDef]]

### BackupId
- **Type**: typing.Optional[str]


# CreateServerResponseTypeDef

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBackupRequestTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerRequestTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAttributesResponseTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm_classes.AccountAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBackupsRequestPaginateTypeDef

### BackupId
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm_classes.PaginatorConfigTypeDef]


# DescribeBackupsRequestTypeDef

### BackupId
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeBackupsResponseTypeDef

### Backups
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm_classes.BackupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsRequestPaginateTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm_classes.PaginatorConfigTypeDef]


# DescribeEventsRequestTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeEventsResponseTypeDef

### ServerEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm_classes.ServerEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeNodeAssociationStatusRequestTypeDef

### NodeAssociationStatusToken
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeAssociationStatusRequestWaitTypeDef

### NodeAssociationStatusToken
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm_classes.WaiterConfigTypeDef]


# DescribeNodeAssociationStatusResponseTypeDef

### NodeAssociationStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### EngineAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm_classes.EngineAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServersRequestPaginateTypeDef

### ServerName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm_classes.PaginatorConfigTypeDef]


# DescribeServersRequestTypeDef

### ServerName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeServersResponseTypeDef

### Servers
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm_classes.ServerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateNodeRequestTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworkscm_classes.EngineAttributeTypeDef]]


# DisassociateNodeResponseTypeDef

### NodeAssociationStatusToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EngineAttributeTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ExportServerEngineAttributeRequestTypeDef

### ExportAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworkscm_classes.EngineAttributeTypeDef]]


# ExportServerEngineAttributeResponseTypeDef

### EngineAttribute
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.EngineAttributeTypeDef'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# RestoreServerRequestTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[str]

### KeyPair
- **Type**: typing.Optional[str]


# RestoreServerResponseTypeDef

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServerEventTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ServerName
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### LogUrl
- **Type**: typing.Optional[str]


# ServerTypeDef

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### BackupRetentionCount
- **Type**: typing.Optional[int]

### ServerName
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### CloudFormationStackArn
- **Type**: typing.Optional[str]

### CustomDomain
- **Type**: typing.Optional[str]

### DisableAutomatedBackup
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### EngineModel
- **Type**: typing.Optional[str]

### EngineAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworkscm_classes.EngineAttributeTypeDef]]

### EngineVersion
- **Type**: typing.Optional[str]

### InstanceProfileArn
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### KeyPair
- **Type**: typing.Optional[str]

### MaintenanceStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCESS']]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['BACKING_UP', 'CONNECTION_LOST', 'CREATING', 'DELETING', 'FAILED', 'HEALTHY', 'MODIFYING', 'RESTORING', 'RUNNING', 'SETUP', 'TERMINATED', 'UNDER_MAINTENANCE', 'UNHEALTHY']]

### StatusReason
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### ServerArn
- **Type**: typing.Optional[str]


# StartMaintenanceRequestTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworkscm_classes.EngineAttributeTypeDef]]


# StartMaintenanceResponseTypeDef

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opsworkscm_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateServerEngineAttributesRequestTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# UpdateServerEngineAttributesResponseTypeDef

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServerRequestTypeDef

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### DisableAutomatedBackup
- **Type**: typing.Optional[bool]

### BackupRetentionCount
- **Type**: typing.Optional[int]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]


# UpdateServerResponseTypeDef

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


