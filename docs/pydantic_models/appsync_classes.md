# Appsync Classes

# AdditionalAuthenticationProvider

### authenticationType
- **Type**: typing.Optional[typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfig]

### userPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CognitoUserPoolConfig]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfig]


# Api

### apiId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### ownerContact
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### dns
- **Type**: typing.Optional[typing.Dict[str, str]]

### apiArn
- **Type**: typing.Optional[str]

### created
- **Type**: typing.Optional[datetime.datetime]

### xrayEnabled
- **Type**: typing.Optional[bool]

### wafWebAclArn
- **Type**: typing.Optional[str]

### eventConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventConfigOutput]


# ApiAssociation

### domainName
- **Type**: typing.Optional[str]

### apiId
- **Type**: typing.Optional[str]

### associationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCESS']]

### deploymentDetail
- **Type**: typing.Optional[str]


# ApiCache

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiKey

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppSyncRuntime

### name
- **Type**: typing.Literal['APPSYNC_JS']
- **Required**: Yes

### runtimeVersion
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateApiRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateApiResponse

### apiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateMergedGraphqlApiRequest

### sourceApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sourceApiAssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationConfig]


# AssociateMergedGraphqlApiResponse

### sourceApiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateSourceGraphqlApiRequest

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sourceApiAssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationConfig]


# AssociateSourceGraphqlApiResponse

### sourceApiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# AuthMode

### authType
- **Type**: typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']
- **Required**: Yes


# AuthProvider

### authType
- **Type**: typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']
- **Required**: Yes

### cognitoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CognitoConfig]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfig]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfig]


# AuthorizationConfig

### authorizationType
- **Type**: typing.Literal['AWS_IAM']
- **Required**: Yes

### awsIamConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AwsIamConfig]


# AwsIamConfig

### signingRegion
- **Type**: typing.Optional[str]

### signingServiceName
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CachingConfig

### ttl
- **Type**: <class 'int'>
- **Required**: Yes

### cachingKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# CachingConfigOutput

### ttl
- **Type**: <class 'int'>
- **Required**: Yes

### cachingKeys
- **Type**: typing.Optional[typing.List[str]]


# CachingConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelNamespace

### apiId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### subscribeAuthModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]]

### publishAuthModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]]

### codeHandlers
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### channelNamespaceArn
- **Type**: typing.Optional[str]

### created
- **Type**: typing.Optional[datetime.datetime]

### lastModified
- **Type**: typing.Optional[datetime.datetime]


# CodeError

### errorType
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CodeErrorLocation]


# CodeErrorLocation

### line
- **Type**: typing.Optional[int]

### column
- **Type**: typing.Optional[int]

### span
- **Type**: typing.Optional[int]


# CognitoConfig

### userPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### appIdClientRegex
- **Type**: typing.Optional[str]


# CognitoUserPoolConfig

### userPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### appIdClientRegex
- **Type**: typing.Optional[str]


# CreateApiCacheResponse

### apiCache
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiCache'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApiKeyRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### expires
- **Type**: typing.Optional[int]


# CreateApiKeyResponse

### apiKey
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApiRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ownerContact
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### eventConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventConfigUnion]


# CreateApiResponse

### api
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.Api'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelNamespaceRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subscribeAuthModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]]

### publishAuthModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]]

### codeHandlers
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChannelNamespaceResponse

### channelNamespace
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ChannelNamespace'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceResponse

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainNameRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateDomainNameResponse

### domainNameConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFunctionRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### requestMappingTemplate
- **Type**: typing.Optional[str]

### responseMappingTemplate
- **Type**: typing.Optional[str]

### functionVersion
- **Type**: typing.Optional[str]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfig]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntime]

### code
- **Type**: typing.Optional[str]


# CreateFunctionResponse

### functionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.FunctionConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGraphqlApiRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### authenticationType
- **Type**: typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']
- **Required**: Yes

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LogConfig]

### userPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.UserPoolConfig]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfig]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### additionalAuthenticationProviders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AdditionalAuthenticationProvider]]

### xrayEnabled
- **Type**: typing.Optional[bool]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfig]

### apiType
- **Type**: typing.Optional[typing.Literal['GRAPHQL', 'MERGED']]

### mergedApiExecutionRoleArn
- **Type**: typing.Optional[str]

### visibility
- **Type**: typing.Optional[typing.Literal['GLOBAL', 'PRIVATE']]

