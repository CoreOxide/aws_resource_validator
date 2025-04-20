# Mq Mq Classes

# ActionRequired

### ActionRequiredCode
- **Type**: typing.Optional[str]

### ActionRequiredInfo
- **Type**: typing.Optional[str]


# AvailabilityZone

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrokerEngineType

### EngineType
- **Type**: typing.Optional[typing.Literal['ACTIVEMQ', 'RABBITMQ']]

### EngineVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.EngineVersion]]


# BrokerInstance

### ConsoleURL
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.List[str]]

### IpAddress
- **Type**: typing.Optional[str]


# BrokerInstanceOption

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.AvailabilityZone]]

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


# BrokerSummary

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


# Configuration

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationRevision'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConfigurationId

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Revision
- **Type**: typing.Optional[int]


# ConfigurationRevision

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# Configurations

### Current
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationId]

### History
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationId]]

### Pending
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationId]


# CreateBrokerRequest

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.User]
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Optional[typing.Literal['LDAP', 'SIMPLE']]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationId]

### CreatorRequestId
- **Type**: typing.Optional[str]

### EncryptionOptions
- **Type**: <class 'NoneType'>

### EngineVersion
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.LdapServerMetadataInput]

### Logs
- **Type**: <class 'NoneType'>

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.WeeklyStartTime]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### StorageType
- **Type**: typing.Optional[typing.Literal['EBS', 'EFS']]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### DataReplicationMode
- **Type**: typing.Optional[typing.Literal['CRDR', 'NONE']]

### DataReplicationPrimaryBrokerArn
- **Type**: typing.Optional[str]


# CreateBrokerResponse

### BrokerArn
- **Type**: <class 'str'>
- **Required**: Yes

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfigurationRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationRevision'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateUserRequest

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
- **Type**: typing.Optional[typing.List[str]]

### ReplicationUser
- **Type**: typing.Optional[bool]


# DataReplicationCounterpart

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# DataReplicationMetadataOutput

### DataReplicationRole
- **Type**: <class 'str'>
- **Required**: Yes

### DataReplicationCounterpart
- **Type**: <class 'NoneType'>


# DeleteBrokerRequest

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBrokerResponse

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteUserRequest

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBrokerEngineTypesRequest

### EngineType
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBrokerEngineTypesResponse

### BrokerEngineTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.BrokerEngineType]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBrokerInstanceOptionsRequest

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


# DescribeBrokerInstanceOptionsResponse

### BrokerInstanceOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.BrokerInstanceOption]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBrokerRequest

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBrokerResponse

### ActionsRequired
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.ActionRequired]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.BrokerInstance]
- **Required**: Yes

### BrokerName
- **Type**: <class 'str'>
- **Required**: Yes

### BrokerState
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'CRITICAL_ACTION_REQUIRED', 'DELETION_IN_PROGRESS', 'REBOOT_IN_PROGRESS', 'REPLICA', 'RUNNING']
- **Required**: Yes

### Configurations
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.Configurations'>
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeploymentMode
- **Type**: typing.Literal['ACTIVE_STANDBY_MULTI_AZ', 'CLUSTER_MULTI_AZ', 'SINGLE_INSTANCE']
- **Required**: Yes

### EncryptionOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.EncryptionOptions'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.LdapServerMetadataOutput'>
- **Required**: Yes

### Logs
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.LogsSummary'>
- **Required**: Yes

### MaintenanceWindowStartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.WeeklyStartTime'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.LdapServerMetadataOutput'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.UserSummary]
- **Required**: Yes

### DataReplicationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.DataReplicationMetadataOutput'>
- **Required**: Yes

### DataReplicationMode
- **Type**: typing.Literal['CRDR', 'NONE']
- **Required**: Yes

### PendingDataReplicationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.DataReplicationMetadataOutput'>
- **Required**: Yes

