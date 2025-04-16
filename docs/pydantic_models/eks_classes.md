# Eks Classes

# AccessConfigResponse

### bootstrapClusterCreatorAdminPermissions
- **Type**: typing.Optional[bool]

### authenticationMode
- **Type**: typing.Optional[typing.Literal['API', 'API_AND_CONFIG_MAP', 'CONFIG_MAP']]


# AccessEntry

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessPolicy

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# AccessScopeOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessScopeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Addon

### addonName
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DEGRADED', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### addonVersion
- **Type**: typing.Optional[str]

### health
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.AddonHealth]

### addonArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### serviceAccountRoleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### publisher
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]

### marketplaceInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.MarketplaceInformation]

### configurationValues
- **Type**: typing.Optional[str]

### podIdentityAssociations
- **Type**: typing.Optional[typing.List[str]]


# AddonCompatibilityDetail

### name
- **Type**: typing.Optional[str]

### compatibleVersions
- **Type**: typing.Optional[typing.List[str]]


# AddonHealth

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonIssue]]


# AddonInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddonIssue

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AddonPermissionFailure', 'AddonSubscriptionNeeded', 'AdmissionRequestDenied', 'ClusterUnreachable', 'ConfigurationConflict', 'InsufficientNumberOfReplicas', 'InternalFailure', 'K8sResourceNotFound', 'UnsupportedAddonModification']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# AddonPodIdentityAssociations

### serviceAccount
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AddonPodIdentityConfiguration

### serviceAccount
- **Type**: typing.Optional[str]

### recommendedManagedPolicies
- **Type**: typing.Optional[typing.List[str]]


# AddonVersionInfo

### addonVersion
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[typing.List[str]]

### computeTypes
- **Type**: typing.Optional[typing.List[str]]

### compatibilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.Compatibility]]

### requiresConfiguration
- **Type**: typing.Optional[bool]

### requiresIamPermissions
- **Type**: typing.Optional[bool]


# AssociateAccessPolicyRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes

### accessScope
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessScopeUnion'>
- **Required**: Yes


# AssociateAccessPolicyResponse

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedAccessPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AssociatedAccessPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateEncryptionConfigRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigUnion]
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# AssociateEncryptionConfigResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateIdentityProviderConfigRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### oidc
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.OidcIdentityProviderConfigRequest'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientRequestToken
- **Type**: typing.Optional[str]


# AssociateIdentityProviderConfigResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatedAccessPolicy

### policyArn
- **Type**: typing.Optional[str]

### accessScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.AccessScopeOutput]

### associatedAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


# AutoScalingGroup

### name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockStorage

### enabled
- **Type**: typing.Optional[bool]


# Certificate

### data
- **Type**: typing.Optional[str]


# ClientStat

### userAgent
- **Type**: typing.Optional[str]

### numberOfRequestsLast30Days
- **Type**: typing.Optional[int]

### lastRequestTime
- **Type**: typing.Optional[datetime.datetime]


# Cluster

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClusterHealth

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.ClusterIssue]]


# ClusterIssue

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'ClusterUnreachable', 'ConfigurationConflict', 'Ec2SecurityGroupNotFound', 'Ec2ServiceNotSubscribed', 'Ec2SubnetNotFound', 'IamRoleNotFound', 'InsufficientFreeAddresses', 'InternalFailure', 'KmsGrantRevoked', 'KmsKeyDisabled', 'KmsKeyMarkedForDeletion', 'KmsKeyNotFound', 'Other', 'ResourceLimitExceeded', 'ResourceNotFound', 'StsRegionalEndpointDisabled', 'UnsupportedVersion', 'VpcNotFound']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# ClusterVersionInformation

### clusterVersion
- **Type**: typing.Optional[str]

### clusterType
- **Type**: typing.Optional[str]

### defaultPlatformVersion
- **Type**: typing.Optional[str]

### defaultVersion
- **Type**: typing.Optional[bool]

### releaseDate
- **Type**: typing.Optional[datetime.datetime]

