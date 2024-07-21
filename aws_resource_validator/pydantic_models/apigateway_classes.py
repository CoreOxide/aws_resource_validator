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
from aws_resource_validator.pydantic_models.apigateway_constants import *

class AccessLogSettingsTypeDef(BaseModel):
    format: Optional[str] = None
    destinationArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ThrottleSettingsTypeDef(BaseModel):
    burstLimit: Optional[int] = None
    rateLimit: Optional[float] = None

class ApiKeyTypeDef(BaseModel):
    id: Optional[str] = None
    value: Optional[str] = None
    name: Optional[str] = None
    customerId: Optional[str] = None
    description: Optional[str] = None
    enabled: Optional[bool] = None
    createdDate: Optional[datetime] = None
    lastUpdatedDate: Optional[datetime] = None
    stageKeys: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None

class AuthorizerTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[AuthorizerTypeType] = None
    providerARNs: Optional[List[str]] = None
    authType: Optional[str] = None
    authorizerUri: Optional[str] = None
    authorizerCredentials: Optional[str] = None
    identitySource: Optional[str] = None
    identityValidationExpression: Optional[str] = None
    authorizerResultTtlInSeconds: Optional[int] = None

class BasePathMappingTypeDef(BaseModel):
    basePath: Optional[str] = None
    restApiId: Optional[str] = None
    stage: Optional[str] = None

class CanarySettingsOutputTypeDef(BaseModel):
    percentTraffic: Optional[float] = None
    deploymentId: Optional[str] = None
    stageVariableOverrides: Optional[Dict[str, str]] = None
    useStageCache: Optional[bool] = None

class CanarySettingsTypeDef(BaseModel):
    percentTraffic: Optional[float] = None
    deploymentId: Optional[str] = None
    stageVariableOverrides: Optional[Mapping[str, str]] = None
    useStageCache: Optional[bool] = None

class ClientCertificateTypeDef(BaseModel):
    clientCertificateId: Optional[str] = None
    description: Optional[str] = None
    pemEncodedCertificate: Optional[str] = None
    createdDate: Optional[datetime] = None
    expirationDate: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class StageKeyTypeDef(BaseModel):
    restApiId: Optional[str] = None
    stageName: Optional[str] = None

class CreateAuthorizerRequestRequestTypeDef(BaseModel):
    restApiId: str
    name: str
    type: AuthorizerTypeType
    providerARNs: Optional[Sequence[str]] = None
    authType: Optional[str] = None
    authorizerUri: Optional[str] = None
    authorizerCredentials: Optional[str] = None
    identitySource: Optional[str] = None
    identityValidationExpression: Optional[str] = None
    authorizerResultTtlInSeconds: Optional[int] = None

class CreateBasePathMappingRequestRequestTypeDef(BaseModel):
    domainName: str
    restApiId: str
    basePath: Optional[str] = None
    stage: Optional[str] = None

class DeploymentCanarySettingsTypeDef(BaseModel):
    percentTraffic: Optional[float] = None
    stageVariableOverrides: Optional[Mapping[str, str]] = None
    useStageCache: Optional[bool] = None

class DocumentationPartLocationTypeDef(BaseModel):
    type: DocumentationPartTypeType
    path: Optional[str] = None
    method: Optional[str] = None
    statusCode: Optional[str] = None
    name: Optional[str] = None

class CreateDocumentationVersionRequestRequestTypeDef(BaseModel):
    restApiId: str
    documentationVersion: str
    stageName: Optional[str] = None
    description: Optional[str] = None

class EndpointConfigurationTypeDef(BaseModel):
    types: Optional[Sequence[EndpointTypeType]] = None
    vpcEndpointIds: Optional[Sequence[str]] = None

class MutualTlsAuthenticationInputTypeDef(BaseModel):
    truststoreUri: Optional[str] = None
    truststoreVersion: Optional[str] = None

class CreateModelRequestRequestTypeDef(BaseModel):
    restApiId: str
    name: str
    contentType: str
    description: Optional[str] = None
    schema: Optional[str] = None

class CreateRequestValidatorRequestRequestTypeDef(BaseModel):
    restApiId: str
    name: Optional[str] = None
    validateRequestBody: Optional[bool] = None
    validateRequestParameters: Optional[bool] = None

class CreateResourceRequestRequestTypeDef(BaseModel):
    restApiId: str
    parentId: str
    pathPart: str

class CreateUsagePlanKeyRequestRequestTypeDef(BaseModel):
    usagePlanId: str
    keyId: str
    keyType: str

