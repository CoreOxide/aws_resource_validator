# Redshift Serverless Classes

# Association

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

# ConfigParameter

### parameterKey
- **Type**: typing.Optional[str]

### parameterValue
- **Type**: typing.Optional[str]


# ConvertRecoveryPointToSnapshotRequest

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Tag]]


# ConvertRecoveryPointToSnapshotResponse

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomDomainAssociationRequest

### customDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCustomDomainAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEndpointAccessRequest

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ownerAccount
- **Type**: typing.Optional[str]

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# CreateEndpointAccessResponse

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.EndpointAccess'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNamespaceRequest

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
- **Type**: typing.Optional[typing.List[str]]

### kmsKeyId
- **Type**: typing.Optional[str]

### logExports
- **Type**: typing.Optional[typing.List[typing.Literal['connectionlog', 'useractivitylog', 'userlog']]]

### manageAdminPassword
- **Type**: typing.Optional[bool]

### redshiftIdcApplicationArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Tag]]


# CreateNamespaceResponse

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Namespace'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScheduledActionRequest

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### schedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Schedule, aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ScheduleOutput]
- **Required**: Yes

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes

### targetAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TargetAction, aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TargetActionOutput]
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### scheduledActionDescription
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CreateScheduledActionResponse

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ScheduledActionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotCopyConfigurationRequest

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


# CreateSnapshotCopyConfigurationResponse

### snapshotCopyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.SnapshotCopyConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotRequest

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Tag]]


# CreateSnapshotResponse

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotScheduleActionParameters

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotNamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Tag]]


# CreateSnapshotScheduleActionParametersOutput

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotNamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Tag]]


# CreateUsageLimitRequest

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


# CreateUsageLimitResponse

### usageLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.UsageLimit'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkgroupRequest

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: typing.Optional[int]

### configParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ConfigParameter]]

### enhancedVpcRouting
- **Type**: typing.Optional[bool]

### ipAddressType
- **Type**: typing.Optional[str]

### maxCapacity
- **Type**: typing.Optional[int]

### port
- **Type**: typing.Optional[int]

### pricePerformanceTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PerformanceTarget]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Tag]]

### trackName
- **Type**: typing.Optional[str]


# CreateWorkgroupResponse

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Workgroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCustomDomainAssociationRequest

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointAccessRequest

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointAccessResponse

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.EndpointAccess'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNamespaceRequest

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### finalSnapshotName
- **Type**: typing.Optional[str]

### finalSnapshotRetentionPeriod
- **Type**: typing.Optional[int]


# DeleteNamespaceResponse

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Namespace'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledActionRequest

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteScheduledActionResponse

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ScheduledActionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSnapshotCopyConfigurationRequest

### snapshotCopyConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotCopyConfigurationResponse

### snapshotCopyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.SnapshotCopyConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSnapshotRequest

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotResponse

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUsageLimitRequest

### usageLimitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUsageLimitResponse

### usageLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.UsageLimit'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkgroupRequest

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkgroupResponse

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Workgroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### address
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### vpcEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.VpcEndpoint]]


# EndpointAccess

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.VpcEndpoint]

### vpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.VpcSecurityGroupMembership]]

### workgroupName
- **Type**: typing.Optional[str]


# GetCredentialsRequest

### customDomainName
- **Type**: typing.Optional[str]

### dbName
- **Type**: typing.Optional[str]

### durationSeconds
- **Type**: typing.Optional[int]

### workgroupName
- **Type**: typing.Optional[str]


# GetCredentialsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetCustomDomainAssociationRequest

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomDomainAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetEndpointAccessRequest

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEndpointAccessResponse

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.EndpointAccess'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetNamespaceRequest

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetNamespaceResponse

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Namespace'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecoveryPointRequest

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecoveryPointResponse

### recoveryPoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.RecoveryPoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### resourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetScheduledActionRequest

### scheduledActionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetScheduledActionResponse

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ScheduledActionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetSnapshotRequest

### ownerAccount
- **Type**: typing.Optional[str]

### snapshotArn
- **Type**: typing.Optional[str]

### snapshotName
- **Type**: typing.Optional[str]


# GetSnapshotResponse

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetTableRestoreStatusRequest

### tableRestoreRequestId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTableRestoreStatusResponse

### tableRestoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TableRestoreStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrackRequest

### trackName
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrackResponse

### track
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ServerlessTrack'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetUsageLimitRequest

### usageLimitId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsageLimitResponse

### usageLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.UsageLimit'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkgroupRequest

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkgroupResponse

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Workgroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# ListCustomDomainAssociationsRequest

### customDomainCertificateArn
- **Type**: typing.Optional[str]

### customDomainName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomDomainAssociationsRequestPaginate

### customDomainCertificateArn
- **Type**: typing.Optional[str]

### customDomainName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListCustomDomainAssociationsResponse

### associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Association]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEndpointAccessRequest

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


# ListEndpointAccessRequestPaginate

### ownerAccount
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListEndpointAccessResponse

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.EndpointAccess]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedWorkgroupsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sourceArn
- **Type**: typing.Optional[str]


# ListManagedWorkgroupsRequestPaginate

### sourceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListManagedWorkgroupsResponse

### managedWorkgroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ManagedWorkgroupListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNamespacesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNamespacesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListNamespacesResponse

### namespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Namespace]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecoveryPointsRequest

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


# ListRecoveryPointsRequestPaginate

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### namespaceArn
- **Type**: typing.Optional[str]

### namespaceName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListRecoveryPointsResponse

### recoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.RecoveryPoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsRequest

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListScheduledActionsRequestPaginate

### namespaceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListScheduledActionsResponse

### scheduledActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ScheduledActionAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSnapshotCopyConfigurationsRequest

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListSnapshotCopyConfigurationsRequestPaginate

### namespaceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListSnapshotCopyConfigurationsResponse

### snapshotCopyConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.SnapshotCopyConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSnapshotsRequest

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


# ListSnapshotsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListSnapshotsResponse

### snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Snapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTableRestoreStatusRequest

### maxResults
- **Type**: typing.Optional[int]

### namespaceName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]


# ListTableRestoreStatusRequestPaginate

### namespaceName
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListTableRestoreStatusResponse

### tableRestoreStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TableRestoreStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# ListTracksRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTracksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListTracksResponse

### tracks
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ServerlessTrack]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUsageLimitsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['cross-region-datasharing', 'serverless-compute']]


# ListUsageLimitsRequestPaginate

### resourceArn
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['cross-region-datasharing', 'serverless-compute']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListUsageLimitsResponse

### usageLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.UsageLimit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkgroupsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### ownerAccount
- **Type**: typing.Optional[str]


# ListWorkgroupsRequestPaginate

### ownerAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PaginatorConfig]


# ListWorkgroupsResponse

### workgroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Workgroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ManagedWorkgroupListItem

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


# Namespace

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


# NetworkInterface

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceTarget

### level
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# PutResourcePolicyRequest

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyResponse

### resourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# RecoveryPoint

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


# ResourcePolicy

### policy
- **Type**: typing.Optional[str]

### resourceArn
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


# RestoreFromRecoveryPointRequest

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreFromRecoveryPointResponse

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Namespace'>
- **Required**: Yes

### recoveryPointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreFromSnapshotRequest

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


# RestoreFromSnapshotResponse

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Namespace'>
- **Required**: Yes

### ownerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreTableFromRecoveryPointRequest

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


# RestoreTableFromRecoveryPointResponse

### tableRestoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TableRestoreStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# RestoreTableFromSnapshotRequest

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


# RestoreTableFromSnapshotResponse

### tableRestoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TableRestoreStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# Schedule

### at
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### cron
- **Type**: typing.Optional[str]