### endOfStandardSupportDate
- **Type**: typing.Optional[datetime.datetime]

### endOfExtendedSupportDate
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['extended-support', 'standard-support', 'unsupported']]

### versionStatus
- **Type**: typing.Optional[typing.Literal['EXTENDED_SUPPORT', 'STANDARD_SUPPORT', 'UNSUPPORTED']]

### kubernetesPatchVersion
- **Type**: typing.Optional[str]


# Compatibility

### clusterVersion
- **Type**: typing.Optional[str]

### platformVersions
- **Type**: typing.Optional[typing.List[str]]

### defaultVersion
- **Type**: typing.Optional[bool]


# ComputeConfigRequest

### enabled
- **Type**: typing.Optional[bool]

### nodePools
- **Type**: typing.Optional[typing.Sequence[str]]

### nodeRoleArn
- **Type**: typing.Optional[str]


# ComputeConfigResponse

### enabled
- **Type**: typing.Optional[bool]

### nodePools
- **Type**: typing.Optional[typing.List[str]]

### nodeRoleArn
- **Type**: typing.Optional[str]


# ConnectorConfigRequest

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['AKS', 'ANTHOS', 'EC2', 'EKS_ANYWHERE', 'GKE', 'OPENSHIFT', 'OTHER', 'RANCHER', 'TANZU']
- **Required**: Yes


# ConnectorConfigResponse

### activationId
- **Type**: typing.Optional[str]

### activationCode
- **Type**: typing.Optional[str]

### activationExpiry
- **Type**: typing.Optional[datetime.datetime]

### provider
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# ControlPlanePlacementRequest

### groupName
- **Type**: typing.Optional[str]


# ControlPlanePlacementResponse

### groupName
- **Type**: typing.Optional[str]


# CreateAccessConfigRequest

### bootstrapClusterCreatorAdminPermissions
- **Type**: typing.Optional[bool]

### authenticationMode
- **Type**: typing.Optional[typing.Literal['API', 'API_AND_CONFIG_MAP', 'CONFIG_MAP']]


# CreateAccessEntryResponse

### accessEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessEntry'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAddonRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### addonVersion
- **Type**: typing.Optional[str]

### serviceAccountRoleArn
- **Type**: typing.Optional[str]

### resolveConflicts
- **Type**: typing.Optional[typing.Literal['NONE', 'OVERWRITE', 'PRESERVE']]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### configurationValues
- **Type**: typing.Optional[str]

### podIdentityAssociations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.AddonPodIdentityAssociations]]


# CreateAddonResponse

### addon
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Addon'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourcesVpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.VpcConfigRequest'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]

### kubernetesNetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.KubernetesNetworkConfigRequest]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LoggingUnion]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### encryptionConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigUnion]]

### outpostConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OutpostConfigRequest]

### accessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.CreateAccessConfigRequest]

### bootstrapSelfManagedAddons
- **Type**: typing.Optional[bool]

### upgradePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpgradePolicyRequest]

### zonalShiftConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ZonalShiftConfigRequest]

### remoteNetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.RemoteNetworkConfigRequest]

### computeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ComputeConfigRequest]

### storageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.StorageConfigRequest]


# CreateClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEksAnywhereSubscriptionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### term
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTerm'>
- **Required**: Yes

### licenseQuantity
- **Type**: typing.Optional[int]

### licenseType
- **Type**: typing.Optional[typing.Literal['Cluster']]

### autoRenew
- **Type**: typing.Optional[bool]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEksAnywhereSubscriptionResponse

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFargateProfileRequest

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### podExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### selectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.FargateProfileSelectorUnion]]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFargateProfileResponse

### fargateProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.FargateProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNodegroupRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### nodeRole
- **Type**: <class 'str'>
- **Required**: Yes

### scalingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupScalingConfig]

### diskSize
- **Type**: typing.Optional[int]

### instanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### amiType
- **Type**: typing.Optional[typing.Literal['AL2023_ARM_64_STANDARD', 'AL2023_x86_64_NEURON', 'AL2023_x86_64_NVIDIA', 'AL2023_x86_64_STANDARD', 'AL2_ARM_64', 'AL2_x86_64', 'AL2_x86_64_GPU', 'BOTTLEROCKET_ARM_64', 'BOTTLEROCKET_ARM_64_NVIDIA', 'BOTTLEROCKET_x86_64', 'BOTTLEROCKET_x86_64_NVIDIA', 'CUSTOM', 'WINDOWS_CORE_2019_x86_64', 'WINDOWS_CORE_2022_x86_64', 'WINDOWS_FULL_2019_x86_64', 'WINDOWS_FULL_2022_x86_64']]

### remoteAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.RemoteAccessConfigUnion]

### labels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### taints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.Taint]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientRequestToken
- **Type**: typing.Optional[str]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LaunchTemplateSpecification]

### updateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupUpdateConfig]

### nodeRepairConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodeRepairConfig]

### capacityType
- **Type**: typing.Optional[typing.Literal['CAPACITY_BLOCK', 'ON_DEMAND', 'SPOT']]

### version
- **Type**: typing.Optional[str]

### releaseVersion
- **Type**: typing.Optional[str]


# CreateNodegroupResponse

### nodegroup
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Nodegroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePodIdentityAssociationRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### serviceAccount
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePodIdentityAssociationResponse

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAccessEntryRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAddonRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### preserve
- **Type**: typing.Optional[bool]


# DeleteAddonResponse

### addon
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Addon'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEksAnywhereSubscriptionResponse

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFargateProfileRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFargateProfileResponse

### fargateProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.FargateProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNodegroupRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNodegroupResponse

### nodegroup
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Nodegroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePodIdentityAssociationRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePodIdentityAssociationResponse

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DeprecationDetail

### usage
- **Type**: typing.Optional[str]

### replacedWith
- **Type**: typing.Optional[str]

### stopServingVersion
- **Type**: typing.Optional[str]

### startServingReplacementVersion
- **Type**: typing.Optional[str]

### clientStats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.ClientStat]]


# DeregisterClusterRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccessEntryRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessEntryResponse

### accessEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessEntry'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAddonConfigurationRequest

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### addonVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAddonConfigurationResponse

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### addonVersion
- **Type**: <class 'str'>
- **Required**: Yes

### configurationSchema
- **Type**: <class 'str'>
- **Required**: Yes

### podIdentityConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonPodIdentityConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAddonRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAddonRequestWait

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeAddonRequestWaitExtra

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeAddonResponse

### addon
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Addon'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAddonVersionsResponse

### addons
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeClusterRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequestWait

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterRequestWaitExtra

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterVersionsRequest

### clusterType
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### defaultOnly
- **Type**: typing.Optional[bool]

### includeAll
- **Type**: typing.Optional[bool]

### clusterVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### status
- **Type**: typing.Optional[typing.Literal['extended-support', 'standard-support', 'unsupported']]

### versionStatus
- **Type**: typing.Optional[typing.Literal['EXTENDED_SUPPORT', 'STANDARD_SUPPORT', 'UNSUPPORTED']]


# DescribeClusterVersionsRequestPaginate

### clusterType
- **Type**: typing.Optional[str]

### defaultOnly
- **Type**: typing.Optional[bool]

### includeAll
- **Type**: typing.Optional[bool]

### clusterVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### status
- **Type**: typing.Optional[typing.Literal['extended-support', 'standard-support', 'unsupported']]

