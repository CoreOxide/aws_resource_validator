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
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.apigateway_constants import *

class AccessLogSettingsTypeDef(BaseValidatorModel):
    format: Optional[str] = None
    destinationArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ThrottleSettingsTypeDef(BaseValidatorModel):
    burstLimit: Optional[int] = None
    rateLimit: Optional[float] = None

class ApiKeyTypeDef(BaseValidatorModel):
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

class AuthorizerTypeDef(BaseValidatorModel):
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

class BasePathMappingTypeDef(BaseValidatorModel):
    basePath: Optional[str] = None
    restApiId: Optional[str] = None
    stage: Optional[str] = None

class CanarySettingsOutputTypeDef(BaseValidatorModel):
    percentTraffic: Optional[float] = None
    deploymentId: Optional[str] = None
    stageVariableOverrides: Optional[Dict[str, str]] = None
    useStageCache: Optional[bool] = None

class CanarySettingsTypeDef(BaseValidatorModel):
    percentTraffic: Optional[float] = None
    deploymentId: Optional[str] = None
    stageVariableOverrides: Optional[Mapping[str, str]] = None
    useStageCache: Optional[bool] = None

class ClientCertificateTypeDef(BaseValidatorModel):
    clientCertificateId: Optional[str] = None
    description: Optional[str] = None
    pemEncodedCertificate: Optional[str] = None
    createdDate: Optional[datetime] = None
    expirationDate: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class StageKeyTypeDef(BaseValidatorModel):
    restApiId: Optional[str] = None
    stageName: Optional[str] = None

class CreateAuthorizerRequestRequestTypeDef(BaseValidatorModel):
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

class CreateBasePathMappingRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    restApiId: str
    basePath: Optional[str] = None
    stage: Optional[str] = None

class DeploymentCanarySettingsTypeDef(BaseValidatorModel):
    percentTraffic: Optional[float] = None
    stageVariableOverrides: Optional[Mapping[str, str]] = None
    useStageCache: Optional[bool] = None

class DocumentationPartLocationTypeDef(BaseValidatorModel):
    type: DocumentationPartTypeType
    path: Optional[str] = None
    method: Optional[str] = None
    statusCode: Optional[str] = None
    name: Optional[str] = None

class CreateDocumentationVersionRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationVersion: str
    stageName: Optional[str] = None
    description: Optional[str] = None

class EndpointConfigurationTypeDef(BaseValidatorModel):
    types: Optional[Sequence[EndpointTypeType]] = None
    vpcEndpointIds: Optional[Sequence[str]] = None

class MutualTlsAuthenticationInputTypeDef(BaseValidatorModel):
    truststoreUri: Optional[str] = None
    truststoreVersion: Optional[str] = None

class CreateModelRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    name: str
    contentType: str
    description: Optional[str] = None
    schema: Optional[str] = None

class CreateRequestValidatorRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    name: Optional[str] = None
    validateRequestBody: Optional[bool] = None
    validateRequestParameters: Optional[bool] = None

class CreateResourceRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    parentId: str
    pathPart: str

class CreateUsagePlanKeyRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    keyId: str
    keyType: str

class QuotaSettingsTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    offset: Optional[int] = None
    period: Optional[QuotaPeriodTypeType] = None

class CreateVpcLinkRequestRequestTypeDef(BaseValidatorModel):
    name: str
    targetArns: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteApiKeyRequestRequestTypeDef(BaseValidatorModel):
    apiKey: str

class DeleteAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    authorizerId: str

class DeleteBasePathMappingRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    basePath: str

class DeleteClientCertificateRequestRequestTypeDef(BaseValidatorModel):
    clientCertificateId: str

class DeleteDeploymentRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    deploymentId: str

class DeleteDocumentationPartRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationPartId: str

class DeleteDocumentationVersionRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationVersion: str

class DeleteDomainNameRequestRequestTypeDef(BaseValidatorModel):
    domainName: str

class DeleteGatewayResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType

class DeleteIntegrationRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str

class DeleteIntegrationResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class DeleteMethodRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str

class DeleteMethodResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class DeleteModelRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    modelName: str

class DeleteRequestValidatorRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str

class DeleteResourceRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str

class DeleteRestApiRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str

class DeleteStageRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str

class DeleteUsagePlanKeyRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    keyId: str

class DeleteUsagePlanRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str

class DeleteVpcLinkRequestRequestTypeDef(BaseValidatorModel):
    vpcLinkId: str