### ownerContact
- **Type**: typing.Optional[str]

### introspectionConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### queryDepthLimit
- **Type**: typing.Optional[int]

### resolverCountLimit
- **Type**: typing.Optional[int]

### enhancedMetricsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EnhancedMetricsConfig]


# CreateGraphqlApiResponse

### graphqlApi
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.GraphqlApi'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResolverRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceName
- **Type**: typing.Optional[str]

### requestMappingTemplate
- **Type**: typing.Optional[str]

### responseMappingTemplate
- **Type**: typing.Optional[str]

### kind
- **Type**: typing.Optional[typing.Literal['PIPELINE', 'UNIT']]

### pipelineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PipelineConfigUnion]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfig]

### cachingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CachingConfigUnion]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntime]

### code
- **Type**: typing.Optional[str]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateResolverResponse

### resolver
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.Resolver'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# DataSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceIntrospectionModel

### name
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModelField]]

### primaryKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModelIndex]

### indexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModelIndex]]

### sdl
- **Type**: typing.Optional[str]


# DataSourceIntrospectionModelField

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceIntrospectionModelIndex

### name
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.List[str]]


# DataSourceIntrospectionResult

### models
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModel]]

### nextToken
- **Type**: typing.Optional[str]


# DeleteApiCacheRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelNamespaceRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGraphqlApiRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTypeRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeltaSyncConfig

### baseTableTTL
- **Type**: typing.Optional[int]

### deltaSyncTableName
- **Type**: typing.Optional[str]

### deltaSyncTableTTL
- **Type**: typing.Optional[int]


# DisassociateApiRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMergedGraphqlApiRequest

### sourceApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMergedGraphqlApiResponse

### sourceApiAssociationStatus
- **Type**: typing.Literal['AUTO_MERGE_SCHEDULE_FAILED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'DELETION_SCHEDULED', 'MERGE_FAILED', 'MERGE_IN_PROGRESS', 'MERGE_SCHEDULED', 'MERGE_SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateSourceGraphqlApiRequest

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateSourceGraphqlApiResponse

### sourceApiAssociationStatus
- **Type**: typing.Literal['AUTO_MERGE_SCHEDULE_FAILED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'DELETION_SCHEDULED', 'MERGE_FAILED', 'MERGE_IN_PROGRESS', 'MERGE_SCHEDULED', 'MERGE_SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# DomainNameConfig

### domainName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### certificateArn
- **Type**: typing.Optional[str]

### appsyncDomainName
- **Type**: typing.Optional[str]

### hostedZoneId
- **Type**: typing.Optional[str]


# DynamodbDataSourceConfig

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### useCallerCredentials
- **Type**: typing.Optional[bool]

### deltaSyncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.DeltaSyncConfig]

### versioned
- **Type**: typing.Optional[bool]


# ElasticsearchDataSourceConfig

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# EnhancedMetricsConfig

### resolverLevelMetricsBehavior
- **Type**: typing.Literal['FULL_REQUEST_RESOLVER_METRICS', 'PER_RESOLVER_METRICS']
- **Required**: Yes

### dataSourceLevelMetricsBehavior
- **Type**: typing.Literal['FULL_REQUEST_DATA_SOURCE_METRICS', 'PER_DATA_SOURCE_METRICS']
- **Required**: Yes

### operationLevelMetricsConfig
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# ErrorDetail

### message
- **Type**: typing.Optional[str]


# EvaluateCodeErrorDetail

### message
- **Type**: typing.Optional[str]

### codeErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.CodeError]]


# EvaluateCodeRequest

### runtime
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntime'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### context
- **Type**: <class 'str'>
- **Required**: Yes

### function
- **Type**: typing.Optional[str]


# EvaluateCodeResponse

### evaluationResult
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.EvaluateCodeErrorDetail'>
- **Required**: Yes

### logs
- **Type**: typing.List[str]
- **Required**: Yes

### stash
- **Type**: <class 'str'>
- **Required**: Yes

### outErrors
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# EvaluateMappingTemplateRequest

### template
- **Type**: <class 'str'>
- **Required**: Yes

### context
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateMappingTemplateResponse

### evaluationResult
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ErrorDetail'>
- **Required**: Yes

### logs
- **Type**: typing.List[str]
- **Required**: Yes

### stash
- **Type**: <class 'str'>
- **Required**: Yes

### outErrors
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# EventBridgeDataSourceConfig

### eventBusArn
- **Type**: <class 'str'>
- **Required**: Yes


# EventConfig

### authProviders
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthProvider]
- **Required**: Yes

### connectionAuthModes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]
- **Required**: Yes

### defaultPublishAuthModes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]
- **Required**: Yes

### defaultSubscribeAuthModes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]
- **Required**: Yes

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventLogConfig]