### versionStatus
- **Type**: typing.Optional[typing.Literal['EXTENDED_SUPPORT', 'STANDARD_SUPPORT', 'UNSUPPORTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# DescribeClusterVersionsResponse

### clusterVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.ClusterVersionInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeEksAnywhereSubscriptionResponse

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFargateProfileRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFargateProfileRequestWait

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeFargateProfileRequestWaitExtra

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeFargateProfileResponse

### fargateProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.FargateProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIdentityProviderConfigRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.IdentityProviderConfig'>
- **Required**: Yes


# DescribeIdentityProviderConfigResponse

### identityProviderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.IdentityProviderConfigResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInsightResponse

### insight
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Insight'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNodegroupRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodegroupRequestWait

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeNodegroupRequestWaitExtra

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeNodegroupResponse

### nodegroup
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Nodegroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePodIdentityAssociationRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePodIdentityAssociationResponse

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUpdateRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updateId
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: typing.Optional[str]

### addonName
- **Type**: typing.Optional[str]


# DescribeUpdateResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateAccessPolicyRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateIdentityProviderConfigRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.IdentityProviderConfig'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# DisassociateIdentityProviderConfigResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# EksAnywhereSubscription

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EksAnywhereSubscriptionTerm

### duration
- **Type**: typing.Optional[int]

### unit
- **Type**: typing.Optional[typing.Literal['MONTHS']]


# ElasticLoadBalancing

### enabled
- **Type**: typing.Optional[bool]


# EncryptionConfig

### resources
- **Type**: typing.Optional[typing.Sequence[str]]

### provider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.Provider]


# EncryptionConfigOutput

### resources
- **Type**: typing.Optional[typing.List[str]]

### provider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.Provider]


# EncryptionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ErrorDetail

### errorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AdmissionRequestDenied', 'ClusterUnreachable', 'ConfigurationConflict', 'EniLimitReached', 'InsufficientFreeAddresses', 'InsufficientNumberOfReplicas', 'IpNotAvailable', 'K8sResourceNotFound', 'NodeCreationFailure', 'OperationNotPermitted', 'PodEvictionFailure', 'SecurityGroupNotFound', 'SubnetNotFound', 'Unknown', 'UnsupportedAddonModification', 'VpcIdNotFound']]

### errorMessage
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# FargateProfile

### fargateProfileName
- **Type**: typing.Optional[str]

### fargateProfileArn
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### podExecutionRoleArn
- **Type**: typing.Optional[str]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### selectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.FargateProfileSelectorOutput]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### health
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.FargateProfileHealth]


# FargateProfileHealth

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.FargateProfileIssue]]


# FargateProfileIssue

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'ClusterUnreachable', 'InternalFailure', 'PodExecutionRoleAlreadyInUse']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# FargateProfileSelector

### namespace
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FargateProfileSelectorOutput

### namespace
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Dict[str, str]]


# FargateProfileSelectorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Identity

### oidc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OIDC]


# IdentityProviderConfig

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdentityProviderConfigResponse

### oidc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OidcIdentityProviderConfig]


# Insight

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InsightCategorySpecificSummary

### deprecationDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.DeprecationDetail]]

### addonCompatibilityDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonCompatibilityDetail]]


# InsightResourceDetail

### insightStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.InsightStatus]

### kubernetesResourceUri
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# InsightStatus

### status
- **Type**: typing.Optional[typing.Literal['ERROR', 'PASSING', 'UNKNOWN', 'WARNING']]

### reason
- **Type**: typing.Optional[str]


# InsightSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InsightsFilter

### categories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['UPGRADE_READINESS']]]

### kubernetesVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ERROR', 'PASSING', 'UNKNOWN', 'WARNING']]]


# Issue

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AmiIdNotFound', 'AsgInstanceLaunchFailures', 'AutoScalingGroupInstanceRefreshActive', 'AutoScalingGroupInvalidConfiguration', 'AutoScalingGroupNotFound', 'AutoScalingGroupOptInRequired', 'AutoScalingGroupRateLimitExceeded', 'ClusterUnreachable', 'Ec2InstanceTypeDoesNotExist', 'Ec2LaunchTemplateDeletionFailure', 'Ec2LaunchTemplateInvalidConfiguration', 'Ec2LaunchTemplateMaxLimitExceeded', 'Ec2LaunchTemplateNotFound', 'Ec2LaunchTemplateVersionMaxLimitExceeded', 'Ec2LaunchTemplateVersionMismatch', 'Ec2SecurityGroupDeletionFailure', 'Ec2SecurityGroupNotFound', 'Ec2SubnetInvalidConfiguration', 'Ec2SubnetListTooLong', 'Ec2SubnetMissingIpv6Assignment', 'Ec2SubnetNotFound', 'IamInstanceProfileNotFound', 'IamLimitExceeded', 'IamNodeRoleNotFound', 'IamThrottling', 'InstanceLimitExceeded', 'InsufficientFreeAddresses', 'InternalFailure', 'KubernetesLabelInvalid', 'LimitExceeded', 'NodeCreationFailure', 'NodeTerminationFailure', 'PodEvictionFailure', 'SourceEc2LaunchTemplateNotFound', 'Unknown']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# KubernetesNetworkConfigRequest

