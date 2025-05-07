# Redshift Classes

# AcceptReservedNodeExchangeInputMessage

### ReservedNodeId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetReservedNodeOfferingId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptReservedNodeExchangeOutputMessage

### ExchangedReservedNode
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNode'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# AccountAttribute

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.AttributeValueTarget]]


# AccountAttributeList

### AccountAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.AccountAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# AccountWithRestoreAccess

### AccountId
- **Type**: typing.Optional[str]

### AccountAlias
- **Type**: typing.Optional[str]


# AquaConfiguration

### AquaStatus
- **Type**: typing.Optional[typing.Literal['applying', 'disabled', 'enabled']]

### AquaConfigurationStatus
- **Type**: typing.Optional[typing.Literal['auto', 'disabled', 'enabled']]


# AssociateDataShareConsumerMessage

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociateEntireAccount
- **Type**: typing.Optional[bool]

### ConsumerArn
- **Type**: typing.Optional[str]

### ConsumerRegion
- **Type**: typing.Optional[str]

### AllowWrites
- **Type**: typing.Optional[bool]


# Association

### CustomDomainCertificateArn
- **Type**: typing.Optional[str]

### CustomDomainCertificateExpiryDate
- **Type**: typing.Optional[datetime.datetime]

### CertificateAssociations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.CertificateAssociation]]


# AttributeValueTarget

### AttributeValue
- **Type**: typing.Optional[str]


# AuthenticationProfile

### AuthenticationProfileName
- **Type**: typing.Optional[str]

### AuthenticationProfileContent
- **Type**: typing.Optional[str]


# AuthorizeClusterSecurityGroupIngressMessage

### ClusterSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CIDRIP
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# AuthorizeClusterSecurityGroupIngressResult

### ClusterSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# AuthorizeDataShareMessage

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AllowWrites
- **Type**: typing.Optional[bool]


# AuthorizeEndpointAccessMessage

### Account
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### VpcIds
- **Type**: typing.Optional[typing.List[str]]


# AuthorizeSnapshotAccessMessage

### AccountWithRestoreAccess
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]


# AuthorizeSnapshotAccessResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# AuthorizedTokenIssuer

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]

### AuthorizedAudiencesList
- **Type**: typing.Optional[typing.List[str]]


# AuthorizedTokenIssuerOutput

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]

### AuthorizedAudiencesList
- **Type**: typing.Optional[typing.List[str]]


# AvailabilityZone

### Name
- **Type**: typing.Optional[str]

### SupportedPlatforms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SupportedPlatform]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteClusterSnapshotsRequest

### Identifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DeleteClusterSnapshotMessage]
- **Required**: Yes


# BatchDeleteClusterSnapshotsResult

### Resources
- **Type**: typing.List[str]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SnapshotErrorMessage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# BatchModifyClusterSnapshotsMessage

### SnapshotIdentifierList
- **Type**: typing.List[str]
- **Required**: Yes

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### Force
- **Type**: typing.Optional[bool]


# BatchModifyClusterSnapshotsOutputMessage

### Resources
- **Type**: typing.List[str]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SnapshotErrorMessage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CancelResizeMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CertificateAssociation

### CustomDomainName
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]


# Cluster

### ClusterIdentifier
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### ClusterStatus
- **Type**: typing.Optional[str]

### ClusterAvailabilityStatus
- **Type**: typing.Optional[str]

### ModifyStatus
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: <class 'NoneType'>

### ClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterSecurityGroupMembership]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.VpcSecurityGroupMembership]]

### ClusterParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterParameterGroupStatus]]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: <class 'NoneType'>

### ClusterVersion
- **Type**: typing.Optional[str]

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Encrypted
- **Type**: typing.Optional[bool]

### RestoreStatus
- **Type**: <class 'NoneType'>

### DataTransferProgress
- **Type**: <class 'NoneType'>

### HsmStatus
- **Type**: <class 'NoneType'>

### ClusterSnapshotCopyStatus
- **Type**: <class 'NoneType'>

### ClusterPublicKey
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterNode]]

### ElasticIpStatus
- **Type**: <class 'NoneType'>

### ClusterRevisionNumber
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### IamRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterIamRole]]

### PendingActions
- **Type**: typing.Optional[typing.List[str]]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### ElasticResizeNumberOfNodeOptions
- **Type**: typing.Optional[str]

### DeferredMaintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DeferredMaintenanceWindow]]

### SnapshotScheduleIdentifier
- **Type**: typing.Optional[str]

### SnapshotScheduleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'MODIFYING']]

### ExpectedNextSnapshotScheduleTime
- **Type**: typing.Optional[datetime.datetime]

### ExpectedNextSnapshotScheduleTimeStatus
- **Type**: typing.Optional[str]

### NextMaintenanceWindowStartTime
- **Type**: typing.Optional[datetime.datetime]

### ResizeInfo
- **Type**: <class 'NoneType'>

### AvailabilityZoneRelocationStatus
- **Type**: typing.Optional[str]

### ClusterNamespaceArn
- **Type**: typing.Optional[str]

### TotalStorageCapacityInMegaBytes
- **Type**: typing.Optional[int]

### AquaConfiguration
- **Type**: <class 'NoneType'>

### DefaultIamRoleArn
- **Type**: typing.Optional[str]

### ReservedNodeExchangeStatus
- **Type**: <class 'NoneType'>

### CustomDomainName
- **Type**: typing.Optional[str]

### CustomDomainCertificateArn
- **Type**: typing.Optional[str]

### CustomDomainCertificateExpiryDate
- **Type**: typing.Optional[datetime.datetime]

### MasterPasswordSecretArn
- **Type**: typing.Optional[str]

### MasterPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[str]

### MultiAZSecondary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.SecondaryClusterInfo]


# ClusterAssociatedToSchedule

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ScheduleAssociationState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'MODIFYING']]


# ClusterCredentials

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### DbPassword
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClusterDbRevision

### ClusterIdentifier
- **Type**: typing.Optional[str]

### CurrentDatabaseRevision
- **Type**: typing.Optional[str]

### DatabaseRevisionReleaseDate
- **Type**: typing.Optional[datetime.datetime]

### RevisionTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.RevisionTarget]]


# ClusterDbRevisionsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterDbRevisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterDbRevision]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClusterExtendedCredentials

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### DbPassword
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextRefreshTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClusterIamRole

### IamRoleArn
- **Type**: typing.Optional[str]

