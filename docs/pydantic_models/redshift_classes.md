# Redshift Classes

# AcceptReservedNodeExchangeInputMessageTypeDef

### ReservedNodeId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetReservedNodeOfferingId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptReservedNodeExchangeOutputMessageTypeDef

### ExchangedReservedNode
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccountAttributeListTypeDef

### AccountAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.AccountAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccountAttributeTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.AttributeValueTargetTypeDef]]


# AccountWithRestoreAccessTypeDef

### AccountId
- **Type**: typing.Optional[str]

### AccountAlias
- **Type**: typing.Optional[str]


# AquaConfigurationTypeDef

### AquaStatus
- **Type**: typing.Optional[typing.Literal['applying', 'disabled', 'enabled']]

### AquaConfigurationStatus
- **Type**: typing.Optional[typing.Literal['auto', 'disabled', 'enabled']]


# AssociateDataShareConsumerMessageTypeDef

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


# AssociationTypeDef

### CustomDomainCertificateArn
- **Type**: typing.Optional[str]

### CustomDomainCertificateExpiryDate
- **Type**: typing.Optional[datetime.datetime]

### CertificateAssociations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.CertificateAssociationTypeDef]]


# AttributeValueTargetTypeDef

### AttributeValue
- **Type**: typing.Optional[str]


# AuthenticationProfileTypeDef

### AuthenticationProfileName
- **Type**: typing.Optional[str]

### AuthenticationProfileContent
- **Type**: typing.Optional[str]


# AuthorizeClusterSecurityGroupIngressMessageTypeDef

### ClusterSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CIDRIP
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# AuthorizeClusterSecurityGroupIngressResultTypeDef

### ClusterSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizeDataShareMessageTypeDef

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AllowWrites
- **Type**: typing.Optional[bool]


# AuthorizeEndpointAccessMessageTypeDef

### Account
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### VpcIds
- **Type**: typing.Optional[typing.Sequence[str]]


# AuthorizeSnapshotAccessMessageTypeDef

### AccountWithRestoreAccess
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]


# AuthorizeSnapshotAccessResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizedTokenIssuerOutputTypeDef

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]

### AuthorizedAudiencesList
- **Type**: typing.Optional[typing.List[str]]


# AuthorizedTokenIssuerTypeDef

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]

### AuthorizedAudiencesList
- **Type**: typing.Optional[typing.Sequence[str]]


# AuthorizedTokenIssuerUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]

### SupportedPlatforms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.SupportedPlatformTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteClusterSnapshotsRequestTypeDef

### Identifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.DeleteClusterSnapshotMessageTypeDef]
- **Required**: Yes


# BatchDeleteClusterSnapshotsResultTypeDef

### Resources
- **Type**: typing.List[str]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.SnapshotErrorMessageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchModifyClusterSnapshotsMessageTypeDef

### SnapshotIdentifierList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### Force
- **Type**: typing.Optional[bool]


# BatchModifyClusterSnapshotsOutputMessageTypeDef

### Resources
- **Type**: typing.List[str]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.SnapshotErrorMessageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelResizeMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CertificateAssociationTypeDef

### CustomDomainName
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]


# ClusterAssociatedToScheduleTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ScheduleAssociationState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'MODIFYING']]


# ClusterCredentialsTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterDbRevisionTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### CurrentDatabaseRevision
- **Type**: typing.Optional[str]

### DatabaseRevisionReleaseDate
- **Type**: typing.Optional[datetime.datetime]

### RevisionTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.RevisionTargetTypeDef]]


# ClusterDbRevisionsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterDbRevisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterDbRevisionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterExtendedCredentialsTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterIamRoleTypeDef

### IamRoleArn
- **Type**: typing.Optional[str]

### ApplyStatus
- **Type**: typing.Optional[str]


# ClusterNodeTypeDef

### NodeRole
- **Type**: typing.Optional[str]

### PrivateIPAddress
- **Type**: typing.Optional[str]

### PublicIPAddress
- **Type**: typing.Optional[str]


# ClusterParameterGroupDetailsTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ParameterTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterParameterGroupNameMessageTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterGroupStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterParameterGroupStatusTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ClusterParameterStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterParameterStatusTypeDef]]


# ClusterParameterGroupTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### ParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# ClusterParameterGroupsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterParameterGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterParameterStatusTypeDef

### ParameterName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterApplyErrorDescription
- **Type**: typing.Optional[str]


# ClusterSecurityGroupMembershipTypeDef

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ClusterSecurityGroupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSecurityGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterSecurityGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterSecurityGroupTypeDef

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EC2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.EC2SecurityGroupTypeDef]]

### IPRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.IPRangeTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# ClusterSnapshotCopyStatusTypeDef

### DestinationRegion
- **Type**: typing.Optional[str]

### RetentionPeriod
- **Type**: typing.Optional[int]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]


# ClusterSubnetGroupMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSubnetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterSubnetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClusterSubnetGroupTypeDef

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.SubnetTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]

### SupportedClusterIpAddressTypes
- **Type**: typing.Optional[typing.List[str]]


# ClusterTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.EndpointTypeDef]

### ClusterCreateTime
- **Type**: typing.Optional[datetime.datetime]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterSecurityGroupMembershipTypeDef]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.VpcSecurityGroupMembershipTypeDef]]

### ClusterParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterParameterGroupStatusTypeDef]]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PendingModifiedValuesTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.RestoreStatusTypeDef]

### DataTransferProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.DataTransferProgressTypeDef]

### HsmStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.HsmStatusTypeDef]

### ClusterSnapshotCopyStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ClusterSnapshotCopyStatusTypeDef]

### ClusterPublicKey
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterNodeTypeDef]]

### ElasticIpStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ElasticIpStatusTypeDef]

### ClusterRevisionNumber
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### IamRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterIamRoleTypeDef]]

### PendingActions
- **Type**: typing.Optional[typing.List[str]]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### ElasticResizeNumberOfNodeOptions
- **Type**: typing.Optional[str]

### DeferredMaintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.DeferredMaintenanceWindowTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ResizeInfoTypeDef]

### AvailabilityZoneRelocationStatus
- **Type**: typing.Optional[str]

### ClusterNamespaceArn
- **Type**: typing.Optional[str]

### TotalStorageCapacityInMegaBytes
- **Type**: typing.Optional[int]

### AquaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.AquaConfigurationTypeDef]

### DefaultIamRoleArn
- **Type**: typing.Optional[str]

### ReservedNodeExchangeStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeExchangeStatusTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.SecondaryClusterInfoTypeDef]


# ClusterVersionTypeDef

### ClusterVersion
- **Type**: typing.Optional[str]

### ClusterParameterGroupFamily
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ClusterVersionsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClustersMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopyClusterSnapshotMessageTypeDef

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


# CopyClusterSnapshotResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAuthenticationProfileMessageTypeDef

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationProfileContent
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAuthenticationProfileResultTypeDef

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationProfileContent
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### AdditionalInfo
- **Type**: typing.Optional[str]

### IamRoles
- **Type**: typing.Optional[typing.Sequence[str]]

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


# CreateClusterParameterGroupMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CreateClusterParameterGroupResultTypeDef

### ClusterParameterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterParameterGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterSecurityGroupMessageTypeDef

### ClusterSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CreateClusterSecurityGroupResultTypeDef

### ClusterSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterSnapshotMessageTypeDef

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CreateClusterSnapshotResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterSubnetGroupMessageTypeDef

### ClusterSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CreateClusterSubnetGroupResultTypeDef

### ClusterSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomDomainAssociationMessageTypeDef

### CustomDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomDomainAssociationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEndpointAccessMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateEventSubscriptionMessageTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]

### SourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Severity
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CreateEventSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHsmClientCertificateMessageTypeDef

### HsmClientCertificateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CreateHsmClientCertificateResultTypeDef

### HsmClientCertificate
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.HsmClientCertificateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHsmConfigurationMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CreateHsmConfigurationResultTypeDef

### HsmConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.HsmConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]

### AdditionalEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Description
- **Type**: typing.Optional[str]


# CreateRedshiftIdcApplicationMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.AuthorizedTokenIssuerUnionTypeDef]]

### ServiceIntegrations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.ServiceIntegrationsUnionUnionTypeDef]]


# CreateRedshiftIdcApplicationResultTypeDef

### RedshiftIdcApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.RedshiftIdcApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateScheduledActionMessageTypeDef

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ScheduledActionTypeTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### Enable
- **Type**: typing.Optional[bool]


# CreateSnapshotCopyGrantMessageTypeDef

### SnapshotCopyGrantName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CreateSnapshotCopyGrantResultTypeDef

### SnapshotCopyGrant
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.SnapshotCopyGrantTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotScheduleMessageTypeDef

### ScheduleDefinitions
- **Type**: typing.Optional[typing.Sequence[str]]

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### ScheduleDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]

### DryRun
- **Type**: typing.Optional[bool]

### NextInvocations
- **Type**: typing.Optional[int]


# CreateTagsMessageTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]
- **Required**: Yes


# CreateUsageLimitMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# CustomDomainAssociationsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.AssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerStorageMessageTypeDef

### TotalBackupSizeInMegaBytes
- **Type**: <class 'float'>
- **Required**: Yes

### TotalProvisionedStorageInMegaBytes
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataShareAssociationTypeDef

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


# DataShareResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.DataShareAssociationTypeDef]
- **Required**: Yes

### ManagedBy
- **Type**: <class 'str'>
- **Required**: Yes

### DataShareType
- **Type**: typing.Literal['INTERNAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataShareTypeDef

### DataShareArn
- **Type**: typing.Optional[str]

### ProducerArn
- **Type**: typing.Optional[str]

### AllowPubliclyAccessibleConsumers
- **Type**: typing.Optional[bool]

### DataShareAssociations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.DataShareAssociationTypeDef]]

### ManagedBy
- **Type**: typing.Optional[str]

### DataShareType
- **Type**: typing.Optional[typing.Literal['INTERNAL']]


# DataTransferProgressTypeDef

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


# DeauthorizeDataShareMessageTypeDef

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DefaultClusterParametersTypeDef

### ParameterGroupFamily
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ParameterTypeDef]]


# DeferredMaintenanceWindowTypeDef

### DeferMaintenanceIdentifier
- **Type**: typing.Optional[str]

### DeferMaintenanceStartTime
- **Type**: typing.Optional[datetime.datetime]

### DeferMaintenanceEndTime
- **Type**: typing.Optional[datetime.datetime]


# DeleteAuthenticationProfileMessageTypeDef

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthenticationProfileResultTypeDef

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SkipFinalClusterSnapshot
- **Type**: typing.Optional[bool]

### FinalClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### FinalClusterSnapshotRetentionPeriod
- **Type**: typing.Optional[int]


# DeleteClusterParameterGroupMessageTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterSecurityGroupMessageTypeDef

### ClusterSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterSnapshotMessageRequestTypeDef

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]


# DeleteClusterSnapshotMessageTypeDef

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]


# DeleteClusterSnapshotResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterSubnetGroupMessageTypeDef

### ClusterSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomDomainAssociationMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointAccessMessageTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSubscriptionMessageTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHsmClientCertificateMessageTypeDef

### HsmClientCertificateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHsmConfigurationMessageTypeDef

### HsmConfigurationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationMessageTypeDef

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRedshiftIdcApplicationMessageTypeDef

### RedshiftIdcApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyMessageTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledActionMessageTypeDef

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotCopyGrantMessageTypeDef

### SnapshotCopyGrantName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotScheduleMessageTypeDef

### ScheduleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsMessageTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteUsageLimitMessageTypeDef

### UsageLimitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterNamespaceInputMessageTypeDef

### NamespaceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.NamespaceIdentifierUnionTypeDef'>
- **Required**: Yes

### ConsumerIdentifiers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeregisterNamespaceOutputMessageTypeDef

### Status
- **Type**: typing.Literal['Deregistering', 'Registering']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountAttributesMessageTypeDef

### AttributeNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeAuthenticationProfilesMessageTypeDef

### AuthenticationProfileName
- **Type**: typing.Optional[str]


# DescribeAuthenticationProfilesResultTypeDef

### AuthenticationProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.AuthenticationProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterDbRevisionsMessagePaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClusterDbRevisionsMessageTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeClusterParameterGroupsMessagePaginateTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClusterParameterGroupsMessageTypeDef

### ParameterGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeClusterParametersMessagePaginateTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClusterParametersMessageTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeClusterSecurityGroupsMessagePaginateTypeDef

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClusterSecurityGroupsMessageTypeDef

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeClusterSnapshotsMessagePaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### OwnerAccount
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### ClusterExists
- **Type**: typing.Optional[bool]

### SortingEntities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.SnapshotSortingEntityTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClusterSnapshotsMessageTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### OwnerAccount
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### ClusterExists
- **Type**: typing.Optional[bool]

### SortingEntities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.SnapshotSortingEntityTypeDef]]


# DescribeClusterSnapshotsMessageWaitTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### OwnerAccount
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### ClusterExists
- **Type**: typing.Optional[bool]

### SortingEntities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.SnapshotSortingEntityTypeDef]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.WaiterConfigTypeDef]


# DescribeClusterSubnetGroupsMessagePaginateTypeDef

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClusterSubnetGroupsMessageTypeDef

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeClusterTracksMessagePaginateTypeDef

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClusterTracksMessageTypeDef

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeClusterVersionsMessagePaginateTypeDef

### ClusterVersion
- **Type**: typing.Optional[str]

### ClusterParameterGroupFamily
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClusterVersionsMessageTypeDef

### ClusterVersion
- **Type**: typing.Optional[str]

