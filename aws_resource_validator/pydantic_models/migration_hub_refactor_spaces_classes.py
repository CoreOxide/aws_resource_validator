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
from aws_resource_validator.pydantic_models.migration_hub_refactor_spaces_constants import *

class ApiGatewayProxyConfigTypeDef(BaseValidatorModel):
    ApiGatewayId: Optional[str] = None
    EndpointType: Optional[ApiGatewayEndpointTypeType] = None
    NlbArn: Optional[str] = None
    NlbName: Optional[str] = None
    ProxyUrl: Optional[str] = None
    StageName: Optional[str] = None
    VpcLinkId: Optional[str] = None


class ApiGatewayProxyInputTypeDef(BaseValidatorModel):
    EndpointType: Optional[ApiGatewayEndpointTypeType] = None
    StageName: Optional[str] = None


class ApiGatewayProxySummaryTypeDef(BaseValidatorModel):
    ApiGatewayId: Optional[str] = None
    EndpointType: Optional[ApiGatewayEndpointTypeType] = None
    NlbArn: Optional[str] = None
    NlbName: Optional[str] = None
    ProxyUrl: Optional[str] = None
    StageName: Optional[str] = None
    VpcLinkId: Optional[str] = None


class ErrorResponseTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    AdditionalDetails: Optional[Dict[str, str]] = None
    Code: Optional[ErrorCodeType] = None
    Message: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[ErrorResourceTypeType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateEnvironmentRequestTypeDef(BaseValidatorModel):
    Name: str
    NetworkFabricType: NetworkFabricTypeType
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class DefaultRouteInputTypeDef(BaseValidatorModel):
    ActivationState: Optional[RouteActivationStateType] = None


class UriPathRouteInputOutputTypeDef(BaseValidatorModel):
    ActivationState: RouteActivationStateType
    SourcePath: str
    AppendSourcePath: Optional[bool] = None
    IncludeChildPaths: Optional[bool] = None
    Methods: Optional[List[HttpMethodType]] = None


class LambdaEndpointInputTypeDef(BaseValidatorModel):
    Arn: str


class UrlEndpointInputTypeDef(BaseValidatorModel):
    Url: str
    HealthUrl: Optional[str] = None


class DeleteApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str


class DeleteEnvironmentRequestTypeDef(BaseValidatorModel):
    EnvironmentIdentifier: str


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    Identifier: str


class DeleteRouteRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    RouteIdentifier: str


class DeleteServiceRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ServiceIdentifier: str


class EnvironmentVpcTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    CidrBlocks: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None
    EnvironmentId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None
    VpcId: Optional[str] = None
    VpcName: Optional[str] = None


class GetApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str


class GetEnvironmentRequestTypeDef(BaseValidatorModel):
    EnvironmentIdentifier: str


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetRouteRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    RouteIdentifier: str


class GetServiceRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ServiceIdentifier: str


class LambdaEndpointConfigTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class UrlEndpointConfigTypeDef(BaseValidatorModel):
    HealthUrl: Optional[str] = None
    Url: Optional[str] = None


class LambdaEndpointSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    EnvironmentIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEnvironmentVpcsRequestTypeDef(BaseValidatorModel):
    EnvironmentIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEnvironmentsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoutesRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServicesRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    Policy: str
    ResourceArn: str


class UrlEndpointSummaryTypeDef(BaseValidatorModel):
    HealthUrl: Optional[str] = None
    Url: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateRouteRequestTypeDef(BaseValidatorModel):
    ActivationState: RouteActivationStateType
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    RouteIdentifier: str


class UriPathRouteInputTypeDef(BaseValidatorModel):
    ActivationState: RouteActivationStateType
    SourcePath: str
    AppendSourcePath: Optional[bool] = None
    IncludeChildPaths: Optional[bool] = None
    Methods: Optional[Sequence[HttpMethodType]] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    EnvironmentIdentifier: str
    Name: str
    ProxyType: Literal["API_GATEWAY"]
    VpcId: str
    ApiGatewayProxy: Optional[ApiGatewayProxyInputTypeDef] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ApplicationSummaryTypeDef(BaseValidatorModel):
    ApiGatewayProxy: Optional[ApiGatewayProxySummaryTypeDef] = None
    ApplicationId: Optional[str] = None
    Arn: Optional[str] = None
    CreatedByAccountId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    EnvironmentId: Optional[str] = None
    Error: Optional[ErrorResponseTypeDef] = None
    LastUpdatedTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    ProxyType: Optional[Literal["API_GATEWAY"]] = None
    State: Optional[ApplicationStateType] = None
    Tags: Optional[Dict[str, str]] = None
    VpcId: Optional[str] = None


class EnvironmentSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Description: Optional[str] = None
    EnvironmentId: Optional[str] = None
    Error: Optional[ErrorResponseTypeDef] = None
    LastUpdatedTime: Optional[datetime] = None
    Name: Optional[str] = None
    NetworkFabricType: Optional[NetworkFabricTypeType] = None
    OwnerAccountId: Optional[str] = None
    State: Optional[EnvironmentStateType] = None
    Tags: Optional[Dict[str, str]] = None
    TransitGatewayId: Optional[str] = None


class RouteSummaryTypeDef(BaseValidatorModel):
    AppendSourcePath: Optional[bool] = None
    ApplicationId: Optional[str] = None
    Arn: Optional[str] = None
    CreatedByAccountId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    EnvironmentId: Optional[str] = None
    Error: Optional[ErrorResponseTypeDef] = None
    IncludeChildPaths: Optional[bool] = None
    LastUpdatedTime: Optional[datetime] = None
    Methods: Optional[List[HttpMethodType]] = None
    OwnerAccountId: Optional[str] = None
    PathResourceToId: Optional[Dict[str, str]] = None
    RouteId: Optional[str] = None
    RouteType: Optional[RouteTypeType] = None
    ServiceId: Optional[str] = None
    SourcePath: Optional[str] = None
    State: Optional[RouteStateType] = None
    Tags: Optional[Dict[str, str]] = None


class CreateApplicationResponseTypeDef(BaseValidatorModel):
    ApiGatewayProxy: ApiGatewayProxyInputTypeDef
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    OwnerAccountId: str
    ProxyType: Literal["API_GATEWAY"]
    State: ApplicationStateType
    Tags: Dict[str, str]
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEnvironmentResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedTime: datetime
    Description: str
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    NetworkFabricType: NetworkFabricTypeType
    OwnerAccountId: str
    State: EnvironmentStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    State: ApplicationStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEnvironmentResponseTypeDef(BaseValidatorModel):
    Arn: str
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    State: EnvironmentStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRouteResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    LastUpdatedTime: datetime
    RouteId: str
    ServiceId: str
    State: RouteStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteServiceResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    ServiceId: str
    State: ServiceStateType
    ResponseMetadata: ResponseMetadataTypeDef


class GetApplicationResponseTypeDef(BaseValidatorModel):
    ApiGatewayProxy: ApiGatewayProxyConfigTypeDef
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    EnvironmentId: str
    Error: ErrorResponseTypeDef
    LastUpdatedTime: datetime
    Name: str
    OwnerAccountId: str
    ProxyType: Literal["API_GATEWAY"]
    State: ApplicationStateType
    Tags: Dict[str, str]
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetEnvironmentResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedTime: datetime
    Description: str
    EnvironmentId: str
    Error: ErrorResponseTypeDef
    LastUpdatedTime: datetime
    Name: str
    NetworkFabricType: NetworkFabricTypeType
    OwnerAccountId: str
    State: EnvironmentStateType
    Tags: Dict[str, str]
    TransitGatewayId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRouteResponseTypeDef(BaseValidatorModel):
    AppendSourcePath: bool
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    EnvironmentId: str
    Error: ErrorResponseTypeDef
    IncludeChildPaths: bool
    LastUpdatedTime: datetime
    Methods: List[HttpMethodType]
    OwnerAccountId: str
    PathResourceToId: Dict[str, str]
    RouteId: str
    RouteType: RouteTypeType
    ServiceId: str
    SourcePath: str
    State: RouteStateType
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRouteResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    LastUpdatedTime: datetime
    RouteId: str
    ServiceId: str
    State: RouteStateType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRouteResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    OwnerAccountId: str
    RouteId: str
    RouteType: RouteTypeType
    ServiceId: str
    State: RouteStateType
    Tags: Dict[str, str]
    UriPathRoute: UriPathRouteInputOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateServiceRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EndpointType: ServiceEndpointTypeType
    EnvironmentIdentifier: str
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    LambdaEndpoint: Optional[LambdaEndpointInputTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    UrlEndpoint: Optional[UrlEndpointInputTypeDef] = None
    VpcId: Optional[str] = None


class CreateServiceResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    Description: str
    EndpointType: ServiceEndpointTypeType
    EnvironmentId: str
    LambdaEndpoint: LambdaEndpointInputTypeDef
    LastUpdatedTime: datetime
    Name: str
    OwnerAccountId: str
    ServiceId: str
    State: ServiceStateType
    Tags: Dict[str, str]
    UrlEndpoint: UrlEndpointInputTypeDef
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListEnvironmentVpcsResponseTypeDef(BaseValidatorModel):
    EnvironmentVpcList: List[EnvironmentVpcTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetServiceResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    Description: str
    EndpointType: ServiceEndpointTypeType
    EnvironmentId: str
    Error: ErrorResponseTypeDef
    LambdaEndpoint: LambdaEndpointConfigTypeDef
    LastUpdatedTime: datetime
    Name: str
    OwnerAccountId: str
    ServiceId: str
    State: ServiceStateType
    Tags: Dict[str, str]
    UrlEndpoint: UrlEndpointConfigTypeDef
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    EnvironmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentVpcsRequestPaginateTypeDef(BaseValidatorModel):
    EnvironmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRoutesRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicesRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ServiceSummaryTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    Arn: Optional[str] = None
    CreatedByAccountId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Description: Optional[str] = None
    EndpointType: Optional[ServiceEndpointTypeType] = None
    EnvironmentId: Optional[str] = None
    Error: Optional[ErrorResponseTypeDef] = None
    LambdaEndpoint: Optional[LambdaEndpointSummaryTypeDef] = None
    LastUpdatedTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    ServiceId: Optional[str] = None
    State: Optional[ServiceStateType] = None
    Tags: Optional[Dict[str, str]] = None
    UrlEndpoint: Optional[UrlEndpointSummaryTypeDef] = None
    VpcId: Optional[str] = None


class ListApplicationsResponseTypeDef(BaseValidatorModel):
    ApplicationSummaryList: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEnvironmentsResponseTypeDef(BaseValidatorModel):
    EnvironmentSummaryList: List[EnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRoutesResponseTypeDef(BaseValidatorModel):
    RouteSummaryList: List[RouteSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListServicesResponseTypeDef(BaseValidatorModel):
    ServiceSummaryList: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UriPathRouteInputUnionTypeDef(BaseValidatorModel):
    pass


class CreateRouteRequestTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    RouteType: RouteTypeType
    ServiceIdentifier: str
    ClientToken: Optional[str] = None
    DefaultRoute: Optional[DefaultRouteInputTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    UriPathRoute: Optional[UriPathRouteInputUnionTypeDef] = None


