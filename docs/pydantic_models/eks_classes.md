# eks_classes

# AccessConfigResponseTypeDef

### bootstrapClusterCreatorAdminPermissions
- **Type**: typing.Optional[bool]

### authenticationMode
- **Type**: typing.Optional[typing.Literal['API', 'API_AND_CONFIG_MAP', 'CONFIG_MAP']]


# AccessEntryTypeDef

### clusterName
- **Type**: typing.Optional[str]

### principalArn
- **Type**: typing.Optional[str]

### kubernetesGroups
- **Type**: typing.Optional[typing.List[str]]

### accessEntryArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### username
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# AccessPolicyTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# AccessScopeExtraOutputTypeDef

### type
- **Type**: typing.Optional[typing.Literal['cluster', 'namespace']]

### namespaces
- **Type**: typing.Optional[typing.List[str]]


# AccessScopeOutputTypeDef

### type
- **Type**: typing.Optional[typing.Literal['cluster', 'namespace']]

### namespaces
- **Type**: typing.Optional[typing.List[str]]


# AccessScopeTypeDef

### type
- **Type**: typing.Optional[typing.Literal['cluster', 'namespace']]

### namespaces
- **Type**: typing.Optional[typing.Sequence[str]]


# AddonHealthTypeDef

### issues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonIssueTypeDef]]


# AddonInfoTypeDef

### addonName
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### addonVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonVersionInfoTypeDef]]

### publisher
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]

### marketplaceInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.MarketplaceInformationTypeDef]


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

### compatibilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.CompatibilityTypeDef]]

### requiresConfiguration
- **Type**: typing.Optional[bool]

### requiresIamPermissions
- **Type**: typing.Optional[bool]


# AssociateAccessPolicyRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessScopeTypeDef'>
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


# AssociateEncryptionConfigRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfig
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigTypeDef, aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigOutputTypeDef]]
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


# AssociateIdentityProviderConfigRequestRequestTypeDef

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

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### version
- **Type**: typing.Optional[str]

### endpoint
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### resourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.VpcConfigResponseTypeDef]

### kubernetesNetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.KubernetesNetworkConfigResponseTypeDef]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LoggingOutputTypeDef]

### identity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.IdentityTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'PENDING', 'UPDATING']]

### certificateAuthority
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.CertificateTypeDef]

### clientRequestToken
- **Type**: typing.Optional[str]

### platformVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### encryptionConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigOutputTypeDef]]

### connectorConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ConnectorConfigResponseTypeDef]

### id
- **Type**: typing.Optional[str]

### health
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.ClusterHealthTypeDef]

### outpostConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OutpostConfigResponseTypeDef]

### accessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.AccessConfigResponseTypeDef]


# CompatibilityTypeDef

### clusterVersion
- **Type**: typing.Optional[str]

### platformVersions
- **Type**: typing.Optional[typing.List[str]]

### defaultVersion
- **Type**: typing.Optional[bool]


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


# CreateAccessEntryRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### kubernetesGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientRequestToken
- **Type**: typing.Optional[str]

### username
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# CreateAccessEntryResponseTypeDef

### accessEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AccessEntryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAddonRequestRequestTypeDef

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


# CreateClusterRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LoggingTypeDef]

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### encryptionConfig
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigTypeDef, aws_resource_validator.pydantic_models.eks_classes.EncryptionConfigOutputTypeDef]]]

### outpostConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OutpostConfigRequestTypeDef]

### accessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.CreateAccessConfigRequestTypeDef]

### bootstrapSelfManagedAddons
- **Type**: typing.Optional[bool]


# CreateClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEksAnywhereSubscriptionRequestRequestTypeDef

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


# CreateFargateProfileRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.eks_classes.FargateProfileSelectorTypeDef, aws_resource_validator.pydantic_models.eks_classes.FargateProfileSelectorOutputTypeDef]]]

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


# CreateNodegroupRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['AL2023_ARM_64_STANDARD', 'AL2023_x86_64_STANDARD', 'AL2_ARM_64', 'AL2_x86_64', 'AL2_x86_64_GPU', 'BOTTLEROCKET_ARM_64', 'BOTTLEROCKET_ARM_64_NVIDIA', 'BOTTLEROCKET_x86_64', 'BOTTLEROCKET_x86_64_NVIDIA', 'CUSTOM', 'WINDOWS_CORE_2019_x86_64', 'WINDOWS_CORE_2022_x86_64', 'WINDOWS_FULL_2019_x86_64', 'WINDOWS_FULL_2022_x86_64']]

### remoteAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.RemoteAccessConfigTypeDef]

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


# CreatePodIdentityAssociationRequestRequestTypeDef

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


# DeleteAccessEntryRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAddonRequestRequestTypeDef

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


# DeleteClusterRequestRequestTypeDef

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


# DeleteEksAnywhereSubscriptionRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEksAnywhereSubscriptionResponseTypeDef

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFargateProfileRequestRequestTypeDef

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


# DeleteNodegroupRequestRequestTypeDef

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


# DeletePodIdentityAssociationRequestRequestTypeDef

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


# DeregisterClusterRequestRequestTypeDef

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


# DescribeAccessEntryRequestRequestTypeDef

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


# DescribeAddonConfigurationRequestRequestTypeDef

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


# DescribeAddonRequestAddonActiveWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeAddonRequestAddonDeletedWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeAddonRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### addonName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAddonResponseTypeDef

### addon
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.AddonTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAddonVersionsRequestDescribeAddonVersionsPaginateTypeDef

### kubernetesVersion
- **Type**: typing.Optional[str]

### addonName
- **Type**: typing.Optional[str]

### types
- **Type**: typing.Optional[typing.Sequence[str]]

### publishers
- **Type**: typing.Optional[typing.Sequence[str]]

### owners
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# DescribeAddonVersionsRequestRequestTypeDef

### kubernetesVersion
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### addonName
- **Type**: typing.Optional[str]

### types
- **Type**: typing.Optional[typing.Sequence[str]]

### publishers
- **Type**: typing.Optional[typing.Sequence[str]]

### owners
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeAddonVersionsResponseTypeDef

### addons
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AddonInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterRequestClusterActiveWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeClusterRequestClusterDeletedWaitTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeClusterRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEksAnywhereSubscriptionRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEksAnywhereSubscriptionResponseTypeDef

### subscription
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFargateProfileRequestFargateProfileActiveWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeFargateProfileRequestFargateProfileDeletedWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeFargateProfileRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### fargateProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFargateProfileResponseTypeDef

### fargateProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.FargateProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIdentityProviderConfigRequestRequestTypeDef

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


# DescribeInsightRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInsightResponseTypeDef

### insight
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.InsightTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNodegroupRequestNodegroupActiveWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeNodegroupRequestNodegroupDeletedWaitTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.WaiterConfigTypeDef]


# DescribeNodegroupRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodegroupResponseTypeDef

### nodegroup
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.NodegroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePodIdentityAssociationRequestRequestTypeDef

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


# DescribeUpdateRequestRequestTypeDef

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


# DisassociateAccessPolicyRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateIdentityProviderConfigRequestRequestTypeDef

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

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### effectiveDate
- **Type**: typing.Optional[datetime.datetime]

### expirationDate
- **Type**: typing.Optional[datetime.datetime]

### licenseQuantity
- **Type**: typing.Optional[int]

### licenseType
- **Type**: typing.Optional[typing.Literal['Cluster']]

### term
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.EksAnywhereSubscriptionTermTypeDef]

### status
- **Type**: typing.Optional[str]

### autoRenew
- **Type**: typing.Optional[bool]

### licenseArns
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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

### type
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# IdentityTypeDef

### oidc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.OIDCTypeDef]


# InsightCategorySpecificSummaryTypeDef

### deprecationDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.DeprecationDetailTypeDef]]


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

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[typing.Literal['UPGRADE_READINESS']]

### kubernetesVersion
- **Type**: typing.Optional[str]

### lastRefreshTime
- **Type**: typing.Optional[datetime.datetime]

### lastTransitionTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### insightStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.InsightStatusTypeDef]


# InsightTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[typing.Literal['UPGRADE_READINESS']]

### kubernetesVersion
- **Type**: typing.Optional[str]