class MethodSnapshotTypeDef(BaseValidatorModel):
    authorizationType: Optional[str] = None
    apiKeyRequired: Optional[bool] = None

class DocumentationVersionTypeDef(BaseValidatorModel):
    version: Optional[str] = None
    createdDate: Optional[datetime] = None
    description: Optional[str] = None

class EndpointConfigurationOutputTypeDef(BaseValidatorModel):
    types: Optional[List[EndpointTypeType]] = None
    vpcEndpointIds: Optional[List[str]] = None

class MutualTlsAuthenticationTypeDef(BaseValidatorModel):
    truststoreUri: Optional[str] = None
    truststoreVersion: Optional[str] = None
    truststoreWarnings: Optional[List[str]] = None

class EndpointConfigurationExtraOutputTypeDef(BaseValidatorModel):
    types: Optional[List[EndpointTypeType]] = None
    vpcEndpointIds: Optional[List[str]] = None

class FlushStageAuthorizersCacheRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str

class FlushStageCacheRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str

class GatewayResponseTypeDef(BaseValidatorModel):
    responseType: Optional[GatewayResponseTypeType] = None
    statusCode: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None
    defaultResponse: Optional[bool] = None

class GenerateClientCertificateRequestRequestTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetApiKeyRequestRequestTypeDef(BaseValidatorModel):
    apiKey: str
    includeValue: Optional[bool] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetApiKeysRequestRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None
    nameQuery: Optional[str] = None
    customerId: Optional[str] = None
    includeValues: Optional[bool] = None

class GetAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    authorizerId: str

class GetAuthorizersRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetBasePathMappingRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    basePath: str

class GetBasePathMappingsRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetClientCertificateRequestRequestTypeDef(BaseValidatorModel):
    clientCertificateId: str

class GetClientCertificatesRequestRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class GetDeploymentRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    deploymentId: str
    embed: Optional[Sequence[str]] = None

class GetDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetDocumentationPartRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationPartId: str

class GetDocumentationPartsRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    type: Optional[DocumentationPartTypeType] = None
    nameQuery: Optional[str] = None
    path: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None
    locationStatus: Optional[LocationStatusTypeType] = None

class GetDocumentationVersionRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationVersion: str

class GetDocumentationVersionsRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetDomainNameRequestRequestTypeDef(BaseValidatorModel):
    domainName: str

class GetDomainNamesRequestRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class GetExportRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str
    exportType: str
    parameters: Optional[Mapping[str, str]] = None
    accepts: Optional[str] = None

class GetGatewayResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType

class GetGatewayResponsesRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetIntegrationRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str

class GetIntegrationResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class GetMethodRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str

class GetMethodResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str

class GetModelRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    modelName: str
    flatten: Optional[bool] = None

class GetModelTemplateRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    modelName: str

class GetModelsRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetRequestValidatorRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str

class GetRequestValidatorsRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetResourceRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    embed: Optional[Sequence[str]] = None

class GetResourcesRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None
    embed: Optional[Sequence[str]] = None

class GetRestApiRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str

class GetRestApisRequestRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class GetSdkRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str
    sdkType: str
    parameters: Optional[Mapping[str, str]] = None

class GetSdkTypeRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetSdkTypesRequestRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class GetStageRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str

class GetStagesRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    deploymentId: Optional[str] = None

class GetTagsRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    position: Optional[str] = None
    limit: Optional[int] = None

class GetUsagePlanKeyRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    keyId: str

class GetUsagePlanKeysRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    position: Optional[str] = None
    limit: Optional[int] = None
    nameQuery: Optional[str] = None

class GetUsagePlanRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str

class GetUsagePlansRequestRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    keyId: Optional[str] = None
    limit: Optional[int] = None

class GetUsageRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None

class GetVpcLinkRequestRequestTypeDef(BaseValidatorModel):
    vpcLinkId: str

class GetVpcLinksRequestRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None

class IntegrationResponseTypeDef(BaseValidatorModel):
    statusCode: Optional[str] = None
    selectionPattern: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None

class TlsConfigTypeDef(BaseValidatorModel):
    insecureSkipVerification: Optional[bool] = None

class MethodResponseTypeDef(BaseValidatorModel):
    statusCode: Optional[str] = None
    responseParameters: Optional[Dict[str, bool]] = None
    responseModels: Optional[Dict[str, str]] = None

class MethodSettingTypeDef(BaseValidatorModel):
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

class ModelTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    schema: Optional[str] = None
    contentType: Optional[str] = None

class PatchOperationTypeDef(BaseValidatorModel):
    op: Optional[OpType] = None
    path: Optional[str] = None
    value: Optional[str] = None
    _from: Optional[str] = None

class PutGatewayResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType
    statusCode: Optional[str] = None
    responseParameters: Optional[Mapping[str, str]] = None
    responseTemplates: Optional[Mapping[str, str]] = None

class PutIntegrationResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    selectionPattern: Optional[str] = None
    responseParameters: Optional[Mapping[str, str]] = None
    responseTemplates: Optional[Mapping[str, str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None

class PutMethodRequestRequestTypeDef(BaseValidatorModel):
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

class PutMethodResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    responseParameters: Optional[Mapping[str, bool]] = None
    responseModels: Optional[Mapping[str, str]] = None

class RequestValidatorTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    validateRequestBody: Optional[bool] = None
    validateRequestParameters: Optional[bool] = None

class SdkConfigurationPropertyTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    friendlyName: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    defaultValue: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TestInvokeAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    authorizerId: str
    headers: Optional[Mapping[str, str]] = None
    multiValueHeaders: Optional[Mapping[str, Sequence[str]]] = None
    pathWithQueryString: Optional[str] = None
    body: Optional[str] = None
    stageVariables: Optional[Mapping[str, str]] = None
    additionalContext: Optional[Mapping[str, str]] = None

class TestInvokeMethodRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    pathWithQueryString: Optional[str] = None
    body: Optional[str] = None
    headers: Optional[Mapping[str, str]] = None
    multiValueHeaders: Optional[Mapping[str, Sequence[str]]] = None
    clientCertificateId: Optional[str] = None
    stageVariables: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UsagePlanKeyTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    name: Optional[str] = None

class VpcLinkTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    targetArns: Optional[List[str]] = None
    status: Optional[VpcLinkStatusType] = None
    statusMessage: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ApiKeyIdsTypeDef(BaseValidatorModel):
    ids: List[str]
    warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ApiKeyResponseTypeDef(BaseValidatorModel):
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

class AuthorizerResponseTypeDef(BaseValidatorModel):
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

class BasePathMappingResponseTypeDef(BaseValidatorModel):
    basePath: str
    restApiId: str
    stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClientCertificateResponseTypeDef(BaseValidatorModel):
    clientCertificateId: str
    description: str
    pemEncodedCertificate: str
    createdDate: datetime
    expirationDate: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentationPartIdsTypeDef(BaseValidatorModel):
    ids: List[str]
    warnings: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentationVersionResponseTypeDef(BaseValidatorModel):
    version: str
    createdDate: datetime
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportResponseTypeDef(BaseValidatorModel):
    contentType: str
    contentDisposition: str
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayResponseResponseTypeDef(BaseValidatorModel):
    responseType: GatewayResponseTypeType
    statusCode: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    defaultResponse: bool
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationResponseResponseTypeDef(BaseValidatorModel):
    statusCode: str
    selectionPattern: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    contentHandling: ContentHandlingStrategyType
    ResponseMetadata: ResponseMetadataTypeDef

class MethodResponseResponseTypeDef(BaseValidatorModel):
    statusCode: str
    responseParameters: Dict[str, bool]
    responseModels: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ModelResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    description: str
    schema: str
    contentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class RequestValidatorResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    validateRequestBody: bool
    validateRequestParameters: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SdkResponseTypeDef(BaseValidatorModel):
    contentType: str
    contentDisposition: str
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class TagsTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TemplateTypeDef(BaseValidatorModel):
    value: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestInvokeAuthorizerResponseTypeDef(BaseValidatorModel):
    clientStatus: int
    log: str
    latency: int
    principalId: str
    policy: str
    authorization: Dict[str, List[str]]
    claims: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TestInvokeMethodResponseTypeDef(BaseValidatorModel):
    status: int
    body: str
    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    log: str
    latency: int
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlanKeyResponseTypeDef(BaseValidatorModel):
    id: str
    type: str
    value: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UsageTypeDef(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    position: str
    items: Dict[str, List[List[int]]]
    ResponseMetadata: ResponseMetadataTypeDef

class VpcLinkResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    description: str
    targetArns: List[str]
    status: VpcLinkStatusType
    statusMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class AccountTypeDef(BaseValidatorModel):
    cloudwatchRoleArn: str
    throttleSettings: ThrottleSettingsTypeDef
    features: List[str]
    apiKeyVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ApiStageExtraOutputTypeDef(BaseValidatorModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Dict[str, ThrottleSettingsTypeDef]] = None

class ApiStageOutputTypeDef(BaseValidatorModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Dict[str, ThrottleSettingsTypeDef]] = None

class ApiStageTypeDef(BaseValidatorModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Mapping[str, ThrottleSettingsTypeDef]] = None

class ApiKeysTypeDef(BaseValidatorModel):
    warnings: List[str]
    position: str
    items: List[ApiKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizersTypeDef(BaseValidatorModel):
    position: str
    items: List[AuthorizerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BasePathMappingsTypeDef(BaseValidatorModel):
    position: str
    items: List[BasePathMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportApiKeysRequestRequestTypeDef(BaseValidatorModel):
    body: BlobTypeDef
    format: Literal["csv"]
    failOnWarnings: Optional[bool] = None

class ImportDocumentationPartsRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    body: BlobTypeDef
    mode: Optional[PutModeType] = None
    failOnWarnings: Optional[bool] = None

class ImportRestApiRequestRequestTypeDef(BaseValidatorModel):
    body: BlobTypeDef
    failOnWarnings: Optional[bool] = None
    parameters: Optional[Mapping[str, str]] = None

class PutRestApiRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    body: BlobTypeDef
    mode: Optional[PutModeType] = None
    failOnWarnings: Optional[bool] = None
    parameters: Optional[Mapping[str, str]] = None

class CreateStageRequestRequestTypeDef(BaseValidatorModel):
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

class ClientCertificatesTypeDef(BaseValidatorModel):
    position: str
    items: List[ClientCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiKeyRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    enabled: Optional[bool] = None
    generateDistinctId: Optional[bool] = None
    value: Optional[str] = None
    stageKeys: Optional[Sequence[StageKeyTypeDef]] = None
    customerId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateDeploymentRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: Optional[str] = None
    stageDescription: Optional[str] = None
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    variables: Optional[Mapping[str, str]] = None
    canarySettings: Optional[DeploymentCanarySettingsTypeDef] = None
    tracingEnabled: Optional[bool] = None

class CreateDocumentationPartRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    location: DocumentationPartLocationTypeDef
    properties: str

class DocumentationPartResponseTypeDef(BaseValidatorModel):
    id: str
    location: DocumentationPartLocationTypeDef
    properties: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentationPartTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    location: Optional[DocumentationPartLocationTypeDef] = None
    properties: Optional[str] = None

class CreateRestApiRequestRequestTypeDef(BaseValidatorModel):
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

class CreateDomainNameRequestRequestTypeDef(BaseValidatorModel):
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

class DeploymentResponseTypeDef(BaseValidatorModel):
    id: str
    description: str
    createdDate: datetime
    apiSummary: Dict[str, Dict[str, MethodSnapshotTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[datetime] = None
    apiSummary: Optional[Dict[str, Dict[str, MethodSnapshotTypeDef]]] = None

class DocumentationVersionsTypeDef(BaseValidatorModel):
    position: str
    items: List[DocumentationVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestApiResponseTypeDef(BaseValidatorModel):
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

class RestApiTypeDef(BaseValidatorModel):
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

class DomainNameResponseTypeDef(BaseValidatorModel):
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

class DomainNameTypeDef(BaseValidatorModel):
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

class GatewayResponsesTypeDef(BaseValidatorModel):
    position: str
    items: List[GatewayResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiKeysRequestGetApiKeysPaginateTypeDef(BaseValidatorModel):
    nameQuery: Optional[str] = None
    customerId: Optional[str] = None
    includeValues: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAuthorizersRequestGetAuthorizersPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBasePathMappingsRequestGetBasePathMappingsPaginateTypeDef(BaseValidatorModel):
    domainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetClientCertificatesRequestGetClientCertificatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDeploymentsRequestGetDeploymentsPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDocumentationPartsRequestGetDocumentationPartsPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    type: Optional[DocumentationPartTypeType] = None
    nameQuery: Optional[str] = None
    path: Optional[str] = None
    locationStatus: Optional[LocationStatusTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDocumentationVersionsRequestGetDocumentationVersionsPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDomainNamesRequestGetDomainNamesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetGatewayResponsesRequestGetGatewayResponsesPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetModelsRequestGetModelsPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRequestValidatorsRequestGetRequestValidatorsPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourcesRequestGetResourcesPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    embed: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRestApisRequestGetRestApisPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSdkTypesRequestGetSdkTypesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUsagePlanKeysRequestGetUsagePlanKeysPaginateTypeDef(BaseValidatorModel):
    usagePlanId: str
    nameQuery: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUsagePlansRequestGetUsagePlansPaginateTypeDef(BaseValidatorModel):
    keyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUsageRequestGetUsagePaginateTypeDef(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetVpcLinksRequestGetVpcLinksPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class IntegrationExtraResponseTypeDef(BaseValidatorModel):
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

class IntegrationTypeDef(BaseValidatorModel):
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

class PutIntegrationRequestRequestTypeDef(BaseValidatorModel):
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

class StageResponseTypeDef(BaseValidatorModel):
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

class StageTypeDef(BaseValidatorModel):
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

class ModelsTypeDef(BaseValidatorModel):
    position: str
    items: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountRequestRequestTypeDef(BaseValidatorModel):
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateApiKeyRequestRequestTypeDef(BaseValidatorModel):
    apiKey: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    authorizerId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateBasePathMappingRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    basePath: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateClientCertificateRequestRequestTypeDef(BaseValidatorModel):
    clientCertificateId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateDeploymentRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    deploymentId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateDocumentationPartRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationPartId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateDocumentationVersionRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationVersion: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateDomainNameRequestRequestTypeDef(BaseValidatorModel):
    domainName: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateGatewayResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateIntegrationRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateIntegrationResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateMethodRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateMethodResponseRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateModelRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    modelName: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateRequestValidatorRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateResourceRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateRestApiRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateStageRequestRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateUsagePlanRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateUsageRequestRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    keyId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class UpdateVpcLinkRequestRequestTypeDef(BaseValidatorModel):
    vpcLinkId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None

class RequestValidatorsTypeDef(BaseValidatorModel):
    position: str
    items: List[RequestValidatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SdkTypeResponseTypeDef(BaseValidatorModel):
    id: str
    friendlyName: str
    description: str
    configurationProperties: List[SdkConfigurationPropertyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SdkTypeTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    friendlyName: Optional[str] = None
    description: Optional[str] = None
    configurationProperties: Optional[List[SdkConfigurationPropertyTypeDef]] = None

class UsagePlanKeysTypeDef(BaseValidatorModel):
    position: str
    items: List[UsagePlanKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VpcLinksTypeDef(BaseValidatorModel):
    position: str
    items: List[VpcLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlanResponseTypeDef(BaseValidatorModel):
    id: str
    name: str
    description: str
    apiStages: List[ApiStageOutputTypeDef]
    throttle: ThrottleSettingsTypeDef
    quota: QuotaSettingsTypeDef
    productCode: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlanTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    apiStages: Optional[List[ApiStageOutputTypeDef]] = None
    throttle: Optional[ThrottleSettingsTypeDef] = None
    quota: Optional[QuotaSettingsTypeDef] = None
    productCode: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class DocumentationPartsTypeDef(BaseValidatorModel):
    position: str
    items: List[DocumentationPartTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentsTypeDef(BaseValidatorModel):
    position: str
    items: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestApisTypeDef(BaseValidatorModel):
    position: str
    items: List[RestApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNamesTypeDef(BaseValidatorModel):
    position: str
    items: List[DomainNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MethodExtraResponseTypeDef(BaseValidatorModel):
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

class MethodTypeDef(BaseValidatorModel):
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

class StagesTypeDef(BaseValidatorModel):
    item: List[StageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SdkTypesTypeDef(BaseValidatorModel):
    position: str
    items: List[SdkTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UsagePlansTypeDef(BaseValidatorModel):
    position: str
    items: List[UsagePlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsagePlanRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    apiStages: Optional[Sequence[ApiStageUnionTypeDef]] = None
    throttle: Optional[ThrottleSettingsTypeDef] = None
    quota: Optional[QuotaSettingsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class ResourceResponseTypeDef(BaseValidatorModel):
    id: str
    parentId: str
    pathPart: str
    path: str
    resourceMethods: Dict[str, MethodTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    parentId: Optional[str] = None
    pathPart: Optional[str] = None
    path: Optional[str] = None
    resourceMethods: Optional[Dict[str, MethodTypeDef]] = None

class ResourcesTypeDef(BaseValidatorModel):
    position: str
    items: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

