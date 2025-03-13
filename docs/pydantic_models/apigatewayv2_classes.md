# Apigatewayv2 Classes

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationOutputTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CorsOutputTypeDef

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


# CorsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApiMappingRequestTypeDef

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


# CreateApiRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsUnionTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsOutputTypeDef'>
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


# CreateAuthorizerRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationUnionTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationOutputTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentRequestTypeDef

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


# CreateDomainNameRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationUnionTypeDef]]

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationOutputTypeDef]
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


# CreateIntegrationRequestTypeDef

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


# CreateIntegrationResponseRequestTypeDef

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


# CreateModelRequestTypeDef

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


# CreateRouteRequestTypeDef

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


# CreateRouteResponseRequestTypeDef

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


# CreateStageRequestTypeDef

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


# CreateVpcLinkRequestTypeDef

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


# DeleteAccessLogSettingsRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiMappingRequestTypeDef

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthorizerRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCorsConfigurationRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponseRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteRequestParameterRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestParameterKey
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteResponseRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteSettingsRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStageRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcLinkRequestTypeDef

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


# DomainNameConfigurationOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.TimestampTypeDef]

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


# DomainNameConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DomainNameTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingSelectionExpression
- **Type**: typing.Optional[str]

### DomainNameConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationOutputTypeDef]]

### MutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.MutualTlsAuthenticationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportApiRequestTypeDef

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


# GetApiMappingRequestTypeDef

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


# GetApiMappingsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetApiRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsOutputTypeDef'>
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


# GetApisRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetApisRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetApisResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.ApiTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAuthorizerRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationOutputTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAuthorizersRequestPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetAuthorizersRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetAuthorizersResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.AuthorizerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDeploymentRequestTypeDef

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


# GetDeploymentsRequestPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetDeploymentsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDomainNameRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationOutputTypeDef]
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


# GetDomainNamesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetDomainNamesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetDomainNamesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetIntegrationRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseRequestTypeDef

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


# GetIntegrationResponsesRequestPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetIntegrationResponsesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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


# GetIntegrationsRequestPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetIntegrationsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetModelRequestTypeDef

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


# GetModelTemplateRequestTypeDef

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


# GetModelsRequestPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetModelsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRouteRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteResponseRequestTypeDef

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


# GetRouteResponsesRequestPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetRouteResponsesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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


# GetRoutesRequestPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetRoutesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStageRequestTypeDef

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


# GetStagesRequestPaginateTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.PaginatorConfigTypeDef]


# GetStagesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTagsRequestTypeDef

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


# GetVpcLinkRequestTypeDef

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


# GetVpcLinksRequestTypeDef

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetVpcLinksResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.VpcLinkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ImportApiRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsOutputTypeDef'>
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


# JWTConfigurationOutputTypeDef

### Audience
- **Type**: typing.Optional[typing.List[str]]

### Issuer
- **Type**: typing.Optional[str]


# JWTConfigurationTypeDef

### Audience
- **Type**: typing.Optional[typing.Sequence[str]]

### Issuer
- **Type**: typing.Optional[str]


# JWTConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReimportApiRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsOutputTypeDef'>
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


# ResetAuthorizersCacheRequestTypeDef

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


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TlsConfigInputTypeDef

### ServerNameToVerify
- **Type**: typing.Optional[str]


# TlsConfigTypeDef

### ServerNameToVerify
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApiMappingRequestTypeDef

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


# UpdateApiRequestTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsUnionTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.CorsOutputTypeDef'>
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


# UpdateAuthorizerRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationUnionTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.JWTConfigurationOutputTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDeploymentRequestTypeDef

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


# UpdateDomainNameRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationUnionTypeDef]]

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2_classes.DomainNameConfigurationOutputTypeDef]
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


# UpdateIntegrationRequestTypeDef

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


# UpdateIntegrationResponseRequestTypeDef

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


# UpdateModelRequestTypeDef

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


# UpdateRouteRequestTypeDef

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


# UpdateRouteResponseRequestTypeDef

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


# UpdateStageRequestTypeDef

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


# UpdateVpcLinkRequestTypeDef

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


