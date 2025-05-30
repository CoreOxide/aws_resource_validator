from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.apigatewayv2.apigatewayv2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessLogSettings(BaseValidatorModel):
    DestinationArn: Optional[str] = None
    Format: Optional[str] = None


class ApiMapping(BaseValidatorModel):
    ApiId: str
    Stage: str
    ApiMappingId: Optional[str] = None
    ApiMappingKey: Optional[str] = None


class CorsOutput(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[List[str]] = None
    AllowMethods: Optional[List[str]] = None
    AllowOrigins: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None


class JWTConfigurationOutput(BaseValidatorModel):
    Audience: Optional[List[str]] = None
    Issuer: Optional[str] = None


class Cors(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[List[str]] = None
    AllowMethods: Optional[List[str]] = None
    AllowOrigins: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None


# This class is the input for the 'create_api_mapping' function.
class CreateApiMappingRequest(BaseValidatorModel):
    ApiId: str
    DomainName: str
    Stage: str
    ApiMappingKey: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_deployment' function.
class CreateDeploymentRequest(BaseValidatorModel):
    ApiId: str
    Description: Optional[str] = None
    StageName: Optional[str] = None


class MutualTlsAuthenticationInput(BaseValidatorModel):
    TruststoreUri: Optional[str] = None
    TruststoreVersion: Optional[str] = None


class DomainNameConfigurationOutput(BaseValidatorModel):
    ApiGatewayDomainName: Optional[str] = None
    CertificateArn: Optional[str] = None
    CertificateName: Optional[str] = None
    CertificateUploadDate: Optional[datetime] = None
    DomainNameStatus: Optional[DomainNameStatusType] = None
    DomainNameStatusMessage: Optional[str] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostedZoneId: Optional[str] = None
    SecurityPolicy: Optional[SecurityPolicyType] = None
    OwnershipVerificationCertificateArn: Optional[str] = None


class MutualTlsAuthentication(BaseValidatorModel):
    TruststoreUri: Optional[str] = None
    TruststoreVersion: Optional[str] = None
    TruststoreWarnings: Optional[List[str]] = None


class TlsConfigInput(BaseValidatorModel):
    ServerNameToVerify: Optional[str] = None


# This class is the input for the 'create_integration_response' function.
class CreateIntegrationResponseRequest(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseKey: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    ResponseParameters: Optional[Dict[str, str]] = None
    ResponseTemplates: Optional[Dict[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None


class TlsConfig(BaseValidatorModel):
    ServerNameToVerify: Optional[str] = None


# This class is the input for the 'create_model' function.
class CreateModelRequest(BaseValidatorModel):
    ApiId: str
    Name: str
    Schema: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None


class ParameterConstraints(BaseValidatorModel):
    Required: Optional[bool] = None


class RouteSettings(BaseValidatorModel):
    DataTraceEnabled: Optional[bool] = None
    DetailedMetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[LoggingLevelType] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None


# This class is the input for the 'create_vpc_link' function.
class CreateVpcLinkRequest(BaseValidatorModel):
    Name: str
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'delete_access_log_settings' function.
class DeleteAccessLogSettingsRequest(BaseValidatorModel):
    ApiId: str
    StageName: str


# This class is the input for the 'delete_api_mapping' function.
class DeleteApiMappingRequest(BaseValidatorModel):
    ApiMappingId: str
    DomainName: str


# This class is the input for the 'delete_api' function.
class DeleteApiRequest(BaseValidatorModel):
    ApiId: str


# This class is the input for the 'delete_authorizer' function.
class DeleteAuthorizerRequest(BaseValidatorModel):
    ApiId: str
    AuthorizerId: str


# This class is the input for the 'delete_cors_configuration' function.
class DeleteCorsConfigurationRequest(BaseValidatorModel):
    ApiId: str


# This class is the input for the 'delete_deployment' function.
class DeleteDeploymentRequest(BaseValidatorModel):
    ApiId: str
    DeploymentId: str


# This class is the input for the 'delete_domain_name' function.
class DeleteDomainNameRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'delete_integration' function.
class DeleteIntegrationRequest(BaseValidatorModel):
    ApiId: str
    IntegrationId: str


# This class is the input for the 'delete_integration_response' function.
class DeleteIntegrationResponseRequest(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str


# This class is the input for the 'delete_model' function.
class DeleteModelRequest(BaseValidatorModel):
    ApiId: str
    ModelId: str


# This class is the input for the 'delete_route_request_parameter' function.
class DeleteRouteRequestParameterRequest(BaseValidatorModel):
    ApiId: str
    RequestParameterKey: str
    RouteId: str


# This class is the input for the 'delete_route' function.
class DeleteRouteRequest(BaseValidatorModel):
    ApiId: str
    RouteId: str


# This class is the input for the 'delete_route_response' function.
class DeleteRouteResponseRequest(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str


# This class is the input for the 'delete_route_settings' function.
class DeleteRouteSettingsRequest(BaseValidatorModel):
    ApiId: str
    RouteKey: str
    StageName: str


# This class is the input for the 'delete_stage' function.
class DeleteStageRequest(BaseValidatorModel):
    ApiId: str
    StageName: str


class DeleteVpcLinkRequest(BaseValidatorModel):
    VpcLinkId: str


class Deployment(BaseValidatorModel):
    AutoDeployed: Optional[bool] = None
    CreatedDate: Optional[datetime] = None
    DeploymentId: Optional[str] = None
    DeploymentStatus: Optional[DeploymentStatusType] = None
    DeploymentStatusMessage: Optional[str] = None
    Description: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'export_api' function.
class ExportApiRequest(BaseValidatorModel):
    ApiId: str
    OutputType: JSONYAMLType
    Specification: Literal['OAS30']
    ExportVersion: Optional[str] = None
    IncludeExtensions: Optional[bool] = None
    StageName: Optional[str] = None


# This class is the input for the 'get_api_mapping' function.
class GetApiMappingRequest(BaseValidatorModel):
    ApiMappingId: str
    DomainName: str


# This class is the input for the 'get_api_mappings' function.
class GetApiMappingsRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_api' function.
class GetApiRequest(BaseValidatorModel):
    ApiId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_apis' function.
class GetApisRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_authorizer' function.
class GetAuthorizerRequest(BaseValidatorModel):
    ApiId: str
    AuthorizerId: str


# This class is the input for the 'get_authorizers' function.
class GetAuthorizersRequest(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_deployment' function.
class GetDeploymentRequest(BaseValidatorModel):
    ApiId: str
    DeploymentId: str


# This class is the input for the 'get_deployments' function.
class GetDeploymentsRequest(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_domain_name' function.
class GetDomainNameRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'get_domain_names' function.
class GetDomainNamesRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_integration' function.
class GetIntegrationRequest(BaseValidatorModel):
    ApiId: str
    IntegrationId: str


# This class is the input for the 'get_integration_response' function.
class GetIntegrationResponseRequest(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str


# This class is the input for the 'get_integration_responses' function.
class GetIntegrationResponsesRequest(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class IntegrationResponse(BaseValidatorModel):
    IntegrationResponseKey: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    IntegrationResponseId: Optional[str] = None
    ResponseParameters: Optional[Dict[str, str]] = None
    ResponseTemplates: Optional[Dict[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None


# This class is the input for the 'get_integrations' function.
class GetIntegrationsRequest(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_model' function.
class GetModelRequest(BaseValidatorModel):
    ApiId: str
    ModelId: str


# This class is the input for the 'get_model_template' function.
class GetModelTemplateRequest(BaseValidatorModel):
    ApiId: str
    ModelId: str


# This class is the input for the 'get_models' function.
class GetModelsRequest(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class Model(BaseValidatorModel):
    Name: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None
    ModelId: Optional[str] = None
    Schema: Optional[str] = None


# This class is the input for the 'get_route' function.
class GetRouteRequest(BaseValidatorModel):
    ApiId: str
    RouteId: str


# This class is the input for the 'get_route_response' function.
class GetRouteResponseRequest(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str


# This class is the input for the 'get_route_responses' function.
class GetRouteResponsesRequest(BaseValidatorModel):
    ApiId: str
    RouteId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_routes' function.
class GetRoutesRequest(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_stage' function.
class GetStageRequest(BaseValidatorModel):
    ApiId: str
    StageName: str


# This class is the input for the 'get_stages' function.
class GetStagesRequest(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_tags' function.
class GetTagsRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_vpc_link' function.
class GetVpcLinkRequest(BaseValidatorModel):
    VpcLinkId: str


# This class is the input for the 'get_vpc_links' function.
class GetVpcLinksRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class VpcLink(BaseValidatorModel):
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    VpcLinkId: str
    CreatedDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    VpcLinkStatus: Optional[VpcLinkStatusType] = None
    VpcLinkStatusMessage: Optional[str] = None
    VpcLinkVersion: Optional[Literal['V2']] = None


# This class is the input for the 'import_api' function.
class ImportApiRequest(BaseValidatorModel):
    Body: str
    Basepath: Optional[str] = None
    FailOnWarnings: Optional[bool] = None


class JWTConfiguration(BaseValidatorModel):
    Audience: Optional[List[str]] = None
    Issuer: Optional[str] = None


# This class is the input for the 'reimport_api' function.
class ReimportApiRequest(BaseValidatorModel):
    ApiId: str
    Body: str
    Basepath: Optional[str] = None
    FailOnWarnings: Optional[bool] = None


# This class is the input for the 'reset_authorizers_cache' function.
class ResetAuthorizersCacheRequest(BaseValidatorModel):
    ApiId: str
    StageName: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_api_mapping' function.
class UpdateApiMappingRequest(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    DomainName: str
    ApiMappingKey: Optional[str] = None
    Stage: Optional[str] = None


# This class is the input for the 'update_deployment' function.
class UpdateDeploymentRequest(BaseValidatorModel):
    ApiId: str
    DeploymentId: str
    Description: Optional[str] = None


# This class is the input for the 'update_integration_response' function.
class UpdateIntegrationResponseRequest(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    IntegrationResponseKey: Optional[str] = None
    ResponseParameters: Optional[Dict[str, str]] = None
    ResponseTemplates: Optional[Dict[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None


# This class is the input for the 'update_model' function.
class UpdateModelRequest(BaseValidatorModel):
    ApiId: str
    ModelId: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    Schema: Optional[str] = None


# This class is the input for the 'update_vpc_link' function.
class UpdateVpcLinkRequest(BaseValidatorModel):
    VpcLinkId: str
    Name: Optional[str] = None


class Api(BaseValidatorModel):
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    ApiEndpoint: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsOutput] = None
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    ImportInfo: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    Version: Optional[str] = None
    Warnings: Optional[List[str]] = None


class Authorizer(BaseValidatorModel):
    Name: str
    AuthorizerCredentialsArn: Optional[str] = None
    AuthorizerId: Optional[str] = None
    AuthorizerPayloadFormatVersion: Optional[str] = None
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerType: Optional[AuthorizerTypeType] = None
    AuthorizerUri: Optional[str] = None
    EnableSimpleResponses: Optional[bool] = None
    IdentitySource: Optional[List[str]] = None
    IdentityValidationExpression: Optional[str] = None
    JwtConfiguration: Optional[JWTConfigurationOutput] = None

CorsUnion = Union[Cors, CorsOutput]


# This class is the output for the 'create_api_mapping' function.
class CreateApiMappingResponse(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_api' function.
class CreateApiResponse(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutput
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_authorizer' function.
class CreateAuthorizerResponse(BaseValidatorModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutput
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_deployment' function.
class CreateDeploymentResponse(BaseValidatorModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_integration_response' function.
class CreateIntegrationResponseResponse(BaseValidatorModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model' function.
class CreateModelResponse(BaseValidatorModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vpc_link' function.
class CreateVpcLinkResponse(BaseValidatorModel):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal['V2']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_api' function.
class ExportApiResponse(BaseValidatorModel):
    body: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_api_mapping' function.
class GetApiMappingResponse(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_api_mappings' function.
class GetApiMappingsResponse(BaseValidatorModel):
    Items: List[ApiMapping]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_api' function.
class GetApiResponse(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutput
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_authorizer' function.
class GetAuthorizerResponse(BaseValidatorModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutput
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_deployment' function.
class GetDeploymentResponse(BaseValidatorModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_integration_response' function.
class GetIntegrationResponseResponse(BaseValidatorModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_model' function.
class GetModelResponse(BaseValidatorModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_model_template' function.
class GetModelTemplateResponse(BaseValidatorModel):
    Value: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_tags' function.
class GetTagsResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_vpc_link' function.
class GetVpcLinkResponse(BaseValidatorModel):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal['V2']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_api' function.
class ImportApiResponse(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutput
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reimport_api' function.
class ReimportApiResponse(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutput
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_api_mapping' function.
class UpdateApiMappingResponse(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_api' function.
class UpdateApiResponse(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutput
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_authorizer' function.
class UpdateAuthorizerResponse(BaseValidatorModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutput
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_deployment' function.
class UpdateDeploymentResponse(BaseValidatorModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_integration_response' function.
class UpdateIntegrationResponseResponse(BaseValidatorModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_model' function.
class UpdateModelResponse(BaseValidatorModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vpc_link' function.
class UpdateVpcLinkResponse(BaseValidatorModel):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal['V2']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_domain_name' function.
class CreateDomainNameResponse(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutput]
    MutualTlsAuthentication: MutualTlsAuthentication
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DomainName(BaseValidatorModel):
    DomainName: str
    ApiMappingSelectionExpression: Optional[str] = None
    DomainNameConfigurations: Optional[List[DomainNameConfigurationOutput]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthentication] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_domain_name' function.
class GetDomainNameResponse(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutput]
    MutualTlsAuthentication: MutualTlsAuthentication
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_name' function.
class UpdateDomainNameResponse(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutput]
    MutualTlsAuthentication: MutualTlsAuthentication
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_integration' function.
class CreateIntegrationRequest(BaseValidatorModel):
    ApiId: str
    IntegrationType: IntegrationTypeType
    ConnectionId: Optional[str] = None
    ConnectionType: Optional[ConnectionTypeType] = None
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    IntegrationMethod: Optional[str] = None
    IntegrationSubtype: Optional[str] = None
    IntegrationUri: Optional[str] = None
    PassthroughBehavior: Optional[PassthroughBehaviorType] = None
    PayloadFormatVersion: Optional[str] = None
    RequestParameters: Optional[Dict[str, str]] = None
    RequestTemplates: Optional[Dict[str, str]] = None
    ResponseParameters: Optional[Dict[str, Dict[str, str]]] = None
    TemplateSelectionExpression: Optional[str] = None
    TimeoutInMillis: Optional[int] = None
    TlsConfig: Optional[TlsConfigInput] = None


# This class is the input for the 'update_integration' function.
class UpdateIntegrationRequest(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    ConnectionId: Optional[str] = None
    ConnectionType: Optional[ConnectionTypeType] = None
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    IntegrationMethod: Optional[str] = None
    IntegrationSubtype: Optional[str] = None
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationUri: Optional[str] = None
    PassthroughBehavior: Optional[PassthroughBehaviorType] = None
    PayloadFormatVersion: Optional[str] = None
    RequestParameters: Optional[Dict[str, str]] = None
    RequestTemplates: Optional[Dict[str, str]] = None
    ResponseParameters: Optional[Dict[str, Dict[str, str]]] = None
    TemplateSelectionExpression: Optional[str] = None
    TimeoutInMillis: Optional[int] = None
    TlsConfig: Optional[TlsConfigInput] = None


# This class is the output for the 'create_integration' function.
class CreateIntegrationResult(BaseValidatorModel):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    ContentHandlingStrategy: ContentHandlingStrategyType
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationTypeType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehaviorType
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: TlsConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_integration' function.
class GetIntegrationResult(BaseValidatorModel):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    ContentHandlingStrategy: ContentHandlingStrategyType
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationTypeType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehaviorType
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: TlsConfig
    ResponseMetadata: ResponseMetadata


class Integration(BaseValidatorModel):
    ApiGatewayManaged: Optional[bool] = None
    ConnectionId: Optional[str] = None
    ConnectionType: Optional[ConnectionTypeType] = None
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    IntegrationId: Optional[str] = None
    IntegrationMethod: Optional[str] = None
    IntegrationResponseSelectionExpression: Optional[str] = None
    IntegrationSubtype: Optional[str] = None
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationUri: Optional[str] = None
    PassthroughBehavior: Optional[PassthroughBehaviorType] = None
    PayloadFormatVersion: Optional[str] = None
    RequestParameters: Optional[Dict[str, str]] = None
    RequestTemplates: Optional[Dict[str, str]] = None
    ResponseParameters: Optional[Dict[str, Dict[str, str]]] = None
    TemplateSelectionExpression: Optional[str] = None
    TimeoutInMillis: Optional[int] = None
    TlsConfig: Optional[TlsConfig] = None


# This class is the output for the 'update_integration' function.
class UpdateIntegrationResult(BaseValidatorModel):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionTypeType
    ContentHandlingStrategy: ContentHandlingStrategyType
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationTypeType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehaviorType
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: TlsConfig
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_route' function.
class CreateRouteRequest(BaseValidatorModel):
    ApiId: str
    RouteKey: str
    ApiKeyRequired: Optional[bool] = None
    AuthorizationScopes: Optional[List[str]] = None
    AuthorizationType: Optional[AuthorizationTypeType] = None
    AuthorizerId: Optional[str] = None
    ModelSelectionExpression: Optional[str] = None
    OperationName: Optional[str] = None
    RequestModels: Optional[Dict[str, str]] = None
    RequestParameters: Optional[Dict[str, ParameterConstraints]] = None
    RouteResponseSelectionExpression: Optional[str] = None
    Target: Optional[str] = None


# This class is the input for the 'create_route_response' function.
class CreateRouteResponseRequest(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseKey: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Dict[str, str]] = None
    ResponseParameters: Optional[Dict[str, ParameterConstraints]] = None


# This class is the output for the 'create_route_response' function.
class CreateRouteResponseResponse(BaseValidatorModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraints]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_route' function.
class CreateRouteResult(BaseValidatorModel):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraints]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_route_response' function.
class GetRouteResponseResponse(BaseValidatorModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraints]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_route' function.
class GetRouteResult(BaseValidatorModel):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraints]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadata


class RouteResponse(BaseValidatorModel):
    RouteResponseKey: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Dict[str, str]] = None
    ResponseParameters: Optional[Dict[str, ParameterConstraints]] = None
    RouteResponseId: Optional[str] = None


class Route(BaseValidatorModel):
    RouteKey: str
    ApiGatewayManaged: Optional[bool] = None
    ApiKeyRequired: Optional[bool] = None
    AuthorizationScopes: Optional[List[str]] = None
    AuthorizationType: Optional[AuthorizationTypeType] = None
    AuthorizerId: Optional[str] = None
    ModelSelectionExpression: Optional[str] = None
    OperationName: Optional[str] = None
    RequestModels: Optional[Dict[str, str]] = None
    RequestParameters: Optional[Dict[str, ParameterConstraints]] = None
    RouteId: Optional[str] = None
    RouteResponseSelectionExpression: Optional[str] = None
    Target: Optional[str] = None


# This class is the input for the 'update_route' function.
class UpdateRouteRequest(BaseValidatorModel):
    ApiId: str
    RouteId: str
    ApiKeyRequired: Optional[bool] = None
    AuthorizationScopes: Optional[List[str]] = None
    AuthorizationType: Optional[AuthorizationTypeType] = None
    AuthorizerId: Optional[str] = None
    ModelSelectionExpression: Optional[str] = None
    OperationName: Optional[str] = None
    RequestModels: Optional[Dict[str, str]] = None
    RequestParameters: Optional[Dict[str, ParameterConstraints]] = None
    RouteKey: Optional[str] = None
    RouteResponseSelectionExpression: Optional[str] = None
    Target: Optional[str] = None


# This class is the input for the 'update_route_response' function.
class UpdateRouteResponseRequest(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Dict[str, str]] = None
    ResponseParameters: Optional[Dict[str, ParameterConstraints]] = None
    RouteResponseKey: Optional[str] = None


# This class is the output for the 'update_route_response' function.
class UpdateRouteResponseResponse(BaseValidatorModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraints]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_route' function.
class UpdateRouteResult(BaseValidatorModel):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraints]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_stage' function.
class CreateStageRequest(BaseValidatorModel):
    ApiId: str
    StageName: str
    AccessLogSettings: Optional[AccessLogSettings] = None
    AutoDeploy: Optional[bool] = None
    ClientCertificateId: Optional[str] = None
    DefaultRouteSettings: Optional[RouteSettings] = None
    DeploymentId: Optional[str] = None
    Description: Optional[str] = None
    RouteSettings: Optional[Dict[str, RouteSettings]] = None
    StageVariables: Optional[Dict[str, str]] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_stage' function.
class CreateStageResponse(BaseValidatorModel):
    AccessLogSettings: AccessLogSettings
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettings
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettings]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_stage' function.
class GetStageResponse(BaseValidatorModel):
    AccessLogSettings: AccessLogSettings
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettings
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettings]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Stage(BaseValidatorModel):
    StageName: str
    AccessLogSettings: Optional[AccessLogSettings] = None
    ApiGatewayManaged: Optional[bool] = None
    AutoDeploy: Optional[bool] = None
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    DefaultRouteSettings: Optional[RouteSettings] = None
    DeploymentId: Optional[str] = None
    Description: Optional[str] = None
    LastDeploymentStatusMessage: Optional[str] = None
    LastUpdatedDate: Optional[datetime] = None
    RouteSettings: Optional[Dict[str, RouteSettings]] = None
    StageVariables: Optional[Dict[str, str]] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_stage' function.
class UpdateStageRequest(BaseValidatorModel):
    ApiId: str
    StageName: str
    AccessLogSettings: Optional[AccessLogSettings] = None
    AutoDeploy: Optional[bool] = None
    ClientCertificateId: Optional[str] = None
    DefaultRouteSettings: Optional[RouteSettings] = None
    DeploymentId: Optional[str] = None
    Description: Optional[str] = None
    RouteSettings: Optional[Dict[str, RouteSettings]] = None
    StageVariables: Optional[Dict[str, str]] = None


# This class is the output for the 'update_stage' function.
class UpdateStageResponse(BaseValidatorModel):
    AccessLogSettings: AccessLogSettings
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettings
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettings]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_deployments' function.
class GetDeploymentsResponse(BaseValidatorModel):
    Items: List[Deployment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DomainNameConfiguration(BaseValidatorModel):
    ApiGatewayDomainName: Optional[str] = None
    CertificateArn: Optional[str] = None
    CertificateName: Optional[str] = None
    CertificateUploadDate: Optional[Timestamp] = None
    DomainNameStatus: Optional[DomainNameStatusType] = None
    DomainNameStatusMessage: Optional[str] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostedZoneId: Optional[str] = None
    SecurityPolicy: Optional[SecurityPolicyType] = None
    OwnershipVerificationCertificateArn: Optional[str] = None


class GetApisRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAuthorizersRequestPaginate(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDeploymentsRequestPaginate(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDomainNamesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetIntegrationResponsesRequestPaginate(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetIntegrationsRequestPaginate(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetModelsRequestPaginate(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRouteResponsesRequestPaginate(BaseValidatorModel):
    ApiId: str
    RouteId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRoutesRequestPaginate(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetStagesRequestPaginate(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'get_integration_responses' function.
class GetIntegrationResponsesResponse(BaseValidatorModel):
    Items: List[IntegrationResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_models' function.
class GetModelsResponse(BaseValidatorModel):
    Items: List[Model]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_vpc_links' function.
class GetVpcLinksResponse(BaseValidatorModel):
    Items: List[VpcLink]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

JWTConfigurationUnion = Union[JWTConfiguration, JWTConfigurationOutput]


# This class is the output for the 'get_apis' function.
class GetApisResponse(BaseValidatorModel):
    Items: List[Api]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_authorizers' function.
class GetAuthorizersResponse(BaseValidatorModel):
    Items: List[Authorizer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_api' function.
class CreateApiRequest(BaseValidatorModel):
    Name: str
    ProtocolType: ProtocolTypeType
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsUnion] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    RouteKey: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    Target: Optional[str] = None
    Version: Optional[str] = None


# This class is the input for the 'update_api' function.
class UpdateApiRequest(BaseValidatorModel):
    ApiId: str
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsUnion] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    Name: Optional[str] = None
    RouteKey: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    Target: Optional[str] = None
    Version: Optional[str] = None


# This class is the output for the 'get_domain_names' function.
class GetDomainNamesResponse(BaseValidatorModel):
    Items: List[DomainName]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_integrations' function.
class GetIntegrationsResponse(BaseValidatorModel):
    Items: List[Integration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_route_responses' function.
class GetRouteResponsesResponse(BaseValidatorModel):
    Items: List[RouteResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_routes' function.
class GetRoutesResponse(BaseValidatorModel):
    Items: List[Route]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_stages' function.
class GetStagesResponse(BaseValidatorModel):
    Items: List[Stage]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

DomainNameConfigurationUnion = Union[DomainNameConfiguration, DomainNameConfigurationOutput]


# This class is the input for the 'create_authorizer' function.
class CreateAuthorizerRequest(BaseValidatorModel):
    ApiId: str
    AuthorizerType: AuthorizerTypeType
    IdentitySource: List[str]
    Name: str
    AuthorizerCredentialsArn: Optional[str] = None
    AuthorizerPayloadFormatVersion: Optional[str] = None
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerUri: Optional[str] = None
    EnableSimpleResponses: Optional[bool] = None
    IdentityValidationExpression: Optional[str] = None
    JwtConfiguration: Optional[JWTConfigurationUnion] = None


# This class is the input for the 'update_authorizer' function.
class UpdateAuthorizerRequest(BaseValidatorModel):
    ApiId: str
    AuthorizerId: str
    AuthorizerCredentialsArn: Optional[str] = None
    AuthorizerPayloadFormatVersion: Optional[str] = None
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerType: Optional[AuthorizerTypeType] = None
    AuthorizerUri: Optional[str] = None
    EnableSimpleResponses: Optional[bool] = None
    IdentitySource: Optional[List[str]] = None
    IdentityValidationExpression: Optional[str] = None
    JwtConfiguration: Optional[JWTConfigurationUnion] = None
    Name: Optional[str] = None


# This class is the input for the 'create_domain_name' function.
class CreateDomainNameRequest(BaseValidatorModel):
    DomainName: str
    DomainNameConfigurations: Optional[List[DomainNameConfigurationUnion]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInput] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_domain_name' function.
class UpdateDomainNameRequest(BaseValidatorModel):
    DomainName: str
    DomainNameConfigurations: Optional[List[DomainNameConfigurationUnion]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInput] = None