### serviceIpv4Cidr
- **Type**: typing.Optional[str]

### ipFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### elasticLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ElasticLoadBalancing]


# KubernetesNetworkConfigResponse

### serviceIpv4Cidr
- **Type**: typing.Optional[str]

### serviceIpv6Cidr
- **Type**: typing.Optional[str]

### ipFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### elasticLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ElasticLoadBalancing]


# LaunchTemplateSpecification

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccessEntriesRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPolicyArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessEntriesRequestPaginate

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPolicyArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListAccessEntriesResponse

### accessEntries
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAccessPoliciesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessPoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListAccessPoliciesResponse

### accessPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AccessPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAddonsRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAddonsRequestPaginate

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListAddonsResponse

### addons
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedAccessPoliciesRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedAccessPoliciesRequestPaginate

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListAssociatedAccessPoliciesResponse

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedAccessPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AssociatedAccessPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListClustersRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[str]]


# ListClustersRequestPaginate

### include
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListClustersResponse

### clusters
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEksAnywhereSubscriptionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### includeStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'EXPIRED', 'EXPIRING', 'UPDATING']]]


# ListEksAnywhereSubscriptionsRequestPaginate

### includeStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'EXPIRED', 'EXPIRING', 'UPDATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListEksAnywhereSubscriptionsResponse

### subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFargateProfilesRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFargateProfilesRequestPaginate

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListFargateProfilesResponse

### fargateProfileNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdentityProviderConfigsRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdentityProviderConfigsRequestPaginate

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListIdentityProviderConfigsResponse

### identityProviderConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.IdentityProviderConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInsightsResponse

### insights
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.InsightSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNodegroupsRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNodegroupsRequestPaginate

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListNodegroupsResponse

### nodegroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPodIdentityAssociationsRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### serviceAccount
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPodIdentityAssociationsRequestPaginate

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### serviceAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListPodIdentityAssociationsResponse

### associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# ListUpdatesRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: typing.Optional[str]

### addonName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListUpdatesRequestPaginate

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: typing.Optional[str]

### addonName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfig]


# ListUpdatesResponse

### updateIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogSetup

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LogSetupOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Logging

### clusterLogging
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.LogSetup]]


# LoggingOutput

### clusterLogging
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.LogSetupOutput]]


# LoggingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MarketplaceInformation

### productId
- **Type**: typing.Optional[str]

### productUrl
- **Type**: typing.Optional[str]


# NodeRepairConfig

### enabled
- **Type**: typing.Optional[bool]


# Nodegroup

### nodegroupName
- **Type**: typing.Optional[str]

### nodegroupArn
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### releaseVersion
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DEGRADED', 'DELETE_FAILED', 'DELETING', 'UPDATING']]

### capacityType
- **Type**: typing.Optional[typing.Literal['CAPACITY_BLOCK', 'ON_DEMAND', 'SPOT']]

### scalingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupScalingConfig]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### remoteAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.RemoteAccessConfigOutput]