### ApplyStatus
- **Type**: typing.Optional[str]


# ClusterNode

### NodeRole
- **Type**: typing.Optional[str]

### PrivateIPAddress
- **Type**: typing.Optional[str]

### PublicIPAddress
- **Type**: typing.Optional[str]


# ClusterParameterGroup

### ParameterGroupName
- **Type**: typing.Optional[str]

### ParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# ClusterParameterGroupDetails

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Parameter]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClusterParameterGroupNameMessage

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterGroupStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClusterParameterGroupStatus

### ParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ClusterParameterStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterParameterStatus]]


# ClusterParameterGroupsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterParameterGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClusterParameterStatus

### ParameterName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterApplyErrorDescription
- **Type**: typing.Optional[str]


# ClusterSecurityGroup

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EC2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.EC2SecurityGroup]]

### IPRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.IPRange]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# ClusterSecurityGroupMembership

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ClusterSecurityGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterSecurityGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClusterSnapshotCopyStatus

### DestinationRegion
- **Type**: typing.Optional[str]

### RetentionPeriod
- **Type**: typing.Optional[int]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]


# ClusterSubnetGroup

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Subnet]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]

### SupportedClusterIpAddressTypes
- **Type**: typing.Optional[typing.List[str]]


# ClusterSubnetGroupMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterSubnetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClusterVersion

### ClusterVersion
- **Type**: typing.Optional[str]

### ClusterParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ClusterVersionsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ClustersMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CopyClusterSnapshotMessage

### SourceSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### TargetSnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceSnapshotClusterIdentifier
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]


# CopyClusterSnapshotResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAuthenticationProfileMessage

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationProfileContent
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAuthenticationProfileResult

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationProfileContent
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NodeType
- **Type**: <class 'str'>
- **Required**: Yes

### MasterUsername
- **Type**: <class 'str'>
- **Required**: Yes

### DBName
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ClusterParameterGroupName
- **Type**: typing.Optional[str]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### Port
- **Type**: typing.Optional[int]

### ClusterVersion
- **Type**: typing.Optional[str]

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### Encrypted
- **Type**: typing.Optional[bool]

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### ElasticIp
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### AdditionalInfo
- **Type**: typing.Optional[str]

### IamRoles
- **Type**: typing.Optional[typing.List[str]]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### SnapshotScheduleIdentifier
- **Type**: typing.Optional[str]

### AvailabilityZoneRelocation
- **Type**: typing.Optional[bool]

### AquaConfigurationStatus
- **Type**: typing.Optional[typing.Literal['auto', 'disabled', 'enabled']]

### DefaultIamRoleArn
- **Type**: typing.Optional[str]

### LoadSampleData
- **Type**: typing.Optional[str]

### ManageMasterPassword
- **Type**: typing.Optional[bool]

### MasterPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### RedshiftIdcApplicationArn
- **Type**: typing.Optional[str]


# CreateClusterParameterGroupMessage

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CreateClusterParameterGroupResult

### ClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterParameterGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterSecurityGroupMessage

### ClusterSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CreateClusterSecurityGroupResult

### ClusterSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterSnapshotMessage

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CreateClusterSnapshotResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterSubnetGroupMessage

### ClusterSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CreateClusterSubnetGroupResult

### ClusterSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomDomainAssociationMessage

### CustomDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomDomainAssociationResult

### CustomDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainCertExpiryTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEndpointAccessMessage

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# CreateEventSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]

### SourceIds
- **Type**: typing.Optional[typing.List[str]]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### Severity
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CreateEventSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHsmClientCertificateMessage

### HsmClientCertificateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CreateHsmClientCertificateResult

### HsmClientCertificate
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.HsmClientCertificate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHsmConfigurationMessage

### HsmConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HsmIpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### HsmPartitionName
- **Type**: <class 'str'>
- **Required**: Yes

### HsmPartitionPassword
- **Type**: <class 'str'>
- **Required**: Yes

### HsmServerPublicCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CreateHsmConfigurationResult

### HsmConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.HsmConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntegrationMessage

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyId
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]

### AdditionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### Description
- **Type**: typing.Optional[str]


# CreateRedshiftIdcApplicationMessage

### IdcInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### RedshiftIdcApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### IdcDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityNamespace
- **Type**: typing.Optional[str]

### AuthorizedTokenIssuerList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.redshift.redshift_classes.AuthorizedTokenIssuer, aws_resource_validator.pydantic_models.redshift.redshift_classes.AuthorizedTokenIssuerOutput]]]

### ServiceIntegrations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.redshift.redshift_classes.ServiceIntegrationsUnion, aws_resource_validator.pydantic_models.redshift.redshift_classes.ServiceIntegrationsUnionOutput]]]


# CreateRedshiftIdcApplicationResult

### RedshiftIdcApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.RedshiftIdcApplication'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScheduledActionMessage

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ScheduledActionType'>
- **Required**: Yes

### Schedule
- **Type**: <class 'str'>
- **Required**: Yes

### IamRole
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActionDescription
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Enable
- **Type**: typing.Optional[bool]


# CreateSnapshotCopyGrantMessage

### SnapshotCopyGrantName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CreateSnapshotCopyGrantResult

### SnapshotCopyGrant
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.SnapshotCopyGrant'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotScheduleMessage

### ScheduleDefinitions
- **Type**: typing.Optional[typing.List[str]]

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### ScheduleDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]

### DryRun
- **Type**: typing.Optional[bool]

### NextInvocations
- **Type**: typing.Optional[int]


# CreateTagsMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]
- **Required**: Yes


# CreateUsageLimitMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureType
- **Type**: typing.Literal['concurrency-scaling', 'cross-region-datasharing', 'spectrum']
- **Required**: Yes

### LimitType
- **Type**: typing.Literal['data-scanned', 'time']
- **Required**: Yes

### Amount
- **Type**: <class 'int'>
- **Required**: Yes

### Period
- **Type**: typing.Optional[typing.Literal['daily', 'monthly', 'weekly']]