### ClusterParameterGroupFamily
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeClustersMessagePaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeClustersMessageTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeClustersMessageWaitExtraExtraTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.WaiterConfigTypeDef]


# DescribeClustersMessageWaitExtraTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.WaiterConfigTypeDef]


# DescribeClustersMessageWaitTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.WaiterConfigTypeDef]


# DescribeCustomDomainAssociationsMessagePaginateTypeDef

### CustomDomainName
- **Type**: typing.Optional[str]

### CustomDomainCertificateArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeCustomDomainAssociationsMessageTypeDef

### CustomDomainName
- **Type**: typing.Optional[str]

### CustomDomainCertificateArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataSharesForConsumerMessagePaginateTypeDef

### ConsumerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AVAILABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeDataSharesForConsumerMessageTypeDef

### ConsumerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AVAILABLE']]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataSharesForConsumerResultTypeDef

### DataShares
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.DataShareTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSharesForProducerMessagePaginateTypeDef

### ProducerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AUTHORIZED', 'DEAUTHORIZED', 'PENDING_AUTHORIZATION', 'REJECTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeDataSharesForProducerMessageTypeDef

### ProducerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AUTHORIZED', 'DEAUTHORIZED', 'PENDING_AUTHORIZATION', 'REJECTED']]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataSharesForProducerResultTypeDef

### DataShares
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.DataShareTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSharesMessagePaginateTypeDef

### DataShareArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeDataSharesMessageTypeDef

### DataShareArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDataSharesResultTypeDef

### DataShares
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.DataShareTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDefaultClusterParametersMessagePaginateTypeDef

### ParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeDefaultClusterParametersMessageTypeDef

### ParameterGroupFamily
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeDefaultClusterParametersResultTypeDef

### DefaultClusterParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.DefaultClusterParametersTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointAccessMessagePaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeEndpointAccessMessageTypeDef

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


# DescribeEndpointAuthorizationMessagePaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Account
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeEndpointAuthorizationMessageTypeDef

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


# DescribeEventCategoriesMessageTypeDef

### SourceType
- **Type**: typing.Optional[str]


# DescribeEventSubscriptionsMessagePaginateTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeEventSubscriptionsMessageTypeDef

### SubscriptionName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeEventsMessagePaginateTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cluster', 'cluster-parameter-group', 'cluster-security-group', 'cluster-snapshot', 'scheduled-action']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeEventsMessageTypeDef

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['cluster', 'cluster-parameter-group', 'cluster-security-group', 'cluster-snapshot', 'scheduled-action']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### Duration
- **Type**: typing.Optional[int]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeHsmClientCertificatesMessagePaginateTypeDef

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeHsmClientCertificatesMessageTypeDef

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeHsmConfigurationsMessagePaginateTypeDef

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeHsmConfigurationsMessageTypeDef

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeInboundIntegrationsMessagePaginateTypeDef

### IntegrationArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeInboundIntegrationsMessageTypeDef

### IntegrationArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeIntegrationsFilterTypeDef

### Name
- **Type**: typing.Literal['integration-arn', 'source-arn', 'source-types', 'status']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeIntegrationsMessagePaginateTypeDef

### IntegrationArn
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.DescribeIntegrationsFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeIntegrationsMessageTypeDef

### IntegrationArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.DescribeIntegrationsFilterTypeDef]]


# DescribeLoggingStatusMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeConfigurationOptionsMessagePaginateTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.NodeConfigurationOptionsFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeNodeConfigurationOptionsMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.NodeConfigurationOptionsFilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeOrderableClusterOptionsMessagePaginateTypeDef

### ClusterVersion
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeOrderableClusterOptionsMessageTypeDef

### ClusterVersion
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribePartnersInputMessageTypeDef

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


# DescribePartnersOutputMessageTypeDef

### PartnerIntegrationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.PartnerIntegrationInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRedshiftIdcApplicationsMessagePaginateTypeDef

### RedshiftIdcApplicationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeRedshiftIdcApplicationsMessageTypeDef

### RedshiftIdcApplicationArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeRedshiftIdcApplicationsResultTypeDef

### RedshiftIdcApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.RedshiftIdcApplicationTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReservedNodeExchangeStatusInputMessagePaginateTypeDef

### ReservedNodeId
- **Type**: typing.Optional[str]

### ReservedNodeExchangeRequestId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeReservedNodeExchangeStatusInputMessageTypeDef

### ReservedNodeId
- **Type**: typing.Optional[str]

### ReservedNodeExchangeRequestId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedNodeExchangeStatusOutputMessageTypeDef

### ReservedNodeExchangeStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeExchangeStatusTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReservedNodeOfferingsMessagePaginateTypeDef

