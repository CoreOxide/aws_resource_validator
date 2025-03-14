# Redshift Serverless Classes

# AssociationTypeDef

### customDomainCertificateArn
- **Type**: typing.Optional[str]

### customDomainCertificateExpiryTime
- **Type**: typing.Optional[datetime.datetime]

### customDomainName
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigParameterTypeDef

### parameterKey
- **Type**: typing.Optional[str]

### parameterValue
- **Type**: typing.Optional[str]


# ConvertRecoveryPointToSnapshotRequestTypeDef

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]]


# ConvertRecoveryPointToSnapshotResponseTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomDomainAssociationRequestTypeDef

### customDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomDomainAssociationResponseTypeDef

### customDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainCertificateExpiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEndpointAccessRequestTypeDef

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: typing.Optional[str]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateEndpointAccessResponseTypeDef

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.EndpointAccessTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNamespaceRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### adminPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### adminUserPassword
- **Type**: typing.Optional[str]

### adminUsername
- **Type**: typing.Optional[str]

### dbName
- **Type**: typing.Optional[str]

### defaultIamRoleArn
- **Type**: typing.Optional[str]

### iamRoles
- **Type**: typing.Optional[typing.Sequence[str]]

### kmsKeyId
- **Type**: typing.Optional[str]

### logExports
- **Type**: typing.Optional[typing.Sequence[typing.Literal['connectionlog', 'useractivitylog', 'userlog']]]

### manageAdminPassword
- **Type**: typing.Optional[bool]

### redshiftIdcApplicationArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]]


# CreateNamespaceResponseTypeDef

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.NamespaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateScheduledActionRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduleUnionTypeDef'>
- **Required**: Yes

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### targetAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.TargetActionUnionTypeDef'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### scheduledActionDescription
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]


# CreateScheduledActionResponseTypeDef

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduledActionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotCopyConfigurationRequestTypeDef

### destinationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### destinationKmsKeyId
- **Type**: typing.Optional[str]

### snapshotRetentionPeriod
- **Type**: typing.Optional[int]


# CreateSnapshotCopyConfigurationResponseTypeDef

### snapshotCopyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotCopyConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]]


# CreateSnapshotResponseTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotScheduleActionParametersOutputTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotNamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]]


# CreateSnapshotScheduleActionParametersTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotNamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]]


# CreateUsageLimitRequestTypeDef

### amount
- **Type**: <class 'int'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### usageType
- **Type**: typing.Literal['cross-region-datasharing', 'serverless-compute']
- **Required**: Yes

### breachAction
- **Type**: typing.Optional[typing.Literal['deactivate', 'emit-metric', 'log']]

### period
- **Type**: typing.Optional[typing.Literal['daily', 'monthly', 'weekly']]


# CreateUsageLimitResponseTypeDef

### usageLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.UsageLimitTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkgroupRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: typing.Optional[int]

### configParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.ConfigParameterTypeDef]]

### enhancedVpcRouting
- **Type**: typing.Optional[bool]

### ipAddressType
- **Type**: typing.Optional[str]

### maxCapacity
- **Type**: typing.Optional[int]

### port
- **Type**: typing.Optional[int]

### pricePerformanceTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PerformanceTargetTypeDef]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]]

### trackName
- **Type**: typing.Optional[str]


# CreateWorkgroupResponseTypeDef

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.WorkgroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomDomainAssociationRequestTypeDef

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointAccessRequestTypeDef

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointAccessResponseTypeDef

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.EndpointAccessTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNamespaceRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### finalSnapshotName
- **Type**: typing.Optional[str]

### finalSnapshotRetentionPeriod
- **Type**: typing.Optional[int]


# DeleteNamespaceResponseTypeDef

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.NamespaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledActionRequestTypeDef

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledActionResponseTypeDef

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduledActionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSnapshotCopyConfigurationRequestTypeDef

### snapshotCopyConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotCopyConfigurationResponseTypeDef

### snapshotCopyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotCopyConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSnapshotRequestTypeDef

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotResponseTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUsageLimitRequestTypeDef

### usageLimitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUsageLimitResponseTypeDef

### usageLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.UsageLimitTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkgroupRequestTypeDef

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkgroupResponseTypeDef

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.WorkgroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointAccessTypeDef

### address
- **Type**: typing.Optional[str]

### endpointArn
- **Type**: typing.Optional[str]

### endpointCreateTime
- **Type**: typing.Optional[datetime.datetime]

### endpointName
- **Type**: typing.Optional[str]

### endpointStatus
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### vpcEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.VpcEndpointTypeDef]

### vpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.VpcSecurityGroupMembershipTypeDef]]

### workgroupName
- **Type**: typing.Optional[str]


# EndpointTypeDef

### address
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### vpcEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.VpcEndpointTypeDef]]


# GetCredentialsRequestTypeDef

### customDomainName
- **Type**: typing.Optional[str]

### dbName
- **Type**: typing.Optional[str]

### durationSeconds
- **Type**: typing.Optional[int]

### workgroupName
- **Type**: typing.Optional[str]


# GetCredentialsResponseTypeDef

### dbPassword
- **Type**: <class 'str'>
- **Required**: Yes

### dbUser
- **Type**: <class 'str'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### nextRefreshTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCustomDomainAssociationRequestTypeDef

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomDomainAssociationResponseTypeDef

### customDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainCertificateExpiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEndpointAccessRequestTypeDef

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEndpointAccessResponseTypeDef

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.EndpointAccessTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNamespaceRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetNamespaceResponseTypeDef

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.NamespaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecoveryPointRequestTypeDef

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecoveryPointResponseTypeDef

### recoveryPoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.RecoveryPointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

### resourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetScheduledActionRequestTypeDef

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetScheduledActionResponseTypeDef

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduledActionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSnapshotRequestTypeDef

### ownerAccount
- **Type**: typing.Optional[str]

### snapshotArn
- **Type**: typing.Optional[str]

### snapshotName
- **Type**: typing.Optional[str]


# GetSnapshotResponseTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTableRestoreStatusRequestTypeDef

### tableRestoreRequestId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableRestoreStatusResponseTypeDef

### tableRestoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.TableRestoreStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrackRequestTypeDef

### trackName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrackResponseTypeDef

### track
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ServerlessTrackTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUsageLimitRequestTypeDef

### usageLimitId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsageLimitResponseTypeDef

### usageLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.UsageLimitTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkgroupRequestTypeDef

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkgroupResponseTypeDef

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.WorkgroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomDomainAssociationsRequestPaginateTypeDef

### customDomainCertificateArn
- **Type**: typing.Optional[str]

### customDomainName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListCustomDomainAssociationsRequestTypeDef

### customDomainCertificateArn
- **Type**: typing.Optional[str]

### customDomainName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomDomainAssociationsResponseTypeDef

### associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.AssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEndpointAccessRequestPaginateTypeDef

### ownerAccount
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListEndpointAccessRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]


# ListEndpointAccessResponseTypeDef

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.EndpointAccessTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedWorkgroupsRequestPaginateTypeDef

### sourceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListManagedWorkgroupsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sourceArn
- **Type**: typing.Optional[str]


# ListManagedWorkgroupsResponseTypeDef

### managedWorkgroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.ManagedWorkgroupListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNamespacesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListNamespacesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNamespacesResponseTypeDef

### namespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.NamespaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecoveryPointsRequestPaginateTypeDef

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListRecoveryPointsRequestTypeDef

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]


# ListRecoveryPointsResponseTypeDef

### recoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.RecoveryPointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsRequestPaginateTypeDef

### namespaceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListScheduledActionsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsResponseTypeDef

### scheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduledActionAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSnapshotCopyConfigurationsRequestPaginateTypeDef

### namespaceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListSnapshotCopyConfigurationsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListSnapshotCopyConfigurationsResponseTypeDef

### snapshotCopyConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotCopyConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSnapshotsRequestPaginateTypeDef

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListSnapshotsRequestTypeDef

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]


# ListSnapshotsResponseTypeDef

### snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTableRestoreStatusRequestPaginateTypeDef

