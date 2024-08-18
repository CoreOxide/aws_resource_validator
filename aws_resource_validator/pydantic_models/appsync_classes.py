from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class CognitoUserPoolConfigTypeDef(BaseValidatorModel):
    userPoolId: str
    awsRegion: str
    appIdClientRegex: Optional[str] = None

class LambdaAuthorizerConfigTypeDef(BaseValidatorModel):
    authorizerUri: str
    authorizerResultTtlInSeconds: Optional[int] = None
    identityValidationExpression: Optional[str] = None

class OpenIDConnectConfigTypeDef(BaseValidatorModel):
    issuer: str
    clientId: Optional[str] = None
    iatTTL: Optional[int] = None
    authTTL: Optional[int] = None

class ApiAssociationTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None
    apiId: Optional[str] = None
    associationStatus: Optional[AssociationStatusType] = None
    deploymentDetail: Optional[str] = None

class ApiCacheTypeDef(BaseValidatorModel):
    ttl: Optional[int] = None
    apiCachingBehavior: Optional[ApiCachingBehaviorType] = None
    transitEncryptionEnabled: Optional[bool] = None
    atRestEncryptionEnabled: Optional[bool] = None
    type: Optional[ApiCacheTypeType] = None
    status: Optional[ApiCacheStatusType] = None
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None

class ApiKeyTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    expires: Optional[int] = None
    deletes: Optional[int] = None

class AppSyncRuntimeTypeDef(BaseValidatorModel):
    name: Literal["APPSYNC_JS"]
    runtimeVersion: str

class AssociateApiRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    apiId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SourceApiAssociationConfigTypeDef(BaseValidatorModel):
    mergeType: Optional[MergeTypeType] = None

class AwsIamConfigTypeDef(BaseValidatorModel):
    signingRegion: Optional[str] = None
    signingServiceName: Optional[str] = None

class CachingConfigExtraOutputTypeDef(BaseValidatorModel):
    ttl: int
    cachingKeys: Optional[List[str]] = None

class CachingConfigOutputTypeDef(BaseValidatorModel):
    ttl: int
    cachingKeys: Optional[List[str]] = None

class CachingConfigTypeDef(BaseValidatorModel):
    ttl: int
    cachingKeys: Optional[Sequence[str]] = None

class CodeErrorLocationTypeDef(BaseValidatorModel):
    line: Optional[int] = None
    column: Optional[int] = None
    span: Optional[int] = None

class CreateApiCacheRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    ttl: int
    apiCachingBehavior: ApiCachingBehaviorType
    type: ApiCacheTypeType
    transitEncryptionEnabled: Optional[bool] = None
    atRestEncryptionEnabled: Optional[bool] = None
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None

class CreateApiKeyRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    description: Optional[str] = None
    expires: Optional[int] = None

class ElasticsearchDataSourceConfigTypeDef(BaseValidatorModel):
    endpoint: str
    awsRegion: str

class EventBridgeDataSourceConfigTypeDef(BaseValidatorModel):
    eventBusArn: str

class LambdaDataSourceConfigTypeDef(BaseValidatorModel):
    lambdaFunctionArn: str

class OpenSearchServiceDataSourceConfigTypeDef(BaseValidatorModel):
    endpoint: str
    awsRegion: str

class CreateDomainNameRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    certificateArn: str
    description: Optional[str] = None

class DomainNameConfigTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None
    description: Optional[str] = None
    certificateArn: Optional[str] = None
    appsyncDomainName: Optional[str] = None
    hostedZoneId: Optional[str] = None

class EnhancedMetricsConfigTypeDef(BaseValidatorModel):
    resolverLevelMetricsBehavior: ResolverLevelMetricsBehaviorType
    dataSourceLevelMetricsBehavior: DataSourceLevelMetricsBehaviorType
    operationLevelMetricsConfig: OperationLevelMetricsConfigType

class LogConfigTypeDef(BaseValidatorModel):
    fieldLogLevel: FieldLogLevelType
    cloudWatchLogsRoleArn: str
    excludeVerboseContent: Optional[bool] = None

class UserPoolConfigTypeDef(BaseValidatorModel):
    userPoolId: str
    awsRegion: str
    defaultAction: DefaultActionType
    appIdClientRegex: Optional[str] = None

class PipelineConfigTypeDef(BaseValidatorModel):
    functions: Optional[Sequence[str]] = None

class CreateTypeRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    definition: str
    format: TypeDefinitionFormatType

class TypeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    arn: Optional[str] = None
    definition: Optional[str] = None
    format: Optional[TypeDefinitionFormatType] = None

class DataSourceIntrospectionModelFieldTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional["DataSourceIntrospectionModelFieldTypeTypeDef"] = None
    length: Optional[int] = None

class DataSourceIntrospectionModelFieldTypeTypeDef(BaseValidatorModel):
    kind: Optional[str] = None
    name: Optional[str] = None
    type: Optional[Dict[str, Any]] = None
    values: Optional[List[str]] = None

class DataSourceIntrospectionModelIndexTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    fields: Optional[List[str]] = None

class DeleteApiCacheRequestRequestTypeDef(BaseValidatorModel):
    apiId: str

class DeleteApiKeyRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    id: str

class DeleteDataSourceRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str

class DeleteDomainNameRequestRequestTypeDef(BaseValidatorModel):
    domainName: str

class DeleteFunctionRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    functionId: str

class DeleteGraphqlApiRequestRequestTypeDef(BaseValidatorModel):
    apiId: str

class DeleteResolverRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str

class DeleteTypeRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str

class DeltaSyncConfigTypeDef(BaseValidatorModel):
    baseTableTTL: Optional[int] = None
    deltaSyncTableName: Optional[str] = None
    deltaSyncTableTTL: Optional[int] = None

class DisassociateApiRequestRequestTypeDef(BaseValidatorModel):
    domainName: str

class DisassociateMergedGraphqlApiRequestRequestTypeDef(BaseValidatorModel):
    sourceApiIdentifier: str
    associationId: str

