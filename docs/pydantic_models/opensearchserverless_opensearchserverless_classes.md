# Opensearchserverless Opensearchserverless Classes

# AccessPolicyDetail

### type
- **Type**: typing.Optional[typing.Literal['data']]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# AccessPolicyStats

### DataPolicyCount
- **Type**: typing.Optional[int]


# AccessPolicySummary

### type
- **Type**: typing.Optional[typing.Literal['data']]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# AccountSettingsDetail

### capacityLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CapacityLimits]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetCollectionRequest

### ids
- **Type**: typing.Optional[typing.List[str]]

### names
- **Type**: typing.Optional[typing.List[str]]


# BatchGetCollectionResponse

### collectionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CollectionDetail]
- **Required**: Yes

### collectionErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CollectionErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetEffectiveLifecyclePolicyRequest

### resourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.LifecyclePolicyResourceIdentifier]
- **Required**: Yes


# BatchGetEffectiveLifecyclePolicyResponse

### effectiveLifecyclePolicyDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.EffectiveLifecyclePolicyDetail]
- **Required**: Yes

### effectiveLifecyclePolicyErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.EffectiveLifecyclePolicyErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetLifecyclePolicyRequest

### identifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.LifecyclePolicyIdentifier]
- **Required**: Yes


# BatchGetLifecyclePolicyResponse

### lifecyclePolicyDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.LifecyclePolicyDetail]
- **Required**: Yes

### lifecyclePolicyErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.LifecyclePolicyErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetVpcEndpointRequest

### ids
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetVpcEndpointResponse

### vpcEndpointDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.VpcEndpointDetail]
- **Required**: Yes

### vpcEndpointErrorDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.VpcEndpointErrorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CapacityLimits

### maxIndexingCapacityInOCU
- **Type**: typing.Optional[int]

### maxSearchCapacityInOCU
- **Type**: typing.Optional[int]


# CollectionDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### type
- **Type**: typing.Optional[typing.Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH']]

### description
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### standbyReplicas
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]

### collectionEndpoint
- **Type**: typing.Optional[str]

### dashboardEndpoint
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]


# CollectionErrorDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]


# CollectionFilters

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]


# CollectionSummary

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### arn
- **Type**: typing.Optional[str]


# CreateAccessPolicyRequest

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# CreateAccessPolicyResponse

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.AccessPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCollectionDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### type
- **Type**: typing.Optional[typing.Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH']]

### description
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### standbyReplicas
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# CreateCollectionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH']]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.Tag]]

### standbyReplicas
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### clientToken
- **Type**: typing.Optional[str]


# CreateCollectionResponse

### createCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CreateCollectionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIamIdentityCenterConfigOptions

### instanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### userAttribute
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### groupAttribute
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# CreateLifecyclePolicyRequest

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# CreateLifecyclePolicyResponse

### lifecyclePolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.LifecyclePolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecurityConfigRequest

### type
- **Type**: typing.Literal['iamidentitycenter', 'saml']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### samlOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SamlConfigOptions]

### iamIdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CreateIamIdentityCenterConfigOptions]

### clientToken
- **Type**: typing.Optional[str]


# CreateSecurityConfigResponse

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityConfigDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSecurityPolicyRequest

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# CreateSecurityPolicyResponse

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcEndpointDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# CreateVpcEndpointRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### clientToken
- **Type**: typing.Optional[str]


# CreateVpcEndpointResponse

### createVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CreateVpcEndpointDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAccessPolicyRequest

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteCollectionDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]


# DeleteCollectionRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteCollectionResponse

### deleteCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.DeleteCollectionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLifecyclePolicyRequest

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteSecurityConfigRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteSecurityPolicyRequest

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteVpcEndpointDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# DeleteVpcEndpointRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteVpcEndpointResponse

### deleteVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.DeleteVpcEndpointDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# EffectiveLifecyclePolicyDetail

### type
- **Type**: typing.Optional[typing.Literal['retention']]

### resource
- **Type**: typing.Optional[str]

### policyName
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['index']]

### retentionPeriod
- **Type**: typing.Optional[str]

### noMinRetentionPeriod
- **Type**: typing.Optional[bool]


# EffectiveLifecyclePolicyErrorDetail

### type
- **Type**: typing.Optional[typing.Literal['retention']]

### resource
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]


# GetAccessPolicyRequest

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPolicyResponse

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.AccessPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccountSettingsResponse

### accountSettingsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.AccountSettingsDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetPoliciesStatsResponse

### AccessPolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.AccessPolicyStats'>
- **Required**: Yes

### SecurityPolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityPolicyStats'>
- **Required**: Yes

### SecurityConfigStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityConfigStats'>
- **Required**: Yes

