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
from aws_resource_validator.pydantic_models.apigateway_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ThrottleSettingsTypeDef(BaseValidatorModel):
    burstLimit: Optional[int] = None
    rateLimit: Optional[float] = None


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


class CreateBasePathMappingRequestTypeDef(BaseValidatorModel):
    domainName: str
    restApiId: str
    domainNameId: Optional[str] = None
    basePath: Optional[str] = None
    stage: Optional[str] = None


class DeploymentCanarySettingsTypeDef(BaseValidatorModel):
    percentTraffic: Optional[float] = None
    stageVariableOverrides: Optional[Mapping[str, str]] = None
    useStageCache: Optional[bool] = None


class CreateDocumentationVersionRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationVersion: str
    stageName: Optional[str] = None
    description: Optional[str] = None


class CreateDomainNameAccessAssociationRequestTypeDef(BaseValidatorModel):
    domainNameArn: str
    accessAssociationSourceType: Literal["VPCE"]
    accessAssociationSource: str
    tags: Optional[Mapping[str, str]] = None


class MutualTlsAuthenticationInputTypeDef(BaseValidatorModel):
    truststoreUri: Optional[str] = None
    truststoreVersion: Optional[str] = None


class CreateModelRequestTypeDef(BaseValidatorModel):
    restApiId: str
    name: str
    contentType: str
    description: Optional[str] = None
    schema: Optional[str] = None


class CreateRequestValidatorRequestTypeDef(BaseValidatorModel):
    restApiId: str
    name: Optional[str] = None
    validateRequestBody: Optional[bool] = None
    validateRequestParameters: Optional[bool] = None


class CreateResourceRequestTypeDef(BaseValidatorModel):
    restApiId: str
    parentId: str
    pathPart: str


class CreateUsagePlanKeyRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    keyId: str
    keyType: str


class QuotaSettingsTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    offset: Optional[int] = None
    period: Optional[QuotaPeriodTypeType] = None


class CreateVpcLinkRequestTypeDef(BaseValidatorModel):
    name: str
    targetArns: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteApiKeyRequestTypeDef(BaseValidatorModel):
    apiKey: str


class DeleteAuthorizerRequestTypeDef(BaseValidatorModel):
    restApiId: str
    authorizerId: str


class DeleteBasePathMappingRequestTypeDef(BaseValidatorModel):
    domainName: str
    basePath: str
    domainNameId: Optional[str] = None


class DeleteClientCertificateRequestTypeDef(BaseValidatorModel):
    clientCertificateId: str


class DeleteDeploymentRequestTypeDef(BaseValidatorModel):
    restApiId: str
    deploymentId: str


class DeleteDocumentationPartRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationPartId: str


class DeleteDocumentationVersionRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationVersion: str


class DeleteDomainNameAccessAssociationRequestTypeDef(BaseValidatorModel):
    domainNameAccessAssociationArn: str


