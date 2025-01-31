# apigatewayv2_classes

# AccessLogSettingsTypeDef

### DestinationArn
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[str]


# ApiMappingTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingId
- **Type**: typing.Optional[str]

### ApiMappingKey
- **Type**: typing.Optional[str]


# ApiPaginatorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### RouteSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ApiEndpoint
- **Type**: typing.Optional[str]

### ApiGatewayManaged
- **Type**: typing.Optional[bool]

### ApiId
- **Type**: typing.Optional[str]

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsPaginatorTypeDef]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### DisableSchemaValidation
- **Type**: typing.Optional[bool]

### DisableExecuteApiEndpoint
- **Type**: typing.Optional[bool]

### ImportInfo
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Version
- **Type**: typing.Optional[str]

### Warnings
- **Type**: typing.Optional[typing.List[str]]


# ApiTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### RouteSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ApiEndpoint
- **Type**: typing.Optional[str]

### ApiGatewayManaged
- **Type**: typing.Optional[bool]

### ApiId
- **Type**: typing.Optional[str]

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsTypeDef]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### DisableSchemaValidation
- **Type**: typing.Optional[bool]

### DisableExecuteApiEndpoint
- **Type**: typing.Optional[bool]

### ImportInfo
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Version
- **Type**: typing.Optional[str]

### Warnings
- **Type**: typing.Optional[typing.List[str]]


# AuthorizerPaginatorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerCredentialsArn
- **Type**: typing.Optional[str]

### AuthorizerId
- **Type**: typing.Optional[str]

### AuthorizerPayloadFormatVersion
- **Type**: typing.Optional[str]

### AuthorizerResultTtlInSeconds
- **Type**: typing.Optional[int]

### AuthorizerType
- **Type**: typing.Optional[typing.Literal['JWT', 'REQUEST']]

### AuthorizerUri
- **Type**: typing.Optional[str]

### EnableSimpleResponses
- **Type**: typing.Optional[bool]

### IdentitySource
- **Type**: typing.Optional[typing.List[str]]

### IdentityValidationExpression
- **Type**: typing.Optional[str]

### JwtConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationPaginatorTypeDef]


# AuthorizerTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerCredentialsArn
- **Type**: typing.Optional[str]

### AuthorizerId
- **Type**: typing.Optional[str]

### AuthorizerPayloadFormatVersion
- **Type**: typing.Optional[str]

### AuthorizerResultTtlInSeconds
- **Type**: typing.Optional[int]

### AuthorizerType
- **Type**: typing.Optional[typing.Literal['JWT', 'REQUEST']]

### AuthorizerUri
- **Type**: typing.Optional[str]

### EnableSimpleResponses
- **Type**: typing.Optional[bool]

### IdentitySource
- **Type**: typing.Optional[typing.List[str]]

### IdentityValidationExpression
- **Type**: typing.Optional[str]

### JwtConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CorsPaginatorTypeDef

### AllowCredentials
- **Type**: typing.Optional[bool]

### AllowHeaders
- **Type**: typing.Optional[typing.List[str]]

### AllowMethods
- **Type**: typing.Optional[typing.List[str]]

### AllowOrigins
- **Type**: typing.Optional[typing.List[str]]

### ExposeHeaders
- **Type**: typing.Optional[typing.List[str]]

### MaxAge
- **Type**: typing.Optional[int]


# CorsTypeDef

### AllowCredentials
- **Type**: typing.Optional[bool]

### AllowHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowMethods
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowOrigins
- **Type**: typing.Optional[typing.Sequence[str]]

### ExposeHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxAge
- **Type**: typing.Optional[int]


# CreateApiMappingRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingKey
- **Type**: typing.Optional[str]


# CreateApiMappingResponseTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingKey
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApiRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsTypeDef]

### CredentialsArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisableSchemaValidation
- **Type**: typing.Optional[bool]

### DisableExecuteApiEndpoint
- **Type**: typing.Optional[bool]

### RouteKey
- **Type**: typing.Optional[str]

### RouteSelectionExpression
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Target
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# CreateApiResponseTypeDef

### ApiEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### CorsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsTypeDef'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DisableSchemaValidation
- **Type**: <class 'bool'>
- **Required**: Yes

