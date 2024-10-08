# Pydantic Models in mq_classes

# ActionRequiredTypeDef

### ActionRequiredCode
- **Type**: typing.Optional[str]

### ActionRequiredInfo
- **Type**: typing.Optional[str]


# AvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrokerEngineTypeTypeDef

### EngineType
- **Type**: typing.Optional[typing.Literal['ACTIVEMQ', 'RABBITMQ']]

### EngineVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mq_classes.EngineVersionTypeDef]]


# BrokerInstanceOptionTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mq_classes.AvailabilityZoneTypeDef]]

### EngineType
- **Type**: typing.Optional[typing.Literal['ACTIVEMQ', 'RABBITMQ']]

### HostInstanceType
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[typing.Literal['EBS', 'EFS']]

### SupportedDeploymentModes
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE_STANDBY_MULTI_AZ', 'CLUSTER_MULTI_AZ', 'SINGLE_INSTANCE']]]

### SupportedEngineVersions
- **Type**: typing.Optional[typing.List[str]]


# BrokerInstanceTypeDef

### ConsoleURL
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.List[str]]

### IpAddress
- **Type**: typing.Optional[str]


# BrokerSummaryTypeDef

### DeploymentMode
- **Type**: typing.Literal['ACTIVE_STANDBY_MULTI_AZ', 'CLUSTER_MULTI_AZ', 'SINGLE_INSTANCE']
- **Required**: Yes

### EngineType
- **Type**: typing.Literal['ACTIVEMQ', 'RABBITMQ']
- **Required**: Yes

### BrokerArn
- **Type**: typing.Optional[str]

### BrokerId
- **Type**: typing.Optional[str]

### BrokerName
- **Type**: typing.Optional[str]

### BrokerState
- **Type**: typing.Optional[typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CRITICAL_ACTION_REQUIRED', 'DELETION_IN_PROGRESS', 'REBOOT_IN_PROGRESS', 'REPLICA', 'RUNNING']]

### Created
- **Type**: typing.Optional[datetime.datetime]

### HostInstanceType
- **Type**: typing.Optional[str]


# ConfigurationIdTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Revision
- **Type**: typing.Optional[int]


# ConfigurationRevisionTypeDef

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ConfigurationTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Literal['LDAP', 'SIMPLE']
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EngineType
- **Type**: typing.Literal['ACTIVEMQ', 'RABBITMQ']
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ConfigurationRevisionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConfigurationsTypeDef

### Current
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.ConfigurationIdTypeDef]

### History
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mq_classes.ConfigurationIdTypeDef]]

### Pending
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.ConfigurationIdTypeDef]


# CreateBrokerRequestRequestTypeDef

### BrokerName
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentMode
- **Type**: typing.Literal['ACTIVE_STANDBY_MULTI_AZ', 'CLUSTER_MULTI_AZ', 'SINGLE_INSTANCE']
- **Required**: Yes

### EngineType
- **Type**: typing.Literal['ACTIVEMQ', 'RABBITMQ']
- **Required**: Yes

### HostInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### PubliclyAccessible
- **Type**: <class 'bool'>
- **Required**: Yes

### Users
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mq_classes.UserTypeDef]
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Optional[typing.Literal['LDAP', 'SIMPLE']]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.ConfigurationIdTypeDef]

### CreatorRequestId
- **Type**: typing.Optional[str]

### EncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.EncryptionOptionsTypeDef]

### EngineVersion
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.LdapServerMetadataInputTypeDef]

### Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.LogsTypeDef]

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.WeeklyStartTimeTypeDef]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### StorageType
- **Type**: typing.Optional[typing.Literal['EBS', 'EFS']]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DataReplicationMode
- **Type**: typing.Optional[typing.Literal['CRDR', 'NONE']]

### DataReplicationPrimaryBrokerArn
- **Type**: typing.Optional[str]


# CreateBrokerResponseTypeDef

### BrokerArn
- **Type**: <class 'str'>
- **Required**: Yes

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfigurationRequestRequestTypeDef

### EngineType
- **Type**: typing.Literal['ACTIVEMQ', 'RABBITMQ']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Optional[typing.Literal['LDAP', 'SIMPLE']]

### EngineVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Literal['LDAP', 'SIMPLE']
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ConfigurationRevisionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTagsRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateUserRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ConsoleAccess
- **Type**: typing.Optional[bool]

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]

### ReplicationUser
- **Type**: typing.Optional[bool]


# DataReplicationCounterpartTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# DataReplicationMetadataOutputTypeDef

### DataReplicationRole
- **Type**: <class 'str'>
- **Required**: Yes