### amiType
- **Type**: typing.Optional[typing.Literal['AL2023_ARM_64_STANDARD', 'AL2023_x86_64_NEURON', 'AL2023_x86_64_NVIDIA', 'AL2023_x86_64_STANDARD', 'AL2_ARM_64', 'AL2_x86_64', 'AL2_x86_64_GPU', 'BOTTLEROCKET_ARM_64', 'BOTTLEROCKET_ARM_64_NVIDIA', 'BOTTLEROCKET_x86_64', 'BOTTLEROCKET_x86_64_NVIDIA', 'CUSTOM', 'WINDOWS_CORE_2019_x86_64', 'WINDOWS_CORE_2022_x86_64', 'WINDOWS_FULL_2019_x86_64', 'WINDOWS_FULL_2022_x86_64']]

### nodeRole
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Dict[str, str]]

### taints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.Taint]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupResources]

### diskSize
- **Type**: typing.Optional[int]

### health
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupHealth]

### updateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupUpdateConfig]

### nodeRepairConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodeRepairConfig]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LaunchTemplateSpecification]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# NodegroupHealth

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.Issue]]


# NodegroupResources

### autoScalingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.AutoScalingGroup]]

### remoteAccessSecurityGroup
- **Type**: typing.Optional[str]


# NodegroupScalingConfig

### minSize
- **Type**: typing.Optional[int]

### maxSize
- **Type**: typing.Optional[int]

### desiredSize
- **Type**: typing.Optional[int]


# NodegroupUpdateConfig

### maxUnavailable
- **Type**: typing.Optional[int]

### maxUnavailablePercentage
- **Type**: typing.Optional[int]

### updateStrategy
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'MINIMAL']]


# OIDC

### issuer
- **Type**: typing.Optional[str]


# OidcIdentityProviderConfig

### identityProviderConfigName
- **Type**: typing.Optional[str]

### identityProviderConfigArn
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]

### issuerUrl
- **Type**: typing.Optional[str]

### clientId
- **Type**: typing.Optional[str]

### usernameClaim
- **Type**: typing.Optional[str]

### usernamePrefix
- **Type**: typing.Optional[str]

### groupsClaim
- **Type**: typing.Optional[str]

### groupsPrefix
- **Type**: typing.Optional[str]

### requiredClaims
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING']]


# OidcIdentityProviderConfigRequest

### identityProviderConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### issuerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### usernameClaim
- **Type**: typing.Optional[str]

### usernamePrefix
- **Type**: typing.Optional[str]

### groupsClaim
- **Type**: typing.Optional[str]

### groupsPrefix
- **Type**: typing.Optional[str]

### requiredClaims
- **Type**: typing.Optional[typing.Mapping[str, str]]


# OutpostConfigRequest

### outpostArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### controlPlaneInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### controlPlanePlacement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ControlPlanePlacementRequest]


# OutpostConfigResponse

### outpostArns
- **Type**: typing.List[str]
- **Required**: Yes

### controlPlaneInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### controlPlanePlacement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ControlPlanePlacementResponse]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PodIdentityAssociation

### clusterName
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### serviceAccount
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### associationArn
- **Type**: typing.Optional[str]

### associationId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### ownerArn
- **Type**: typing.Optional[str]


# PodIdentityAssociationSummary

### clusterName
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### serviceAccount
- **Type**: typing.Optional[str]

### associationArn
- **Type**: typing.Optional[str]

### associationId
- **Type**: typing.Optional[str]

### ownerArn
- **Type**: typing.Optional[str]


# Provider

### keyArn
- **Type**: typing.Optional[str]


# RegisterClusterRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### connectorConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ConnectorConfigRequest'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# RemoteAccessConfig

### ec2SshKey
- **Type**: typing.Optional[str]

### sourceSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# RemoteAccessConfigOutput

### ec2SshKey
- **Type**: typing.Optional[str]

### sourceSecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# RemoteAccessConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemoteNetworkConfigRequest

### remoteNodeNetworks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.RemoteNodeNetworkUnion]]

### remotePodNetworks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.RemotePodNetworkUnion]]


# RemoteNetworkConfigResponse

### remoteNodeNetworks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.RemoteNodeNetworkOutput]]

### remotePodNetworks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.RemotePodNetworkOutput]]


# RemoteNodeNetwork

