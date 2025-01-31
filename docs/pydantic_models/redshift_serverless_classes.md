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


# ConvertRecoveryPointToSnapshotRequestRequestTypeDef

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


# CreateCustomDomainAssociationRequestRequestTypeDef

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


# CreateEndpointAccessRequestRequestTypeDef

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


# CreateNamespaceRequestRequestTypeDef

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


# CreateScheduledActionRequestRequestTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduleTypeDef'>
- **Required**: Yes

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### targetAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.TargetActionTypeDef'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### scheduledActionDescription
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CreateScheduledActionResponseTypeDef

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduledActionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotCopyConfigurationRequestRequestTypeDef

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


# CreateSnapshotRequestRequestTypeDef

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


# CreateUsageLimitRequestRequestTypeDef

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


# CreateWorkgroupRequestRequestTypeDef

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

### maxCapacity
- **Type**: typing.Optional[int]

### port
- **Type**: typing.Optional[int]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.TagTypeDef]]


# CreateWorkgroupResponseTypeDef

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.WorkgroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomDomainAssociationRequestRequestTypeDef

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointAccessRequestRequestTypeDef

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


# DeleteNamespaceRequestRequestTypeDef

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


# DeleteResourcePolicyRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledActionRequestRequestTypeDef

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


# DeleteSnapshotCopyConfigurationRequestRequestTypeDef

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


# DeleteSnapshotRequestRequestTypeDef

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


# DeleteUsageLimitRequestRequestTypeDef

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


# DeleteWorkgroupRequestRequestTypeDef

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


# GetCredentialsRequestRequestTypeDef

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


# GetCustomDomainAssociationRequestRequestTypeDef

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


# GetEndpointAccessRequestRequestTypeDef

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


# GetNamespaceRequestRequestTypeDef

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


# GetRecoveryPointRequestRequestTypeDef

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


# GetResourcePolicyRequestRequestTypeDef

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


# GetScheduledActionRequestRequestTypeDef

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


# GetSnapshotRequestRequestTypeDef

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


# GetTableRestoreStatusRequestRequestTypeDef

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


# GetUsageLimitRequestRequestTypeDef

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


# GetWorkgroupRequestRequestTypeDef

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


# ListCustomDomainAssociationsRequestListCustomDomainAssociationsPaginateTypeDef

### customDomainCertificateArn
- **Type**: typing.Optional[str]

### customDomainName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListCustomDomainAssociationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEndpointAccessRequestListEndpointAccessPaginateTypeDef

### ownerAccount
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListEndpointAccessRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNamespacesRequestListNamespacesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListNamespacesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNamespacesResponseTypeDef

### namespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.NamespaceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecoveryPointsRequestListRecoveryPointsPaginateTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListRecoveryPointsRequestRequestTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListRecoveryPointsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### recoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.RecoveryPointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListScheduledActionsRequestListScheduledActionsPaginateTypeDef

### namespaceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListScheduledActionsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### scheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduledActionAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSnapshotCopyConfigurationsRequestListSnapshotCopyConfigurationsPaginateTypeDef

### namespaceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListSnapshotCopyConfigurationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListSnapshotCopyConfigurationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotCopyConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotCopyConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSnapshotsRequestListSnapshotsPaginateTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListSnapshotsRequestRequestTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# ListSnapshotsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTableRestoreStatusRequestListTableRestoreStatusPaginateTypeDef

### namespaceName
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListTableRestoreStatusRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]


# ListTableRestoreStatusResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### tableRestoreStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.TableRestoreStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListUsageLimitsRequestListUsageLimitsPaginateTypeDef

### resourceArn
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['cross-region-datasharing', 'serverless-compute']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListUsageLimitsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['cross-region-datasharing', 'serverless-compute']]


# ListUsageLimitsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### usageLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.UsageLimitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkgroupsRequestListWorkgroupsPaginateTypeDef

### ownerAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.PaginatorConfigTypeDef]


# ListWorkgroupsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]


# ListWorkgroupsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workgroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless_classes.WorkgroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# PutResourcePolicyRequestRequestTypeDef

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


# RestoreFromRecoveryPointRequestRequestTypeDef

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


# RestoreFromSnapshotRequestRequestTypeDef

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


# RestoreTableFromRecoveryPointRequestRequestTypeDef

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


# RestoreTableFromSnapshotRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### cron
- **Type**: typing.Optional[str]


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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCustomDomainAssociationRequestRequestTypeDef

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


# UpdateEndpointAccessRequestRequestTypeDef

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


# UpdateNamespaceRequestRequestTypeDef

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


# UpdateScheduledActionRequestRequestTypeDef

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### roleArn
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduleTypeDef]

### scheduledActionDescription
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### targetAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless_classes.TargetActionTypeDef]


# UpdateScheduledActionResponseTypeDef

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ScheduledActionResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSnapshotCopyConfigurationRequestRequestTypeDef

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


# UpdateSnapshotRequestRequestTypeDef

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


# UpdateUsageLimitRequestRequestTypeDef

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


# UpdateWorkgroupRequestRequestTypeDef

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: typing.Optional[int]

### configParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_serverless_classes.ConfigParameterTypeDef]]

### enhancedVpcRouting
- **Type**: typing.Optional[bool]

### maxCapacity
- **Type**: typing.Optional[int]

### port
- **Type**: typing.Optional[int]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]


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

### maxCapacity
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### patchVersion
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'MODIFYING']]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### workgroupArn
- **Type**: typing.Optional[str]

### workgroupId
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### workgroupVersion
- **Type**: typing.Optional[str]