### ReservedNodeOfferingId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeReservedNodeOfferingsMessageTypeDef

### ReservedNodeOfferingId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeReservedNodesMessagePaginateTypeDef

### ReservedNodeId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeReservedNodesMessageTypeDef

### ReservedNodeId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeResizeMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScheduledActionsMessagePaginateTypeDef

### ScheduledActionName
- **Type**: typing.Optional[str]

### TargetActionType
- **Type**: typing.Optional[typing.Literal['PauseCluster', 'ResizeCluster', 'ResumeCluster']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### Active
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.ScheduledActionFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeScheduledActionsMessageTypeDef

### ScheduledActionName
- **Type**: typing.Optional[str]

### TargetActionType
- **Type**: typing.Optional[typing.Literal['PauseCluster', 'ResizeCluster', 'ResumeCluster']]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### Active
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.ScheduledActionFilterTypeDef]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeSnapshotCopyGrantsMessagePaginateTypeDef

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeSnapshotCopyGrantsMessageTypeDef

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeSnapshotSchedulesMessagePaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeSnapshotSchedulesMessageTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]


# DescribeSnapshotSchedulesOutputMessageTypeDef

### SnapshotSchedules
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.SnapshotScheduleTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTableRestoreStatusMessagePaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### TableRestoreRequestId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeTableRestoreStatusMessageTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### TableRestoreRequestId
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeTagsMessagePaginateTypeDef

### ResourceName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeTagsMessageTypeDef

### ResourceName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeUsageLimitsMessagePaginateTypeDef

### UsageLimitId
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### FeatureType
- **Type**: typing.Optional[typing.Literal['concurrency-scaling', 'cross-region-datasharing', 'spectrum']]

### TagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# DescribeUsageLimitsMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### TagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DisableLoggingMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisableSnapshotCopyMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisableSnapshotCopyResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateDataShareConsumerMessageTypeDef

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisassociateEntireAccount
- **Type**: typing.Optional[bool]

### ConsumerArn
- **Type**: typing.Optional[str]

### ConsumerRegion
- **Type**: typing.Optional[str]


# EC2SecurityGroupTypeDef

### Status
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# ElasticIpStatusTypeDef

### ElasticIp
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableLoggingMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]


# EnableSnapshotCopyMessageTypeDef

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


# EnableSnapshotCopyResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointAccessListTypeDef

### EndpointAccessList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.EndpointAccessTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointAccessResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.VpcSecurityGroupMembershipTypeDef]
- **Required**: Yes

### VpcEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.VpcEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointAccessTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.VpcSecurityGroupMembershipTypeDef]]

### VpcEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.VpcEndpointTypeDef]


# EndpointAuthorizationListTypeDef

### EndpointAuthorizationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.EndpointAuthorizationTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointAuthorizationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointAuthorizationTypeDef

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


# EndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.VpcEndpointTypeDef]]


# EventCategoriesMapTypeDef

### SourceType
- **Type**: typing.Optional[str]

### Events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.EventInfoMapTypeDef]]


# EventCategoriesMessageTypeDef

### EventCategoriesMapList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.EventCategoriesMapTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventInfoMapTypeDef

### EventId
- **Type**: typing.Optional[str]

### EventCategories
- **Type**: typing.Optional[typing.List[str]]

### EventDescription
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]


# EventSubscriptionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# EventSubscriptionsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSubscriptionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.EventSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventTypeDef

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


# EventsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailoverPrimaryComputeInputMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# FailoverPrimaryComputeResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetClusterCredentialsMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### CustomDomainName
- **Type**: typing.Optional[str]


# GetClusterCredentialsWithIAMMessageTypeDef

### DbName
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]

### CustomDomainName
- **Type**: typing.Optional[str]


# GetReservedNodeExchangeConfigurationOptionsInputMessagePaginateTypeDef

### ActionType
- **Type**: typing.Literal['resize-cluster', 'restore-cluster']
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# GetReservedNodeExchangeConfigurationOptionsInputMessageTypeDef

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


# GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodeConfigurationOptionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeConfigurationOptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReservedNodeExchangeOfferingsInputMessagePaginateTypeDef

### ReservedNodeId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# GetReservedNodeExchangeOfferingsInputMessageTypeDef

### ReservedNodeId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetReservedNodeExchangeOfferingsOutputMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodeOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyMessageTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResultTypeDef

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HsmClientCertificateMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### HsmClientCertificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.HsmClientCertificateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HsmClientCertificateTypeDef

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmClientCertificatePublicKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# HsmConfigurationMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### HsmConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.HsmConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HsmConfigurationTypeDef

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HsmIpAddress
- **Type**: typing.Optional[str]

