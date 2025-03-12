from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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


class AppSyncRuntimeTypeDef(BaseValidatorModel):
    name: Literal["APPSYNC_JS"]
    runtimeVersion: str


class AssociateApiRequestTypeDef(BaseValidatorModel):
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


class AuthModeTypeDef(BaseValidatorModel):
    authType: AuthenticationTypeType


class CognitoConfigTypeDef(BaseValidatorModel):
    userPoolId: str
    awsRegion: str
    appIdClientRegex: Optional[str] = None


class AwsIamConfigTypeDef(BaseValidatorModel):
    signingRegion: Optional[str] = None
    signingServiceName: Optional[str] = None


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


class CreateApiKeyRequestTypeDef(BaseValidatorModel):
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


class CreateDomainNameRequestTypeDef(BaseValidatorModel):
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


class DataSourceIntrospectionModelIndexTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    fields: Optional[List[str]] = None


class DeleteApiCacheRequestTypeDef(BaseValidatorModel):
    apiId: str


class DeleteApiRequestTypeDef(BaseValidatorModel):
    apiId: str


class DeleteChannelNamespaceRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str


class DeleteDataSourceRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str


class DeleteDomainNameRequestTypeDef(BaseValidatorModel):
    domainName: str


class DeleteFunctionRequestTypeDef(BaseValidatorModel):
    apiId: str
    functionId: str


class DeleteGraphqlApiRequestTypeDef(BaseValidatorModel):
    apiId: str


class DeleteResolverRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str


class DeleteTypeRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str


class DeltaSyncConfigTypeDef(BaseValidatorModel):
    baseTableTTL: Optional[int] = None
    deltaSyncTableName: Optional[str] = None
    deltaSyncTableTTL: Optional[int] = None


class DisassociateApiRequestTypeDef(BaseValidatorModel):
    domainName: str


class DisassociateMergedGraphqlApiRequestTypeDef(BaseValidatorModel):
    sourceApiIdentifier: str
    associationId: str


