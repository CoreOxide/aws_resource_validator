from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.migration_hub_refactor_spaces.migration_hub_refactor_spaces_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApiGatewayProxyConfig(BaseValidatorModel):
    ApiGatewayId: Optional[str] = None
    EndpointType: Optional[ApiGatewayEndpointTypeType] = None
    NlbArn: Optional[str] = None
    NlbName: Optional[str] = None
    ProxyUrl: Optional[str] = None
    StageName: Optional[str] = None
    VpcLinkId: Optional[str] = None


class ApiGatewayProxyInput(BaseValidatorModel):
    EndpointType: Optional[ApiGatewayEndpointTypeType] = None
    StageName: Optional[str] = None


class ApiGatewayProxySummary(BaseValidatorModel):
    ApiGatewayId: Optional[str] = None
    EndpointType: Optional[ApiGatewayEndpointTypeType] = None
    NlbArn: Optional[str] = None
    NlbName: Optional[str] = None
    ProxyUrl: Optional[str] = None
    StageName: Optional[str] = None
    VpcLinkId: Optional[str] = None


class ErrorResponse(BaseValidatorModel):
    AccountId: Optional[str] = None
    AdditionalDetails: Optional[Dict[str, str]] = None
    Code: Optional[ErrorCodeType] = None
    Message: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ResourceType: Optional[ErrorResourceTypeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_environment' function.
class CreateEnvironmentRequest(BaseValidatorModel):
    Name: str
    NetworkFabricType: NetworkFabricTypeType
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class DefaultRouteInput(BaseValidatorModel):
    ActivationState: Optional[RouteActivationStateType] = None


class UriPathRouteInputOutput(BaseValidatorModel):
    ActivationState: RouteActivationStateType
    SourcePath: str
    AppendSourcePath: Optional[bool] = None
    IncludeChildPaths: Optional[bool] = None
    Methods: Optional[List[HttpMethodType]] = None


class LambdaEndpointInput(BaseValidatorModel):
    Arn: str


class UrlEndpointInput(BaseValidatorModel):
    Url: str
    HealthUrl: Optional[str] = None


# This class is the input for the 'delete_application' function.
class DeleteApplicationRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str


# This class is the input for the 'delete_environment' function.
class DeleteEnvironmentRequest(BaseValidatorModel):
    EnvironmentIdentifier: str


class DeleteResourcePolicyRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'delete_route' function.
class DeleteRouteRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    RouteIdentifier: str


# This class is the input for the 'delete_service' function.
class DeleteServiceRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ServiceIdentifier: str


class EnvironmentVpc(BaseValidatorModel):
    AccountId: Optional[str] = None
    CidrBlocks: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None
    EnvironmentId: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None
    VpcId: Optional[str] = None
    VpcName: Optional[str] = None


# This class is the input for the 'get_application' function.
class GetApplicationRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str


# This class is the input for the 'get_environment' function.
class GetEnvironmentRequest(BaseValidatorModel):
    EnvironmentIdentifier: str


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_route' function.
class GetRouteRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    RouteIdentifier: str


# This class is the input for the 'get_service' function.
class GetServiceRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    ServiceIdentifier: str


class LambdaEndpointConfig(BaseValidatorModel):
    Arn: Optional[str] = None


class UrlEndpointConfig(BaseValidatorModel):
    HealthUrl: Optional[str] = None
    Url: Optional[str] = None


class LambdaEndpointSummary(BaseValidatorModel):
    Arn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsRequest(BaseValidatorModel):
    EnvironmentIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_environment_vpcs' function.
class ListEnvironmentVpcsRequest(BaseValidatorModel):
    EnvironmentIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_environments' function.
class ListEnvironmentsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_routes' function.
class ListRoutesRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_services' function.
class ListServicesRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class PutResourcePolicyRequest(BaseValidatorModel):
    Policy: str
    ResourceArn: str


class UrlEndpointSummary(BaseValidatorModel):
    HealthUrl: Optional[str] = None
    Url: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_route' function.
class UpdateRouteRequest(BaseValidatorModel):
    ActivationState: RouteActivationStateType
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    RouteIdentifier: str


class UriPathRouteInput(BaseValidatorModel):
    ActivationState: RouteActivationStateType
    SourcePath: str
    AppendSourcePath: Optional[bool] = None
    IncludeChildPaths: Optional[bool] = None
    Methods: Optional[List[HttpMethodType]] = None


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    EnvironmentIdentifier: str
    Name: str
    ProxyType: Literal['API_GATEWAY']
    VpcId: str
    ApiGatewayProxy: Optional[ApiGatewayProxyInput] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ApplicationSummary(BaseValidatorModel):
    ApiGatewayProxy: Optional[ApiGatewayProxySummary] = None
    ApplicationId: Optional[str] = None
    Arn: Optional[str] = None
    CreatedByAccountId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    EnvironmentId: Optional[str] = None
    Error: Optional[ErrorResponse] = None
    LastUpdatedTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    ProxyType: Optional[Literal['API_GATEWAY']] = None
    State: Optional[ApplicationStateType] = None
    Tags: Optional[Dict[str, str]] = None
    VpcId: Optional[str] = None


class EnvironmentSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Description: Optional[str] = None
    EnvironmentId: Optional[str] = None
    Error: Optional[ErrorResponse] = None
    LastUpdatedTime: Optional[datetime] = None
    Name: Optional[str] = None
    NetworkFabricType: Optional[NetworkFabricTypeType] = None
    OwnerAccountId: Optional[str] = None
    State: Optional[EnvironmentStateType] = None
    Tags: Optional[Dict[str, str]] = None
    TransitGatewayId: Optional[str] = None


class RouteSummary(BaseValidatorModel):
    AppendSourcePath: Optional[bool] = None
    ApplicationId: Optional[str] = None
    Arn: Optional[str] = None
    CreatedByAccountId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    EnvironmentId: Optional[str] = None
    Error: Optional[ErrorResponse] = None
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


# This class is the output for the 'create_application' function.
class CreateApplicationResponse(BaseValidatorModel):
    ApiGatewayProxy: ApiGatewayProxyInput
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    OwnerAccountId: str
    ProxyType: Literal['API_GATEWAY']
    State: ApplicationStateType
    Tags: Dict[str, str]
    VpcId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_environment' function.
class CreateEnvironmentResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_application' function.
class DeleteApplicationResponse(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    State: ApplicationStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_environment' function.
class DeleteEnvironmentResponse(BaseValidatorModel):
    Arn: str
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    State: EnvironmentStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_route' function.
class DeleteRouteResponse(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    LastUpdatedTime: datetime
    RouteId: str
    ServiceId: str
    State: RouteStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service' function.
class DeleteServiceResponse(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    EnvironmentId: str
    LastUpdatedTime: datetime
    Name: str
    ServiceId: str
    State: ServiceStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_application' function.
class GetApplicationResponse(BaseValidatorModel):
    ApiGatewayProxy: ApiGatewayProxyConfig
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    EnvironmentId: str
    Error: ErrorResponse
    LastUpdatedTime: datetime
    Name: str
    OwnerAccountId: str
    ProxyType: Literal['API_GATEWAY']
    State: ApplicationStateType
    Tags: Dict[str, str]
    VpcId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_environment' function.
class GetEnvironmentResponse(BaseValidatorModel):
    Arn: str
    CreatedTime: datetime
    Description: str
    EnvironmentId: str
    Error: ErrorResponse
    LastUpdatedTime: datetime
    Name: str
    NetworkFabricType: NetworkFabricTypeType
    OwnerAccountId: str
    State: EnvironmentStateType
    Tags: Dict[str, str]
    TransitGatewayId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_route' function.
class GetRouteResponse(BaseValidatorModel):
    AppendSourcePath: bool
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    EnvironmentId: str
    Error: ErrorResponse
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_route' function.
class UpdateRouteResponse(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    LastUpdatedTime: datetime
    RouteId: str
    ServiceId: str
    State: RouteStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_route' function.
class CreateRouteResponse(BaseValidatorModel):
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
    UriPathRoute: UriPathRouteInputOutput
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_service' function.
class CreateServiceRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EndpointType: ServiceEndpointTypeType
    EnvironmentIdentifier: str
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    LambdaEndpoint: Optional[LambdaEndpointInput] = None
    Tags: Optional[Dict[str, str]] = None
    UrlEndpoint: Optional[UrlEndpointInput] = None
    VpcId: Optional[str] = None


# This class is the output for the 'create_service' function.
class CreateServiceResponse(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    Description: str
    EndpointType: ServiceEndpointTypeType
    EnvironmentId: str
    LambdaEndpoint: LambdaEndpointInput
    LastUpdatedTime: datetime
    Name: str
    OwnerAccountId: str
    ServiceId: str
    State: ServiceStateType
    Tags: Dict[str, str]
    UrlEndpoint: UrlEndpointInput
    VpcId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_environment_vpcs' function.
class ListEnvironmentVpcsResponse(BaseValidatorModel):
    EnvironmentVpcList: List[EnvironmentVpc]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_service' function.
class GetServiceResponse(BaseValidatorModel):
    ApplicationId: str
    Arn: str
    CreatedByAccountId: str
    CreatedTime: datetime
    Description: str
    EndpointType: ServiceEndpointTypeType
    EnvironmentId: str
    Error: ErrorResponse
    LambdaEndpoint: LambdaEndpointConfig
    LastUpdatedTime: datetime
    Name: str
    OwnerAccountId: str
    ServiceId: str
    State: ServiceStateType
    Tags: Dict[str, str]
    UrlEndpoint: UrlEndpointConfig
    VpcId: str
    ResponseMetadata: ResponseMetadata


class ListApplicationsRequestPaginate(BaseValidatorModel):
    EnvironmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentVpcsRequestPaginate(BaseValidatorModel):
    EnvironmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoutesRequestPaginate(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesRequestPaginate(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ServiceSummary(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    Arn: Optional[str] = None
    CreatedByAccountId: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Description: Optional[str] = None
    EndpointType: Optional[ServiceEndpointTypeType] = None
    EnvironmentId: Optional[str] = None
    Error: Optional[ErrorResponse] = None
    LambdaEndpoint: Optional[LambdaEndpointSummary] = None
    LastUpdatedTime: Optional[datetime] = None
    Name: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    ServiceId: Optional[str] = None
    State: Optional[ServiceStateType] = None
    Tags: Optional[Dict[str, str]] = None
    UrlEndpoint: Optional[UrlEndpointSummary] = None
    VpcId: Optional[str] = None

UriPathRouteInputUnion = Union[UriPathRouteInput, UriPathRouteInputOutput]


# This class is the output for the 'list_applications' function.
class ListApplicationsResponse(BaseValidatorModel):
    ApplicationSummaryList: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_environments' function.
class ListEnvironmentsResponse(BaseValidatorModel):
    EnvironmentSummaryList: List[EnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_routes' function.
class ListRoutesResponse(BaseValidatorModel):
    RouteSummaryList: List[RouteSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_services' function.
class ListServicesResponse(BaseValidatorModel):
    ServiceSummaryList: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_route' function.
class CreateRouteRequest(BaseValidatorModel):
    ApplicationIdentifier: str
    EnvironmentIdentifier: str
    RouteType: RouteTypeType
    ServiceIdentifier: str
    ClientToken: Optional[str] = None
    DefaultRoute: Optional[DefaultRouteInput] = None
    Tags: Optional[Dict[str, str]] = None
    UriPathRoute: Optional[UriPathRouteInputUnion] = None