### BreachAction
- **Type**: typing.Optional[typing.Literal['disable', 'emit-metric', 'log']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# CustomDomainAssociationsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Association]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerStorageMessage

### TotalBackupSizeInMegaBytes
- **Type**: <class 'float'>
- **Required**: Yes

### TotalProvisionedStorageInMegaBytes
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DataShare

### DataShareArn
- **Type**: typing.Optional[str]

### ProducerArn
- **Type**: typing.Optional[str]

### AllowPubliclyAccessibleConsumers
- **Type**: typing.Optional[bool]

### DataShareAssociations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DataShareAssociation]]

### ManagedBy
- **Type**: typing.Optional[str]

### DataShareType
- **Type**: typing.Optional[typing.Literal['INTERNAL']]


# DataShareAssociation

### ConsumerIdentifier
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AUTHORIZED', 'AVAILABLE', 'DEAUTHORIZED', 'PENDING_AUTHORIZATION', 'REJECTED']]

### ConsumerRegion
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### StatusChangeDate
- **Type**: typing.Optional[datetime.datetime]

### ProducerAllowedWrites
- **Type**: typing.Optional[bool]

### ConsumerAcceptedWrites
- **Type**: typing.Optional[bool]


# DataShareResponse

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProducerArn
- **Type**: <class 'str'>
- **Required**: Yes

### AllowPubliclyAccessibleConsumers
- **Type**: <class 'bool'>
- **Required**: Yes

### DataShareAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DataShareAssociation]
- **Required**: Yes

### ManagedBy
- **Type**: <class 'str'>
- **Required**: Yes

### DataShareType
- **Type**: typing.Literal['INTERNAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DataTransferProgress

### Status
- **Type**: typing.Optional[str]

### CurrentRateInMegaBytesPerSecond
- **Type**: typing.Optional[float]

### TotalDataInMegaBytes
- **Type**: typing.Optional[int]

### DataTransferredInMegaBytes
- **Type**: typing.Optional[int]

### EstimatedTimeToCompletionInSeconds
- **Type**: typing.Optional[int]

### ElapsedTimeInSeconds
- **Type**: typing.Optional[int]


# DeauthorizeDataShareMessage

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DefaultClusterParameters

### ParameterGroupFamily
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Parameter]]


# DeferredMaintenanceWindow

### DeferMaintenanceIdentifier
- **Type**: typing.Optional[str]

### DeferMaintenanceStartTime
- **Type**: typing.Optional[datetime.datetime]

### DeferMaintenanceEndTime
- **Type**: typing.Optional[datetime.datetime]


# DeleteAuthenticationProfileMessage

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthenticationProfileResult

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalClusterSnapshot
- **Type**: typing.Optional[bool]

### FinalClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### FinalClusterSnapshotRetentionPeriod
- **Type**: typing.Optional[int]


# DeleteClusterParameterGroupMessage

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterSecurityGroupMessage

### ClusterSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterSnapshotMessage

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]


# DeleteClusterSnapshotMessageRequest

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]


# DeleteClusterSnapshotResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterSubnetGroupMessage

### ClusterSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomDomainAssociationMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointAccessMessage

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHsmClientCertificateMessage

### HsmClientCertificateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHsmConfigurationMessage

### HsmConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationMessage

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRedshiftIdcApplicationMessage

### RedshiftIdcApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyMessage

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledActionMessage

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotCopyGrantMessage

### SnapshotCopyGrantName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotScheduleMessage

### ScheduleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsMessage

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteUsageLimitMessage

### UsageLimitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterNamespaceInputMessage

### NamespaceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.NamespaceIdentifierUnion'>
- **Required**: Yes

### ConsumerIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes


# DeregisterNamespaceOutputMessage

### Status
- **Type**: typing.Literal['Deregistering', 'Registering']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountAttributesMessage

### AttributeNames
- **Type**: typing.Optional[typing.List[str]]


# DescribeAuthenticationProfilesMessage

### AuthenticationProfileName
- **Type**: typing.Optional[str]


# DescribeAuthenticationProfilesResult

### AuthenticationProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.AuthenticationProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterDbRevisionsMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeClusterDbRevisionsMessagePaginate

### ClusterIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClusterParameterGroupsMessage

### ParameterGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeClusterParameterGroupsMessagePaginate

### ParameterGroupName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClusterParametersMessage

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeClusterParametersMessagePaginate

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClusterSecurityGroupsMessage

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeClusterSecurityGroupsMessagePaginate

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClusterSnapshotsMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### OwnerAccount
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### ClusterExists
- **Type**: typing.Optional[bool]

### SortingEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SnapshotSortingEntity]]


# DescribeClusterSnapshotsMessagePaginate

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### OwnerAccount
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### ClusterExists
- **Type**: typing.Optional[bool]

### SortingEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SnapshotSortingEntity]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClusterSnapshotsMessageWait

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### OwnerAccount
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### ClusterExists
- **Type**: typing.Optional[bool]

### SortingEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SnapshotSortingEntity]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterSubnetGroupsMessage

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeClusterSubnetGroupsMessagePaginate

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClusterTracksMessage

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeClusterTracksMessagePaginate

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClusterVersionsMessage

### ClusterVersion
- **Type**: typing.Optional[str]

### ClusterParameterGroupFamily
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeClusterVersionsMessagePaginate

### ClusterVersion
- **Type**: typing.Optional[str]

### ClusterParameterGroupFamily
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClustersMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeClustersMessagePaginate

### ClusterIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeClustersMessageWait

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClustersMessageWaitExtra

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClustersMessageWaitExtraExtra

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeCustomDomainAssociationsMessage

### CustomDomainName
- **Type**: typing.Optional[str]

### CustomDomainCertificateArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeCustomDomainAssociationsMessagePaginate

### CustomDomainName
- **Type**: typing.Optional[str]

### CustomDomainCertificateArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeDataSharesForConsumerMessage

### ConsumerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AVAILABLE']]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataSharesForConsumerMessagePaginate

### ConsumerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AVAILABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeDataSharesForConsumerResult

### DataShares
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DataShare]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataSharesForProducerMessage

### ProducerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AUTHORIZED', 'DEAUTHORIZED', 'PENDING_AUTHORIZATION', 'REJECTED']]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataSharesForProducerMessagePaginate

### ProducerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AUTHORIZED', 'DEAUTHORIZED', 'PENDING_AUTHORIZATION', 'REJECTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeDataSharesForProducerResult

### DataShares
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DataShare]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataSharesMessage

### DataShareArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataSharesMessagePaginate

### DataShareArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeDataSharesResult

### DataShares
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DataShare]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDefaultClusterParametersMessage

### ParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDefaultClusterParametersMessagePaginate

### ParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeDefaultClusterParametersResult

### DefaultClusterParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.DefaultClusterParameters'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointAccessMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEndpointAccessMessagePaginate

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeEndpointAuthorizationMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Account
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[bool]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEndpointAuthorizationMessagePaginate

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Account
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeEventCategoriesMessage

### SourceType
- **Type**: typing.Optional[str]


# DescribeEventSubscriptionsMessage

### SubscriptionName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeEventSubscriptionsMessagePaginate

### SubscriptionName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeEventsMessage

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cluster', 'cluster-parameter-group', 'cluster-security-group', 'cluster-snapshot', 'scheduled-action']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeEventsMessagePaginate

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cluster', 'cluster-parameter-group', 'cluster-security-group', 'cluster-snapshot', 'scheduled-action']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Duration
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeHsmClientCertificatesMessage

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeHsmClientCertificatesMessagePaginate

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeHsmConfigurationsMessage

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeHsmConfigurationsMessagePaginate

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeInboundIntegrationsMessage

### IntegrationArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeInboundIntegrationsMessagePaginate

### IntegrationArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeIntegrationsFilter

### Name
- **Type**: typing.Literal['integration-arn', 'source-arn', 'source-types', 'status']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeIntegrationsMessage

### IntegrationArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DescribeIntegrationsFilter]]


# DescribeIntegrationsMessagePaginate

### IntegrationArn
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.DescribeIntegrationsFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeLoggingStatusMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeConfigurationOptionsMessage

### ActionType
- **Type**: typing.Literal['recommend-node-config', 'resize-cluster', 'restore-cluster']
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### OwnerAccount
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.NodeConfigurationOptionsFilter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeNodeConfigurationOptionsMessagePaginate

### ActionType
- **Type**: typing.Literal['recommend-node-config', 'resize-cluster', 'restore-cluster']
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### OwnerAccount
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.NodeConfigurationOptionsFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeOrderableClusterOptionsMessage

### ClusterVersion
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeOrderableClusterOptionsMessagePaginate

### ClusterVersion
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribePartnersInputMessage

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: typing.Optional[str]

### PartnerName
- **Type**: typing.Optional[str]


# DescribePartnersOutputMessage

### PartnerIntegrationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.PartnerIntegrationInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRedshiftIdcApplicationsMessage

### RedshiftIdcApplicationArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeRedshiftIdcApplicationsMessagePaginate

### RedshiftIdcApplicationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeRedshiftIdcApplicationsResult

### RedshiftIdcApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.RedshiftIdcApplication]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReservedNodeExchangeStatusInputMessage

### ReservedNodeId
- **Type**: typing.Optional[str]

### ReservedNodeExchangeRequestId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedNodeExchangeStatusInputMessagePaginate

### ReservedNodeId
- **Type**: typing.Optional[str]

### ReservedNodeExchangeRequestId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeReservedNodeExchangeStatusOutputMessage

### ReservedNodeExchangeStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNodeExchangeStatus]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReservedNodeOfferingsMessage

### ReservedNodeOfferingId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedNodeOfferingsMessagePaginate

### ReservedNodeOfferingId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeReservedNodesMessage

### ReservedNodeId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedNodesMessagePaginate

### ReservedNodeId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeResizeMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScheduledActionsMessage

### ScheduledActionName
- **Type**: typing.Optional[str]

### TargetActionType
- **Type**: typing.Optional[typing.Literal['PauseCluster', 'ResizeCluster', 'ResumeCluster']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Active
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ScheduledActionFilter]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeScheduledActionsMessagePaginate

### ScheduledActionName
- **Type**: typing.Optional[str]

### TargetActionType
- **Type**: typing.Optional[typing.Literal['PauseCluster', 'ResizeCluster', 'ResumeCluster']]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Active
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ScheduledActionFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeSnapshotCopyGrantsMessage

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeSnapshotCopyGrantsMessagePaginate

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeSnapshotSchedulesMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeSnapshotSchedulesMessagePaginate

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeSnapshotSchedulesOutputMessage

### SnapshotSchedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SnapshotSchedule]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTableRestoreStatusMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### TableRestoreRequestId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeTableRestoreStatusMessagePaginate

### ClusterIdentifier
- **Type**: typing.Optional[str]

### TableRestoreRequestId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeTagsMessage

### ResourceName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeTagsMessagePaginate

### ResourceName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DescribeUsageLimitsMessage

### UsageLimitId
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### FeatureType
- **Type**: typing.Optional[typing.Literal['concurrency-scaling', 'cross-region-datasharing', 'spectrum']]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeUsageLimitsMessagePaginate

### UsageLimitId
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### FeatureType
- **Type**: typing.Optional[typing.Literal['concurrency-scaling', 'cross-region-datasharing', 'spectrum']]

### TagKeys
- **Type**: typing.Optional[typing.List[str]]

### TagValues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# DisableLoggingMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisableSnapshotCopyMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisableSnapshotCopyResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateDataShareConsumerMessage

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisassociateEntireAccount
- **Type**: typing.Optional[bool]

### ConsumerArn
- **Type**: typing.Optional[str]

### ConsumerRegion
- **Type**: typing.Optional[str]


# EC2SecurityGroup

### Status
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# ElasticIpStatus

### ElasticIp
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# EnableLoggingMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### BucketName
- **Type**: typing.Optional[str]

### S3KeyPrefix
- **Type**: typing.Optional[str]

### LogDestinationType
- **Type**: typing.Optional[typing.Literal['cloudwatch', 's3']]

### LogExports
- **Type**: typing.Optional[typing.List[str]]


# EnableSnapshotCopyMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: typing.Optional[int]

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]


# EnableSnapshotCopyResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.VpcEndpoint]]


# EndpointAccess

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### SubnetGroupName
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### EndpointCreateTime
- **Type**: typing.Optional[datetime.datetime]

### Port
- **Type**: typing.Optional[int]

### Address
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.VpcSecurityGroupMembership]]

### VpcEndpoint
- **Type**: <class 'NoneType'>


# EndpointAccessList

### EndpointAccessList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.EndpointAccess]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointAccessResponse

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointStatus
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointCreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.VpcSecurityGroupMembership]
- **Required**: Yes

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.VpcEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointAuthorization

### Grantor
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### AuthorizeTime
- **Type**: typing.Optional[datetime.datetime]