# EventConfigOutput

### authProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthProvider]
- **Required**: Yes

### connectionAuthModes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]
- **Required**: Yes

### defaultPublishAuthModes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]
- **Required**: Yes

### defaultSubscribeAuthModes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]
- **Required**: Yes

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventLogConfig]


# EventConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventLogConfig

### logLevel
- **Type**: typing.Literal['ALL', 'DEBUG', 'ERROR', 'INFO', 'NONE']
- **Required**: Yes

### cloudWatchLogsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# FlushApiCacheRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# FunctionConfiguration

### functionId
- **Type**: typing.Optional[str]

### functionArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### dataSourceName
- **Type**: typing.Optional[str]

### requestMappingTemplate
- **Type**: typing.Optional[str]

### responseMappingTemplate
- **Type**: typing.Optional[str]

### functionVersion
- **Type**: typing.Optional[str]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfig]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntime]

### code
- **Type**: typing.Optional[str]


# GetApiAssociationRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiAssociationResponse

### apiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetApiCacheRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiCacheResponse

### apiCache
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiCache'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetApiRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiResponse

### api
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.Api'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelNamespaceRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelNamespaceResponse

### channelNamespace
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ChannelNamespace'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSourceIntrospectionRequest

### introspectionId
- **Type**: <class 'str'>
- **Required**: Yes

### includeModelsSDL
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetDataSourceIntrospectionResponse

### introspectionId
- **Type**: <class 'str'>
- **Required**: Yes

### introspectionStatus
- **Type**: typing.Literal['FAILED', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### introspectionStatusDetail
- **Type**: <class 'str'>
- **Required**: Yes

### introspectionResult
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSourceRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceResponse

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainNameRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainNameResponse

### domainNameConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetFunctionRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionResponse

### functionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.FunctionConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetGraphqlApiEnvironmentVariablesRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphqlApiEnvironmentVariablesResponse

### environmentVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetGraphqlApiRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphqlApiResponse

### graphqlApi
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.GraphqlApi'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetIntrospectionSchemaResponse

### schema
- **Type**: <class 'botocore.response.StreamingBody'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.appsync_classes.GetIntrospectionSchemaResponse'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetResolverRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverResponse

### resolver
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.Resolver'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaCreationStatusRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaCreationStatusResponse

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'NOT_APPLICABLE', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### details
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GetSourceApiAssociationRequest

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSourceApiAssociationResponse

### sourceApiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# GraphqlApi

### name
- **Type**: typing.Optional[str]

### apiId
- **Type**: typing.Optional[str]

### authenticationType
- **Type**: typing.Optional[typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']]

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LogConfig]

### userPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.UserPoolConfig]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfig]

### arn
- **Type**: typing.Optional[str]

### uris
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### additionalAuthenticationProviders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.AdditionalAuthenticationProvider]]

### xrayEnabled
- **Type**: typing.Optional[bool]

### wafWebAclArn
- **Type**: typing.Optional[str]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfig]

### dns
- **Type**: typing.Optional[typing.Dict[str, str]]

### visibility
- **Type**: typing.Optional[typing.Literal['GLOBAL', 'PRIVATE']]

### apiType
- **Type**: typing.Optional[typing.Literal['GRAPHQL', 'MERGED']]

### mergedApiExecutionRoleArn
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]

### ownerContact
- **Type**: typing.Optional[str]

### introspectionConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### queryDepthLimit
- **Type**: typing.Optional[int]

### resolverCountLimit
- **Type**: typing.Optional[int]

### enhancedMetricsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EnhancedMetricsConfig]


# HttpDataSourceConfig

### endpoint
- **Type**: typing.Optional[str]

### authorizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AuthorizationConfig]


# LambdaAuthorizerConfig

### authorizerUri
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerResultTtlInSeconds
- **Type**: typing.Optional[int]

### identityValidationExpression
- **Type**: typing.Optional[str]


# LambdaConflictHandlerConfig

### lambdaConflictHandlerArn
- **Type**: typing.Optional[str]


