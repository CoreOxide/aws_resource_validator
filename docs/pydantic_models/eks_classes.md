# Eks Classes

# AccessConfigResponseTypeDef

### bootstrapClusterCreatorAdminPermissions
- **Type**: typing.Optional[bool]

### authenticationMode
- **Type**: typing.Optional[typing.Literal['API', 'API_AND_CONFIG_MAP', 'CONFIG_MAP']]


# AccessEntryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessPolicyTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# AccessScopeOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessScopeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddonCompatibilityDetailTypeDef

### name
- **Type**: typing.Optional[str]

### compatibleVersions
- **Type**: typing.Optional[typing.List[str]]


# AddonHealthTypeDef

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonIssueTypeDef]]


# AddonInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddonIssueTypeDef

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AddonPermissionFailure', 'AddonSubscriptionNeeded', 'AdmissionRequestDenied', 'ClusterUnreachable', 'ConfigurationConflict', 'InsufficientNumberOfReplicas', 'InternalFailure', 'K8sResourceNotFound', 'UnsupportedAddonModification']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# AddonPodIdentityAssociationsTypeDef

### serviceAccount
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AddonPodIdentityConfigurationTypeDef

### serviceAccount
- **Type**: typing.Optional[str]

### recommendedManagedPolicies
- **Type**: typing.Optional[typing.List[str]]


# AddonTypeDef

### addonName
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DEGRADED', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### addonVersion
- **Type**: typing.Optional[str]

### health
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.AddonHealthTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.MarketplaceInformationTypeDef]

### configurationValues
- **Type**: typing.Optional[str]

### podIdentityAssociations
- **Type**: typing.Optional[typing.List[str]]


# AddonVersionInfoTypeDef

### addonVersion
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[typing.List[str]]

### computeTypes
- **Type**: typing.Optional[typing.List[str]]

### compatibilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.CompatibilityTypeDef]]

### requiresConfiguration
- **Type**: typing.Optional[bool]

### requiresIamPermissions
- **Type**: typing.Optional[bool]


# AssociateAccessPolicyRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessScopeUnionTypeDef'>
- **Required**: Yes


# AssociateAccessPolicyResponseTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedAccessPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AssociatedAccessPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateEncryptionConfigRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigUnionTypeDef]
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# AssociateEncryptionConfigResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateIdentityProviderConfigRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### oidc
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.OidcIdentityProviderConfigRequestTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientRequestToken
- **Type**: typing.Optional[str]


# AssociateIdentityProviderConfigResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatedAccessPolicyTypeDef

### policyArn
- **Type**: typing.Optional[str]

### accessScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.AccessScopeOutputTypeDef]

### associatedAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


# AutoScalingGroupTypeDef

### name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockStorageTypeDef

### enabled
- **Type**: typing.Optional[bool]


# CertificateTypeDef

### data
- **Type**: typing.Optional[str]


# ClientStatTypeDef

### userAgent
- **Type**: typing.Optional[str]

### numberOfRequestsLast30Days
- **Type**: typing.Optional[int]

### lastRequestTime
- **Type**: typing.Optional[datetime.datetime]


# ClusterHealthTypeDef

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.ClusterIssueTypeDef]]


# ClusterIssueTypeDef

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'ClusterUnreachable', 'ConfigurationConflict', 'Ec2SecurityGroupNotFound', 'Ec2ServiceNotSubscribed', 'Ec2SubnetNotFound', 'IamRoleNotFound', 'InsufficientFreeAddresses', 'InternalFailure', 'KmsGrantRevoked', 'KmsKeyDisabled', 'KmsKeyMarkedForDeletion', 'KmsKeyNotFound', 'Other', 'ResourceLimitExceeded', 'ResourceNotFound', 'StsRegionalEndpointDisabled', 'UnsupportedVersion', 'VpcNotFound']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# ClusterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClusterVersionInformationTypeDef

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


# CompatibilityTypeDef

### clusterVersion
- **Type**: typing.Optional[str]

### platformVersions
- **Type**: typing.Optional[typing.List[str]]

### defaultVersion
- **Type**: typing.Optional[bool]