### lastRefreshTime
- **Type**: typing.Optional[datetime.datetime]

### lastTransitionTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### insightStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.InsightStatusTypeDef]

### recommendation
- **Type**: typing.Optional[str]

### additionalInfo
- **Type**: typing.Optional[typing.Dict[str, str]]

### resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.InsightResourceDetailTypeDef]]

### categorySpecificSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.InsightCategorySpecificSummaryTypeDef]


# InsightsFilterTypeDef

### categories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['UPGRADE_READINESS']]]

### kubernetesVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ERROR', 'PASSING', 'UNKNOWN', 'WARNING']]]


# IssueTypeDef

### code
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'AmiIdNotFound', 'AsgInstanceLaunchFailures', 'AutoScalingGroupInstanceRefreshActive', 'AutoScalingGroupInvalidConfiguration', 'AutoScalingGroupNotFound', 'AutoScalingGroupOptInRequired', 'AutoScalingGroupRateLimitExceeded', 'ClusterUnreachable', 'Ec2LaunchTemplateDeletionFailure', 'Ec2LaunchTemplateInvalidConfiguration', 'Ec2LaunchTemplateMaxLimitExceeded', 'Ec2LaunchTemplateNotFound', 'Ec2LaunchTemplateVersionMaxLimitExceeded', 'Ec2LaunchTemplateVersionMismatch', 'Ec2SecurityGroupDeletionFailure', 'Ec2SecurityGroupNotFound', 'Ec2SubnetInvalidConfiguration', 'Ec2SubnetListTooLong', 'Ec2SubnetMissingIpv6Assignment', 'Ec2SubnetNotFound', 'IamInstanceProfileNotFound', 'IamLimitExceeded', 'IamNodeRoleNotFound', 'IamThrottling', 'InstanceLimitExceeded', 'InsufficientFreeAddresses', 'InternalFailure', 'KubernetesLabelInvalid', 'LimitExceeded', 'NodeCreationFailure', 'NodeTerminationFailure', 'PodEvictionFailure', 'SourceEc2LaunchTemplateNotFound', 'Unknown']]

### message
- **Type**: typing.Optional[str]

### resourceIds
- **Type**: typing.Optional[typing.List[str]]


# KubernetesNetworkConfigRequestTypeDef

### serviceIpv4Cidr
- **Type**: typing.Optional[str]

### ipFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# KubernetesNetworkConfigResponseTypeDef

### serviceIpv4Cidr
- **Type**: typing.Optional[str]

### serviceIpv6Cidr
- **Type**: typing.Optional[str]

### ipFamily
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# LaunchTemplateSpecificationTypeDef

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# ListAccessEntriesRequestListAccessEntriesPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPolicyArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListAccessEntriesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListAccessPoliciesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessPoliciesResponseTypeDef

### accessPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AccessPolicyTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAddonsRequestListAddonsPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListAddonsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssociatedAccessPoliciesRequestListAssociatedAccessPoliciesPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListAssociatedAccessPoliciesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### associatedAccessPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.AssociatedAccessPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListClustersRequestListClustersPaginateTypeDef

### include
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListClustersRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEksAnywhereSubscriptionsRequestListEksAnywhereSubscriptionsPaginateTypeDef

### includeStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'EXPIRED', 'EXPIRING', 'UPDATING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListEksAnywhereSubscriptionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFargateProfilesRequestListFargateProfilesPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListFargateProfilesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIdentityProviderConfigsRequestListIdentityProviderConfigsPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListIdentityProviderConfigsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInsightsRequestListInsightsPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.InsightsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListInsightsRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.InsightsFilterTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInsightsResponseTypeDef

### insights
- **Type**: typing.List[aws_resource_validator.pydantic_models.eks_classes.InsightSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNodegroupsRequestListNodegroupsPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListNodegroupsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPodIdentityAssociationsRequestListPodIdentityAssociationsPaginateTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### serviceAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListPodIdentityAssociationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListUpdatesRequestListUpdatesPaginateTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nodegroupName
- **Type**: typing.Optional[str]

### addonName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.PaginatorConfigTypeDef]


# ListUpdatesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogSetupOutputTypeDef

### types
- **Type**: typing.Optional[typing.List[typing.Literal['api', 'audit', 'authenticator', 'controllerManager', 'scheduler']]]

### enabled
- **Type**: typing.Optional[bool]


# LogSetupTypeDef

### types
- **Type**: typing.Optional[typing.Sequence[typing.Literal['api', 'audit', 'authenticator', 'controllerManager', 'scheduler']]]

### enabled
- **Type**: typing.Optional[bool]


# LoggingOutputTypeDef

### clusterLogging
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.LogSetupOutputTypeDef]]