### namespaceName
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListTableRestoreStatusRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]


# ListTableRestoreStatusResponseTypeDef

### tableRestoreStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.TableRestoreStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTracksRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListTracksRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTracksResponseTypeDef

### tracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.ServerlessTrackTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsageLimitsRequestPaginateTypeDef

### resourceArn
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['cross-region-datasharing', 'serverless-compute']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListUsageLimitsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['cross-region-datasharing', 'serverless-compute']]


# ListUsageLimitsResponseTypeDef

### usageLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.UsageLimitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkgroupsRequestPaginateTypeDef

### ownerAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListWorkgroupsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]


# ListWorkgroupsResponseTypeDef

### workgroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.WorkgroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ManagedWorkgroupListItemTypeDef

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### managedWorkgroupId
- **Type**: typing.Optional[str]

### managedWorkgroupName
- **Type**: typing.Optional[str]

### sourceArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'MODIFYING', 'NOT_AVAILABLE']]


# NamespaceTypeDef

### adminPasswordSecretArn
- **Type**: typing.Optional[str]

### adminPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### adminUsername
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### dbName
- **Type**: typing.Optional[str]

### defaultIamRoleArn
- **Type**: typing.Optional[str]

### iamRoles
- **Type**: typing.Optional[typing.List[str]]

### kmsKeyId
- **Type**: typing.Optional[str]

### logExports
- **Type**: typing.Optional[typing.List[typing.Literal['connectionlog', 'useractivitylog', 'userlog']]]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceId
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'MODIFYING']]


# NetworkInterfaceTypeDef

### availabilityZone
- **Type**: typing.Optional[str]

### ipv6Address
- **Type**: typing.Optional[str]

### networkInterfaceId
- **Type**: typing.Optional[str]

### privateIpAddress
- **Type**: typing.Optional[str]

### subnetId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceTargetTypeDef

### level
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# PutResourcePolicyRequestTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyResponseTypeDef

### resourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecoveryPointTypeDef

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### recoveryPointCreateTime
- **Type**: typing.Optional[datetime.datetime]

### recoveryPointId
- **Type**: typing.Optional[str]

### totalSizeInMegaBytes
- **Type**: typing.Optional[float]

### workgroupName
- **Type**: typing.Optional[str]


# ResourcePolicyTypeDef

### policy
- **Type**: typing.Optional[str]

### resourceArn
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


# RestoreFromRecoveryPointRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreFromRecoveryPointResponseTypeDef

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.NamespaceTypeDef'>
- **Required**: Yes

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreFromSnapshotRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### adminPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### manageAdminPassword
- **Type**: typing.Optional[bool]

### ownerAccount
- **Type**: typing.Optional[str]

### snapshotArn
- **Type**: typing.Optional[str]

### snapshotName
- **Type**: typing.Optional[str]


# RestoreFromSnapshotResponseTypeDef

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.NamespaceTypeDef'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreTableFromRecoveryPointRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### newTableName
- **Type**: <class 'str'>
- **Required**: Yes

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceTableName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### activateCaseSensitiveIdentifier
- **Type**: typing.Optional[bool]

### sourceSchemaName
- **Type**: typing.Optional[str]

### targetDatabaseName
- **Type**: typing.Optional[str]

### targetSchemaName
- **Type**: typing.Optional[str]


# RestoreTableFromRecoveryPointResponseTypeDef

### tableRestoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.TableRestoreStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestoreTableFromSnapshotRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### newTableName
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceTableName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### activateCaseSensitiveIdentifier
- **Type**: typing.Optional[bool]

### sourceSchemaName
- **Type**: typing.Optional[str]

### targetDatabaseName
- **Type**: typing.Optional[str]

### targetSchemaName
- **Type**: typing.Optional[str]


# RestoreTableFromSnapshotResponseTypeDef

### tableRestoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.TableRestoreStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ScheduleOutputTypeDef

### at
- **Type**: typing.Optional[datetime.datetime]

### cron
- **Type**: typing.Optional[str]


# ScheduleTypeDef