### HsmPartitionName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# HsmStatusTypeDef

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# IPRangeTypeDef

### Status
- **Type**: typing.Optional[str]

### CIDRIP
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# InboundIntegrationTypeDef

### IntegrationArn
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### TargetArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['active', 'creating', 'deleting', 'failed', 'modifying', 'needs_attention', 'syncing']]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.IntegrationErrorTypeDef]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]


# InboundIntegrationsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### InboundIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.InboundIntegrationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IntegrationErrorTypeDef

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: typing.Optional[str]


# IntegrationResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.IntegrationErrorTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IntegrationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.IntegrationErrorTypeDef]]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### KMSKeyId
- **Type**: typing.Optional[str]

### AdditionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# IntegrationsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Integrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.IntegrationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LakeFormationQueryTypeDef

### Authorization
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# LakeFormationScopeUnionTypeDef

### LakeFormationQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.LakeFormationQueryTypeDef]


# ListRecommendationsMessagePaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### NamespaceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PaginatorConfigTypeDef]


# ListRecommendationsMessageTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### NamespaceArn
- **Type**: typing.Optional[str]

### MaxRecords
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListRecommendationsResultTypeDef

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.RecommendationTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingStatusTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MaintenanceTrackTypeDef

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### DatabaseVersion
- **Type**: typing.Optional[str]

### UpdateTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.UpdateTargetTypeDef]]


# ModifyAquaInputMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AquaConfigurationStatus
- **Type**: typing.Optional[typing.Literal['auto', 'disabled', 'enabled']]


# ModifyAquaOutputMessageTypeDef

### AquaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.AquaConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyAuthenticationProfileMessageTypeDef

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationProfileContent
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyAuthenticationProfileResultTypeDef

### AuthenticationProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationProfileContent
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyClusterDbRevisionMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionTarget
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyClusterDbRevisionResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyClusterIamRolesMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AddIamRoles
- **Type**: typing.Optional[typing.Sequence[str]]

### RemoveIamRoles
- **Type**: typing.Optional[typing.Sequence[str]]

### DefaultIamRoleArn
- **Type**: typing.Optional[str]


# ModifyClusterIamRolesResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyClusterMaintenanceMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeferMaintenance
- **Type**: typing.Optional[bool]

### DeferMaintenanceIdentifier
- **Type**: typing.Optional[str]

### DeferMaintenanceStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### DeferMaintenanceEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### DeferMaintenanceDuration
- **Type**: typing.Optional[int]


# ModifyClusterMaintenanceResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyClusterMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

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


# ModifyClusterParameterGroupMessageTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.ParameterTypeDef]
- **Required**: Yes


# ModifyClusterResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyClusterSnapshotMessageTypeDef

### SnapshotIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### Force
- **Type**: typing.Optional[bool]


# ModifyClusterSnapshotResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyClusterSnapshotScheduleMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### DisassociateSchedule
- **Type**: typing.Optional[bool]


# ModifyClusterSubnetGroupMessageTypeDef

### ClusterSubnetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ModifyClusterSubnetGroupResultTypeDef

### ClusterSubnetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterSubnetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyCustomDomainAssociationMessageTypeDef

### CustomDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ModifyCustomDomainAssociationResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyEndpointAccessMessageTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ModifyEventSubscriptionMessageTypeDef

### SubscriptionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### SourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EventCategories
- **Type**: typing.Optional[typing.Sequence[str]]

### Severity
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# ModifyEventSubscriptionResultTypeDef

### EventSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.EventSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyIntegrationMessageTypeDef

### IntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IntegrationName
- **Type**: typing.Optional[str]


# ModifyRedshiftIdcApplicationMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.AuthorizedTokenIssuerUnionTypeDef]]

### ServiceIntegrations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.ServiceIntegrationsUnionUnionTypeDef]]


# ModifyRedshiftIdcApplicationResultTypeDef

### RedshiftIdcApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.RedshiftIdcApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyScheduledActionMessageTypeDef

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ScheduledActionTypeTypeDef]

### Schedule
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[str]

### ScheduledActionDescription
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TimestampTypeDef]

### Enable
- **Type**: typing.Optional[bool]


# ModifySnapshotCopyRetentionPeriodMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### Manual
- **Type**: typing.Optional[bool]


# ModifySnapshotCopyRetentionPeriodResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifySnapshotScheduleMessageTypeDef

### ScheduleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleDefinitions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ModifyUsageLimitMessageTypeDef

### UsageLimitId
- **Type**: <class 'str'>
- **Required**: Yes

### Amount
- **Type**: typing.Optional[int]

