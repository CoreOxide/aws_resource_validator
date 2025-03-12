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
from aws_resource_validator.pydantic_models.apigatewayv2_constants import *

class AccessLogSettingsTypeDef(BaseValidatorModel):
    DestinationArn: Optional[str] = None
    Format: Optional[str] = None


class ApiMappingTypeDef(BaseValidatorModel):
    ApiId: str
    Stage: str
    ApiMappingId: Optional[str] = None
    ApiMappingKey: Optional[str] = None


class CorsOutputTypeDef(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[List[str]] = None
    AllowMethods: Optional[List[str]] = None
    AllowOrigins: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None


class JWTConfigurationOutputTypeDef(BaseValidatorModel):
    Audience: Optional[List[str]] = None
    Issuer: Optional[str] = None


class CorsTypeDef(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[Sequence[str]] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowOrigins: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None


class CreateApiMappingRequestTypeDef(BaseValidatorModel):
    ApiId: str
    DomainName: str
    Stage: str
    ApiMappingKey: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateDeploymentRequestTypeDef(BaseValidatorModel):
    ApiId: str
    Description: Optional[str] = None
    StageName: Optional[str] = None


class MutualTlsAuthenticationInputTypeDef(BaseValidatorModel):
    TruststoreUri: Optional[str] = None
    TruststoreVersion: Optional[str] = None


class DomainNameConfigurationOutputTypeDef(BaseValidatorModel):
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


class MutualTlsAuthenticationTypeDef(BaseValidatorModel):
    TruststoreUri: Optional[str] = None
    TruststoreVersion: Optional[str] = None
    TruststoreWarnings: Optional[List[str]] = None


class TlsConfigInputTypeDef(BaseValidatorModel):
    ServerNameToVerify: Optional[str] = None


class CreateIntegrationResponseRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseKey: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    ResponseParameters: Optional[Mapping[str, str]] = None
    ResponseTemplates: Optional[Mapping[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None


class TlsConfigTypeDef(BaseValidatorModel):
    ServerNameToVerify: Optional[str] = None


class CreateModelRequestTypeDef(BaseValidatorModel):
    ApiId: str
    Name: str
    Schema: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None


class RouteSettingsTypeDef(BaseValidatorModel):
    DataTraceEnabled: Optional[bool] = None
    DetailedMetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[LoggingLevelType] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None


class CreateVpcLinkRequestTypeDef(BaseValidatorModel):
    Name: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class DeleteAccessLogSettingsRequestTypeDef(BaseValidatorModel):
    ApiId: str
    StageName: str


class DeleteApiMappingRequestTypeDef(BaseValidatorModel):
    ApiMappingId: str
    DomainName: str


class DeleteApiRequestTypeDef(BaseValidatorModel):
    ApiId: str


class DeleteAuthorizerRequestTypeDef(BaseValidatorModel):
    ApiId: str
    AuthorizerId: str


class DeleteCorsConfigurationRequestTypeDef(BaseValidatorModel):
    ApiId: str


class DeleteDeploymentRequestTypeDef(BaseValidatorModel):
    ApiId: str
    DeploymentId: str


class DeleteDomainNameRequestTypeDef(BaseValidatorModel):
    DomainName: str


class DeleteIntegrationRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str


class DeleteIntegrationResponseRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str


class DeleteModelRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ModelId: str


class DeleteRouteRequestParameterRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RequestParameterKey: str
    RouteId: str


class DeleteRouteRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str


class DeleteRouteResponseRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str


class DeleteRouteSettingsRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteKey: str
    StageName: str


class DeleteStageRequestTypeDef(BaseValidatorModel):
    ApiId: str
    StageName: str


class DeleteVpcLinkRequestTypeDef(BaseValidatorModel):
    VpcLinkId: str


class DeploymentTypeDef(BaseValidatorModel):
    AutoDeployed: Optional[bool] = None
    CreatedDate: Optional[datetime] = None
    DeploymentId: Optional[str] = None
    DeploymentStatus: Optional[DeploymentStatusType] = None
    DeploymentStatusMessage: Optional[str] = None
    Description: Optional[str] = None


class ExportApiRequestTypeDef(BaseValidatorModel):
    ApiId: str
    OutputType: JSONYAMLType
    Specification: Literal["OAS30"]
    ExportVersion: Optional[str] = None
    IncludeExtensions: Optional[bool] = None
    StageName: Optional[str] = None


class GetApiMappingRequestTypeDef(BaseValidatorModel):
    ApiMappingId: str
    DomainName: str


class GetApiMappingsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetApiRequestTypeDef(BaseValidatorModel):
    ApiId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetApisRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetAuthorizerRequestTypeDef(BaseValidatorModel):
    ApiId: str
    AuthorizerId: str


class GetAuthorizersRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetDeploymentRequestTypeDef(BaseValidatorModel):
    ApiId: str
    DeploymentId: str


class GetDeploymentsRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetDomainNameRequestTypeDef(BaseValidatorModel):
    DomainName: str


class GetDomainNamesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetIntegrationRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str


class GetIntegrationResponseRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str


class GetIntegrationResponsesRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class IntegrationResponseTypeDef(BaseValidatorModel):
    IntegrationResponseKey: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    IntegrationResponseId: Optional[str] = None
    ResponseParameters: Optional[Dict[str, str]] = None
    ResponseTemplates: Optional[Dict[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None


class GetIntegrationsRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetModelRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ModelId: str


class GetModelTemplateRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ModelId: str


class GetModelsRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ModelTypeDef(BaseValidatorModel):
    Name: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None
    ModelId: Optional[str] = None
    Schema: Optional[str] = None


class GetRouteRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str


class GetRouteResponseRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str


class GetRouteResponsesRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetRoutesRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetStageRequestTypeDef(BaseValidatorModel):
    ApiId: str
    StageName: str


class GetStagesRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class GetTagsRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class GetVpcLinkRequestTypeDef(BaseValidatorModel):
    VpcLinkId: str


class GetVpcLinksRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class VpcLinkTypeDef(BaseValidatorModel):
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    VpcLinkId: str
    CreatedDate: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None
    VpcLinkStatus: Optional[VpcLinkStatusType] = None
    VpcLinkStatusMessage: Optional[str] = None
    VpcLinkVersion: Optional[Literal["V2"]] = None


class ImportApiRequestTypeDef(BaseValidatorModel):
    Body: str
    Basepath: Optional[str] = None
    FailOnWarnings: Optional[bool] = None


class JWTConfigurationTypeDef(BaseValidatorModel):
    Audience: Optional[Sequence[str]] = None
    Issuer: Optional[str] = None


class ReimportApiRequestTypeDef(BaseValidatorModel):
    ApiId: str
    Body: str
    Basepath: Optional[str] = None
    FailOnWarnings: Optional[bool] = None


class ResetAuthorizersCacheRequestTypeDef(BaseValidatorModel):
    ApiId: str
    StageName: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Optional[Mapping[str, str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateApiMappingRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    DomainName: str
    ApiMappingKey: Optional[str] = None
    Stage: Optional[str] = None


class UpdateDeploymentRequestTypeDef(BaseValidatorModel):
    ApiId: str
    DeploymentId: str
    Description: Optional[str] = None


class UpdateIntegrationResponseRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    IntegrationResponseKey: Optional[str] = None
    ResponseParameters: Optional[Mapping[str, str]] = None
    ResponseTemplates: Optional[Mapping[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None


class UpdateModelRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ModelId: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    Schema: Optional[str] = None


class UpdateVpcLinkRequestTypeDef(BaseValidatorModel):
    VpcLinkId: str
    Name: Optional[str] = None


class ApiTypeDef(BaseValidatorModel):
    Name: str
    ProtocolType: ProtocolTypeType
    RouteSelectionExpression: str
    ApiEndpoint: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsOutputTypeDef] = None
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    ImportInfo: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    Version: Optional[str] = None
    Warnings: Optional[List[str]] = None


class AuthorizerTypeDef(BaseValidatorModel):
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
    JwtConfiguration: Optional[JWTConfigurationOutputTypeDef] = None


class CreateApiMappingResponseTypeDef(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateApiResponseTypeDef(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
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


class CreateAuthorizerResponseTypeDef(BaseValidatorModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutputTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDeploymentResponseTypeDef(BaseValidatorModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIntegrationResponseResponseTypeDef(BaseValidatorModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateModelResponseTypeDef(BaseValidatorModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVpcLinkResponseTypeDef(BaseValidatorModel):
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


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ExportApiResponseTypeDef(BaseValidatorModel):
    body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetApiMappingResponseTypeDef(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetApiMappingsResponseTypeDef(BaseValidatorModel):
    Items: List[ApiMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetApiResponseTypeDef(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
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


class GetAuthorizerResponseTypeDef(BaseValidatorModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutputTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeploymentResponseTypeDef(BaseValidatorModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetIntegrationResponseResponseTypeDef(BaseValidatorModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetModelResponseTypeDef(BaseValidatorModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetModelTemplateResponseTypeDef(BaseValidatorModel):
    Value: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTagsResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetVpcLinkResponseTypeDef(BaseValidatorModel):
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


class ImportApiResponseTypeDef(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
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


class ReimportApiResponseTypeDef(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
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


class UpdateApiMappingResponseTypeDef(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApiResponseTypeDef(BaseValidatorModel):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: CorsOutputTypeDef
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


class UpdateAuthorizerResponseTypeDef(BaseValidatorModel):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerTypeType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: JWTConfigurationOutputTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDeploymentResponseTypeDef(BaseValidatorModel):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatusType
    DeploymentStatusMessage: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIntegrationResponseResponseTypeDef(BaseValidatorModel):
    ContentHandlingStrategy: ContentHandlingStrategyType
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateModelResponseTypeDef(BaseValidatorModel):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVpcLinkResponseTypeDef(BaseValidatorModel):
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


class CreateDomainNameResponseTypeDef(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutputTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DomainNameTypeDef(BaseValidatorModel):
    DomainName: str
    ApiMappingSelectionExpression: Optional[str] = None
    DomainNameConfigurations: Optional[List[DomainNameConfigurationOutputTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationTypeDef] = None
    Tags: Optional[Dict[str, str]] = None


class GetDomainNameResponseTypeDef(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutputTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDomainNameResponseTypeDef(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationOutputTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIntegrationRequestTypeDef(BaseValidatorModel):
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


class UpdateIntegrationRequestTypeDef(BaseValidatorModel):
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


class CreateIntegrationResultTypeDef(BaseValidatorModel):
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


class GetIntegrationResultTypeDef(BaseValidatorModel):
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


class IntegrationTypeDef(BaseValidatorModel):
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


class UpdateIntegrationResultTypeDef(BaseValidatorModel):
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


class ParameterConstraintsTypeDef(BaseValidatorModel):
    pass


class CreateRouteRequestTypeDef(BaseValidatorModel):
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


class CreateRouteResponseRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseKey: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Mapping[str, str]] = None
    ResponseParameters: Optional[Mapping[str, ParameterConstraintsTypeDef]] = None


class CreateRouteResponseResponseTypeDef(BaseValidatorModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRouteResultTypeDef(BaseValidatorModel):
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


class GetRouteResponseResponseTypeDef(BaseValidatorModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRouteResultTypeDef(BaseValidatorModel):
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


class RouteResponseTypeDef(BaseValidatorModel):
    RouteResponseKey: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Dict[str, str]] = None
    ResponseParameters: Optional[Dict[str, ParameterConstraintsTypeDef]] = None
    RouteResponseId: Optional[str] = None


class RouteTypeDef(BaseValidatorModel):
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


class UpdateRouteRequestTypeDef(BaseValidatorModel):
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


class UpdateRouteResponseRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str
    ModelSelectionExpression: Optional[str] = None
    ResponseModels: Optional[Mapping[str, str]] = None
    ResponseParameters: Optional[Mapping[str, ParameterConstraintsTypeDef]] = None
    RouteResponseKey: Optional[str] = None


class UpdateRouteResponseResponseTypeDef(BaseValidatorModel):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, ParameterConstraintsTypeDef]
    RouteResponseId: str
    RouteResponseKey: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRouteResultTypeDef(BaseValidatorModel):
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


class CreateStageRequestTypeDef(BaseValidatorModel):
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


class CreateStageResponseTypeDef(BaseValidatorModel):
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


class GetStageResponseTypeDef(BaseValidatorModel):
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


class StageTypeDef(BaseValidatorModel):
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


class UpdateStageRequestTypeDef(BaseValidatorModel):
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


class UpdateStageResponseTypeDef(BaseValidatorModel):
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


class GetDeploymentsResponseTypeDef(BaseValidatorModel):
    Items: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DomainNameConfigurationTypeDef(BaseValidatorModel):
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


class GetApisRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetAuthorizersRequestPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDeploymentsRequestPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDomainNamesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetIntegrationResponsesRequestPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetIntegrationsRequestPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetModelsRequestPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRouteResponsesRequestPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRoutesRequestPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetStagesRequestPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetIntegrationResponsesResponseTypeDef(BaseValidatorModel):
    Items: List[IntegrationResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetModelsResponseTypeDef(BaseValidatorModel):
    Items: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetVpcLinksResponseTypeDef(BaseValidatorModel):
    Items: List[VpcLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetApisResponseTypeDef(BaseValidatorModel):
    Items: List[ApiTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetAuthorizersResponseTypeDef(BaseValidatorModel):
    Items: List[AuthorizerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CorsUnionTypeDef(BaseValidatorModel):
    pass


class CreateApiRequestTypeDef(BaseValidatorModel):
    Name: str
    ProtocolType: ProtocolTypeType
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsUnionTypeDef] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    RouteKey: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Target: Optional[str] = None
    Version: Optional[str] = None


class UpdateApiRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[CorsUnionTypeDef] = None
    CredentialsArn: Optional[str] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = None
    DisableExecuteApiEndpoint: Optional[bool] = None
    Name: Optional[str] = None
    RouteKey: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    Target: Optional[str] = None
    Version: Optional[str] = None


class GetDomainNamesResponseTypeDef(BaseValidatorModel):
    Items: List[DomainNameTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetIntegrationsResponseTypeDef(BaseValidatorModel):
    Items: List[IntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetRouteResponsesResponseTypeDef(BaseValidatorModel):
    Items: List[RouteResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetRoutesResponseTypeDef(BaseValidatorModel):
    Items: List[RouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetStagesResponseTypeDef(BaseValidatorModel):
    Items: List[StageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class JWTConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateAuthorizerRequestTypeDef(BaseValidatorModel):
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
    JwtConfiguration: Optional[JWTConfigurationUnionTypeDef] = None


class UpdateAuthorizerRequestTypeDef(BaseValidatorModel):
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
    JwtConfiguration: Optional[JWTConfigurationUnionTypeDef] = None
    Name: Optional[str] = None


class DomainNameConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDomainNameRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DomainNameConfigurations: Optional[Sequence[DomainNameConfigurationUnionTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInputTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateDomainNameRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DomainNameConfigurations: Optional[Sequence[DomainNameConfigurationUnionTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInputTypeDef] = None


