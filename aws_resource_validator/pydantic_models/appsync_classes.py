from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.appsync_constants import *

class CognitoUserPoolConfigTypeDef(BaseModel):
    userPoolId: str
    awsRegion: str
    appIdClientRegex: Optional[str] = None

class LambdaAuthorizerConfigTypeDef(BaseModel):
    authorizerUri: str
    authorizerResultTtlInSeconds: Optional[int] = None
    identityValidationExpression: Optional[str] = None

class OpenIDConnectConfigTypeDef(BaseModel):
    issuer: str
    clientId: Optional[str] = None
    iatTTL: Optional[int] = None
    authTTL: Optional[int] = None

class ApiAssociationTypeDef(BaseModel):
    domainName: Optional[str] = None
    apiId: Optional[str] = None
    associationStatus: Optional[AssociationStatusType] = None
    deploymentDetail: Optional[str] = None

class ApiCacheTypeDef(BaseModel):
    ttl: Optional[int] = None
    apiCachingBehavior: Optional[ApiCachingBehaviorType] = None
    transitEncryptionEnabled: Optional[bool] = None
    atRestEncryptionEnabled: Optional[bool] = None
    type: Optional[ApiCacheTypeType] = None
    status: Optional[ApiCacheStatusType] = None
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None

class ApiKeyTypeDef(BaseModel):
    id: Optional[str] = None
    description: Optional[str] = None
    expires: Optional[int] = None
    deletes: Optional[int] = None

class AppSyncRuntimeTypeDef(BaseModel):
    name: Literal["APPSYNC_JS"]
    runtimeVersion: str

class AssociateApiRequestRequestTypeDef(BaseModel):
    domainName: str
    apiId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SourceApiAssociationConfigTypeDef(BaseModel):
    mergeType: Optional[MergeTypeType] = None

class AwsIamConfigTypeDef(BaseModel):
    signingRegion: Optional[str] = None
    signingServiceName: Optional[str] = None

class CachingConfigExtraOutputTypeDef(BaseModel):
    ttl: int
    cachingKeys: Optional[List[str]] = None

class CachingConfigOutputTypeDef(BaseModel):
    ttl: int
    cachingKeys: Optional[List[str]] = None

class CachingConfigTypeDef(BaseModel):
    ttl: int
    cachingKeys: Optional[Sequence[str]] = None

class CodeErrorLocationTypeDef(BaseModel):
    line: Optional[int] = None
    column: Optional[int] = None
    span: Optional[int] = None

class CreateApiCacheRequestRequestTypeDef(BaseModel):
    apiId: str
    ttl: int
    apiCachingBehavior: ApiCachingBehaviorType
    type: ApiCacheTypeType
    transitEncryptionEnabled: Optional[bool] = None
    atRestEncryptionEnabled: Optional[bool] = None
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None

class CreateApiKeyRequestRequestTypeDef(BaseModel):
    apiId: str
    description: Optional[str] = None
    expires: Optional[int] = None

class ElasticsearchDataSourceConfigTypeDef(BaseModel):
    endpoint: str
    awsRegion: str

class EventBridgeDataSourceConfigTypeDef(BaseModel):
    eventBusArn: str

class LambdaDataSourceConfigTypeDef(BaseModel):
    lambdaFunctionArn: str

class OpenSearchServiceDataSourceConfigTypeDef(BaseModel):
    endpoint: str
    awsRegion: str

class CreateDomainNameRequestRequestTypeDef(BaseModel):
    domainName: str
    certificateArn: str
    description: Optional[str] = None

class DomainNameConfigTypeDef(BaseModel):
    domainName: Optional[str] = None
    description: Optional[str] = None
    certificateArn: Optional[str] = None
    appsyncDomainName: Optional[str] = None
    hostedZoneId: Optional[str] = None

class EnhancedMetricsConfigTypeDef(BaseModel):
    resolverLevelMetricsBehavior: ResolverLevelMetricsBehaviorType
    dataSourceLevelMetricsBehavior: DataSourceLevelMetricsBehaviorType
    operationLevelMetricsConfig: OperationLevelMetricsConfigType

