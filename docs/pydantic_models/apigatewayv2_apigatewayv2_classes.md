# Apigatewayv2 Apigatewayv2 Classes

# AccessLogSettings

### DestinationArn
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[str]


# Api

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.CorsOutput]

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


# ApiMapping

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


# Authorizer

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.JWTConfigurationOutput]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Cors

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


# CorsOutput

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


# CreateApiMappingRequest

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


# CreateApiMappingResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApiRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['HTTP', 'WEBSOCKET']
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Cors, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.CorsOutput, NoneType]

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### Target
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# CreateApiResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.CorsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAuthorizerRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerType
- **Type**: typing.Literal['JWT', 'REQUEST']
- **Required**: Yes

### IdentitySource
- **Type**: typing.List[str]
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.JWTConfiguration, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.JWTConfigurationOutput, NoneType]


# CreateAuthorizerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.JWTConfigurationOutput'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]


# CreateDeploymentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainNameRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainNameConfiguration, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainNameConfigurationOutput]]]

### MutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.MutualTlsAuthenticationInput]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDomainNameResponse

### ApiMappingSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainNameConfigurationOutput]
- **Required**: Yes

### MutualTlsAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.MutualTlsAuthentication'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntegrationRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.TlsConfigInput]


# CreateIntegrationResponseRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResponseTemplates
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateSelectionExpression
- **Type**: typing.Optional[str]


# CreateIntegrationResponseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntegrationResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.TlsConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelRequest

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


# CreateModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRouteRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]]

### RouteResponseSelectionExpression
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# CreateRouteResponseRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]]


# CreateRouteResponseResponse

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRouteResult

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStageRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessLogSettings
- **Type**: <class 'NoneType'>

### AutoDeploy
- **Type**: typing.Optional[bool]

### ClientCertificateId
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings]

### DeploymentId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[typing.Dict[str, NoneType]]

### StageVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateStageResponse

### AccessLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.AccessLogSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings'>
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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcLinkRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateVpcLinkResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAccessLogSettingsRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiMappingRequest

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAuthorizerRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCorsConfigurationRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponseRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteRequestParameterRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestParameterKey
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteResponseRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRouteSettingsRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteKey
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStageRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcLinkRequest

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# Deployment

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


# DomainName

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiMappingSelectionExpression
- **Type**: typing.Optional[str]

### DomainNameConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainNameConfigurationOutput]]

### MutualTlsAuthentication
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DomainNameConfiguration

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


# DomainNameConfigurationOutput

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# ExportApiRequest

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


# ExportApiResponse

### body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetApiMappingRequest

### ApiMappingId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiMappingResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetApiMappingsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetApiMappingsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ApiMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetApiRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.CorsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetApisRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetApisRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetApisResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Api]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAuthorizerRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAuthorizerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.JWTConfigurationOutput'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetAuthorizersRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetAuthorizersRequestPaginate

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetAuthorizersResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Authorizer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDeploymentRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentsRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetDeploymentsRequestPaginate

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetDeploymentsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Deployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDomainNameRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainNameResponse

### ApiMappingSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainNameConfigurationOutput]
- **Required**: Yes

### MutualTlsAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.MutualTlsAuthentication'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainNamesRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetDomainNamesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetDomainNamesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainName]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetIntegrationRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetIntegrationResponsesRequest

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


# GetIntegrationResponsesRequestPaginate

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### IntegrationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetIntegrationResponsesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.IntegrationResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetIntegrationResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.TlsConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetIntegrationsRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetIntegrationsRequestPaginate

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetIntegrationsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Integration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetModelRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelTemplateRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ModelId
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelTemplateResponse

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelsRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetModelsRequestPaginate

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetModelsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Model]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRouteRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteResponseRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRouteResponseResponse

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetRouteResponsesRequest

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


# GetRouteResponsesRequestPaginate

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetRouteResponsesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRouteResult

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetRoutesRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetRoutesRequestPaginate

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetRoutesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Route]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStageRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStageResponse

### AccessLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.AccessLogSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings'>
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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetStagesRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetStagesRequestPaginate

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.PaginatorConfig]


# GetStagesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Stage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTagsResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetVpcLinkRequest

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcLinkResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetVpcLinksRequest

### MaxResults
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetVpcLinksResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.VpcLink]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ImportApiRequest

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### Basepath
- **Type**: typing.Optional[str]

### FailOnWarnings
- **Type**: typing.Optional[bool]


# ImportApiResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.CorsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# Integration

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
- **Type**: <class 'NoneType'>


# IntegrationResponse

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


# JWTConfiguration

### Audience
- **Type**: typing.Optional[typing.List[str]]

### Issuer
- **Type**: typing.Optional[str]


# JWTConfigurationOutput

### Audience
- **Type**: typing.Optional[typing.List[str]]

### Issuer
- **Type**: typing.Optional[str]


# Model

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


# MutualTlsAuthentication

### TruststoreUri
- **Type**: typing.Optional[str]

### TruststoreVersion
- **Type**: typing.Optional[str]

### TruststoreWarnings
- **Type**: typing.Optional[typing.List[str]]


# MutualTlsAuthenticationInput

### TruststoreUri
- **Type**: typing.Optional[str]

### TruststoreVersion
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterConstraints

### Required
- **Type**: typing.Optional[bool]


# ReimportApiRequest

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


# ReimportApiResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.CorsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# ResetAuthorizersCacheRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
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


# Route

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]]

### RouteId
- **Type**: typing.Optional[str]

### RouteResponseSelectionExpression
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# RouteResponse

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSelectionExpression
- **Type**: typing.Optional[str]

### ResponseModels
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]]

### RouteResponseId
- **Type**: typing.Optional[str]


# RouteSettings

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


# Stage

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessLogSettings
- **Type**: <class 'NoneType'>

### ApiGatewayManaged
- **Type**: typing.Optional[bool]

### AutoDeploy
- **Type**: typing.Optional[bool]

### ClientCertificateId
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings]

### DeploymentId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LastDeploymentStatusMessage
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### RouteSettings
- **Type**: typing.Optional[typing.Dict[str, NoneType]]

### StageVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TlsConfig

### ServerNameToVerify
- **Type**: typing.Optional[str]


# TlsConfigInput

### ServerNameToVerify
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApiMappingRequest

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


# UpdateApiMappingResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApiRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.Cors, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.CorsOutput, NoneType]

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


# UpdateApiResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.CorsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAuthorizerRequest

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
- **Type**: typing.Optional[typing.List[str]]

### IdentityValidationExpression
- **Type**: typing.Optional[str]

### JwtConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.JWTConfiguration, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.JWTConfigurationOutput, NoneType]

### Name
- **Type**: typing.Optional[str]


# UpdateAuthorizerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.JWTConfigurationOutput'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDeploymentRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateDeploymentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainNameRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainNameConfiguration, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainNameConfigurationOutput]]]

### MutualTlsAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.MutualTlsAuthenticationInput]


# UpdateDomainNameResponse

### ApiMappingSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainNameConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.DomainNameConfigurationOutput]
- **Required**: Yes

### MutualTlsAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.MutualTlsAuthentication'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIntegrationRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.TlsConfigInput]


# UpdateIntegrationResponseRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResponseTemplates
- **Type**: typing.Optional[typing.Dict[str, str]]

### TemplateSelectionExpression
- **Type**: typing.Optional[str]


# UpdateIntegrationResponseResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIntegrationResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.TlsConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateModelRequest

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


# UpdateModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRouteRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteId
- **Type**: <class 'str'>
- **Required**: Yes

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]]

### RouteKey
- **Type**: typing.Optional[str]

### RouteResponseSelectionExpression
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# UpdateRouteResponseRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResponseParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]]

### RouteResponseKey
- **Type**: typing.Optional[str]


# UpdateRouteResponseResponse

### ModelSelectionExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseModels
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]
- **Required**: Yes

### RouteResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### RouteResponseKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRouteResult

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ParameterConstraints]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStageRequest

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessLogSettings
- **Type**: <class 'NoneType'>

### AutoDeploy
- **Type**: typing.Optional[bool]

### ClientCertificateId
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings]

### DeploymentId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[typing.Dict[str, NoneType]]

### StageVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateStageResponse

### AccessLogSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.AccessLogSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings'>
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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.RouteSettings]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVpcLinkRequest

### VpcLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateVpcLinkResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_classes.ResponseMetadata'>
- **Required**: Yes


# VpcLink

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


