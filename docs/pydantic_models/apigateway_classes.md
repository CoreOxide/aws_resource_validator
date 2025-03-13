# Apigateway Classes

# AccessLogSettingsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccountTypeDef

### cloudwatchRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### throttleSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettingsTypeDef'>
- **Required**: Yes

### features
- **Type**: typing.List[str]
- **Required**: Yes

### apiKeyVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApiKeyIdsTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApiKeyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiKeysTypeDef

### warnings
- **Type**: typing.List[str]
- **Required**: Yes

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.ApiKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApiStageOutputTypeDef

### apiId
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]

### throttle
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettingsTypeDef]]


# ApiStageTypeDef

### apiId
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]

### throttle
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettingsTypeDef]]


# ApiStageUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuthorizerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuthorizersTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.AuthorizerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BasePathMappingResponseTypeDef

### basePath
- **Type**: <class 'str'>
- **Required**: Yes

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BasePathMappingTypeDef

### basePath
- **Type**: typing.Optional[str]

### restApiId
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]


# BasePathMappingsTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.BasePathMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CanarySettingsOutputTypeDef

### percentTraffic
- **Type**: typing.Optional[float]

### deploymentId
- **Type**: typing.Optional[str]

### stageVariableOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### useStageCache
- **Type**: typing.Optional[bool]


# CanarySettingsTypeDef

### percentTraffic
- **Type**: typing.Optional[float]

### deploymentId
- **Type**: typing.Optional[str]

### stageVariableOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### useStageCache
- **Type**: typing.Optional[bool]


# CanarySettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientCertificateResponseTypeDef

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### pemEncodedCertificate
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expirationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ClientCertificateTypeDef

### clientCertificateId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### pemEncodedCertificate
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### expirationDate
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ClientCertificatesTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.ClientCertificateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApiKeyRequestTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### generateDistinctId
- **Type**: typing.Optional[bool]

### value
- **Type**: typing.Optional[str]

### stageKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.StageKeyTypeDef]]

### customerId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateBasePathMappingRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### basePath
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]


# CreateDeploymentRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: typing.Optional[str]

### stageDescription
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### cacheClusterEnabled
- **Type**: typing.Optional[bool]

### cacheClusterSize
- **Type**: typing.Optional[typing.Literal['0.5', '1.6', '118', '13.5', '237', '28.4', '58.2', '6.1']]

### variables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### canarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.DeploymentCanarySettingsTypeDef]

### tracingEnabled
- **Type**: typing.Optional[bool]


# CreateDocumentationPartRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.DocumentationPartLocationTypeDef'>
- **Required**: Yes

### properties
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDocumentationVersionRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateDomainNameAccessAssociationRequestTypeDef

### domainNameArn
- **Type**: <class 'str'>
- **Required**: Yes

### accessAssociationSourceType
- **Type**: typing.Literal['VPCE']
- **Required**: Yes

### accessAssociationSource
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDomainNameRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: typing.Optional[str]

### certificateBody
- **Type**: typing.Optional[str]

### certificatePrivateKey
- **Type**: typing.Optional[str]

### certificateChain
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### regionalCertificateName
- **Type**: typing.Optional[str]

### regionalCertificateArn
- **Type**: typing.Optional[str]

### endpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### securityPolicy
- **Type**: typing.Optional[typing.Literal['TLS_1_0', 'TLS_1_2']]

### mutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.MutualTlsAuthenticationInputTypeDef]

### ownershipVerificationCertificateArn
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]


# CreateModelRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]


# CreateRequestValidatorRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### validateRequestBody
- **Type**: typing.Optional[bool]

### validateRequestParameters
- **Type**: typing.Optional[bool]


# CreateResourceRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### parentId
- **Type**: <class 'str'>
- **Required**: Yes

### pathPart
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRestApiRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### cloneFrom
- **Type**: typing.Optional[str]

### binaryMediaTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### minimumCompressionSize
- **Type**: typing.Optional[int]

### apiKeySource
- **Type**: typing.Optional[typing.Literal['AUTHORIZER', 'HEADER']]

### endpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationUnionTypeDef]

### policy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### disableExecuteApiEndpoint
- **Type**: typing.Optional[bool]


# CreateStageRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### cacheClusterEnabled
- **Type**: typing.Optional[bool]

### cacheClusterSize
- **Type**: typing.Optional[typing.Literal['0.5', '1.6', '118', '13.5', '237', '28.4', '58.2', '6.1']]

### variables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### documentationVersion
- **Type**: typing.Optional[str]

### canarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.CanarySettingsUnionTypeDef]

### tracingEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateUsagePlanKeyRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes

### keyType
- **Type**: <class 'str'>
- **Required**: Yes


# CreateUsagePlanRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### apiStages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.ApiStageUnionTypeDef]]

### throttle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettingsTypeDef]

### quota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.QuotaSettingsTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVpcLinkRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### targetArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DeleteApiKeyRequestTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthorizerRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBasePathMappingRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]


# DeleteClientCertificateRequestTypeDef

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDocumentationPartRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDocumentationVersionRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameAccessAssociationRequestTypeDef

### domainNameAccessAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]


# DeleteGatewayResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes


# DeleteIntegrationRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMethodRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMethodResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRequestValidatorRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestApiRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStageRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUsagePlanKeyRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUsagePlanRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcLinkRequestTypeDef

### vpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentCanarySettingsTypeDef

### percentTraffic
- **Type**: typing.Optional[float]

### stageVariableOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### useStageCache
- **Type**: typing.Optional[bool]


# DeploymentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentsTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DeploymentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentationPartIdsTypeDef

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentationPartLocationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentationPartTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentationPartsTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DocumentationPartTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentationVersionResponseTypeDef

### version
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentationVersionTypeDef

### version
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]


# DocumentationVersionsTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DocumentationVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainNameAccessAssociationResponseTypeDef

### domainNameAccessAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameArn
- **Type**: <class 'str'>
- **Required**: Yes

### accessAssociationSourceType
- **Type**: typing.Literal['VPCE']
- **Required**: Yes

### accessAssociationSource
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainNameAccessAssociationTypeDef

### domainNameAccessAssociationArn
- **Type**: typing.Optional[str]

### domainNameArn
- **Type**: typing.Optional[str]

### accessAssociationSourceType
- **Type**: typing.Optional[typing.Literal['VPCE']]

### accessAssociationSource
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DomainNameAccessAssociationsTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DomainNameAccessAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainNameResponseTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificateUploadDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### regionalDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### regionalHostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### regionalCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### regionalCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### distributionDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### distributionHostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### endpointConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationOutputTypeDef'>
- **Required**: Yes

### domainNameStatus
- **Type**: typing.Literal['AVAILABLE', 'PENDING', 'PENDING_CERTIFICATE_REIMPORT', 'PENDING_OWNERSHIP_VERIFICATION', 'UPDATING']
- **Required**: Yes

### domainNameStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### securityPolicy
- **Type**: typing.Literal['TLS_1_0', 'TLS_1_2']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### mutualTlsAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.MutualTlsAuthenticationTypeDef'>
- **Required**: Yes

### ownershipVerificationCertificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### managementPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainNameTypeDef

### domainName
- **Type**: typing.Optional[str]

### domainNameId
- **Type**: typing.Optional[str]

### domainNameArn
- **Type**: typing.Optional[str]

### certificateName
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### certificateUploadDate
- **Type**: typing.Optional[datetime.datetime]

### regionalDomainName
- **Type**: typing.Optional[str]

### regionalHostedZoneId
- **Type**: typing.Optional[str]

### regionalCertificateName
- **Type**: typing.Optional[str]

### regionalCertificateArn
- **Type**: typing.Optional[str]

### distributionDomainName
- **Type**: typing.Optional[str]

### distributionHostedZoneId
- **Type**: typing.Optional[str]

### endpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationOutputTypeDef]

### domainNameStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'PENDING', 'PENDING_CERTIFICATE_REIMPORT', 'PENDING_OWNERSHIP_VERIFICATION', 'UPDATING']]

### domainNameStatusMessage
- **Type**: typing.Optional[str]

### securityPolicy
- **Type**: typing.Optional[typing.Literal['TLS_1_0', 'TLS_1_2']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### mutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.MutualTlsAuthenticationTypeDef]

### ownershipVerificationCertificateArn
- **Type**: typing.Optional[str]

### managementPolicy
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]


# DomainNamesTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DomainNameTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EndpointConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExportResponseTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### contentDisposition
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FlushStageAuthorizersCacheRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# FlushStageCacheRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# GatewayResponseResponseTypeDef

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### responseParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### responseTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### defaultResponse
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GatewayResponseTypeDef

### responseType
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']]

### statusCode
- **Type**: typing.Optional[str]

### responseParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### responseTemplates
- **Type**: typing.Optional[typing.Dict[str, str]]

### defaultResponse
- **Type**: typing.Optional[bool]


# GatewayResponsesTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.GatewayResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateClientCertificateRequestTypeDef

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetApiKeyRequestTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### includeValue
- **Type**: typing.Optional[bool]


# GetApiKeysRequestPaginateTypeDef

### nameQuery
- **Type**: typing.Optional[str]

### customerId
- **Type**: typing.Optional[str]

### includeValues
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetApiKeysRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### nameQuery
- **Type**: typing.Optional[str]

### customerId
- **Type**: typing.Optional[str]

### includeValues
- **Type**: typing.Optional[bool]


# GetAuthorizerRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthorizersRequestPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetAuthorizersRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetBasePathMappingRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]


# GetBasePathMappingsRequestPaginateTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetBasePathMappingsRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetClientCertificateRequestTypeDef

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetClientCertificatesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetClientCertificatesRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetDeploymentRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetDeploymentsRequestPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetDeploymentsRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetDocumentationPartRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDocumentationVersionRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetDocumentationVersionsRequestPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetDocumentationVersionsRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetDomainNameAccessAssociationsRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### resourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]


# GetDomainNameRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]


# GetDomainNamesRequestPaginateTypeDef

### resourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetDomainNamesRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### resourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]


# GetExportRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### exportType
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### accepts
- **Type**: typing.Optional[str]


# GetGatewayResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes


# GetGatewayResponsesRequestPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetGatewayResponsesRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetIntegrationRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes


# GetMethodRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# GetMethodResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### flatten
- **Type**: typing.Optional[bool]


# GetModelTemplateRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelsRequestPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetModelsRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetRequestValidatorRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRequestValidatorsRequestPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetRequestValidatorsRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetResourceRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetResourcesRequestPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetResourcesRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetRestApiRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestApisRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetRestApisRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetSdkRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### sdkType
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetSdkTypesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetSdkTypesRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetStageRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStagesRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]


# GetTagsRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetUsagePlanKeyRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsagePlanKeysRequestPaginateTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### nameQuery
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetUsagePlanKeysRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### nameQuery
- **Type**: typing.Optional[str]


# GetUsagePlanRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsagePlansRequestPaginateTypeDef

### keyId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetUsagePlansRequestTypeDef

### position
- **Type**: typing.Optional[str]

### keyId
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetUsageRequestPaginateTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'str'>
- **Required**: Yes

### endDate
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetUsageRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'str'>
- **Required**: Yes

### endDate
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetVpcLinkRequestTypeDef

### vpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcLinksRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetVpcLinksRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# ImportDocumentationPartsRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.BlobTypeDef'>
- **Required**: Yes

### mode
- **Type**: typing.Optional[typing.Literal['merge', 'overwrite']]

### failOnWarnings
- **Type**: typing.Optional[bool]


# ImportRestApiRequestTypeDef

### body
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.BlobTypeDef'>
- **Required**: Yes

### failOnWarnings
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# IntegrationResponseResponseTypeDef

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### selectionPattern
- **Type**: <class 'str'>
- **Required**: Yes

### responseParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### responseTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### contentHandling
- **Type**: typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IntegrationResponseTypeDef

### statusCode
- **Type**: typing.Optional[str]

### selectionPattern
- **Type**: typing.Optional[str]

### responseParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### responseTemplates
- **Type**: typing.Optional[typing.Dict[str, str]]

### contentHandling
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]


# IntegrationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MethodResponseExtraTypeDef

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### authorizationType
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### apiKeyRequired
- **Type**: <class 'bool'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes

### operationName
- **Type**: <class 'str'>
- **Required**: Yes

### requestParameters
- **Type**: typing.Dict[str, bool]
- **Required**: Yes

### requestModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### methodResponses
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodResponseTypeDef]
- **Required**: Yes

### methodIntegration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.IntegrationTypeDef'>
- **Required**: Yes

### authorizationScopes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MethodResponseResponseTypeDef

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### responseParameters
- **Type**: typing.Dict[str, bool]
- **Required**: Yes

### responseModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MethodResponseTypeDef

### statusCode
- **Type**: typing.Optional[str]

### responseParameters
- **Type**: typing.Optional[typing.Dict[str, bool]]

### responseModels
- **Type**: typing.Optional[typing.Dict[str, str]]


# MethodSettingTypeDef

### metricsEnabled
- **Type**: typing.Optional[bool]

### loggingLevel
- **Type**: typing.Optional[str]

### dataTraceEnabled
- **Type**: typing.Optional[bool]

### throttlingBurstLimit
- **Type**: typing.Optional[int]

### throttlingRateLimit
- **Type**: typing.Optional[float]

### cachingEnabled
- **Type**: typing.Optional[bool]

### cacheTtlInSeconds
- **Type**: typing.Optional[int]

### cacheDataEncrypted
- **Type**: typing.Optional[bool]

### requireAuthorizationForCacheControl
- **Type**: typing.Optional[bool]

### unauthorizedCacheControlHeaderStrategy
- **Type**: typing.Optional[typing.Literal['FAIL_WITH_403', 'SUCCEED_WITHOUT_RESPONSE_HEADER', 'SUCCEED_WITH_RESPONSE_HEADER']]


# MethodSnapshotTypeDef

### authorizationType
- **Type**: typing.Optional[str]

### apiKeyRequired
- **Type**: typing.Optional[bool]


# MethodTypeDef

### httpMethod
- **Type**: typing.Optional[str]

### authorizationType
- **Type**: typing.Optional[str]

### authorizerId
- **Type**: typing.Optional[str]

### apiKeyRequired
- **Type**: typing.Optional[bool]

### requestValidatorId
- **Type**: typing.Optional[str]

### operationName
- **Type**: typing.Optional[str]

### requestParameters
- **Type**: typing.Optional[typing.Dict[str, bool]]

### requestModels
- **Type**: typing.Optional[typing.Dict[str, str]]

### methodResponses
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodResponseTypeDef]]

### methodIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.IntegrationTypeDef]

### authorizationScopes
- **Type**: typing.Optional[typing.List[str]]


# ModelTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelsTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.ModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MutualTlsAuthenticationInputTypeDef

### truststoreUri
- **Type**: typing.Optional[str]

### truststoreVersion
- **Type**: typing.Optional[str]


# MutualTlsAuthenticationTypeDef

### truststoreUri
- **Type**: typing.Optional[str]

### truststoreVersion
- **Type**: typing.Optional[str]

### truststoreWarnings
- **Type**: typing.Optional[typing.List[str]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PatchOperationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutGatewayResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes

### statusCode
- **Type**: typing.Optional[str]

### responseParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### responseTemplates
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutIntegrationResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### selectionPattern
- **Type**: typing.Optional[str]

### responseParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### responseTemplates
- **Type**: typing.Optional[typing.Mapping[str, str]]

### contentHandling
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]


# PutMethodRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### authorizationType
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: typing.Optional[str]

### apiKeyRequired
- **Type**: typing.Optional[bool]

### operationName
- **Type**: typing.Optional[str]

### requestParameters
- **Type**: typing.Optional[typing.Mapping[str, bool]]

### requestModels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### requestValidatorId
- **Type**: typing.Optional[str]

### authorizationScopes
- **Type**: typing.Optional[typing.Sequence[str]]


# PutMethodResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### responseParameters
- **Type**: typing.Optional[typing.Mapping[str, bool]]

### responseModels
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutRestApiRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.BlobTypeDef'>
- **Required**: Yes

### mode
- **Type**: typing.Optional[typing.Literal['merge', 'overwrite']]

### failOnWarnings
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# QuotaSettingsTypeDef

### limit
- **Type**: typing.Optional[int]

### offset
- **Type**: typing.Optional[int]

### period
- **Type**: typing.Optional[typing.Literal['DAY', 'MONTH', 'WEEK']]


# RejectDomainNameAccessAssociationRequestTypeDef

### domainNameAccessAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameArn
- **Type**: <class 'str'>
- **Required**: Yes


# RequestValidatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RequestValidatorsTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.RequestValidatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourcesTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.ResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RestApiTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RestApisTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.RestApiTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SdkConfigurationPropertyTypeDef

### name
- **Type**: typing.Optional[str]

### friendlyName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]

### defaultValue
- **Type**: typing.Optional[str]


# SdkResponseTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### contentDisposition
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SdkTypeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SdkTypesTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.SdkTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StageKeyTypeDef

### restApiId
- **Type**: typing.Optional[str]

### stageName
- **Type**: typing.Optional[str]


# StageResponseTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### cacheClusterEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### cacheClusterSize
- **Type**: typing.Literal['0.5', '1.6', '118', '13.5', '237', '28.4', '58.2', '6.1']
- **Required**: Yes

### cacheClusterStatus
- **Type**: typing.Literal['AVAILABLE', 'CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'FLUSH_IN_PROGRESS', 'NOT_AVAILABLE']
- **Required**: Yes

### methodSettings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodSettingTypeDef]
- **Required**: Yes

### variables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### accessLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.AccessLogSettingsTypeDef'>
- **Required**: Yes

### canarySettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.CanarySettingsOutputTypeDef'>
- **Required**: Yes

### tracingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### webAclArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StageTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### clientCertificateId
- **Type**: typing.Optional[str]

### stageName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### cacheClusterEnabled
- **Type**: typing.Optional[bool]

### cacheClusterSize
- **Type**: typing.Optional[typing.Literal['0.5', '1.6', '118', '13.5', '237', '28.4', '58.2', '6.1']]

### cacheClusterStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'FLUSH_IN_PROGRESS', 'NOT_AVAILABLE']]

### methodSettings
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodSettingTypeDef]]

### variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### documentationVersion
- **Type**: typing.Optional[str]

### accessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.AccessLogSettingsTypeDef]

### canarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.CanarySettingsOutputTypeDef]

### tracingEnabled
- **Type**: typing.Optional[bool]

### webAclArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]


# StagesTypeDef

### item
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.StageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagsTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TemplateTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TestInvokeAuthorizerRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### headers
- **Type**: typing.Optional[typing.Mapping[str, str]]

### multiValueHeaders
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### pathWithQueryString
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]

### stageVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### additionalContext
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TestInvokeAuthorizerResponseTypeDef

### clientStatus
- **Type**: <class 'int'>
- **Required**: Yes

### log
- **Type**: <class 'str'>
- **Required**: Yes

### latency
- **Type**: <class 'int'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### authorization
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### claims
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TestInvokeMethodRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### pathWithQueryString
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[typing.Mapping[str, str]]

### multiValueHeaders
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### clientCertificateId
- **Type**: typing.Optional[str]

### stageVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TestInvokeMethodResponseTypeDef

### status
- **Type**: <class 'int'>
- **Required**: Yes

### body
- **Type**: <class 'str'>
- **Required**: Yes

### headers
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### multiValueHeaders
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### log
- **Type**: <class 'str'>
- **Required**: Yes

### latency
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ThrottleSettingsTypeDef

### burstLimit
- **Type**: typing.Optional[int]

### rateLimit
- **Type**: typing.Optional[float]


# TlsConfigTypeDef

### insecureSkipVerification
- **Type**: typing.Optional[bool]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountRequestTypeDef

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateApiKeyRequestTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateAuthorizerRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateBasePathMappingRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateClientCertificateRequestTypeDef

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateDeploymentRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateDocumentationPartRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateDocumentationVersionRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateDomainNameRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateGatewayResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateIntegrationRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateIntegrationResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateMethodRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateMethodResponseRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### statusCode
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateModelRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateRequestValidatorRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateResourceRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateRestApiRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateStageRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateUsagePlanRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateUsageRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateVpcLinkRequestTypeDef

### vpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UsagePlanKeyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsagePlanKeysTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.UsagePlanKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsagePlanTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsagePlansTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.UsagePlanTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'str'>
- **Required**: Yes

### endDate
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.Dict[str, typing.List[typing.List[int]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcLinkTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcLinksTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.VpcLinkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


