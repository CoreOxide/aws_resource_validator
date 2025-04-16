# Apigateway Classes

# AccessLogSettings

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Account

### cloudwatchRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### throttleSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettings'>
- **Required**: Yes

### features
- **Type**: typing.List[str]
- **Required**: Yes

### apiKeyVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# ApiKey

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiKeyIds

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# ApiKeys

### warnings
- **Type**: typing.List[str]
- **Required**: Yes

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.ApiKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# ApiStage

### apiId
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]

### throttle
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettings]]


# ApiStageOutput

### apiId
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]

### throttle
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettings]]


# ApiStageUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Authorizer

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Authorizers

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.Authorizer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# BasePathMapping

### basePath
- **Type**: typing.Optional[str]

### restApiId
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[str]


# BasePathMappingResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# BasePathMappings

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.BasePathMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CanarySettings

### percentTraffic
- **Type**: typing.Optional[float]

### deploymentId
- **Type**: typing.Optional[str]

### stageVariableOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### useStageCache
- **Type**: typing.Optional[bool]


# CanarySettingsOutput

### percentTraffic
- **Type**: typing.Optional[float]

### deploymentId
- **Type**: typing.Optional[str]

### stageVariableOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### useStageCache
- **Type**: typing.Optional[bool]


# CanarySettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientCertificate

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


# ClientCertificateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# ClientCertificates

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.ClientCertificate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApiKeyRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.StageKey]]

### customerId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateBasePathMappingRequest

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


# CreateDeploymentRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.DeploymentCanarySettings]

### tracingEnabled
- **Type**: typing.Optional[bool]


# CreateDocumentationPartRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.DocumentationPartLocation'>
- **Required**: Yes

### properties
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDocumentationVersionRequest

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


# CreateDomainNameAccessAssociationRequest

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


# CreateDomainNameRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationUnion]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### securityPolicy
- **Type**: typing.Optional[typing.Literal['TLS_1_0', 'TLS_1_2']]

### mutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.MutualTlsAuthenticationInput]

### ownershipVerificationCertificateArn
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]


# CreateModelRequest

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


# CreateRequestValidatorRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### validateRequestBody
- **Type**: typing.Optional[bool]

### validateRequestParameters
- **Type**: typing.Optional[bool]


# CreateResourceRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### parentId
- **Type**: <class 'str'>
- **Required**: Yes

### pathPart
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRestApiRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationUnion]

### policy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### disableExecuteApiEndpoint
- **Type**: typing.Optional[bool]


# CreateStageRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.CanarySettingsUnion]

### tracingEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateUsagePlanKeyRequest

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes

### keyType
- **Type**: <class 'str'>
- **Required**: Yes


# CreateUsagePlanRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### apiStages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.ApiStageUnion]]

### throttle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.ThrottleSettings]

### quota
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.QuotaSettings]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVpcLinkRequest

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


# DeleteApiKeyRequest

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthorizerRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBasePathMappingRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]


# DeleteClientCertificateRequest

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDocumentationPartRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDocumentationVersionRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameAccessAssociationRequest

### domainNameAccessAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]


# DeleteGatewayResponseRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes


# DeleteIntegrationRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponseRequest

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


# DeleteMethodRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMethodResponseRequest

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


# DeleteModelRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRequestValidatorRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestApiRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStageRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUsagePlanKeyRequest

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUsagePlanRequest

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcLinkRequest

### vpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# Deployment

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentCanarySettings

### percentTraffic
- **Type**: typing.Optional[float]

### stageVariableOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### useStageCache
- **Type**: typing.Optional[bool]


# Deployments

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.Deployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# DocumentationPart

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentationPartIds

### ids
- **Type**: typing.List[str]
- **Required**: Yes

### warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# DocumentationPartLocation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentationParts

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DocumentationPart]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# DocumentationVersion

### version
- **Type**: typing.Optional[str]

### createdDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]


# DocumentationVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# DocumentationVersions

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DocumentationVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# DomainName

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationOutput]

### domainNameStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'PENDING', 'PENDING_CERTIFICATE_REIMPORT', 'PENDING_OWNERSHIP_VERIFICATION', 'UPDATING']]

### domainNameStatusMessage
- **Type**: typing.Optional[str]