### at
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### cron
- **Type**: typing.Optional[str]


# ScheduleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduledActionAssociationTypeDef

### namespaceName
- **Type**: typing.Optional[str]

### scheduledActionName
- **Type**: typing.Optional[str]


# ScheduledActionResponseTypeDef

### endTime
- **Type**: typing.Optional[datetime.datetime]

### namespaceName
- **Type**: typing.Optional[str]

### nextInvocations
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### roleArn
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduleOutputTypeDef]

### scheduledActionDescription
- **Type**: typing.Optional[str]

### scheduledActionName
- **Type**: typing.Optional[str]

### scheduledActionUuid
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DISABLED']]

### targetAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TargetActionOutputTypeDef]


# ServerlessTrackTypeDef

### trackName
- **Type**: typing.Optional[str]

### updateTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.UpdateTargetTypeDef]]

### workgroupVersion
- **Type**: typing.Optional[str]


# SnapshotCopyConfigurationTypeDef

### destinationKmsKeyId
- **Type**: typing.Optional[str]

### destinationRegion
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### snapshotCopyConfigurationArn
- **Type**: typing.Optional[str]

### snapshotCopyConfigurationId
- **Type**: typing.Optional[str]

### snapshotRetentionPeriod
- **Type**: typing.Optional[int]


# SnapshotTypeDef

### accountsWithProvisionedRestoreAccess
- **Type**: typing.Optional[typing.List[str]]

### accountsWithRestoreAccess
- **Type**: typing.Optional[typing.List[str]]

### actualIncrementalBackupSizeInMegaBytes
- **Type**: typing.Optional[float]

### adminPasswordSecretArn
- **Type**: typing.Optional[str]

### adminPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### adminUsername
- **Type**: typing.Optional[str]

### backupProgressInMegaBytes
- **Type**: typing.Optional[float]

### currentBackupRateInMegaBytesPerSecond
- **Type**: typing.Optional[float]

### elapsedTimeInSeconds
- **Type**: typing.Optional[int]

### estimatedSecondsToCompletion
- **Type**: typing.Optional[int]

### kmsKeyId
- **Type**: typing.Optional[str]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]

### snapshotArn
- **Type**: typing.Optional[str]

### snapshotCreateTime
- **Type**: typing.Optional[datetime.datetime]

### snapshotName
- **Type**: typing.Optional[str]

### snapshotRemainingDays
- **Type**: typing.Optional[int]

### snapshotRetentionPeriod
- **Type**: typing.Optional[int]

### snapshotRetentionStartTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CANCELLED', 'COPYING', 'CREATING', 'DELETED', 'FAILED']]

### totalBackupSizeInMegaBytes
- **Type**: typing.Optional[float]


# TableRestoreStatusTypeDef

### message
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### newTableName
- **Type**: typing.Optional[str]

### progressInMegaBytes
- **Type**: typing.Optional[int]

### recoveryPointId
- **Type**: typing.Optional[str]

### requestTime
- **Type**: typing.Optional[datetime.datetime]

### snapshotName
- **Type**: typing.Optional[str]

### sourceDatabaseName
- **Type**: typing.Optional[str]

### sourceSchemaName
- **Type**: typing.Optional[str]

### sourceTableName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### tableRestoreRequestId
- **Type**: typing.Optional[str]

### targetDatabaseName
- **Type**: typing.Optional[str]

### targetSchemaName
- **Type**: typing.Optional[str]

### totalDataInMegaBytes
- **Type**: typing.Optional[int]

### workgroupName
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetActionOutputTypeDef

### createSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.CreateSnapshotScheduleActionParametersOutputTypeDef]


# TargetActionTypeDef

### createSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.CreateSnapshotScheduleActionParametersTypeDef]


# TargetActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCustomDomainAssociationRequestTypeDef

### customDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCustomDomainAssociationResponseTypeDef

### customDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainCertificateExpiryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEndpointAccessRequestTypeDef

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateEndpointAccessResponseTypeDef

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.EndpointAccessTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNamespaceRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### adminPasswordSecretKmsKeyId
- **Type**: typing.Optional[str]