# ScheduleOutput

### at
- **Type**: typing.Optional[datetime.datetime]

### cron
- **Type**: typing.Optional[str]


# ScheduledActionAssociation

### namespaceName
- **Type**: typing.Optional[str]

### scheduledActionName
- **Type**: typing.Optional[str]


# ScheduledActionResponse

### endTime
- **Type**: typing.Optional[datetime.datetime]

### namespaceName
- **Type**: typing.Optional[str]

### nextInvocations
- **Type**: typing.Optional[typing.List[datetime.datetime]]

### roleArn
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ScheduleOutput]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TargetActionOutput]


# ServerlessTrack

### trackName
- **Type**: typing.Optional[str]

### updateTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.UpdateTarget]]

### workgroupVersion
- **Type**: typing.Optional[str]


# Snapshot

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


# SnapshotCopyConfiguration

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


# TableRestoreStatus

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


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Tag]
- **Required**: Yes


# TargetAction

### createSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.CreateSnapshotScheduleActionParameters]


# TargetActionOutput

### createSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.CreateSnapshotScheduleActionParametersOutput]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCustomDomainAssociationRequest

### customDomainCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### customDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCustomDomainAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEndpointAccessRequest

### endpointName
- **Type**: <class 'str'>
- **Required**: Yes

### vpcSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# UpdateEndpointAccessResponse

### endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.EndpointAccess'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNamespaceRequest

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
- **Type**: typing.Optional[typing.List[str]]

### kmsKeyId
- **Type**: typing.Optional[str]

### logExports
- **Type**: typing.Optional[typing.List[typing.Literal['connectionlog', 'useractivitylog', 'userlog']]]

### manageAdminPassword
- **Type**: typing.Optional[bool]


# UpdateNamespaceResponse

### namespace
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Namespace'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScheduledActionRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Schedule, aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ScheduleOutput, NoneType]

### scheduledActionDescription
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### targetAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TargetAction, aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.TargetActionOutput, NoneType]


# UpdateScheduledActionResponse

### scheduledAction
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ScheduledActionResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSnapshotCopyConfigurationRequest

### snapshotCopyConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotRetentionPeriod
- **Type**: typing.Optional[int]


# UpdateSnapshotCopyConfigurationResponse

### snapshotCopyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.SnapshotCopyConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSnapshotRequest

### snapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionPeriod
- **Type**: typing.Optional[int]


# UpdateSnapshotResponse

### snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTarget

### trackName
- **Type**: typing.Optional[str]

### workgroupVersion
- **Type**: typing.Optional[str]


# UpdateUsageLimitRequest

### usageLimitId
- **Type**: <class 'str'>
- **Required**: Yes

### amount
- **Type**: typing.Optional[int]

### breachAction
- **Type**: typing.Optional[typing.Literal['deactivate', 'emit-metric', 'log']]


# UpdateUsageLimitResponse

### usageLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.UsageLimit'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkgroupRequest

### workgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### baseCapacity
- **Type**: typing.Optional[int]

### configParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ConfigParameter]]

### enhancedVpcRouting
- **Type**: typing.Optional[bool]

### ipAddressType
- **Type**: typing.Optional[str]

### maxCapacity
- **Type**: typing.Optional[int]

### port
- **Type**: typing.Optional[int]

### pricePerformanceTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PerformanceTarget]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### trackName
- **Type**: typing.Optional[str]


# UpdateWorkgroupResponse

### workgroup
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Workgroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# UsageLimit

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


# VpcEndpoint

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.NetworkInterface]]

### vpcEndpointId
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]


# VpcSecurityGroupMembership

### status
- **Type**: typing.Optional[str]

### vpcSecurityGroupId
- **Type**: typing.Optional[str]


# Workgroup

### baseCapacity
- **Type**: typing.Optional[int]

### configParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.ConfigParameter]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.Endpoint]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_serverless.redshift_serverless_classes.PerformanceTarget]

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


