# Opensearchserverless Classes

# AccessPolicyDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessPolicyStats

### DataPolicyCount
- **Type**: typing.Optional[int]


# AccessPolicySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccountSettingsDetail

### capacityLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.CapacityLimits]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetCollectionRequest

### ids
- **Type**: typing.Optional[typing.Sequence[str]]

### names
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetCollectionResponse

### collectionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionDetail]
- **Required**: Yes

### collectionErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetEffectiveLifecyclePolicyRequest

### resourceIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyResourceIdentifier]
- **Required**: Yes


# BatchGetEffectiveLifecyclePolicyResponse

### effectiveLifecyclePolicyDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.EffectiveLifecyclePolicyDetail]
- **Required**: Yes

### effectiveLifecyclePolicyErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.EffectiveLifecyclePolicyErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetLifecyclePolicyRequest

### identifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyIdentifier]
- **Required**: Yes


# BatchGetLifecyclePolicyResponse

### lifecyclePolicyDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyDetail]
- **Required**: Yes

### lifecyclePolicyErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetVpcEndpointRequest

### ids
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetVpcEndpointResponse

### vpcEndpointDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointDetail]
- **Required**: Yes

### vpcEndpointErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CapacityLimits

### maxIndexingCapacityInOCU
- **Type**: typing.Optional[int]

### maxSearchCapacityInOCU
- **Type**: typing.Optional[int]


# CollectionDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollectionErrorDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CollectionFilters

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]


# CollectionSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessPolicyResponse

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCollectionDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCollectionResponse

### createCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.CreateCollectionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIamIdentityCenterConfigOptions

### instanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### userAttribute
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### groupAttribute
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# CreateLifecyclePolicyResponse

### lifecyclePolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecurityConfigResponse

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecurityPolicyResponse

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcEndpointDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateVpcEndpointRequest

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


# CreateVpcEndpointResponse

### createVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.CreateVpcEndpointDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCollectionDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteCollectionResponse

### deleteCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.DeleteCollectionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVpcEndpointDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteVpcEndpointResponse

### deleteVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.DeleteVpcEndpointDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# EffectiveLifecyclePolicyDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EffectiveLifecyclePolicyErrorDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAccessPolicyResponse

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccountSettingsResponse

### accountSettingsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccountSettingsDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetPoliciesStatsResponse

### AccessPolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyStats'>
- **Required**: Yes

### SecurityPolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyStats'>
- **Required**: Yes

### SecurityConfigStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigStats'>
- **Required**: Yes

### LifecyclePolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyStats'>
- **Required**: Yes

### TotalPolicyCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetSecurityConfigResponse

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetSecurityPolicyResponse

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# IamIdentityCenterConfigOptions

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


# LifecyclePolicyDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyErrorDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyIdentifier

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyResourceIdentifier

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecyclePolicyStats

### RetentionPolicyCount
- **Type**: typing.Optional[int]


# LifecyclePolicySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccessPoliciesResponse

### accessPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollectionsRequest

### collectionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionFilters]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollectionsResponse

### collectionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecyclePoliciesResponse

### lifecyclePolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigsResponse

### securityConfigSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityPoliciesResponse

### securityPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcEndpointsRequest

### vpcEndpointFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointFilters]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListVpcEndpointsResponse

### vpcEndpointSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
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


# SamlConfigOptions

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


# SecurityConfigDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityConfigStats

### SamlConfigCount
- **Type**: typing.Optional[int]


# SecurityConfigSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityPolicyDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SecurityPolicyStats

### EncryptionPolicyCount
- **Type**: typing.Optional[int]

### NetworkPolicyCount
- **Type**: typing.Optional[int]


# SecurityPolicySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.opensearchserverless_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessPolicyResponse

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAccountSettingsRequest

### capacityLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.CapacityLimits]


# UpdateAccountSettingsResponse

### accountSettingsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccountSettingsDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCollectionDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateCollectionResponse

### updateCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.UpdateCollectionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIamIdentityCenterConfigOptions

### userAttribute
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### groupAttribute
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# UpdateLifecyclePolicyResponse

### lifecyclePolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSecurityConfigResponse

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSecurityPolicyResponse

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVpcEndpointDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateVpcEndpointResponse

### UpdateVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.UpdateVpcEndpointDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# VpcEndpointDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcEndpointErrorDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcEndpointFilters

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# VpcEndpointSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

