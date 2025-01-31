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

### ttl
- **Type**: typing.Optional[int]

### apiCachingBehavior
- **Type**: typing.Optional[typing.Literal['FULL_REQUEST_CACHING', 'PER_RESOLVER_CACHING']]

### transitEncryptionEnabled
- **Type**: typing.Optional[bool]

### atRestEncryptionEnabled
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[typing.Literal['LARGE', 'LARGE_12X', 'LARGE_2X', 'LARGE_4X', 'LARGE_8X', 'MEDIUM', 'R4_2XLARGE', 'R4_4XLARGE', 'R4_8XLARGE', 'R4_LARGE', 'R4_XLARGE', 'SMALL', 'T2_MEDIUM', 'T2_SMALL', 'XLARGE']]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'MODIFYING']]

### healthMetricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ApiKeyTypeDef

### id
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### expires
- **Type**: typing.Optional[int]

### deletes
- **Type**: typing.Optional[int]


# AppSyncRuntimeTypeDef

### name
- **Type**: typing.Literal['APPSYNC_JS']
- **Required**: Yes

### runtimeVersion
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateApiRequestRequestTypeDef

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


# AssociateMergedGraphqlApiRequestRequestTypeDef

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


# AssociateSourceGraphqlApiRequestRequestTypeDef

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

# CachingConfigExtraOutputTypeDef

### ttl
- **Type**: <class 'int'>
- **Required**: Yes

### cachingKeys
- **Type**: typing.Optional[typing.List[str]]


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


# CognitoUserPoolConfigTypeDef

### userPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### awsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### appIdClientRegex
- **Type**: typing.Optional[str]


# CreateApiCacheRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### ttl
- **Type**: <class 'int'>
- **Required**: Yes

### apiCachingBehavior
- **Type**: typing.Literal['FULL_REQUEST_CACHING', 'PER_RESOLVER_CACHING']
- **Required**: Yes

### type
- **Type**: typing.Literal['LARGE', 'LARGE_12X', 'LARGE_2X', 'LARGE_4X', 'LARGE_8X', 'MEDIUM', 'R4_2XLARGE', 'R4_4XLARGE', 'R4_8XLARGE', 'R4_LARGE', 'R4_XLARGE', 'SMALL', 'T2_MEDIUM', 'T2_SMALL', 'XLARGE']
- **Required**: Yes

### transitEncryptionEnabled
- **Type**: typing.Optional[bool]

### atRestEncryptionEnabled
- **Type**: typing.Optional[bool]

### healthMetricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateApiCacheResponseTypeDef

### apiCache
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApiKeyRequestRequestTypeDef

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


# CreateDataSourceRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AMAZON_DYNAMODB', 'AMAZON_ELASTICSEARCH', 'AMAZON_EVENTBRIDGE', 'AMAZON_OPENSEARCH_SERVICE', 'AWS_LAMBDA', 'HTTP', 'NONE', 'RELATIONAL_DATABASE']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### serviceRoleArn
- **Type**: typing.Optional[str]

### dynamodbConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.DynamodbDataSourceConfigTypeDef]

### lambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaDataSourceConfigTypeDef]

### elasticsearchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.ElasticsearchDataSourceConfigTypeDef]

### openSearchServiceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenSearchServiceDataSourceConfigTypeDef]

### httpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.HttpDataSourceConfigTypeDef]

### relationalDatabaseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.RelationalDatabaseDataSourceConfigTypeDef]

### eventBridgeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventBridgeDataSourceConfigTypeDef]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainNameRequestRequestTypeDef

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


# CreateFunctionRequestRequestTypeDef

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


# CreateGraphqlApiRequestRequestTypeDef

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

### visibility
- **Type**: typing.Optional[typing.Literal['GLOBAL', 'PRIVATE']]

### apiType
- **Type**: typing.Optional[typing.Literal['GRAPHQL', 'MERGED']]

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


# CreateGraphqlApiResponseTypeDef