### ClusterStatus
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Authorized', 'Revoking']]

### AllowedAllVPCs
- **Type**: typing.Optional[bool]

### AllowedVPCs
- **Type**: typing.Optional[typing.List[str]]

### EndpointCount
- **Type**: typing.Optional[int]


# EndpointAuthorizationList

### EndpointAuthorizationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.EndpointAuthorization]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointAuthorizationResponse

### Grantor
- **Type**: <class 'str'>
- **Required**: Yes

### Grantee
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizeTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ClusterStatus
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Authorized', 'Revoking']
- **Required**: Yes

### AllowedAllVPCs
- **Type**: <class 'bool'>
- **Required**: Yes

### AllowedVPCs
- **Type**: typing.List[str]
- **Required**: Yes

### EndpointCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# Event

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cluster', 'cluster-parameter-group', 'cluster-security-group', 'cluster-snapshot', 'scheduled-action']]

### Message
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### Severity
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[datetime.datetime]

### EventId
- **Type**: typing.Optional[str]


# EventCategoriesMap

### SourceType
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.EventInfoMap]]


# EventCategoriesMessage

### EventCategoriesMapList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.EventCategoriesMap]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# EventInfoMap

### EventId
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### EventDescription
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]


# EventSubscription

### CustomerAwsId
- **Type**: typing.Optional[str]

### CustSubscriptionId
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubscriptionCreationTime
- **Type**: typing.Optional[datetime.datetime]

### SourceType
- **Type**: typing.Optional[str]

### SourceIdsList
- **Type**: typing.Optional[typing.List[str]]

### EventCategoriesList
- **Type**: typing.Optional[typing.List[str]]

### Severity
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# EventSubscriptionsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSubscriptionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.EventSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# EventsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# FailoverPrimaryComputeInputMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# FailoverPrimaryComputeResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# GetClusterCredentialsMessage

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### DbName
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]

### AutoCreate
- **Type**: typing.Optional[bool]

### DbGroups
- **Type**: typing.Optional[typing.List[str]]

### CustomDomainName
- **Type**: typing.Optional[str]


# GetClusterCredentialsWithIAMMessage

### DbName
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]

### CustomDomainName
- **Type**: typing.Optional[str]


# GetReservedNodeExchangeConfigurationOptionsInputMessage

### ActionType
- **Type**: typing.Literal['resize-cluster', 'restore-cluster']
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetReservedNodeExchangeConfigurationOptionsInputMessagePaginate

### ActionType
- **Type**: typing.Literal['resize-cluster', 'restore-cluster']
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# GetReservedNodeExchangeConfigurationOptionsOutputMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodeConfigurationOptionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNodeConfigurationOption]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# GetReservedNodeExchangeOfferingsInputMessage

### ReservedNodeId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetReservedNodeExchangeOfferingsInputMessagePaginate

### ReservedNodeId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# GetReservedNodeExchangeOfferingsOutputMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodeOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNodeOffering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyMessage

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResult

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# HsmClientCertificate

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmClientCertificatePublicKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# HsmClientCertificateMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### HsmClientCertificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.HsmClientCertificate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# HsmConfiguration

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HsmIpAddress
- **Type**: typing.Optional[str]

### HsmPartitionName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# HsmConfigurationMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### HsmConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.HsmConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# HsmStatus

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# IPRange

### Status
- **Type**: typing.Optional[str]

### CIDRIP
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# InboundIntegration

### IntegrationArn
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['active', 'creating', 'deleting', 'failed', 'modifying', 'needs_attention', 'syncing']]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.IntegrationError]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]


# InboundIntegrationsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### InboundIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.InboundIntegration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# Integration

### IntegrationArn
- **Type**: typing.Optional[str]

### IntegrationName
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['active', 'creating', 'deleting', 'failed', 'modifying', 'needs_attention', 'syncing']]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.IntegrationError]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### KMSKeyId
- **Type**: typing.Optional[str]

### AdditionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# IntegrationError

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: typing.Optional[str]


# IntegrationResponse

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['active', 'creating', 'deleting', 'failed', 'modifying', 'needs_attention', 'syncing']
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.IntegrationError]
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalEncryptionContext
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# IntegrationsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Integrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Integration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# LakeFormationQuery

### Authorization
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# LakeFormationScopeUnion

### LakeFormationQuery
- **Type**: <class 'NoneType'>


# ListRecommendationsMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### NamespaceArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListRecommendationsMessagePaginate

### ClusterIdentifier
- **Type**: typing.Optional[str]

### NamespaceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PaginatorConfig]


# ListRecommendationsResult

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Recommendation]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingStatus

### LoggingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### LastSuccessfulDeliveryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastFailureTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastFailureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationType
- **Type**: typing.Literal['cloudwatch', 's3']
- **Required**: Yes

### LogExports
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# MaintenanceTrack

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### DatabaseVersion
- **Type**: typing.Optional[str]

### UpdateTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.UpdateTarget]]


# ModifyAquaInputMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AquaConfigurationStatus
- **Type**: typing.Optional[typing.Literal['auto', 'disabled', 'enabled']]


# ModifyAquaOutputMessage

### AquaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.AquaConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyAuthenticationProfileMessage

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationProfileContent
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyAuthenticationProfileResult

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationProfileContent
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyClusterDbRevisionMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionTarget
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyClusterDbRevisionResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyClusterIamRolesMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AddIamRoles
- **Type**: typing.Optional[typing.List[str]]

### RemoveIamRoles
- **Type**: typing.Optional[typing.List[str]]

### DefaultIamRoleArn
- **Type**: typing.Optional[str]


# ModifyClusterIamRolesResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyClusterMaintenanceMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeferMaintenance
- **Type**: typing.Optional[bool]

### DeferMaintenanceIdentifier
- **Type**: typing.Optional[str]

### DeferMaintenanceStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DeferMaintenanceEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DeferMaintenanceDuration
- **Type**: typing.Optional[int]


# ModifyClusterMaintenanceResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyClusterMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterType
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### MasterUserPassword
- **Type**: typing.Optional[str]

### ClusterParameterGroupName
- **Type**: typing.Optional[str]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### NewClusterIdentifier
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ElasticIp
- **Type**: typing.Optional[str]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### AvailabilityZoneRelocation
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ManageMasterPassword
- **Type**: typing.Optional[bool]

### MasterPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]


# ModifyClusterParameterGroupMessage

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Parameter]
- **Required**: Yes


# ModifyClusterResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyClusterSnapshotMessage

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### Force
- **Type**: typing.Optional[bool]


# ModifyClusterSnapshotResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyClusterSnapshotScheduleMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### DisassociateSchedule
- **Type**: typing.Optional[bool]


# ModifyClusterSubnetGroupMessage

### ClusterSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ModifyClusterSubnetGroupResult

### ClusterSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterSubnetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyCustomDomainAssociationMessage

### CustomDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyCustomDomainAssociationResult

### CustomDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainCertExpiryTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyEndpointAccessMessage

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# ModifyEventSubscriptionMessage

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### SourceIds
- **Type**: typing.Optional[typing.List[str]]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### Severity
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# ModifyEventSubscriptionResult

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.EventSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyIntegrationMessage

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IntegrationName
- **Type**: typing.Optional[str]


# ModifyRedshiftIdcApplicationMessage

### RedshiftIdcApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityNamespace
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]

### IdcDisplayName
- **Type**: typing.Optional[str]

### AuthorizedTokenIssuerList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.redshift.redshift_classes.AuthorizedTokenIssuer, aws_resource_validator.pydantic_models.redshift.redshift_classes.AuthorizedTokenIssuerOutput]]]

### ServiceIntegrations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.redshift.redshift_classes.ServiceIntegrationsUnion, aws_resource_validator.pydantic_models.redshift.redshift_classes.ServiceIntegrationsUnionOutput]]]


# ModifyRedshiftIdcApplicationResult

### RedshiftIdcApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.RedshiftIdcApplication'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyScheduledActionMessage

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.ScheduledActionType]

### Schedule
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[str]

### ScheduledActionDescription
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Enable
- **Type**: typing.Optional[bool]


# ModifySnapshotCopyRetentionPeriodMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### Manual
- **Type**: typing.Optional[bool]


# ModifySnapshotCopyRetentionPeriodResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ModifySnapshotScheduleMessage

### ScheduleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleDefinitions
- **Type**: typing.List[str]
- **Required**: Yes


# ModifyUsageLimitMessage

### UsageLimitId
- **Type**: <class 'str'>
- **Required**: Yes

### Amount
- **Type**: typing.Optional[int]

### BreachAction
- **Type**: typing.Optional[typing.Literal['disable', 'emit-metric', 'log']]


# NamespaceIdentifierUnion

### ServerlessIdentifier
- **Type**: <class 'NoneType'>

### ProvisionedIdentifier
- **Type**: <class 'NoneType'>


# NetworkInterface

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### Ipv6Address
- **Type**: typing.Optional[str]


# NodeConfigurationOption

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### EstimatedDiskUtilizationPercent
- **Type**: typing.Optional[float]

### Mode
- **Type**: typing.Optional[typing.Literal['high-performance', 'standard']]


# NodeConfigurationOptionsFilter

### Name
- **Type**: typing.Optional[typing.Literal['EstimatedDiskUtilizationPercent', 'Mode', 'NodeType', 'NumberOfNodes']]

### Operator
- **Type**: typing.Optional[typing.Literal['between', 'eq', 'ge', 'gt', 'in', 'le', 'lt']]

### Values
- **Type**: typing.Optional[typing.List[str]]


# NodeConfigurationOptionsMessage

### NodeConfigurationOptionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.NodeConfigurationOption]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# OrderableClusterOption

### ClusterVersion
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.AvailabilityZone]]


# OrderableClusterOptionsMessage

### OrderableClusterOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.OrderableClusterOption]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### ApplyType
- **Type**: typing.Optional[typing.Literal['dynamic', 'static']]

### IsModifiable
- **Type**: typing.Optional[bool]

### MinimumEngineVersion
- **Type**: typing.Optional[str]


# PartnerIntegrationInfo

### DatabaseName
- **Type**: typing.Optional[str]

### PartnerName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'ConnectionFailure', 'Inactive', 'RuntimeFailure']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# PartnerIntegrationInputMessage

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerName
- **Type**: <class 'str'>
- **Required**: Yes


# PartnerIntegrationInputMessageRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerName
- **Type**: <class 'str'>
- **Required**: Yes


# PartnerIntegrationOutputMessage

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# PauseClusterMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PauseClusterMessageRequest

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PauseClusterResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# PendingModifiedValues

### MasterUserPassword
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### ClusterType
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### EncryptionType
- **Type**: typing.Optional[str]


# ProvisionedIdentifier

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PurchaseReservedNodeOfferingMessage

### ReservedNodeOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeCount
- **Type**: typing.Optional[int]


# PurchaseReservedNodeOfferingResult

### ReservedNode
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNode'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyMessage

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyResult

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ReadWriteAccess

### Authorization
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# RebootClusterMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RebootClusterResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# Recommendation

### Id
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### NamespaceArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### RecommendationType
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Observation
- **Type**: typing.Optional[str]

### ImpactRanking
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### RecommendationText
- **Type**: typing.Optional[str]

### RecommendedActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.RecommendedAction]]

### ReferenceLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ReferenceLink]]


# RecommendedAction

### Text
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### Command
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CLI', 'SQL']]


# RecurringCharge

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RedshiftIdcApplication

### IdcInstanceArn
- **Type**: typing.Optional[str]

### RedshiftIdcApplicationName
- **Type**: typing.Optional[str]

### RedshiftIdcApplicationArn
- **Type**: typing.Optional[str]

### IdentityNamespace
- **Type**: typing.Optional[str]

### IdcDisplayName
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]

### IdcManagedApplicationArn
- **Type**: typing.Optional[str]

### IdcOnboardStatus
- **Type**: typing.Optional[str]

### AuthorizedTokenIssuerList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.AuthorizedTokenIssuerOutput]]

### ServiceIntegrations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ServiceIntegrationsUnionOutput]]


# ReferenceLink

### Text
- **Type**: typing.Optional[str]

### Link
- **Type**: typing.Optional[str]


# RegisterNamespaceInputMessage

### NamespaceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.NamespaceIdentifierUnion'>
- **Required**: Yes

### ConsumerIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes


# RegisterNamespaceOutputMessage

### Status
- **Type**: typing.Literal['Deregistering', 'Registering']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# RejectDataShareMessage

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes


# ReservedNode

### ReservedNodeId
- **Type**: typing.Optional[str]

### ReservedNodeOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### UsagePrice
- **Type**: typing.Optional[float]

