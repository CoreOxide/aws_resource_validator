# Appsync Classes

# AdditionalAuthenticationProviderTypeDef

### authenticationType
- **Type**: typing.Optional[typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfigTypeDef]

### userPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CognitoUserPoolConfigTypeDef]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfigTypeDef]


# ApiAssociationTypeDef

### domainName
- **Type**: typing.Optional[str]

### apiId
- **Type**: typing.Optional[str]

### associationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PROCESSING', 'SUCCESS']]

### deploymentDetail
- **Type**: typing.Optional[str]


# ApiCacheTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiKeyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventConfigOutputTypeDef]


# AppSyncRuntimeTypeDef

### name
- **Type**: typing.Literal['APPSYNC_JS']
- **Required**: Yes

### runtimeVersion
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateApiRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateApiResponseTypeDef

### apiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateMergedGraphqlApiRequestTypeDef

### sourceApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sourceApiAssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationConfigTypeDef]


# AssociateMergedGraphqlApiResponseTypeDef

### sourceApiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateSourceGraphqlApiRequestTypeDef

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sourceApiAssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationConfigTypeDef]


# AssociateSourceGraphqlApiResponseTypeDef

### sourceApiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthModeTypeDef

### authType
- **Type**: typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']
- **Required**: Yes


# AuthProviderTypeDef

### authType
- **Type**: typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']
- **Required**: Yes

### cognitoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CognitoConfigTypeDef]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfigTypeDef]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfigTypeDef]


# AuthorizationConfigTypeDef

### authorizationType
- **Type**: typing.Literal['AWS_IAM']
- **Required**: Yes

### awsIamConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AwsIamConfigTypeDef]


# AwsIamConfigTypeDef

### signingRegion
- **Type**: typing.Optional[str]

### signingServiceName
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CachingConfigOutputTypeDef

### ttl
- **Type**: <class 'int'>
- **Required**: Yes

### cachingKeys
- **Type**: typing.Optional[typing.List[str]]


# CachingConfigTypeDef

### ttl
- **Type**: <class 'int'>
- **Required**: Yes

### cachingKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# CachingConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelNamespaceTypeDef

### apiId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### subscribeAuthModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]]

### publishAuthModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]]

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


# CodeErrorLocationTypeDef

### line
- **Type**: typing.Optional[int]

### column
- **Type**: typing.Optional[int]

### span
- **Type**: typing.Optional[int]


# CodeErrorTypeDef

### errorType
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CodeErrorLocationTypeDef]


# CognitoConfigTypeDef

### userPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### appIdClientRegex
- **Type**: typing.Optional[str]


# CognitoUserPoolConfigTypeDef

### userPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### appIdClientRegex
- **Type**: typing.Optional[str]


# CreateApiCacheResponseTypeDef

### apiCache
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApiKeyRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### expires
- **Type**: typing.Optional[int]


# CreateApiKeyResponseTypeDef

### apiKey
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApiRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ownerContact
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### eventConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventConfigUnionTypeDef]


# CreateApiResponseTypeDef

### api
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelNamespaceRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subscribeAuthModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]]

### publishAuthModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]]

### codeHandlers
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChannelNamespaceResponseTypeDef

### channelNamespace
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ChannelNamespaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainNameRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateDomainNameResponseTypeDef

### domainNameConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFunctionRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfigTypeDef]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntimeTypeDef]

### code
- **Type**: typing.Optional[str]


# CreateFunctionResponseTypeDef

### functionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.FunctionConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGraphqlApiRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### authenticationType
- **Type**: typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']
- **Required**: Yes

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LogConfigTypeDef]

### userPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.UserPoolConfigTypeDef]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### additionalAuthenticationProviders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AdditionalAuthenticationProviderTypeDef]]

### xrayEnabled
- **Type**: typing.Optional[bool]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfigTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EnhancedMetricsConfigTypeDef]


# CreateGraphqlApiResponseTypeDef

### graphqlApi
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.GraphqlApiTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResolverRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PipelineConfigUnionTypeDef]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfigTypeDef]

### cachingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CachingConfigUnionTypeDef]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntimeTypeDef]

### code
- **Type**: typing.Optional[str]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateResolverResponseTypeDef

### resolver
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResolverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSourceIntrospectionModelFieldTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceIntrospectionModelIndexTypeDef

### name
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.List[str]]


# DataSourceIntrospectionModelTypeDef

### name
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModelFieldTypeDef]]

### primaryKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModelIndexTypeDef]

### indexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModelIndexTypeDef]]

### sdl
- **Type**: typing.Optional[str]