### DataReplicationCounterpart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.DataReplicationCounterpartTypeDef]


# DeleteBrokerRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBrokerResponseTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTagsRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBrokerEngineTypesRequestRequestTypeDef

### EngineType
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBrokerEngineTypesResponseTypeDef

### BrokerEngineTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.BrokerEngineTypeTypeDef]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBrokerInstanceOptionsRequestRequestTypeDef

### EngineType
- **Type**: typing.Optional[str]

### HostInstanceType
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]


# DescribeBrokerInstanceOptionsResponseTypeDef

### BrokerInstanceOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.BrokerInstanceOptionTypeDef]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBrokerRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBrokerResponseTypeDef

### ActionsRequired
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.ActionRequiredTypeDef]
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Literal['LDAP', 'SIMPLE']
- **Required**: Yes

### AutoMinorVersionUpgrade
- **Type**: <class 'bool'>
- **Required**: Yes

### BrokerArn
- **Type**: <class 'str'>
- **Required**: Yes

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### BrokerInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.BrokerInstanceTypeDef]
- **Required**: Yes

### BrokerName
- **Type**: <class 'str'>
- **Required**: Yes

### BrokerState
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CRITICAL_ACTION_REQUIRED', 'DELETION_IN_PROGRESS', 'REBOOT_IN_PROGRESS', 'REPLICA', 'RUNNING']
- **Required**: Yes

### Configurations
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ConfigurationsTypeDef'>
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeploymentMode
- **Type**: typing.Literal['ACTIVE_STANDBY_MULTI_AZ', 'CLUSTER_MULTI_AZ', 'SINGLE_INSTANCE']
- **Required**: Yes

### EncryptionOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.EncryptionOptionsTypeDef'>
- **Required**: Yes

### EngineType
- **Type**: typing.Literal['ACTIVEMQ', 'RABBITMQ']
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HostInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### LdapServerMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.LdapServerMetadataOutputTypeDef'>
- **Required**: Yes

### Logs
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.LogsSummaryTypeDef'>
- **Required**: Yes

### MaintenanceWindowStartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.WeeklyStartTimeTypeDef'>
- **Required**: Yes

### PendingAuthenticationStrategy
- **Type**: typing.Literal['LDAP', 'SIMPLE']
- **Required**: Yes

### PendingEngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PendingHostInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### PendingLdapServerMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.LdapServerMetadataOutputTypeDef'>
- **Required**: Yes

### PendingSecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### PubliclyAccessible
- **Type**: <class 'bool'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### StorageType
- **Type**: typing.Literal['EBS', 'EFS']
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.UserSummaryTypeDef]
- **Required**: Yes

### DataReplicationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.DataReplicationMetadataOutputTypeDef'>
- **Required**: Yes

### DataReplicationMode
- **Type**: typing.Literal['CRDR', 'NONE']
- **Required**: Yes

### PendingDataReplicationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.DataReplicationMetadataOutputTypeDef'>
- **Required**: Yes

### PendingDataReplicationMode
- **Type**: typing.Literal['CRDR', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConfigurationRequestRequestTypeDef

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Literal['LDAP', 'SIMPLE']
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EngineType
- **Type**: typing.Literal['ACTIVEMQ', 'RABBITMQ']
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ConfigurationRevisionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConfigurationRevisionRequestRequestTypeDef

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationRevision
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConfigurationRevisionResponseTypeDef

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Data
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponseTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### ConsoleAccess
- **Type**: <class 'bool'>
- **Required**: Yes

### Groups
- **Type**: typing.List[str]
- **Required**: Yes

### Pending
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.UserPendingChangesTypeDef'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationUser
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionOptionsTypeDef

### UseAwsOwnedKey
- **Type**: <class 'bool'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# EngineVersionTypeDef

### Name
- **Type**: typing.Optional[str]


# LdapServerMetadataInputTypeDef

### Hosts
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RoleBase
- **Type**: <class 'str'>
- **Required**: Yes

### RoleSearchMatching
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccountPassword
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccountUsername
- **Type**: <class 'str'>
- **Required**: Yes

### UserBase
- **Type**: <class 'str'>
- **Required**: Yes

### UserSearchMatching
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: typing.Optional[str]

### RoleSearchSubtree
- **Type**: typing.Optional[bool]

### UserRoleName
- **Type**: typing.Optional[str]

### UserSearchSubtree
- **Type**: typing.Optional[bool]


# LdapServerMetadataOutputTypeDef

### Hosts
- **Type**: typing.List[str]
- **Required**: Yes

### RoleBase
- **Type**: <class 'str'>
- **Required**: Yes

### RoleSearchMatching
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccountUsername
- **Type**: <class 'str'>
- **Required**: Yes

### UserBase
- **Type**: <class 'str'>
- **Required**: Yes

### UserSearchMatching
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: typing.Optional[str]

### RoleSearchSubtree
- **Type**: typing.Optional[bool]

### UserRoleName
- **Type**: typing.Optional[str]

### UserSearchSubtree
- **Type**: typing.Optional[bool]


# ListBrokersRequestListBrokersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.PaginatorConfigTypeDef]


# ListBrokersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBrokersResponseTypeDef

### BrokerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.BrokerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRevisionsRequestRequestTypeDef

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRevisionsResponseTypeDef

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.ConfigurationRevisionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsResponseTypeDef

### Configurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.ConfigurationTypeDef]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUsersResponseTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.UserSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogsSummaryTypeDef

### General
- **Type**: <class 'bool'>
- **Required**: Yes

### GeneralLogGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Audit
- **Type**: typing.Optional[bool]

### AuditLogGroup
- **Type**: typing.Optional[str]

### Pending
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.PendingLogsTypeDef]