### graphqlApi
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.GraphqlApiTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResolverRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PipelineConfigTypeDef]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfigTypeDef]

### cachingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CachingConfigTypeDef]

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


# CreateTypeRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['JSON', 'SDL']
- **Required**: Yes


# CreateTypeResponseTypeDef

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.TypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSourceIntrospectionModelFieldTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.DataSourceIntrospectionModelFieldTypeTypeDef]

### length
- **Type**: typing.Optional[int]


# DataSourceIntrospectionModelFieldTypeTypeDef

### kind
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### values
- **Type**: typing.Optional[typing.List[str]]


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

### dataSourceArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AMAZON_DYNAMODB', 'AMAZON_ELASTICSEARCH', 'AMAZON_EVENTBRIDGE', 'AMAZON_OPENSEARCH_SERVICE', 'AWS_LAMBDA', 'HTTP', 'NONE', 'RELATIONAL_DATABASE']]

### serviceRoleArn
- **Type**: typing.Optional[str]

### dynamodbConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.DynamodbDataSourceConfigTypeDef]

### lambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaDataSourceConfigTypeDef]

### elasticsearchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.ElasticsearchDataSourceConfigTypeDef]

### openSearchServiceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenSearchServiceDataSourceConfigTypeDef]

### httpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.HttpDataSourceConfigTypeDef]

### relationalDatabaseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.RelationalDatabaseDataSourceConfigTypeDef]

### eventBridgeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventBridgeDataSourceConfigTypeDef]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DeleteApiCacheRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApiKeyRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainNameRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGraphqlApiRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResolverRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTypeRequestRequestTypeDef

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


# DisassociateApiRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMergedGraphqlApiRequestRequestTypeDef

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


# DisassociateSourceGraphqlApiRequestRequestTypeDef

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


# EvaluateCodeRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EvaluateMappingTemplateRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventBridgeDataSourceConfigTypeDef

### eventBusArn
- **Type**: <class 'str'>
- **Required**: Yes


# FlushApiCacheRequestRequestTypeDef

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


# GetApiAssociationRequestRequestTypeDef

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


# GetApiCacheRequestRequestTypeDef

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


# GetDataSourceIntrospectionRequestRequestTypeDef

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


# GetDataSourceRequestRequestTypeDef

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


# GetDomainNameRequestRequestTypeDef

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


# GetFunctionRequestRequestTypeDef

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


# GetGraphqlApiEnvironmentVariablesRequestRequestTypeDef

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


# GetGraphqlApiRequestRequestTypeDef

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


# GetIntrospectionSchemaRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['JSON', 'SDL']
- **Required**: Yes

### includeDirectives
- **Type**: typing.Optional[bool]


# GetIntrospectionSchemaResponseTypeDef

### schema
- **Type**: <class 'botocore.response.StreamingBody'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.appsync_classes.GetIntrospectionSchemaResponseTypeDef'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResolverRequestRequestTypeDef

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


# GetSchemaCreationStatusRequestRequestTypeDef

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


# GetSourceApiAssociationRequestRequestTypeDef

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


# GetTypeRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['JSON', 'SDL']
- **Required**: Yes


# GetTypeResponseTypeDef

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.TypeTypeDef'>
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


# ListApiKeysRequestListApiKeysPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListApiKeysRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourcesRequestListDataSourcesPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListDataSourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainNamesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDomainNamesResponseTypeDef

### domainNameConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.DomainNameConfigTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionsRequestListFunctionsPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListFunctionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGraphqlApisRequestListGraphqlApisPaginateTypeDef

### apiType
- **Type**: typing.Optional[typing.Literal['GRAPHQL', 'MERGED']]

### owner
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'OTHER_ACCOUNTS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListGraphqlApisRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### functionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListResolversByFunctionRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResolversRequestListResolversPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListResolversRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSourceApiAssociationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListTypesByAssociationRequestRequestTypeDef

### mergedApiIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['JSON', 'SDL']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTypesByAssociationResponseTypeDef

### types
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.TypeTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTypesRequestListTypesPaginateTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['JSON', 'SDL']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PaginatorConfigTypeDef]


# ListTypesRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['JSON', 'SDL']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTypesResponseTypeDef

### types
- **Type**: typing.List[aws_resource_validator.pydantic_models.appsync_classes.TypeTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogConfigTypeDef

### fieldLogLevel
- **Type**: typing.Literal['ALL', 'ERROR', 'NONE']
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


# PipelineConfigExtraOutputTypeDef

### functions
- **Type**: typing.Optional[typing.List[str]]


# PipelineConfigOutputTypeDef

### functions
- **Type**: typing.Optional[typing.List[str]]


# PipelineConfigTypeDef

### functions
- **Type**: typing.Optional[typing.Sequence[str]]


# PutGraphqlApiEnvironmentVariablesRequestRequestTypeDef

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


# StartDataSourceIntrospectionRequestRequestTypeDef

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


# StartSchemaCreationRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# StartSchemaCreationResponseTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'NOT_APPLICABLE', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSchemaMergeRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TypeTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### definition
- **Type**: typing.Optional[str]

### format
- **Type**: typing.Optional[typing.Literal['JSON', 'SDL']]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApiCacheRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### ttl
- **Type**: <class 'int'>
- **Required**: Yes

### apiCachingBehavior
- **Type**: typing.Literal['FULL_REQUEST_CACHING', 'PER_RESOLVER_CACHING']
- **Required**: Yes

### type
- **Type**: typing.Literal['LARGE', 'LARGE_12X', 'LARGE_2X', 'LARGE_4X', 'LARGE_8X', 'MEDIUM', 'R4_2XLARGE', 'R4_4XLARGE', 'R4_8XLARGE', 'R4_LARGE', 'R4_XLARGE', 'SMALL', 'T2_MEDIUM', 'T2_SMALL', 'XLARGE']
- **Required**: Yes

### healthMetricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateApiCacheResponseTypeDef

### apiCache
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApiKeyRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### expires
- **Type**: typing.Optional[int]


# UpdateApiKeyResponseTypeDef

### apiKey
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ApiKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSourceRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AMAZON_DYNAMODB', 'AMAZON_ELASTICSEARCH', 'AMAZON_EVENTBRIDGE', 'AMAZON_OPENSEARCH_SERVICE', 'AWS_LAMBDA', 'HTTP', 'NONE', 'RELATIONAL_DATABASE']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### serviceRoleArn
- **Type**: typing.Optional[str]

### dynamodbConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.DynamodbDataSourceConfigTypeDef]

### lambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.LambdaDataSourceConfigTypeDef]

### elasticsearchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.ElasticsearchDataSourceConfigTypeDef]

### openSearchServiceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.OpenSearchServiceDataSourceConfigTypeDef]

### httpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.HttpDataSourceConfigTypeDef]

### relationalDatabaseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.RelationalDatabaseDataSourceConfigTypeDef]

### eventBridgeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.EventBridgeDataSourceConfigTypeDef]

### metricsConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainNameRequestRequestTypeDef

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


# UpdateFunctionRequestRequestTypeDef

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


# UpdateGraphqlApiRequestRequestTypeDef

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


# UpdateResolverRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.PipelineConfigTypeDef]

### syncConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.SyncConfigTypeDef]

### cachingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appsync_classes.CachingConfigTypeDef]

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


# UpdateSourceApiAssociationRequestRequestTypeDef

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


# UpdateTypeRequestRequestTypeDef

### apiId
- **Type**: <class 'str'>
- **Required**: Yes

### typeName
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['JSON', 'SDL']
- **Required**: Yes

### definition
- **Type**: typing.Optional[str]


# UpdateTypeResponseTypeDef

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.appsync_classes.TypeTypeDef'>
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


