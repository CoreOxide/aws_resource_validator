from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.apigateway.apigateway_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessLogSettings(BaseValidatorModel):
    format: Optional[str] = None
    destinationArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ThrottleSettings(BaseValidatorModel):
    burstLimit: Optional[int] = None
    rateLimit: Optional[float] = None


class ApiKey(BaseValidatorModel):
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


class Authorizer(BaseValidatorModel):
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


class BasePathMapping(BaseValidatorModel):
    basePath: Optional[str] = None
    restApiId: Optional[str] = None
    stage: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CanarySettingsOutput(BaseValidatorModel):
    percentTraffic: Optional[float] = None
    deploymentId: Optional[str] = None
    stageVariableOverrides: Optional[Dict[str, str]] = None
    useStageCache: Optional[bool] = None


class CanarySettings(BaseValidatorModel):
    percentTraffic: Optional[float] = None
    deploymentId: Optional[str] = None
    stageVariableOverrides: Optional[Dict[str, str]] = None
    useStageCache: Optional[bool] = None


class ClientCertificate(BaseValidatorModel):
    clientCertificateId: Optional[str] = None
    description: Optional[str] = None
    pemEncodedCertificate: Optional[str] = None
    createdDate: Optional[datetime] = None
    expirationDate: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class StageKey(BaseValidatorModel):
    restApiId: Optional[str] = None
    stageName: Optional[str] = None


# This class is the input for the 'create_authorizer' function.
class CreateAuthorizerRequest(BaseValidatorModel):
    restApiId: str
    name: str
    type: AuthorizerTypeType
    providerARNs: Optional[List[str]] = None
    authType: Optional[str] = None
    authorizerUri: Optional[str] = None
    authorizerCredentials: Optional[str] = None
    identitySource: Optional[str] = None
    identityValidationExpression: Optional[str] = None
    authorizerResultTtlInSeconds: Optional[int] = None


# This class is the input for the 'create_base_path_mapping' function.
class CreateBasePathMappingRequest(BaseValidatorModel):
    domainName: str
    restApiId: str
    domainNameId: Optional[str] = None
    basePath: Optional[str] = None
    stage: Optional[str] = None


class DeploymentCanarySettings(BaseValidatorModel):
    percentTraffic: Optional[float] = None
    stageVariableOverrides: Optional[Dict[str, str]] = None
    useStageCache: Optional[bool] = None


class DocumentationPartLocation(BaseValidatorModel):
    type: DocumentationPartTypeType
    path: Optional[str] = None
    method: Optional[str] = None
    statusCode: Optional[str] = None
    name: Optional[str] = None


# This class is the input for the 'create_documentation_version' function.
class CreateDocumentationVersionRequest(BaseValidatorModel):
    restApiId: str
    documentationVersion: str
    stageName: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'create_domain_name_access_association' function.
class CreateDomainNameAccessAssociationRequest(BaseValidatorModel):
    domainNameArn: str
    accessAssociationSourceType: Literal['VPCE']
    accessAssociationSource: str
    tags: Optional[Dict[str, str]] = None


class MutualTlsAuthenticationInput(BaseValidatorModel):
    truststoreUri: Optional[str] = None
    truststoreVersion: Optional[str] = None


# This class is the input for the 'create_model' function.
class CreateModelRequest(BaseValidatorModel):
    restApiId: str
    name: str
    contentType: str
    description: Optional[str] = None
    schema: Optional[str] = None


# This class is the input for the 'create_request_validator' function.
class CreateRequestValidatorRequest(BaseValidatorModel):
    restApiId: str
    name: Optional[str] = None
    validateRequestBody: Optional[bool] = None
    validateRequestParameters: Optional[bool] = None


# This class is the input for the 'create_resource' function.
class CreateResourceRequest(BaseValidatorModel):
    restApiId: str
    parentId: str
    pathPart: str


# This class is the input for the 'create_usage_plan_key' function.
class CreateUsagePlanKeyRequest(BaseValidatorModel):
    usagePlanId: str
    keyId: str
    keyType: str


class QuotaSettings(BaseValidatorModel):
    limit: Optional[int] = None
    offset: Optional[int] = None
    period: Optional[QuotaPeriodTypeType] = None


# This class is the input for the 'create_vpc_link' function.
class CreateVpcLinkRequest(BaseValidatorModel):
    name: str
    targetArns: List[str]
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'delete_api_key' function.
class DeleteApiKeyRequest(BaseValidatorModel):
    apiKey: str


# This class is the input for the 'delete_authorizer' function.
class DeleteAuthorizerRequest(BaseValidatorModel):
    restApiId: str
    authorizerId: str


# This class is the input for the 'delete_base_path_mapping' function.
class DeleteBasePathMappingRequest(BaseValidatorModel):
    domainName: str
    basePath: str
    domainNameId: Optional[str] = None


# This class is the input for the 'delete_client_certificate' function.
class DeleteClientCertificateRequest(BaseValidatorModel):
    clientCertificateId: str