# LoggingTypeDef

### clusterLogging
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.eks_classes.LogSetupTypeDef]]


# MarketplaceInformationTypeDef

### productId
- **Type**: typing.Optional[str]

### productUrl
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.Literal['AL2023_ARM_64_STANDARD', 'AL2023_x86_64_STANDARD', 'AL2_ARM_64', 'AL2_x86_64', 'AL2_x86_64_GPU', 'BOTTLEROCKET_ARM_64', 'BOTTLEROCKET_ARM_64_NVIDIA', 'BOTTLEROCKET_x86_64', 'BOTTLEROCKET_x86_64_NVIDIA', 'CUSTOM', 'WINDOWS_CORE_2019_x86_64', 'WINDOWS_CORE_2022_x86_64', 'WINDOWS_FULL_2019_x86_64', 'WINDOWS_FULL_2022_x86_64']]

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

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LaunchTemplateSpecificationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# NodegroupUpdateConfigTypeDef

### maxUnavailable
- **Type**: typing.Optional[int]

### maxUnavailablePercentage
- **Type**: typing.Optional[int]


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


# RegisterClusterRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessConfigRequestTypeDef

### authenticationMode
- **Type**: typing.Optional[typing.Literal['API', 'API_AND_CONFIG_MAP', 'CONFIG_MAP']]


# UpdateAccessEntryRequestRequestTypeDef

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


# UpdateAddonRequestRequestTypeDef

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


# UpdateClusterConfigRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.VpcConfigRequestTypeDef]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.LoggingTypeDef]

### clientRequestToken
- **Type**: typing.Optional[str]

### accessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.eks_classes.UpdateAccessConfigRequestTypeDef]


# UpdateClusterConfigResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterVersionRequestRequestTypeDef

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


# UpdateEksAnywhereSubscriptionRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### autoRenew
- **Type**: <class 'bool'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


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


# UpdateNodegroupConfigRequestRequestTypeDef

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

### clientRequestToken
- **Type**: typing.Optional[str]


# UpdateNodegroupConfigResponseTypeDef

### update
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.UpdateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNodegroupVersionRequestRequestTypeDef

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


# UpdateParamTypeDef

### type
- **Type**: typing.Optional[typing.Literal['AddonVersion', 'AuthenticationMode', 'ClusterLogging', 'ConfigurationValues', 'DesiredSize', 'EncryptionConfig', 'EndpointPrivateAccess', 'EndpointPublicAccess', 'IdentityProviderConfig', 'LabelsToAdd', 'LabelsToRemove', 'LaunchTemplateName', 'LaunchTemplateVersion', 'MaxSize', 'MaxUnavailable', 'MaxUnavailablePercentage', 'MinSize', 'PlatformVersion', 'PodIdentityAssociations', 'PublicAccessCidrs', 'ReleaseVersion', 'ResolveConflicts', 'SecurityGroups', 'ServiceAccountRoleArn', 'Subnets', 'TaintsToAdd', 'TaintsToRemove', 'Version']]

### value
- **Type**: typing.Optional[str]


# UpdatePodIdentityAssociationRequestRequestTypeDef

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

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Failed', 'InProgress', 'Successful']]

### type
- **Type**: typing.Optional[typing.Literal['AccessConfigUpdate', 'AddonUpdate', 'AssociateEncryptionConfig', 'AssociateIdentityProviderConfig', 'ConfigUpdate', 'DisassociateIdentityProviderConfig', 'EndpointAccessUpdate', 'LoggingUpdate', 'VersionUpdate', 'VpcConfigUpdate']]

### params
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.UpdateParamTypeDef]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.eks_classes.ErrorDetailTypeDef]]


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