class LogConfigTypeDef(BaseModel):
    fieldLogLevel: FieldLogLevelType
    cloudWatchLogsRoleArn: str
    excludeVerboseContent: Optional[bool] = None

class UserPoolConfigTypeDef(BaseModel):
    userPoolId: str
    awsRegion: str
    defaultAction: DefaultActionType
    appIdClientRegex: Optional[str] = None

class PipelineConfigTypeDef(BaseModel):
    functions: Optional[Sequence[str]] = None

class CreateTypeRequestRequestTypeDef(BaseModel):
    apiId: str
    definition: str
    format: TypeDefinitionFormatType

class TypeTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    arn: Optional[str] = None
    definition: Optional[str] = None
    format: Optional[TypeDefinitionFormatType] = None

class DataSourceIntrospectionModelFieldTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional["DataSourceIntrospectionModelFieldTypeTypeDef"] = None
    length: Optional[int] = None

class DataSourceIntrospectionModelFieldTypeTypeDef(BaseModel):
    kind: Optional[str] = None
    name: Optional[str] = None
    type: Optional[Dict[str, Any]] = None
    values: Optional[List[str]] = None

class DataSourceIntrospectionModelIndexTypeDef(BaseModel):
    name: Optional[str] = None
    fields: Optional[List[str]] = None

class DeleteApiCacheRequestRequestTypeDef(BaseModel):
    apiId: str

class DeleteApiKeyRequestRequestTypeDef(BaseModel):
    apiId: str
    id: str

class DeleteDataSourceRequestRequestTypeDef(BaseModel):
    apiId: str
    name: str

class DeleteDomainNameRequestRequestTypeDef(BaseModel):
    domainName: str

class DeleteFunctionRequestRequestTypeDef(BaseModel):
    apiId: str
    functionId: str

class DeleteGraphqlApiRequestRequestTypeDef(BaseModel):
    apiId: str

class DeleteResolverRequestRequestTypeDef(BaseModel):
    apiId: str
    typeName: str
    fieldName: str

class DeleteTypeRequestRequestTypeDef(BaseModel):
    apiId: str
    typeName: str

class DeltaSyncConfigTypeDef(BaseModel):
    baseTableTTL: Optional[int] = None
    deltaSyncTableName: Optional[str] = None
    deltaSyncTableTTL: Optional[int] = None

class DisassociateApiRequestRequestTypeDef(BaseModel):
    domainName: str

class DisassociateMergedGraphqlApiRequestRequestTypeDef(BaseModel):
    sourceApiIdentifier: str
    associationId: str

class DisassociateSourceGraphqlApiRequestRequestTypeDef(BaseModel):
    mergedApiIdentifier: str
    associationId: str

class ErrorDetailTypeDef(BaseModel):
    message: Optional[str] = None

class EvaluateMappingTemplateRequestRequestTypeDef(BaseModel):
    template: str
    context: str

class FlushApiCacheRequestRequestTypeDef(BaseModel):
    apiId: str

class GetApiAssociationRequestRequestTypeDef(BaseModel):
    domainName: str

class GetApiCacheRequestRequestTypeDef(BaseModel):
    apiId: str

class GetDataSourceIntrospectionRequestRequestTypeDef(BaseModel):
    introspectionId: str
    includeModelsSDL: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetDataSourceRequestRequestTypeDef(BaseModel):
    apiId: str
    name: str

class GetDomainNameRequestRequestTypeDef(BaseModel):
    domainName: str

class GetFunctionRequestRequestTypeDef(BaseModel):
    apiId: str
    functionId: str

class GetGraphqlApiEnvironmentVariablesRequestRequestTypeDef(BaseModel):
    apiId: str

class GetGraphqlApiRequestRequestTypeDef(BaseModel):
    apiId: str