# This class is the input for the 'delete_deployment' function.
class DeleteDeploymentRequest(BaseValidatorModel):
    restApiId: str
    deploymentId: str


# This class is the input for the 'delete_documentation_part' function.
class DeleteDocumentationPartRequest(BaseValidatorModel):
    restApiId: str
    documentationPartId: str


# This class is the input for the 'delete_documentation_version' function.
class DeleteDocumentationVersionRequest(BaseValidatorModel):
    restApiId: str
    documentationVersion: str


# This class is the input for the 'delete_domain_name_access_association' function.
class DeleteDomainNameAccessAssociationRequest(BaseValidatorModel):
    domainNameAccessAssociationArn: str


# This class is the input for the 'delete_domain_name' function.
class DeleteDomainNameRequest(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None


# This class is the input for the 'delete_gateway_response' function.
class DeleteGatewayResponseRequest(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType


# This class is the input for the 'delete_integration' function.
class DeleteIntegrationRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str


# This class is the input for the 'delete_integration_response' function.
class DeleteIntegrationResponseRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str


# This class is the input for the 'delete_method' function.
class DeleteMethodRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str


# This class is the input for the 'delete_method_response' function.
class DeleteMethodResponseRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str


# This class is the input for the 'delete_model' function.
class DeleteModelRequest(BaseValidatorModel):
    restApiId: str
    modelName: str


# This class is the input for the 'delete_request_validator' function.
class DeleteRequestValidatorRequest(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str


# This class is the input for the 'delete_resource' function.
class DeleteResourceRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str


# This class is the input for the 'delete_rest_api' function.
class DeleteRestApiRequest(BaseValidatorModel):
    restApiId: str


# This class is the input for the 'delete_stage' function.
class DeleteStageRequest(BaseValidatorModel):
    restApiId: str
    stageName: str


# This class is the input for the 'delete_usage_plan_key' function.
class DeleteUsagePlanKeyRequest(BaseValidatorModel):
    usagePlanId: str
    keyId: str


# This class is the input for the 'delete_usage_plan' function.
class DeleteUsagePlanRequest(BaseValidatorModel):
    usagePlanId: str


# This class is the input for the 'delete_vpc_link' function.
class DeleteVpcLinkRequest(BaseValidatorModel):
    vpcLinkId: str


class MethodSnapshot(BaseValidatorModel):
    authorizationType: Optional[str] = None
    apiKeyRequired: Optional[bool] = None


class DocumentationVersion(BaseValidatorModel):
    version: Optional[str] = None
    createdDate: Optional[datetime] = None
    description: Optional[str] = None


class DomainNameAccessAssociation(BaseValidatorModel):
    domainNameAccessAssociationArn: Optional[str] = None
    domainNameArn: Optional[str] = None
    accessAssociationSourceType: Optional[Literal['VPCE']] = None
    accessAssociationSource: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class EndpointConfigurationOutput(BaseValidatorModel):
    types: Optional[List[EndpointTypeType]] = None
    vpcEndpointIds: Optional[List[str]] = None


class MutualTlsAuthentication(BaseValidatorModel):
    truststoreUri: Optional[str] = None
    truststoreVersion: Optional[str] = None
    truststoreWarnings: Optional[List[str]] = None


class EndpointConfiguration(BaseValidatorModel):
    types: Optional[List[EndpointTypeType]] = None
    vpcEndpointIds: Optional[List[str]] = None


# This class is the input for the 'flush_stage_authorizers_cache' function.
class FlushStageAuthorizersCacheRequest(BaseValidatorModel):
    restApiId: str
    stageName: str


# This class is the input for the 'flush_stage_cache' function.
class FlushStageCacheRequest(BaseValidatorModel):
    restApiId: str
    stageName: str


class GatewayResponse(BaseValidatorModel):
    responseType: Optional[GatewayResponseTypeType] = None
    statusCode: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None
    defaultResponse: Optional[bool] = None


# This class is the input for the 'generate_client_certificate' function.
class GenerateClientCertificateRequest(BaseValidatorModel):
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'get_api_key' function.
class GetApiKeyRequest(BaseValidatorModel):
    apiKey: str
    includeValue: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_api_keys' function.
class GetApiKeysRequest(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None
    nameQuery: Optional[str] = None
    customerId: Optional[str] = None
    includeValues: Optional[bool] = None


# This class is the input for the 'get_authorizer' function.
class GetAuthorizerRequest(BaseValidatorModel):
    restApiId: str
    authorizerId: str


# This class is the input for the 'get_authorizers' function.
class GetAuthorizersRequest(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_base_path_mapping' function.
class GetBasePathMappingRequest(BaseValidatorModel):
    domainName: str
    basePath: str
    domainNameId: Optional[str] = None


# This class is the input for the 'get_base_path_mappings' function.
class GetBasePathMappingsRequest(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_client_certificate' function.
class GetClientCertificateRequest(BaseValidatorModel):
    clientCertificateId: str


# This class is the input for the 'get_client_certificates' function.
class GetClientCertificatesRequest(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_deployment' function.
class GetDeploymentRequest(BaseValidatorModel):
    restApiId: str
    deploymentId: str
    embed: Optional[List[str]] = None


# This class is the input for the 'get_deployments' function.
class GetDeploymentsRequest(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_documentation_part' function.
class GetDocumentationPartRequest(BaseValidatorModel):
    restApiId: str
    documentationPartId: str


# This class is the input for the 'get_documentation_parts' function.
class GetDocumentationPartsRequest(BaseValidatorModel):
    restApiId: str
    type: Optional[DocumentationPartTypeType] = None
    nameQuery: Optional[str] = None
    path: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None
    locationStatus: Optional[LocationStatusTypeType] = None


# This class is the input for the 'get_documentation_version' function.
class GetDocumentationVersionRequest(BaseValidatorModel):
    restApiId: str
    documentationVersion: str


# This class is the input for the 'get_documentation_versions' function.
class GetDocumentationVersionsRequest(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_domain_name_access_associations' function.
class GetDomainNameAccessAssociationsRequest(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None
    resourceOwner: Optional[ResourceOwnerType] = None


# This class is the input for the 'get_domain_name' function.
class GetDomainNameRequest(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None


# This class is the input for the 'get_domain_names' function.
class GetDomainNamesRequest(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None
    resourceOwner: Optional[ResourceOwnerType] = None


# This class is the input for the 'get_export' function.
class GetExportRequest(BaseValidatorModel):
    restApiId: str
    stageName: str
    exportType: str
    parameters: Optional[Dict[str, str]] = None
    accepts: Optional[str] = None


# This class is the input for the 'get_gateway_response' function.
class GetGatewayResponseRequest(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType


# This class is the input for the 'get_gateway_responses' function.
class GetGatewayResponsesRequest(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_integration' function.
class GetIntegrationRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str


# This class is the input for the 'get_integration_response' function.
class GetIntegrationResponseRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str


# This class is the input for the 'get_method' function.
class GetMethodRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str


# This class is the input for the 'get_method_response' function.
class GetMethodResponseRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str


# This class is the input for the 'get_model' function.
class GetModelRequest(BaseValidatorModel):
    restApiId: str
    modelName: str
    flatten: Optional[bool] = None


# This class is the input for the 'get_model_template' function.
class GetModelTemplateRequest(BaseValidatorModel):
    restApiId: str
    modelName: str


# This class is the input for the 'get_models' function.
class GetModelsRequest(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_request_validator' function.
class GetRequestValidatorRequest(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str


# This class is the input for the 'get_request_validators' function.
class GetRequestValidatorsRequest(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_resource' function.
class GetResourceRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    embed: Optional[List[str]] = None


# This class is the input for the 'get_resources' function.
class GetResourcesRequest(BaseValidatorModel):
    restApiId: str
    position: Optional[str] = None
    limit: Optional[int] = None
    embed: Optional[List[str]] = None


# This class is the input for the 'get_rest_api' function.
class GetRestApiRequest(BaseValidatorModel):
    restApiId: str


# This class is the input for the 'get_rest_apis' function.
class GetRestApisRequest(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_sdk' function.
class GetSdkRequest(BaseValidatorModel):
    restApiId: str
    stageName: str
    sdkType: str
    parameters: Optional[Dict[str, str]] = None


# This class is the input for the 'get_sdk_type' function.
class GetSdkTypeRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_sdk_types' function.
class GetSdkTypesRequest(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_stage' function.
class GetStageRequest(BaseValidatorModel):
    restApiId: str
    stageName: str


# This class is the input for the 'get_stages' function.
class GetStagesRequest(BaseValidatorModel):
    restApiId: str
    deploymentId: Optional[str] = None


# This class is the input for the 'get_tags' function.
class GetTagsRequest(BaseValidatorModel):
    resourceArn: str
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_usage_plan_key' function.
class GetUsagePlanKeyRequest(BaseValidatorModel):
    usagePlanId: str
    keyId: str


# This class is the input for the 'get_usage_plan_keys' function.
class GetUsagePlanKeysRequest(BaseValidatorModel):
    usagePlanId: str
    position: Optional[str] = None
    limit: Optional[int] = None
    nameQuery: Optional[str] = None


# This class is the input for the 'get_usage_plan' function.
class GetUsagePlanRequest(BaseValidatorModel):
    usagePlanId: str


# This class is the input for the 'get_usage_plans' function.
class GetUsagePlansRequest(BaseValidatorModel):
    position: Optional[str] = None
    keyId: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_usage' function.
class GetUsageRequest(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: Optional[str] = None
    position: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'get_vpc_link' function.
class GetVpcLinkRequest(BaseValidatorModel):
    vpcLinkId: str


# This class is the input for the 'get_vpc_links' function.
class GetVpcLinksRequest(BaseValidatorModel):
    position: Optional[str] = None
    limit: Optional[int] = None


class IntegrationResponse(BaseValidatorModel):
    statusCode: Optional[str] = None
    selectionPattern: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None


class TlsConfig(BaseValidatorModel):
    insecureSkipVerification: Optional[bool] = None


class MethodResponse(BaseValidatorModel):
    statusCode: Optional[str] = None
    responseParameters: Optional[Dict[str, bool]] = None
    responseModels: Optional[Dict[str, str]] = None


class MethodSetting(BaseValidatorModel):
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


class Model(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    schema: Optional[str] = None
    contentType: Optional[str] = None


class PatchOperation(BaseValidatorModel):
    op: Optional[OpType] = None
    path: Optional[str] = None
    value: Optional[str] = None
    from_: Optional[str] = None


# This class is the input for the 'put_gateway_response' function.
class PutGatewayResponseRequest(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType
    statusCode: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None


# This class is the input for the 'put_integration_response' function.
class PutIntegrationResponseRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    selectionPattern: Optional[str] = None
    responseParameters: Optional[Dict[str, str]] = None
    responseTemplates: Optional[Dict[str, str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None


# This class is the input for the 'put_method' function.
class PutMethodRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    authorizationType: str
    authorizerId: Optional[str] = None
    apiKeyRequired: Optional[bool] = None
    operationName: Optional[str] = None
    requestParameters: Optional[Dict[str, bool]] = None
    requestModels: Optional[Dict[str, str]] = None
    requestValidatorId: Optional[str] = None
    authorizationScopes: Optional[List[str]] = None


# This class is the input for the 'put_method_response' function.
class PutMethodResponseRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    responseParameters: Optional[Dict[str, bool]] = None
    responseModels: Optional[Dict[str, str]] = None


# This class is the input for the 'reject_domain_name_access_association' function.
class RejectDomainNameAccessAssociationRequest(BaseValidatorModel):
    domainNameAccessAssociationArn: str
    domainNameArn: str


class RequestValidator(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    validateRequestBody: Optional[bool] = None
    validateRequestParameters: Optional[bool] = None


class SdkConfigurationProperty(BaseValidatorModel):
    name: Optional[str] = None
    friendlyName: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    defaultValue: Optional[str] = None


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'test_invoke_authorizer' function.
class TestInvokeAuthorizerRequest(BaseValidatorModel):
    restApiId: str
    authorizerId: str
    headers: Optional[Dict[str, str]] = None
    multiValueHeaders: Optional[Dict[str, List[str]]] = None
    pathWithQueryString: Optional[str] = None
    body: Optional[str] = None
    stageVariables: Optional[Dict[str, str]] = None
    additionalContext: Optional[Dict[str, str]] = None


# This class is the input for the 'test_invoke_method' function.
class TestInvokeMethodRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    pathWithQueryString: Optional[str] = None
    body: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    multiValueHeaders: Optional[Dict[str, List[str]]] = None
    clientCertificateId: Optional[str] = None
    stageVariables: Optional[Dict[str, str]] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UsagePlanKey(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    name: Optional[str] = None


class VpcLink(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    targetArns: Optional[List[str]] = None
    status: Optional[VpcLinkStatusType] = None
    statusMessage: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'import_api_keys' function.
class ApiKeyIds(BaseValidatorModel):
    ids: List[str]
    warnings: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_api_key' function.
class ApiKeyResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_authorizer' function.
class AuthorizerResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_base_path_mapping' function.
class BasePathMappingResponse(BaseValidatorModel):
    basePath: str
    restApiId: str
    stage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_client_certificate' function.
class ClientCertificateResponse(BaseValidatorModel):
    clientCertificateId: str
    description: str
    pemEncodedCertificate: str
    createdDate: datetime
    expirationDate: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_documentation_parts' function.
class DocumentationPartIds(BaseValidatorModel):
    ids: List[str]
    warnings: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_documentation_version' function.
class DocumentationVersionResponse(BaseValidatorModel):
    version: str
    createdDate: datetime
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_domain_name_access_association' function.
class DomainNameAccessAssociationResponse(BaseValidatorModel):
    domainNameAccessAssociationArn: str
    domainNameArn: str
    accessAssociationSourceType: Literal['VPCE']
    accessAssociationSource: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_export' function.
class ExportResponse(BaseValidatorModel):
    contentType: str
    contentDisposition: str
    body: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_gateway_response' function.
class GatewayResponseResponse(BaseValidatorModel):
    responseType: GatewayResponseTypeType
    statusCode: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    defaultResponse: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_integration_response' function.
class IntegrationResponseResponse(BaseValidatorModel):
    statusCode: str
    selectionPattern: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    contentHandling: ContentHandlingStrategyType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_method_response' function.
class MethodResponseResponse(BaseValidatorModel):
    statusCode: str
    responseParameters: Dict[str, bool]
    responseModels: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_model' function.
class ModelResponse(BaseValidatorModel):
    id: str
    name: str
    description: str
    schema: str
    contentType: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_request_validator' function.
class RequestValidatorResponse(BaseValidatorModel):
    id: str
    name: str
    validateRequestBody: bool
    validateRequestParameters: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sdk' function.
class SdkResponse(BaseValidatorModel):
    contentType: str
    contentDisposition: str
    body: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_tags' function.
class Tags(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_model_template' function.
class Template(BaseValidatorModel):
    value: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_invoke_authorizer' function.
class TestInvokeAuthorizerResponse(BaseValidatorModel):
    clientStatus: int
    log: str
    latency: int
    principalId: str
    policy: str
    authorization: Dict[str, List[str]]
    claims: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_invoke_method' function.
class TestInvokeMethodResponse(BaseValidatorModel):
    status: int
    body: str
    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    log: str
    latency: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_usage_plan_key' function.
class UsagePlanKeyResponse(BaseValidatorModel):
    id: str
    type: str
    value: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_usage' function.
class Usage(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    position: str
    items: Dict[str, List[List[int]]]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vpc_link' function.
class VpcLinkResponse(BaseValidatorModel):
    id: str
    name: str
    description: str
    targetArns: List[str]
    status: VpcLinkStatusType
    statusMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_account' function.
class Account(BaseValidatorModel):
    cloudwatchRoleArn: str
    throttleSettings: ThrottleSettings
    features: List[str]
    apiKeyVersion: str
    ResponseMetadata: ResponseMetadata


class ApiStageOutput(BaseValidatorModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Dict[str, ThrottleSettings]] = None


class ApiStage(BaseValidatorModel):
    apiId: Optional[str] = None
    stage: Optional[str] = None
    throttle: Optional[Dict[str, ThrottleSettings]] = None


# This class is the output for the 'get_api_keys' function.
class ApiKeys(BaseValidatorModel):
    warnings: List[str]
    position: str
    items: List[ApiKey]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_authorizers' function.
class Authorizers(BaseValidatorModel):
    position: str
    items: List[Authorizer]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_base_path_mappings' function.
class BasePathMappings(BaseValidatorModel):
    position: str
    items: List[BasePathMapping]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'import_api_keys' function.
class ImportApiKeysRequest(BaseValidatorModel):
    body: Blob
    format: Literal['csv']
    failOnWarnings: Optional[bool] = None


# This class is the input for the 'import_documentation_parts' function.
class ImportDocumentationPartsRequest(BaseValidatorModel):
    restApiId: str
    body: Blob
    mode: Optional[PutModeType] = None
    failOnWarnings: Optional[bool] = None


# This class is the input for the 'import_rest_api' function.
class ImportRestApiRequest(BaseValidatorModel):
    body: Blob
    failOnWarnings: Optional[bool] = None
    parameters: Optional[Dict[str, str]] = None


# This class is the input for the 'put_rest_api' function.
class PutRestApiRequest(BaseValidatorModel):
    restApiId: str
    body: Blob
    mode: Optional[PutModeType] = None
    failOnWarnings: Optional[bool] = None
    parameters: Optional[Dict[str, str]] = None

CanarySettingsUnion = Union[CanarySettings, CanarySettingsOutput]


# This class is the output for the 'get_client_certificates' function.
class ClientCertificates(BaseValidatorModel):
    position: str
    items: List[ClientCertificate]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_api_key' function.
class CreateApiKeyRequest(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    enabled: Optional[bool] = None
    generateDistinctId: Optional[bool] = None
    value: Optional[str] = None
    stageKeys: Optional[List[StageKey]] = None
    customerId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_deployment' function.
class CreateDeploymentRequest(BaseValidatorModel):
    restApiId: str
    stageName: Optional[str] = None
    stageDescription: Optional[str] = None
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    variables: Optional[Dict[str, str]] = None
    canarySettings: Optional[DeploymentCanarySettings] = None
    tracingEnabled: Optional[bool] = None


# This class is the input for the 'create_documentation_part' function.
class CreateDocumentationPartRequest(BaseValidatorModel):
    restApiId: str
    location: DocumentationPartLocation
    properties: str


# This class is the output for the 'update_documentation_part' function.
class DocumentationPartResponse(BaseValidatorModel):
    id: str
    location: DocumentationPartLocation
    properties: str
    ResponseMetadata: ResponseMetadata


class DocumentationPart(BaseValidatorModel):
    id: Optional[str] = None
    location: Optional[DocumentationPartLocation] = None
    properties: Optional[str] = None


# This class is the output for the 'update_deployment' function.
class DeploymentResponse(BaseValidatorModel):
    id: str
    description: str
    createdDate: datetime
    apiSummary: Dict[str, Dict[str, MethodSnapshot]]
    ResponseMetadata: ResponseMetadata


class Deployment(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[datetime] = None
    apiSummary: Optional[Dict[str, Dict[str, MethodSnapshot]]] = None


# This class is the output for the 'get_documentation_versions' function.
class DocumentationVersions(BaseValidatorModel):
    position: str
    items: List[DocumentationVersion]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain_name_access_associations' function.
class DomainNameAccessAssociations(BaseValidatorModel):
    position: str
    items: List[DomainNameAccessAssociation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_rest_api' function.
class RestApiResponse(BaseValidatorModel):
    id: str
    name: str
    description: str
    createdDate: datetime
    version: str
    warnings: List[str]
    binaryMediaTypes: List[str]
    minimumCompressionSize: int
    apiKeySource: ApiKeySourceTypeType
    endpointConfiguration: EndpointConfigurationOutput
    policy: str
    tags: Dict[str, str]
    disableExecuteApiEndpoint: bool
    rootResourceId: str
    ResponseMetadata: ResponseMetadata


class RestApi(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[datetime] = None
    version: Optional[str] = None
    warnings: Optional[List[str]] = None
    binaryMediaTypes: Optional[List[str]] = None
    minimumCompressionSize: Optional[int] = None
    apiKeySource: Optional[ApiKeySourceTypeType] = None
    endpointConfiguration: Optional[EndpointConfigurationOutput] = None
    policy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    disableExecuteApiEndpoint: Optional[bool] = None
    rootResourceId: Optional[str] = None


# This class is the output for the 'update_domain_name' function.
class DomainNameResponse(BaseValidatorModel):
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
    endpointConfiguration: EndpointConfigurationOutput
    domainNameStatus: DomainNameStatusType
    domainNameStatusMessage: str
    securityPolicy: SecurityPolicyType
    tags: Dict[str, str]
    mutualTlsAuthentication: MutualTlsAuthentication
    ownershipVerificationCertificateArn: str
    managementPolicy: str
    policy: str
    ResponseMetadata: ResponseMetadata


class DomainName(BaseValidatorModel):
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
    endpointConfiguration: Optional[EndpointConfigurationOutput] = None
    domainNameStatus: Optional[DomainNameStatusType] = None
    domainNameStatusMessage: Optional[str] = None
    securityPolicy: Optional[SecurityPolicyType] = None
    tags: Optional[Dict[str, str]] = None
    mutualTlsAuthentication: Optional[MutualTlsAuthentication] = None
    ownershipVerificationCertificateArn: Optional[str] = None
    managementPolicy: Optional[str] = None
    policy: Optional[str] = None

EndpointConfigurationUnion = Union[EndpointConfiguration, EndpointConfigurationOutput]


# This class is the output for the 'get_gateway_responses' function.
class GatewayResponses(BaseValidatorModel):
    position: str
    items: List[GatewayResponse]
    ResponseMetadata: ResponseMetadata


class GetApiKeysRequestPaginate(BaseValidatorModel):
    nameQuery: Optional[str] = None
    customerId: Optional[str] = None
    includeValues: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAuthorizersRequestPaginate(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBasePathMappingsRequestPaginate(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetClientCertificatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDeploymentsRequestPaginate(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDocumentationPartsRequestPaginate(BaseValidatorModel):
    restApiId: str
    type: Optional[DocumentationPartTypeType] = None
    nameQuery: Optional[str] = None
    path: Optional[str] = None
    locationStatus: Optional[LocationStatusTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDocumentationVersionsRequestPaginate(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDomainNamesRequestPaginate(BaseValidatorModel):
    resourceOwner: Optional[ResourceOwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetGatewayResponsesRequestPaginate(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetModelsRequestPaginate(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRequestValidatorsRequestPaginate(BaseValidatorModel):
    restApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourcesRequestPaginate(BaseValidatorModel):
    restApiId: str
    embed: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRestApisRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSdkTypesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetUsagePlanKeysRequestPaginate(BaseValidatorModel):
    usagePlanId: str
    nameQuery: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetUsagePlansRequestPaginate(BaseValidatorModel):
    keyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetUsageRequestPaginate(BaseValidatorModel):
    usagePlanId: str
    startDate: str
    endDate: str
    keyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetVpcLinksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'update_integration' function.
class IntegrationResponseExtra(BaseValidatorModel):
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
    integrationResponses: Dict[str, IntegrationResponse]
    tlsConfig: TlsConfig
    ResponseMetadata: ResponseMetadata


class Integration(BaseValidatorModel):
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
    integrationResponses: Optional[Dict[str, IntegrationResponse]] = None
    tlsConfig: Optional[TlsConfig] = None


# This class is the input for the 'put_integration' function.
class PutIntegrationRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    type: IntegrationTypeType
    integrationHttpMethod: Optional[str] = None
    uri: Optional[str] = None
    connectionType: Optional[ConnectionTypeType] = None
    connectionId: Optional[str] = None
    credentials: Optional[str] = None
    requestParameters: Optional[Dict[str, str]] = None
    requestTemplates: Optional[Dict[str, str]] = None
    passthroughBehavior: Optional[str] = None
    cacheNamespace: Optional[str] = None
    cacheKeyParameters: Optional[List[str]] = None
    contentHandling: Optional[ContentHandlingStrategyType] = None
    timeoutInMillis: Optional[int] = None
    tlsConfig: Optional[TlsConfig] = None


# This class is the output for the 'update_stage' function.
class StageResponse(BaseValidatorModel):
    deploymentId: str
    clientCertificateId: str
    stageName: str
    description: str
    cacheClusterEnabled: bool
    cacheClusterSize: CacheClusterSizeType
    cacheClusterStatus: CacheClusterStatusType
    methodSettings: Dict[str, MethodSetting]
    variables: Dict[str, str]
    documentationVersion: str
    accessLogSettings: AccessLogSettings
    canarySettings: CanarySettingsOutput
    tracingEnabled: bool
    webAclArn: str
    tags: Dict[str, str]
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadata


class Stage(BaseValidatorModel):
    deploymentId: Optional[str] = None
    clientCertificateId: Optional[str] = None
    stageName: Optional[str] = None
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    cacheClusterStatus: Optional[CacheClusterStatusType] = None
    methodSettings: Optional[Dict[str, MethodSetting]] = None
    variables: Optional[Dict[str, str]] = None
    documentationVersion: Optional[str] = None
    accessLogSettings: Optional[AccessLogSettings] = None
    canarySettings: Optional[CanarySettingsOutput] = None
    tracingEnabled: Optional[bool] = None
    webAclArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    createdDate: Optional[datetime] = None
    lastUpdatedDate: Optional[datetime] = None


# This class is the output for the 'get_models' function.
class Models(BaseValidatorModel):
    position: str
    items: List[Model]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_account' function.
class UpdateAccountRequest(BaseValidatorModel):
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_api_key' function.
class UpdateApiKeyRequest(BaseValidatorModel):
    apiKey: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_authorizer' function.
class UpdateAuthorizerRequest(BaseValidatorModel):
    restApiId: str
    authorizerId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_base_path_mapping' function.
class UpdateBasePathMappingRequest(BaseValidatorModel):
    domainName: str
    basePath: str
    domainNameId: Optional[str] = None
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_client_certificate' function.
class UpdateClientCertificateRequest(BaseValidatorModel):
    clientCertificateId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_deployment' function.
class UpdateDeploymentRequest(BaseValidatorModel):
    restApiId: str
    deploymentId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_documentation_part' function.
class UpdateDocumentationPartRequest(BaseValidatorModel):
    restApiId: str
    documentationPartId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_documentation_version' function.
class UpdateDocumentationVersionRequest(BaseValidatorModel):
    restApiId: str
    documentationVersion: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_domain_name' function.
class UpdateDomainNameRequest(BaseValidatorModel):
    domainName: str
    domainNameId: Optional[str] = None
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_gateway_response' function.
class UpdateGatewayResponseRequest(BaseValidatorModel):
    restApiId: str
    responseType: GatewayResponseTypeType
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_integration' function.
class UpdateIntegrationRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_integration_response' function.
class UpdateIntegrationResponseRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_method' function.
class UpdateMethodRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_method_response' function.
class UpdateMethodResponseRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    httpMethod: str
    statusCode: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_model' function.
class UpdateModelRequest(BaseValidatorModel):
    restApiId: str
    modelName: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_request_validator' function.
class UpdateRequestValidatorRequest(BaseValidatorModel):
    restApiId: str
    requestValidatorId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_resource' function.
class UpdateResourceRequest(BaseValidatorModel):
    restApiId: str
    resourceId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_rest_api' function.
class UpdateRestApiRequest(BaseValidatorModel):
    restApiId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_stage' function.
class UpdateStageRequest(BaseValidatorModel):
    restApiId: str
    stageName: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_usage_plan' function.
class UpdateUsagePlanRequest(BaseValidatorModel):
    usagePlanId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_usage' function.
class UpdateUsageRequest(BaseValidatorModel):
    usagePlanId: str
    keyId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the input for the 'update_vpc_link' function.
class UpdateVpcLinkRequest(BaseValidatorModel):
    vpcLinkId: str
    patchOperations: Optional[List[PatchOperation]] = None


# This class is the output for the 'get_request_validators' function.
class RequestValidators(BaseValidatorModel):
    position: str
    items: List[RequestValidator]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sdk_type' function.
class SdkTypeResponse(BaseValidatorModel):
    id: str
    friendlyName: str
    description: str
    configurationProperties: List[SdkConfigurationProperty]
    ResponseMetadata: ResponseMetadata


class SdkType(BaseValidatorModel):
    id: Optional[str] = None
    friendlyName: Optional[str] = None
    description: Optional[str] = None
    configurationProperties: Optional[List[SdkConfigurationProperty]] = None


# This class is the output for the 'get_usage_plan_keys' function.
class UsagePlanKeys(BaseValidatorModel):
    position: str
    items: List[UsagePlanKey]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_vpc_links' function.
class VpcLinks(BaseValidatorModel):
    position: str
    items: List[VpcLink]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_usage_plan' function.
class UsagePlanResponse(BaseValidatorModel):
    id: str
    name: str
    description: str
    apiStages: List[ApiStageOutput]
    throttle: ThrottleSettings
    quota: QuotaSettings
    productCode: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UsagePlan(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    apiStages: Optional[List[ApiStageOutput]] = None
    throttle: Optional[ThrottleSettings] = None
    quota: Optional[QuotaSettings] = None
    productCode: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

ApiStageUnion = Union[ApiStage, ApiStageOutput]


# This class is the input for the 'create_stage' function.
class CreateStageRequest(BaseValidatorModel):
    restApiId: str
    stageName: str
    deploymentId: str
    description: Optional[str] = None
    cacheClusterEnabled: Optional[bool] = None
    cacheClusterSize: Optional[CacheClusterSizeType] = None
    variables: Optional[Dict[str, str]] = None
    documentationVersion: Optional[str] = None
    canarySettings: Optional[CanarySettingsUnion] = None
    tracingEnabled: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_documentation_parts' function.
class DocumentationParts(BaseValidatorModel):
    position: str
    items: List[DocumentationPart]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_deployments' function.
class Deployments(BaseValidatorModel):
    position: str
    items: List[Deployment]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rest_apis' function.
class RestApis(BaseValidatorModel):
    position: str
    items: List[RestApi]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain_names' function.
class DomainNames(BaseValidatorModel):
    position: str
    items: List[DomainName]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_domain_name' function.
class CreateDomainNameRequest(BaseValidatorModel):
    domainName: str
    certificateName: Optional[str] = None
    certificateBody: Optional[str] = None
    certificatePrivateKey: Optional[str] = None
    certificateChain: Optional[str] = None
    certificateArn: Optional[str] = None
    regionalCertificateName: Optional[str] = None
    regionalCertificateArn: Optional[str] = None
    endpointConfiguration: Optional[EndpointConfigurationUnion] = None
    tags: Optional[Dict[str, str]] = None
    securityPolicy: Optional[SecurityPolicyType] = None
    mutualTlsAuthentication: Optional[MutualTlsAuthenticationInput] = None
    ownershipVerificationCertificateArn: Optional[str] = None
    policy: Optional[str] = None


# This class is the input for the 'create_rest_api' function.
class CreateRestApiRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    version: Optional[str] = None
    cloneFrom: Optional[str] = None
    binaryMediaTypes: Optional[List[str]] = None
    minimumCompressionSize: Optional[int] = None
    apiKeySource: Optional[ApiKeySourceTypeType] = None
    endpointConfiguration: Optional[EndpointConfigurationUnion] = None
    policy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    disableExecuteApiEndpoint: Optional[bool] = None


# This class is the output for the 'update_method' function.
class MethodResponseExtra(BaseValidatorModel):
    httpMethod: str
    authorizationType: str
    authorizerId: str
    apiKeyRequired: bool
    requestValidatorId: str
    operationName: str
    requestParameters: Dict[str, bool]
    requestModels: Dict[str, str]
    methodResponses: Dict[str, MethodResponse]
    methodIntegration: Integration
    authorizationScopes: List[str]
    ResponseMetadata: ResponseMetadata


class Method(BaseValidatorModel):
    httpMethod: Optional[str] = None
    authorizationType: Optional[str] = None
    authorizerId: Optional[str] = None
    apiKeyRequired: Optional[bool] = None
    requestValidatorId: Optional[str] = None
    operationName: Optional[str] = None
    requestParameters: Optional[Dict[str, bool]] = None
    requestModels: Optional[Dict[str, str]] = None
    methodResponses: Optional[Dict[str, MethodResponse]] = None
    methodIntegration: Optional[Integration] = None
    authorizationScopes: Optional[List[str]] = None


# This class is the output for the 'get_stages' function.
class Stages(BaseValidatorModel):
    item: List[Stage]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sdk_types' function.
class SdkTypes(BaseValidatorModel):
    position: str
    items: List[SdkType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_usage_plans' function.
class UsagePlans(BaseValidatorModel):
    position: str
    items: List[UsagePlan]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_usage_plan' function.
class CreateUsagePlanRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    apiStages: Optional[List[ApiStageUnion]] = None
    throttle: Optional[ThrottleSettings] = None
    quota: Optional[QuotaSettings] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'update_resource' function.
class ResourceResponse(BaseValidatorModel):
    id: str
    parentId: str
    pathPart: str
    path: str
    resourceMethods: Dict[str, Method]
    ResponseMetadata: ResponseMetadata


class Resource(BaseValidatorModel):
    id: Optional[str] = None
    parentId: Optional[str] = None
    pathPart: Optional[str] = None
    path: Optional[str] = None
    resourceMethods: Optional[Dict[str, Method]] = None


# This class is the output for the 'get_resources' function.
class Resources(BaseValidatorModel):
    position: str
    items: List[Resource]
    ResponseMetadata: ResponseMetadata