# ComputeConfigRequestTypeDef

### enabled
- **Type**: typing.Optional[bool]

### nodePools
- **Type**: typing.Optional[typing.Sequence[str]]

### nodeRoleArn
- **Type**: typing.Optional[str]


# ComputeConfigResponseTypeDef

### enabled
- **Type**: typing.Optional[bool]

### nodePools
- **Type**: typing.Optional[typing.List[str]]

### nodeRoleArn
- **Type**: typing.Optional[str]


# ConnectorConfigRequestTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: typing.Literal['AKS', 'ANTHOS', 'EC2', 'EKS_ANYWHERE', 'GKE', 'OPENSHIFT', 'OTHER', 'RANCHER', 'TANZU']
- **Required**: Yes


# ConnectorConfigResponseTypeDef

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


# ControlPlanePlacementRequestTypeDef

### groupName
- **Type**: typing.Optional[str]


# ControlPlanePlacementResponseTypeDef

### groupName
- **Type**: typing.Optional[str]


# CreateAccessConfigRequestTypeDef

### bootstrapClusterCreatorAdminPermissions
- **Type**: typing.Optional[bool]

### authenticationMode
- **Type**: typing.Optional[typing.Literal['API', 'API_AND_CONFIG_MAP', 'CONFIG_MAP']]


# CreateAccessEntryResponseTypeDef

### accessEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessEntryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAddonRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.AddonPodIdentityAssociationsTypeDef]]


# CreateAddonResponseTypeDef

### addon
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AddonTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourcesVpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.VpcConfigRequestTypeDef'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]

### kubernetesNetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.KubernetesNetworkConfigRequestTypeDef]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LoggingUnionTypeDef]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### encryptionConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigUnionTypeDef]]

### outpostConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OutpostConfigRequestTypeDef]

### accessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.CreateAccessConfigRequestTypeDef]

### bootstrapSelfManagedAddons
- **Type**: typing.Optional[bool]

### upgradePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpgradePolicyRequestTypeDef]

### zonalShiftConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ZonalShiftConfigRequestTypeDef]

### remoteNetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.RemoteNetworkConfigRequestTypeDef]

### computeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ComputeConfigRequestTypeDef]

### storageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.StorageConfigRequestTypeDef]


# CreateClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEksAnywhereSubscriptionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### term
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTermTypeDef'>
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


# CreateEksAnywhereSubscriptionResponseTypeDef

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFargateProfileRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.FargateProfileSelectorUnionTypeDef]]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFargateProfileResponseTypeDef

### fargateProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.FargateProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNodegroupRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupScalingConfigTypeDef]

### diskSize
- **Type**: typing.Optional[int]

### instanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### amiType
- **Type**: typing.Optional[typing.Literal['AL2023_ARM_64_STANDARD', 'AL2023_x86_64_NEURON', 'AL2023_x86_64_NVIDIA', 'AL2023_x86_64_STANDARD', 'AL2_ARM_64', 'AL2_x86_64', 'AL2_x86_64_GPU', 'BOTTLEROCKET_ARM_64', 'BOTTLEROCKET_ARM_64_NVIDIA', 'BOTTLEROCKET_x86_64', 'BOTTLEROCKET_x86_64_NVIDIA', 'CUSTOM', 'WINDOWS_CORE_2019_x86_64', 'WINDOWS_CORE_2022_x86_64', 'WINDOWS_FULL_2019_x86_64', 'WINDOWS_FULL_2022_x86_64']]

### remoteAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.RemoteAccessConfigUnionTypeDef]

### labels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### taints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.TaintTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientRequestToken
- **Type**: typing.Optional[str]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LaunchTemplateSpecificationTypeDef]

### updateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupUpdateConfigTypeDef]

### nodeRepairConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodeRepairConfigTypeDef]

### capacityType
- **Type**: typing.Optional[typing.Literal['CAPACITY_BLOCK', 'ON_DEMAND', 'SPOT']]

### version
- **Type**: typing.Optional[str]

### releaseVersion
- **Type**: typing.Optional[str]


# CreateNodegroupResponseTypeDef