### DisableExecuteApiEndpoint
- **Type**: <class 'bool'>
- **Required**: Yes

### ImportInfo
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### RouteSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAuthorizerRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerType
- **Type**: typing.Literal['JWT', 'REQUEST']
- **Required**: Yes

### IdentitySource
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerCredentialsArn
- **Type**: typing.Optional[str]

### AuthorizerPayloadFormatVersion
- **Type**: typing.Optional[str]

### AuthorizerResultTtlInSeconds
- **Type**: typing.Optional[int]

### AuthorizerUri
- **Type**: typing.Optional[str]

### EnableSimpleResponses
- **Type**: typing.Optional[bool]

### IdentityValidationExpression
- **Type**: typing.Optional[str]

### JwtConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationTypeDef]


# CreateAuthorizerResponseTypeDef

### AuthorizerCredentialsArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerPayloadFormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerResultTtlInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### AuthorizerType
- **Type**: typing.Literal['JWT', 'REQUEST']
- **Required**: Yes

### AuthorizerUri
- **Type**: <class 'str'>
- **Required**: Yes

### EnableSimpleResponses
- **Type**: <class 'bool'>
- **Required**: Yes

### IdentitySource
- **Type**: typing.List[str]
- **Required**: Yes

### IdentityValidationExpression
- **Type**: <class 'str'>
- **Required**: Yes

### JwtConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]


# CreateDeploymentResponseTypeDef

### AutoDeployed
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentStatus
- **Type**: typing.Literal['DEPLOYED', 'FAILED', 'PENDING']
- **Required**: Yes

### DeploymentStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainNameRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationTypeDef]]

### MutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.MutualTlsAuthenticationInputTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDomainNameResponseTypeDef

### ApiMappingSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationTypeDef]
- **Required**: Yes

### MutualTlsAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.MutualTlsAuthenticationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationType
- **Type**: typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']
- **Required**: Yes

### ConnectionId
- **Type**: typing.Optional[str]

### ConnectionType
- **Type**: typing.Optional[typing.Literal['INTERNET', 'VPC_LINK']]

### ContentHandlingStrategy
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]

### CredentialsArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IntegrationMethod
- **Type**: typing.Optional[str]

### IntegrationSubtype
- **Type**: typing.Optional[str]

### IntegrationUri
- **Type**: typing.Optional[str]

### PassthroughBehavior
- **Type**: typing.Optional[typing.Literal['NEVER', 'WHEN_NO_MATCH', 'WHEN_NO_TEMPLATES']]

### PayloadFormatVersion
- **Type**: typing.Optional[str]

### RequestParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestTemplates
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]

### TemplateSelectionExpression
- **Type**: typing.Optional[str]

### TimeoutInMillis
- **Type**: typing.Optional[int]

### TlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.TlsConfigInputTypeDef]


# CreateIntegrationResponseRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ContentHandlingStrategy
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]

### ResponseParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ResponseTemplates
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateSelectionExpression
- **Type**: typing.Optional[str]


# CreateIntegrationResponseResponseTypeDef

### ContentHandlingStrategy
- **Type**: typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TemplateSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationResultTypeDef

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: typing.Literal['INTERNET', 'VPC_LINK']
- **Required**: Yes

### ContentHandlingStrategy
- **Type**: typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']
- **Required**: Yes

### CredentialsArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationMethod
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationSubtype
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationType
- **Type**: typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']
- **Required**: Yes

### IntegrationUri
- **Type**: <class 'str'>
- **Required**: Yes

### PassthroughBehavior
- **Type**: typing.Literal['NEVER', 'WHEN_NO_MATCH', 'WHEN_NO_TEMPLATES']
- **Required**: Yes

### PayloadFormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RequestParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RequestTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### TemplateSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### TlsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.TlsConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CreateModelResponseTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRouteRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeyRequired
- **Type**: typing.Optional[bool]

### AuthorizationScopes
- **Type**: typing.Optional[typing.Sequence[str]]

### AuthorizationType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'CUSTOM', 'JWT', 'NONE']]

### AuthorizerId
- **Type**: typing.Optional[str]

### ModelSelectionExpression
- **Type**: typing.Optional[str]

### OperationName
- **Type**: typing.Optional[str]

### RequestModels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]]