### LifecyclePolicyStats
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.LifecyclePolicyStats'>
- **Required**: Yes

### TotalPolicyCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetSecurityConfigRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSecurityConfigResponse

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityConfigDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetSecurityPolicyRequest

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSecurityPolicyResponse

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
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

### type
- **Type**: typing.Optional[typing.Literal['retention']]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# LifecyclePolicyErrorDetail

### type
- **Type**: typing.Optional[typing.Literal['retention']]

### name
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]


# LifecyclePolicyIdentifier

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# LifecyclePolicyResourceIdentifier

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes


# LifecyclePolicyStats

### RetentionPolicyCount
- **Type**: typing.Optional[int]


# LifecyclePolicySummary

### type
- **Type**: typing.Optional[typing.Literal['retention']]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# ListAccessPoliciesRequest

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### resource
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccessPoliciesResponse

### accessPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.AccessPolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollectionsRequest

### collectionFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CollectionFilters]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollectionsResponse

### collectionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CollectionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLifecyclePoliciesRequest

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### resources
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLifecyclePoliciesResponse

### lifecyclePolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.LifecyclePolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigsRequest

### type
- **Type**: typing.Literal['iamidentitycenter', 'saml']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSecurityConfigsResponse

### securityConfigSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityConfigSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSecurityPoliciesRequest

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### resource
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSecurityPoliciesResponse

### securityPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityPolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcEndpointsRequest

### vpcEndpointFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.VpcEndpointFilters]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListVpcEndpointsResponse

### vpcEndpointSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.VpcEndpointSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
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

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['iamidentitycenter', 'saml']]

### configVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### samlOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SamlConfigOptions]

### iamIdentityCenterOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.IamIdentityCenterConfigOptions]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# SecurityConfigStats

### SamlConfigCount
- **Type**: typing.Optional[int]


# SecurityConfigSummary

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['iamidentitycenter', 'saml']]

### configVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# SecurityPolicyDetail

### type
- **Type**: typing.Optional[typing.Literal['encryption', 'network']]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# SecurityPolicyStats

### EncryptionPolicyCount
- **Type**: typing.Optional[int]

### NetworkPolicyCount
- **Type**: typing.Optional[int]


# SecurityPolicySummary

### type
- **Type**: typing.Optional[typing.Literal['encryption', 'network']]

### name
- **Type**: typing.Optional[str]

### policyVersion
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccessPolicyRequest

### type
- **Type**: typing.Literal['data']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersion
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateAccessPolicyResponse

### accessPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.AccessPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAccountSettingsRequest

### capacityLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.CapacityLimits]


# UpdateAccountSettingsResponse

### accountSettingsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.AccountSettingsDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCollectionDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### type
- **Type**: typing.Optional[typing.Literal['SEARCH', 'TIMESERIES', 'VECTORSEARCH']]

### description
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[int]

### lastModifiedDate
- **Type**: typing.Optional[int]


# UpdateCollectionRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateCollectionResponse

### updateCollectionDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.UpdateCollectionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIamIdentityCenterConfigOptions

### userAttribute
- **Type**: typing.Optional[typing.Literal['Email', 'UserId', 'UserName']]

### groupAttribute
- **Type**: typing.Optional[typing.Literal['GroupId', 'GroupName']]


# UpdateLifecyclePolicyRequest

### type
- **Type**: typing.Literal['retention']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersion
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateLifecyclePolicyResponse

### lifecyclePolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.LifecyclePolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSecurityConfigRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### configVersion
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### samlOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SamlConfigOptions]

### iamIdentityCenterOptionsUpdates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.UpdateIamIdentityCenterConfigOptions]

### clientToken
- **Type**: typing.Optional[str]


# UpdateSecurityConfigResponse

### securityConfigDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityConfigDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSecurityPolicyRequest

### type
- **Type**: typing.Literal['encryption', 'network']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### policyVersion
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateSecurityPolicyResponse

### securityPolicyDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.SecurityPolicyDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVpcEndpointDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### lastModifiedDate
- **Type**: typing.Optional[int]


# UpdateVpcEndpointRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### addSubnetIds
- **Type**: typing.Optional[typing.List[str]]

### removeSubnetIds
- **Type**: typing.Optional[typing.List[str]]

### addSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### removeSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### clientToken
- **Type**: typing.Optional[str]


# UpdateVpcEndpointResponse

### UpdateVpcEndpointDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.UpdateVpcEndpointDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_classes.ResponseMetadata'>
- **Required**: Yes


# VpcEndpointDetail

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### createdDate
- **Type**: typing.Optional[int]

### failureCode
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]


# VpcEndpointErrorDetail

### id
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]


# VpcEndpointFilters

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# VpcEndpointSummary

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


