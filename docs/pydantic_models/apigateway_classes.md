# Pydantic Models in apigateway_classes

# AccessLogSettingsTypeDef

### format
- **Type**: typing.Optional[str]

### destinationArn
- **Type**: typing.Optional[str]


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


# ApiKeyResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### customerId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stageKeys
- **Type**: typing.List[str]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApiKeyTypeDef

### id
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### customerId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### stageKeys
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# ApiStageExtraOutputTypeDef

### apiId
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]

### throttle
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettingsTypeDef]]


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


# AuthorizerResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['COGNITO_USER_POOLS', 'REQUEST', 'TOKEN']
- **Required**: Yes

### providerARNs
- **Type**: typing.List[str]
- **Required**: Yes

### authType
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerUri
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerCredentials
- **Type**: <class 'str'>
- **Required**: Yes

### identitySource
- **Type**: <class 'str'>
- **Required**: Yes

### identityValidationExpression
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerResultTtlInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthorizerTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['COGNITO_USER_POOLS', 'REQUEST', 'TOKEN']]

### providerARNs
- **Type**: typing.Optional[typing.List[str]]

### authType
- **Type**: typing.Optional[str]

### authorizerUri
- **Type**: typing.Optional[str]

### authorizerCredentials
- **Type**: typing.Optional[str]

### identitySource
- **Type**: typing.Optional[str]

### identityValidationExpression
- **Type**: typing.Optional[str]

### authorizerResultTtlInSeconds
- **Type**: typing.Optional[int]


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


# CreateApiKeyRequestRequestTypeDef

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


# CreateAuthorizerRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['COGNITO_USER_POOLS', 'REQUEST', 'TOKEN']
- **Required**: Yes

### providerARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### authType
- **Type**: typing.Optional[str]

### authorizerUri
- **Type**: typing.Optional[str]

### authorizerCredentials
- **Type**: typing.Optional[str]

### identitySource
- **Type**: typing.Optional[str]

### identityValidationExpression
- **Type**: typing.Optional[str]

### authorizerResultTtlInSeconds
- **Type**: typing.Optional[int]


# CreateBasePathMappingRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]


# CreateDeploymentRequestRequestTypeDef

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


# CreateDocumentationPartRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.DocumentationPartLocationTypeDef'>
- **Required**: Yes

### properties
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDocumentationVersionRequestRequestTypeDef

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


# CreateDomainNameRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### securityPolicy
- **Type**: typing.Optional[typing.Literal['TLS_1_0', 'TLS_1_2']]

### mutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.MutualTlsAuthenticationInputTypeDef]

### ownershipVerificationCertificateArn
- **Type**: typing.Optional[str]


# CreateModelRequestRequestTypeDef

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


# CreateRequestValidatorRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### validateRequestBody
- **Type**: typing.Optional[bool]

### validateRequestParameters
- **Type**: typing.Optional[bool]


# CreateResourceRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### parentId
- **Type**: <class 'str'>
- **Required**: Yes

### pathPart
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRestApiRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationTypeDef]

### policy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### disableExecuteApiEndpoint
- **Type**: typing.Optional[bool]


# CreateStageRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.CanarySettingsTypeDef]

### tracingEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateUsagePlanKeyRequestRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes

### keyType
- **Type**: <class 'str'>
- **Required**: Yes


# CreateUsagePlanRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### apiStages
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.apigateway_classes.ApiStageTypeDef, aws_resource_validator.pydantic_models.apigateway_classes.ApiStageExtraOutputTypeDef]]]

### throttle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettingsTypeDef]

### quota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.QuotaSettingsTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVpcLinkRequestRequestTypeDef

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


# DeleteApiKeyRequestRequestTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthorizerRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBasePathMappingRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClientCertificateRequestRequestTypeDef

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDocumentationPartRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDocumentationVersionRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGatewayResponseRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes


# DeleteIntegrationRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponseRequestRequestTypeDef

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


# DeleteMethodRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMethodResponseRequestRequestTypeDef

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


# DeleteModelRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRequestValidatorRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestApiRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStageRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUsagePlanKeyRequestRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUsagePlanRequestRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcLinkRequestRequestTypeDef

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


# DeploymentResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### apiSummary
- **Type**: typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodSnapshotTypeDef]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeploymentTypeDef

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### apiSummary
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodSnapshotTypeDef]]]


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