### RouteResponseSelectionExpression
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# CreateRouteResponseRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSelectionExpression
- **Type**: typing.Optional[str]

### ResponseModels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]]


# CreateRouteResponseResponseTypeDef

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRouteResultTypeDef

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ApiKeyRequired
- **Type**: <class 'bool'>
- **Required**: Yes

### AuthorizationScopes
- **Type**: typing.List[str]
- **Required**: Yes

### AuthorizationType
- **Type**: typing.Literal['AWS_IAM', 'CUSTOM', 'JWT', 'NONE']
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### OperationName
- **Type**: <class 'str'>
- **Required**: Yes

### RequestModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RequestParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStageRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.AccessLogSettingsTypeDef]

### AutoDeploy
- **Type**: typing.Optional[bool]

### ClientCertificateId
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]

### DeploymentId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]]

### StageVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStageResponseTypeDef

### AccessLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.AccessLogSettingsTypeDef'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoDeploy
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultRouteSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastDeploymentStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RouteSettings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### StageVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcLinkRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVpcLinkResponseTypeDef

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcLinkStatus
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'FAILED', 'INACTIVE', 'PENDING']
- **Required**: Yes

### VpcLinkStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VpcLinkVersion
- **Type**: typing.Literal['V2']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAccessLogSettingsRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiMappingRequestRequestTypeDef

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthorizerRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCorsConfigurationRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponseRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteRequestParameterRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestParameterKey
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteResponseRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteSettingsRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStageRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcLinkRequestRequestTypeDef

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentTypeDef

### AutoDeployed
- **Type**: typing.Optional[bool]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### DeploymentId
- **Type**: typing.Optional[str]

### DeploymentStatus
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'FAILED', 'PENDING']]

### DeploymentStatusMessage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# DomainNameConfigurationPaginatorTypeDef

### ApiGatewayDomainName
- **Type**: typing.Optional[str]

### CertificateArn
- **Type**: typing.Optional[str]

### CertificateName
- **Type**: typing.Optional[str]

### CertificateUploadDate
- **Type**: typing.Optional[datetime.datetime]

### DomainNameStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'PENDING_CERTIFICATE_REIMPORT', 'PENDING_OWNERSHIP_VERIFICATION', 'UPDATING']]

### DomainNameStatusMessage
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[typing.Literal['EDGE', 'REGIONAL']]

### HostedZoneId
- **Type**: typing.Optional[str]

### SecurityPolicy
- **Type**: typing.Optional[typing.Literal['TLS_1_0', 'TLS_1_2']]

### OwnershipVerificationCertificateArn
- **Type**: typing.Optional[str]


# DomainNameConfigurationTypeDef

### ApiGatewayDomainName
- **Type**: typing.Optional[str]

### CertificateArn
- **Type**: typing.Optional[str]

### CertificateName
- **Type**: typing.Optional[str]

### CertificateUploadDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DomainNameStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'PENDING_CERTIFICATE_REIMPORT', 'PENDING_OWNERSHIP_VERIFICATION', 'UPDATING']]

### DomainNameStatusMessage
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[typing.Literal['EDGE', 'REGIONAL']]

### HostedZoneId
- **Type**: typing.Optional[str]

### SecurityPolicy
- **Type**: typing.Optional[typing.Literal['TLS_1_0', 'TLS_1_2']]

### OwnershipVerificationCertificateArn
- **Type**: typing.Optional[str]


# DomainNamePaginatorTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingSelectionExpression
- **Type**: typing.Optional[str]

### DomainNameConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationPaginatorTypeDef]]

### MutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.MutualTlsAuthenticationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DomainNameTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingSelectionExpression
- **Type**: typing.Optional[str]

### DomainNameConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationTypeDef]]

### MutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.MutualTlsAuthenticationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportApiRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputType
- **Type**: typing.Literal['JSON', 'YAML']
- **Required**: Yes

### Specification
- **Type**: typing.Literal['OAS30']
- **Required**: Yes

### ExportVersion
- **Type**: typing.Optional[str]

### IncludeExtensions
- **Type**: typing.Optional[bool]

### StageName
- **Type**: typing.Optional[str]


# ExportApiResponseTypeDef