class GetIntrospectionSchemaRequestRequestTypeDef(BaseModel):
    apiId: str
    format: OutputTypeType
    includeDirectives: Optional[bool] = None

class GetResolverRequestRequestTypeDef(BaseModel):
    apiId: str
    typeName: str
    fieldName: str

class GetSchemaCreationStatusRequestRequestTypeDef(BaseModel):
    apiId: str

class GetSourceApiAssociationRequestRequestTypeDef(BaseModel):
    mergedApiIdentifier: str
    associationId: str

class GetTypeRequestRequestTypeDef(BaseModel):
    apiId: str
    typeName: str
    format: TypeDefinitionFormatType

class LambdaConflictHandlerConfigTypeDef(BaseModel):
    lambdaConflictHandlerArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApiKeysRequestRequestTypeDef(BaseModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDataSourcesRequestRequestTypeDef(BaseModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDomainNamesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFunctionsRequestRequestTypeDef(BaseModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListGraphqlApisRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    apiType: Optional[GraphQLApiTypeType] = None
    owner: Optional[OwnershipType] = None

class ListResolversByFunctionRequestRequestTypeDef(BaseModel):
    apiId: str
    functionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListResolversRequestRequestTypeDef(BaseModel):
    apiId: str
    typeName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSourceApiAssociationsRequestRequestTypeDef(BaseModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SourceApiAssociationSummaryTypeDef(BaseModel):
    associationId: Optional[str] = None
    associationArn: Optional[str] = None
    sourceApiId: Optional[str] = None
    sourceApiArn: Optional[str] = None
    mergedApiId: Optional[str] = None
    mergedApiArn: Optional[str] = None
    description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTypesByAssociationRequestRequestTypeDef(BaseModel):
    mergedApiIdentifier: str
    associationId: str
    format: TypeDefinitionFormatType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTypesRequestRequestTypeDef(BaseModel):
    apiId: str
    format: TypeDefinitionFormatType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PipelineConfigExtraOutputTypeDef(BaseModel):
    functions: Optional[List[str]] = None

class PipelineConfigOutputTypeDef(BaseModel):
    functions: Optional[List[str]] = None

class PutGraphqlApiEnvironmentVariablesRequestRequestTypeDef(BaseModel):
    apiId: str
    environmentVariables: Mapping[str, str]

class RdsDataApiConfigTypeDef(BaseModel):
    resourceArn: str
    secretArn: str
    databaseName: str

class RdsHttpEndpointConfigTypeDef(BaseModel):
    awsRegion: Optional[str] = None
    dbClusterIdentifier: Optional[str] = None
    databaseName: Optional[str] = None
    schema: Optional[str] = None
    awsSecretStoreArn: Optional[str] = None

class StartSchemaMergeRequestRequestTypeDef(BaseModel):
    associationId: str
    mergedApiIdentifier: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApiCacheRequestRequestTypeDef(BaseModel):
    apiId: str
    ttl: int
    apiCachingBehavior: ApiCachingBehaviorType
    type: ApiCacheTypeType
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None

class UpdateApiKeyRequestRequestTypeDef(BaseModel):
    apiId: str
    id: str
    description: Optional[str] = None
    expires: Optional[int] = None

class UpdateDomainNameRequestRequestTypeDef(BaseModel):
    domainName: str
    description: Optional[str] = None

class UpdateTypeRequestRequestTypeDef(BaseModel):
    apiId: str
    typeName: str
    format: TypeDefinitionFormatType
    definition: Optional[str] = None

class AdditionalAuthenticationProviderTypeDef(BaseModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    userPoolConfig: Optional[CognitoUserPoolConfigTypeDef] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfigTypeDef] = None

class EvaluateCodeRequestRequestTypeDef(BaseModel):
    runtime: AppSyncRuntimeTypeDef
    code: str
    context: str
    function: Optional[str] = None

class AssociateApiResponseTypeDef(BaseModel):
    apiAssociation: ApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiCacheResponseTypeDef(BaseModel):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiKeyResponseTypeDef(BaseModel):
    apiKey: ApiKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateMergedGraphqlApiResponseTypeDef(BaseModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateSourceGraphqlApiResponseTypeDef(BaseModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiAssociationResponseTypeDef(BaseModel):
    apiAssociation: ApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiCacheResponseTypeDef(BaseModel):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphqlApiEnvironmentVariablesResponseTypeDef(BaseModel):
    environmentVariables: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntrospectionSchemaResponseTypeDef(BaseModel):
    schema: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaCreationStatusResponseTypeDef(BaseModel):
    status: SchemaStatusType
    details: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApiKeysResponseTypeDef(BaseModel):
    apiKeys: List[ApiKeyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutGraphqlApiEnvironmentVariablesResponseTypeDef(BaseModel):
    environmentVariables: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceIntrospectionResponseTypeDef(BaseModel):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaCreationResponseTypeDef(BaseModel):
    status: SchemaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaMergeResponseTypeDef(BaseModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiCacheResponseTypeDef(BaseModel):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiKeyResponseTypeDef(BaseModel):
    apiKey: ApiKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateMergedGraphqlApiRequestRequestTypeDef(BaseModel):
    sourceApiIdentifier: str
    mergedApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None

class AssociateSourceGraphqlApiRequestRequestTypeDef(BaseModel):
    mergedApiIdentifier: str
    sourceApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None

class SourceApiAssociationTypeDef(BaseModel):
    associationId: Optional[str] = None
    associationArn: Optional[str] = None
    sourceApiId: Optional[str] = None
    sourceApiArn: Optional[str] = None
    mergedApiArn: Optional[str] = None
    mergedApiId: Optional[str] = None
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None
    sourceApiAssociationStatus: Optional[SourceApiAssociationStatusType] = None
    sourceApiAssociationStatusDetail: Optional[str] = None
    lastSuccessfulMergeDate: Optional[datetime] = None

class UpdateSourceApiAssociationRequestRequestTypeDef(BaseModel):
    associationId: str
    mergedApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None

class AuthorizationConfigTypeDef(BaseModel):
    authorizationType: Literal["AWS_IAM"]
    awsIamConfig: Optional[AwsIamConfigTypeDef] = None

class StartSchemaCreationRequestRequestTypeDef(BaseModel):
    apiId: str
    definition: BlobTypeDef

class CodeErrorTypeDef(BaseModel):
    errorType: Optional[str] = None
    value: Optional[str] = None
    location: Optional[CodeErrorLocationTypeDef] = None

class CreateDomainNameResponseTypeDef(BaseModel):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainNameResponseTypeDef(BaseModel):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainNamesResponseTypeDef(BaseModel):
    domainNameConfigs: List[DomainNameConfigTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameResponseTypeDef(BaseModel):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTypeResponseTypeDef(BaseModel):
    type: TypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTypeResponseTypeDef(BaseModel):
    type: TypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTypesByAssociationResponseTypeDef(BaseModel):
    types: List[TypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTypesResponseTypeDef(BaseModel):
    types: List[TypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTypeResponseTypeDef(BaseModel):
    type: TypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceIntrospectionModelTypeDef(BaseModel):
    name: Optional[str] = None
    fields: Optional[List[DataSourceIntrospectionModelFieldTypeDef]] = None
    primaryKey: Optional[DataSourceIntrospectionModelIndexTypeDef] = None
    indexes: Optional[List[DataSourceIntrospectionModelIndexTypeDef]] = None
    sdl: Optional[str] = None

class DynamodbDataSourceConfigTypeDef(BaseModel):
    tableName: str
    awsRegion: str
    useCallerCredentials: Optional[bool] = None
    deltaSyncConfig: Optional[DeltaSyncConfigTypeDef] = None
    versioned: Optional[bool] = None

class EvaluateMappingTemplateResponseTypeDef(BaseModel):
    evaluationResult: str
    error: ErrorDetailTypeDef
    logs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SyncConfigTypeDef(BaseModel):
    conflictHandler: Optional[ConflictHandlerTypeType] = None
    conflictDetection: Optional[ConflictDetectionTypeType] = None
    lambdaConflictHandlerConfig: Optional[LambdaConflictHandlerConfigTypeDef] = None

class ListApiKeysRequestListApiKeysPaginateTypeDef(BaseModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(BaseModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionsRequestListFunctionsPaginateTypeDef(BaseModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGraphqlApisRequestListGraphqlApisPaginateTypeDef(BaseModel):
    apiType: Optional[GraphQLApiTypeType] = None
    owner: Optional[OwnershipType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef(BaseModel):
    apiId: str
    functionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolversRequestListResolversPaginateTypeDef(BaseModel):
    apiId: str
    typeName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTypesRequestListTypesPaginateTypeDef(BaseModel):
    apiId: str
    format: TypeDefinitionFormatType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceApiAssociationsResponseTypeDef(BaseModel):
    sourceApiAssociationSummaries: List[SourceApiAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceIntrospectionRequestRequestTypeDef(BaseModel):
    rdsDataApiConfig: Optional[RdsDataApiConfigTypeDef] = None

class RelationalDatabaseDataSourceConfigTypeDef(BaseModel):
    relationalDatabaseSourceType: Optional[Literal["RDS_HTTP_ENDPOINT"]] = None
    rdsHttpEndpointConfig: Optional[RdsHttpEndpointConfigTypeDef] = None

class CreateGraphqlApiRequestRequestTypeDef(BaseModel):
    name: str
    authenticationType: AuthenticationTypeType
    logConfig: Optional[LogConfigTypeDef] = None
    userPoolConfig: Optional[UserPoolConfigTypeDef] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    additionalAuthenticationProviders: Optional[       Sequence[AdditionalAuthenticationProviderTypeDef]     ] = None
    xrayEnabled: Optional[bool] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfigTypeDef] = None
    visibility: Optional[GraphQLApiVisibilityType] = None
    apiType: Optional[GraphQLApiTypeType] = None
    mergedApiExecutionRoleArn: Optional[str] = None
    ownerContact: Optional[str] = None
    introspectionConfig: Optional[GraphQLApiIntrospectionConfigType] = None
    queryDepthLimit: Optional[int] = None
    resolverCountLimit: Optional[int] = None
    enhancedMetricsConfig: Optional[EnhancedMetricsConfigTypeDef] = None

class GraphqlApiTypeDef(BaseModel):
    name: Optional[str] = None
    apiId: Optional[str] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    logConfig: Optional[LogConfigTypeDef] = None
    userPoolConfig: Optional[UserPoolConfigTypeDef] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    arn: Optional[str] = None
    uris: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    additionalAuthenticationProviders: Optional[       List[AdditionalAuthenticationProviderTypeDef]     ] = None
    xrayEnabled: Optional[bool] = None
    wafWebAclArn: Optional[str] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfigTypeDef] = None
    dns: Optional[Dict[str, str]] = None
    visibility: Optional[GraphQLApiVisibilityType] = None
    apiType: Optional[GraphQLApiTypeType] = None
    mergedApiExecutionRoleArn: Optional[str] = None
    owner: Optional[str] = None
    ownerContact: Optional[str] = None
    introspectionConfig: Optional[GraphQLApiIntrospectionConfigType] = None
    queryDepthLimit: Optional[int] = None
    resolverCountLimit: Optional[int] = None
    enhancedMetricsConfig: Optional[EnhancedMetricsConfigTypeDef] = None

class UpdateGraphqlApiRequestRequestTypeDef(BaseModel):
    apiId: str
    name: str
    authenticationType: AuthenticationTypeType
    logConfig: Optional[LogConfigTypeDef] = None
    userPoolConfig: Optional[UserPoolConfigTypeDef] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    additionalAuthenticationProviders: Optional[       Sequence[AdditionalAuthenticationProviderTypeDef]     ] = None
    xrayEnabled: Optional[bool] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfigTypeDef] = None
    mergedApiExecutionRoleArn: Optional[str] = None
    ownerContact: Optional[str] = None
    introspectionConfig: Optional[GraphQLApiIntrospectionConfigType] = None
    queryDepthLimit: Optional[int] = None
    resolverCountLimit: Optional[int] = None
    enhancedMetricsConfig: Optional[EnhancedMetricsConfigTypeDef] = None

class AssociateMergedGraphqlApiResponseTypeDef(BaseModel):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSourceGraphqlApiResponseTypeDef(BaseModel):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceApiAssociationResponseTypeDef(BaseModel):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSourceApiAssociationResponseTypeDef(BaseModel):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HttpDataSourceConfigTypeDef(BaseModel):
    endpoint: Optional[str] = None
    authorizationConfig: Optional[AuthorizationConfigTypeDef] = None

class EvaluateCodeErrorDetailTypeDef(BaseModel):
    message: Optional[str] = None
    codeErrors: Optional[List[CodeErrorTypeDef]] = None

class DataSourceIntrospectionResultTypeDef(BaseModel):
    models: Optional[List[DataSourceIntrospectionModelTypeDef]] = None
    nextToken: Optional[str] = None

class CreateFunctionRequestRequestTypeDef(BaseModel):
    apiId: str
    name: str
    dataSourceName: str
    description: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    functionVersion: Optional[str] = None
    syncConfig: Optional[SyncConfigTypeDef] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntimeTypeDef] = None
    code: Optional[str] = None

class CreateResolverRequestRequestTypeDef(BaseModel):
    apiId: str
    typeName: str
    fieldName: str
    dataSourceName: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    kind: Optional[ResolverKindType] = None
    pipelineConfig: Optional[PipelineConfigTypeDef] = None
    syncConfig: Optional[SyncConfigTypeDef] = None
    cachingConfig: Optional[CachingConfigTypeDef] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntimeTypeDef] = None
    code: Optional[str] = None
    metricsConfig: Optional[ResolverLevelMetricsConfigType] = None

class FunctionConfigurationTypeDef(BaseModel):
    functionId: Optional[str] = None
    functionArn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dataSourceName: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    functionVersion: Optional[str] = None
    syncConfig: Optional[SyncConfigTypeDef] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntimeTypeDef] = None
    code: Optional[str] = None

class ResolverTypeDef(BaseModel):
    typeName: Optional[str] = None
    fieldName: Optional[str] = None
    dataSourceName: Optional[str] = None
    resolverArn: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    kind: Optional[ResolverKindType] = None
    pipelineConfig: Optional[PipelineConfigOutputTypeDef] = None
    syncConfig: Optional[SyncConfigTypeDef] = None
    cachingConfig: Optional[CachingConfigOutputTypeDef] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntimeTypeDef] = None
    code: Optional[str] = None
    metricsConfig: Optional[ResolverLevelMetricsConfigType] = None

class UpdateFunctionRequestRequestTypeDef(BaseModel):
    apiId: str
    name: str
    functionId: str
    dataSourceName: str
    description: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    functionVersion: Optional[str] = None
    syncConfig: Optional[SyncConfigTypeDef] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntimeTypeDef] = None
    code: Optional[str] = None

class UpdateResolverRequestRequestTypeDef(BaseModel):
    apiId: str
    typeName: str
    fieldName: str
    dataSourceName: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    kind: Optional[ResolverKindType] = None
    pipelineConfig: Optional[PipelineConfigTypeDef] = None
    syncConfig: Optional[SyncConfigTypeDef] = None
    cachingConfig: Optional[CachingConfigTypeDef] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntimeTypeDef] = None
    code: Optional[str] = None
    metricsConfig: Optional[ResolverLevelMetricsConfigType] = None

class CreateGraphqlApiResponseTypeDef(BaseModel):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphqlApiResponseTypeDef(BaseModel):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGraphqlApisResponseTypeDef(BaseModel):
    graphqlApis: List[GraphqlApiTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGraphqlApiResponseTypeDef(BaseModel):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceRequestRequestTypeDef(BaseModel):
    apiId: str
    name: str
    type: DataSourceTypeType
    description: Optional[str] = None
    serviceRoleArn: Optional[str] = None
    dynamodbConfig: Optional[DynamodbDataSourceConfigTypeDef] = None
    lambdaConfig: Optional[LambdaDataSourceConfigTypeDef] = None
    elasticsearchConfig: Optional[ElasticsearchDataSourceConfigTypeDef] = None
    openSearchServiceConfig: Optional[OpenSearchServiceDataSourceConfigTypeDef] = None
    httpConfig: Optional[HttpDataSourceConfigTypeDef] = None
    relationalDatabaseConfig: Optional[RelationalDatabaseDataSourceConfigTypeDef] = None
    eventBridgeConfig: Optional[EventBridgeDataSourceConfigTypeDef] = None
    metricsConfig: Optional[DataSourceLevelMetricsConfigType] = None

class DataSourceTypeDef(BaseModel):
    dataSourceArn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[DataSourceTypeType] = None
    serviceRoleArn: Optional[str] = None
    dynamodbConfig: Optional[DynamodbDataSourceConfigTypeDef] = None
    lambdaConfig: Optional[LambdaDataSourceConfigTypeDef] = None
    elasticsearchConfig: Optional[ElasticsearchDataSourceConfigTypeDef] = None
    openSearchServiceConfig: Optional[OpenSearchServiceDataSourceConfigTypeDef] = None
    httpConfig: Optional[HttpDataSourceConfigTypeDef] = None
    relationalDatabaseConfig: Optional[RelationalDatabaseDataSourceConfigTypeDef] = None
    eventBridgeConfig: Optional[EventBridgeDataSourceConfigTypeDef] = None
    metricsConfig: Optional[DataSourceLevelMetricsConfigType] = None

class UpdateDataSourceRequestRequestTypeDef(BaseModel):
    apiId: str
    name: str
    type: DataSourceTypeType
    description: Optional[str] = None
    serviceRoleArn: Optional[str] = None
    dynamodbConfig: Optional[DynamodbDataSourceConfigTypeDef] = None
    lambdaConfig: Optional[LambdaDataSourceConfigTypeDef] = None
    elasticsearchConfig: Optional[ElasticsearchDataSourceConfigTypeDef] = None
    openSearchServiceConfig: Optional[OpenSearchServiceDataSourceConfigTypeDef] = None
    httpConfig: Optional[HttpDataSourceConfigTypeDef] = None
    relationalDatabaseConfig: Optional[RelationalDatabaseDataSourceConfigTypeDef] = None
    eventBridgeConfig: Optional[EventBridgeDataSourceConfigTypeDef] = None
    metricsConfig: Optional[DataSourceLevelMetricsConfigType] = None

class EvaluateCodeResponseTypeDef(BaseModel):
    evaluationResult: str
    error: EvaluateCodeErrorDetailTypeDef
    logs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceIntrospectionResponseTypeDef(BaseModel):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    introspectionResult: DataSourceIntrospectionResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionResponseTypeDef(BaseModel):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionResponseTypeDef(BaseModel):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsResponseTypeDef(BaseModel):
    functions: List[FunctionConfigurationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFunctionResponseTypeDef(BaseModel):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResolverResponseTypeDef(BaseModel):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverResponseTypeDef(BaseModel):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolversByFunctionResponseTypeDef(BaseModel):
    resolvers: List[ResolverTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolversResponseTypeDef(BaseModel):
    resolvers: List[ResolverTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResolverResponseTypeDef(BaseModel):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceResponseTypeDef(BaseModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceResponseTypeDef(BaseModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesResponseTypeDef(BaseModel):
    dataSources: List[DataSourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(BaseModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