### type
- **Type**: typing.Literal['API', 'AUTHORIZER', 'METHOD', 'MODEL', 'PATH_PARAMETER', 'QUERY_PARAMETER', 'REQUEST_BODY', 'REQUEST_HEADER', 'RESOURCE', 'RESPONSE', 'RESPONSE_BODY', 'RESPONSE_HEADER']
- **Required**: Yes

### path
- **Type**: typing.Optional[str]

### method
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# DocumentationPartResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.DocumentationPartLocationTypeDef'>
- **Required**: Yes

### properties
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentationPartTypeDef

### id
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.DocumentationPartLocationTypeDef]

### properties
- **Type**: typing.Optional[str]


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


# DomainNameResponseTypeDef

### domainName
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainNameTypeDef

### domainName
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


# EndpointConfigurationExtraOutputTypeDef

### types
- **Type**: typing.Optional[typing.List[typing.Literal['EDGE', 'PRIVATE', 'REGIONAL']]]

### vpcEndpointIds
- **Type**: typing.Optional[typing.List[str]]


# EndpointConfigurationOutputTypeDef

### types
- **Type**: typing.Optional[typing.List[typing.Literal['EDGE', 'PRIVATE', 'REGIONAL']]]

### vpcEndpointIds
- **Type**: typing.Optional[typing.List[str]]


# EndpointConfigurationTypeDef

### types
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EDGE', 'PRIVATE', 'REGIONAL']]]

### vpcEndpointIds
- **Type**: typing.Optional[typing.Sequence[str]]


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


# FlushStageAuthorizersCacheRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# FlushStageCacheRequestRequestTypeDef

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


# GenerateClientCertificateRequestRequestTypeDef

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetApiKeyRequestRequestTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### includeValue
- **Type**: typing.Optional[bool]


# GetApiKeysRequestGetApiKeysPaginateTypeDef

### nameQuery
- **Type**: typing.Optional[str]

### customerId
- **Type**: typing.Optional[str]

### includeValues
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetApiKeysRequestRequestTypeDef

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


# GetAuthorizerRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthorizersRequestGetAuthorizersPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetAuthorizersRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetBasePathMappingRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes


# GetBasePathMappingsRequestGetBasePathMappingsPaginateTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetBasePathMappingsRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetClientCertificateRequestRequestTypeDef

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetClientCertificatesRequestGetClientCertificatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetClientCertificatesRequestRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetDeploymentRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetDeploymentsRequestGetDeploymentsPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetDeploymentsRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetDocumentationPartRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDocumentationPartsRequestGetDocumentationPartsPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['API', 'AUTHORIZER', 'METHOD', 'MODEL', 'PATH_PARAMETER', 'QUERY_PARAMETER', 'REQUEST_BODY', 'REQUEST_HEADER', 'RESOURCE', 'RESPONSE', 'RESPONSE_BODY', 'RESPONSE_HEADER']]