# DataSourceIntrospectionResultTypeDef

### models
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModelTypeDef]]

### nextToken
- **Type**: typing.Optional[str]


# DataSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteApiCacheRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelNamespaceRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGraphqlApiRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTypeRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeltaSyncConfigTypeDef

### baseTableTTL
- **Type**: typing.Optional[int]

### deltaSyncTableName
- **Type**: typing.Optional[str]

### deltaSyncTableTTL
- **Type**: typing.Optional[int]


# DisassociateApiRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMergedGraphqlApiRequestTypeDef

### sourceApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMergedGraphqlApiResponseTypeDef

### sourceApiAssociationStatus
- **Type**: typing.Literal['AUTO_MERGE_SCHEDULE_FAILED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'DELETION_SCHEDULED', 'MERGE_FAILED', 'MERGE_IN_PROGRESS', 'MERGE_SCHEDULED', 'MERGE_SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateSourceGraphqlApiRequestTypeDef

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateSourceGraphqlApiResponseTypeDef

### sourceApiAssociationStatus
- **Type**: typing.Literal['AUTO_MERGE_SCHEDULE_FAILED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'DELETION_SCHEDULED', 'MERGE_FAILED', 'MERGE_IN_PROGRESS', 'MERGE_SCHEDULED', 'MERGE_SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainNameConfigTypeDef

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


# DynamodbDataSourceConfigTypeDef

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### useCallerCredentials
- **Type**: typing.Optional[bool]

### deltaSyncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.DeltaSyncConfigTypeDef]

### versioned
- **Type**: typing.Optional[bool]


# ElasticsearchDataSourceConfigTypeDef

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# EnhancedMetricsConfigTypeDef

### resolverLevelMetricsBehavior
- **Type**: typing.Literal['FULL_REQUEST_RESOLVER_METRICS', 'PER_RESOLVER_METRICS']
- **Required**: Yes

### dataSourceLevelMetricsBehavior
- **Type**: typing.Literal['FULL_REQUEST_DATA_SOURCE_METRICS', 'PER_DATA_SOURCE_METRICS']
- **Required**: Yes

### operationLevelMetricsConfig
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# ErrorDetailTypeDef

### message
- **Type**: typing.Optional[str]


# EvaluateCodeErrorDetailTypeDef

### message
- **Type**: typing.Optional[str]

### codeErrors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.CodeErrorTypeDef]]


# EvaluateCodeRequestTypeDef

### runtime
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntimeTypeDef'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### context
- **Type**: <class 'str'>
- **Required**: Yes

### function
- **Type**: typing.Optional[str]


# EvaluateCodeResponseTypeDef

### evaluationResult
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.EvaluateCodeErrorDetailTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EvaluateMappingTemplateRequestTypeDef

### template
- **Type**: <class 'str'>
- **Required**: Yes

### context
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateMappingTemplateResponseTypeDef

### evaluationResult
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ErrorDetailTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventBridgeDataSourceConfigTypeDef

### eventBusArn
- **Type**: <class 'str'>
- **Required**: Yes


# EventConfigOutputTypeDef

### authProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthProviderTypeDef]
- **Required**: Yes

### connectionAuthModes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]
- **Required**: Yes

### defaultPublishAuthModes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]
- **Required**: Yes

### defaultSubscribeAuthModes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]
- **Required**: Yes

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventLogConfigTypeDef]


# EventConfigTypeDef

### authProviders
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthProviderTypeDef]
- **Required**: Yes

### connectionAuthModes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]
- **Required**: Yes

### defaultPublishAuthModes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]
- **Required**: Yes

### defaultSubscribeAuthModes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]
- **Required**: Yes

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventLogConfigTypeDef]


# EventConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventLogConfigTypeDef

### logLevel
- **Type**: typing.Literal['ALL', 'DEBUG', 'ERROR', 'INFO', 'NONE']
- **Required**: Yes

### cloudWatchLogsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# FlushApiCacheRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# FunctionConfigurationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfigTypeDef]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntimeTypeDef]

### code
- **Type**: typing.Optional[str]


# GetApiAssociationRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiAssociationResponseTypeDef

### apiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApiCacheRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiCacheResponseTypeDef

### apiCache
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApiRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApiResponseTypeDef

### api
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelNamespaceRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelNamespaceResponseTypeDef

### channelNamespace
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ChannelNamespaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSourceIntrospectionRequestTypeDef

### introspectionId
- **Type**: <class 'str'>
- **Required**: Yes

### includeModelsSDL
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetDataSourceIntrospectionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSourceRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainNameRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainNameResponseTypeDef

### domainNameConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionResponseTypeDef

### functionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.FunctionConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGraphqlApiEnvironmentVariablesRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphqlApiEnvironmentVariablesResponseTypeDef

### environmentVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGraphqlApiRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGraphqlApiResponseTypeDef

### graphqlApi
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.GraphqlApiTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntrospectionSchemaResponseTypeDef

### schema
- **Type**: <class 'botocore.response.StreamingBody'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.appsync_classes.GetIntrospectionSchemaResponseTypeDef'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes


# GetResolverResponseTypeDef

### resolver
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResolverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSchemaCreationStatusRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaCreationStatusResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'NOT_APPLICABLE', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### details
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSourceApiAssociationRequestTypeDef

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSourceApiAssociationResponseTypeDef

### sourceApiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GraphqlApiTypeDef

### name
- **Type**: typing.Optional[str]

### apiId
- **Type**: typing.Optional[str]

### authenticationType
- **Type**: typing.Optional[typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'AWS_LAMBDA', 'OPENID_CONNECT']]

### logConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LogConfigTypeDef]

### userPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.UserPoolConfigTypeDef]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfigTypeDef]

### arn
- **Type**: typing.Optional[str]

### uris
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### additionalAuthenticationProviders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appsync_classes.AdditionalAuthenticationProviderTypeDef]]

### xrayEnabled
- **Type**: typing.Optional[bool]

### wafWebAclArn
- **Type**: typing.Optional[str]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfigTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EnhancedMetricsConfigTypeDef]


# HttpDataSourceConfigTypeDef

### endpoint
- **Type**: typing.Optional[str]

### authorizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AuthorizationConfigTypeDef]


# LambdaAuthorizerConfigTypeDef

### authorizerUri
- **Type**: <class 'str'>
- **Required**: Yes

### authorizerResultTtlInSeconds
- **Type**: typing.Optional[int]

### identityValidationExpression
- **Type**: typing.Optional[str]


# LambdaConflictHandlerConfigTypeDef

### lambdaConflictHandlerArn
- **Type**: typing.Optional[str]


# LambdaDataSourceConfigTypeDef

### lambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListApiKeysRequestPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListApiKeysRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApiKeysResponseTypeDef

### apiKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.ApiKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListApisRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListApisRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApisResponseTypeDef

### apis
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.ApiTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListChannelNamespacesRequestPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListChannelNamespacesRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListChannelNamespacesResponseTypeDef

### channelNamespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.ChannelNamespaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequestPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListDataSourcesRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataSourcesResponseTypeDef

### dataSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.DataSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainNamesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListDomainNamesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDomainNamesResponseTypeDef

### domainNameConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFunctionsRequestPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListFunctionsRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFunctionsResponseTypeDef

### functions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.FunctionConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGraphqlApisRequestPaginateTypeDef

### apiType
- **Type**: typing.Optional[typing.Literal['GRAPHQL', 'MERGED']]

### owner
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'OTHER_ACCOUNTS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListGraphqlApisRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### apiType
- **Type**: typing.Optional[typing.Literal['GRAPHQL', 'MERGED']]

### owner
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'OTHER_ACCOUNTS']]


# ListGraphqlApisResponseTypeDef

### graphqlApis
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.GraphqlApiTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResolversByFunctionRequestPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListResolversByFunctionRequestTypeDef

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


# ListResolversByFunctionResponseTypeDef

### resolvers
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.ResolverTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResolversRequestPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListResolversRequestTypeDef

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


# ListResolversResponseTypeDef

### resolvers
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.ResolverTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceApiAssociationsRequestPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListSourceApiAssociationsRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSourceApiAssociationsResponseTypeDef

### sourceApiAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogConfigTypeDef

### fieldLogLevel
- **Type**: typing.Literal['ALL', 'DEBUG', 'ERROR', 'INFO', 'NONE']
- **Required**: Yes

### cloudWatchLogsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### excludeVerboseContent
- **Type**: typing.Optional[bool]


# OpenIDConnectConfigTypeDef

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: typing.Optional[str]

### iatTTL
- **Type**: typing.Optional[int]

### authTTL
- **Type**: typing.Optional[int]


# OpenSearchServiceDataSourceConfigTypeDef

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PipelineConfigOutputTypeDef

### functions
- **Type**: typing.Optional[typing.List[str]]


# PipelineConfigTypeDef

### functions
- **Type**: typing.Optional[typing.Sequence[str]]


# PipelineConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutGraphqlApiEnvironmentVariablesRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentVariables
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# PutGraphqlApiEnvironmentVariablesResponseTypeDef

### environmentVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RdsDataApiConfigTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# RdsHttpEndpointConfigTypeDef

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


# RelationalDatabaseDataSourceConfigTypeDef

### relationalDatabaseSourceType
- **Type**: typing.Optional[typing.Literal['RDS_HTTP_ENDPOINT']]

### rdsHttpEndpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.RdsHttpEndpointConfigTypeDef]


# ResolverTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PipelineConfigOutputTypeDef]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfigTypeDef]

### cachingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CachingConfigOutputTypeDef]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntimeTypeDef]

### code
- **Type**: typing.Optional[str]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


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


# SourceApiAssociationConfigTypeDef

### mergeType
- **Type**: typing.Optional[typing.Literal['AUTO_MERGE', 'MANUAL_MERGE']]


# SourceApiAssociationSummaryTypeDef

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


# SourceApiAssociationTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationConfigTypeDef]

### sourceApiAssociationStatus
- **Type**: typing.Optional[typing.Literal['AUTO_MERGE_SCHEDULE_FAILED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'DELETION_SCHEDULED', 'MERGE_FAILED', 'MERGE_IN_PROGRESS', 'MERGE_SCHEDULED', 'MERGE_SUCCESS']]

### sourceApiAssociationStatusDetail
- **Type**: typing.Optional[str]

### lastSuccessfulMergeDate
- **Type**: typing.Optional[datetime.datetime]


# StartDataSourceIntrospectionRequestTypeDef

### rdsDataApiConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.RdsDataApiConfigTypeDef]


# StartDataSourceIntrospectionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSchemaCreationRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.BlobTypeDef'>
- **Required**: Yes


# StartSchemaCreationResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'NOT_APPLICABLE', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSchemaMergeRequestTypeDef

### associationId
- **Type**: <class 'str'>
- **Required**: Yes

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartSchemaMergeResponseTypeDef

### sourceApiAssociationStatus
- **Type**: typing.Literal['AUTO_MERGE_SCHEDULE_FAILED', 'DELETION_FAILED', 'DELETION_IN_PROGRESS', 'DELETION_SCHEDULED', 'MERGE_FAILED', 'MERGE_IN_PROGRESS', 'MERGE_SCHEDULED', 'MERGE_SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SyncConfigTypeDef

### conflictHandler
- **Type**: typing.Optional[typing.Literal['AUTOMERGE', 'LAMBDA', 'NONE', 'OPTIMISTIC_CONCURRENCY']]

### conflictDetection
- **Type**: typing.Optional[typing.Literal['NONE', 'VERSION']]

### lambdaConflictHandlerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaConflictHandlerConfigTypeDef]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApiCacheResponseTypeDef

### apiCache
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApiKeyResponseTypeDef

### apiKey
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApiRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ownerContact
- **Type**: typing.Optional[str]

### eventConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventConfigUnionTypeDef]


# UpdateApiResponseTypeDef

### api
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelNamespaceRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subscribeAuthModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]]

### publishAuthModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AuthModeTypeDef]]

### codeHandlers
- **Type**: typing.Optional[str]


# UpdateChannelNamespaceResponseTypeDef

### channelNamespace
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ChannelNamespaceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainNameRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateDomainNameResponseTypeDef

### domainNameConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFunctionRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfigTypeDef]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntimeTypeDef]

### code
- **Type**: typing.Optional[str]


# UpdateFunctionResponseTypeDef

### functionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.FunctionConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGraphqlApiRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LogConfigTypeDef]

### userPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.UserPoolConfigTypeDef]

### openIDConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenIDConnectConfigTypeDef]

### additionalAuthenticationProviders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appsync_classes.AdditionalAuthenticationProviderTypeDef]]

### xrayEnabled
- **Type**: typing.Optional[bool]

### lambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaAuthorizerConfigTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EnhancedMetricsConfigTypeDef]


# UpdateGraphqlApiResponseTypeDef

### graphqlApi
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.GraphqlApiTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResolverRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PipelineConfigUnionTypeDef]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfigTypeDef]

### cachingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CachingConfigUnionTypeDef]

### maxBatchSize
- **Type**: typing.Optional[int]

### runtime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.AppSyncRuntimeTypeDef]

### code
- **Type**: typing.Optional[str]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateResolverResponseTypeDef

### resolver
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResolverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSourceApiAssociationRequestTypeDef

### associationId
- **Type**: <class 'str'>
- **Required**: Yes

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### sourceApiAssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationConfigTypeDef]


# UpdateSourceApiAssociationResponseTypeDef

### sourceApiAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.SourceApiAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserPoolConfigTypeDef

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