class DisassociateSourceGraphqlApiRequestRequestTypeDef(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str

class ErrorDetailTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class EvaluateMappingTemplateRequestRequestTypeDef(BaseValidatorModel):
    template: str
    context: str

class FlushApiCacheRequestRequestTypeDef(BaseValidatorModel):
    apiId: str

class GetApiAssociationRequestRequestTypeDef(BaseValidatorModel):
    domainName: str

class GetApiCacheRequestRequestTypeDef(BaseValidatorModel):
    apiId: str

class GetDataSourceIntrospectionRequestRequestTypeDef(BaseValidatorModel):
    introspectionId: str
    includeModelsSDL: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetDataSourceRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str

class GetDomainNameRequestRequestTypeDef(BaseValidatorModel):
    domainName: str

class GetFunctionRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    functionId: str

class GetGraphqlApiEnvironmentVariablesRequestRequestTypeDef(BaseValidatorModel):
    apiId: str

class GetGraphqlApiRequestRequestTypeDef(BaseValidatorModel):
    apiId: str

class GetIntrospectionSchemaRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    format: OutputTypeType
    includeDirectives: Optional[bool] = None

class GetResolverRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str

class GetSchemaCreationStatusRequestRequestTypeDef(BaseValidatorModel):
    apiId: str

class GetSourceApiAssociationRequestRequestTypeDef(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str

class GetTypeRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    format: TypeDefinitionFormatType

class LambdaConflictHandlerConfigTypeDef(BaseValidatorModel):
    lambdaConflictHandlerArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApiKeysRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDataSourcesRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDomainNamesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFunctionsRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListGraphqlApisRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    apiType: Optional[GraphQLApiTypeType] = None
    owner: Optional[OwnershipType] = None

class ListResolversByFunctionRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    functionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListResolversRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSourceApiAssociationsRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SourceApiAssociationSummaryTypeDef(BaseValidatorModel):
    associationId: Optional[str] = None
    associationArn: Optional[str] = None
    sourceApiId: Optional[str] = None
    sourceApiArn: Optional[str] = None
    mergedApiId: Optional[str] = None
    mergedApiArn: Optional[str] = None
    description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTypesByAssociationRequestRequestTypeDef(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str
    format: TypeDefinitionFormatType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTypesRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    format: TypeDefinitionFormatType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PipelineConfigExtraOutputTypeDef(BaseValidatorModel):
    functions: Optional[List[str]] = None

class PipelineConfigOutputTypeDef(BaseValidatorModel):
    functions: Optional[List[str]] = None

class PutGraphqlApiEnvironmentVariablesRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    environmentVariables: Mapping[str, str]

class RdsDataApiConfigTypeDef(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    databaseName: str

class RdsHttpEndpointConfigTypeDef(BaseValidatorModel):
    awsRegion: Optional[str] = None
    dbClusterIdentifier: Optional[str] = None
    databaseName: Optional[str] = None
    schema: Optional[str] = None
    awsSecretStoreArn: Optional[str] = None

class StartSchemaMergeRequestRequestTypeDef(BaseValidatorModel):
    associationId: str
    mergedApiIdentifier: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApiCacheRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    ttl: int
    apiCachingBehavior: ApiCachingBehaviorType
    type: ApiCacheTypeType
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None

class UpdateApiKeyRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    id: str
    description: Optional[str] = None
    expires: Optional[int] = None

class UpdateDomainNameRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    description: Optional[str] = None

class UpdateTypeRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    format: TypeDefinitionFormatType
    definition: Optional[str] = None

class AdditionalAuthenticationProviderTypeDef(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    userPoolConfig: Optional[CognitoUserPoolConfigTypeDef] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfigTypeDef] = None

class EvaluateCodeRequestRequestTypeDef(BaseValidatorModel):
    runtime: AppSyncRuntimeTypeDef
    code: str
    context: str
    function: Optional[str] = None

class AssociateApiResponseTypeDef(BaseValidatorModel):
    apiAssociation: ApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiCacheResponseTypeDef(BaseValidatorModel):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiKeyResponseTypeDef(BaseValidatorModel):
    apiKey: ApiKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateMergedGraphqlApiResponseTypeDef(BaseValidatorModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateSourceGraphqlApiResponseTypeDef(BaseValidatorModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiAssociationResponseTypeDef(BaseValidatorModel):
    apiAssociation: ApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiCacheResponseTypeDef(BaseValidatorModel):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphqlApiEnvironmentVariablesResponseTypeDef(BaseValidatorModel):
    environmentVariables: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntrospectionSchemaResponseTypeDef(BaseValidatorModel):
    schema: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaCreationStatusResponseTypeDef(BaseValidatorModel):
    status: SchemaStatusType
    details: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApiKeysResponseTypeDef(BaseValidatorModel):
    apiKeys: List[ApiKeyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutGraphqlApiEnvironmentVariablesResponseTypeDef(BaseValidatorModel):
    environmentVariables: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceIntrospectionResponseTypeDef(BaseValidatorModel):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaCreationResponseTypeDef(BaseValidatorModel):
    status: SchemaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaMergeResponseTypeDef(BaseValidatorModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiCacheResponseTypeDef(BaseValidatorModel):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiKeyResponseTypeDef(BaseValidatorModel):
    apiKey: ApiKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateMergedGraphqlApiRequestRequestTypeDef(BaseValidatorModel):
    sourceApiIdentifier: str
    mergedApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None

class AssociateSourceGraphqlApiRequestRequestTypeDef(BaseValidatorModel):
    mergedApiIdentifier: str
    sourceApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None

class SourceApiAssociationTypeDef(BaseValidatorModel):
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

class UpdateSourceApiAssociationRequestRequestTypeDef(BaseValidatorModel):
    associationId: str
    mergedApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None

class AuthorizationConfigTypeDef(BaseValidatorModel):
    authorizationType: Literal["AWS_IAM"]
    awsIamConfig: Optional[AwsIamConfigTypeDef] = None

class StartSchemaCreationRequestRequestTypeDef(BaseValidatorModel):
    apiId: str
    definition: BlobTypeDef

class CodeErrorTypeDef(BaseValidatorModel):
    errorType: Optional[str] = None
    value: Optional[str] = None
    location: Optional[CodeErrorLocationTypeDef] = None

class CreateDomainNameResponseTypeDef(BaseValidatorModel):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainNameResponseTypeDef(BaseValidatorModel):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainNamesResponseTypeDef(BaseValidatorModel):
    domainNameConfigs: List[DomainNameConfigTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameResponseTypeDef(BaseValidatorModel):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTypeResponseTypeDef(BaseValidatorModel):
    type: TypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTypeResponseTypeDef(BaseValidatorModel):
    type: TypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTypesByAssociationResponseTypeDef(BaseValidatorModel):
    types: List[TypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTypesResponseTypeDef(BaseValidatorModel):
    types: List[TypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTypeResponseTypeDef(BaseValidatorModel):
    type: TypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceIntrospectionModelTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    fields: Optional[List[DataSourceIntrospectionModelFieldTypeDef]] = None
    primaryKey: Optional[DataSourceIntrospectionModelIndexTypeDef] = None
    indexes: Optional[List[DataSourceIntrospectionModelIndexTypeDef]] = None
    sdl: Optional[str] = None

class DynamodbDataSourceConfigTypeDef(BaseValidatorModel):
    tableName: str
    awsRegion: str
    useCallerCredentials: Optional[bool] = None
    deltaSyncConfig: Optional[DeltaSyncConfigTypeDef] = None
    versioned: Optional[bool] = None

class EvaluateMappingTemplateResponseTypeDef(BaseValidatorModel):
    evaluationResult: str
    error: ErrorDetailTypeDef
    logs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SyncConfigTypeDef(BaseValidatorModel):
    conflictHandler: Optional[ConflictHandlerTypeType] = None
    conflictDetection: Optional[ConflictDetectionTypeType] = None
    lambdaConflictHandlerConfig: Optional[LambdaConflictHandlerConfigTypeDef] = None

class ListApiKeysRequestListApiKeysPaginateTypeDef(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionsRequestListFunctionsPaginateTypeDef(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGraphqlApisRequestListGraphqlApisPaginateTypeDef(BaseValidatorModel):
    apiType: Optional[GraphQLApiTypeType] = None
    owner: Optional[OwnershipType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolversByFunctionRequestListResolversByFunctionPaginateTypeDef(BaseValidatorModel):
    apiId: str
    functionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResolversRequestListResolversPaginateTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTypesRequestListTypesPaginateTypeDef(BaseValidatorModel):
    apiId: str
    format: TypeDefinitionFormatType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSourceApiAssociationsResponseTypeDef(BaseValidatorModel):
    sourceApiAssociationSummaries: List[SourceApiAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceIntrospectionRequestRequestTypeDef(BaseValidatorModel):
    rdsDataApiConfig: Optional[RdsDataApiConfigTypeDef] = None

class RelationalDatabaseDataSourceConfigTypeDef(BaseValidatorModel):
    relationalDatabaseSourceType: Optional[Literal["RDS_HTTP_ENDPOINT"]] = None
    rdsHttpEndpointConfig: Optional[RdsHttpEndpointConfigTypeDef] = None

class CreateGraphqlApiRequestRequestTypeDef(BaseValidatorModel):
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

class GraphqlApiTypeDef(BaseValidatorModel):
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

class UpdateGraphqlApiRequestRequestTypeDef(BaseValidatorModel):
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

class AssociateMergedGraphqlApiResponseTypeDef(BaseValidatorModel):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSourceGraphqlApiResponseTypeDef(BaseValidatorModel):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceApiAssociationResponseTypeDef(BaseValidatorModel):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSourceApiAssociationResponseTypeDef(BaseValidatorModel):
    sourceApiAssociation: SourceApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HttpDataSourceConfigTypeDef(BaseValidatorModel):
    endpoint: Optional[str] = None
    authorizationConfig: Optional[AuthorizationConfigTypeDef] = None

class EvaluateCodeErrorDetailTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    codeErrors: Optional[List[CodeErrorTypeDef]] = None

class DataSourceIntrospectionResultTypeDef(BaseValidatorModel):
    models: Optional[List[DataSourceIntrospectionModelTypeDef]] = None
    nextToken: Optional[str] = None

class CreateFunctionRequestRequestTypeDef(BaseValidatorModel):
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

class CreateResolverRequestRequestTypeDef(BaseValidatorModel):
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

class FunctionConfigurationTypeDef(BaseValidatorModel):
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

class ResolverTypeDef(BaseValidatorModel):
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

class UpdateFunctionRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateResolverRequestRequestTypeDef(BaseValidatorModel):
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

class CreateGraphqlApiResponseTypeDef(BaseValidatorModel):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGraphqlApiResponseTypeDef(BaseValidatorModel):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGraphqlApisResponseTypeDef(BaseValidatorModel):
    graphqlApis: List[GraphqlApiTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGraphqlApiResponseTypeDef(BaseValidatorModel):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceRequestRequestTypeDef(BaseValidatorModel):
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

class DataSourceTypeDef(BaseValidatorModel):
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

class UpdateDataSourceRequestRequestTypeDef(BaseValidatorModel):
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

class EvaluateCodeResponseTypeDef(BaseValidatorModel):
    evaluationResult: str
    error: EvaluateCodeErrorDetailTypeDef
    logs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceIntrospectionResponseTypeDef(BaseValidatorModel):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    introspectionResult: DataSourceIntrospectionResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionResponseTypeDef(BaseValidatorModel):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionResponseTypeDef(BaseValidatorModel):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsResponseTypeDef(BaseValidatorModel):
    functions: List[FunctionConfigurationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFunctionResponseTypeDef(BaseValidatorModel):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResolverResponseTypeDef(BaseValidatorModel):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResolverResponseTypeDef(BaseValidatorModel):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolversByFunctionResponseTypeDef(BaseValidatorModel):
    resolvers: List[ResolverTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResolversResponseTypeDef(BaseValidatorModel):
    resolvers: List[ResolverTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResolverResponseTypeDef(BaseValidatorModel):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    dataSources: List[DataSourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