### BreachAction
- **Type**: typing.Optional[typing.Literal['disable', 'emit-metric', 'log']]


# NamespaceIdentifierUnionTypeDef

### ServerlessIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ServerlessIdentifierTypeDef]

### ProvisionedIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ProvisionedIdentifierTypeDef]


# NetworkInterfaceTypeDef

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


# NodeConfigurationOptionTypeDef

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### EstimatedDiskUtilizationPercent
- **Type**: typing.Optional[float]

### Mode
- **Type**: typing.Optional[typing.Literal['high-performance', 'standard']]


# NodeConfigurationOptionsFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['EstimatedDiskUtilizationPercent', 'Mode', 'NodeType', 'NumberOfNodes']]

### Operator
- **Type**: typing.Optional[typing.Literal['between', 'eq', 'ge', 'gt', 'in', 'le', 'lt']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# NodeConfigurationOptionsMessageTypeDef

### NodeConfigurationOptionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.NodeConfigurationOptionTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OrderableClusterOptionTypeDef

### ClusterVersion
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.AvailabilityZoneTypeDef]]


# OrderableClusterOptionsMessageTypeDef

### OrderableClusterOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.OrderableClusterOptionTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterTypeDef

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


# PartnerIntegrationInfoTypeDef

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


# PartnerIntegrationInputMessageRequestTypeDef

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


# PartnerIntegrationInputMessageTypeDef

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


# PartnerIntegrationOutputMessageTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PauseClusterMessageRequestTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PauseClusterMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PauseClusterResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PendingModifiedValuesTypeDef

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


# ProvisionedIdentifierTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PurchaseReservedNodeOfferingMessageTypeDef

### ReservedNodeOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeCount
- **Type**: typing.Optional[int]


# PurchaseReservedNodeOfferingResultTypeDef

### ReservedNode
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyMessageTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyResultTypeDef

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReadWriteAccessTypeDef

### Authorization
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# RebootClusterMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RebootClusterResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecommendationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.RecommendedActionTypeDef]]

### ReferenceLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ReferenceLinkTypeDef]]


# RecommendedActionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecurringChargeTypeDef

### RecurringChargeAmount
- **Type**: typing.Optional[float]

### RecurringChargeFrequency
- **Type**: typing.Optional[str]


# RedshiftIdcApplicationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.AuthorizedTokenIssuerOutputTypeDef]]

### ServiceIntegrations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ServiceIntegrationsUnionOutputTypeDef]]


# ReferenceLinkTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegisterNamespaceInputMessageTypeDef

### NamespaceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.NamespaceIdentifierUnionTypeDef'>
- **Required**: Yes

### ConsumerIdentifiers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RegisterNamespaceOutputMessageTypeDef

### Status
- **Type**: typing.Literal['Deregistering', 'Registering']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RejectDataShareMessageTypeDef

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes


# ReservedNodeConfigurationOptionTypeDef

### SourceReservedNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeTypeDef]

### TargetReservedNodeCount
- **Type**: typing.Optional[int]

### TargetReservedNodeOffering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeOfferingTypeDef]


# ReservedNodeExchangeStatusTypeDef

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


# ReservedNodeOfferingTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.RecurringChargeTypeDef]]

### ReservedNodeOfferingType
- **Type**: typing.Optional[typing.Literal['Regular', 'Upgradable']]


# ReservedNodeOfferingsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodeOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReservedNodeTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.RecurringChargeTypeDef]]

### ReservedNodeOfferingType
- **Type**: typing.Optional[typing.Literal['Regular', 'Upgradable']]


# ReservedNodesMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ReservedNodeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResetClusterParameterGroupMessageTypeDef

### ParameterGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResetAllParameters
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.ParameterTypeDef]]


# ResizeClusterMessageRequestTypeDef

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


# ResizeClusterMessageTypeDef

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


# ResizeClusterResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResizeInfoTypeDef

### ResizeType
- **Type**: typing.Optional[str]

### AllowCancelResize
- **Type**: typing.Optional[bool]


# ResizeProgressMessageTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourcePolicyTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### Policy
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


# RestoreFromClusterSnapshotMessageTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

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
- **Type**: typing.Optional[typing.Sequence[str]]

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


# RestoreFromClusterSnapshotResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreStatusTypeDef

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


# RestoreTableFromClusterSnapshotMessageTypeDef

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


# RestoreTableFromClusterSnapshotResultTypeDef

### TableRestoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.TableRestoreStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResumeClusterMessageRequestTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeClusterMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeClusterResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RevisionTargetTypeDef

### DatabaseRevision
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DatabaseRevisionReleaseDate
- **Type**: typing.Optional[datetime.datetime]