### cidrs
- **Type**: typing.Optional[typing.Sequence[str]]


# RemoteNodeNetworkOutput

### cidrs
- **Type**: typing.Optional[typing.List[str]]


# RemoteNodeNetworkUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemotePodNetwork

### cidrs
- **Type**: typing.Optional[typing.Sequence[str]]


# RemotePodNetworkOutput

### cidrs
- **Type**: typing.Optional[typing.List[str]]


# RemotePodNetworkUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# StorageConfigRequest

### blockStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.BlockStorage]


# StorageConfigResponse

### blockStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.BlockStorage]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Taint

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### effect
- **Type**: typing.Optional[typing.Literal['NO_EXECUTE', 'NO_SCHEDULE', 'PREFER_NO_SCHEDULE']]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# Update

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateAccessConfigRequest

### authenticationMode
- **Type**: typing.Optional[typing.Literal['API', 'API_AND_CONFIG_MAP', 'CONFIG_MAP']]


# UpdateAccessEntryRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### kubernetesGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### clientRequestToken
- **Type**: typing.Optional[str]

### username
- **Type**: typing.Optional[str]


# UpdateAccessEntryResponse

### accessEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessEntry'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAddonRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### addonVersion
- **Type**: typing.Optional[str]

### serviceAccountRoleArn
- **Type**: typing.Optional[str]

### resolveConflicts
- **Type**: typing.Optional[typing.Literal['NONE', 'OVERWRITE', 'PRESERVE']]

### clientRequestToken
- **Type**: typing.Optional[str]

### configurationValues
- **Type**: typing.Optional[str]

### podIdentityAssociations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.AddonPodIdentityAssociations]]


# UpdateAddonResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterConfigRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.VpcConfigRequest]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LoggingUnion]

### clientRequestToken
- **Type**: typing.Optional[str]

### accessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpdateAccessConfigRequest]

### upgradePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpgradePolicyRequest]

### zonalShiftConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ZonalShiftConfigRequest]

### computeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ComputeConfigRequest]

### kubernetesNetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.KubernetesNetworkConfigRequest]

### storageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.StorageConfigRequest]


# UpdateClusterConfigResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterVersionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateClusterVersionResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEksAnywhereSubscriptionResponse

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLabelsPayload

### addOrUpdateLabels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### removeLabels
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateNodegroupConfigRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### labels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpdateLabelsPayload]

### taints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpdateTaintsPayload]

### scalingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupScalingConfig]

### updateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupUpdateConfig]

### nodeRepairConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodeRepairConfig]

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateNodegroupConfigResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNodegroupVersionRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]

### releaseVersion
- **Type**: typing.Optional[str]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LaunchTemplateSpecification]

### force
- **Type**: typing.Optional[bool]

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateNodegroupVersionResponse

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.Update'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePodIdentityAssociationRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdatePodIdentityAssociationResponse

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTaintsPayload

### addOrUpdateTaints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.Taint]]

### removeTaints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.Taint]]


# UpgradePolicyRequest

### supportType
- **Type**: typing.Optional[typing.Literal['EXTENDED', 'STANDARD']]


# UpgradePolicyResponse

### supportType
- **Type**: typing.Optional[typing.Literal['EXTENDED', 'STANDARD']]


# VpcConfigRequest

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### endpointPublicAccess
- **Type**: typing.Optional[bool]

### endpointPrivateAccess
- **Type**: typing.Optional[bool]

### publicAccessCidrs
- **Type**: typing.Optional[typing.Sequence[str]]


# VpcConfigResponse

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### clusterSecurityGroupId
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]

### endpointPublicAccess
- **Type**: typing.Optional[bool]

### endpointPrivateAccess
- **Type**: typing.Optional[bool]

### publicAccessCidrs
- **Type**: typing.Optional[typing.List[str]]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# ZonalShiftConfigRequest

### enabled
- **Type**: typing.Optional[bool]


# ZonalShiftConfigResponse

### enabled
- **Type**: typing.Optional[bool]