### nameQuery
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### locationStatus
- **Type**: typing.Optional[typing.Literal['DOCUMENTED', 'UNDOCUMENTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetDocumentationPartsRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['API', 'AUTHORIZER', 'METHOD', 'MODEL', 'PATH_PARAMETER', 'QUERY_PARAMETER', 'REQUEST_BODY', 'REQUEST_HEADER', 'RESOURCE', 'RESPONSE', 'RESPONSE_BODY', 'RESPONSE_HEADER']]

### nameQuery
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### locationStatus
- **Type**: typing.Optional[typing.Literal['DOCUMENTED', 'UNDOCUMENTED']]


# GetDocumentationVersionRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetDocumentationVersionsRequestGetDocumentationVersionsPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetDocumentationVersionsRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetDomainNameRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainNamesRequestGetDomainNamesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetDomainNamesRequestRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetExportRequestRequestTypeDef

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


# GetGatewayResponseRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes


# GetGatewayResponsesRequestGetGatewayResponsesPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetGatewayResponsesRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetIntegrationRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseRequestRequestTypeDef

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


# GetMethodRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# GetMethodResponseRequestRequestTypeDef

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


# GetModelRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### flatten
- **Type**: typing.Optional[bool]


# GetModelTemplateRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelsRequestGetModelsPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetModelsRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetRequestValidatorRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRequestValidatorsRequestGetRequestValidatorsPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetRequestValidatorsRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetResourceRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetResourcesRequestGetResourcesPaginateTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetResourcesRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetRestApiRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestApisRequestGetRestApisPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetRestApisRequestRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetSdkRequestRequestTypeDef

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


# GetSdkTypeRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSdkTypesRequestGetSdkTypesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetSdkTypesRequestRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetStageRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStagesRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]


# GetTagsRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetUsagePlanKeyRequestRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsagePlanKeysRequestGetUsagePlanKeysPaginateTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### nameQuery
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetUsagePlanKeysRequestRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### nameQuery
- **Type**: typing.Optional[str]


# GetUsagePlanRequestRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsagePlansRequestGetUsagePlansPaginateTypeDef

### keyId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetUsagePlansRequestRequestTypeDef

### position
- **Type**: typing.Optional[str]

### keyId
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetUsageRequestGetUsagePaginateTypeDef

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


# GetUsageRequestRequestTypeDef

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


# GetVpcLinkRequestRequestTypeDef

### vpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcLinksRequestGetVpcLinksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfigTypeDef]


# GetVpcLinksRequestRequestTypeDef

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# ImportApiKeysRequestRequestTypeDef

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### format
- **Type**: typing.Literal['csv']
- **Required**: Yes

### failOnWarnings
- **Type**: typing.Optional[bool]


# ImportDocumentationPartsRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### mode
- **Type**: typing.Optional[typing.Literal['merge', 'overwrite']]

### failOnWarnings
- **Type**: typing.Optional[bool]


# ImportRestApiRequestRequestTypeDef

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### failOnWarnings
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# IntegrationExtraResponseTypeDef

### type
- **Type**: typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### connectionType
- **Type**: typing.Literal['INTERNET', 'VPC_LINK']
- **Required**: Yes

### connectionId
- **Type**: <class 'str'>
- **Required**: Yes

### credentials
- **Type**: <class 'str'>
- **Required**: Yes

### requestParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### requestTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### passthroughBehavior
- **Type**: <class 'str'>
- **Required**: Yes

### contentHandling
- **Type**: typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']
- **Required**: Yes

### timeoutInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### cacheNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### cacheKeyParameters
- **Type**: typing.List[str]
- **Required**: Yes

### integrationResponses
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.IntegrationResponseTypeDef]
- **Required**: Yes

### tlsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.TlsConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### type
- **Type**: typing.Optional[typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']]

### httpMethod
- **Type**: typing.Optional[str]

### uri
- **Type**: typing.Optional[str]

### connectionType
- **Type**: typing.Optional[typing.Literal['INTERNET', 'VPC_LINK']]

### connectionId
- **Type**: typing.Optional[str]

### credentials
- **Type**: typing.Optional[str]

### requestParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### requestTemplates
- **Type**: typing.Optional[typing.Dict[str, str]]

### passthroughBehavior
- **Type**: typing.Optional[str]

### contentHandling
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]

### timeoutInMillis
- **Type**: typing.Optional[int]

### cacheNamespace
- **Type**: typing.Optional[str]

### cacheKeyParameters
- **Type**: typing.Optional[typing.List[str]]

### integrationResponses
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.IntegrationResponseTypeDef]]

### tlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.TlsConfigTypeDef]


# MethodExtraResponseTypeDef

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


# ModelResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.apigateway_classes.ModelResponseTypeDef'>>

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModelTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[str]


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

### op
- **Type**: typing.Optional[typing.Literal['add', 'copy', 'move', 'remove', 'replace', 'test']]

### path
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# PutGatewayResponseRequestRequestTypeDef

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


# PutIntegrationRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']
- **Required**: Yes

### integrationHttpMethod
- **Type**: typing.Optional[str]

### uri
- **Type**: typing.Optional[str]

### connectionType
- **Type**: typing.Optional[typing.Literal['INTERNET', 'VPC_LINK']]

### connectionId
- **Type**: typing.Optional[str]

### credentials
- **Type**: typing.Optional[str]

### requestParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### requestTemplates
- **Type**: typing.Optional[typing.Mapping[str, str]]

### passthroughBehavior
- **Type**: typing.Optional[str]

### cacheNamespace
- **Type**: typing.Optional[str]