### nodegroup
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.NodegroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePodIdentityAssociationRequestTypeDef

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


# CreatePodIdentityAssociationResponseTypeDef

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAccessEntryRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAddonRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### preserve
- **Type**: typing.Optional[bool]


# DeleteAddonResponseTypeDef

### addon
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AddonTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEksAnywhereSubscriptionResponseTypeDef

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFargateProfileRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFargateProfileResponseTypeDef

### fargateProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.FargateProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNodegroupRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNodegroupResponseTypeDef

### nodegroup
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.NodegroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePodIdentityAssociationRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePodIdentityAssociationResponseTypeDef

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeprecationDetailTypeDef

### usage
- **Type**: typing.Optional[str]

### replacedWith
- **Type**: typing.Optional[str]

### stopServingVersion
- **Type**: typing.Optional[str]

### startServingReplacementVersion
- **Type**: typing.Optional[str]

### clientStats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.ClientStatTypeDef]]


# DeregisterClusterRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccessEntryRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessEntryResponseTypeDef

### accessEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessEntryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAddonConfigurationRequestTypeDef

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### addonVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAddonConfigurationResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonPodIdentityConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAddonRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAddonRequestWaitExtraTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeAddonRequestWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeAddonResponseTypeDef

### addon
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AddonTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAddonVersionsResponseTypeDef

### addons
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeClusterRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequestWaitExtraTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeClusterRequestWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterVersionsRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# DescribeClusterVersionsRequestTypeDef

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


# DescribeClusterVersionsResponseTypeDef

### clusterVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.ClusterVersionInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeEksAnywhereSubscriptionResponseTypeDef

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFargateProfileRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFargateProfileRequestWaitExtraTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeFargateProfileRequestWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeFargateProfileResponseTypeDef

### fargateProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.FargateProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIdentityProviderConfigRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.IdentityProviderConfigTypeDef'>
- **Required**: Yes


# DescribeIdentityProviderConfigResponseTypeDef

### identityProviderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.IdentityProviderConfigResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInsightResponseTypeDef

### insight
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.InsightTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNodegroupRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodegroupRequestWaitExtraTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeNodegroupRequestWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeNodegroupResponseTypeDef

### nodegroup
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.NodegroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePodIdentityAssociationRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePodIdentityAssociationResponseTypeDef

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUpdateRequestTypeDef

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


# DescribeUpdateResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateAccessPolicyRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateIdentityProviderConfigRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.IdentityProviderConfigTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# DisassociateIdentityProviderConfigResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EksAnywhereSubscriptionTermTypeDef

### duration
- **Type**: typing.Optional[int]

### unit
- **Type**: typing.Optional[typing.Literal['MONTHS']]


# EksAnywhereSubscriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ElasticLoadBalancingTypeDef

### enabled
- **Type**: typing.Optional[bool]


# EncryptionConfigOutputTypeDef

### resources
- **Type**: typing.Optional[typing.List[str]]

### provider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ProviderTypeDef]


# EncryptionConfigTypeDef

### resources
- **Type**: typing.Optional[typing.Sequence[str]]

### provider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ProviderTypeDef]


# EncryptionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ErrorDetailTypeDef

### errorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AdmissionRequestDenied', 'ClusterUnreachable', 'ConfigurationConflict', 'EniLimitReached', 'InsufficientFreeAddresses', 'InsufficientNumberOfReplicas', 'IpNotAvailable', 'K8sResourceNotFound', 'NodeCreationFailure', 'OperationNotPermitted', 'PodEvictionFailure', 'SecurityGroupNotFound', 'SubnetNotFound', 'Unknown', 'UnsupportedAddonModification', 'VpcIdNotFound']]

### errorMessage
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# FargateProfileHealthTypeDef

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.FargateProfileIssueTypeDef]]


# FargateProfileIssueTypeDef

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'ClusterUnreachable', 'InternalFailure', 'PodExecutionRoleAlreadyInUse']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# FargateProfileSelectorOutputTypeDef

### namespace
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Dict[str, str]]


# FargateProfileSelectorTypeDef