### securityPolicy
- **Type**: typing.Optional[typing.Literal['TLS_1_0', 'TLS_1_2']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### mutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.MutualTlsAuthentication]

### ownershipVerificationCertificateArn
- **Type**: typing.Optional[str]

### managementPolicy
- **Type**: typing.Optional[str]

### policy
- **Type**: typing.Optional[str]


# DomainNameAccessAssociation

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


# DomainNameAccessAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# DomainNameAccessAssociations

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DomainNameAccessAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# DomainNameResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.EndpointConfigurationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.MutualTlsAuthentication'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# DomainNames

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.DomainName]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EndpointConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# FlushStageAuthorizersCacheRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# FlushStageCacheRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# GatewayResponse

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


# GatewayResponseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# GatewayResponses

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.GatewayResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateClientCertificateRequest

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetApiKeyRequest

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### includeValue
- **Type**: typing.Optional[bool]


# GetApiKeysRequest

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


# GetApiKeysRequestPaginate

### nameQuery
- **Type**: typing.Optional[str]

### customerId
- **Type**: typing.Optional[str]

### includeValues
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetAuthorizerRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthorizersRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetAuthorizersRequestPaginate

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetBasePathMappingRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]


# GetBasePathMappingsRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetBasePathMappingsRequestPaginate

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetClientCertificateRequest

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetClientCertificatesRequest

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetClientCertificatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetDeploymentRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetDeploymentsRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetDeploymentsRequestPaginate

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetDocumentationPartRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDocumentationVersionRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetDocumentationVersionsRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetDocumentationVersionsRequestPaginate

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetDomainNameAccessAssociationsRequest

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### resourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]


# GetDomainNameRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]


# GetDomainNamesRequest

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### resourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]


# GetDomainNamesRequestPaginate

### resourceOwner
- **Type**: typing.Optional[typing.Literal['OTHER_ACCOUNTS', 'SELF']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetExportRequest

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


# GetGatewayResponseRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes


# GetGatewayResponsesRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetGatewayResponsesRequestPaginate

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetIntegrationRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseRequest

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


# GetMethodRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### httpMethod
- **Type**: <class 'str'>
- **Required**: Yes


# GetMethodResponseRequest

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


# GetModelRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### flatten
- **Type**: typing.Optional[bool]


# GetModelTemplateRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelsRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetModelsRequestPaginate

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetRequestValidatorRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRequestValidatorsRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetRequestValidatorsRequestPaginate

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetResourceRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetResourcesRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### embed
- **Type**: typing.Optional[typing.Sequence[str]]


# GetResourcesRequestPaginate

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### embed
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetRestApiRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestApisRequest

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetRestApisRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetSdkRequest

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


# GetSdkTypesRequest

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetSdkTypesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetStageRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStagesRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: typing.Optional[str]


# GetTagsRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetUsagePlanKeyRequest

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsagePlanKeysRequest

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### nameQuery
- **Type**: typing.Optional[str]


# GetUsagePlanKeysRequestPaginate

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### nameQuery
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetUsagePlanRequest

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUsagePlansRequest

### position
- **Type**: typing.Optional[str]

### keyId
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetUsagePlansRequestPaginate

### keyId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetUsageRequest

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


# GetUsageRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# GetVpcLinkRequest

### vpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcLinksRequest

### position
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# GetVpcLinksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.PaginatorConfig]


# ImportDocumentationPartsRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.Blob'>
- **Required**: Yes

### mode
- **Type**: typing.Optional[typing.Literal['merge', 'overwrite']]

### failOnWarnings
- **Type**: typing.Optional[bool]


# ImportRestApiRequest

### body
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.Blob'>
- **Required**: Yes

### failOnWarnings
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# Integration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntegrationResponse

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


# IntegrationResponseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# Method

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodResponse]]

### methodIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.Integration]

### authorizationScopes
- **Type**: typing.Optional[typing.List[str]]


# MethodResponse

### statusCode
- **Type**: typing.Optional[str]

### responseParameters
- **Type**: typing.Optional[typing.Dict[str, bool]]

### responseModels
- **Type**: typing.Optional[typing.Dict[str, str]]


# MethodResponseExtra

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodResponse]
- **Required**: Yes

### methodIntegration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.Integration'>
- **Required**: Yes

### authorizationScopes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# MethodResponseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# MethodSetting

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


# MethodSnapshot

### authorizationType
- **Type**: typing.Optional[str]

### apiKeyRequired
- **Type**: typing.Optional[bool]