### body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApiMappingRequestRequestTypeDef

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiMappingResponseTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingKey
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApiMappingsRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetApiMappingsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.ApiMappingTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApiRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiResponseTypeDef

### ApiEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### CorsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsTypeDef'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DisableSchemaValidation
- **Type**: <class 'bool'>
- **Required**: Yes

### DisableExecuteApiEndpoint
- **Type**: <class 'bool'>
- **Required**: Yes

### ImportInfo
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### RouteSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApisRequestGetApisPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetApisRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetApisResponsePaginatorTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.ApiPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApisResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.ApiTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAuthorizerRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthorizerResponseTypeDef

### AuthorizerCredentialsArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerPayloadFormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerResultTtlInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### AuthorizerType
- **Type**: typing.Literal['JWT', 'REQUEST']
- **Required**: Yes

### AuthorizerUri
- **Type**: <class 'str'>
- **Required**: Yes

### EnableSimpleResponses
- **Type**: <class 'bool'>
- **Required**: Yes

### IdentitySource
- **Type**: typing.List[str]
- **Required**: Yes

### IdentityValidationExpression
- **Type**: <class 'str'>
- **Required**: Yes

### JwtConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAuthorizersRequestGetAuthorizersPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetAuthorizersRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetAuthorizersResponsePaginatorTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.AuthorizerPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAuthorizersResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.AuthorizerTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentResponseTypeDef

### AutoDeployed
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentStatus
- **Type**: typing.Literal['DEPLOYED', 'FAILED', 'PENDING']
- **Required**: Yes

### DeploymentStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentsRequestGetDeploymentsPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetDeploymentsRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetDeploymentsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DeploymentTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainNameRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainNameResponseTypeDef

### ApiMappingSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationTypeDef]
- **Required**: Yes

### MutualTlsAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.MutualTlsAuthenticationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainNamesRequestGetDomainNamesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetDomainNamesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetDomainNamesResponsePaginatorTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNamePaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainNamesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntegrationRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseResponseTypeDef

### ContentHandlingStrategy
- **Type**: typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TemplateSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntegrationResponsesRequestGetIntegrationResponsesPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetIntegrationResponsesRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetIntegrationResponsesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.IntegrationResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntegrationResultTypeDef

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: typing.Literal['INTERNET', 'VPC_LINK']
- **Required**: Yes

### ContentHandlingStrategy
- **Type**: typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']
- **Required**: Yes

### CredentialsArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationMethod
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationSubtype
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationType
- **Type**: typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']
- **Required**: Yes

### IntegrationUri
- **Type**: <class 'str'>
- **Required**: Yes

### PassthroughBehavior
- **Type**: typing.Literal['NEVER', 'WHEN_NO_MATCH', 'WHEN_NO_TEMPLATES']
- **Required**: Yes

### PayloadFormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RequestParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RequestTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### TemplateSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### TlsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.TlsConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntegrationsRequestGetIntegrationsPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetIntegrationsRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetIntegrationsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.IntegrationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelResponseTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelTemplateRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelTemplateResponseTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelsRequestGetModelsPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetModelsRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetModelsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.ModelTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRouteRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteResponseRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteResponseResponseTypeDef

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRouteResponsesRequestGetRouteResponsesPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetRouteResponsesRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetRouteResponsesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteResponseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRouteResultTypeDef

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ApiKeyRequired
- **Type**: <class 'bool'>
- **Required**: Yes

### AuthorizationScopes
- **Type**: typing.List[str]
- **Required**: Yes

### AuthorizationType
- **Type**: typing.Literal['AWS_IAM', 'CUSTOM', 'JWT', 'NONE']
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### OperationName
- **Type**: <class 'str'>
- **Required**: Yes

### RequestModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RequestParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRoutesRequestGetRoutesPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetRoutesRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetRoutesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStageRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStageResponseTypeDef

### AccessLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.AccessLogSettingsTypeDef'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoDeploy
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultRouteSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastDeploymentStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RouteSettings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### StageVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStagesRequestGetStagesPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetStagesRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetStagesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.StageTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTagsRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTagsResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVpcLinkRequestRequestTypeDef

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcLinkResponseTypeDef

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcLinkStatus
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'FAILED', 'INACTIVE', 'PENDING']
- **Required**: Yes

### VpcLinkStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VpcLinkVersion
- **Type**: typing.Literal['V2']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVpcLinksRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetVpcLinksResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.VpcLinkTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportApiRequestRequestTypeDef

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### Basepath
- **Type**: typing.Optional[str]

### FailOnWarnings
- **Type**: typing.Optional[bool]


# ImportApiResponseTypeDef

### ApiEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### CorsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsTypeDef'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DisableSchemaValidation
- **Type**: <class 'bool'>
- **Required**: Yes

### DisableExecuteApiEndpoint
- **Type**: <class 'bool'>
- **Required**: Yes

### ImportInfo
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### RouteSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IntegrationResponseTypeDef

### IntegrationResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ContentHandlingStrategy
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]

### IntegrationResponseId
- **Type**: typing.Optional[str]

### ResponseParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResponseTemplates
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateSelectionExpression
- **Type**: typing.Optional[str]


# IntegrationTypeDef

### ApiGatewayManaged
- **Type**: typing.Optional[bool]

### ConnectionId
- **Type**: typing.Optional[str]

### ConnectionType
- **Type**: typing.Optional[typing.Literal['INTERNET', 'VPC_LINK']]

### ContentHandlingStrategy
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]

### CredentialsArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IntegrationId
- **Type**: typing.Optional[str]

### IntegrationMethod
- **Type**: typing.Optional[str]

### IntegrationResponseSelectionExpression
- **Type**: typing.Optional[str]

### IntegrationSubtype
- **Type**: typing.Optional[str]

### IntegrationType
- **Type**: typing.Optional[typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']]

### IntegrationUri
- **Type**: typing.Optional[str]

### PassthroughBehavior
- **Type**: typing.Optional[typing.Literal['NEVER', 'WHEN_NO_MATCH', 'WHEN_NO_TEMPLATES']]

### PayloadFormatVersion
- **Type**: typing.Optional[str]

### RequestParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestTemplates
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### TemplateSelectionExpression
- **Type**: typing.Optional[str]

### TimeoutInMillis
- **Type**: typing.Optional[int]

### TlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.TlsConfigTypeDef]


# JWTConfigurationPaginatorTypeDef

### Audience
- **Type**: typing.Optional[typing.List[str]]

### Issuer
- **Type**: typing.Optional[str]


# JWTConfigurationTypeDef

### Audience
- **Type**: typing.Optional[typing.Sequence[str]]

### Issuer
- **Type**: typing.Optional[str]


# ModelTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ModelId
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]


# MutualTlsAuthenticationInputTypeDef

### TruststoreUri
- **Type**: typing.Optional[str]

### TruststoreVersion
- **Type**: typing.Optional[str]


# MutualTlsAuthenticationTypeDef

### TruststoreUri
- **Type**: typing.Optional[str]

### TruststoreVersion
- **Type**: typing.Optional[str]

### TruststoreWarnings
- **Type**: typing.Optional[typing.List[str]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterConstraintsTypeDef

### Required
- **Type**: typing.Optional[bool]


# ReimportApiRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### Basepath
- **Type**: typing.Optional[str]

### FailOnWarnings
- **Type**: typing.Optional[bool]


# ReimportApiResponseTypeDef

### ApiEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### CorsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsTypeDef'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DisableSchemaValidation
- **Type**: <class 'bool'>
- **Required**: Yes

### DisableExecuteApiEndpoint
- **Type**: <class 'bool'>
- **Required**: Yes

### ImportInfo
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### RouteSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResetAuthorizersCacheRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
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


# RouteResponseTypeDef

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSelectionExpression
- **Type**: typing.Optional[str]

### ResponseModels
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]]

### RouteResponseId
- **Type**: typing.Optional[str]


# RouteSettingsTypeDef

### DataTraceEnabled
- **Type**: typing.Optional[bool]

### DetailedMetricsEnabled
- **Type**: typing.Optional[bool]

### LoggingLevel
- **Type**: typing.Optional[typing.Literal['ERROR', 'INFO', 'OFF']]

### ThrottlingBurstLimit
- **Type**: typing.Optional[int]

### ThrottlingRateLimit
- **Type**: typing.Optional[float]


# RouteTypeDef

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: typing.Optional[bool]