# LambdaDataSourceConfig

### lambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListApiKeysRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApiKeysRequestPaginate

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListApiKeysResponse

### apiKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.ApiKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListApisRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApisRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListApisResponse

### apis
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.Api]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListChannelNamespacesRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListChannelNamespacesRequestPaginate

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListChannelNamespacesResponse

### channelNamespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.ChannelNamespace]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataSourcesRequestPaginate

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListDataSourcesResponse

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.DataSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainNamesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDomainNamesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListDomainNamesResponse

### domainNameConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFunctionsRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFunctionsRequestPaginate

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListFunctionsResponse

### functions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.FunctionConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGraphqlApisRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### apiType
- **Type**: typing.Optional[typing.Literal['GRAPHQL', 'MERGED']]

### owner
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'OTHER_ACCOUNTS']]


# ListGraphqlApisRequestPaginate

### apiType
- **Type**: typing.Optional[typing.Literal['GRAPHQL', 'MERGED']]

### owner
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'OTHER_ACCOUNTS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListGraphqlApisResponse

### graphqlApis
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.GraphqlApi]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResolversByFunctionRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListResolversByFunctionRequestPaginate

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListResolversByFunctionResponse

### resolvers
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.Resolver]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResolversRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListResolversRequestPaginate

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListResolversResponse

### resolvers
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.Resolver]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceApiAssociationsRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSourceApiAssociationsRequestPaginate

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfig]


# ListSourceApiAssociationsResponse

### sourceApiAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# LogConfig

### fieldLogLevel
- **Type**: typing.Literal['ALL', 'DEBUG', 'ERROR', 'INFO', 'NONE']
- **Required**: Yes

### cloudWatchLogsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### excludeVerboseContent
- **Type**: typing.Optional[bool]


# OpenIDConnectConfig

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: typing.Optional[str]

### iatTTL
- **Type**: typing.Optional[int]

### authTTL
- **Type**: typing.Optional[int]


# OpenSearchServiceDataSourceConfig

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PipelineConfig

### functions
- **Type**: typing.Optional[typing.Sequence[str]]


# PipelineConfigOutput

### functions
- **Type**: typing.Optional[typing.List[str]]


# PipelineConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutGraphqlApiEnvironmentVariablesRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentVariables
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# PutGraphqlApiEnvironmentVariablesResponse

### environmentVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# RdsDataApiConfig

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# RdsHttpEndpointConfig

### awsRegion
- **Type**: typing.Optional[str]

### dbClusterIdentifier
- **Type**: typing.Optional[str]

### databaseName
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### awsSecretStoreArn
- **Type**: typing.Optional[str]


# RelationalDatabaseDataSourceConfig

### relationalDatabaseSourceType
- **Type**: typing.Optional[typing.Literal['RDS_HTTP_ENDPOINT']]

### rdsHttpEndpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.RdsHttpEndpointConfig]


# Resolver

### typeName
- **Type**: typing.Optional[str]

### fieldName
- **Type**: typing.Optional[str]

### dataSourceName
- **Type**: typing.Optional[str]

### resolverArn
- **Type**: typing.Optional[str]

### requestMappingTemplate
- **Type**: typing.Optional[str]

### responseMappingTemplate
- **Type**: typing.Optional[str]

### kind
- **Type**: typing.Optional[typing.Literal['PIPELINE', 'UNIT']]

### pipelineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PipelineConfigOutput]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfig]

### cachingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CachingConfigOutput]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntime]

### code
- **Type**: typing.Optional[str]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


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


# SourceApiAssociation

### associationId
- **Type**: typing.Optional[str]

### associationArn
- **Type**: typing.Optional[str]

### sourceApiId
- **Type**: typing.Optional[str]

### sourceApiArn
- **Type**: typing.Optional[str]

### mergedApiArn
- **Type**: typing.Optional[str]

### mergedApiId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### sourceApiAssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationConfig]

