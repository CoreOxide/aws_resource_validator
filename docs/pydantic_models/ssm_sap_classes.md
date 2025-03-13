# Ssm Sap Classes

# ApplicationCredentialTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CredentialType
- **Type**: typing.Literal['ADMIN']
- **Required**: Yes

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApplicationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociatedHostTypeDef

### Hostname
- **Type**: typing.Optional[str]

### Ec2InstanceId
- **Type**: typing.Optional[str]

### IpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap_classes.IpAddressMemberTypeDef]]

### OsVersion
- **Type**: typing.Optional[str]


# BackintConfigTypeDef

### BackintMode
- **Type**: typing.Literal['AWSBackup']
- **Required**: Yes

### EnsureNoBackupInProcess
- **Type**: <class 'bool'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentInfoTypeDef

### ComponentType
- **Type**: typing.Literal['ABAP', 'ASCS', 'DIALOG', 'ERS', 'HANA', 'HANA_NODE', 'WD', 'WEBDISP']
- **Required**: Yes

### Sid
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# ComponentSummaryTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### ComponentType
- **Type**: typing.Optional[typing.Literal['ABAP', 'ASCS', 'DIALOG', 'ERS', 'HANA', 'HANA_NODE', 'WD', 'WEBDISP']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Arn
- **Type**: typing.Optional[str]


# ComponentTypeDef

### ComponentId
- **Type**: typing.Optional[str]

### Sid
- **Type**: typing.Optional[str]

### SystemNumber
- **Type**: typing.Optional[str]

### ParentComponent
- **Type**: typing.Optional[str]

### ChildComponents
- **Type**: typing.Optional[typing.List[str]]

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentType
- **Type**: typing.Optional[typing.Literal['ABAP', 'ASCS', 'DIALOG', 'ERS', 'HANA', 'HANA_NODE', 'WD', 'WEBDISP']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'RUNNING', 'RUNNING_WITH_ERROR', 'STARTING', 'STOPPED', 'STOPPING', 'UNDEFINED']]

### SapHostname
- **Type**: typing.Optional[str]

### SapFeature
- **Type**: typing.Optional[str]

### SapKernelVersion
- **Type**: typing.Optional[str]

### HdbVersion
- **Type**: typing.Optional[str]

### Resilience
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.ResilienceTypeDef]

### AssociatedHost
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.AssociatedHostTypeDef]

### Databases
- **Type**: typing.Optional[typing.List[str]]

### Hosts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap_classes.HostTypeDef]]

### PrimaryHost
- **Type**: typing.Optional[str]

### DatabaseConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.DatabaseConnectionTypeDef]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]


# DatabaseConnectionTypeDef

### DatabaseConnectionMethod
- **Type**: typing.Optional[typing.Literal['DIRECT', 'OVERLAY']]

### DatabaseArn
- **Type**: typing.Optional[str]

### ConnectionIp
- **Type**: typing.Optional[str]


# DatabaseSummaryTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseType
- **Type**: typing.Optional[typing.Literal['SYSTEM', 'TENANT']]

### Arn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DatabaseTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### Credentials
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap_classes.ApplicationCredentialTypeDef]]

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### DatabaseType
- **Type**: typing.Optional[typing.Literal['SYSTEM', 'TENANT']]

### Arn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ERROR', 'RUNNING', 'STARTING', 'STOPPED', 'UNKNOWN', 'WARNING']]

### PrimaryHost
- **Type**: typing.Optional[str]

### SQLPort
- **Type**: typing.Optional[int]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### ConnectedComponentArns
- **Type**: typing.Optional[typing.List[str]]


# DeleteResourcePermissionInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionType
- **Type**: typing.Optional[typing.Literal['RESTORE']]

### SourceResourceArn
- **Type**: typing.Optional[str]


# DeleteResourcePermissionOutputTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterApplicationInputTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['Equals', 'GreaterThanOrEquals', 'LessThanOrEquals']
- **Required**: Yes


# GetApplicationInputTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### AppRegistryArn
- **Type**: typing.Optional[str]


# GetApplicationOutputTypeDef

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ApplicationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComponentInputTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentOutputTypeDef

### Component
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ComponentTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDatabaseInputTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseArn
- **Type**: typing.Optional[str]


# GetDatabaseOutputTypeDef

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.DatabaseTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOperationInputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOperationOutputTypeDef

### Operation
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePermissionInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionType
- **Type**: typing.Optional[typing.Literal['RESTORE']]


# GetResourcePermissionOutputTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HostTypeDef

### HostName
- **Type**: typing.Optional[str]

### HostIp
- **Type**: typing.Optional[str]

### EC2InstanceId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### HostRole
- **Type**: typing.Optional[typing.Literal['LEADER', 'STANDBY', 'UNKNOWN', 'WORKER']]

### OsVersion
- **Type**: typing.Optional[str]


# IpAddressMemberTypeDef

### IpAddress
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]

### AllocationType
- **Type**: typing.Optional[typing.Literal['ELASTIC_IP', 'OVERLAY', 'UNKNOWN', 'VPC_SUBNET']]


# ListApplicationsInputPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.PaginatorConfigTypeDef]


# ListApplicationsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.FilterTypeDef]]


# ListApplicationsOutputTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComponentsInputPaginateTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.PaginatorConfigTypeDef]


# ListComponentsInputTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComponentsOutputTypeDef

### Components
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap_classes.ComponentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatabasesInputPaginateTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.PaginatorConfigTypeDef]


# ListDatabasesInputTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatabasesOutputTypeDef

### Databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap_classes.DatabaseSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOperationEventsInputPaginateTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.PaginatorConfigTypeDef]


# ListOperationEventsInputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.FilterTypeDef]]


# ListOperationEventsOutputTypeDef

### OperationEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap_classes.OperationEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOperationsInputPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.PaginatorConfigTypeDef]


# ListOperationsInputTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.FilterTypeDef]]


# ListOperationsOutputTypeDef

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OperationEventTypeDef

### Description
- **Type**: typing.Optional[str]

### Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.ResourceTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# OperationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePermissionInputTypeDef

### ActionType
- **Type**: typing.Literal['RESTORE']
- **Required**: Yes

### SourceResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePermissionOutputTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterApplicationInputTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationType
- **Type**: typing.Literal['HANA', 'SAP_ABAP']
- **Required**: Yes

### Instances
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SapInstanceNumber
- **Type**: typing.Optional[str]

### Sid
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Credentials
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.ApplicationCredentialTypeDef]]

### DatabaseArn
- **Type**: typing.Optional[str]

### ComponentsInfo
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.ComponentInfoTypeDef]]


# RegisterApplicationOutputTypeDef

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ApplicationTypeDef'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResilienceTypeDef

### HsrTier
- **Type**: typing.Optional[str]

### HsrReplicationMode
- **Type**: typing.Optional[typing.Literal['ASYNC', 'NONE', 'PRIMARY', 'SYNC', 'SYNCMEM']]

### HsrOperationMode
- **Type**: typing.Optional[typing.Literal['DELTA_DATASHIPPING', 'LOGREPLAY', 'LOGREPLAY_READACCESS', 'NONE', 'PRIMARY']]

### ClusterStatus
- **Type**: typing.Optional[typing.Literal['MAINTENANCE', 'NONE', 'OFFLINE', 'ONLINE', 'STANDBY']]

### EnqueueReplication
- **Type**: typing.Optional[bool]


# ResourceTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
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


# StartApplicationInputTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartApplicationOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartApplicationRefreshInputTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartApplicationRefreshOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopApplicationInputTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### StopConnectedEntity
- **Type**: typing.Optional[typing.Literal['DBMS']]

### IncludeEc2InstanceShutdown
- **Type**: typing.Optional[bool]


# StopApplicationOutputTypeDef

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
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


# UpdateApplicationSettingsInputTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CredentialsToAddOrUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.ApplicationCredentialTypeDef]]

### CredentialsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_sap_classes.ApplicationCredentialTypeDef]]

### Backint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap_classes.BackintConfigTypeDef]

### DatabaseArn
- **Type**: typing.Optional[str]


# UpdateApplicationSettingsOutputTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### OperationIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