### ApiKeyRequired
- **Type**: typing.Optional[bool]

### AuthorizationScopes
- **Type**: typing.Optional[typing.List[str]]

### AuthorizationType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'CUSTOM', 'JWT', 'NONE']]

### AuthorizerId
- **Type**: typing.Optional[str]

### ModelSelectionExpression
- **Type**: typing.Optional[str]

### OperationName
- **Type**: typing.Optional[str]

### RequestModels
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]]

### RouteId
- **Type**: typing.Optional[str]

### RouteResponseSelectionExpression
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# StageTypeDef

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.AccessLogSettingsTypeDef]

### ApiGatewayManaged
- **Type**: typing.Optional[bool]

### AutoDeploy
- **Type**: typing.Optional[bool]

### ClientCertificateId
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]

### DeploymentId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LastDeploymentStatusMessage
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### RouteSettings
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]]

### StageVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TlsConfigInputTypeDef

### ServerNameToVerify
- **Type**: typing.Optional[str]


# TlsConfigTypeDef

### ServerNameToVerify
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApiMappingRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingKey
- **Type**: typing.Optional[str]

### Stage
- **Type**: typing.Optional[str]


# UpdateApiMappingResponseTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingKey
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApiRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsTypeDef]

### CredentialsArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisableSchemaValidation
- **Type**: typing.Optional[bool]

### DisableExecuteApiEndpoint
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]

### RouteKey
- **Type**: typing.Optional[str]

### RouteSelectionExpression
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# UpdateApiResponseTypeDef

### ApiEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### CorsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsTypeDef'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DisableSchemaValidation
- **Type**: <class 'bool'>
- **Required**: Yes

### DisableExecuteApiEndpoint
- **Type**: <class 'bool'>
- **Required**: Yes

### ImportInfo
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### RouteSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAuthorizerRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerCredentialsArn
- **Type**: typing.Optional[str]

### AuthorizerPayloadFormatVersion
- **Type**: typing.Optional[str]

### AuthorizerResultTtlInSeconds
- **Type**: typing.Optional[int]

### AuthorizerType
- **Type**: typing.Optional[typing.Literal['JWT', 'REQUEST']]

### AuthorizerUri
- **Type**: typing.Optional[str]

### EnableSimpleResponses
- **Type**: typing.Optional[bool]

### IdentitySource
- **Type**: typing.Optional[typing.Sequence[str]]

### IdentityValidationExpression
- **Type**: typing.Optional[str]

### JwtConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationTypeDef]

### Name
- **Type**: typing.Optional[str]


# UpdateAuthorizerResponseTypeDef

### AuthorizerCredentialsArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerPayloadFormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerResultTtlInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### AuthorizerType
- **Type**: typing.Literal['JWT', 'REQUEST']
- **Required**: Yes

### AuthorizerUri
- **Type**: <class 'str'>
- **Required**: Yes

### EnableSimpleResponses
- **Type**: <class 'bool'>
- **Required**: Yes

### IdentitySource
- **Type**: typing.List[str]
- **Required**: Yes

### IdentityValidationExpression
- **Type**: <class 'str'>
- **Required**: Yes

### JwtConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDeploymentRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateDeploymentResponseTypeDef

### AutoDeployed
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentStatus
- **Type**: typing.Literal['DEPLOYED', 'FAILED', 'PENDING']
- **Required**: Yes

### DeploymentStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainNameRequestRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationTypeDef]]

### MutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.MutualTlsAuthenticationInputTypeDef]


# UpdateDomainNameResponseTypeDef

### ApiMappingSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationTypeDef]
- **Required**: Yes

### MutualTlsAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.MutualTlsAuthenticationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIntegrationRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionId
- **Type**: typing.Optional[str]

### ConnectionType
- **Type**: typing.Optional[typing.Literal['INTERNET', 'VPC_LINK']]

### ContentHandlingStrategy
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]

### CredentialsArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IntegrationMethod
- **Type**: typing.Optional[str]

### IntegrationSubtype
- **Type**: typing.Optional[str]

