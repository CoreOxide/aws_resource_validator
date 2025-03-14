# Opensearchserverless Classes

# AccessPolicyDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessPolicyStatsTypeDef

### DataPolicyCount
- **Type**: typing.Optional[int]


# AccessPolicySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccountSettingsDetailTypeDef

### capacityLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.CapacityLimitsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetCollectionRequestTypeDef

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### names
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetCollectionResponseTypeDef

### collectionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionDetailTypeDef]
- **Required**: Yes

### collectionErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionErrorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetEffectiveLifecyclePolicyRequestTypeDef

### resourceIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyResourceIdentifierTypeDef]
- **Required**: Yes


# BatchGetEffectiveLifecyclePolicyResponseTypeDef

### effectiveLifecyclePolicyDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.EffectiveLifecyclePolicyDetailTypeDef]
- **Required**: Yes

### effectiveLifecyclePolicyErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.EffectiveLifecyclePolicyErrorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetLifecyclePolicyRequestTypeDef

### identifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyIdentifierTypeDef]
- **Required**: Yes


# BatchGetLifecyclePolicyResponseTypeDef

### lifecyclePolicyDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyDetailTypeDef]
- **Required**: Yes

### lifecyclePolicyErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyErrorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetVpcEndpointRequestTypeDef

### ids
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetVpcEndpointResponseTypeDef

### vpcEndpointDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointDetailTypeDef]
- **Required**: Yes

### vpcEndpointErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointErrorDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CapacityLimitsTypeDef

### maxIndexingCapacityInOCU
- **Type**: typing.Optional[int]

### maxSearchCapacityInOCU
- **Type**: typing.Optional[int]


# CollectionDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollectionErrorDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollectionFiltersTypeDef

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]


# CollectionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessPolicyResponseTypeDef

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCollectionDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCollectionResponseTypeDef

### createCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.CreateCollectionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIamIdentityCenterConfigOptionsTypeDef

### instanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### userAttribute
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### groupAttribute
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# CreateLifecyclePolicyResponseTypeDef

### lifecyclePolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecurityConfigResponseTypeDef

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecurityPolicyResponseTypeDef

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcEndpointDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateVpcEndpointRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateVpcEndpointResponseTypeDef

### createVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.CreateVpcEndpointDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCollectionDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteCollectionResponseTypeDef

### deleteCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.DeleteCollectionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVpcEndpointDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteVpcEndpointResponseTypeDef

### deleteVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.DeleteVpcEndpointDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EffectiveLifecyclePolicyDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EffectiveLifecyclePolicyErrorDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAccessPolicyResponseTypeDef

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccountSettingsResponseTypeDef

### accountSettingsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccountSettingsDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPoliciesStatsResponseTypeDef

### AccessPolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyStatsTypeDef'>
- **Required**: Yes

### SecurityPolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyStatsTypeDef'>
- **Required**: Yes

### SecurityConfigStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigStatsTypeDef'>
- **Required**: Yes

### LifecyclePolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyStatsTypeDef'>
- **Required**: Yes

### TotalPolicyCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSecurityConfigResponseTypeDef

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSecurityPolicyResponseTypeDef

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IamIdentityCenterConfigOptionsTypeDef

### instanceArn
- **Type**: typing.Optional[str]

### applicationArn
- **Type**: typing.Optional[str]

### applicationName
- **Type**: typing.Optional[str]

### applicationDescription
- **Type**: typing.Optional[str]

### userAttribute
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### groupAttribute
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# LifecyclePolicyDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyErrorDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyIdentifierTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyResourceIdentifierTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyStatsTypeDef

### RetentionPolicyCount
- **Type**: typing.Optional[int]


# LifecyclePolicySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccessPoliciesResponseTypeDef

### accessPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollectionsRequestTypeDef

### collectionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionFiltersTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollectionsResponseTypeDef

### collectionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecyclePoliciesResponseTypeDef

### lifecyclePolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigsResponseTypeDef

### securityConfigSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityPoliciesResponseTypeDef

### securityPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcEndpointsRequestTypeDef

### vpcEndpointFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointFiltersTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListVpcEndpointsResponseTypeDef

### vpcEndpointSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
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


# SamlConfigOptionsTypeDef

### metadata
- **Type**: <class 'str'>
- **Required**: Yes

### userAttribute
- **Type**: typing.Optional[str]

### groupAttribute
- **Type**: typing.Optional[str]

### openSearchServerlessEntityId
- **Type**: typing.Optional[str]

### sessionTimeout
- **Type**: typing.Optional[int]


# SecurityConfigDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityConfigStatsTypeDef

### SamlConfigCount
- **Type**: typing.Optional[int]


# SecurityConfigSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityPolicyDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityPolicyStatsTypeDef

### EncryptionPolicyCount
- **Type**: typing.Optional[int]

### NetworkPolicyCount
- **Type**: typing.Optional[int]


# SecurityPolicySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opensearchserverless_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessPolicyResponseTypeDef

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAccountSettingsRequestTypeDef

### capacityLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.CapacityLimitsTypeDef]


# UpdateAccountSettingsResponseTypeDef

### accountSettingsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccountSettingsDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCollectionDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateCollectionResponseTypeDef

### updateCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.UpdateCollectionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIamIdentityCenterConfigOptionsTypeDef

### userAttribute
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### groupAttribute
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# UpdateLifecyclePolicyResponseTypeDef

### lifecyclePolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSecurityConfigResponseTypeDef

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSecurityPolicyResponseTypeDef

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVpcEndpointDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateVpcEndpointResponseTypeDef

### UpdateVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.UpdateVpcEndpointDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcEndpointDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcEndpointErrorDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcEndpointFiltersTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# VpcEndpointSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