### PendingDataReplicationMode
- **Type**: typing.Literal['CRDR', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConfigurationRequest

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationRevision'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConfigurationRevisionRequest

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationRevision
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConfigurationRevisionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserRequest

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.UserPendingChanges'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationUser
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionOptions

### UseAwsOwnedKey
- **Type**: <class 'bool'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# EngineVersion

### Name
- **Type**: typing.Optional[str]


# LdapServerMetadataInput

### Hosts
- **Type**: typing.List[str]
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


# LdapServerMetadataOutput

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


# ListBrokersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBrokersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.PaginatorConfig]


# ListBrokersResponse

### BrokerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.BrokerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRevisionsRequest

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRevisionsResponse

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationRevision]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsResponse

### Configurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.Configuration]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# ListUsersRequest

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUsersResponse

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.UserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Logs

### Audit
- **Type**: typing.Optional[bool]

### General
- **Type**: typing.Optional[bool]


# LogsSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.PendingLogs]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingLogs

### Audit
- **Type**: typing.Optional[bool]

### General
- **Type**: typing.Optional[bool]


# PromoteRequest

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Literal['FAILOVER', 'SWITCHOVER']
- **Required**: Yes


# PromoteResponse

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# RebootBrokerRequest

### BrokerId
- **Type**: <class 'str'>
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


# SanitizationWarning

### Reason
- **Type**: typing.Literal['DISALLOWED_ATTRIBUTE_REMOVED', 'DISALLOWED_ELEMENT_REMOVED', 'INVALID_ATTRIBUTE_VALUE_REMOVED']
- **Required**: Yes

### AttributeName
- **Type**: typing.Optional[str]

### ElementName
- **Type**: typing.Optional[str]


# UpdateBrokerRequest

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationStrategy
- **Type**: typing.Optional[typing.Literal['LDAP', 'SIMPLE']]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationId]

### EngineVersion
- **Type**: typing.Optional[str]

### HostInstanceType
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.LdapServerMetadataInput]

### Logs
- **Type**: <class 'NoneType'>

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mq.mq_classes.WeeklyStartTime]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### DataReplicationMode
- **Type**: typing.Optional[typing.Literal['CRDR', 'NONE']]


# UpdateBrokerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationId'>
- **Required**: Yes

### EngineVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HostInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### LdapServerMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.LdapServerMetadataOutput'>
- **Required**: Yes

### Logs
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.Logs'>
- **Required**: Yes

### MaintenanceWindowStartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.WeeklyStartTime'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### DataReplicationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.DataReplicationMetadataOutput'>
- **Required**: Yes

### DataReplicationMode
- **Type**: typing.Literal['CRDR', 'NONE']
- **Required**: Yes

### PendingDataReplicationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.DataReplicationMetadataOutput'>
- **Required**: Yes

### PendingDataReplicationMode
- **Type**: typing.Literal['CRDR', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfigurationRequest

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### Data
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ConfigurationRevision'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.mq.mq_classes.SanitizationWarning]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mq.mq_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserRequest

### BrokerId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ConsoleAccess
- **Type**: typing.Optional[bool]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### Password
- **Type**: typing.Optional[str]

### ReplicationUser
- **Type**: typing.Optional[bool]


# User

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ConsoleAccess
- **Type**: typing.Optional[bool]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### ReplicationUser
- **Type**: typing.Optional[bool]


# UserPendingChanges

### PendingChange
- **Type**: typing.Literal['CREATE', 'DELETE', 'UPDATE']
- **Required**: Yes

### ConsoleAccess
- **Type**: typing.Optional[bool]

### Groups
- **Type**: typing.Optional[typing.List[str]]


# UserSummary

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### PendingChange
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]


# WeeklyStartTime

### DayOfWeek
- **Type**: typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']
- **Required**: Yes

### TimeOfDay
- **Type**: <class 'str'>
- **Required**: Yes

### TimeZone
- **Type**: typing.Optional[str]


