from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.appmesh.appmesh_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AwsCloudMapInstanceAttribute(BaseValidatorModel):
    key: str
    value: str


class ListenerTlsFileCertificate(BaseValidatorModel):
    certificateChain: str
    privateKey: str


class ListenerTlsSdsCertificate(BaseValidatorModel):
    secretName: str


class TagRef(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'delete_gateway_route' function.
class DeleteGatewayRouteInput(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'delete_mesh' function.
class DeleteMeshInput(BaseValidatorModel):
    meshName: str


# This class is the input for the 'delete_route' function.
class DeleteRouteInput(BaseValidatorModel):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'delete_virtual_gateway' function.
class DeleteVirtualGatewayInput(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'delete_virtual_node' function.
class DeleteVirtualNodeInput(BaseValidatorModel):
    meshName: str
    virtualNodeName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'delete_virtual_router' function.
class DeleteVirtualRouterInput(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'delete_virtual_service' function.
class DeleteVirtualServiceInput(BaseValidatorModel):
    meshName: str
    virtualServiceName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'describe_gateway_route' function.
class DescribeGatewayRouteInput(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'describe_mesh' function.
class DescribeMeshInput(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'describe_route' function.
class DescribeRouteInput(BaseValidatorModel):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'describe_virtual_gateway' function.
class DescribeVirtualGatewayInput(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'describe_virtual_node' function.
class DescribeVirtualNodeInput(BaseValidatorModel):
    meshName: str
    virtualNodeName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'describe_virtual_router' function.
class DescribeVirtualRouterInput(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None


# This class is the input for the 'describe_virtual_service' function.
class DescribeVirtualServiceInput(BaseValidatorModel):
    meshName: str
    virtualServiceName: str
    meshOwner: Optional[str] = None


class DnsServiceDiscovery(BaseValidatorModel):
    hostname: str
    ipPreference: Optional[IpPreferenceType] = None
    responseType: Optional[DnsResponseTypeType] = None


class Duration(BaseValidatorModel):
    unit: Optional[DurationUnitType] = None
    value: Optional[int] = None


class EgressFilter(BaseValidatorModel):
    type: EgressFilterTypeType


class GatewayRouteStatus(BaseValidatorModel):
    status: GatewayRouteStatusCodeType


class ResourceMetadata(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshOwner: str
    resourceOwner: str
    uid: str
    version: int


class GatewayRouteHostnameMatch(BaseValidatorModel):
    exact: Optional[str] = None
    suffix: Optional[str] = None


class GatewayRouteHostnameRewrite(BaseValidatorModel):
    defaultTargetHostname: Optional[DefaultGatewayRouteRewriteType] = None


class GatewayRouteRef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    gatewayRouteName: str
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str


class GatewayRouteVirtualService(BaseValidatorModel):
    virtualServiceName: str


class MatchRange(BaseValidatorModel):
    end: int
    start: int


class WeightedTarget(BaseValidatorModel):
    virtualNode: str
    weight: int
    port: Optional[int] = None


class HealthCheckPolicy(BaseValidatorModel):
    healthyThreshold: int
    intervalMillis: int
    protocol: PortProtocolType
    timeoutMillis: int
    unhealthyThreshold: int
    path: Optional[str] = None
    port: Optional[int] = None


class HttpPathMatch(BaseValidatorModel):
    exact: Optional[str] = None
    regex: Optional[str] = None


class HttpGatewayRoutePathRewrite(BaseValidatorModel):
    exact: Optional[str] = None


class HttpGatewayRoutePrefixRewrite(BaseValidatorModel):
    defaultPrefix: Optional[DefaultGatewayRouteRewriteType] = None
    value: Optional[str] = None


class QueryParameterMatch(BaseValidatorModel):
    exact: Optional[str] = None


class JsonFormatRef(BaseValidatorModel):
    key: str
    value: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_gateway_routes' function.
class ListGatewayRoutesInput(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_meshes' function.
class ListMeshesInput(BaseValidatorModel):
    limit: Optional[int] = None
    nextToken: Optional[str] = None


class MeshRef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int


# This class is the input for the 'list_routes' function.
class ListRoutesInput(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None


class RouteRef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    routeName: str
    version: int
    virtualRouterName: str


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_virtual_gateways' function.
class ListVirtualGatewaysInput(BaseValidatorModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None


class VirtualGatewayRef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str


# This class is the input for the 'list_virtual_nodes' function.
class ListVirtualNodesInput(BaseValidatorModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None


class VirtualNodeRef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualNodeName: str


# This class is the input for the 'list_virtual_routers' function.
class ListVirtualRoutersInput(BaseValidatorModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None


class VirtualRouterRef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualRouterName: str


# This class is the input for the 'list_virtual_services' function.
class ListVirtualServicesInput(BaseValidatorModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None


class VirtualServiceRef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualServiceName: str


class PortMapping(BaseValidatorModel):
    port: int
    protocol: PortProtocolType


class ListenerTlsAcmCertificate(BaseValidatorModel):
    certificateArn: str


class TlsValidationContextFileTrust(BaseValidatorModel):
    certificateChain: str


class TlsValidationContextSdsTrust(BaseValidatorModel):
    secretName: str


class MeshStatus(BaseValidatorModel):
    status: Optional[MeshStatusCodeType] = None


class MeshServiceDiscovery(BaseValidatorModel):
    ipPreference: Optional[IpPreferenceType] = None


class RouteStatus(BaseValidatorModel):
    status: RouteStatusCodeType


class SubjectAlternativeNameMatchersOutput(BaseValidatorModel):
    exact: List[str]


class SubjectAlternativeNameMatchers(BaseValidatorModel):
    exact: List[str]


class TcpRouteMatch(BaseValidatorModel):
    port: Optional[int] = None


class TlsValidationContextAcmTrustOutput(BaseValidatorModel):
    certificateAuthorityArns: List[str]


class TlsValidationContextAcmTrust(BaseValidatorModel):
    certificateAuthorityArns: List[str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class VirtualGatewayListenerTlsFileCertificate(BaseValidatorModel):
    certificateChain: str
    privateKey: str


class VirtualGatewayListenerTlsSdsCertificate(BaseValidatorModel):
    secretName: str


class VirtualGatewayGrpcConnectionPool(BaseValidatorModel):
    maxRequests: int


class VirtualGatewayHttp2ConnectionPool(BaseValidatorModel):
    maxRequests: int


class VirtualGatewayHttpConnectionPool(BaseValidatorModel):
    maxConnections: int
    maxPendingRequests: Optional[int] = None


class VirtualGatewayStatus(BaseValidatorModel):
    status: VirtualGatewayStatusCodeType


class VirtualGatewayHealthCheckPolicy(BaseValidatorModel):
    healthyThreshold: int
    intervalMillis: int
    protocol: VirtualGatewayPortProtocolType
    timeoutMillis: int
    unhealthyThreshold: int
    path: Optional[str] = None
    port: Optional[int] = None


class VirtualGatewayPortMapping(BaseValidatorModel):
    port: int
    protocol: VirtualGatewayPortProtocolType


class VirtualGatewayListenerTlsAcmCertificate(BaseValidatorModel):
    certificateArn: str


class VirtualGatewayTlsValidationContextFileTrust(BaseValidatorModel):
    certificateChain: str


class VirtualGatewayTlsValidationContextSdsTrust(BaseValidatorModel):
    secretName: str


class VirtualGatewayTlsValidationContextAcmTrustOutput(BaseValidatorModel):
    certificateAuthorityArns: List[str]


class VirtualGatewayTlsValidationContextAcmTrust(BaseValidatorModel):
    certificateAuthorityArns: List[str]


class VirtualNodeGrpcConnectionPool(BaseValidatorModel):
    maxRequests: int


class VirtualNodeHttp2ConnectionPool(BaseValidatorModel):
    maxRequests: int


class VirtualNodeHttpConnectionPool(BaseValidatorModel):
    maxConnections: int
    maxPendingRequests: Optional[int] = None


class VirtualNodeTcpConnectionPool(BaseValidatorModel):
    maxConnections: int


class VirtualNodeStatus(BaseValidatorModel):
    status: VirtualNodeStatusCodeType


class VirtualNodeServiceProvider(BaseValidatorModel):
    virtualNodeName: str


class VirtualRouterStatus(BaseValidatorModel):
    status: VirtualRouterStatusCodeType


class VirtualRouterServiceProvider(BaseValidatorModel):
    virtualRouterName: str


class VirtualServiceStatus(BaseValidatorModel):
    status: VirtualServiceStatusCodeType


class AwsCloudMapServiceDiscoveryOutput(BaseValidatorModel):
    namespaceName: str
    serviceName: str
    attributes: Optional[List[AwsCloudMapInstanceAttribute]] = None
    ipPreference: Optional[IpPreferenceType] = None


class AwsCloudMapServiceDiscovery(BaseValidatorModel):
    namespaceName: str
    serviceName: str
    attributes: Optional[List[AwsCloudMapInstanceAttribute]] = None
    ipPreference: Optional[IpPreferenceType] = None


class ClientTlsCertificate(BaseValidatorModel):
    file: Optional[ListenerTlsFileCertificate] = None
    sds: Optional[ListenerTlsSdsCertificate] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: List[TagRef]


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: List[TagRef]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GrpcRetryPolicyOutput(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: Duration
    grpcRetryEvents: Optional[List[GrpcRetryPolicyEventType]] = None
    httpRetryEvents: Optional[List[str]] = None
    tcpRetryEvents: Optional[List[Literal['connection-error']]] = None


class GrpcRetryPolicy(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: Duration
    grpcRetryEvents: Optional[List[GrpcRetryPolicyEventType]] = None
    httpRetryEvents: Optional[List[str]] = None
    tcpRetryEvents: Optional[List[Literal['connection-error']]] = None


class GrpcTimeout(BaseValidatorModel):
    idle: Optional[Duration] = None
    perRequest: Optional[Duration] = None


class HttpRetryPolicyOutput(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: Duration
    httpRetryEvents: Optional[List[str]] = None
    tcpRetryEvents: Optional[List[Literal['connection-error']]] = None


class HttpRetryPolicy(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: Duration
    httpRetryEvents: Optional[List[str]] = None
    tcpRetryEvents: Optional[List[Literal['connection-error']]] = None


class HttpTimeout(BaseValidatorModel):
    idle: Optional[Duration] = None
    perRequest: Optional[Duration] = None


class OutlierDetection(BaseValidatorModel):
    baseEjectionDuration: Duration
    interval: Duration
    maxEjectionPercent: int
    maxServerErrors: int


class TcpTimeout(BaseValidatorModel):
    idle: Optional[Duration] = None


class GrpcGatewayRouteRewrite(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameRewrite] = None


# This class is the output for the 'list_gateway_routes' function.
class ListGatewayRoutesOutput(BaseValidatorModel):
    gatewayRoutes: List[GatewayRouteRef]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GatewayRouteTarget(BaseValidatorModel):
    virtualService: GatewayRouteVirtualService
    port: Optional[int] = None


class GrpcMetadataMatchMethod(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRange] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None


class GrpcRouteMetadataMatchMethod(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRange] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None


class HeaderMatchMethod(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRange] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None


class GrpcRouteActionOutput(BaseValidatorModel):
    weightedTargets: List[WeightedTarget]


class GrpcRouteAction(BaseValidatorModel):
    weightedTargets: List[WeightedTarget]


class HttpRouteActionOutput(BaseValidatorModel):
    weightedTargets: List[WeightedTarget]


class HttpRouteAction(BaseValidatorModel):
    weightedTargets: List[WeightedTarget]


class TcpRouteActionOutput(BaseValidatorModel):
    weightedTargets: List[WeightedTarget]


class TcpRouteAction(BaseValidatorModel):
    weightedTargets: List[WeightedTarget]


class HttpGatewayRouteRewrite(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameRewrite] = None
    path: Optional[HttpGatewayRoutePathRewrite] = None
    prefix: Optional[HttpGatewayRoutePrefixRewrite] = None


class HttpQueryParameter(BaseValidatorModel):
    name: str
    match: Optional[QueryParameterMatch] = None


class LoggingFormatOutput(BaseValidatorModel):
    json: Optional[List[JsonFormatRef]] = None
    text: Optional[str] = None


class LoggingFormat(BaseValidatorModel):
    json: Optional[List[JsonFormatRef]] = None
    text: Optional[str] = None


class ListGatewayRoutesInputPaginate(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMeshesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoutesInputPaginate(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceInputPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVirtualGatewaysInputPaginate(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVirtualNodesInputPaginate(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVirtualRoutersInputPaginate(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVirtualServicesInputPaginate(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_meshes' function.
class ListMeshesOutput(BaseValidatorModel):
    meshes: List[MeshRef]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_routes' function.
class ListRoutesOutput(BaseValidatorModel):
    routes: List[RouteRef]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_virtual_gateways' function.
class ListVirtualGatewaysOutput(BaseValidatorModel):
    virtualGateways: List[VirtualGatewayRef]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_virtual_nodes' function.
class ListVirtualNodesOutput(BaseValidatorModel):
    virtualNodes: List[VirtualNodeRef]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_virtual_routers' function.
class ListVirtualRoutersOutput(BaseValidatorModel):
    virtualRouters: List[VirtualRouterRef]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_virtual_services' function.
class ListVirtualServicesOutput(BaseValidatorModel):
    virtualServices: List[VirtualServiceRef]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class VirtualRouterListener(BaseValidatorModel):
    portMapping: PortMapping


class ListenerTlsCertificate(BaseValidatorModel):
    acm: Optional[ListenerTlsAcmCertificate] = None
    file: Optional[ListenerTlsFileCertificate] = None
    sds: Optional[ListenerTlsSdsCertificate] = None


class ListenerTlsValidationContextTrust(BaseValidatorModel):
    file: Optional[TlsValidationContextFileTrust] = None
    sds: Optional[TlsValidationContextSdsTrust] = None


class MeshSpec(BaseValidatorModel):
    egressFilter: Optional[EgressFilter] = None
    serviceDiscovery: Optional[MeshServiceDiscovery] = None


class SubjectAlternativeNamesOutput(BaseValidatorModel):
    match: SubjectAlternativeNameMatchersOutput


class SubjectAlternativeNames(BaseValidatorModel):
    match: SubjectAlternativeNameMatchers


class TlsValidationContextTrustOutput(BaseValidatorModel):
    acm: Optional[TlsValidationContextAcmTrustOutput] = None
    file: Optional[TlsValidationContextFileTrust] = None
    sds: Optional[TlsValidationContextSdsTrust] = None


class TlsValidationContextTrust(BaseValidatorModel):
    acm: Optional[TlsValidationContextAcmTrust] = None
    file: Optional[TlsValidationContextFileTrust] = None
    sds: Optional[TlsValidationContextSdsTrust] = None


class VirtualGatewayClientTlsCertificate(BaseValidatorModel):
    file: Optional[VirtualGatewayListenerTlsFileCertificate] = None
    sds: Optional[VirtualGatewayListenerTlsSdsCertificate] = None


class VirtualGatewayConnectionPool(BaseValidatorModel):
    grpc: Optional[VirtualGatewayGrpcConnectionPool] = None
    http: Optional[VirtualGatewayHttpConnectionPool] = None
    http2: Optional[VirtualGatewayHttp2ConnectionPool] = None


class VirtualGatewayListenerTlsCertificate(BaseValidatorModel):
    acm: Optional[VirtualGatewayListenerTlsAcmCertificate] = None
    file: Optional[VirtualGatewayListenerTlsFileCertificate] = None
    sds: Optional[VirtualGatewayListenerTlsSdsCertificate] = None


class VirtualGatewayListenerTlsValidationContextTrust(BaseValidatorModel):
    file: Optional[VirtualGatewayTlsValidationContextFileTrust] = None
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrust] = None


class VirtualGatewayTlsValidationContextTrustOutput(BaseValidatorModel):
    acm: Optional[VirtualGatewayTlsValidationContextAcmTrustOutput] = None
    file: Optional[VirtualGatewayTlsValidationContextFileTrust] = None
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrust] = None


class VirtualGatewayTlsValidationContextTrust(BaseValidatorModel):
    acm: Optional[VirtualGatewayTlsValidationContextAcmTrust] = None
    file: Optional[VirtualGatewayTlsValidationContextFileTrust] = None
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrust] = None


class VirtualNodeConnectionPool(BaseValidatorModel):
    grpc: Optional[VirtualNodeGrpcConnectionPool] = None
    http: Optional[VirtualNodeHttpConnectionPool] = None
    http2: Optional[VirtualNodeHttp2ConnectionPool] = None
    tcp: Optional[VirtualNodeTcpConnectionPool] = None


class VirtualServiceProvider(BaseValidatorModel):
    virtualNode: Optional[VirtualNodeServiceProvider] = None
    virtualRouter: Optional[VirtualRouterServiceProvider] = None


class ServiceDiscoveryOutput(BaseValidatorModel):
    awsCloudMap: Optional[AwsCloudMapServiceDiscoveryOutput] = None
    dns: Optional[DnsServiceDiscovery] = None


class ServiceDiscovery(BaseValidatorModel):
    awsCloudMap: Optional[AwsCloudMapServiceDiscovery] = None
    dns: Optional[DnsServiceDiscovery] = None


class ListenerTimeout(BaseValidatorModel):
    grpc: Optional[GrpcTimeout] = None
    http: Optional[HttpTimeout] = None
    http2: Optional[HttpTimeout] = None
    tcp: Optional[TcpTimeout] = None


class GrpcGatewayRouteAction(BaseValidatorModel):
    target: GatewayRouteTarget
    rewrite: Optional[GrpcGatewayRouteRewrite] = None


class GrpcGatewayRouteMetadata(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[GrpcMetadataMatchMethod] = None


class GrpcRouteMetadata(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[GrpcRouteMetadataMatchMethod] = None


class HttpGatewayRouteHeader(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[HeaderMatchMethod] = None


class HttpRouteHeader(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[HeaderMatchMethod] = None


class TcpRouteOutput(BaseValidatorModel):
    action: TcpRouteActionOutput
    match: Optional[TcpRouteMatch] = None
    timeout: Optional[TcpTimeout] = None


class TcpRoute(BaseValidatorModel):
    action: TcpRouteAction
    match: Optional[TcpRouteMatch] = None
    timeout: Optional[TcpTimeout] = None


class HttpGatewayRouteAction(BaseValidatorModel):
    target: GatewayRouteTarget
    rewrite: Optional[HttpGatewayRouteRewrite] = None


class FileAccessLogOutput(BaseValidatorModel):
    path: str
    format: Optional[LoggingFormatOutput] = None


class VirtualGatewayFileAccessLogOutput(BaseValidatorModel):
    path: str
    format: Optional[LoggingFormatOutput] = None


class FileAccessLog(BaseValidatorModel):
    path: str
    format: Optional[LoggingFormat] = None


class VirtualGatewayFileAccessLog(BaseValidatorModel):
    path: str
    format: Optional[LoggingFormat] = None


class VirtualRouterSpecOutput(BaseValidatorModel):
    listeners: Optional[List[VirtualRouterListener]] = None


class VirtualRouterSpec(BaseValidatorModel):
    listeners: Optional[List[VirtualRouterListener]] = None


# This class is the input for the 'create_mesh' function.
class CreateMeshInput(BaseValidatorModel):
    meshName: str
    clientToken: Optional[str] = None
    spec: Optional[MeshSpec] = None
    tags: Optional[List[TagRef]] = None


class MeshData(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadata
    spec: MeshSpec
    status: MeshStatus


# This class is the input for the 'update_mesh' function.
class UpdateMeshInput(BaseValidatorModel):
    meshName: str
    clientToken: Optional[str] = None
    spec: Optional[MeshSpec] = None


class ListenerTlsValidationContextOutput(BaseValidatorModel):
    trust: ListenerTlsValidationContextTrust
    subjectAlternativeNames: Optional[SubjectAlternativeNamesOutput] = None


class ListenerTlsValidationContext(BaseValidatorModel):
    trust: ListenerTlsValidationContextTrust
    subjectAlternativeNames: Optional[SubjectAlternativeNames] = None


class TlsValidationContextOutput(BaseValidatorModel):
    trust: TlsValidationContextTrustOutput
    subjectAlternativeNames: Optional[SubjectAlternativeNamesOutput] = None


class TlsValidationContext(BaseValidatorModel):
    trust: TlsValidationContextTrust
    subjectAlternativeNames: Optional[SubjectAlternativeNames] = None


class VirtualGatewayListenerTlsValidationContextOutput(BaseValidatorModel):
    trust: VirtualGatewayListenerTlsValidationContextTrust
    subjectAlternativeNames: Optional[SubjectAlternativeNamesOutput] = None


class VirtualGatewayListenerTlsValidationContext(BaseValidatorModel):
    trust: VirtualGatewayListenerTlsValidationContextTrust
    subjectAlternativeNames: Optional[SubjectAlternativeNames] = None


class VirtualGatewayTlsValidationContextOutput(BaseValidatorModel):
    trust: VirtualGatewayTlsValidationContextTrustOutput
    subjectAlternativeNames: Optional[SubjectAlternativeNamesOutput] = None


class VirtualGatewayTlsValidationContext(BaseValidatorModel):
    trust: VirtualGatewayTlsValidationContextTrust
    subjectAlternativeNames: Optional[SubjectAlternativeNames] = None


class VirtualServiceSpec(BaseValidatorModel):
    provider: Optional[VirtualServiceProvider] = None


class GrpcGatewayRouteMatchOutput(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameMatch] = None
    metadata: Optional[List[GrpcGatewayRouteMetadata]] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None


class GrpcGatewayRouteMatch(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameMatch] = None
    metadata: Optional[List[GrpcGatewayRouteMetadata]] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None


class GrpcRouteMatchOutput(BaseValidatorModel):
    metadata: Optional[List[GrpcRouteMetadata]] = None
    methodName: Optional[str] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None


class GrpcRouteMatch(BaseValidatorModel):
    metadata: Optional[List[GrpcRouteMetadata]] = None
    methodName: Optional[str] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None


class HttpGatewayRouteMatchOutput(BaseValidatorModel):
    headers: Optional[List[HttpGatewayRouteHeader]] = None
    hostname: Optional[GatewayRouteHostnameMatch] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatch] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[List[HttpQueryParameter]] = None


class HttpGatewayRouteMatch(BaseValidatorModel):
    headers: Optional[List[HttpGatewayRouteHeader]] = None
    hostname: Optional[GatewayRouteHostnameMatch] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatch] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[List[HttpQueryParameter]] = None


class HttpRouteMatchOutput(BaseValidatorModel):
    headers: Optional[List[HttpRouteHeader]] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatch] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[List[HttpQueryParameter]] = None
    scheme: Optional[HttpSchemeType] = None


class HttpRouteMatch(BaseValidatorModel):
    headers: Optional[List[HttpRouteHeader]] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatch] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[List[HttpQueryParameter]] = None
    scheme: Optional[HttpSchemeType] = None


class AccessLogOutput(BaseValidatorModel):
    file: Optional[FileAccessLogOutput] = None


class VirtualGatewayAccessLogOutput(BaseValidatorModel):
    file: Optional[VirtualGatewayFileAccessLogOutput] = None


class AccessLog(BaseValidatorModel):
    file: Optional[FileAccessLog] = None


class VirtualGatewayAccessLog(BaseValidatorModel):
    file: Optional[VirtualGatewayFileAccessLog] = None


class VirtualRouterData(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadata
    spec: VirtualRouterSpecOutput
    status: VirtualRouterStatus
    virtualRouterName: str

VirtualRouterSpecUnion = Union[VirtualRouterSpec, VirtualRouterSpecOutput]


# This class is the output for the 'create_mesh' function.
class CreateMeshOutput(BaseValidatorModel):
    mesh: MeshData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_mesh' function.
class DeleteMeshOutput(BaseValidatorModel):
    mesh: MeshData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_mesh' function.
class DescribeMeshOutput(BaseValidatorModel):
    mesh: MeshData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_mesh' function.
class UpdateMeshOutput(BaseValidatorModel):
    mesh: MeshData
    ResponseMetadata: ResponseMetadata


class ListenerTlsOutput(BaseValidatorModel):
    certificate: ListenerTlsCertificate
    mode: ListenerTlsModeType
    validation: Optional[ListenerTlsValidationContextOutput] = None


class ListenerTls(BaseValidatorModel):
    certificate: ListenerTlsCertificate
    mode: ListenerTlsModeType
    validation: Optional[ListenerTlsValidationContext] = None


class ClientPolicyTlsOutput(BaseValidatorModel):
    validation: TlsValidationContextOutput
    certificate: Optional[ClientTlsCertificate] = None
    enforce: Optional[bool] = None
    ports: Optional[List[int]] = None


class ClientPolicyTls(BaseValidatorModel):
    validation: TlsValidationContext
    certificate: Optional[ClientTlsCertificate] = None
    enforce: Optional[bool] = None
    ports: Optional[List[int]] = None


class VirtualGatewayListenerTlsOutput(BaseValidatorModel):
    certificate: VirtualGatewayListenerTlsCertificate
    mode: VirtualGatewayListenerTlsModeType
    validation: Optional[VirtualGatewayListenerTlsValidationContextOutput] = None


class VirtualGatewayListenerTls(BaseValidatorModel):
    certificate: VirtualGatewayListenerTlsCertificate
    mode: VirtualGatewayListenerTlsModeType
    validation: Optional[VirtualGatewayListenerTlsValidationContext] = None


class VirtualGatewayClientPolicyTlsOutput(BaseValidatorModel):
    validation: VirtualGatewayTlsValidationContextOutput
    certificate: Optional[VirtualGatewayClientTlsCertificate] = None
    enforce: Optional[bool] = None
    ports: Optional[List[int]] = None


class VirtualGatewayClientPolicyTls(BaseValidatorModel):
    validation: VirtualGatewayTlsValidationContext
    certificate: Optional[VirtualGatewayClientTlsCertificate] = None
    enforce: Optional[bool] = None
    ports: Optional[List[int]] = None


# This class is the input for the 'create_virtual_service' function.
class CreateVirtualServiceInput(BaseValidatorModel):
    meshName: str
    spec: VirtualServiceSpec
    virtualServiceName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[List[TagRef]] = None


# This class is the input for the 'update_virtual_service' function.
class UpdateVirtualServiceInput(BaseValidatorModel):
    meshName: str
    spec: VirtualServiceSpec
    virtualServiceName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


class VirtualServiceData(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadata
    spec: VirtualServiceSpec
    status: VirtualServiceStatus
    virtualServiceName: str


class GrpcGatewayRouteOutput(BaseValidatorModel):
    action: GrpcGatewayRouteAction
    match: GrpcGatewayRouteMatchOutput


class GrpcGatewayRoute(BaseValidatorModel):
    action: GrpcGatewayRouteAction
    match: GrpcGatewayRouteMatch


class GrpcRouteOutput(BaseValidatorModel):
    action: GrpcRouteActionOutput
    match: GrpcRouteMatchOutput
    retryPolicy: Optional[GrpcRetryPolicyOutput] = None
    timeout: Optional[GrpcTimeout] = None


class GrpcRoute(BaseValidatorModel):
    action: GrpcRouteAction
    match: GrpcRouteMatch
    retryPolicy: Optional[GrpcRetryPolicy] = None
    timeout: Optional[GrpcTimeout] = None


class HttpGatewayRouteOutput(BaseValidatorModel):
    action: HttpGatewayRouteAction
    match: HttpGatewayRouteMatchOutput


class HttpGatewayRoute(BaseValidatorModel):
    action: HttpGatewayRouteAction
    match: HttpGatewayRouteMatch


class HttpRouteOutput(BaseValidatorModel):
    action: HttpRouteActionOutput
    match: HttpRouteMatchOutput
    retryPolicy: Optional[HttpRetryPolicyOutput] = None
    timeout: Optional[HttpTimeout] = None


class HttpRoute(BaseValidatorModel):
    action: HttpRouteAction
    match: HttpRouteMatch
    retryPolicy: Optional[HttpRetryPolicy] = None
    timeout: Optional[HttpTimeout] = None


class LoggingOutput(BaseValidatorModel):
    accessLog: Optional[AccessLogOutput] = None


class VirtualGatewayLoggingOutput(BaseValidatorModel):
    accessLog: Optional[VirtualGatewayAccessLogOutput] = None


class Logging(BaseValidatorModel):
    accessLog: Optional[AccessLog] = None


class VirtualGatewayLogging(BaseValidatorModel):
    accessLog: Optional[VirtualGatewayAccessLog] = None


# This class is the output for the 'create_virtual_router' function.
class CreateVirtualRouterOutput(BaseValidatorModel):
    virtualRouter: VirtualRouterData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_virtual_router' function.
class DeleteVirtualRouterOutput(BaseValidatorModel):
    virtualRouter: VirtualRouterData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_virtual_router' function.
class DescribeVirtualRouterOutput(BaseValidatorModel):
    virtualRouter: VirtualRouterData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_virtual_router' function.
class UpdateVirtualRouterOutput(BaseValidatorModel):
    virtualRouter: VirtualRouterData
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_virtual_router' function.
class CreateVirtualRouterInput(BaseValidatorModel):
    meshName: str
    spec: VirtualRouterSpecUnion
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[List[TagRef]] = None


# This class is the input for the 'update_virtual_router' function.
class UpdateVirtualRouterInput(BaseValidatorModel):
    meshName: str
    spec: VirtualRouterSpecUnion
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


class ListenerOutput(BaseValidatorModel):
    portMapping: PortMapping
    connectionPool: Optional[VirtualNodeConnectionPool] = None
    healthCheck: Optional[HealthCheckPolicy] = None
    outlierDetection: Optional[OutlierDetection] = None
    timeout: Optional[ListenerTimeout] = None
    tls: Optional[ListenerTlsOutput] = None


class Listener(BaseValidatorModel):
    portMapping: PortMapping
    connectionPool: Optional[VirtualNodeConnectionPool] = None
    healthCheck: Optional[HealthCheckPolicy] = None
    outlierDetection: Optional[OutlierDetection] = None
    timeout: Optional[ListenerTimeout] = None
    tls: Optional[ListenerTls] = None


class ClientPolicyOutput(BaseValidatorModel):
    tls: Optional[ClientPolicyTlsOutput] = None


class ClientPolicy(BaseValidatorModel):
    tls: Optional[ClientPolicyTls] = None


class VirtualGatewayListenerOutput(BaseValidatorModel):
    portMapping: VirtualGatewayPortMapping
    connectionPool: Optional[VirtualGatewayConnectionPool] = None
    healthCheck: Optional[VirtualGatewayHealthCheckPolicy] = None
    tls: Optional[VirtualGatewayListenerTlsOutput] = None


class VirtualGatewayListener(BaseValidatorModel):
    portMapping: VirtualGatewayPortMapping
    connectionPool: Optional[VirtualGatewayConnectionPool] = None
    healthCheck: Optional[VirtualGatewayHealthCheckPolicy] = None
    tls: Optional[VirtualGatewayListenerTls] = None


class VirtualGatewayClientPolicyOutput(BaseValidatorModel):
    tls: Optional[VirtualGatewayClientPolicyTlsOutput] = None


class VirtualGatewayClientPolicy(BaseValidatorModel):
    tls: Optional[VirtualGatewayClientPolicyTls] = None


# This class is the output for the 'create_virtual_service' function.
class CreateVirtualServiceOutput(BaseValidatorModel):
    virtualService: VirtualServiceData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_virtual_service' function.
class DeleteVirtualServiceOutput(BaseValidatorModel):
    virtualService: VirtualServiceData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_virtual_service' function.
class DescribeVirtualServiceOutput(BaseValidatorModel):
    virtualService: VirtualServiceData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_virtual_service' function.
class UpdateVirtualServiceOutput(BaseValidatorModel):
    virtualService: VirtualServiceData
    ResponseMetadata: ResponseMetadata


class GatewayRouteSpecOutput(BaseValidatorModel):
    grpcRoute: Optional[GrpcGatewayRouteOutput] = None
    http2Route: Optional[HttpGatewayRouteOutput] = None
    httpRoute: Optional[HttpGatewayRouteOutput] = None
    priority: Optional[int] = None


class GatewayRouteSpec(BaseValidatorModel):
    grpcRoute: Optional[GrpcGatewayRoute] = None
    http2Route: Optional[HttpGatewayRoute] = None
    httpRoute: Optional[HttpGatewayRoute] = None
    priority: Optional[int] = None


class RouteSpecOutput(BaseValidatorModel):
    grpcRoute: Optional[GrpcRouteOutput] = None
    http2Route: Optional[HttpRouteOutput] = None
    httpRoute: Optional[HttpRouteOutput] = None
    priority: Optional[int] = None
    tcpRoute: Optional[TcpRouteOutput] = None


class RouteSpec(BaseValidatorModel):
    grpcRoute: Optional[GrpcRoute] = None
    http2Route: Optional[HttpRoute] = None
    httpRoute: Optional[HttpRoute] = None
    priority: Optional[int] = None
    tcpRoute: Optional[TcpRoute] = None


class BackendDefaultsOutput(BaseValidatorModel):
    clientPolicy: Optional[ClientPolicyOutput] = None


class VirtualServiceBackendOutput(BaseValidatorModel):
    virtualServiceName: str
    clientPolicy: Optional[ClientPolicyOutput] = None


class BackendDefaults(BaseValidatorModel):
    clientPolicy: Optional[ClientPolicy] = None


class VirtualServiceBackend(BaseValidatorModel):
    virtualServiceName: str
    clientPolicy: Optional[ClientPolicy] = None


class VirtualGatewayBackendDefaultsOutput(BaseValidatorModel):
    clientPolicy: Optional[VirtualGatewayClientPolicyOutput] = None


class VirtualGatewayBackendDefaults(BaseValidatorModel):
    clientPolicy: Optional[VirtualGatewayClientPolicy] = None


class GatewayRouteData(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    metadata: ResourceMetadata
    spec: GatewayRouteSpecOutput
    status: GatewayRouteStatus
    virtualGatewayName: str

GatewayRouteSpecUnion = Union[GatewayRouteSpec, GatewayRouteSpecOutput]


class RouteData(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadata
    routeName: str
    spec: RouteSpecOutput
    status: RouteStatus
    virtualRouterName: str

RouteSpecUnion = Union[RouteSpec, RouteSpecOutput]


class BackendOutput(BaseValidatorModel):
    virtualService: Optional[VirtualServiceBackendOutput] = None


class Backend(BaseValidatorModel):
    virtualService: Optional[VirtualServiceBackend] = None


class VirtualGatewaySpecOutput(BaseValidatorModel):
    listeners: List[VirtualGatewayListenerOutput]
    backendDefaults: Optional[VirtualGatewayBackendDefaultsOutput] = None
    logging: Optional[VirtualGatewayLoggingOutput] = None


class VirtualGatewaySpec(BaseValidatorModel):
    listeners: List[VirtualGatewayListener]
    backendDefaults: Optional[VirtualGatewayBackendDefaults] = None
    logging: Optional[VirtualGatewayLogging] = None


# This class is the output for the 'create_gateway_route' function.
class CreateGatewayRouteOutput(BaseValidatorModel):
    gatewayRoute: GatewayRouteData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_gateway_route' function.
class DeleteGatewayRouteOutput(BaseValidatorModel):
    gatewayRoute: GatewayRouteData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_gateway_route' function.
class DescribeGatewayRouteOutput(BaseValidatorModel):
    gatewayRoute: GatewayRouteData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_gateway_route' function.
class UpdateGatewayRouteOutput(BaseValidatorModel):
    gatewayRoute: GatewayRouteData
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_gateway_route' function.
class CreateGatewayRouteInput(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecUnion
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[List[TagRef]] = None


# This class is the input for the 'update_gateway_route' function.
class UpdateGatewayRouteInput(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecUnion
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


# This class is the output for the 'create_route' function.
class CreateRouteOutput(BaseValidatorModel):
    route: RouteData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_route' function.
class DeleteRouteOutput(BaseValidatorModel):
    route: RouteData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_route' function.
class DescribeRouteOutput(BaseValidatorModel):
    route: RouteData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_route' function.
class UpdateRouteOutput(BaseValidatorModel):
    route: RouteData
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_route' function.
class CreateRouteInput(BaseValidatorModel):
    meshName: str
    routeName: str
    spec: RouteSpecUnion
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[List[TagRef]] = None


# This class is the input for the 'update_route' function.
class UpdateRouteInput(BaseValidatorModel):
    meshName: str
    routeName: str
    spec: RouteSpecUnion
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


class VirtualNodeSpecOutput(BaseValidatorModel):
    backendDefaults: Optional[BackendDefaultsOutput] = None
    backends: Optional[List[BackendOutput]] = None
    listeners: Optional[List[ListenerOutput]] = None
    logging: Optional[LoggingOutput] = None
    serviceDiscovery: Optional[ServiceDiscoveryOutput] = None


class VirtualNodeSpec(BaseValidatorModel):
    backendDefaults: Optional[BackendDefaults] = None
    backends: Optional[List[Backend]] = None
    listeners: Optional[List[Listener]] = None
    logging: Optional[Logging] = None
    serviceDiscovery: Optional[ServiceDiscovery] = None


class VirtualGatewayData(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadata
    spec: VirtualGatewaySpecOutput
    status: VirtualGatewayStatus
    virtualGatewayName: str

VirtualGatewaySpecUnion = Union[VirtualGatewaySpec, VirtualGatewaySpecOutput]


class VirtualNodeData(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadata
    spec: VirtualNodeSpecOutput
    status: VirtualNodeStatus
    virtualNodeName: str

VirtualNodeSpecUnion = Union[VirtualNodeSpec, VirtualNodeSpecOutput]


# This class is the output for the 'create_virtual_gateway' function.
class CreateVirtualGatewayOutput(BaseValidatorModel):
    virtualGateway: VirtualGatewayData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_virtual_gateway' function.
class DeleteVirtualGatewayOutput(BaseValidatorModel):
    virtualGateway: VirtualGatewayData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_virtual_gateway' function.
class DescribeVirtualGatewayOutput(BaseValidatorModel):
    virtualGateway: VirtualGatewayData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_virtual_gateway' function.
class UpdateVirtualGatewayOutput(BaseValidatorModel):
    virtualGateway: VirtualGatewayData
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_virtual_gateway' function.
class CreateVirtualGatewayInput(BaseValidatorModel):
    meshName: str
    spec: VirtualGatewaySpecUnion
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[List[TagRef]] = None


# This class is the input for the 'update_virtual_gateway' function.
class UpdateVirtualGatewayInput(BaseValidatorModel):
    meshName: str
    spec: VirtualGatewaySpecUnion
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


# This class is the output for the 'create_virtual_node' function.
class CreateVirtualNodeOutput(BaseValidatorModel):
    virtualNode: VirtualNodeData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_virtual_node' function.
class DeleteVirtualNodeOutput(BaseValidatorModel):
    virtualNode: VirtualNodeData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_virtual_node' function.
class DescribeVirtualNodeOutput(BaseValidatorModel):
    virtualNode: VirtualNodeData
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_virtual_node' function.
class UpdateVirtualNodeOutput(BaseValidatorModel):
    virtualNode: VirtualNodeData
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_virtual_node' function.
class CreateVirtualNodeInput(BaseValidatorModel):
    meshName: str
    spec: VirtualNodeSpecUnion
    virtualNodeName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[List[TagRef]] = None


# This class is the input for the 'update_virtual_node' function.
class UpdateVirtualNodeInput(BaseValidatorModel):
    meshName: str
    spec: VirtualNodeSpecUnion
    virtualNodeName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None