# RevokeClusterSecurityGroupIngressMessageTypeDef

### ClusterSecurityGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CIDRIP
- **Type**: typing.Optional[str]

### EC2SecurityGroupName
- **Type**: typing.Optional[str]

### EC2SecurityGroupOwnerId
- **Type**: typing.Optional[str]


# RevokeClusterSecurityGroupIngressResultTypeDef

### ClusterSecurityGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterSecurityGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RevokeEndpointAccessMessageTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Account
- **Type**: typing.Optional[str]

### VpcIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Force
- **Type**: typing.Optional[bool]


# RevokeSnapshotAccessMessageTypeDef

### AccountWithRestoreAccess
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotArn
- **Type**: typing.Optional[str]

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]


# RevokeSnapshotAccessResultTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RotateEncryptionKeyMessageTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RotateEncryptionKeyResultTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3AccessGrantsScopeUnionTypeDef

### ReadWriteAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ReadWriteAccessTypeDef]


# ScheduledActionFilterTypeDef

### Name
- **Type**: typing.Literal['cluster-identifier', 'iam-role']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ScheduledActionResponseTypeDef

### ScheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ScheduledActionTypeTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ScheduledActionTypeDef

### ScheduledActionName
- **Type**: typing.Optional[str]

### TargetAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ScheduledActionTypeTypeDef]

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


# ScheduledActionTypeTypeDef

### ResizeCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ResizeClusterMessageTypeDef]

### PauseCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.PauseClusterMessageTypeDef]

### ResumeCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.ResumeClusterMessageTypeDef]


# ScheduledActionsMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ScheduledActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SecondaryClusterInfoTypeDef

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterNodeTypeDef]]


# ServerlessIdentifierTypeDef

### NamespaceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### WorkgroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceIntegrationsUnionOutputTypeDef

### LakeFormation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.LakeFormationScopeUnionTypeDef]]

### S3AccessGrants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.S3AccessGrantsScopeUnionTypeDef]]


# ServiceIntegrationsUnionTypeDef

### LakeFormation
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.LakeFormationScopeUnionTypeDef]]

### S3AccessGrants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_classes.S3AccessGrantsScopeUnionTypeDef]]


# ServiceIntegrationsUnionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnapshotCopyGrantMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotCopyGrants
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.SnapshotCopyGrantTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SnapshotCopyGrantTypeDef

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# SnapshotErrorMessageTypeDef

### SnapshotIdentifier
- **Type**: typing.Optional[str]

### SnapshotClusterIdentifier
- **Type**: typing.Optional[str]

### FailureCode
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# SnapshotMessageTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SnapshotScheduleResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]
- **Required**: Yes

### NextInvocations
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### AssociatedClusterCount
- **Type**: <class 'int'>
- **Required**: Yes

### AssociatedClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterAssociatedToScheduleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SnapshotScheduleTypeDef

### ScheduleDefinitions
- **Type**: typing.Optional[typing.List[str]]

### ScheduleIdentifier
- **Type**: typing.Optional[str]

### ScheduleDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]

### NextInvocations
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### AssociatedClusterCount
- **Type**: typing.Optional[int]

### AssociatedClusters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.ClusterAssociatedToScheduleTypeDef]]


# SnapshotSortingEntityTypeDef

### Attribute
- **Type**: typing.Literal['CREATE_TIME', 'SOURCE_TYPE', 'TOTAL_SIZE']
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# SnapshotTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.AccountWithRestoreAccessTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]

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


# SubnetTypeDef

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.AvailabilityZoneTypeDef]

### SubnetStatus
- **Type**: typing.Optional[str]


# SupportedOperationTypeDef

### OperationName
- **Type**: typing.Optional[str]


# SupportedPlatformTypeDef

### Name
- **Type**: typing.Optional[str]


# TableRestoreStatusMessageTypeDef

### TableRestoreStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.TableRestoreStatusTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TableRestoreStatusTypeDef

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


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TaggedResourceListMessageTypeDef

### TaggedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.TaggedResourceTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TaggedResourceTypeDef

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]

### ResourceName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrackListMessageTypeDef

### MaintenanceTracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.MaintenanceTrackTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePartnerStatusInputMessageTypeDef

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


# UpdateTargetTypeDef

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### DatabaseVersion
- **Type**: typing.Optional[str]

### SupportedOperations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.SupportedOperationTypeDef]]


# UsageLimitListTypeDef

### UsageLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.UsageLimitTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageLimitResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageLimitTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.TagTypeDef]]


# VpcEndpointTypeDef

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### NetworkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_classes.NetworkInterfaceTypeDef]]


# VpcSecurityGroupMembershipTypeDef

### VpcSecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