class QuotaSettingsTypeDef(BaseModel):
    limit: Optional[int] = None
    offset: Optional[int] = None
    period: Optional[QuotaPeriodTypeType] = None

class CreateVpcLinkRequestRequestTypeDef(BaseModel):
    name: str
    targetArns: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteApiKeyRequestRequestTypeDef(BaseModel):
    apiKey: str

class DeleteAuthorizerRequestRequestTypeDef(BaseModel):
    restApiId: str
    authorizerId: str

class DeleteBasePathMappingRequestRequestTypeDef(BaseModel):
    domainName: str
    basePath: str

class DeleteClientCertificateRequestRequestTypeDef(BaseModel):
    clientCertificateId: str

class DeleteDeploymentRequestRequestTypeDef(BaseModel):
    restApiId: str
    deploymentId: str

class DeleteDocumentationPartRequestRequestTypeDef(BaseModel):
    restApiId: str
    documentationPartId: str

class DeleteDocumentationVersionRequestRequestTypeDef(BaseModel):
    restApiId: str
    documentationVersion: str

class DeleteDomainNameRequestRequestTypeDef(BaseModel):
    domainName: str

class DeleteGatewayResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    responseType: GatewayResponseTypeType

class DeleteIntegrationRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str

class DeleteIntegrationResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class DeleteMethodRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str

class DeleteMethodResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class DeleteModelRequestRequestTypeDef(BaseModel):
    restApiId: str
    modelName: str

class DeleteRequestValidatorRequestRequestTypeDef(BaseModel):
    restApiId: str
    requestValidatorId: str

class DeleteResourceRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str

class DeleteRestApiRequestRequestTypeDef(BaseModel):
    restApiId: str

class DeleteStageRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: str

class DeleteUsagePlanKeyRequestRequestTypeDef(BaseModel):
    usagePlanId: str
    keyId: str

class DeleteUsagePlanRequestRequestTypeDef(BaseModel):
    usagePlanId: str

class DeleteVpcLinkRequestRequestTypeDef(BaseModel):
    vpcLinkId: str

class MethodSnapshotTypeDef(BaseModel):
    authorizationType: Optional[str] = None
    apiKeyRequired: Optional[bool] = None

class DocumentationVersionTypeDef(BaseModel):
    version: Optional[str] = None
    createdDate: Optional[datetime] = None
    description: Optional[str] = None

class EndpointConfigurationOutputTypeDef(BaseModel):
    types: Optional[List[EndpointTypeType]] = None
    vpcEndpointIds: Optional[List[str]] = None

class MutualTlsAuthenticationTypeDef(BaseModel):
    truststoreUri: Optional[str] = None
    truststoreVersion: Optional[str] = None
    truststoreWarnings: Optional[List[str]] = None

class EndpointConfigurationExtraOutputTypeDef(BaseModel):
    types: Optional[List[EndpointTypeType]] = None
    vpcEndpointIds: Optional[List[str]] = None

class FlushStageAuthorizersCacheRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: str

class FlushStageCacheRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: str

class GatewayResponseTypeDef(BaseModel):
    responseType: Optional[GatewayResponseTypeType] = None
    statusCode: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None
    defaultResponse: Optional[bool] = None

class GenerateClientCertificateRequestRequestTypeDef(BaseModel):
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetApiKeyRequestRequestTypeDef(BaseModel):
    apiKey: str
    includeValue: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetApiKeysRequestRequestTypeDef(BaseModel):
    position: Optional[str] = None
    limit: Optional[int] = None
    nameQuery: Optional[str] = None
    customerId: Optional[str] = None
    includeValues: Optional[bool] = None

class GetAuthorizerRequestRequestTypeDef(BaseModel):
    restApiId: str
    authorizerId: str

