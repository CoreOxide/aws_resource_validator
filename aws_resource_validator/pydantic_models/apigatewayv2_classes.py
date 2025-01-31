from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.apigatewayv2_constants import *

class AccessLogSettingsTypeDef(BaseValidatorModel):
    DestinationArn: Optional[str] = None
    Format: Optional[str] = None

class ApiMappingTypeDef(BaseValidatorModel):
    ApiId: str
    Stage: str
    ApiMappingId: Optional[str] = None
    ApiMappingKey: Optional[str] = None

class CorsPaginatorTypeDef(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[List[str]] = None
    AllowMethods: Optional[List[str]] = None
    AllowOrigins: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None

class CorsTypeDef(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[Sequence[str]] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowOrigins: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None

class JWTConfigurationPaginatorTypeDef(BaseValidatorModel):
    Audience: Optional[List[str]] = None
    Issuer: Optional[str] = None

class JWTConfigurationTypeDef(BaseValidatorModel):
    Audience: Optional[Sequence[str]] = None
    Issuer: Optional[str] = None

class CreateApiMappingRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    DomainName: str
    Stage: str
    ApiMappingKey: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    Description: Optional[str] = None
    StageName: Optional[str] = None

class MutualTlsAuthenticationInputTypeDef(BaseValidatorModel):
    TruststoreUri: Optional[str] = None
    TruststoreVersion: Optional[str] = None

class MutualTlsAuthenticationTypeDef(BaseValidatorModel):
    TruststoreUri: Optional[str] = None
    TruststoreVersion: Optional[str] = None
    TruststoreWarnings: Optional[List[str]] = None

class TlsConfigInputTypeDef(BaseValidatorModel):
    ServerNameToVerify: Optional[str] = None

class CreateIntegrationResponseRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseKey: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    ResponseParameters: Optional[Mapping[str, str]] = None
    ResponseTemplates: Optional[Mapping[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None

class TlsConfigTypeDef(BaseValidatorModel):
    ServerNameToVerify: Optional[str] = None

class CreateModelRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    Name: str
    Schema: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None

class ParameterConstraintsTypeDef(BaseValidatorModel):
    Required: Optional[bool] = None

class RouteSettingsTypeDef(BaseValidatorModel):
    DataTraceEnabled: Optional[bool] = None
    DetailedMetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[LoggingLevelType] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None

class CreateVpcLinkRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteAccessLogSettingsRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    StageName: str

class DeleteApiMappingRequestRequestTypeDef(BaseValidatorModel):
    ApiMappingId: str
    DomainName: str

class DeleteApiRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str

class DeleteAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    AuthorizerId: str

class DeleteCorsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str

class DeleteDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    DeploymentId: str

class DeleteDomainNameRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DeleteIntegrationRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str

class DeleteIntegrationResponseRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str

class DeleteModelRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ModelId: str

class DeleteRouteRequestParameterRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RequestParameterKey: str
    RouteId: str

class DeleteRouteRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str

class DeleteRouteResponseRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str

class DeleteRouteSettingsRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteKey: str
    StageName: str

class DeleteStageRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    StageName: str

class DeleteVpcLinkRequestRequestTypeDef(BaseValidatorModel):
    VpcLinkId: str

class DeploymentTypeDef(BaseValidatorModel):
    AutoDeployed: Optional[bool] = None
    CreatedDate: Optional[datetime] = None
    DeploymentId: Optional[str] = None
    DeploymentStatus: Optional[DeploymentStatusType] = None
    DeploymentStatusMessage: Optional[str] = None
    Description: Optional[str] = None

class DomainNameConfigurationPaginatorTypeDef(BaseValidatorModel):
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

class ExportApiRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    OutputType: JSONYAMLType
    Specification: Literal["OAS30"]
    ExportVersion: Optional[str] = None
    IncludeExtensions: Optional[bool] = None
    StageName: Optional[str] = None

class GetApiMappingRequestRequestTypeDef(BaseValidatorModel):
    ApiMappingId: str
    DomainName: str

class GetApiMappingsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetApiRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetApisRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    AuthorizerId: str

class GetAuthorizersRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    DeploymentId: str

class GetDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetDomainNameRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class GetDomainNamesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetIntegrationRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str

class GetIntegrationResponseRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str

class GetIntegrationResponsesRequestRequestTypeDef(BaseValidatorModel):
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

class GetIntegrationsRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetModelRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ModelId: str

class GetModelTemplateRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ModelId: str

class GetModelsRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ModelTypeDef(BaseValidatorModel):
    Name: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None
    ModelId: Optional[str] = None
    Schema: Optional[str] = None

class GetRouteRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str

class GetRouteResponseRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    RouteResponseId: str

class GetRouteResponsesRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetRoutesRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetStageRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    StageName: str

class GetStagesRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class GetTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class GetVpcLinkRequestRequestTypeDef(BaseValidatorModel):
    VpcLinkId: str

class GetVpcLinksRequestRequestTypeDef(BaseValidatorModel):
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

class ImportApiRequestRequestTypeDef(BaseValidatorModel):
    Body: str
    Basepath: Optional[str] = None
    FailOnWarnings: Optional[bool] = None

class ReimportApiRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    Body: str
    Basepath: Optional[str] = None
    FailOnWarnings: Optional[bool] = None

class ResetAuthorizersCacheRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    StageName: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApiMappingRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ApiMappingId: str
    DomainName: str
    ApiMappingKey: Optional[str] = None
    Stage: Optional[str] = None

class UpdateDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    DeploymentId: str
    Description: Optional[str] = None

class UpdateIntegrationResponseRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    IntegrationResponseId: str
    ContentHandlingStrategy: Optional[ContentHandlingStrategyType] = None
    IntegrationResponseKey: Optional[str] = None
    ResponseParameters: Optional[Mapping[str, str]] = None
    ResponseTemplates: Optional[Mapping[str, str]] = None
    TemplateSelectionExpression: Optional[str] = None

class UpdateModelRequestRequestTypeDef(BaseValidatorModel):
    ApiId: str
    ModelId: str
    ContentType: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    Schema: Optional[str] = None

class UpdateVpcLinkRequestRequestTypeDef(BaseValidatorModel):
    VpcLinkId: str
    Name: Optional[str] = None

class ApiPaginatorTypeDef(BaseValidatorModel):
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

class ApiTypeDef(BaseValidatorModel):
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

class CreateApiRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateApiRequestRequestTypeDef(BaseValidatorModel):
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

class AuthorizerPaginatorTypeDef(BaseValidatorModel):
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
    JwtConfiguration: Optional[JWTConfigurationTypeDef] = None

class CreateAuthorizerRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateAuthorizerRequestRequestTypeDef(BaseValidatorModel):
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
    JwtConfiguration: JWTConfigurationTypeDef
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiResponseTypeDef(BaseValidatorModel):
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
    JwtConfiguration: JWTConfigurationTypeDef
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

class ReimportApiResponseTypeDef(BaseValidatorModel):
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
    JwtConfiguration: JWTConfigurationTypeDef
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

class CreateIntegrationRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateIntegrationRequestRequestTypeDef(BaseValidatorModel):
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

class CreateRouteRequestRequestTypeDef(BaseValidatorModel):
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

class CreateRouteResponseRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateRouteRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateRouteResponseRequestRequestTypeDef(BaseValidatorModel):
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

class CreateStageRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateStageRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNamePaginatorTypeDef(BaseValidatorModel):
    DomainName: str
    ApiMappingSelectionExpression: Optional[str] = None
    DomainNameConfigurations: Optional[List[DomainNameConfigurationPaginatorTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationTypeDef] = None
    Tags: Optional[Dict[str, str]] = None

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

class GetApisRequestGetApisPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAuthorizersRequestGetAuthorizersPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDeploymentsRequestGetDeploymentsPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDomainNamesRequestGetDomainNamesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntegrationResponsesRequestGetIntegrationResponsesPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    IntegrationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntegrationsRequestGetIntegrationsPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetModelsRequestGetModelsPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRouteResponsesRequestGetRouteResponsesPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    RouteId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRoutesRequestGetRoutesPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetStagesRequestGetStagesPaginateTypeDef(BaseValidatorModel):
    ApiId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIntegrationResponsesResponseTypeDef(BaseValidatorModel):
    Items: List[IntegrationResponseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelsResponseTypeDef(BaseValidatorModel):
    Items: List[ModelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcLinksResponseTypeDef(BaseValidatorModel):
    Items: List[VpcLinkTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApisResponsePaginatorTypeDef(BaseValidatorModel):
    Items: List[ApiPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApisResponseTypeDef(BaseValidatorModel):
    Items: List[ApiTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthorizersResponsePaginatorTypeDef(BaseValidatorModel):
    Items: List[AuthorizerPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthorizersResponseTypeDef(BaseValidatorModel):
    Items: List[AuthorizerTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationsResponseTypeDef(BaseValidatorModel):
    Items: List[IntegrationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRouteResponsesResponseTypeDef(BaseValidatorModel):
    Items: List[RouteResponseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoutesResponseTypeDef(BaseValidatorModel):
    Items: List[RouteTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStagesResponseTypeDef(BaseValidatorModel):
    Items: List[StageTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainNamesResponsePaginatorTypeDef(BaseValidatorModel):
    Items: List[DomainNamePaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainNameRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DomainNameConfigurations: Optional[Sequence[DomainNameConfigurationTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInputTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateDomainNameResponseTypeDef(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainNameTypeDef(BaseValidatorModel):
    DomainName: str
    ApiMappingSelectionExpression: Optional[str] = None
    DomainNameConfigurations: Optional[List[DomainNameConfigurationTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationTypeDef] = None
    Tags: Optional[Dict[str, str]] = None

class GetDomainNameResponseTypeDef(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DomainNameConfigurations: Optional[Sequence[DomainNameConfigurationTypeDef]] = None
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInputTypeDef] = None

class UpdateDomainNameResponseTypeDef(BaseValidatorModel):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List[DomainNameConfigurationTypeDef]
    MutualTlsAuthentication: MutualTlsAuthenticationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainNamesResponseTypeDef(BaseValidatorModel):
    Items: List[DomainNameTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