class DisassociateSourceGraphqlApiRequestTypeDef(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str


class ErrorDetailTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class EvaluateMappingTemplateRequestTypeDef(BaseValidatorModel):
    template: str
    context: str


class EventLogConfigTypeDef(BaseValidatorModel):
    logLevel: EventLogLevelType
    cloudWatchLogsRoleArn: str


class FlushApiCacheRequestTypeDef(BaseValidatorModel):
    apiId: str


class GetApiAssociationRequestTypeDef(BaseValidatorModel):
    domainName: str


class GetApiCacheRequestTypeDef(BaseValidatorModel):
    apiId: str


class GetApiRequestTypeDef(BaseValidatorModel):
    apiId: str


class GetChannelNamespaceRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str


class GetDataSourceIntrospectionRequestTypeDef(BaseValidatorModel):
    introspectionId: str
    includeModelsSDL: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetDataSourceRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str


class GetDomainNameRequestTypeDef(BaseValidatorModel):
    domainName: str


class GetFunctionRequestTypeDef(BaseValidatorModel):
    apiId: str
    functionId: str


class GetGraphqlApiEnvironmentVariablesRequestTypeDef(BaseValidatorModel):
    apiId: str


class GetGraphqlApiRequestTypeDef(BaseValidatorModel):
    apiId: str


class GetResolverRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str


class GetSchemaCreationStatusRequestTypeDef(BaseValidatorModel):
    apiId: str


class GetSourceApiAssociationRequestTypeDef(BaseValidatorModel):
    mergedApiIdentifier: str
    associationId: str


class LambdaConflictHandlerConfigTypeDef(BaseValidatorModel):
    lambdaConflictHandlerArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApiKeysRequestTypeDef(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListApisRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListChannelNamespacesRequestTypeDef(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataSourcesRequestTypeDef(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDomainNamesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFunctionsRequestTypeDef(BaseValidatorModel):
    apiId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListGraphqlApisRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    apiType: Optional[GraphQLApiTypeType] = None
    owner: Optional[OwnershipType] = None


class ListResolversByFunctionRequestTypeDef(BaseValidatorModel):
    apiId: str
    functionId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListResolversRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSourceApiAssociationsRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PipelineConfigOutputTypeDef(BaseValidatorModel):
    functions: Optional[List[str]] = None


class PipelineConfigTypeDef(BaseValidatorModel):
    functions: Optional[Sequence[str]] = None


class PutGraphqlApiEnvironmentVariablesRequestTypeDef(BaseValidatorModel):
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


class StartSchemaMergeRequestTypeDef(BaseValidatorModel):
    associationId: str
    mergedApiIdentifier: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDomainNameRequestTypeDef(BaseValidatorModel):
    domainName: str
    description: Optional[str] = None


class AdditionalAuthenticationProviderTypeDef(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    userPoolConfig: Optional[CognitoUserPoolConfigTypeDef] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfigTypeDef] = None


class EvaluateCodeRequestTypeDef(BaseValidatorModel):
    runtime: AppSyncRuntimeTypeDef
    code: str
    context: str
    function: Optional[str] = None


class AssociateApiResponseTypeDef(BaseValidatorModel):
    apiAssociation: ApiAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ApiCacheTypeDef(BaseValidatorModel):
    pass


class CreateApiCacheResponseTypeDef(BaseValidatorModel):
    apiCache: ApiCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ApiKeyTypeDef(BaseValidatorModel):
    pass


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class AssociateMergedGraphqlApiRequestTypeDef(BaseValidatorModel):
    sourceApiIdentifier: str
    mergedApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None


class AssociateSourceGraphqlApiRequestTypeDef(BaseValidatorModel):
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


class UpdateSourceApiAssociationRequestTypeDef(BaseValidatorModel):
    associationId: str
    mergedApiIdentifier: str
    description: Optional[str] = None
    sourceApiAssociationConfig: Optional[SourceApiAssociationConfigTypeDef] = None


class ChannelNamespaceTypeDef(BaseValidatorModel):
    apiId: Optional[str] = None
    name: Optional[str] = None
    subscribeAuthModes: Optional[List[AuthModeTypeDef]] = None
    publishAuthModes: Optional[List[AuthModeTypeDef]] = None
    codeHandlers: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    channelNamespaceArn: Optional[str] = None
    created: Optional[datetime] = None
    lastModified: Optional[datetime] = None


class CreateChannelNamespaceRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str
    subscribeAuthModes: Optional[Sequence[AuthModeTypeDef]] = None
    publishAuthModes: Optional[Sequence[AuthModeTypeDef]] = None
    codeHandlers: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateChannelNamespaceRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str
    subscribeAuthModes: Optional[Sequence[AuthModeTypeDef]] = None
    publishAuthModes: Optional[Sequence[AuthModeTypeDef]] = None
    codeHandlers: Optional[str] = None


class AuthProviderTypeDef(BaseValidatorModel):
    authType: AuthenticationTypeType
    cognitoConfig: Optional[CognitoConfigTypeDef] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfigTypeDef] = None


class AuthorizationConfigTypeDef(BaseValidatorModel):
    authorizationType: Literal["AWS_IAM"]
    awsIamConfig: Optional[AwsIamConfigTypeDef] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class StartSchemaCreationRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDomainNameResponseTypeDef(BaseValidatorModel):
    domainNameConfig: DomainNameConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
    stash: str
    outErrors: str
    ResponseMetadata: ResponseMetadataTypeDef


class SyncConfigTypeDef(BaseValidatorModel):
    conflictHandler: Optional[ConflictHandlerTypeType] = None
    conflictDetection: Optional[ConflictDetectionTypeType] = None
    lambdaConflictHandlerConfig: Optional[LambdaConflictHandlerConfigTypeDef] = None


class ListApiKeysRequestPaginateTypeDef(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApisRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListChannelNamespacesRequestPaginateTypeDef(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSourcesRequestPaginateTypeDef(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDomainNamesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFunctionsRequestPaginateTypeDef(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGraphqlApisRequestPaginateTypeDef(BaseValidatorModel):
    apiType: Optional[GraphQLApiTypeType] = None
    owner: Optional[OwnershipType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolversByFunctionRequestPaginateTypeDef(BaseValidatorModel):
    apiId: str
    functionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResolversRequestPaginateTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSourceApiAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    apiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSourceApiAssociationsResponseTypeDef(BaseValidatorModel):
    sourceApiAssociationSummaries: List[SourceApiAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartDataSourceIntrospectionRequestTypeDef(BaseValidatorModel):
    rdsDataApiConfig: Optional[RdsDataApiConfigTypeDef] = None


class RelationalDatabaseDataSourceConfigTypeDef(BaseValidatorModel):
    relationalDatabaseSourceType: Optional[Literal["RDS_HTTP_ENDPOINT"]] = None
    rdsHttpEndpointConfig: Optional[RdsHttpEndpointConfigTypeDef] = None


class CreateGraphqlApiRequestTypeDef(BaseValidatorModel):
    name: str
    authenticationType: AuthenticationTypeType
    logConfig: Optional[LogConfigTypeDef] = None
    userPoolConfig: Optional[UserPoolConfigTypeDef] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    additionalAuthenticationProviders: Optional[ Sequence[AdditionalAuthenticationProviderTypeDef] ] = None
    xrayEnabled: Optional[bool] = None
    lambdaAuthorizerConfig: Optional[LambdaAuthorizerConfigTypeDef] = None
    apiType: Optional[GraphQLApiTypeType] = None
    mergedApiExecutionRoleArn: Optional[str] = None
    visibility: Optional[GraphQLApiVisibilityType] = None
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
    additionalAuthenticationProviders: Optional[List[AdditionalAuthenticationProviderTypeDef]] = None
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


class UpdateGraphqlApiRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str
    authenticationType: AuthenticationTypeType
    logConfig: Optional[LogConfigTypeDef] = None
    userPoolConfig: Optional[UserPoolConfigTypeDef] = None
    openIDConnectConfig: Optional[OpenIDConnectConfigTypeDef] = None
    additionalAuthenticationProviders: Optional[ Sequence[AdditionalAuthenticationProviderTypeDef] ] = None
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


class CreateChannelNamespaceResponseTypeDef(BaseValidatorModel):
    channelNamespace: ChannelNamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetChannelNamespaceResponseTypeDef(BaseValidatorModel):
    channelNamespace: ChannelNamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelNamespacesResponseTypeDef(BaseValidatorModel):
    channelNamespaces: List[ChannelNamespaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateChannelNamespaceResponseTypeDef(BaseValidatorModel):
    channelNamespace: ChannelNamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EventConfigOutputTypeDef(BaseValidatorModel):
    authProviders: List[AuthProviderTypeDef]
    connectionAuthModes: List[AuthModeTypeDef]
    defaultPublishAuthModes: List[AuthModeTypeDef]
    defaultSubscribeAuthModes: List[AuthModeTypeDef]
    logConfig: Optional[EventLogConfigTypeDef] = None


class EventConfigTypeDef(BaseValidatorModel):
    authProviders: Sequence[AuthProviderTypeDef]
    connectionAuthModes: Sequence[AuthModeTypeDef]
    defaultPublishAuthModes: Sequence[AuthModeTypeDef]
    defaultSubscribeAuthModes: Sequence[AuthModeTypeDef]
    logConfig: Optional[EventLogConfigTypeDef] = None


class HttpDataSourceConfigTypeDef(BaseValidatorModel):
    endpoint: Optional[str] = None
    authorizationConfig: Optional[AuthorizationConfigTypeDef] = None


class EvaluateCodeErrorDetailTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    codeErrors: Optional[List[CodeErrorTypeDef]] = None


class DataSourceIntrospectionModelFieldTypeDef(BaseValidatorModel):
    pass


class DataSourceIntrospectionModelTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    fields: Optional[List[DataSourceIntrospectionModelFieldTypeDef]] = None
    primaryKey: Optional[DataSourceIntrospectionModelIndexTypeDef] = None
    indexes: Optional[List[DataSourceIntrospectionModelIndexTypeDef]] = None
    sdl: Optional[str] = None


class CreateFunctionRequestTypeDef(BaseValidatorModel):
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


class UpdateFunctionRequestTypeDef(BaseValidatorModel):
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


class PipelineConfigUnionTypeDef(BaseValidatorModel):
    pass


class CachingConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateResolverRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str
    dataSourceName: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    kind: Optional[ResolverKindType] = None
    pipelineConfig: Optional[PipelineConfigUnionTypeDef] = None
    syncConfig: Optional[SyncConfigTypeDef] = None
    cachingConfig: Optional[CachingConfigUnionTypeDef] = None
    maxBatchSize: Optional[int] = None
    runtime: Optional[AppSyncRuntimeTypeDef] = None
    code: Optional[str] = None
    metricsConfig: Optional[ResolverLevelMetricsConfigType] = None


class UpdateResolverRequestTypeDef(BaseValidatorModel):
    apiId: str
    typeName: str
    fieldName: str
    dataSourceName: Optional[str] = None
    requestMappingTemplate: Optional[str] = None
    responseMappingTemplate: Optional[str] = None
    kind: Optional[ResolverKindType] = None
    pipelineConfig: Optional[PipelineConfigUnionTypeDef] = None
    syncConfig: Optional[SyncConfigTypeDef] = None
    cachingConfig: Optional[CachingConfigUnionTypeDef] = None
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateGraphqlApiResponseTypeDef(BaseValidatorModel):
    graphqlApi: GraphqlApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ApiTypeDef(BaseValidatorModel):
    apiId: Optional[str] = None
    name: Optional[str] = None
    ownerContact: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    dns: Optional[Dict[str, str]] = None
    apiArn: Optional[str] = None
    created: Optional[datetime] = None
    xrayEnabled: Optional[bool] = None
    wafWebAclArn: Optional[str] = None
    eventConfig: Optional[EventConfigOutputTypeDef] = None


class EvaluateCodeResponseTypeDef(BaseValidatorModel):
    evaluationResult: str
    error: EvaluateCodeErrorDetailTypeDef
    logs: List[str]
    stash: str
    outErrors: str
    ResponseMetadata: ResponseMetadataTypeDef


class DataSourceIntrospectionResultTypeDef(BaseValidatorModel):
    models: Optional[List[DataSourceIntrospectionModelTypeDef]] = None
    nextToken: Optional[str] = None


class CreateFunctionResponseTypeDef(BaseValidatorModel):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFunctionResponseTypeDef(BaseValidatorModel):
    functionConfiguration: FunctionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFunctionsResponseTypeDef(BaseValidatorModel):
    functions: List[FunctionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListResolversResponseTypeDef(BaseValidatorModel):
    resolvers: List[ResolverTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateResolverResponseTypeDef(BaseValidatorModel):
    resolver: ResolverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateApiResponseTypeDef(BaseValidatorModel):
    api: ApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetApiResponseTypeDef(BaseValidatorModel):
    api: ApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListApisResponseTypeDef(BaseValidatorModel):
    apis: List[ApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateApiResponseTypeDef(BaseValidatorModel):
    api: ApiTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EventConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateApiRequestTypeDef(BaseValidatorModel):
    name: str
    ownerContact: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    eventConfig: Optional[EventConfigUnionTypeDef] = None


class UpdateApiRequestTypeDef(BaseValidatorModel):
    apiId: str
    name: str
    ownerContact: Optional[str] = None
    eventConfig: Optional[EventConfigUnionTypeDef] = None


class DataSourceTypeDef(BaseValidatorModel):
    pass


class CreateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    dataSources: List[DataSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataSourceIntrospectionResponseTypeDef(BaseValidatorModel):
    introspectionId: str
    introspectionStatus: DataSourceIntrospectionStatusType
    introspectionStatusDetail: str
    introspectionResult: DataSourceIntrospectionResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