# LogsTypeDef

### Audit
- **Type**: typing.Optional[bool]

### General
- **Type**: typing.Optional[bool]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingLogsTypeDef

### Audit
- **Type**: typing.Optional[bool]

### General
- **Type**: typing.Optional[bool]


# PromoteRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Literal['FAILOVER', 'SWITCHOVER']
- **Required**: Yes


# PromoteResponseTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebootBrokerRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
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


# SanitizationWarningTypeDef

### Reason
- **Type**: typing.Literal['DISALLOWED_ATTRIBUTE_REMOVED', 'DISALLOWED_ELEMENT_REMOVED', 'INVALID_ATTRIBUTE_VALUE_REMOVED']
- **Required**: Yes

### AttributeName
- **Type**: typing.Optional[str]

### ElementName
- **Type**: typing.Optional[str]


# UpdateBrokerRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Optional[typing.Literal['LDAP', 'SIMPLE']]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.ConfigurationIdTypeDef]

### EngineVersion
- **Type**: typing.Optional[str]

### HostInstanceType
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.LdapServerMetadataInputTypeDef]

### Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.LogsTypeDef]

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq_classes.WeeklyStartTimeTypeDef]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### DataReplicationMode
- **Type**: typing.Optional[typing.Literal['CRDR', 'NONE']]


# UpdateBrokerResponseTypeDef

### AuthenticationStrategy
- **Type**: typing.Literal['LDAP', 'SIMPLE']
- **Required**: Yes

### AutoMinorVersionUpgrade
- **Type**: <class 'bool'>
- **Required**: Yes

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ConfigurationIdTypeDef'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HostInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### LdapServerMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.LdapServerMetadataOutputTypeDef'>
- **Required**: Yes

### Logs
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.LogsTypeDef'>
- **Required**: Yes

### MaintenanceWindowStartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.WeeklyStartTimeTypeDef'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### DataReplicationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.DataReplicationMetadataOutputTypeDef'>
- **Required**: Yes

### DataReplicationMode
- **Type**: typing.Literal['CRDR', 'NONE']
- **Required**: Yes

### PendingDataReplicationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.DataReplicationMetadataOutputTypeDef'>
- **Required**: Yes

### PendingDataReplicationMode
- **Type**: typing.Literal['CRDR', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfigurationRequestRequestTypeDef

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ConfigurationRevisionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq_classes.SanitizationWarningTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserRequestRequestTypeDef

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ConsoleAccess
- **Type**: typing.Optional[bool]

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]

### Password
- **Type**: typing.Optional[str]

### ReplicationUser
- **Type**: typing.Optional[bool]


# UserPendingChangesTypeDef

### PendingChange
- **Type**: typing.Literal['CREATE', 'DELETE', 'UPDATE']
- **Required**: Yes

### ConsoleAccess
- **Type**: typing.Optional[bool]

### Groups
- **Type**: typing.Optional[typing.List[str]]


# UserSummaryTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### PendingChange
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]


# UserTypeDef

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ConsoleAccess
- **Type**: typing.Optional[bool]

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]

### ReplicationUser
- **Type**: typing.Optional[bool]


# WeeklyStartTimeTypeDef

### DayOfWeek
- **Type**: typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']
- **Required**: Yes

### TimeOfDay
- **Type**: <class 'str'>
- **Required**: Yes

### TimeZone
- **Type**: typing.Optional[str]