### CurrencyCode
- **Type**: typing.Optional[str]

### NodeCount
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.RecurringCharge]]

### ReservedNodeOfferingType
- **Type**: typing.Optional[typing.Literal['Regular', 'Upgradable']]


# ReservedNodeConfigurationOption

### SourceReservedNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNode]

### TargetReservedNodeCount
- **Type**: typing.Optional[int]

### TargetReservedNodeOffering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNodeOffering]


# ReservedNodeExchangeStatus

### ReservedNodeExchangeRequestId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING', 'REQUESTED', 'RETRYING', 'SUCCEEDED']]

### RequestTime
- **Type**: typing.Optional[datetime.datetime]

### SourceReservedNodeId
- **Type**: typing.Optional[str]

### SourceReservedNodeType
- **Type**: typing.Optional[str]

### SourceReservedNodeCount
- **Type**: typing.Optional[int]

### TargetReservedNodeOfferingId
- **Type**: typing.Optional[str]

### TargetReservedNodeType
- **Type**: typing.Optional[str]

### TargetReservedNodeCount
- **Type**: typing.Optional[int]


# ReservedNodeOffering

### ReservedNodeOfferingId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[int]

### FixedPrice
- **Type**: typing.Optional[float]

### UsagePrice
- **Type**: typing.Optional[float]

### CurrencyCode
- **Type**: typing.Optional[str]

### OfferingType
- **Type**: typing.Optional[str]

### RecurringCharges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.RecurringCharge]]

### ReservedNodeOfferingType
- **Type**: typing.Optional[typing.Literal['Regular', 'Upgradable']]


# ReservedNodeOfferingsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodeOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNodeOffering]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ReservedNodesMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ReservedNode]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ResetClusterParameterGroupMessage

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Parameter]]


# ResizeClusterMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterType
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### Classic
- **Type**: typing.Optional[bool]

### ReservedNodeId
- **Type**: typing.Optional[str]

### TargetReservedNodeOfferingId
- **Type**: typing.Optional[str]


# ResizeClusterMessageRequest

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterType
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### Classic
- **Type**: typing.Optional[bool]

### ReservedNodeId
- **Type**: typing.Optional[str]

### TargetReservedNodeOfferingId
- **Type**: typing.Optional[str]


# ResizeClusterResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ResizeInfo

### ResizeType
- **Type**: typing.Optional[str]

### AllowCancelResize
- **Type**: typing.Optional[bool]


# ResizeProgressMessage

### TargetNodeType
- **Type**: <class 'str'>
- **Required**: Yes

### TargetNumberOfNodes
- **Type**: <class 'int'>
- **Required**: Yes

### TargetClusterType
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ImportTablesCompleted
- **Type**: typing.List[str]
- **Required**: Yes

### ImportTablesInProgress
- **Type**: typing.List[str]
- **Required**: Yes

### ImportTablesNotStarted
- **Type**: typing.List[str]
- **Required**: Yes

### AvgResizeRateInMegaBytesPerSecond
- **Type**: <class 'float'>
- **Required**: Yes

### TotalResizeDataInMegaBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ProgressInMegaBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ElapsedTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### EstimatedTimeToCompletionInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResizeType
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### TargetEncryptionType
- **Type**: <class 'str'>
- **Required**: Yes

### DataTransferProgressPercent
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ResourcePolicy

### ResourceArn
- **Type**: typing.Optional[str]

### Policy
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


# RestoreFromClusterSnapshotMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### OwnerAccount
- **Type**: typing.Optional[str]

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### ElasticIp
- **Type**: typing.Optional[str]

### ClusterParameterGroupName
- **Type**: typing.Optional[str]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### AdditionalInfo
- **Type**: typing.Optional[str]

### IamRoles
- **Type**: typing.Optional[typing.List[str]]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### SnapshotScheduleIdentifier
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### AvailabilityZoneRelocation
- **Type**: typing.Optional[bool]

### AquaConfigurationStatus
- **Type**: typing.Optional[typing.Literal['auto', 'disabled', 'enabled']]

### DefaultIamRoleArn
- **Type**: typing.Optional[str]

### ReservedNodeId
- **Type**: typing.Optional[str]

### TargetReservedNodeOfferingId
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### ManageMasterPassword
- **Type**: typing.Optional[bool]

### MasterPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]


# RestoreFromClusterSnapshotResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreStatus

### Status
- **Type**: typing.Optional[str]

### CurrentRestoreRateInMegaBytesPerSecond
- **Type**: typing.Optional[float]

### SnapshotSizeInMegaBytes
- **Type**: typing.Optional[int]

### ProgressInMegaBytes
- **Type**: typing.Optional[int]

### ElapsedTimeInSeconds
- **Type**: typing.Optional[int]

### EstimatedTimeToCompletionInSeconds
- **Type**: typing.Optional[int]


# RestoreTableFromClusterSnapshotMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTableName
- **Type**: <class 'str'>
- **Required**: Yes

### NewTableName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceSchemaName
- **Type**: typing.Optional[str]

### TargetDatabaseName
- **Type**: typing.Optional[str]

### TargetSchemaName
- **Type**: typing.Optional[str]

### EnableCaseSensitiveIdentifier
- **Type**: typing.Optional[bool]


# RestoreTableFromClusterSnapshotResult

### TableRestoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.TableRestoreStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ResumeClusterMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeClusterMessageRequest

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeClusterResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# RevisionTarget

### DatabaseRevision
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DatabaseRevisionReleaseDate
- **Type**: typing.Optional[datetime.datetime]


# RevokeClusterSecurityGroupIngressMessage

### ClusterSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CIDRIP
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# RevokeClusterSecurityGroupIngressResult

### ClusterSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterSecurityGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# RevokeEndpointAccessMessage

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Account
- **Type**: typing.Optional[str]

### VpcIds
- **Type**: typing.Optional[typing.List[str]]

### Force
- **Type**: typing.Optional[bool]


# RevokeSnapshotAccessMessage

### AccountWithRestoreAccess
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]


# RevokeSnapshotAccessResult

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# RotateEncryptionKeyMessage

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RotateEncryptionKeyResult

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# S3AccessGrantsScopeUnion

### ReadWriteAccess
- **Type**: <class 'NoneType'>


# ScheduledAction

### ScheduledActionName
- **Type**: typing.Optional[str]

### TargetAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.ScheduledActionType]

