# opensearchserverless_classes

# AccessPolicyDetailTypeDef

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### policyVersion
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['data']]


# AccessPolicyStatsTypeDef

### DataPolicyCount
- **Type**: typing.Optional[int]


# AccessPolicySummaryTypeDef

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['data']]


# AccountSettingsDetailTypeDef

### capacityLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.CapacityLimitsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetCollectionRequestRequestTypeDef

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


# BatchGetEffectiveLifecyclePolicyRequestRequestTypeDef

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


# BatchGetLifecyclePolicyRequestRequestTypeDef

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


# BatchGetVpcEndpointRequestRequestTypeDef

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

### arn
- **Type**: typing.Optional[str]

### collectionEndpoint
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### dashboardEndpoint
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### standbyReplicas
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### type
- **Type**: typing.Optional[typing.Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH']]


# CollectionErrorDetailTypeDef

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# CollectionFiltersTypeDef

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]


# CollectionSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]


# CreateAccessPolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateAccessPolicyResponseTypeDef

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCollectionDetailTypeDef

### arn
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### standbyReplicas
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### type
- **Type**: typing.Optional[typing.Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH']]


# CreateCollectionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### standbyReplicas
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opensearchserverless_classes.TagTypeDef]]

### type
- **Type**: typing.Optional[typing.Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH']]


# CreateCollectionResponseTypeDef

### createCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.CreateCollectionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLifecyclePolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateLifecyclePolicyResponseTypeDef

### lifecyclePolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecurityConfigRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['saml']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### samlOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.SamlConfigOptionsTypeDef]


# CreateSecurityConfigResponseTypeDef

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSecurityPolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateSecurityPolicyResponseTypeDef

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcEndpointDetailTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# CreateVpcEndpointRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateVpcEndpointResponseTypeDef

### createVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.CreateVpcEndpointDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAccessPolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteCollectionDetailTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]


# DeleteCollectionRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteCollectionResponseTypeDef

### deleteCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.DeleteCollectionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLifecyclePolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteSecurityConfigRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteSecurityPolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteVpcEndpointDetailTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# DeleteVpcEndpointRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteVpcEndpointResponseTypeDef

### deleteVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.DeleteVpcEndpointDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EffectiveLifecyclePolicyDetailTypeDef

### noMinRetentionPeriod
- **Type**: typing.Optional[bool]

### policyName
- **Type**: typing.Optional[str]

### resource
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['index']]

### retentionPeriod
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['retention']]


# EffectiveLifecyclePolicyErrorDetailTypeDef

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### resource
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['retention']]


# GetAccessPolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['data']
- **Required**: Yes


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

### LifecyclePolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyStatsTypeDef'>
- **Required**: Yes

### SecurityConfigStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigStatsTypeDef'>
- **Required**: Yes

### SecurityPolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyStatsTypeDef'>
- **Required**: Yes

### TotalPolicyCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSecurityConfigRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSecurityConfigResponseTypeDef

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSecurityPolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes


# GetSecurityPolicyResponseTypeDef

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LifecyclePolicyDetailTypeDef

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### policyVersion
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['retention']]


# LifecyclePolicyErrorDetailTypeDef

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['retention']]


# LifecyclePolicyIdentifierTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes


# LifecyclePolicyResourceIdentifierTypeDef

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes


# LifecyclePolicyStatsTypeDef

### RetentionPolicyCount
- **Type**: typing.Optional[int]


# LifecyclePolicySummaryTypeDef

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['retention']]


# ListAccessPoliciesRequestRequestTypeDef

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resource
- **Type**: typing.Optional[typing.Sequence[str]]


# ListAccessPoliciesResponseTypeDef

### accessPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCollectionsRequestRequestTypeDef

### collectionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCollectionsResponseTypeDef

### collectionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.CollectionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLifecyclePoliciesRequestRequestTypeDef

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resources
- **Type**: typing.Optional[typing.Sequence[str]]


# ListLifecyclePoliciesResponseTypeDef

### lifecyclePolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSecurityConfigsRequestRequestTypeDef

### type
- **Type**: typing.Literal['saml']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### securityConfigSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSecurityPoliciesRequestRequestTypeDef

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### resource
- **Type**: typing.Optional[typing.Sequence[str]]


# ListSecurityPoliciesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### securityPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListVpcEndpointsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### vpcEndpointFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointFiltersTypeDef]


# ListVpcEndpointsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### vpcEndpointSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless_classes.VpcEndpointSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# SamlConfigOptionsTypeDef

### metadata
- **Type**: <class 'str'>
- **Required**: Yes

### groupAttribute
- **Type**: typing.Optional[str]

### sessionTimeout
- **Type**: typing.Optional[int]

### userAttribute
- **Type**: typing.Optional[str]


# SecurityConfigDetailTypeDef

### configVersion
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### samlOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.SamlConfigOptionsTypeDef]

### type
- **Type**: typing.Optional[typing.Literal['saml']]


# SecurityConfigStatsTypeDef

### SamlConfigCount
- **Type**: typing.Optional[int]


# SecurityConfigSummaryTypeDef

### configVersion
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### type
- **Type**: typing.Optional[typing.Literal['saml']]


# SecurityPolicyDetailTypeDef

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### policyVersion
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['encryption', 'network']]


# SecurityPolicyStatsTypeDef

### EncryptionPolicyCount
- **Type**: typing.Optional[int]

### NetworkPolicyCount
- **Type**: typing.Optional[int]


# SecurityPolicySummaryTypeDef

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['encryption', 'network']]


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessPolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersion
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]


# UpdateAccessPolicyResponseTypeDef

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.AccessPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAccountSettingsRequestRequestTypeDef

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

### arn
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### type
- **Type**: typing.Optional[typing.Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH']]


# UpdateCollectionRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateCollectionResponseTypeDef

### updateCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.UpdateCollectionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLifecyclePolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersion
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]


# UpdateLifecyclePolicyResponseTypeDef

### lifecyclePolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.LifecyclePolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSecurityConfigRequestRequestTypeDef

### configVersion
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### samlOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless_classes.SamlConfigOptionsTypeDef]


# UpdateSecurityConfigResponseTypeDef

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityConfigDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSecurityPolicyRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersion
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]


# UpdateSecurityPolicyResponseTypeDef

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.SecurityPolicyDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVpcEndpointDetailTypeDef

### id
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]


# UpdateVpcEndpointRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### addSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### addSubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]

### removeSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### removeSubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateVpcEndpointResponseTypeDef

### UpdateVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.UpdateVpcEndpointDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcEndpointDetailTypeDef

### createdDate
- **Type**: typing.Optional[int]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]


# VpcEndpointErrorDetailTypeDef

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# VpcEndpointFiltersTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# VpcEndpointSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