### sourceApiAssociationStatus
- **Type**: typing.Optional[typing.Literal['AUTO_MERGE_SCHEDULE_FAILED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'DELETION_SCHEDULED', 'MERGE_FAILED', 'MERGE_IN_PROGRESS', 'MERGE_SCHEDULED', 'MERGE_SUCCESS']]

### sourceApiAssociationStatusDetail
- **Type**: typing.Optional[str]

### lastSuccessfulMergeDate
- **Type**: typing.Optional[datetime.datetime]


# SourceApiAssociationConfig

### mergeType
- **Type**: typing.Optional[typing.Literal['AUTO_MERGE', 'MANUAL_MERGE']]


# SourceApiAssociationSummary

### associationId
- **Type**: typing.Optional[str]

### associationArn
- **Type**: typing.Optional[str]

### sourceApiId
- **Type**: typing.Optional[str]

### sourceApiArn
- **Type**: typing.Optional[str]

### mergedApiId
- **Type**: typing.Optional[str]

### mergedApiArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# StartDataSourceIntrospectionRequest

### rdsDataApiConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.RdsDataApiConfig]


# StartDataSourceIntrospectionResponse

### introspectionId
- **Type**: <class 'str'>
- **Required**: Yes

### introspectionStatus
- **Type**: typing.Literal['FAILED', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### introspectionStatusDetail
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# StartSchemaCreationRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.Blob'>
- **Required**: Yes


# StartSchemaCreationResponse

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'NOT_APPLICABLE', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# StartSchemaMergeRequest

### associationId
- **Type**: <class 'str'>
- **Required**: Yes

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartSchemaMergeResponse

### sourceApiAssociationStatus
- **Type**: typing.Literal['AUTO_MERGE_SCHEDULE_FAILED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'DELETION_SCHEDULED', 'MERGE_FAILED', 'MERGE_IN_PROGRESS', 'MERGE_SCHEDULED', 'MERGE_SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# SyncConfig

### conflictHandler
- **Type**: typing.Optional[typing.Literal['AUTOMERGE', 'LAMBDA', 'NONE', 'OPTIMISTIC_CONCURRENCY']]

### conflictDetection
- **Type**: typing.Optional[typing.Literal['NONE', 'VERSION']]

### lambdaConflictHandlerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaConflictHandlerConfig]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApiCacheResponse

### apiCache
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiCache'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApiKeyResponse

### apiKey
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApiRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ownerContact
- **Type**: typing.Optional[str]

### eventConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventConfigUnion]


# UpdateApiResponse

### api
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.Api'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChannelNamespaceRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subscribeAuthModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]]

### publishAuthModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthMode]]

### codeHandlers
- **Type**: typing.Optional[str]


# UpdateChannelNamespaceResponse

### channelNamespace
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ChannelNamespace'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSourceResponse

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainNameRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateDomainNameResponse

### domainNameConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFunctionRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### requestMappingTemplate
- **Type**: typing.Optional[str]

### responseMappingTemplate
- **Type**: typing.Optional[str]

### functionVersion
- **Type**: typing.Optional[str]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfig]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntime]

### code
- **Type**: typing.Optional[str]


# UpdateFunctionResponse

### functionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.FunctionConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGraphqlApiRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### authenticationType
- **Type**: typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']
- **Required**: Yes

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LogConfig]

### userPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.UserPoolConfig]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfig]

### additionalAuthenticationProviders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AdditionalAuthenticationProvider]]

### xrayEnabled
- **Type**: typing.Optional[bool]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfig]

### mergedApiExecutionRoleArn
- **Type**: typing.Optional[str]

### ownerContact
- **Type**: typing.Optional[str]

### introspectionConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### queryDepthLimit
- **Type**: typing.Optional[int]

### resolverCountLimit
- **Type**: typing.Optional[int]

### enhancedMetricsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EnhancedMetricsConfig]


# UpdateGraphqlApiResponse

### graphqlApi
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.GraphqlApi'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResolverRequest

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes

### dataSourceName
- **Type**: typing.Optional[str]

### requestMappingTemplate
- **Type**: typing.Optional[str]

### responseMappingTemplate
- **Type**: typing.Optional[str]

### kind
- **Type**: typing.Optional[typing.Literal['PIPELINE', 'UNIT']]

### pipelineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PipelineConfigUnion]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfig]

### cachingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CachingConfigUnion]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntime]

### code
- **Type**: typing.Optional[str]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateResolverResponse

### resolver
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.Resolver'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSourceApiAssociationRequest

### associationId
- **Type**: <class 'str'>
- **Required**: Yes

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sourceApiAssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationConfig]


# UpdateSourceApiAssociationResponse

### sourceApiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadata'>
- **Required**: Yes


# UserPoolConfig

### userPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### defaultAction
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### appIdClientRegex
- **Type**: typing.Optional[str]