class DeleteDomainNameRequestTypeDef(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None


class DeleteGatewayResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType


class DeleteIntegrationRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str


class DeleteIntegrationResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str


class DeleteMethodRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str


class DeleteMethodResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str


class DeleteModelRequestTypeDef(BaseValidatorModel):
    restApiId: str
    modelName: str


class DeleteRequestValidatorRequestTypeDef(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str


class DeleteResourceRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str


class DeleteRestApiRequestTypeDef(BaseValidatorModel):
    restApiId: str


class DeleteStageRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str


class DeleteUsagePlanKeyRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    keyId: str


class DeleteUsagePlanRequestTypeDef(BaseValidatorModel):
    usagePlanId: str


class DeleteVpcLinkRequestTypeDef(BaseValidatorModel):
    vpcLinkId: str


class MethodSnapshotTypeDef(BaseValidatorModel):
    authorizationType: Optional[str] = None
    apiKeyRequired: Optional[bool] = None


class DocumentationVersionTypeDef(BaseValidatorModel):
    version: Optional[str] = None
    createdDate: Optional[datetime] = None
    description: Optional[str] = None


class DomainNameAccessAssociationTypeDef(BaseValidatorModel):
    domainNameAccessAssociationArn: Optional[str] = None
    domainNameArn: Optional[str] = None
    accessAssociationSourceType: Optional[Literal["VPCE"]] = None
    accessAssociationSource: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class MutualTlsAuthenticationTypeDef(BaseValidatorModel):
    truststoreUri: Optional[str] = None
    truststoreVersion: Optional[str] = None
    truststoreWarnings: Optional[List[str]] = None


class FlushStageAuthorizersCacheRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str


class FlushStageCacheRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str


class GatewayResponseTypeDef(BaseValidatorModel):
    responseType: Optional[GatewayResponseTypeType] = None
    statusCode: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None
    defaultResponse: Optional[bool] = None


class GenerateClientCertificateRequestTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class GetApiKeyRequestTypeDef(BaseValidatorModel):
    apiKey: str
    includeValue: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetApiKeysRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None
    nameQuery: Optional[str] = None
    customerId: Optional[str] = None
    includeValues: Optional[bool] = None


class GetAuthorizerRequestTypeDef(BaseValidatorModel):
    restApiId: str
    authorizerId: str


class GetAuthorizersRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


class GetBasePathMappingRequestTypeDef(BaseValidatorModel):
    domainName: str
    basePath: str
    domainNameId: Optional[str] = None


class GetBasePathMappingsRequestTypeDef(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None


class GetClientCertificateRequestTypeDef(BaseValidatorModel):
    clientCertificateId: str


class GetClientCertificatesRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None


class GetDeploymentRequestTypeDef(BaseValidatorModel):
    restApiId: str
    deploymentId: str
    embed: Optional[Sequence[str]] = None


class GetDeploymentsRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


class GetDocumentationPartRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationPartId: str


class GetDocumentationVersionRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationVersion: str


class GetDocumentationVersionsRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


class GetDomainNameAccessAssociationsRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None
    resourceOwner: Optional[ResourceOwnerType] = None


class GetDomainNameRequestTypeDef(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None


class GetDomainNamesRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None
    resourceOwner: Optional[ResourceOwnerType] = None


class GetExportRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str
    exportType: str
    parameters: Optional[Mapping[str, str]] = None
    accepts: Optional[str] = None


class GetGatewayResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType


class GetGatewayResponsesRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


class GetIntegrationRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str


class GetIntegrationResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str


class GetMethodRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str


class GetMethodResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str


class GetModelRequestTypeDef(BaseValidatorModel):
    restApiId: str
    modelName: str
    flatten: Optional[bool] = None


class GetModelTemplateRequestTypeDef(BaseValidatorModel):
    restApiId: str
    modelName: str


class GetModelsRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


class GetRequestValidatorRequestTypeDef(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str


class GetRequestValidatorsRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


class GetResourceRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    embed: Optional[Sequence[str]] = None


class GetResourcesRequestTypeDef(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None
    embed: Optional[Sequence[str]] = None


class GetRestApiRequestTypeDef(BaseValidatorModel):
    restApiId: str


class GetRestApisRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None


class GetSdkRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str
    sdkType: str
    parameters: Optional[Mapping[str, str]] = None


class GetSdkTypesRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None


class GetStageRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str


class GetStagesRequestTypeDef(BaseValidatorModel):
    restApiId: str
    deploymentId: Optional[str] = None


class GetTagsRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    position: Optional[str] = None
    limit: Optional[int] = None


class GetUsagePlanKeyRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    keyId: str


class GetUsagePlanKeysRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    position: Optional[str] = None
    limit: Optional[int] = None
    nameQuery: Optional[str] = None


class GetUsagePlanRequestTypeDef(BaseValidatorModel):
    usagePlanId: str


class GetUsagePlansRequestTypeDef(BaseValidatorModel):
    position: Optional[str] = None
    keyId: Optional[str] = None
    limit: Optional[int] = None


class GetUsageRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None


class GetVpcLinkRequestTypeDef(BaseValidatorModel):
    vpcLinkId: str


class GetVpcLinksRequestTypeDef(BaseValidatorModel):
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
    unauthorizedCacheControlHeaderStrategy: Optional[UnauthorizedCacheControlHeaderStrategyType] = None


class PutGatewayResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType
    statusCode: Optional[str] = None
    responseParameters: Optional[Mapping[str, str]] = None
    responseTemplates: Optional[Mapping[str, str]] = None


class PutIntegrationResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    selectionPattern: Optional[str] = None
    responseParameters: Optional[Mapping[str, str]] = None
    responseTemplates: Optional[Mapping[str, str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None


class PutMethodRequestTypeDef(BaseValidatorModel):
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


class PutMethodResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    responseParameters: Optional[Mapping[str, bool]] = None
    responseModels: Optional[Mapping[str, str]] = None


class RejectDomainNameAccessAssociationRequestTypeDef(BaseValidatorModel):
    domainNameAccessAssociationArn: str
    domainNameArn: str


class SdkConfigurationPropertyTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    friendlyName: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    defaultValue: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TestInvokeAuthorizerRequestTypeDef(BaseValidatorModel):
    restApiId: str
    authorizerId: str
    headers: Optional[Mapping[str, str]] = None
    multiValueHeaders: Optional[Mapping[str, Sequence[str]]] = None
    pathWithQueryString: Optional[str] = None
    body: Optional[str] = None
    stageVariables: Optional[Mapping[str, str]] = None
    additionalContext: Optional[Mapping[str, str]] = None


class TestInvokeMethodRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    pathWithQueryString: Optional[str] = None
    body: Optional[str] = None
    headers: Optional[Mapping[str, str]] = None
    multiValueHeaders: Optional[Mapping[str, Sequence[str]]] = None
    clientCertificateId: Optional[str] = None
    stageVariables: Optional[Mapping[str, str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ApiKeyIdsTypeDef(BaseValidatorModel):
    ids: List[str]
    warnings: List[str]
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


class DomainNameAccessAssociationResponseTypeDef(BaseValidatorModel):
    domainNameAccessAssociationArn: str
    domainNameArn: str
    accessAssociationSourceType: Literal["VPCE"]
    accessAssociationSource: str
    tags: Dict[str, str]
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


class UsageTypeDef(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    position: str
    items: Dict[str, List[List[int]]]
    ResponseMetadata: ResponseMetadataTypeDef


class AccountTypeDef(BaseValidatorModel):
    cloudwatchRoleArn: str
    throttleSettings: ThrottleSettingsTypeDef
    features: List[str]
    apiKeyVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class ApiStageOutputTypeDef(BaseValidatorModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Dict[str, ThrottleSettingsTypeDef]] = None


class ApiStageTypeDef(BaseValidatorModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Mapping[str, ThrottleSettingsTypeDef]] = None


class ApiKeyTypeDef(BaseValidatorModel):
    pass


class ApiKeysTypeDef(BaseValidatorModel):
    warnings: List[str]
    position: str
    items: List[ApiKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AuthorizerTypeDef(BaseValidatorModel):
    pass


class AuthorizersTypeDef(BaseValidatorModel):
    position: str
    items: List[AuthorizerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BasePathMappingsTypeDef(BaseValidatorModel):
    position: str
    items: List[BasePathMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class ImportDocumentationPartsRequestTypeDef(BaseValidatorModel):
    restApiId: str
    body: BlobTypeDef
    mode: Optional[PutModeType] = None
    failOnWarnings: Optional[bool] = None


class ImportRestApiRequestTypeDef(BaseValidatorModel):
    body: BlobTypeDef
    failOnWarnings: Optional[bool] = None
    parameters: Optional[Mapping[str, str]] = None


class PutRestApiRequestTypeDef(BaseValidatorModel):
    restApiId: str
    body: BlobTypeDef
    mode: Optional[PutModeType] = None
    failOnWarnings: Optional[bool] = None
    parameters: Optional[Mapping[str, str]] = None


class ClientCertificatesTypeDef(BaseValidatorModel):
    position: str
    items: List[ClientCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateApiKeyRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    enabled: Optional[bool] = None
    generateDistinctId: Optional[bool] = None
    value: Optional[str] = None
    stageKeys: Optional[Sequence[StageKeyTypeDef]] = None
    customerId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateDeploymentRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: Optional[str] = None
    stageDescription: Optional[str] = None
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    variables: Optional[Mapping[str, str]] = None
    canarySettings: Optional[DeploymentCanarySettingsTypeDef] = None
    tracingEnabled: Optional[bool] = None


class DocumentationPartLocationTypeDef(BaseValidatorModel):
    pass


class CreateDocumentationPartRequestTypeDef(BaseValidatorModel):
    restApiId: str
    location: DocumentationPartLocationTypeDef
    properties: str


class DocumentationVersionsTypeDef(BaseValidatorModel):
    position: str
    items: List[DocumentationVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DomainNameAccessAssociationsTypeDef(BaseValidatorModel):
    position: str
    items: List[DomainNameAccessAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class DomainNameResponseTypeDef(BaseValidatorModel):
    domainName: str
    domainNameId: str
    domainNameArn: str
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
    managementPolicy: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class DomainNameTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None
    domainNameId: Optional[str] = None
    domainNameArn: Optional[str] = None
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
    managementPolicy: Optional[str] = None
    policy: Optional[str] = None


class GatewayResponsesTypeDef(BaseValidatorModel):
    position: str
    items: List[GatewayResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetApiKeysRequestPaginateTypeDef(BaseValidatorModel):
    nameQuery: Optional[str] = None
    customerId: Optional[str] = None
    includeValues: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetAuthorizersRequestPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetBasePathMappingsRequestPaginateTypeDef(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetClientCertificatesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDeploymentsRequestPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDocumentationVersionsRequestPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDomainNamesRequestPaginateTypeDef(BaseValidatorModel):
    resourceOwner: Optional[ResourceOwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetGatewayResponsesRequestPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetModelsRequestPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRequestValidatorsRequestPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourcesRequestPaginateTypeDef(BaseValidatorModel):
    restApiId: str
    embed: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRestApisRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetSdkTypesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetUsagePlanKeysRequestPaginateTypeDef(BaseValidatorModel):
    usagePlanId: str
    nameQuery: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetUsagePlansRequestPaginateTypeDef(BaseValidatorModel):
    keyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetUsageRequestPaginateTypeDef(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetVpcLinksRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class AccessLogSettingsTypeDef(BaseValidatorModel):
    pass


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


class ModelTypeDef(BaseValidatorModel):
    pass


class ModelsTypeDef(BaseValidatorModel):
    position: str
    items: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PatchOperationTypeDef(BaseValidatorModel):
    pass


class UpdateAccountRequestTypeDef(BaseValidatorModel):
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateApiKeyRequestTypeDef(BaseValidatorModel):
    apiKey: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateAuthorizerRequestTypeDef(BaseValidatorModel):
    restApiId: str
    authorizerId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateBasePathMappingRequestTypeDef(BaseValidatorModel):
    domainName: str
    basePath: str
    domainNameId: Optional[str] = None
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateClientCertificateRequestTypeDef(BaseValidatorModel):
    clientCertificateId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateDeploymentRequestTypeDef(BaseValidatorModel):
    restApiId: str
    deploymentId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateDocumentationPartRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationPartId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateDocumentationVersionRequestTypeDef(BaseValidatorModel):
    restApiId: str
    documentationVersion: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateDomainNameRequestTypeDef(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateGatewayResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateIntegrationRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateIntegrationResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateMethodRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateMethodResponseRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateModelRequestTypeDef(BaseValidatorModel):
    restApiId: str
    modelName: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateRequestValidatorRequestTypeDef(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateResourceRequestTypeDef(BaseValidatorModel):
    restApiId: str
    resourceId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateRestApiRequestTypeDef(BaseValidatorModel):
    restApiId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateStageRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateUsagePlanRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateUsageRequestTypeDef(BaseValidatorModel):
    usagePlanId: str
    keyId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class UpdateVpcLinkRequestTypeDef(BaseValidatorModel):
    vpcLinkId: str
    patchOperations: Optional[Sequence[PatchOperationTypeDef]] = None


class RequestValidatorTypeDef(BaseValidatorModel):
    pass


class RequestValidatorsTypeDef(BaseValidatorModel):
    position: str
    items: List[RequestValidatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UsagePlanKeyTypeDef(BaseValidatorModel):
    pass


class UsagePlanKeysTypeDef(BaseValidatorModel):
    position: str
    items: List[UsagePlanKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class VpcLinkTypeDef(BaseValidatorModel):
    pass


class VpcLinksTypeDef(BaseValidatorModel):
    position: str
    items: List[VpcLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CanarySettingsUnionTypeDef(BaseValidatorModel):
    pass


class CreateStageRequestTypeDef(BaseValidatorModel):
    restApiId: str
    stageName: str
    deploymentId: str
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    variables: Optional[Mapping[str, str]] = None
    documentationVersion: Optional[str] = None
    canarySettings: Optional[CanarySettingsUnionTypeDef] = None
    tracingEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class DocumentationPartTypeDef(BaseValidatorModel):
    pass


class DocumentationPartsTypeDef(BaseValidatorModel):
    position: str
    items: List[DocumentationPartTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeploymentTypeDef(BaseValidatorModel):
    pass


class DeploymentsTypeDef(BaseValidatorModel):
    position: str
    items: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RestApiTypeDef(BaseValidatorModel):
    pass


class RestApisTypeDef(BaseValidatorModel):
    position: str
    items: List[RestApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DomainNamesTypeDef(BaseValidatorModel):
    position: str
    items: List[DomainNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDomainNameRequestTypeDef(BaseValidatorModel):
    domainName: str
    certificateName: Optional[str] = None
    certificateBody: Optional[str] = None
    certificatePrivateKey: Optional[str] = None
    certificateChain: Optional[str] = None
    certificateArn: Optional[str] = None
    regionalCertificateName: Optional[str] = None
    regionalCertificateArn: Optional[str] = None
    endpointConfiguration: Optional[EndpointConfigurationUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    securityPolicy: Optional[SecurityPolicyType] = None
    mutualTlsAuthentication: Optional[MutualTlsAuthenticationInputTypeDef] = None
    ownershipVerificationCertificateArn: Optional[str] = None
    policy: Optional[str] = None


class CreateRestApiRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    version: Optional[str] = None
    cloneFrom: Optional[str] = None
    binaryMediaTypes: Optional[Sequence[str]] = None
    minimumCompressionSize: Optional[int] = None
    apiKeySource: Optional[ApiKeySourceTypeType] = None
    endpointConfiguration: Optional[EndpointConfigurationUnionTypeDef] = None
    policy: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    disableExecuteApiEndpoint: Optional[bool] = None


class IntegrationTypeDef(BaseValidatorModel):
    pass


class MethodResponseExtraTypeDef(BaseValidatorModel):
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


class SdkTypeTypeDef(BaseValidatorModel):
    pass


class SdkTypesTypeDef(BaseValidatorModel):
    position: str
    items: List[SdkTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UsagePlanTypeDef(BaseValidatorModel):
    pass


class UsagePlansTypeDef(BaseValidatorModel):
    position: str
    items: List[UsagePlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ApiStageUnionTypeDef(BaseValidatorModel):
    pass


class CreateUsagePlanRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    apiStages: Optional[Sequence[ApiStageUnionTypeDef]] = None
    throttle: Optional[ThrottleSettingsTypeDef] = None
    quota: Optional[QuotaSettingsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class ResourceTypeDef(BaseValidatorModel):
    pass


class ResourcesTypeDef(BaseValidatorModel):
    position: str
    items: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