### cacheKeyParameters
- **Type**: typing.Optional[typing.Sequence[str]]

### contentHandling
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]

### timeoutInMillis
- **Type**: typing.Optional[int]

### tlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.TlsConfigTypeDef]


# PutIntegrationResponseRequestRequestTypeDef

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


# PutMethodRequestRequestTypeDef

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


# PutMethodResponseRequestRequestTypeDef

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


# PutRestApiRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# RequestValidatorResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### validateRequestBody
- **Type**: <class 'bool'>
- **Required**: Yes

### validateRequestParameters
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RequestValidatorTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### validateRequestBody
- **Type**: typing.Optional[bool]

### validateRequestParameters
- **Type**: typing.Optional[bool]


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


# ResourceResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### parentId
- **Type**: <class 'str'>
- **Required**: Yes

### pathPart
- **Type**: <class 'str'>
- **Required**: Yes

### path
- **Type**: <class 'str'>
- **Required**: Yes

### resourceMethods
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceTypeDef

### id
- **Type**: typing.Optional[str]

### parentId
- **Type**: typing.Optional[str]

### pathPart
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### resourceMethods
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodTypeDef]]


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


# RestApiResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### warnings
- **Type**: typing.List[str]
- **Required**: Yes

### binaryMediaTypes
- **Type**: typing.List[str]
- **Required**: Yes

### minimumCompressionSize
- **Type**: <class 'int'>
- **Required**: Yes

### apiKeySource
- **Type**: typing.Literal['AUTHORIZER', 'HEADER']
- **Required**: Yes

### endpointConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationOutputTypeDef'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### disableExecuteApiEndpoint
- **Type**: <class 'bool'>
- **Required**: Yes

### rootResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RestApiTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### version
- **Type**: typing.Optional[str]

### warnings
- **Type**: typing.Optional[typing.List[str]]

### binaryMediaTypes
- **Type**: typing.Optional[typing.List[str]]

### minimumCompressionSize
- **Type**: typing.Optional[int]

### apiKeySource
- **Type**: typing.Optional[typing.Literal['AUTHORIZER', 'HEADER']]

### endpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationOutputTypeDef]

### policy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### disableExecuteApiEndpoint
- **Type**: typing.Optional[bool]

### rootResourceId
- **Type**: typing.Optional[str]


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


# SdkTypeResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### friendlyName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### configurationProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.SdkConfigurationPropertyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SdkTypeTypeDef

### id
- **Type**: typing.Optional[str]

### friendlyName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### configurationProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apigateway_classes.SdkConfigurationPropertyTypeDef]]


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


# TagResourceRequestRequestTypeDef

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


# TestInvokeAuthorizerRequestRequestTypeDef

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


# TestInvokeMethodRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountRequestRequestTypeDef

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateApiKeyRequestRequestTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateAuthorizerRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateBasePathMappingRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateClientCertificateRequestRequestTypeDef

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateDeploymentRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateDocumentationPartRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateDocumentationVersionRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateDomainNameRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateGatewayResponseRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateIntegrationRequestRequestTypeDef

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


# UpdateIntegrationResponseRequestRequestTypeDef

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


# UpdateMethodRequestRequestTypeDef

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


# UpdateMethodResponseRequestRequestTypeDef

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


# UpdateModelRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateRequestValidatorRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateResourceRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateRestApiRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateStageRequestRequestTypeDef

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateUsagePlanRequestRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateUsageRequestRequestTypeDef

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UpdateVpcLinkRequestRequestTypeDef

### vpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperationTypeDef]]


# UsagePlanKeyResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsagePlanKeyTypeDef

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


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


# UsagePlanResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### apiStages
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.ApiStageOutputTypeDef]
- **Required**: Yes

### throttle
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettingsTypeDef'>
- **Required**: Yes

### quota
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.QuotaSettingsTypeDef'>
- **Required**: Yes

### productCode
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsagePlanTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### apiStages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apigateway_classes.ApiStageOutputTypeDef]]

### throttle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettingsTypeDef]

### quota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.QuotaSettingsTypeDef]

### productCode
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# VpcLinkResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### targetArns
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcLinkTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### targetArns
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'FAILED', 'PENDING']]

### statusMessage
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