### namespace
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FargateProfileSelectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FargateProfileTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.FargateProfileSelectorOutputTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### health
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.FargateProfileHealthTypeDef]


# IdentityProviderConfigResponseTypeDef

### oidc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OidcIdentityProviderConfigTypeDef]


# IdentityProviderConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdentityTypeDef

### oidc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OIDCTypeDef]


# InsightCategorySpecificSummaryTypeDef

### deprecationDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.DeprecationDetailTypeDef]]

### addonCompatibilityDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonCompatibilityDetailTypeDef]]


# InsightResourceDetailTypeDef

### insightStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.InsightStatusTypeDef]

### kubernetesResourceUri
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# InsightStatusTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ERROR', 'PASSING', 'UNKNOWN', 'WARNING']]

### reason
- **Type**: typing.Optional[str]


# InsightSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InsightTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InsightsFilterTypeDef

### categories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['UPGRADE_READINESS']]]

### kubernetesVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ERROR', 'PASSING', 'UNKNOWN', 'WARNING']]]


# IssueTypeDef

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AmiIdNotFound', 'AsgInstanceLaunchFailures', 'AutoScalingGroupInstanceRefreshActive', 'AutoScalingGroupInvalidConfiguration', 'AutoScalingGroupNotFound', 'AutoScalingGroupOptInRequired', 'AutoScalingGroupRateLimitExceeded', 'ClusterUnreachable', 'Ec2InstanceTypeDoesNotExist', 'Ec2LaunchTemplateDeletionFailure', 'Ec2LaunchTemplateInvalidConfiguration', 'Ec2LaunchTemplateMaxLimitExceeded', 'Ec2LaunchTemplateNotFound', 'Ec2LaunchTemplateVersionMaxLimitExceeded', 'Ec2LaunchTemplateVersionMismatch', 'Ec2SecurityGroupDeletionFailure', 'Ec2SecurityGroupNotFound', 'Ec2SubnetInvalidConfiguration', 'Ec2SubnetListTooLong', 'Ec2SubnetMissingIpv6Assignment', 'Ec2SubnetNotFound', 'IamInstanceProfileNotFound', 'IamLimitExceeded', 'IamNodeRoleNotFound', 'IamThrottling', 'InstanceLimitExceeded', 'InsufficientFreeAddresses', 'InternalFailure', 'KubernetesLabelInvalid', 'LimitExceeded', 'NodeCreationFailure', 'NodeTerminationFailure', 'PodEvictionFailure', 'SourceEc2LaunchTemplateNotFound', 'Unknown']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# KubernetesNetworkConfigRequestTypeDef

### serviceIpv4Cidr
- **Type**: typing.Optional[str]

### ipFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### elasticLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ElasticLoadBalancingTypeDef]


# KubernetesNetworkConfigResponseTypeDef

### serviceIpv4Cidr
- **Type**: typing.Optional[str]

### serviceIpv6Cidr
- **Type**: typing.Optional[str]

### ipFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]

### elasticLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ElasticLoadBalancingTypeDef]


# LaunchTemplateSpecificationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccessEntriesRequestPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPolicyArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListAccessEntriesRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPolicyArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessEntriesResponseTypeDef

### accessEntries
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAccessPoliciesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListAccessPoliciesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessPoliciesResponseTypeDef

### accessPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AccessPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAddonsRequestPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListAddonsRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAddonsResponseTypeDef

### addons
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedAccessPoliciesRequestPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListAssociatedAccessPoliciesRequestTypeDef

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


# ListAssociatedAccessPoliciesResponseTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedAccessPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AssociatedAccessPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginateTypeDef

### include
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListClustersRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[str]]


# ListClustersResponseTypeDef

### clusters
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEksAnywhereSubscriptionsRequestPaginateTypeDef

### includeStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'EXPIRED', 'EXPIRING', 'UPDATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListEksAnywhereSubscriptionsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### includeStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'EXPIRED', 'EXPIRING', 'UPDATING']]]


# ListEksAnywhereSubscriptionsResponseTypeDef

### subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFargateProfilesRequestPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListFargateProfilesRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFargateProfilesResponseTypeDef

### fargateProfileNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdentityProviderConfigsRequestPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListIdentityProviderConfigsRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdentityProviderConfigsResponseTypeDef

### identityProviderConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.IdentityProviderConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInsightsResponseTypeDef

### insights
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.InsightSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNodegroupsRequestPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListNodegroupsRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNodegroupsResponseTypeDef

### nodegroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPodIdentityAssociationsRequestPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### serviceAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListPodIdentityAssociationsRequestTypeDef

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


# ListPodIdentityAssociationsResponseTypeDef

### associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUpdatesRequestPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: typing.Optional[str]

### addonName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListUpdatesRequestTypeDef

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


# ListUpdatesResponseTypeDef

### updateIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogSetupOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LogSetupTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoggingOutputTypeDef

### clusterLogging
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.LogSetupOutputTypeDef]]


# LoggingTypeDef

### clusterLogging
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.LogSetupTypeDef]]


# LoggingUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MarketplaceInformationTypeDef

### productId
- **Type**: typing.Optional[str]

### productUrl
- **Type**: typing.Optional[str]


# NodeRepairConfigTypeDef

### enabled
- **Type**: typing.Optional[bool]


# NodegroupHealthTypeDef

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.IssueTypeDef]]


# NodegroupResourcesTypeDef

### autoScalingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.AutoScalingGroupTypeDef]]

### remoteAccessSecurityGroup
- **Type**: typing.Optional[str]


# NodegroupScalingConfigTypeDef

### minSize
- **Type**: typing.Optional[int]

### maxSize
- **Type**: typing.Optional[int]

### desiredSize
- **Type**: typing.Optional[int]


# NodegroupTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupScalingConfigTypeDef]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### remoteAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.RemoteAccessConfigOutputTypeDef]

### amiType
- **Type**: typing.Optional[typing.Literal['AL2023_ARM_64_STANDARD', 'AL2023_x86_64_NEURON', 'AL2023_x86_64_NVIDIA', 'AL2023_x86_64_STANDARD', 'AL2_ARM_64', 'AL2_x86_64', 'AL2_x86_64_GPU', 'BOTTLEROCKET_ARM_64', 'BOTTLEROCKET_ARM_64_NVIDIA', 'BOTTLEROCKET_x86_64', 'BOTTLEROCKET_x86_64_NVIDIA', 'CUSTOM', 'WINDOWS_CORE_2019_x86_64', 'WINDOWS_CORE_2022_x86_64', 'WINDOWS_FULL_2019_x86_64', 'WINDOWS_FULL_2022_x86_64']]

### nodeRole
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Dict[str, str]]

### taints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.TaintTypeDef]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupResourcesTypeDef]

### diskSize
- **Type**: typing.Optional[int]

### health
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupHealthTypeDef]

### updateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupUpdateConfigTypeDef]

### nodeRepairConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodeRepairConfigTypeDef]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LaunchTemplateSpecificationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# NodegroupUpdateConfigTypeDef

### maxUnavailable
- **Type**: typing.Optional[int]

### maxUnavailablePercentage
- **Type**: typing.Optional[int]

### updateStrategy
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'MINIMAL']]


# OIDCTypeDef

### issuer
- **Type**: typing.Optional[str]


# OidcIdentityProviderConfigRequestTypeDef

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


# OidcIdentityProviderConfigTypeDef

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


# OutpostConfigRequestTypeDef

### outpostArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### controlPlaneInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### controlPlanePlacement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ControlPlanePlacementRequestTypeDef]


# OutpostConfigResponseTypeDef

### outpostArns
- **Type**: typing.List[str]
- **Required**: Yes

### controlPlaneInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### controlPlanePlacement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ControlPlanePlacementResponseTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PodIdentityAssociationSummaryTypeDef

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


# PodIdentityAssociationTypeDef

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


# ProviderTypeDef

### keyArn
- **Type**: typing.Optional[str]


# RegisterClusterRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### connectorConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ConnectorConfigRequestTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoteAccessConfigOutputTypeDef

### ec2SshKey
- **Type**: typing.Optional[str]

### sourceSecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# RemoteAccessConfigTypeDef

### ec2SshKey
- **Type**: typing.Optional[str]

### sourceSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# RemoteAccessConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemoteNetworkConfigRequestTypeDef

### remoteNodeNetworks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.RemoteNodeNetworkUnionTypeDef]]

### remotePodNetworks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.RemotePodNetworkUnionTypeDef]]


# RemoteNetworkConfigResponseTypeDef

### remoteNodeNetworks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.RemoteNodeNetworkOutputTypeDef]]

### remotePodNetworks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.RemotePodNetworkOutputTypeDef]]


# RemoteNodeNetworkOutputTypeDef

### cidrs
- **Type**: typing.Optional[typing.List[str]]


# RemoteNodeNetworkTypeDef

### cidrs
- **Type**: typing.Optional[typing.Sequence[str]]


# RemoteNodeNetworkUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemotePodNetworkOutputTypeDef

### cidrs
- **Type**: typing.Optional[typing.List[str]]


# RemotePodNetworkTypeDef

### cidrs
- **Type**: typing.Optional[typing.Sequence[str]]


# RemotePodNetworkUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# StorageConfigRequestTypeDef

### blockStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.BlockStorageTypeDef]


# StorageConfigResponseTypeDef

### blockStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.BlockStorageTypeDef]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TaintTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### effect
- **Type**: typing.Optional[typing.Literal['NO_EXECUTE', 'NO_SCHEDULE', 'PREFER_NO_SCHEDULE']]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessConfigRequestTypeDef

### authenticationMode
- **Type**: typing.Optional[typing.Literal['API', 'API_AND_CONFIG_MAP', 'CONFIG_MAP']]


# UpdateAccessEntryRequestTypeDef

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


# UpdateAccessEntryResponseTypeDef

### accessEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessEntryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAddonRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.AddonPodIdentityAssociationsTypeDef]]


# UpdateAddonResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterConfigRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.VpcConfigRequestTypeDef]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LoggingUnionTypeDef]

### clientRequestToken
- **Type**: typing.Optional[str]

### accessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpdateAccessConfigRequestTypeDef]

### upgradePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpgradePolicyRequestTypeDef]

### zonalShiftConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ZonalShiftConfigRequestTypeDef]

### computeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ComputeConfigRequestTypeDef]

### kubernetesNetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.KubernetesNetworkConfigRequestTypeDef]

### storageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.StorageConfigRequestTypeDef]


# UpdateClusterConfigResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterVersionRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateClusterVersionResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEksAnywhereSubscriptionResponseTypeDef

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLabelsPayloadTypeDef

### addOrUpdateLabels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### removeLabels
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateNodegroupConfigRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### labels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpdateLabelsPayloadTypeDef]

### taints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpdateTaintsPayloadTypeDef]

### scalingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupScalingConfigTypeDef]

### updateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodegroupUpdateConfigTypeDef]

### nodeRepairConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.NodeRepairConfigTypeDef]

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateNodegroupConfigResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNodegroupVersionRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LaunchTemplateSpecificationTypeDef]

### force
- **Type**: typing.Optional[bool]

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateNodegroupVersionResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePodIdentityAssociationRequestTypeDef

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


# UpdatePodIdentityAssociationResponseTypeDef

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.PodIdentityAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTaintsPayloadTypeDef

### addOrUpdateTaints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.TaintTypeDef]]

### removeTaints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.TaintTypeDef]]


# UpdateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpgradePolicyRequestTypeDef

### supportType
- **Type**: typing.Optional[typing.Literal['EXTENDED', 'STANDARD']]


# UpgradePolicyResponseTypeDef

### supportType
- **Type**: typing.Optional[typing.Literal['EXTENDED', 'STANDARD']]


# VpcConfigRequestTypeDef

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


# VpcConfigResponseTypeDef

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


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# ZonalShiftConfigRequestTypeDef

### enabled
- **Type**: typing.Optional[bool]


# ZonalShiftConfigResponseTypeDef

### enabled
- **Type**: typing.Optional[bool]