### IntegrationType
- **Type**: typing.Optional[typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']]

### IntegrationUri
- **Type**: typing.Optional[str]

### PassthroughBehavior
- **Type**: typing.Optional[typing.Literal['NEVER', 'WHEN_NO_MATCH', 'WHEN_NO_TEMPLATES']]

### PayloadFormatVersion
- **Type**: typing.Optional[str]

### RequestParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestTemplates
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]

### TemplateSelectionExpression
- **Type**: typing.Optional[str]

### TimeoutInMillis
- **Type**: typing.Optional[int]

### TlsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.TlsConfigInputTypeDef]


# UpdateIntegrationResponseRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### ContentHandlingStrategy
- **Type**: typing.Optional[typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']]

### IntegrationResponseKey
- **Type**: typing.Optional[str]

### ResponseParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ResponseTemplates
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TemplateSelectionExpression
- **Type**: typing.Optional[str]


# UpdateIntegrationResponseResponseTypeDef

### ContentHandlingStrategy
- **Type**: typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TemplateSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIntegrationResultTypeDef

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionType
- **Type**: typing.Literal['INTERNET', 'VPC_LINK']
- **Required**: Yes

### ContentHandlingStrategy
- **Type**: typing.Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT']
- **Required**: Yes

### CredentialsArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationMethod
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationSubtype
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationType
- **Type**: typing.Literal['AWS', 'AWS_PROXY', 'HTTP', 'HTTP_PROXY', 'MOCK']
- **Required**: Yes

### IntegrationUri
- **Type**: <class 'str'>
- **Required**: Yes

### PassthroughBehavior
- **Type**: typing.Literal['NEVER', 'WHEN_NO_MATCH', 'WHEN_NO_TEMPLATES']
- **Required**: Yes

### PayloadFormatVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RequestParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RequestTemplates
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### TemplateSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### TimeoutInMillis
- **Type**: <class 'int'>
- **Required**: Yes

### TlsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.TlsConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateModelRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]


# UpdateModelResponseTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRouteRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeyRequired
- **Type**: typing.Optional[bool]

### AuthorizationScopes
- **Type**: typing.Optional[typing.Sequence[str]]

### AuthorizationType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'CUSTOM', 'JWT', 'NONE']]

### AuthorizerId
- **Type**: typing.Optional[str]

### ModelSelectionExpression
- **Type**: typing.Optional[str]

### OperationName
- **Type**: typing.Optional[str]

### RequestModels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]]

### RouteKey
- **Type**: typing.Optional[str]

### RouteResponseSelectionExpression
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# UpdateRouteResponseRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSelectionExpression
- **Type**: typing.Optional[str]

### ResponseModels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]]

### RouteResponseKey
- **Type**: typing.Optional[str]


# UpdateRouteResponseResponseTypeDef

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRouteResultTypeDef

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### ApiKeyRequired
- **Type**: <class 'bool'>
- **Required**: Yes

### AuthorizationScopes
- **Type**: typing.List[str]
- **Required**: Yes

### AuthorizationType
- **Type**: typing.Literal['AWS_IAM', 'CUSTOM', 'JWT', 'NONE']
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### OperationName
- **Type**: <class 'str'>
- **Required**: Yes

### RequestModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RequestParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.ParameterConstraintsTypeDef]
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStageRequestRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.AccessLogSettingsTypeDef]

### AutoDeploy
- **Type**: typing.Optional[bool]

### ClientCertificateId
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]

### DeploymentId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]]

### StageVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateStageResponseTypeDef

### AccessLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.AccessLogSettingsTypeDef'>
- **Required**: Yes

### ApiGatewayManaged
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoDeploy
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultRouteSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastDeploymentStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RouteSettings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2_classes.RouteSettingsTypeDef]
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### StageVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVpcLinkRequestRequestTypeDef

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateVpcLinkResponseTypeDef

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### VpcLinkStatus
- **Type**: typing.Literal['AVAILABLE', 'DELETING', 'FAILED', 'INACTIVE', 'PENDING']
- **Required**: Yes

### VpcLinkStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VpcLinkVersion
- **Type**: typing.Literal['V2']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcLinkTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### VpcLinkStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETING', 'FAILED', 'INACTIVE', 'PENDING']]

### VpcLinkStatusMessage
- **Type**: typing.Optional[str]

### VpcLinkVersion
- **Type**: typing.Optional[typing.Literal['V2']]