### adminUserPassword
- **Type**: typing.Optional[str]

### adminUsername
- **Type**: typing.Optional[str]

### defaultIamRoleArn
- **Type**: typing.Optional[str]

### iamRoles
- **Type**: typing.Optional[typing.Sequence[str]]

### kmsKeyId
- **Type**: typing.Optional[str]

### logExports
- **Type**: typing.Optional[typing.Sequence[typing.Literal['connectionlog', 'useractivitylog', 'userlog']]]

### manageAdminPassword
- **Type**: typing.Optional[bool]


# UpdateNamespaceResponseTypeDef

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.NamespaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScheduledActionRequestTypeDef

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### roleArn
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduleUnionTypeDef]

### scheduledActionDescription
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TimestampTypeDef]

### targetAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TargetActionUnionTypeDef]


# UpdateScheduledActionResponseTypeDef

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduledActionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSnapshotCopyConfigurationRequestTypeDef

### snapshotCopyConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotRetentionPeriod
- **Type**: typing.Optional[int]


# UpdateSnapshotCopyConfigurationResponseTypeDef

### snapshotCopyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotCopyConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSnapshotRequestTypeDef

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]


# UpdateSnapshotResponseTypeDef

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTargetTypeDef

### trackName
- **Type**: typing.Optional[str]

### workgroupVersion
- **Type**: typing.Optional[str]


# UpdateUsageLimitRequestTypeDef

### usageLimitId
- **Type**: <class 'str'>
- **Required**: Yes

### amount
- **Type**: typing.Optional[int]

### breachAction
- **Type**: typing.Optional[typing.Literal['deactivate', 'emit-metric', 'log']]


# UpdateUsageLimitResponseTypeDef

### usageLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.UsageLimitTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkgroupRequestTypeDef

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: typing.Optional[int]

### configParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.ConfigParameterTypeDef]]

### enhancedVpcRouting
- **Type**: typing.Optional[bool]

### ipAddressType
- **Type**: typing.Optional[str]

### maxCapacity
- **Type**: typing.Optional[int]

### port
- **Type**: typing.Optional[int]

### pricePerformanceTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PerformanceTargetTypeDef]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### trackName
- **Type**: typing.Optional[str]


# UpdateWorkgroupResponseTypeDef

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.WorkgroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageLimitTypeDef

### amount
- **Type**: typing.Optional[int]

### breachAction
- **Type**: typing.Optional[typing.Literal['deactivate', 'emit-metric', 'log']]

### period
- **Type**: typing.Optional[typing.Literal['daily', 'monthly', 'weekly']]

### resourceArn
- **Type**: typing.Optional[str]

### usageLimitArn
- **Type**: typing.Optional[str]

### usageLimitId
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['cross-region-datasharing', 'serverless-compute']]


# VpcEndpointTypeDef

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.NetworkInterfaceTypeDef]]

### vpcEndpointId
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]


# VpcSecurityGroupMembershipTypeDef

### status
- **Type**: typing.Optional[str]

### vpcSecurityGroupId
- **Type**: typing.Optional[str]


# WorkgroupTypeDef

### baseCapacity
- **Type**: typing.Optional[int]

### configParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.ConfigParameterTypeDef]]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### crossAccountVpcs
- **Type**: typing.Optional[typing.List[str]]

### customDomainCertificateArn
- **Type**: typing.Optional[str]

### customDomainCertificateExpiryTime
- **Type**: typing.Optional[datetime.datetime]

### customDomainName
- **Type**: typing.Optional[str]

### endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.EndpointTypeDef]

### enhancedVpcRouting
- **Type**: typing.Optional[bool]

### ipAddressType
- **Type**: typing.Optional[str]

### maxCapacity
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### patchVersion
- **Type**: typing.Optional[str]

### pendingTrackName
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### pricePerformanceTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PerformanceTargetTypeDef]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'MODIFYING']]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### trackName
- **Type**: typing.Optional[str]

### workgroupArn
- **Type**: typing.Optional[str]

### workgroupId
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### workgroupVersion
- **Type**: typing.Optional[str]


