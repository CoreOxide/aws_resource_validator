from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.appsync.appsync_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CognitoUserPoolConfig(BaseValidatorModel):
    userPoolId: str
    awsRegion: str
    appIdClientRegex: Optional[str] = None


class LambdaAuthorizerConfig(BaseValidatorModel):
    authorizerUri: str
    authorizerResultTtlInSeconds: Optional[int] = None
    identityValidationExpression: Optional[str] = None


class OpenIDConnectConfig(BaseValidatorModel):
    issuer: str
    clientId: Optional[str] = None
    iatTTL: Optional[int] = None
    authTTL: Optional[int] = None


class ApiAssociation(BaseValidatorModel):
    domainName: Optional[str] = None
    apiId: Optional[str] = None
    associationStatus: Optional[AssociationStatusType] = None
    deploymentDetail: Optional[str] = None


class ApiCache(BaseValidatorModel):
    ttl: Optional[int] = None
    apiCachingBehavior: Optional[ApiCachingBehaviorType] = None
    transitEncryptionEnabled: Optional[bool] = None
    atRestEncryptionEnabled: Optional[bool] = None
    type: Optional[ApiCacheTypeType] = None
    status: Optional[ApiCacheStatusType] = None
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None


class ApiKey(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    expires: Optional[int] = None
    deletes: Optional[int] = None


class AppSyncRuntime(BaseValidatorModel):
    name: Literal['APPSYNC_JS']
    runtimeVersion: str


# This class is the input for the 'associate_api' function.
class AssociateApiRequest(BaseValidatorModel):
    domainName: str
    apiId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SourceApiAssociationConfig(BaseValidatorModel):
    mergeType: Optional[MergeTypeType] = None


class AuthMode(BaseValidatorModel):
    authType: AuthenticationTypeType


class CognitoConfig(BaseValidatorModel):
    userPoolId: str
    awsRegion: str
    appIdClientRegex: Optional[str] = None


class AwsIamConfig(BaseValidatorModel):
    signingRegion: Optional[str] = None
    signingServiceName: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CachingConfigOutput(BaseValidatorModel):
    ttl: int
    cachingKeys: Optional[List[str]] = None


class CachingConfig(BaseValidatorModel):
    ttl: int
    cachingKeys: Optional[List[str]] = None


class CodeErrorLocation(BaseValidatorModel):
    line: Optional[int] = None
    column: Optional[int] = None
    span: Optional[int] = None


# This class is the input for the 'create_api_cache' function.
class CreateApiCacheRequest(BaseValidatorModel):
    apiId: str
    ttl: int
    apiCachingBehavior: ApiCachingBehaviorType
    type: ApiCacheTypeType
    transitEncryptionEnabled: Optional[bool] = None
    atRestEncryptionEnabled: Optional[bool] = None
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None


# This class is the input for the 'create_api_key' function.
class CreateApiKeyRequest(BaseValidatorModel):
    apiId: str
    description: Optional[str] = None
    expires: Optional[int] = None


class ElasticsearchDataSourceConfig(BaseValidatorModel):
    endpoint: str
    awsRegion: str


class EventBridgeDataSourceConfig(BaseValidatorModel):
    eventBusArn: str


class LambdaDataSourceConfig(BaseValidatorModel):
    lambdaFunctionArn: str


class OpenSearchServiceDataSourceConfig(BaseValidatorModel):
    endpoint: str
    awsRegion: str


# This class is the input for the 'create_domain_name' function.
class CreateDomainNameRequest(BaseValidatorModel):
    domainName: str
    certificateArn: str
    description: Optional[str] = None


class DomainNameConfig(BaseValidatorModel):
    domainName: Optional[str] = None
    description: Optional[str] = None
    certificateArn: Optional[str] = None
    appsyncDomainName: Optional[str] = None
    hostedZoneId: Optional[str] = None


class EnhancedMetricsConfig(BaseValidatorModel):
    resolverLevelMetricsBehavior: ResolverLevelMetricsBehaviorType
    dataSourceLevelMetricsBehavior: DataSourceLevelMetricsBehaviorType
    operationLevelMetricsConfig: OperationLevelMetricsConfigType


class LogConfig(BaseValidatorModel):
    fieldLogLevel: FieldLogLevelType
    cloudWatchLogsRoleArn: str
    excludeVerboseContent: Optional[bool] = None


class UserPoolConfig(BaseValidatorModel):
    userPoolId: str
    awsRegion: str
    defaultAction: DefaultActionType
    appIdClientRegex: Optional[str] = None


# This class is the input for the 'create_type' function.
class CreateTypeRequest(BaseValidatorModel):
    apiId: str
    definition: str
    format: TypeDefinitionFormatType


class Type(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    arn: Optional[str] = None
    definition: Optional[str] = None
    format: Optional[TypeDefinitionFormatType] = None


class DataSourceIntrospectionModelFieldType(BaseValidatorModel):
    kind: Optional[str] = None
    name: Optional[str] = None
    type: Optional[Dict[str, Any]] = None
    values: Optional[List[str]] = None


class DataSourceIntrospectionModelIndex(BaseValidatorModel):
    name: Optional[str] = None
    fields: Optional[List[str]] = None


class DeleteApiCacheRequest(BaseValidatorModel):
    apiId: str


class DeleteApiKeyRequest(BaseValidatorModel):
    apiId: str
    id: str


class DeleteApiRequest(BaseValidatorModel):
    apiId: str


class DeleteChannelNamespaceRequest(BaseValidatorModel):
    apiId: str
    name: str


class DeleteDataSourceRequest(BaseValidatorModel):
    apiId: str
    name: str


class DeleteDomainNameRequest(BaseValidatorModel):
    domainName: str


class DeleteFunctionRequest(BaseValidatorModel):
    apiId: str
    functionId: str


class DeleteGraphqlApiRequest(BaseValidatorModel):
    apiId: str


class DeleteResolverRequest(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str


class DeleteTypeRequest(BaseValidatorModel):
    apiId: str
    typeName: str


class DeltaSyncConfig(BaseValidatorModel):
    baseTableTTL: Optional[int] = None
    deltaSyncTableName: Optional[str] = None
    deltaSyncTableTTL: Optional[int] = None


class DisassociateApiRequest(BaseValidatorModel):
    domainName: str


# This class is the input for the 'disassociate_merged_graphql_api' function.
class DisassociateMergedGraphqlApiRequest(BaseValidatorModel):
    sourceApiIdentifier: str
    associationId: str


# This class is the input for the 'disassociate_source_graphql_api' function.
class DisassociateSourceGraphqlApiRequest(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str


class ErrorDetail(BaseValidatorModel):
    message: Optional[str] = None


# This class is the input for the 'evaluate_mapping_template' function.
class EvaluateMappingTemplateRequest(BaseValidatorModel):
    template: str
    context: str


class EventLogConfig(BaseValidatorModel):
    logLevel: EventLogLevelType
    cloudWatchLogsRoleArn: str


class FlushApiCacheRequest(BaseValidatorModel):
    apiId: str


# This class is the input for the 'get_api_association' function.
class GetApiAssociationRequest(BaseValidatorModel):
    domainName: str


# This class is the input for the 'get_api_cache' function.
class GetApiCacheRequest(BaseValidatorModel):
    apiId: str


# This class is the input for the 'get_api' function.
class GetApiRequest(BaseValidatorModel):
    apiId: str


# This class is the input for the 'get_channel_namespace' function.
class GetChannelNamespaceRequest(BaseValidatorModel):
    apiId: str
    name: str


# This class is the input for the 'get_data_source_introspection' function.
class GetDataSourceIntrospectionRequest(BaseValidatorModel):
    introspectionId: str
    includeModelsSDL: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_data_source' function.
class GetDataSourceRequest(BaseValidatorModel):
    apiId: str
    name: str


# This class is the input for the 'get_domain_name' function.
class GetDomainNameRequest(BaseValidatorModel):
    domainName: str


# This class is the input for the 'get_function' function.
class GetFunctionRequest(BaseValidatorModel):
    apiId: str
    functionId: str


# This class is the input for the 'get_graphql_api_environment_variables' function.
class GetGraphqlApiEnvironmentVariablesRequest(BaseValidatorModel):
    apiId: str


# This class is the input for the 'get_graphql_api' function.
class GetGraphqlApiRequest(BaseValidatorModel):
    apiId: str


# This class is the input for the 'get_introspection_schema' function.
class GetIntrospectionSchemaRequest(BaseValidatorModel):
    apiId: str
    format: OutputTypeType
    includeDirectives: Optional[bool] = None


# This class is the input for the 'get_resolver' function.
class GetResolverRequest(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str


# This class is the input for the 'get_schema_creation_status' function.
class GetSchemaCreationStatusRequest(BaseValidatorModel):
    apiId: str


# This class is the input for the 'get_source_api_association' function.
class GetSourceApiAssociationRequest(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str


# This class is the input for the 'get_type' function.
class GetTypeRequest(BaseValidatorModel):
    apiId: str
    typeName: str
    format: TypeDefinitionFormatType


class LambdaConflictHandlerConfig(BaseValidatorModel):
    lambdaConflictHandlerArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_api_keys' function.
class ListApiKeysRequest(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_apis' function.
class ListApisRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_channel_namespaces' function.
class ListChannelNamespacesRequest(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_data_sources' function.
class ListDataSourcesRequest(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_domain_names' function.
class ListDomainNamesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_functions' function.
class ListFunctionsRequest(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_graphql_apis' function.
class ListGraphqlApisRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    apiType: Optional[GraphQLApiTypeType] = None
    owner: Optional[OwnershipType] = None


# This class is the input for the 'list_resolvers_by_function' function.
class ListResolversByFunctionRequest(BaseValidatorModel):
    apiId: str
    functionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_resolvers' function.
class ListResolversRequest(BaseValidatorModel):
    apiId: str
    typeName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_source_api_associations' function.
class ListSourceApiAssociationsRequest(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SourceApiAssociationSummary(BaseValidatorModel):
    associationId: Optional[str] = None
    associationArn: Optional[str] = None
    sourceApiId: Optional[str] = None
    sourceApiArn: Optional[str] = None
    mergedApiId: Optional[str] = None
    mergedApiArn: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_types_by_association' function.
class ListTypesByAssociationRequest(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str
    format: TypeDefinitionFormatType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_types' function.
class ListTypesRequest(BaseValidatorModel):
    apiId: str
    format: TypeDefinitionFormatType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PipelineConfigOutput(BaseValidatorModel):
    functions: Optional[List[str]] = None


class PipelineConfig(BaseValidatorModel):
    functions: Optional[List[str]] = None


# This class is the input for the 'put_graphql_api_environment_variables' function.
class PutGraphqlApiEnvironmentVariablesRequest(BaseValidatorModel):
    apiId: str
    environmentVariables: Dict[str, str]


class RdsDataApiConfig(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    databaseName: str


class RdsHttpEndpointConfig(BaseValidatorModel):
    awsRegion: Optional[str] = None
    dbClusterIdentifier: Optional[str] = None
    databaseName: Optional[str] = None
    schema: Optional[str] = None
    awsSecretStoreArn: Optional[str] = None


# This class is the input for the 'start_schema_merge' function.
class StartSchemaMergeRequest(BaseValidatorModel):
    associationId: str
    mergedApiIdentifier: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_api_cache' function.
class UpdateApiCacheRequest(BaseValidatorModel):
    apiId: str
    ttl: int
    apiCachingBehavior: ApiCachingBehaviorType
    type: ApiCacheTypeType
    healthMetricsConfig: Optional[CacheHealthMetricsConfigType] = None


# This class is the input for the 'update_api_key' function.
class UpdateApiKeyRequest(BaseValidatorModel):
    apiId: str
    id: str
    description: Optional[str] = None
    expires: Optional[int] = None


# This class is the input for the 'update_domain_name' function.
class UpdateDomainNameRequest(BaseValidatorModel):
    domainName: str
    description: Optional[str] = None


# This class is the input for the 'update_type' function.
class UpdateTypeRequest(BaseValidatorModel):
    apiId: str
    typeName: str
    format: TypeDefinitionFormatType
    definition: Optional[str] = None


class AdditionalAuthenticationProvider(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    openIDConnectConfig: Optional[OpenIDConnectConfig] = None
    userPoolConfig: Optional[CognitoUserPoolConfig] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig] = None


# This class is the input for the 'evaluate_code' function.
class EvaluateCodeRequest(BaseValidatorModel):
    runtime: AppSyncRuntime
    code: str
    context: str
    function: Optional[str] = None


# This class is the output for the 'associate_api' function.
class AssociateApiResponse(BaseValidatorModel):
    apiAssociation: ApiAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_api_cache' function.
class CreateApiCacheResponse(BaseValidatorModel):
    apiCache: ApiCache
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_api_key' function.
class CreateApiKeyResponse(BaseValidatorModel):
    apiKey: ApiKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_merged_graphql_api' function.
class DisassociateMergedGraphqlApiResponse(BaseValidatorModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_source_graphql_api' function.
class DisassociateSourceGraphqlApiResponse(BaseValidatorModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_api_association' function.
class GetApiAssociationResponse(BaseValidatorModel):
    apiAssociation: ApiAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_api_cache' function.
class GetApiCacheResponse(BaseValidatorModel):
    apiCache: ApiCache
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_graphql_api_environment_variables' function.
class GetGraphqlApiEnvironmentVariablesResponse(BaseValidatorModel):
    environmentVariables: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_introspection_schema' function.
class GetIntrospectionSchemaResponse(BaseValidatorModel):
    schema: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_schema_creation_status' function.
class GetSchemaCreationStatusResponse(BaseValidatorModel):
    status: SchemaStatusType
    details: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_api_keys' function.
class ListApiKeysResponse(BaseValidatorModel):
    apiKeys: List[ApiKey]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_graphql_api_environment_variables' function.
class PutGraphqlApiEnvironmentVariablesResponse(BaseValidatorModel):
    environmentVariables: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_data_source_introspection' function.
class StartDataSourceIntrospectionResponse(BaseValidatorModel):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_schema_creation' function.
class StartSchemaCreationResponse(BaseValidatorModel):
    status: SchemaStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_schema_merge' function.
class StartSchemaMergeResponse(BaseValidatorModel):
    sourceApiAssociationStatus: SourceApiAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_api_cache' function.
class UpdateApiCacheResponse(BaseValidatorModel):
    apiCache: ApiCache
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_api_key' function.
class UpdateApiKeyResponse(BaseValidatorModel):
    apiKey: ApiKey
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_merged_graphql_api' function.
class AssociateMergedGraphqlApiRequest(BaseValidatorModel):
    sourceApiIdentifier: str
    mergedApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfig] = None


# This class is the input for the 'associate_source_graphql_api' function.
class AssociateSourceGraphqlApiRequest(BaseValidatorModel):
    mergedApiIdentifier: str
    sourceApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfig] = None


class SourceApiAssociation(BaseValidatorModel):
    associationId: Optional[str] = None
    associationArn: Optional[str] = None
    sourceApiId: Optional[str] = None
    sourceApiArn: Optional[str] = None
    mergedApiArn: Optional[str] = None
    mergedApiId: Optional[str] = None
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfig] = None
    sourceApiAssociationStatus: Optional[SourceApiAssociationStatusType] = None
    sourceApiAssociationStatusDetail: Optional[str] = None
    lastSuccessfulMergeDate: Optional[datetime] = None


# This class is the input for the 'update_source_api_association' function.
class UpdateSourceApiAssociationRequest(BaseValidatorModel):
    associationId: str
    mergedApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfig] = None


class ChannelNamespace(BaseValidatorModel):
    apiId: Optional[str] = None
    name: Optional[str] = None
    subscribeAuthModes: Optional[List[AuthMode]] = None
    publishAuthModes: Optional[List[AuthMode]] = None
    codeHandlers: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    channelNamespaceArn: Optional[str] = None
    created: Optional[datetime] = None
    lastModified: Optional[datetime] = None


# This class is the input for the 'create_channel_namespace' function.
class CreateChannelNamespaceRequest(BaseValidatorModel):
    apiId: str
    name: str
    subscribeAuthModes: Optional[List[AuthMode]] = None
    publishAuthModes: Optional[List[AuthMode]] = None
    codeHandlers: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_channel_namespace' function.
class UpdateChannelNamespaceRequest(BaseValidatorModel):
    apiId: str
    name: str
    subscribeAuthModes: Optional[List[AuthMode]] = None
    publishAuthModes: Optional[List[AuthMode]] = None
    codeHandlers: Optional[str] = None


class AuthProvider(BaseValidatorModel):
    authType: AuthenticationTypeType
    cognitoConfig: Optional[CognitoConfig] = None
    openIDConnectConfig: Optional[OpenIDConnectConfig] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig] = None


class AuthorizationConfig(BaseValidatorModel):
    authorizationType: Literal['AWS_IAM']
    awsIamConfig: Optional[AwsIamConfig] = None


# This class is the input for the 'start_schema_creation' function.
class StartSchemaCreationRequest(BaseValidatorModel):
    apiId: str
    definition: Blob

CachingConfigUnion = Union[CachingConfig, CachingConfigOutput]


class CodeError(BaseValidatorModel):
    errorType: Optional[str] = None
    value: Optional[str] = None
    location: Optional[CodeErrorLocation] = None


# This class is the output for the 'create_domain_name' function.
class CreateDomainNameResponse(BaseValidatorModel):
    domainNameConfig: DomainNameConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain_name' function.
class GetDomainNameResponse(BaseValidatorModel):
    domainNameConfig: DomainNameConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_domain_names' function.
class ListDomainNamesResponse(BaseValidatorModel):
    domainNameConfigs: List[DomainNameConfig]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_domain_name' function.
class UpdateDomainNameResponse(BaseValidatorModel):
    domainNameConfig: DomainNameConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_type' function.
class CreateTypeResponse(BaseValidatorModel):
    type: Type
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_type' function.
class GetTypeResponse(BaseValidatorModel):
    type: Type
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_types_by_association' function.
class ListTypesByAssociationResponse(BaseValidatorModel):
    types: List[Type]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_types' function.
class ListTypesResponse(BaseValidatorModel):
    types: List[Type]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_type' function.
class UpdateTypeResponse(BaseValidatorModel):
    type: Type
    ResponseMetadata: ResponseMetadata


class DataSourceIntrospectionModelField(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[DataSourceIntrospectionModelFieldType] = None
    length: Optional[int] = None


class DynamodbDataSourceConfig(BaseValidatorModel):
    tableName: str
    awsRegion: str
    useCallerCredentials: Optional[bool] = None
    deltaSyncConfig: Optional[DeltaSyncConfig] = None
    versioned: Optional[bool] = None


# This class is the output for the 'evaluate_mapping_template' function.
class EvaluateMappingTemplateResponse(BaseValidatorModel):
    evaluationResult: str
    error: ErrorDetail
    logs: List[str]
    stash: str
    outErrors: str
    ResponseMetadata: ResponseMetadata


class SyncConfig(BaseValidatorModel):
    conflictHandler: Optional[ConflictHandlerTypeType] = None
    conflictDetection: Optional[ConflictDetectionTypeType] = None
    lambdaConflictHandlerConfig: Optional[LambdaConflictHandlerConfig] = None


class ListApiKeysRequestPaginate(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApisRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListChannelNamespacesRequestPaginate(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSourcesRequestPaginate(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainNamesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFunctionsRequestPaginate(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGraphqlApisRequestPaginate(BaseValidatorModel):
    apiType: Optional[GraphQLApiTypeType] = None
    owner: Optional[OwnershipType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolversByFunctionRequestPaginate(BaseValidatorModel):
    apiId: str
    functionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResolversRequestPaginate(BaseValidatorModel):
    apiId: str
    typeName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSourceApiAssociationsRequestPaginate(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTypesByAssociationRequestPaginate(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str
    format: TypeDefinitionFormatType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTypesRequestPaginate(BaseValidatorModel):
    apiId: str
    format: TypeDefinitionFormatType
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_source_api_associations' function.
class ListSourceApiAssociationsResponse(BaseValidatorModel):
    sourceApiAssociationSummaries: List[SourceApiAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

PipelineConfigUnion = Union[PipelineConfig, PipelineConfigOutput]


# This class is the input for the 'start_data_source_introspection' function.
class StartDataSourceIntrospectionRequest(BaseValidatorModel):
    rdsDataApiConfig: Optional[RdsDataApiConfig] = None


class RelationalDatabaseDataSourceConfig(BaseValidatorModel):
    relationalDatabaseSourceType: Optional[Literal['RDS_HTTP_ENDPOINT']] = None
    rdsHttpEndpointConfig: Optional[RdsHttpEndpointConfig] = None


# This class is the input for the 'create_graphql_api' function.
class CreateGraphqlApiRequest(BaseValidatorModel):
    name: str
    authenticationType: AuthenticationTypeType
    logConfig: Optional[LogConfig] = None
    userPoolConfig: Optional[UserPoolConfig] = None
    openIDConnectConfig: Optional[OpenIDConnectConfig] = None
    tags: Optional[Dict[str, str]] = None
    additionalAuthenticationProviders: Optional[List[AdditionalAuthenticationProvider]] = None
    xrayEnabled: Optional[bool] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig] = None
    apiType: Optional[GraphQLApiTypeType] = None
    mergedApiExecutionRoleArn: Optional[str] = None
    visibility: Optional[GraphQLApiVisibilityType] = None
    ownerContact: Optional[str] = None
    introspectionConfig: Optional[GraphQLApiIntrospectionConfigType] = None
    queryDepthLimit: Optional[int] = None
    resolverCountLimit: Optional[int] = None
    enhancedMetricsConfig: Optional[EnhancedMetricsConfig] = None


class GraphqlApi(BaseValidatorModel):
    name: Optional[str] = None
    apiId: Optional[str] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    logConfig: Optional[LogConfig] = None
    userPoolConfig: Optional[UserPoolConfig] = None
    openIDConnectConfig: Optional[OpenIDConnectConfig] = None
    arn: Optional[str] = None
    uris: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    additionalAuthenticationProviders: Optional[List[AdditionalAuthenticationProvider]] = None
    xrayEnabled: Optional[bool] = None
    wafWebAclArn: Optional[str] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig] = None
    dns: Optional[Dict[str, str]] = None
    visibility: Optional[GraphQLApiVisibilityType] = None
    apiType: Optional[GraphQLApiTypeType] = None
    mergedApiExecutionRoleArn: Optional[str] = None
    owner: Optional[str] = None
    ownerContact: Optional[str] = None
    introspectionConfig: Optional[GraphQLApiIntrospectionConfigType] = None
    queryDepthLimit: Optional[int] = None
    resolverCountLimit: Optional[int] = None
    enhancedMetricsConfig: Optional[EnhancedMetricsConfig] = None


# This class is the input for the 'update_graphql_api' function.
class UpdateGraphqlApiRequest(BaseValidatorModel):
    apiId: str
    name: str
    authenticationType: AuthenticationTypeType
    logConfig: Optional[LogConfig] = None
    userPoolConfig: Optional[UserPoolConfig] = None
    openIDConnectConfig: Optional[OpenIDConnectConfig] = None
    additionalAuthenticationProviders: Optional[List[AdditionalAuthenticationProvider]] = None
    xrayEnabled: Optional[bool] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfig] = None
    mergedApiExecutionRoleArn: Optional[str] = None
    ownerContact: Optional[str] = None
    introspectionConfig: Optional[GraphQLApiIntrospectionConfigType] = None
    queryDepthLimit: Optional[int] = None
    resolverCountLimit: Optional[int] = None
    enhancedMetricsConfig: Optional[EnhancedMetricsConfig] = None


# This class is the output for the 'associate_merged_graphql_api' function.
class AssociateMergedGraphqlApiResponse(BaseValidatorModel):
    sourceApiAssociation: SourceApiAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_source_graphql_api' function.
class AssociateSourceGraphqlApiResponse(BaseValidatorModel):
    sourceApiAssociation: SourceApiAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_source_api_association' function.
class GetSourceApiAssociationResponse(BaseValidatorModel):
    sourceApiAssociation: SourceApiAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_source_api_association' function.
class UpdateSourceApiAssociationResponse(BaseValidatorModel):
    sourceApiAssociation: SourceApiAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_channel_namespace' function.
class CreateChannelNamespaceResponse(BaseValidatorModel):
    channelNamespace: ChannelNamespace
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_channel_namespace' function.
class GetChannelNamespaceResponse(BaseValidatorModel):
    channelNamespace: ChannelNamespace
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channel_namespaces' function.
class ListChannelNamespacesResponse(BaseValidatorModel):
    channelNamespaces: List[ChannelNamespace]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_channel_namespace' function.
class UpdateChannelNamespaceResponse(BaseValidatorModel):
    channelNamespace: ChannelNamespace
    ResponseMetadata: ResponseMetadata


class EventConfigOutput(BaseValidatorModel):
    authProviders: List[AuthProvider]
    connectionAuthModes: List[AuthMode]
    defaultPublishAuthModes: List[AuthMode]
    defaultSubscribeAuthModes: List[AuthMode]
    logConfig: Optional[EventLogConfig] = None


class EventConfig(BaseValidatorModel):
    authProviders: List[AuthProvider]
    connectionAuthModes: List[AuthMode]
    defaultPublishAuthModes: List[AuthMode]
    defaultSubscribeAuthModes: List[AuthMode]
    logConfig: Optional[EventLogConfig] = None


class HttpDataSourceConfig(BaseValidatorModel):
    endpoint: Optional[str] = None
    authorizationConfig: Optional[AuthorizationConfig] = None


class EvaluateCodeErrorDetail(BaseValidatorModel):
    message: Optional[str] = None
    codeErrors: Optional[List[CodeError]] = None


class DataSourceIntrospectionModel(BaseValidatorModel):
    name: Optional[str] = None
    fields: Optional[List[DataSourceIntrospectionModelField]] = None
    primaryKey: Optional[DataSourceIntrospectionModelIndex] = None
    indexes: Optional[List[DataSourceIntrospectionModelIndex]] = None
    sdl: Optional[str] = None


# This class is the input for the 'create_function' function.
class CreateFunctionRequest(BaseValidatorModel):
    apiId: str
    name: str
    dataSourceName: str
    description: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    functionVersion: Optional[str] = None
    syncConfig: Optional[SyncConfig] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntime] = None
    code: Optional[str] = None


class FunctionConfiguration(BaseValidatorModel):
    functionId: Optional[str] = None
    functionArn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dataSourceName: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    functionVersion: Optional[str] = None
    syncConfig: Optional[SyncConfig] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntime] = None
    code: Optional[str] = None


class Resolver(BaseValidatorModel):
    typeName: Optional[str] = None
    fieldName: Optional[str] = None
    dataSourceName: Optional[str] = None
    resolverArn: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    kind: Optional[ResolverKindType] = None
    pipelineConfig: Optional[PipelineConfigOutput] = None
    syncConfig: Optional[SyncConfig] = None
    cachingConfig: Optional[CachingConfigOutput] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntime] = None
    code: Optional[str] = None
    metricsConfig: Optional[ResolverLevelMetricsConfigType] = None


# This class is the input for the 'update_function' function.
class UpdateFunctionRequest(BaseValidatorModel):
    apiId: str
    name: str
    functionId: str
    dataSourceName: str
    description: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    functionVersion: Optional[str] = None
    syncConfig: Optional[SyncConfig] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntime] = None
    code: Optional[str] = None


# This class is the input for the 'create_resolver' function.
class CreateResolverRequest(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str
    dataSourceName: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    kind: Optional[ResolverKindType] = None
    pipelineConfig: Optional[PipelineConfigUnion] = None
    syncConfig: Optional[SyncConfig] = None
    cachingConfig: Optional[CachingConfigUnion] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntime] = None
    code: Optional[str] = None
    metricsConfig: Optional[ResolverLevelMetricsConfigType] = None


# This class is the input for the 'update_resolver' function.
class UpdateResolverRequest(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str
    dataSourceName: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    kind: Optional[ResolverKindType] = None
    pipelineConfig: Optional[PipelineConfigUnion] = None
    syncConfig: Optional[SyncConfig] = None
    cachingConfig: Optional[CachingConfigUnion] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntime] = None
    code: Optional[str] = None
    metricsConfig: Optional[ResolverLevelMetricsConfigType] = None


# This class is the output for the 'create_graphql_api' function.
class CreateGraphqlApiResponse(BaseValidatorModel):
    graphqlApi: GraphqlApi
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_graphql_api' function.
class GetGraphqlApiResponse(BaseValidatorModel):
    graphqlApi: GraphqlApi
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_graphql_apis' function.
class ListGraphqlApisResponse(BaseValidatorModel):
    graphqlApis: List[GraphqlApi]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_graphql_api' function.
class UpdateGraphqlApiResponse(BaseValidatorModel):
    graphqlApi: GraphqlApi
    ResponseMetadata: ResponseMetadata


class Api(BaseValidatorModel):
    apiId: Optional[str] = None
    name: Optional[str] = None
    ownerContact: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    dns: Optional[Dict[str, str]] = None
    apiArn: Optional[str] = None
    created: Optional[datetime] = None
    xrayEnabled: Optional[bool] = None
    wafWebAclArn: Optional[str] = None
    eventConfig: Optional[EventConfigOutput] = None

EventConfigUnion = Union[EventConfig, EventConfigOutput]


# This class is the input for the 'create_data_source' function.
class CreateDataSourceRequest(BaseValidatorModel):
    apiId: str
    name: str
    type: DataSourceTypeType
    description: Optional[str] = None
    serviceRoleArn: Optional[str] = None
    dynamodbConfig: Optional[DynamodbDataSourceConfig] = None
    lambdaConfig: Optional[LambdaDataSourceConfig] = None
    elasticsearchConfig: Optional[ElasticsearchDataSourceConfig] = None
    openSearchServiceConfig: Optional[OpenSearchServiceDataSourceConfig] = None
    httpConfig: Optional[HttpDataSourceConfig] = None
    relationalDatabaseConfig: Optional[RelationalDatabaseDataSourceConfig] = None
    eventBridgeConfig: Optional[EventBridgeDataSourceConfig] = None
    metricsConfig: Optional[DataSourceLevelMetricsConfigType] = None


class DataSource(BaseValidatorModel):
    dataSourceArn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[DataSourceTypeType] = None
    serviceRoleArn: Optional[str] = None
    dynamodbConfig: Optional[DynamodbDataSourceConfig] = None
    lambdaConfig: Optional[LambdaDataSourceConfig] = None
    elasticsearchConfig: Optional[ElasticsearchDataSourceConfig] = None
    openSearchServiceConfig: Optional[OpenSearchServiceDataSourceConfig] = None
    httpConfig: Optional[HttpDataSourceConfig] = None
    relationalDatabaseConfig: Optional[RelationalDatabaseDataSourceConfig] = None
    eventBridgeConfig: Optional[EventBridgeDataSourceConfig] = None
    metricsConfig: Optional[DataSourceLevelMetricsConfigType] = None


# This class is the input for the 'update_data_source' function.
class UpdateDataSourceRequest(BaseValidatorModel):
    apiId: str
    name: str
    type: DataSourceTypeType
    description: Optional[str] = None
    serviceRoleArn: Optional[str] = None
    dynamodbConfig: Optional[DynamodbDataSourceConfig] = None
    lambdaConfig: Optional[LambdaDataSourceConfig] = None
    elasticsearchConfig: Optional[ElasticsearchDataSourceConfig] = None
    openSearchServiceConfig: Optional[OpenSearchServiceDataSourceConfig] = None
    httpConfig: Optional[HttpDataSourceConfig] = None
    relationalDatabaseConfig: Optional[RelationalDatabaseDataSourceConfig] = None
    eventBridgeConfig: Optional[EventBridgeDataSourceConfig] = None
    metricsConfig: Optional[DataSourceLevelMetricsConfigType] = None


# This class is the output for the 'evaluate_code' function.
class EvaluateCodeResponse(BaseValidatorModel):
    evaluationResult: str
    error: EvaluateCodeErrorDetail
    logs: List[str]
    stash: str
    outErrors: str
    ResponseMetadata: ResponseMetadata


class DataSourceIntrospectionResult(BaseValidatorModel):
    models: Optional[List[DataSourceIntrospectionModel]] = None
    nextToken: Optional[str] = None


# This class is the output for the 'create_function' function.
class CreateFunctionResponse(BaseValidatorModel):
    functionConfiguration: FunctionConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_function' function.
class GetFunctionResponse(BaseValidatorModel):
    functionConfiguration: FunctionConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_functions' function.
class ListFunctionsResponse(BaseValidatorModel):
    functions: List[FunctionConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_function' function.
class UpdateFunctionResponse(BaseValidatorModel):
    functionConfiguration: FunctionConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_resolver' function.
class CreateResolverResponse(BaseValidatorModel):
    resolver: Resolver
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resolver' function.
class GetResolverResponse(BaseValidatorModel):
    resolver: Resolver
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resolvers_by_function' function.
class ListResolversByFunctionResponse(BaseValidatorModel):
    resolvers: List[Resolver]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_resolvers' function.
class ListResolversResponse(BaseValidatorModel):
    resolvers: List[Resolver]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_resolver' function.
class UpdateResolverResponse(BaseValidatorModel):
    resolver: Resolver
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_api' function.
class CreateApiResponse(BaseValidatorModel):
    api: Api
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_api' function.
class GetApiResponse(BaseValidatorModel):
    api: Api
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_apis' function.
class ListApisResponse(BaseValidatorModel):
    apis: List[Api]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_api' function.
class UpdateApiResponse(BaseValidatorModel):
    api: Api
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_api' function.
class CreateApiRequest(BaseValidatorModel):
    name: str
    ownerContact: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    eventConfig: Optional[EventConfigUnion] = None


# This class is the input for the 'update_api' function.
class UpdateApiRequest(BaseValidatorModel):
    apiId: str
    name: str
    ownerContact: Optional[str] = None
    eventConfig: Optional[EventConfigUnion] = None


# This class is the output for the 'create_data_source' function.
class CreateDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_data_source' function.
class GetDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_data_sources' function.
class ListDataSourcesResponse(BaseValidatorModel):
    dataSources: List[DataSource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_data_source' function.
class UpdateDataSourceResponse(BaseValidatorModel):
    dataSource: DataSource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_data_source_introspection' function.
class GetDataSourceIntrospectionResponse(BaseValidatorModel):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    introspectionResult: DataSourceIntrospectionResult
    ResponseMetadata: ResponseMetadata