class GetAuthorizersRequestRequestTypeDef(BaseModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetBasePathMappingRequestRequestTypeDef(BaseModel):
    domainName: str
    basePath: str

class GetBasePathMappingsRequestRequestTypeDef(BaseModel):
    domainName: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetClientCertificateRequestRequestTypeDef(BaseModel):
    clientCertificateId: str

class GetClientCertificatesRequestRequestTypeDef(BaseModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class GetDeploymentRequestRequestTypeDef(BaseModel):
    restApiId: str
    deploymentId: str
    embed: Optional[Sequence[str]] = None

class GetDeploymentsRequestRequestTypeDef(BaseModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetDocumentationPartRequestRequestTypeDef(BaseModel):
    restApiId: str
    documentationPartId: str

class GetDocumentationPartsRequestRequestTypeDef(BaseModel):
    restApiId: str
    type: Optional[DocumentationPartTypeType] = None
    nameQuery: Optional[str] = None
    path: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None
    locationStatus: Optional[LocationStatusTypeType] = None

class GetDocumentationVersionRequestRequestTypeDef(BaseModel):
    restApiId: str
    documentationVersion: str

class GetDocumentationVersionsRequestRequestTypeDef(BaseModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetDomainNameRequestRequestTypeDef(BaseModel):
    domainName: str

class GetDomainNamesRequestRequestTypeDef(BaseModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class GetExportRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: str
    exportType: str
    parameters: Optional[Mapping[str, str]] = None
    accepts: Optional[str] = None

class GetGatewayResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    responseType: GatewayResponseTypeType

class GetGatewayResponsesRequestRequestTypeDef(BaseModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetIntegrationRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str

class GetIntegrationResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class GetMethodRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str

class GetMethodResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class GetModelRequestRequestTypeDef(BaseModel):
    restApiId: str
    modelName: str
    flatten: Optional[bool] = None

class GetModelTemplateRequestRequestTypeDef(BaseModel):
    restApiId: str
    modelName: str

class GetModelsRequestRequestTypeDef(BaseModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetRequestValidatorRequestRequestTypeDef(BaseModel):
    restApiId: str
    requestValidatorId: str

class GetRequestValidatorsRequestRequestTypeDef(BaseModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetResourceRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    embed: Optional[Sequence[str]] = None

class GetResourcesRequestRequestTypeDef(BaseModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None
    embed: Optional[Sequence[str]] = None

class GetRestApiRequestRequestTypeDef(BaseModel):
    restApiId: str

class GetRestApisRequestRequestTypeDef(BaseModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class GetSdkRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: str
    sdkType: str
    parameters: Optional[Mapping[str, str]] = None

class GetSdkTypeRequestRequestTypeDef(BaseModel):
    id: str

class GetSdkTypesRequestRequestTypeDef(BaseModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class GetStageRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: str

class GetStagesRequestRequestTypeDef(BaseModel):
    restApiId: str
    deploymentId: Optional[str] = None

class GetTagsRequestRequestTypeDef(BaseModel):
    resourceArn: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetUsagePlanKeyRequestRequestTypeDef(BaseModel):
    usagePlanId: str
    keyId: str

class GetUsagePlanKeysRequestRequestTypeDef(BaseModel):
    usagePlanId: str
    position: Optional[str] = None
    limit: Optional[int] = None
    nameQuery: Optional[str] = None

class GetUsagePlanRequestRequestTypeDef(BaseModel):
    usagePlanId: str

class GetUsagePlansRequestRequestTypeDef(BaseModel):
    position: Optional[str] = None
    keyId: Optional[str] = None
    limit: Optional[int] = None

class GetUsageRequestRequestTypeDef(BaseModel):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None

class GetVpcLinkRequestRequestTypeDef(BaseModel):
    vpcLinkId: str

class GetVpcLinksRequestRequestTypeDef(BaseModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class IntegrationResponseTypeDef(BaseModel):
    statusCode: Optional[str] = None
    selectionPattern: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None

class TlsConfigTypeDef(BaseModel):
    insecureSkipVerification: Optional[bool] = None

class MethodResponseTypeDef(BaseModel):
    statusCode: Optional[str] = None
    responseParameters: Optional[Dict[str, bool]] = None
    responseModels: Optional[Dict[str, str]] = None

class MethodSettingTypeDef(BaseModel):
    metricsEnabled: Optional[bool] = None
    loggingLevel: Optional[str] = None
    dataTraceEnabled: Optional[bool] = None
    throttlingBurstLimit: Optional[int] = None
    throttlingRateLimit: Optional[float] = None
    cachingEnabled: Optional[bool] = None
    cacheTtlInSeconds: Optional[int] = None
    cacheDataEncrypted: Optional[bool] = None
    requireAuthorizationForCacheControl: Optional[bool] = None
    unauthorizedCacheControlHeaderStrategy: Optional[       UnauthorizedCacheControlHeaderStrategyType     ] = None

class ModelTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    schema: Optional[str] = None
    contentType: Optional[str] = None

class PatchOperationTypeDef(BaseModel):
    op: Optional[OpType] = None
    path: Optional[str] = None
    value: Optional[str] = None
    from: Optional[str] = None

class PutGatewayResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    responseType: GatewayResponseTypeType
    statusCode: Optional[str] = None
    responseParameters: Optional[Mapping[str, str]] = None
    responseTemplates: Optional[Mapping[str, str]] = None

class PutIntegrationResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    selectionPattern: Optional[str] = None
    responseParameters: Optional[Mapping[str, str]] = None
    responseTemplates: Optional[Mapping[str, str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None

class PutMethodRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    authorizationType: str
    authorizerId: Optional[str] = None
    apiKeyRequired: Optional[bool] = None
    operationName: Optional[str] = None
    requestParameters: Optional[Mapping[str, bool]] = None
    requestModels: Optional[Mapping[str, str]] = None
    requestValidatorId: Optional[str] = None
    authorizationScopes: Optional[Sequence[str]] = None

class PutMethodResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    responseParameters: Optional[Mapping[str, bool]] = None
    responseModels: Optional[Mapping[str, str]] = None

class RequestValidatorTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    validateRequestBody: Optional[bool] = None
    validateRequestParameters: Optional[bool] = None

class SdkConfigurationPropertyTypeDef(BaseModel):
    name: Optional[str] = None
    friendlyName: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    defaultValue: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TestInvokeAuthorizerRequestRequestTypeDef(BaseModel):
    restApiId: str
    authorizerId: str
    headers: Optional[Mapping[str, str]] = None
    multiValueHeaders: Optional[Mapping[str, Sequence[str]]] = None
    pathWithQueryString: Optional[str] = None
    body: Optional[str] = None
    stageVariables: Optional[Mapping[str, str]] = None
    additionalContext: Optional[Mapping[str, str]] = None

class TestInvokeMethodRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    pathWithQueryString: Optional[str] = None
    body: Optional[str] = None
    headers: Optional[Mapping[str, str]] = None
    multiValueHeaders: Optional[Mapping[str, Sequence[str]]] = None
    clientCertificateId: Optional[str] = None
    stageVariables: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UsagePlanKeyTypeDef(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    name: Optional[str] = None

class VpcLinkTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    targetArns: Optional[List[str]] = None
    status: Optional[VpcLinkStatusType] = None
    statusMessage: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ApiKeyIdsTypeDef(BaseModel):
    ids: List[str]
    warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ApiKeyResponseTypeDef(BaseModel):
    id: str
    value: str
    name: str
    customerId: str
    description: str
    enabled: bool
    createdDate: datetime
    lastUpdatedDate: datetime
    stageKeys: List[str]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizerResponseTypeDef(BaseModel):
    id: str
    name: str
    type: AuthorizerTypeType
    providerARNs: List[str]
    authType: str
    authorizerUri: str
    authorizerCredentials: str
    identitySource: str
    identityValidationExpression: str
    authorizerResultTtlInSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class BasePathMappingResponseTypeDef(BaseModel):
    basePath: str
    restApiId: str
    stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClientCertificateResponseTypeDef(BaseModel):
    clientCertificateId: str
    description: str
    pemEncodedCertificate: str
    createdDate: datetime
    expirationDate: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentationPartIdsTypeDef(BaseModel):
    ids: List[str]
    warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentationVersionResponseTypeDef(BaseModel):
    version: str
    createdDate: datetime
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportResponseTypeDef(BaseModel):
    contentType: str
    contentDisposition: str
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayResponseResponseTypeDef(BaseModel):
    responseType: GatewayResponseTypeType
    statusCode: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    defaultResponse: bool
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationResponseResponseTypeDef(BaseModel):
    statusCode: str
    selectionPattern: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    contentHandling: ContentHandlingStrategyType
    ResponseMetadata: ResponseMetadataTypeDef

class MethodResponseResponseTypeDef(BaseModel):
    statusCode: str
    responseParameters: Dict[str, bool]
    responseModels: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ModelResponseTypeDef(BaseModel):
    id: str
    name: str
    description: str
    schema: str
    contentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class RequestValidatorResponseTypeDef(BaseModel):
    id: str
    name: str
    validateRequestBody: bool
    validateRequestParameters: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SdkResponseTypeDef(BaseModel):
    contentType: str
    contentDisposition: str
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class TagsTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TemplateTypeDef(BaseModel):
    value: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestInvokeAuthorizerResponseTypeDef(BaseModel):
    clientStatus: int
    log: str
    latency: int
    principalId: str
    policy: str
    authorization: Dict[str, List[str]]
    claims: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TestInvokeMethodResponseTypeDef(BaseModel):
    status: int
    body: str
    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    log: str
    latency: int
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlanKeyResponseTypeDef(BaseModel):
    id: str
    type: str
    value: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UsageTypeDef(BaseModel):
    usagePlanId: str
    startDate: str
    endDate: str
    position: str
    items: Dict[str, List[List[int]]]
    ResponseMetadata: ResponseMetadataTypeDef

class VpcLinkResponseTypeDef(BaseModel):
    id: str
    name: str
    description: str
    targetArns: List[str]
    status: VpcLinkStatusType
    statusMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class AccountTypeDef(BaseModel):
    cloudwatchRoleArn: str
    throttleSettings: ThrottleSettingsTypeDef
    features: List[str]
    apiKeyVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ApiStageExtraOutputTypeDef(BaseModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Dict[str, ThrottleSettingsTypeDef]] = None

class ApiStageOutputTypeDef(BaseModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Dict[str, ThrottleSettingsTypeDef]] = None

class ApiStageTypeDef(BaseModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Mapping[str, ThrottleSettingsTypeDef]] = None

class ApiKeysTypeDef(BaseModel):
    warnings: List[str]
    position: str
    items: List[ApiKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizersTypeDef(BaseModel):
    position: str
    items: List[AuthorizerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BasePathMappingsTypeDef(BaseModel):
    position: str
    items: List[BasePathMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportApiKeysRequestRequestTypeDef(BaseModel):
    body: BlobTypeDef
    format: Literal["csv"]
    failOnWarnings: Optional[bool] = None

class ImportDocumentationPartsRequestRequestTypeDef(BaseModel):
    restApiId: str
    body: BlobTypeDef
    mode: Optional[PutModeType] = None
    failOnWarnings: Optional[bool] = None

class ImportRestApiRequestRequestTypeDef(BaseModel):
    body: BlobTypeDef
    failOnWarnings: Optional[bool] = None
    parameters: Optional[Mapping[str, str]] = None

class PutRestApiRequestRequestTypeDef(BaseModel):
    restApiId: str
    body: BlobTypeDef
    mode: Optional[PutModeType] = None
    failOnWarnings: Optional[bool] = None
    parameters: Optional[Mapping[str, str]] = None

class CreateStageRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: str
    deploymentId: str
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    variables: Optional[Mapping[str, str]] = None
    documentationVersion: Optional[str] = None
    canarySettings: Optional[CanarySettingsTypeDef] = None
    tracingEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class ClientCertificatesTypeDef(BaseModel):
    position: str
    items: List[ClientCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiKeyRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    enabled: Optional[bool] = None
    generateDistinctId: Optional[bool] = None
    value: Optional[str] = None
    stageKeys: Optional[Sequence[StageKeyTypeDef]] = None
    customerId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateDeploymentRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: Optional[str] = None
    stageDescription: Optional[str] = None
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    variables: Optional[Mapping[str, str]] = None
    canarySettings: Optional[DeploymentCanarySettingsTypeDef] = None
    tracingEnabled: Optional[bool] = None

class CreateDocumentationPartRequestRequestTypeDef(BaseModel):
    restApiId: str
    location: DocumentationPartLocationTypeDef
    properties: str

class DocumentationPartResponseTypeDef(BaseModel):
    id: str
    location: DocumentationPartLocationTypeDef
    properties: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentationPartTypeDef(BaseModel):
    id: Optional[str] = None
    location: Optional[DocumentationPartLocationTypeDef] = None
    properties: Optional[str] = None

class CreateRestApiRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    version: Optional[str] = None
    cloneFrom: Optional[str] = None
    binaryMediaTypes: Optional[Sequence[str]] = None
    minimumCompressionSize: Optional[int] = None
    apiKeySource: Optional[ApiKeySourceTypeType] = None
    endpointConfiguration: Optional[EndpointConfigurationTypeDef] = None
    policy: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    disableExecuteApiEndpoint: Optional[bool] = None

class CreateDomainNameRequestRequestTypeDef(BaseModel):
    domainName: str
    certificateName: Optional[str] = None
    certificateBody: Optional[str] = None
    certificatePrivateKey: Optional[str] = None
    certificateChain: Optional[str] = None
    certificateArn: Optional[str] = None
    regionalCertificateName: Optional[str] = None
    regionalCertificateArn: Optional[str] = None
    endpointConfiguration: Optional[EndpointConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    securityPolicy: Optional[SecurityPolicyType] = None
    mutualTlsAuthentication: Optional[MutualTlsAuthenticationInputTypeDef] = None
    ownershipVerificationCertificateArn: Optional[str] = None

class DeploymentResponseTypeDef(BaseModel):
    id: str
    description: str
    createdDate: datetime
    apiSummary: Dict[str, Dict[str, MethodSnapshotTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentTypeDef(BaseModel):
    id: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[datetime] = None
    apiSummary: Optional[Dict[str, Dict[str, MethodSnapshotTypeDef]]] = None

class DocumentationVersionsTypeDef(BaseModel):
    position: str
    items: List[DocumentationVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestApiResponseTypeDef(BaseModel):
    id: str
    name: str
    description: str
    createdDate: datetime
    version: str
    warnings: List[str]
    binaryMediaTypes: List[str]
    minimumCompressionSize: int
    apiKeySource: ApiKeySourceTypeType
    endpointConfiguration: EndpointConfigurationOutputTypeDef
    policy: str
    tags: Dict[str, str]
    disableExecuteApiEndpoint: bool
    rootResourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestApiTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None
    warnings: Optional[List[str]] = None
    binaryMediaTypes: Optional[List[str]] = None
    minimumCompressionSize: Optional[int] = None
    apiKeySource: Optional[ApiKeySourceTypeType] = None
    endpointConfiguration: Optional[EndpointConfigurationOutputTypeDef] = None
    policy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    disableExecuteApiEndpoint: Optional[bool] = None
    rootResourceId: Optional[str] = None

class DomainNameResponseTypeDef(BaseModel):
    domainName: str
    certificateName: str
    certificateArn: str
    certificateUploadDate: datetime
    regionalDomainName: str
    regionalHostedZoneId: str
    regionalCertificateName: str
    regionalCertificateArn: str
    distributionDomainName: str
    distributionHostedZoneId: str
    endpointConfiguration: EndpointConfigurationOutputTypeDef
    domainNameStatus: DomainNameStatusType
    domainNameStatusMessage: str
    securityPolicy: SecurityPolicyType
    tags: Dict[str, str]
    mutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    ownershipVerificationCertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNameTypeDef(BaseModel):
    domainName: Optional[str] = None
    certificateName: Optional[str] = None
    certificateArn: Optional[str] = None
    certificateUploadDate: Optional[datetime] = None
    regionalDomainName: Optional[str] = None
    regionalHostedZoneId: Optional[str] = None
    regionalCertificateName: Optional[str] = None
    regionalCertificateArn: Optional[str] = None
    distributionDomainName: Optional[str] = None
    distributionHostedZoneId: Optional[str] = None
    endpointConfiguration: Optional[EndpointConfigurationOutputTypeDef] = None
    domainNameStatus: Optional[DomainNameStatusType] = None
    domainNameStatusMessage: Optional[str] = None
    securityPolicy: Optional[SecurityPolicyType] = None
    tags: Optional[Dict[str, str]] = None
    mutualTlsAuthentication: Optional[MutualTlsAuthenticationTypeDef] = None
    ownershipVerificationCertificateArn: Optional[str] = None

class GatewayResponsesTypeDef(BaseModel):
    position: str
    items: List[GatewayResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiKeysRequestGetApiKeysPaginateTypeDef(BaseModel):
    nameQuery: Optional[str] = None
    customerId: Optional[str] = None
    includeValues: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAuthorizersRequestGetAuthorizersPaginateTypeDef(BaseModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBasePathMappingsRequestGetBasePathMappingsPaginateTypeDef(BaseModel):
    domainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetClientCertificatesRequestGetClientCertificatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDeploymentsRequestGetDeploymentsPaginateTypeDef(BaseModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDocumentationPartsRequestGetDocumentationPartsPaginateTypeDef(BaseModel):
    restApiId: str
    type: Optional[DocumentationPartTypeType] = None
    nameQuery: Optional[str] = None
    path: Optional[str] = None
    locationStatus: Optional[LocationStatusTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDocumentationVersionsRequestGetDocumentationVersionsPaginateTypeDef(BaseModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDomainNamesRequestGetDomainNamesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetGatewayResponsesRequestGetGatewayResponsesPaginateTypeDef(BaseModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetModelsRequestGetModelsPaginateTypeDef(BaseModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRequestValidatorsRequestGetRequestValidatorsPaginateTypeDef(BaseModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourcesRequestGetResourcesPaginateTypeDef(BaseModel):
    restApiId: str
    embed: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRestApisRequestGetRestApisPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSdkTypesRequestGetSdkTypesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUsagePlanKeysRequestGetUsagePlanKeysPaginateTypeDef(BaseModel):
    usagePlanId: str
    nameQuery: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUsagePlansRequestGetUsagePlansPaginateTypeDef(BaseModel):
    keyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUsageRequestGetUsagePaginateTypeDef(BaseModel):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetVpcLinksRequestGetVpcLinksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class IntegrationExtraResponseTypeDef(BaseModel):
    type: IntegrationTypeType
    httpMethod: str
    uri: str
    connectionType: ConnectionTypeType
    connectionId: str
    credentials: str
    requestParameters: Dict[str, str]
    requestTemplates: Dict[str, str]
    passthroughBehavior: str
    contentHandling: ContentHandlingStrategyType
    timeoutInMillis: int
    cacheNamespace: str
    cacheKeyParameters: List[str]
    integrationResponses: Dict[str, IntegrationResponseTypeDef]
    tlsConfig: TlsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationTypeDef(BaseModel):
    type: Optional[IntegrationTypeType] = None
    httpMethod: Optional[str] = None
    uri: Optional[str] = None
    connectionType: Optional[ConnectionTypeType] = None
    connectionId: Optional[str] = None
    credentials: Optional[str] = None
    requestParameters: Optional[Dict[str, str]] = None
    requestTemplates: Optional[Dict[str, str]] = None
    passthroughBehavior: Optional[str] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None
    timeoutInMillis: Optional[int] = None
    cacheNamespace: Optional[str] = None
    cacheKeyParameters: Optional[List[str]] = None
    integrationResponses: Optional[Dict[str, IntegrationResponseTypeDef]] = None
    tlsConfig: Optional[TlsConfigTypeDef] = None

class PutIntegrationRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    type: IntegrationTypeType
    integrationHttpMethod: Optional[str] = None
    uri: Optional[str] = None
    connectionType: Optional[ConnectionTypeType] = None
    connectionId: Optional[str] = None
    credentials: Optional[str] = None
    requestParameters: Optional[Mapping[str, str]] = None
    requestTemplates: Optional[Mapping[str, str]] = None
    passthroughBehavior: Optional[str] = None
    cacheNamespace: Optional[str] = None
    cacheKeyParameters: Optional[Sequence[str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None
    timeoutInMillis: Optional[int] = None
    tlsConfig: Optional[TlsConfigTypeDef] = None

class StageResponseTypeDef(BaseModel):
    deploymentId: str
    clientCertificateId: str
    stageName: str
    description: str
    cacheClusterEnabled: bool
    cacheClusterSize: CacheClusterSizeType
    cacheClusterStatus: CacheClusterStatusType
    methodSettings: Dict[str, MethodSettingTypeDef]
    variables: Dict[str, str]
    documentationVersion: str
    accessLogSettings: AccessLogSettingsTypeDef
    canarySettings: CanarySettingsOutputTypeDef
    tracingEnabled: bool
    webAclArn: str
    tags: Dict[str, str]
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StageTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    clientCertificateId: Optional[str] = None
    stageName: Optional[str] = None
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    cacheClusterStatus: Optional[CacheClusterStatusType] = None
    methodSettings: Optional[Dict[str, MethodSettingTypeDef]] = None
    variables: Optional[Dict[str, str]] = None
    documentationVersion: Optional[str] = None
    accessLogSettings: Optional[AccessLogSettingsTypeDef] = None
    canarySettings: Optional[CanarySettingsOutputTypeDef] = None
    tracingEnabled: Optional[bool] = None
    webAclArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    createdDate: Optional[datetime] = None
    lastUpdatedDate: Optional[datetime] = None

class ModelsTypeDef(BaseModel):
    position: str
    items: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountRequestRequestTypeDef(BaseModel):
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateApiKeyRequestRequestTypeDef(BaseModel):
    apiKey: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateAuthorizerRequestRequestTypeDef(BaseModel):
    restApiId: str
    authorizerId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateBasePathMappingRequestRequestTypeDef(BaseModel):
    domainName: str
    basePath: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateClientCertificateRequestRequestTypeDef(BaseModel):
    clientCertificateId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateDeploymentRequestRequestTypeDef(BaseModel):
    restApiId: str
    deploymentId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateDocumentationPartRequestRequestTypeDef(BaseModel):
    restApiId: str
    documentationPartId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateDocumentationVersionRequestRequestTypeDef(BaseModel):
    restApiId: str
    documentationVersion: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateDomainNameRequestRequestTypeDef(BaseModel):
    domainName: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateGatewayResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    responseType: GatewayResponseTypeType
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateIntegrationRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateIntegrationResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateMethodRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateMethodResponseRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateModelRequestRequestTypeDef(BaseModel):
    restApiId: str
    modelName: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateRequestValidatorRequestRequestTypeDef(BaseModel):
    restApiId: str
    requestValidatorId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateResourceRequestRequestTypeDef(BaseModel):
    restApiId: str
    resourceId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateRestApiRequestRequestTypeDef(BaseModel):
    restApiId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateStageRequestRequestTypeDef(BaseModel):
    restApiId: str
    stageName: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateUsagePlanRequestRequestTypeDef(BaseModel):
    usagePlanId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateUsageRequestRequestTypeDef(BaseModel):
    usagePlanId: str
    keyId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateVpcLinkRequestRequestTypeDef(BaseModel):
    vpcLinkId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class RequestValidatorsTypeDef(BaseModel):
    position: str
    items: List[RequestValidatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SdkTypeResponseTypeDef(BaseModel):
    id: str
    friendlyName: str
    description: str
    configurationProperties: List[SdkConfigurationPropertyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SdkTypeTypeDef(BaseModel):
    id: Optional[str] = None
    friendlyName: Optional[str] = None
    description: Optional[str] = None
    configurationProperties: Optional[List[SdkConfigurationPropertyTypeDef]] = None

class UsagePlanKeysTypeDef(BaseModel):
    position: str
    items: List[UsagePlanKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VpcLinksTypeDef(BaseModel):
    position: str
    items: List[VpcLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlanResponseTypeDef(BaseModel):
    id: str
    name: str
    description: str
    apiStages: List[ApiStageOutputTypeDef]
    throttle: ThrottleSettingsTypeDef
    quota: QuotaSettingsTypeDef
    productCode: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlanTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    apiStages: Optional[List[ApiStageOutputTypeDef]] = None
    throttle: Optional[ThrottleSettingsTypeDef] = None
    quota: Optional[QuotaSettingsTypeDef] = None
    productCode: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class DocumentationPartsTypeDef(BaseModel):
    position: str
    items: List[DocumentationPartTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentsTypeDef(BaseModel):
    position: str
    items: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestApisTypeDef(BaseModel):
    position: str
    items: List[RestApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNamesTypeDef(BaseModel):
    position: str
    items: List[DomainNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MethodExtraResponseTypeDef(BaseModel):
    httpMethod: str
    authorizationType: str
    authorizerId: str
    apiKeyRequired: bool
    requestValidatorId: str
    operationName: str
    requestParameters: Dict[str, bool]
    requestModels: Dict[str, str]
    methodResponses: Dict[str, MethodResponseTypeDef]
    methodIntegration: IntegrationTypeDef
    authorizationScopes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class MethodTypeDef(BaseModel):
    httpMethod: Optional[str] = None
    authorizationType: Optional[str] = None
    authorizerId: Optional[str] = None
    apiKeyRequired: Optional[bool] = None
    requestValidatorId: Optional[str] = None
    operationName: Optional[str] = None
    requestParameters: Optional[Dict[str, bool]] = None
    requestModels: Optional[Dict[str, str]] = None
    methodResponses: Optional[Dict[str, MethodResponseTypeDef]] = None
    methodIntegration: Optional[IntegrationTypeDef] = None
    authorizationScopes: Optional[List[str]] = None

class StagesTypeDef(BaseModel):
    item: List[StageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SdkTypesTypeDef(BaseModel):
    position: str
    items: List[SdkTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlansTypeDef(BaseModel):
    position: str
    items: List[UsagePlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsagePlanRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    apiStages: Optional[Sequence[ApiStageUnionTypeDef]] = None
    throttle: Optional[ThrottleSettingsTypeDef] = None
    quota: Optional[QuotaSettingsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class ResourceResponseTypeDef(BaseModel):
    id: str
    parentId: str
    pathPart: str
    path: str
    resourceMethods: Dict[str, MethodTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceTypeDef(BaseModel):
    id: Optional[str] = None
    parentId: Optional[str] = None
    pathPart: Optional[str] = None
    path: Optional[str] = None
    resourceMethods: Optional[Dict[str, MethodTypeDef]] = None

class ResourcesTypeDef(BaseModel):
    position: str
    items: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

