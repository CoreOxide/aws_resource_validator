# Opsworkscm Opsworkscm Classes

# AccountAttribute

### Name
- **Type**: typing.Optional[str]

### Maximum
- **Type**: typing.Optional[int]

### Used
- **Type**: typing.Optional[int]


# AssociateNodeRequest

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.EngineAttribute]
- **Required**: Yes


# AssociateNodeResponse

### NodeAssociationStatusToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# Backup

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

# CreateBackupRequest

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Tag]]


# CreateBackupResponse

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Backup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServerRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.EngineAttribute]]

### BackupRetentionCount
- **Type**: typing.Optional[int]

### KeyPair
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Tag]]

### BackupId
- **Type**: typing.Optional[str]


# CreateServerResponse

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Server'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBackupRequest

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerRequest

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAttributesResponse

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.AccountAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBackupsRequest

### BackupId
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeBackupsRequestPaginate

### BackupId
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.PaginatorConfig]


# DescribeBackupsResponse

### Backups
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Backup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventsRequest

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeEventsRequestPaginate

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.PaginatorConfig]


# DescribeEventsResponse

### ServerEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ServerEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeNodeAssociationStatusRequest

### NodeAssociationStatusToken
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeAssociationStatusRequestWait

### NodeAssociationStatusToken
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeNodeAssociationStatusResponse

### NodeAssociationStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### EngineAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.EngineAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServersRequest

### ServerName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeServersRequestPaginate

### ServerName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.PaginatorConfig]


# DescribeServersResponse

### Servers
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Server]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateNodeRequest

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.EngineAttribute]]


# DisassociateNodeResponse

### NodeAssociationStatusToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# EngineAttribute

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ExportServerEngineAttributeRequest

### ExportAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### InputAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.EngineAttribute]]


# ExportServerEngineAttributeResponse

### EngineAttribute
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.EngineAttribute'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# RestoreServerRequest

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


# RestoreServerResponse

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Server'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# Server

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.EngineAttribute]]

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


# ServerEvent

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ServerName
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### LogUrl
- **Type**: typing.Optional[str]


# StartMaintenanceRequest

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### EngineAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.EngineAttribute]]


# StartMaintenanceResponse

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Server'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateServerEngineAttributesRequest

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[str]


# UpdateServerEngineAttributesResponse

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Server'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServerRequest

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


# UpdateServerResponse

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.Server'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


