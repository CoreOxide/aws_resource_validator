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
from aws_resource_validator.pydantic_models.apigatewayv2_constants import *

class AccessLogSettingsTypeDef(BaseModel):
    DestinationArn: Optional[str] = None
    Format: Optional[str] = None

class ApiMappingTypeDef(BaseModel):
    ApiId: str
    Stage: str
    ApiMappingId: Optional[str] = None
    ApiMappingKey: Optional[str] = None

class CorsPaginatorTypeDef(BaseModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[List[str]] = None
    AllowMethods: Optional[List[str]] = None
    AllowOrigins: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None

class CorsTypeDef(BaseModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[Sequence[str]] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowOrigins: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None

class JWTConfigurationPaginatorTypeDef(BaseModel):
    Audience: Optional[List[str]] = None
    Issuer: Optional[str] = None

class JWTConfigurationTypeDef(BaseModel):
    Audience: Optional[Sequence[str]] = None
    Issuer: Optional[str] = None

class CreateApiMappingRequestRequestTypeDef(BaseModel):
    ApiId: str
    DomainName: str
    Stage: str
    ApiMappingKey: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateDeploymentRequestRequestTypeDef(BaseModel):
    ApiId: str
    Description: Optional[str] = None
    StageName: Optional[str] = None

class MutualTlsAuthenticationInputTypeDef(BaseModel):
    TruststoreUri: Optional[str] = None
    TruststoreVersion: Optional[str] = None

class MutualTlsAuthenticationTypeDef(BaseModel):
    TruststoreUri: Optional[str] = None
    TruststoreVersion: Optional[str] = None
    TruststoreWarnings: Optional[List[str]] = None

class TlsConfigInputTypeDef(BaseModel):
    ServerNameToVerify: Optional[str] = None

class CreateIntegrationResponseRequestRequestTypeDef(BaseModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseKey: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    ResponseParameters: Optional[Mapping[str, str]] = None
    ResponseTemplates: Optional[Mapping[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None

class TlsConfigTypeDef(BaseModel):
    ServerNameToVerify: Optional[str] = None

class CreateModelRequestRequestTypeDef(BaseModel):
    ApiId: str
    Name: str
    Schema: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None

class ParameterConstraintsTypeDef(BaseModel):
    Required: Optional[bool] = None

class RouteSettingsTypeDef(BaseModel):
    DataTraceEnabled: Optional[bool] = None
    DetailedMetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[LoggingLevelType] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None

class CreateVpcLinkRequestRequestTypeDef(BaseModel):
    Name: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteAccessLogSettingsRequestRequestTypeDef(BaseModel):
    ApiId: str
    StageName: str

class DeleteApiMappingRequestRequestTypeDef(BaseModel):
    ApiMappingId: str
    DomainName: str

class DeleteApiRequestRequestTypeDef(BaseModel):
    ApiId: str

class DeleteAuthorizerRequestRequestTypeDef(BaseModel):
    ApiId: str
    AuthorizerId: str

class DeleteCorsConfigurationRequestRequestTypeDef(BaseModel):
    ApiId: str

class DeleteDeploymentRequestRequestTypeDef(BaseModel):
    ApiId: str
    DeploymentId: str

class DeleteDomainNameRequestRequestTypeDef(BaseModel):
    DomainName: str

class DeleteIntegrationRequestRequestTypeDef(BaseModel):
    ApiId: str
    IntegrationId: str

class DeleteIntegrationResponseRequestRequestTypeDef(BaseModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str

class DeleteModelRequestRequestTypeDef(BaseModel):
    ApiId: str
    ModelId: str

class DeleteRouteRequestParameterRequestRequestTypeDef(BaseModel):
    ApiId: str
    RequestParameterKey: str
    RouteId: str

class DeleteRouteRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteId: str

class DeleteRouteResponseRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str

class DeleteRouteSettingsRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteKey: str
    StageName: str

class DeleteStageRequestRequestTypeDef(BaseModel):
    ApiId: str
    StageName: str

class DeleteVpcLinkRequestRequestTypeDef(BaseModel):
    VpcLinkId: str

class DeploymentTypeDef(BaseModel):
    AutoDeployed: Optional[bool] = None
    CreatedDate: Optional[datetime] = None
    DeploymentId: Optional[str] = None
    DeploymentStatus: Optional[DeploymentStatusType] = None
    DeploymentStatusMessage: Optional[str] = None
    Description: Optional[str] = None

class DomainNameConfigurationPaginatorTypeDef(BaseModel):
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

class ExportApiRequestRequestTypeDef(BaseModel):
    ApiId: str
    OutputType: JSONYAMLType
    Specification: Literal["OAS30"]
    ExportVersion: Optional[str] = None
    IncludeExtensions: Optional[bool] = None
    StageName: Optional[str] = None

class GetApiMappingRequestRequestTypeDef(BaseModel):
    ApiMappingId: str
    DomainName: str

class GetApiMappingsRequestRequestTypeDef(BaseModel):
    DomainName: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetApiRequestRequestTypeDef(BaseModel):
    ApiId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetApisRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetAuthorizerRequestRequestTypeDef(BaseModel):
    ApiId: str
    AuthorizerId: str

class GetAuthorizersRequestRequestTypeDef(BaseModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetDeploymentRequestRequestTypeDef(BaseModel):
    ApiId: str
    DeploymentId: str

class GetDeploymentsRequestRequestTypeDef(BaseModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetDomainNameRequestRequestTypeDef(BaseModel):
    DomainName: str

class GetDomainNamesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetIntegrationRequestRequestTypeDef(BaseModel):
    ApiId: str
    IntegrationId: str

class GetIntegrationResponseRequestRequestTypeDef(BaseModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str

class GetIntegrationResponsesRequestRequestTypeDef(BaseModel):
    ApiId: str
    IntegrationId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class IntegrationResponseTypeDef(BaseModel):
    IntegrationResponseKey: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    IntegrationResponseId: Optional[str] = None
    ResponseParameters: Optional[Dict[str, str]] = None
    ResponseTemplates: Optional[Dict[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None

class GetIntegrationsRequestRequestTypeDef(BaseModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetModelRequestRequestTypeDef(BaseModel):
    ApiId: str
    ModelId: str

class GetModelTemplateRequestRequestTypeDef(BaseModel):
    ApiId: str
    ModelId: str

class GetModelsRequestRequestTypeDef(BaseModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ModelTypeDef(BaseModel):
    Name: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None
    ModelId: Optional[str] = None
    Schema: Optional[str] = None

class GetRouteRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteId: str

class GetRouteResponseRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str

class GetRouteResponsesRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetRoutesRequestRequestTypeDef(BaseModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetStageRequestRequestTypeDef(BaseModel):
    ApiId: str
    StageName: str

class GetStagesRequestRequestTypeDef(BaseModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetTagsRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GetVpcLinkRequestRequestTypeDef(BaseModel):
    VpcLinkId: str

class GetVpcLinksRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class VpcLinkTypeDef(BaseModel):
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    VpcLinkId: str
    CreatedDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    VpcLinkStatus: Optional[VpcLinkStatusType] = None
    VpcLinkStatusMessage: Optional[str] = None
    VpcLinkVersion: Optional[Literal["V2"]] = None

class ImportApiRequestRequestTypeDef(BaseModel):
    Body: str
    Basepath: Optional[str] = None
    FailOnWarnings: Optional[bool] = None

class ReimportApiRequestRequestTypeDef(BaseModel):
    ApiId: str
    Body: str
    Basepath: Optional[str] = None
    FailOnWarnings: Optional[bool] = None

class ResetAuthorizersCacheRequestRequestTypeDef(BaseModel):
    ApiId: str
    StageName: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApiMappingRequestRequestTypeDef(BaseModel):
    ApiId: str
    ApiMappingId: str
    DomainName: str
    ApiMappingKey: Optional[str] = None
    Stage: Optional[str] = None

class UpdateDeploymentRequestRequestTypeDef(BaseModel):
    ApiId: str
    DeploymentId: str
    Description: Optional[str] = None

class UpdateIntegrationResponseRequestRequestTypeDef(BaseModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    IntegrationResponseKey: Optional[str] = None
    ResponseParameters: Optional[Mapping[str, str]] = None
    ResponseTemplates: Optional[Mapping[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None

class UpdateModelRequestRequestTypeDef(BaseModel):
    ApiId: str
    ModelId: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    Schema: Optional[str] = None

class UpdateVpcLinkRequestRequestTypeDef(BaseModel):
    VpcLinkId: str
    Name: Optional[str] = None

class ApiPaginatorTypeDef(BaseModel):
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    ApiEndpoint: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsPaginatorTypeDef] = None
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    ImportInfo: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    Version: Optional[str] = None
    Warnings: Optional[List[str]] = None

class ApiTypeDef(BaseModel):
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    ApiEndpoint: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsTypeDef] = None
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    ImportInfo: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    Version: Optional[str] = None
    Warnings: Optional[List[str]] = None

class CreateApiRequestRequestTypeDef(BaseModel):
    Name: str
    ProtocolType: ProtocolTypeType
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsTypeDef] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    RouteKey: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Target: Optional[str] = None
    Version: Optional[str] = None

class UpdateApiRequestRequestTypeDef(BaseModel):
    ApiId: str
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsTypeDef] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    Name: Optional[str] = None
    RouteKey: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    Target: Optional[str] = None
    Version: Optional[str] = None

class AuthorizerPaginatorTypeDef(BaseModel):
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
    JwtConfiguration: Optional[JWTConfigurationPaginatorTypeDef] = None

class AuthorizerTypeDef(BaseModel):
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
    JwtConfiguration: Optional[JWTConfigurationTypeDef] = None

class CreateAuthorizerRequestRequestTypeDef(BaseModel):
    ApiId: str
    AuthorizerType: AuthorizerTypeType
    IdentitySource: Sequence[str]
    Name: str
    AuthorizerCredentialsArn: Optional[str] = None
    AuthorizerPayloadFormatVersion: Optional[str] = None
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerUri: Optional[str] = None
    EnableSimpleResponses: Optional[bool] = None
    IdentityValidationExpression: Optional[str] = None
    JwtConfiguration: Optional[JWTConfigurationTypeDef] = None

class UpdateAuthorizerRequestRequestTypeDef(BaseModel):
    ApiId: str
    AuthorizerId: str
    AuthorizerCredentialsArn: Optional[str] = None
    AuthorizerPayloadFormatVersion: Optional[str] = None
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerType: Optional[AuthorizerTypeType] = None
    AuthorizerUri: Optional[str] = None
    EnableSimpleResponses: Optional[bool] = None
    IdentitySource: Optional[Sequence[str]] = None
    IdentityValidationExpression: Optional[str] = None
    JwtConfiguration: Optional[JWTConfigurationTypeDef] = None
    Name: Optional[str] = None

class CreateApiMappingResponseTypeDef(BaseModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiResponseTypeDef(BaseModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAuthorizerResponseTypeDef(BaseModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(BaseModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationResponseResponseTypeDef(BaseModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelResponseTypeDef(BaseModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcLinkResponseTypeDef(BaseModel):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportApiResponseTypeDef(BaseModel):
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiMappingResponseTypeDef(BaseModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiMappingsResponseTypeDef(BaseModel):
    Items: List[ApiMappingTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiResponseTypeDef(BaseModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthorizerResponseTypeDef(BaseModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentResponseTypeDef(BaseModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationResponseResponseTypeDef(BaseModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelResponseTypeDef(BaseModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelTemplateResponseTypeDef(BaseModel):
    Value: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagsResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcLinkResponseTypeDef(BaseModel):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportApiResponseTypeDef(BaseModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class ReimportApiResponseTypeDef(BaseModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiMappingResponseTypeDef(BaseModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiResponseTypeDef(BaseModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAuthorizerResponseTypeDef(BaseModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeploymentResponseTypeDef(BaseModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIntegrationResponseResponseTypeDef(BaseModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelResponseTypeDef(BaseModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcLinkResponseTypeDef(BaseModel):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatusType
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationRequestRequestTypeDef(BaseModel):
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
    RequestParameters: Optional[Mapping[str, str]] = None
    RequestTemplates: Optional[Mapping[str, str]] = None
    ResponseParameters: Optional[Mapping[str, Mapping[str, str]]] = None
    TemplateSelectionExpression: Optional[str] = None
    TimeoutInMillis: Optional[int] = None
    TlsConfig: Optional[TlsConfigInputTypeDef] = None

class UpdateIntegrationRequestRequestTypeDef(BaseModel):
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
    RequestParameters: Optional[Mapping[str, str]] = None
    RequestTemplates: Optional[Mapping[str, str]] = None
    ResponseParameters: Optional[Mapping[str, Mapping[str, str]]] = None
    TemplateSelectionExpression: Optional[str] = None
    TimeoutInMillis: Optional[int] = None
    TlsConfig: Optional[TlsConfigInputTypeDef] = None

class CreateIntegrationResultTypeDef(BaseModel):
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
    TlsConfig: TlsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationResultTypeDef(BaseModel):
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
    TlsConfig: TlsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationTypeDef(BaseModel):
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
    TlsConfig: Optional[TlsConfigTypeDef] = None

class UpdateIntegrationResultTypeDef(BaseModel):
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
    TlsConfig: TlsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteKey: str
    ApiKeyRequired: Optional[bool] = None
    AuthorizationScopes: Optional[Sequence[str]] = None
    AuthorizationType: Optional[AuthorizationTypeType] = None
    AuthorizerId: Optional[str] = None
    ModelSelectionExpression: Optional[str] = None
    OperationName: Optional[str] = None
    RequestModels: Optional[Mapping[str, str]] = None
    RequestParameters: Optional[Mapping[str, ParameterConstraintsTypeDef]] = None
    RouteResponseSelectionExpression: Optional[str] = None
    Target: Optional[str] = None

class CreateRouteResponseRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteId: str
    RouteResponseKey: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Mapping[str, str]] = None
    ResponseParameters: Optional[Mapping[str, ParameterConstraintsTypeDef]] = None

class CreateRouteResponseResponseTypeDef(BaseModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteResultTypeDef(BaseModel):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouteResponseResponseTypeDef(BaseModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouteResultTypeDef(BaseModel):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadataTypeDef

class RouteResponseTypeDef(BaseModel):
    RouteResponseKey: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Dict[str, str]] = None
    ResponseParameters: Optional[Dict[str, ParameterConstraintsTypeDef]] = None
    RouteResponseId: Optional[str] = None

class RouteTypeDef(BaseModel):
    RouteKey: str
    ApiGatewayManaged: Optional[bool] = None
    ApiKeyRequired: Optional[bool] = None
    AuthorizationScopes: Optional[List[str]] = None
    AuthorizationType: Optional[AuthorizationTypeType] = None
    AuthorizerId: Optional[str] = None
    ModelSelectionExpression: Optional[str] = None
    OperationName: Optional[str] = None
    RequestModels: Optional[Dict[str, str]] = None
    RequestParameters: Optional[Dict[str, ParameterConstraintsTypeDef]] = None
    RouteId: Optional[str] = None
    RouteResponseSelectionExpression: Optional[str] = None
    Target: Optional[str] = None

class UpdateRouteRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteId: str
    ApiKeyRequired: Optional[bool] = None
    AuthorizationScopes: Optional[Sequence[str]] = None
    AuthorizationType: Optional[AuthorizationTypeType] = None
    AuthorizerId: Optional[str] = None
    ModelSelectionExpression: Optional[str] = None
    OperationName: Optional[str] = None
    RequestModels: Optional[Mapping[str, str]] = None
    RequestParameters: Optional[Mapping[str, ParameterConstraintsTypeDef]] = None
    RouteKey: Optional[str] = None
    RouteResponseSelectionExpression: Optional[str] = None
    Target: Optional[str] = None

class UpdateRouteResponseRequestRequestTypeDef(BaseModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Mapping[str, str]] = None
    ResponseParameters: Optional[Mapping[str, ParameterConstraintsTypeDef]] = None
    RouteResponseKey: Optional[str] = None

class UpdateRouteResponseResponseTypeDef(BaseModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouteResultTypeDef(BaseModel):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationTypeType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStageRequestRequestTypeDef(BaseModel):
    ApiId: str
    StageName: str
    AccessLogSettings: Optional[AccessLogSettingsTypeDef] = None
    AutoDeploy: Optional[bool] = None
    ClientCertificateId: Optional[str] = None
    DefaultRouteSettings: Optional[RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    Description: Optional[str] = None
    RouteSettings: Optional[Mapping[str, RouteSettingsTypeDef]] = None
    StageVariables: Optional[Mapping[str, str]] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateStageResponseTypeDef(BaseModel):
    AccessLogSettings: AccessLogSettingsTypeDef
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettingsTypeDef
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettingsTypeDef]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStageResponseTypeDef(BaseModel):
    AccessLogSettings: AccessLogSettingsTypeDef
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettingsTypeDef
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettingsTypeDef]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StageTypeDef(BaseModel):
    StageName: str
    AccessLogSettings: Optional[AccessLogSettingsTypeDef] = None
    ApiGatewayManaged: Optional[bool] = None
    AutoDeploy: Optional[bool] = None
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    DefaultRouteSettings: Optional[RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    Description: Optional[str] = None
    LastDeploymentStatusMessage: Optional[str] = None
    LastUpdatedDate: Optional[datetime] = None
    RouteSettings: Optional[Dict[str, RouteSettingsTypeDef]] = None
    StageVariables: Optional[Dict[str, str]] = None
    Tags: Optional[Dict[str, str]] = None

class UpdateStageRequestRequestTypeDef(BaseModel):
    ApiId: str
    StageName: str
    AccessLogSettings: Optional[AccessLogSettingsTypeDef] = None
    AutoDeploy: Optional[bool] = None
    ClientCertificateId: Optional[str] = None
    DefaultRouteSettings: Optional[RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    Description: Optional[str] = None
    RouteSettings: Optional[Mapping[str, RouteSettingsTypeDef]] = None
    StageVariables: Optional[Mapping[str, str]] = None

class UpdateStageResponseTypeDef(BaseModel):
    AccessLogSettings: AccessLogSettingsTypeDef
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: RouteSettingsTypeDef
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, RouteSettingsTypeDef]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentsResponseTypeDef(BaseModel):
    Items: List[DeploymentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNamePaginatorTypeDef(BaseModel):
    DomainName: str
    ApiMappingSelectionExpression: Optional[str] = None
    DomainNameConfigurations: Optional[List[DomainNameConfigurationPaginatorTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationTypeDef] = None
    Tags: Optional[Dict[str, str]] = None

class DomainNameConfigurationTypeDef(BaseModel):
    ApiGatewayDomainName: Optional[str] = None
    CertificateArn: Optional[str] = None
    CertificateName: Optional[str] = None
    CertificateUploadDate: Optional[TimestampTypeDef] = None
    DomainNameStatus: Optional[DomainNameStatusType] = None
    DomainNameStatusMessage: Optional[str] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostedZoneId: Optional[str] = None
    SecurityPolicy: Optional[SecurityPolicyType] = None
    OwnershipVerificationCertificateArn: Optional[str] = None

class GetApisRequestGetApisPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAuthorizersRequestGetAuthorizersPaginateTypeDef(BaseModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDeploymentsRequestGetDeploymentsPaginateTypeDef(BaseModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDomainNamesRequestGetDomainNamesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntegrationResponsesRequestGetIntegrationResponsesPaginateTypeDef(BaseModel):
    ApiId: str
    IntegrationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntegrationsRequestGetIntegrationsPaginateTypeDef(BaseModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetModelsRequestGetModelsPaginateTypeDef(BaseModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRouteResponsesRequestGetRouteResponsesPaginateTypeDef(BaseModel):
    ApiId: str
    RouteId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRoutesRequestGetRoutesPaginateTypeDef(BaseModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetStagesRequestGetStagesPaginateTypeDef(BaseModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntegrationResponsesResponseTypeDef(BaseModel):
    Items: List[IntegrationResponseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelsResponseTypeDef(BaseModel):
    Items: List[ModelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcLinksResponseTypeDef(BaseModel):
    Items: List[VpcLinkTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApisResponsePaginatorTypeDef(BaseModel):
    Items: List[ApiPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApisResponseTypeDef(BaseModel):
    Items: List[ApiTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthorizersResponsePaginatorTypeDef(BaseModel):
    Items: List[AuthorizerPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthorizersResponseTypeDef(BaseModel):
    Items: List[AuthorizerTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationsResponseTypeDef(BaseModel):
    Items: List[IntegrationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouteResponsesResponseTypeDef(BaseModel):
    Items: List[RouteResponseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoutesResponseTypeDef(BaseModel):
    Items: List[RouteTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStagesResponseTypeDef(BaseModel):
    Items: List[StageTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainNamesResponsePaginatorTypeDef(BaseModel):
    Items: List[DomainNamePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainNameRequestRequestTypeDef(BaseModel):
    DomainName: str
    DomainNameConfigurations: Optional[Sequence[DomainNameConfigurationTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInputTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateDomainNameResponseTypeDef(BaseModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNameTypeDef(BaseModel):
    DomainName: str
    ApiMappingSelectionExpression: Optional[str] = None
    DomainNameConfigurations: Optional[List[DomainNameConfigurationTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationTypeDef] = None
    Tags: Optional[Dict[str, str]] = None

class GetDomainNameResponseTypeDef(BaseModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameRequestRequestTypeDef(BaseModel):
    DomainName: str
    DomainNameConfigurations: Optional[Sequence[DomainNameConfigurationTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInputTypeDef] = None

class UpdateDomainNameResponseTypeDef(BaseModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainNamesResponseTypeDef(BaseModel):
    Items: List[DomainNameTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

