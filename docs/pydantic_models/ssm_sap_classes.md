# Ssm Sap Classes

# Application

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['HANA', 'SAP_ABAP']]

### Arn
- **Type**: typing.Optional[str]

### AppRegistryArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'DELETING', 'FAILED', 'REGISTERING', 'STARTING', 'STOPPED', 'STOPPING', 'UNKNOWN']]

### DiscoveryStatus
- **Type**: typing.Optional[typing.Literal['DELETING', 'REFRESH_FAILED', 'REGISTERING', 'REGISTRATION_FAILED', 'SUCCESS']]

### Components
- **Type**: typing.Optional[typing.List[str]]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]

### AssociatedApplicationArns
- **Type**: typing.Optional[typing.List[str]]


# ApplicationCredential

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### CredentialType
- **Type**: typing.Literal['ADMIN']
- **Required**: Yes

### SecretId
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationSummary

### Id
- **Type**: typing.Optional[str]

### DiscoveryStatus
- **Type**: typing.Optional[typing.Literal['DELETING', 'REFRESH_FAILED', 'REGISTERING', 'REGISTRATION_FAILED', 'SUCCESS']]

### Type
- **Type**: typing.Optional[typing.Literal['HANA', 'SAP_ABAP']]

### Arn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssociatedHost

### Hostname
- **Type**: typing.Optional[str]

### Ec2InstanceId
- **Type**: typing.Optional[str]

### IpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.IpAddressMember]]

### OsVersion
- **Type**: typing.Optional[str]


# BackintConfig

### BackintMode
- **Type**: typing.Literal['AWSBackup']
- **Required**: Yes

### EnsureNoBackupInProcess
- **Type**: <class 'bool'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Component

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
- **Type**: <class 'NoneType'>

### AssociatedHost
- **Type**: <class 'NoneType'>

### Databases
- **Type**: typing.Optional[typing.List[str]]

### Hosts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Host]]

### PrimaryHost
- **Type**: typing.Optional[str]

### DatabaseConnection
- **Type**: <class 'NoneType'>

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]


# ComponentInfo

### ComponentType
- **Type**: typing.Literal['ABAP', 'ASCS', 'DIALOG', 'ERS', 'HANA', 'HANA_NODE', 'WD', 'WEBDISP']
- **Required**: Yes

### Sid
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# ComponentSummary

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


# Database

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### Credentials
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ApplicationCredential]]

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


# DatabaseConnection

### DatabaseConnectionMethod
- **Type**: typing.Optional[typing.Literal['DIRECT', 'OVERLAY']]

### DatabaseArn
- **Type**: typing.Optional[str]

### ConnectionIp
- **Type**: typing.Optional[str]


# DatabaseSummary

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


# DeleteResourcePermissionInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionType
- **Type**: typing.Optional[typing.Literal['RESTORE']]

### SourceResourceArn
- **Type**: typing.Optional[str]


# DeleteResourcePermissionOutput

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterApplicationInput

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# Filter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['Equals', 'GreaterThanOrEquals', 'LessThanOrEquals']
- **Required**: Yes


# GetApplicationInput

### ApplicationId
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### AppRegistryArn
- **Type**: typing.Optional[str]


# GetApplicationOutput

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Application'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# GetComponentInput

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentOutput

### Component
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Component'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# GetDatabaseInput

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### DatabaseId
- **Type**: typing.Optional[str]

### DatabaseArn
- **Type**: typing.Optional[str]


# GetDatabaseOutput

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Database'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# GetOperationInput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOperationOutput

### Operation
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePermissionInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionType
- **Type**: typing.Optional[typing.Literal['RESTORE']]


# GetResourcePermissionOutput

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# Host

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


# IpAddressMember

### IpAddress
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]

### AllocationType
- **Type**: typing.Optional[typing.Literal['ELASTIC_IP', 'OVERLAY', 'UNKNOWN', 'VPC_SUBNET']]


# ListApplicationsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Filter]]


# ListApplicationsInputPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.PaginatorConfig]


# ListApplicationsOutput

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComponentsInput

### ApplicationId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComponentsInputPaginate

### ApplicationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.PaginatorConfig]


# ListComponentsOutput

### Components
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ComponentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatabasesInput

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatabasesInputPaginate

### ApplicationId
- **Type**: typing.Optional[str]

### ComponentId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.PaginatorConfig]


# ListDatabasesOutput

### Databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.DatabaseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOperationEventsInput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Filter]]


# ListOperationEventsInputPaginate

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.PaginatorConfig]


# ListOperationEventsOutput

### OperationEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.OperationEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOperationsInput

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Filter]]


# ListOperationsInputPaginate

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.PaginatorConfig]


# ListOperationsOutput

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# Operation

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ERROR', 'INPROGRESS', 'SUCCESS']]

### StatusMessage
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# OperationEvent

### Description
- **Type**: typing.Optional[str]

### Resource
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePermissionInput

### ActionType
- **Type**: typing.Literal['RESTORE']
- **Required**: Yes

### SourceResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePermissionOutput

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterApplicationInput

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationType
- **Type**: typing.Literal['HANA', 'SAP_ABAP']
- **Required**: Yes

### Instances
- **Type**: typing.List[str]
- **Required**: Yes

### SapInstanceNumber
- **Type**: typing.Optional[str]

### Sid
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Credentials
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ApplicationCredential]]

### DatabaseArn
- **Type**: typing.Optional[str]

### ComponentsInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ComponentInfo]]


# RegisterApplicationOutput

### Application
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.Application'>
- **Required**: Yes

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# Resilience

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


# Resource

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
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


# StartApplicationInput

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartApplicationOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# StartApplicationRefreshInput

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartApplicationRefreshOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


# StopApplicationInput

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### StopConnectedEntity
- **Type**: typing.Optional[typing.Literal['DBMS']]

### IncludeEc2InstanceShutdown
- **Type**: typing.Optional[bool]


# StopApplicationOutput

### OperationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
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


# UpdateApplicationSettingsInput

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CredentialsToAddOrUpdate
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ApplicationCredential]]

### CredentialsToRemove
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ApplicationCredential]]

### Backint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.BackintConfig]

### DatabaseArn
- **Type**: typing.Optional[str]


# UpdateApplicationSettingsOutput

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### OperationIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_classes.ResponseMetadata'>
- **Required**: Yes