# Model

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Models

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.Model]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# MutualTlsAuthentication

### truststoreUri
- **Type**: typing.Optional[str]

### truststoreVersion
- **Type**: typing.Optional[str]

### truststoreWarnings
- **Type**: typing.Optional[typing.List[str]]


# MutualTlsAuthenticationInput

### truststoreUri
- **Type**: typing.Optional[str]

### truststoreVersion
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PatchOperation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutGatewayResponseRequest

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


# PutIntegrationResponseRequest

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


# PutMethodRequest

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


# PutMethodResponseRequest

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


# PutRestApiRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.Blob'>
- **Required**: Yes

### mode
- **Type**: typing.Optional[typing.Literal['merge', 'overwrite']]

### failOnWarnings
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# QuotaSettings

### limit
- **Type**: typing.Optional[int]

### offset
- **Type**: typing.Optional[int]

### period
- **Type**: typing.Optional[typing.Literal['DAY', 'MONTH', 'WEEK']]


# RejectDomainNameAccessAssociationRequest

### domainNameAccessAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameArn
- **Type**: <class 'str'>
- **Required**: Yes


# RequestValidator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RequestValidators

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.RequestValidator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# Resource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Resources

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.Resource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


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


# RestApi

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RestApis

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.RestApi]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# SdkConfigurationProperty

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


# SdkResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# SdkType

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SdkTypes

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.SdkType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# Stage

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodSetting]]

### variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### documentationVersion
- **Type**: typing.Optional[str]

### accessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.AccessLogSettings]

### canarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigateway_classes.CanarySettingsOutput]

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


# StageKey

### restApiId
- **Type**: typing.Optional[str]

### stageName
- **Type**: typing.Optional[str]


# StageResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigateway_classes.MethodSetting]
- **Required**: Yes

### variables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### accessLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.AccessLogSettings'>
- **Required**: Yes

### canarySettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.CanarySettingsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# Stages

### item
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.Stage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Tags

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# Template

### value
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# TestInvokeAuthorizerRequest

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


# TestInvokeAuthorizerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# TestInvokeMethodRequest

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


# TestInvokeMethodResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# ThrottleSettings

### burstLimit
- **Type**: typing.Optional[int]

### rateLimit
- **Type**: typing.Optional[float]


# TlsConfig

### insecureSkipVerification
- **Type**: typing.Optional[bool]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountRequest

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateApiKeyRequest

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateAuthorizerRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateBasePathMappingRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### basePath
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateClientCertificateRequest

### clientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateDeploymentRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateDocumentationPartRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationPartId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateDocumentationVersionRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### documentationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateDomainNameRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainNameId
- **Type**: typing.Optional[str]

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateGatewayResponseRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### responseType
- **Type**: typing.Literal['ACCESS_DENIED', 'API_CONFIGURATION_ERROR', 'AUTHORIZER_CONFIGURATION_ERROR', 'AUTHORIZER_FAILURE', 'BAD_REQUEST_BODY', 'BAD_REQUEST_PARAMETERS', 'DEFAULT_4XX', 'DEFAULT_5XX', 'EXPIRED_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'INVALID_API_KEY', 'INVALID_SIGNATURE', 'MISSING_AUTHENTICATION_TOKEN', 'QUOTA_EXCEEDED', 'REQUEST_TOO_LARGE', 'RESOURCE_NOT_FOUND', 'THROTTLED', 'UNAUTHORIZED', 'UNSUPPORTED_MEDIA_TYPE', 'WAF_FILTERED']
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateIntegrationRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateIntegrationResponseRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateMethodRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateMethodResponseRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateModelRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### modelName
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateRequestValidatorRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### requestValidatorId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateResourceRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateRestApiRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateStageRequest

### restApiId
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateUsagePlanRequest

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateUsageRequest

### usagePlanId
- **Type**: <class 'str'>
- **Required**: Yes

### keyId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# UpdateVpcLinkRequest

### vpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### patchOperations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigateway_classes.PatchOperation]]


# Usage

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# UsagePlan

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsagePlanKey

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsagePlanKeys

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.UsagePlanKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# UsagePlans

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.UsagePlan]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


# VpcLink

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcLinks

### position
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigateway_classes.VpcLink]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigateway_classes.ResponseMetadata'>
- **Required**: Yes