### Schedule
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[str]

### ScheduledActionDescription
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DISABLED']]

### NextInvocations
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# ScheduledActionFilter

### Name
- **Type**: typing.Literal['cluster-identifier', 'iam-role']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ScheduledActionResponse

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ScheduledActionType'>
- **Required**: Yes

### Schedule
- **Type**: <class 'str'>
- **Required**: Yes

### IamRole
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActionDescription
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DISABLED']
- **Required**: Yes

### NextInvocations
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# ScheduledActionType

### ResizeCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.ResizeClusterMessage]

### PauseCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.PauseClusterMessage]

### ResumeCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.ResumeClusterMessage]


# ScheduledActionsMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ScheduledAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# SecondaryClusterInfo

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterNode]]


# ServerlessIdentifier

### NamespaceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WorkgroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceIntegrationsUnion

### LakeFormation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.LakeFormationScopeUnion]]

### S3AccessGrants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.S3AccessGrantsScopeUnion]]


# ServiceIntegrationsUnionOutput

### LakeFormation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.LakeFormationScopeUnion]]

### S3AccessGrants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.S3AccessGrantsScopeUnion]]


# Snapshot

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotCreateTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### MasterUsername
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### EngineFullVersion
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### DBName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### EncryptedWithHSM
- **Type**: typing.Optional[bool]

### AccountsWithRestoreAccess
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.AccountWithRestoreAccess]]

### OwnerAccount
- **Type**: typing.Optional[str]

### TotalBackupSizeInMegaBytes
- **Type**: typing.Optional[float]

### ActualIncrementalBackupSizeInMegaBytes
- **Type**: typing.Optional[float]

### BackupProgressInMegaBytes
- **Type**: typing.Optional[float]

### CurrentBackupRateInMegaBytesPerSecond
- **Type**: typing.Optional[float]

### EstimatedSecondsToCompletion
- **Type**: typing.Optional[int]

### ElapsedTimeInSeconds
- **Type**: typing.Optional[int]

### SourceRegion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]

### RestorableNodeTypes
- **Type**: typing.Optional[typing.List[str]]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ManualSnapshotRemainingDays
- **Type**: typing.Optional[int]

### SnapshotRetentionStartTime
- **Type**: typing.Optional[datetime.datetime]

### MasterPasswordSecretArn
- **Type**: typing.Optional[str]

### MasterPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]


# SnapshotCopyGrant

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# SnapshotCopyGrantMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotCopyGrants
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SnapshotCopyGrant]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# SnapshotErrorMessage

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]

### FailureCode
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# SnapshotMessage

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Snapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# SnapshotSchedule

### ScheduleDefinitions
- **Type**: typing.Optional[typing.List[str]]

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### ScheduleDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]

### NextInvocations
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### AssociatedClusterCount
- **Type**: typing.Optional[int]

### AssociatedClusters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterAssociatedToSchedule]]


# SnapshotScheduleResponse

### ScheduleDefinitions
- **Type**: typing.List[str]
- **Required**: Yes

### ScheduleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]
- **Required**: Yes

### NextInvocations
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### AssociatedClusterCount
- **Type**: <class 'int'>
- **Required**: Yes

### AssociatedClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.ClusterAssociatedToSchedule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# SnapshotSortingEntity

### Attribute
- **Type**: typing.Literal['CREATE_TIME', 'SOURCE_TYPE', 'TOTAL_SIZE']
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# Subnet

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift.redshift_classes.AvailabilityZone]

### SubnetStatus
- **Type**: typing.Optional[str]


# SupportedOperation

### OperationName
- **Type**: typing.Optional[str]


# SupportedPlatform

### Name
- **Type**: typing.Optional[str]


# TableRestoreStatus

### TableRestoreRequestId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SUCCEEDED']]

### Message
- **Type**: typing.Optional[str]

### RequestTime
- **Type**: typing.Optional[datetime.datetime]

### ProgressInMegaBytes
- **Type**: typing.Optional[int]

### TotalDataInMegaBytes
- **Type**: typing.Optional[int]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SourceDatabaseName
- **Type**: typing.Optional[str]

### SourceSchemaName
- **Type**: typing.Optional[str]

### SourceTableName
- **Type**: typing.Optional[str]

### TargetDatabaseName
- **Type**: typing.Optional[str]

### TargetSchemaName
- **Type**: typing.Optional[str]

### NewTableName
- **Type**: typing.Optional[str]


# TableRestoreStatusMessage

### TableRestoreStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.TableRestoreStatus]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TaggedResource

### Tag
- **Type**: <class 'NoneType'>

### ResourceName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# TaggedResourceListMessage

### TaggedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.TaggedResource]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# TrackListMessage

### MaintenanceTracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.MaintenanceTrack]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePartnerStatusInputMessage

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'ConnectionFailure', 'Inactive', 'RuntimeFailure']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Optional[str]


# UpdateTarget

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### DatabaseVersion
- **Type**: typing.Optional[str]

### SupportedOperations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.SupportedOperation]]


# UsageLimit

### UsageLimitId
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### FeatureType
- **Type**: typing.Optional[typing.Literal['concurrency-scaling', 'cross-region-datasharing', 'spectrum']]

### LimitType
- **Type**: typing.Optional[typing.Literal['data-scanned', 'time']]

### Amount
- **Type**: typing.Optional[int]

### Period
- **Type**: typing.Optional[typing.Literal['daily', 'monthly', 'weekly']]

### BreachAction
- **Type**: typing.Optional[typing.Literal['disable', 'emit-metric', 'log']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]]


# UsageLimitList

### UsageLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.UsageLimit]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# UsageLimitResponse

### UsageLimitId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureType
- **Type**: typing.Literal['concurrency-scaling', 'cross-region-datasharing', 'spectrum']
- **Required**: Yes

### LimitType
- **Type**: typing.Literal['data-scanned', 'time']
- **Required**: Yes

### Amount
- **Type**: <class 'int'>
- **Required**: Yes

### Period
- **Type**: typing.Literal['daily', 'monthly', 'weekly']
- **Required**: Yes

### BreachAction
- **Type**: typing.Literal['disable', 'emit-metric', 'log']
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift.redshift_classes.ResponseMetadata'>
- **Required**: Yes


# VpcEndpoint

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### NetworkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift.redshift_classes.NetworkInterface]]


# VpcSecurityGroupMembership

### VpcSecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


