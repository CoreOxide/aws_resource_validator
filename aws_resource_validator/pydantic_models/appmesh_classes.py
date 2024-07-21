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
from aws_resource_validator.pydantic_models.appmesh_constants import *

class AwsCloudMapInstanceAttributeTypeDef(BaseModel):
    key: str
    value: str

class ListenerTlsFileCertificateTypeDef(BaseModel):
    certificateChain: str
    privateKey: str

class ListenerTlsSdsCertificateTypeDef(BaseModel):
    secretName: str

class TagRefTypeDef(BaseModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteGatewayRouteInputRequestTypeDef(BaseModel):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None

class DeleteMeshInputRequestTypeDef(BaseModel):
    meshName: str

class DeleteRouteInputRequestTypeDef(BaseModel):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None

class DeleteVirtualGatewayInputRequestTypeDef(BaseModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None

class DeleteVirtualNodeInputRequestTypeDef(BaseModel):
    meshName: str
    virtualNodeName: str
    meshOwner: Optional[str] = None

class DeleteVirtualRouterInputRequestTypeDef(BaseModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None

class DeleteVirtualServiceInputRequestTypeDef(BaseModel):
    meshName: str
    virtualServiceName: str
    meshOwner: Optional[str] = None

class DescribeGatewayRouteInputRequestTypeDef(BaseModel):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None

class DescribeMeshInputRequestTypeDef(BaseModel):
    meshName: str
    meshOwner: Optional[str] = None

class DescribeRouteInputRequestTypeDef(BaseModel):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None

class DescribeVirtualGatewayInputRequestTypeDef(BaseModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None

class DescribeVirtualNodeInputRequestTypeDef(BaseModel):
    meshName: str
    virtualNodeName: str
    meshOwner: Optional[str] = None

class DescribeVirtualRouterInputRequestTypeDef(BaseModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None

class DescribeVirtualServiceInputRequestTypeDef(BaseModel):
    meshName: str
    virtualServiceName: str
    meshOwner: Optional[str] = None

class DnsServiceDiscoveryTypeDef(BaseModel):
    hostname: str
    ipPreference: Optional[IpPreferenceType] = None
    responseType: Optional[DnsResponseTypeType] = None

class DurationTypeDef(BaseModel):
    unit: Optional[DurationUnitType] = None
    value: Optional[int] = None

class EgressFilterTypeDef(BaseModel):
    type: EgressFilterTypeType

class GatewayRouteStatusTypeDef(BaseModel):
    status: GatewayRouteStatusCodeType

class ResourceMetadataTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshOwner: str
    resourceOwner: str
    uid: str
    version: int

class GatewayRouteHostnameMatchTypeDef(BaseModel):
    exact: Optional[str] = None
    suffix: Optional[str] = None

class GatewayRouteHostnameRewriteTypeDef(BaseModel):
    defaultTargetHostname: Optional[DefaultGatewayRouteRewriteType] = None

class GatewayRouteRefTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    gatewayRouteName: str
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str

class GatewayRouteVirtualServiceTypeDef(BaseModel):
    virtualServiceName: str

class MatchRangeTypeDef(BaseModel):
    end: int
    start: int

class WeightedTargetTypeDef(BaseModel):
    virtualNode: str
    weight: int
    port: Optional[int] = None

class HealthCheckPolicyTypeDef(BaseModel):
    healthyThreshold: int
    intervalMillis: int
    protocol: PortProtocolType
    timeoutMillis: int
    unhealthyThreshold: int
    path: Optional[str] = None
    port: Optional[int] = None

class HttpPathMatchTypeDef(BaseModel):
    exact: Optional[str] = None
    regex: Optional[str] = None

class HttpGatewayRoutePathRewriteTypeDef(BaseModel):
    exact: Optional[str] = None

class HttpGatewayRoutePrefixRewriteTypeDef(BaseModel):
    defaultPrefix: Optional[DefaultGatewayRouteRewriteType] = None
    value: Optional[str] = None

class QueryParameterMatchTypeDef(BaseModel):
    exact: Optional[str] = None

class JsonFormatRefTypeDef(BaseModel):
    key: str
    value: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListGatewayRoutesInputRequestTypeDef(BaseModel):
    meshName: str
    virtualGatewayName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class ListMeshesInputRequestTypeDef(BaseModel):
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class MeshRefTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int

class ListRoutesInputRequestTypeDef(BaseModel):
    meshName: str
    virtualRouterName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class RouteRefTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    routeName: str
    version: int
    virtualRouterName: str

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class ListVirtualGatewaysInputRequestTypeDef(BaseModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class VirtualGatewayRefTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str

class ListVirtualNodesInputRequestTypeDef(BaseModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class VirtualNodeRefTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualNodeName: str

class ListVirtualRoutersInputRequestTypeDef(BaseModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class VirtualRouterRefTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualRouterName: str

class ListVirtualServicesInputRequestTypeDef(BaseModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class VirtualServiceRefTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualServiceName: str

class ListenerTlsAcmCertificateTypeDef(BaseModel):
    certificateArn: str

class TlsValidationContextFileTrustTypeDef(BaseModel):
    certificateChain: str

class TlsValidationContextSdsTrustTypeDef(BaseModel):
    secretName: str

class PortMappingTypeDef(BaseModel):
    port: int
    protocol: PortProtocolType

class MeshStatusTypeDef(BaseModel):
    status: Optional[MeshStatusCodeType] = None

class MeshServiceDiscoveryTypeDef(BaseModel):
    ipPreference: Optional[IpPreferenceType] = None

class RouteStatusTypeDef(BaseModel):
    status: RouteStatusCodeType

class SubjectAlternativeNameMatchersTypeDef(BaseModel):
    exact: Sequence[str]

class TcpRouteMatchTypeDef(BaseModel):
    port: Optional[int] = None

class TlsValidationContextAcmTrustTypeDef(BaseModel):
    certificateAuthorityArns: Sequence[str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class VirtualGatewayListenerTlsFileCertificateTypeDef(BaseModel):
    certificateChain: str
    privateKey: str

class VirtualGatewayListenerTlsSdsCertificateTypeDef(BaseModel):
    secretName: str

class VirtualGatewayGrpcConnectionPoolTypeDef(BaseModel):
    maxRequests: int

class VirtualGatewayHttp2ConnectionPoolTypeDef(BaseModel):
    maxRequests: int

class VirtualGatewayHttpConnectionPoolTypeDef(BaseModel):
    maxConnections: int
    maxPendingRequests: Optional[int] = None

class VirtualGatewayStatusTypeDef(BaseModel):
    status: VirtualGatewayStatusCodeType

class VirtualGatewayHealthCheckPolicyTypeDef(BaseModel):
    healthyThreshold: int
    intervalMillis: int
    protocol: VirtualGatewayPortProtocolType
    timeoutMillis: int
    unhealthyThreshold: int
    path: Optional[str] = None
    port: Optional[int] = None

class VirtualGatewayListenerTlsAcmCertificateTypeDef(BaseModel):
    certificateArn: str

class VirtualGatewayTlsValidationContextFileTrustTypeDef(BaseModel):
    certificateChain: str

class VirtualGatewayTlsValidationContextSdsTrustTypeDef(BaseModel):
    secretName: str

class VirtualGatewayPortMappingTypeDef(BaseModel):
    port: int
    protocol: VirtualGatewayPortProtocolType

class VirtualGatewayTlsValidationContextAcmTrustTypeDef(BaseModel):
    certificateAuthorityArns: Sequence[str]

class VirtualNodeGrpcConnectionPoolTypeDef(BaseModel):
    maxRequests: int

class VirtualNodeHttp2ConnectionPoolTypeDef(BaseModel):
    maxRequests: int

class VirtualNodeHttpConnectionPoolTypeDef(BaseModel):
    maxConnections: int
    maxPendingRequests: Optional[int] = None

class VirtualNodeTcpConnectionPoolTypeDef(BaseModel):
    maxConnections: int

class VirtualNodeStatusTypeDef(BaseModel):
    status: VirtualNodeStatusCodeType

class VirtualNodeServiceProviderTypeDef(BaseModel):
    virtualNodeName: str

class VirtualRouterStatusTypeDef(BaseModel):
    status: VirtualRouterStatusCodeType

class VirtualRouterServiceProviderTypeDef(BaseModel):
    virtualRouterName: str

class VirtualServiceStatusTypeDef(BaseModel):
    status: VirtualServiceStatusCodeType

class AwsCloudMapServiceDiscoveryTypeDef(BaseModel):
    namespaceName: str
    serviceName: str
    attributes: Optional[Sequence[AwsCloudMapInstanceAttributeTypeDef]] = None
    ipPreference: Optional[IpPreferenceType] = None

class ClientTlsCertificateTypeDef(BaseModel):
    file: Optional[ListenerTlsFileCertificateTypeDef] = None
    sds: Optional[ListenerTlsSdsCertificateTypeDef] = None

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagRefTypeDef]

class ListTagsForResourceOutputTypeDef(BaseModel):
    nextToken: str
    tags: List[TagRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GrpcRetryPolicyTypeDef(BaseModel):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    grpcRetryEvents: Optional[Sequence[GrpcRetryPolicyEventType]] = None
    httpRetryEvents: Optional[Sequence[str]] = None
    tcpRetryEvents: Optional[Sequence[Literal["connection-error"]]] = None

class GrpcTimeoutTypeDef(BaseModel):
    idle: Optional[DurationTypeDef] = None
    perRequest: Optional[DurationTypeDef] = None

class HttpRetryPolicyTypeDef(BaseModel):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    httpRetryEvents: Optional[Sequence[str]] = None
    tcpRetryEvents: Optional[Sequence[Literal["connection-error"]]] = None

class HttpTimeoutTypeDef(BaseModel):
    idle: Optional[DurationTypeDef] = None
    perRequest: Optional[DurationTypeDef] = None

class OutlierDetectionTypeDef(BaseModel):
    baseEjectionDuration: DurationTypeDef
    interval: DurationTypeDef
    maxEjectionPercent: int
    maxServerErrors: int

class TcpTimeoutTypeDef(BaseModel):
    idle: Optional[DurationTypeDef] = None

class GrpcGatewayRouteRewriteTypeDef(BaseModel):
    hostname: Optional[GatewayRouteHostnameRewriteTypeDef] = None

class ListGatewayRoutesOutputTypeDef(BaseModel):
    gatewayRoutes: List[GatewayRouteRefTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayRouteTargetTypeDef(BaseModel):
    virtualService: GatewayRouteVirtualServiceTypeDef
    port: Optional[int] = None

class GrpcMetadataMatchMethodTypeDef(BaseModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRangeTypeDef] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None

class GrpcRouteMetadataMatchMethodTypeDef(BaseModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRangeTypeDef] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None

class HeaderMatchMethodTypeDef(BaseModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRangeTypeDef] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None

class GrpcRouteActionTypeDef(BaseModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class HttpRouteActionTypeDef(BaseModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class TcpRouteActionTypeDef(BaseModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class HttpGatewayRouteRewriteTypeDef(BaseModel):
    hostname: Optional[GatewayRouteHostnameRewriteTypeDef] = None
    path: Optional[HttpGatewayRoutePathRewriteTypeDef] = None
    prefix: Optional[HttpGatewayRoutePrefixRewriteTypeDef] = None

class HttpQueryParameterTypeDef(BaseModel):
    name: str
    match: Optional[QueryParameterMatchTypeDef] = None

class LoggingFormatTypeDef(BaseModel):
    json: Optional[Sequence[JsonFormatRefTypeDef]] = None
    text: Optional[str] = None

class ListGatewayRoutesInputListGatewayRoutesPaginateTypeDef(BaseModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMeshesInputListMeshesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutesInputListRoutesPaginateTypeDef(BaseModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef(BaseModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualNodesInputListVirtualNodesPaginateTypeDef(BaseModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualRoutersInputListVirtualRoutersPaginateTypeDef(BaseModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualServicesInputListVirtualServicesPaginateTypeDef(BaseModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMeshesOutputTypeDef(BaseModel):
    meshes: List[MeshRefTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoutesOutputTypeDef(BaseModel):
    nextToken: str
    routes: List[RouteRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualGatewaysOutputTypeDef(BaseModel):
    nextToken: str
    virtualGateways: List[VirtualGatewayRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualNodesOutputTypeDef(BaseModel):
    nextToken: str
    virtualNodes: List[VirtualNodeRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualRoutersOutputTypeDef(BaseModel):
    nextToken: str
    virtualRouters: List[VirtualRouterRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualServicesOutputTypeDef(BaseModel):
    nextToken: str
    virtualServices: List[VirtualServiceRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTlsCertificateTypeDef(BaseModel):
    acm: Optional[ListenerTlsAcmCertificateTypeDef] = None
    file: Optional[ListenerTlsFileCertificateTypeDef] = None
    sds: Optional[ListenerTlsSdsCertificateTypeDef] = None

class ListenerTlsValidationContextTrustTypeDef(BaseModel):
    file: Optional[TlsValidationContextFileTrustTypeDef] = None
    sds: Optional[TlsValidationContextSdsTrustTypeDef] = None

class VirtualRouterListenerTypeDef(BaseModel):
    portMapping: PortMappingTypeDef

class MeshSpecTypeDef(BaseModel):
    egressFilter: Optional[EgressFilterTypeDef] = None
    serviceDiscovery: Optional[MeshServiceDiscoveryTypeDef] = None

class SubjectAlternativeNamesTypeDef(BaseModel):
    match: SubjectAlternativeNameMatchersTypeDef

class TlsValidationContextTrustTypeDef(BaseModel):
    acm: Optional[TlsValidationContextAcmTrustTypeDef] = None
    file: Optional[TlsValidationContextFileTrustTypeDef] = None
    sds: Optional[TlsValidationContextSdsTrustTypeDef] = None

class VirtualGatewayClientTlsCertificateTypeDef(BaseModel):
    file: Optional[VirtualGatewayListenerTlsFileCertificateTypeDef] = None
    sds: Optional[VirtualGatewayListenerTlsSdsCertificateTypeDef] = None

class VirtualGatewayConnectionPoolTypeDef(BaseModel):
    grpc: Optional[VirtualGatewayGrpcConnectionPoolTypeDef] = None
    http: Optional[VirtualGatewayHttpConnectionPoolTypeDef] = None
    http2: Optional[VirtualGatewayHttp2ConnectionPoolTypeDef] = None

class VirtualGatewayListenerTlsCertificateTypeDef(BaseModel):
    acm: Optional[VirtualGatewayListenerTlsAcmCertificateTypeDef] = None
    file: Optional[VirtualGatewayListenerTlsFileCertificateTypeDef] = None
    sds: Optional[VirtualGatewayListenerTlsSdsCertificateTypeDef] = None

class VirtualGatewayListenerTlsValidationContextTrustTypeDef(BaseModel):
    file: Optional[VirtualGatewayTlsValidationContextFileTrustTypeDef] = None
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrustTypeDef] = None

class VirtualGatewayTlsValidationContextTrustTypeDef(BaseModel):
    acm: Optional[VirtualGatewayTlsValidationContextAcmTrustTypeDef] = None
    file: Optional[VirtualGatewayTlsValidationContextFileTrustTypeDef] = None
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrustTypeDef] = None

class VirtualNodeConnectionPoolTypeDef(BaseModel):
    grpc: Optional[VirtualNodeGrpcConnectionPoolTypeDef] = None
    http: Optional[VirtualNodeHttpConnectionPoolTypeDef] = None
    http2: Optional[VirtualNodeHttp2ConnectionPoolTypeDef] = None
    tcp: Optional[VirtualNodeTcpConnectionPoolTypeDef] = None

class VirtualServiceProviderTypeDef(BaseModel):
    virtualNode: Optional[VirtualNodeServiceProviderTypeDef] = None
    virtualRouter: Optional[VirtualRouterServiceProviderTypeDef] = None

class ServiceDiscoveryTypeDef(BaseModel):
    awsCloudMap: Optional[AwsCloudMapServiceDiscoveryTypeDef] = None
    dns: Optional[DnsServiceDiscoveryTypeDef] = None

class ListenerTimeoutTypeDef(BaseModel):
    grpc: Optional[GrpcTimeoutTypeDef] = None
    http: Optional[HttpTimeoutTypeDef] = None
    http2: Optional[HttpTimeoutTypeDef] = None
    tcp: Optional[TcpTimeoutTypeDef] = None

class GrpcGatewayRouteActionTypeDef(BaseModel):
    target: GatewayRouteTargetTypeDef
    rewrite: Optional[GrpcGatewayRouteRewriteTypeDef] = None

class GrpcGatewayRouteMetadataTypeDef(BaseModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[GrpcMetadataMatchMethodTypeDef] = None

class GrpcRouteMetadataTypeDef(BaseModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[GrpcRouteMetadataMatchMethodTypeDef] = None

class HttpGatewayRouteHeaderTypeDef(BaseModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[HeaderMatchMethodTypeDef] = None

class HttpRouteHeaderTypeDef(BaseModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[HeaderMatchMethodTypeDef] = None

class TcpRouteTypeDef(BaseModel):
    action: TcpRouteActionTypeDef
    match: Optional[TcpRouteMatchTypeDef] = None
    timeout: Optional[TcpTimeoutTypeDef] = None

class HttpGatewayRouteActionTypeDef(BaseModel):
    target: GatewayRouteTargetTypeDef
    rewrite: Optional[HttpGatewayRouteRewriteTypeDef] = None

class FileAccessLogTypeDef(BaseModel):
    path: str
    format: Optional[LoggingFormatTypeDef] = None

class VirtualGatewayFileAccessLogTypeDef(BaseModel):
    path: str
    format: Optional[LoggingFormatTypeDef] = None

class VirtualRouterSpecTypeDef(BaseModel):
    listeners: Optional[Sequence[VirtualRouterListenerTypeDef]] = None

class CreateMeshInputRequestTypeDef(BaseModel):
    meshName: str
    clientToken: Optional[str] = None
    spec: Optional[MeshSpecTypeDef] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class MeshDataTypeDef(BaseModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: MeshSpecTypeDef
    status: MeshStatusTypeDef

class UpdateMeshInputRequestTypeDef(BaseModel):
    meshName: str
    clientToken: Optional[str] = None
    spec: Optional[MeshSpecTypeDef] = None

class ListenerTlsValidationContextTypeDef(BaseModel):
    trust: ListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None

class TlsValidationContextTypeDef(BaseModel):
    trust: TlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None

class VirtualGatewayListenerTlsValidationContextTypeDef(BaseModel):
    trust: VirtualGatewayListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None

class VirtualGatewayTlsValidationContextTypeDef(BaseModel):
    trust: VirtualGatewayTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None

class VirtualServiceSpecTypeDef(BaseModel):
    provider: Optional[VirtualServiceProviderTypeDef] = None

class GrpcGatewayRouteMatchTypeDef(BaseModel):
    hostname: Optional[GatewayRouteHostnameMatchTypeDef] = None
    metadata: Optional[Sequence[GrpcGatewayRouteMetadataTypeDef]] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None

class GrpcRouteMatchTypeDef(BaseModel):
    metadata: Optional[Sequence[GrpcRouteMetadataTypeDef]] = None
    methodName: Optional[str] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None

class HttpGatewayRouteMatchTypeDef(BaseModel):
    headers: Optional[Sequence[HttpGatewayRouteHeaderTypeDef]] = None
    hostname: Optional[GatewayRouteHostnameMatchTypeDef] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatchTypeDef] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[Sequence[HttpQueryParameterTypeDef]] = None

class HttpRouteMatchTypeDef(BaseModel):
    headers: Optional[Sequence[HttpRouteHeaderTypeDef]] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatchTypeDef] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[Sequence[HttpQueryParameterTypeDef]] = None
    scheme: Optional[HttpSchemeType] = None

class AccessLogTypeDef(BaseModel):
    file: Optional[FileAccessLogTypeDef] = None

class VirtualGatewayAccessLogTypeDef(BaseModel):
    file: Optional[VirtualGatewayFileAccessLogTypeDef] = None

class CreateVirtualRouterInputRequestTypeDef(BaseModel):
    meshName: str
    spec: VirtualRouterSpecTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class UpdateVirtualRouterInputRequestTypeDef(BaseModel):
    meshName: str
    spec: VirtualRouterSpecTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class VirtualRouterDataTypeDef(BaseModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualRouterSpecTypeDef
    status: VirtualRouterStatusTypeDef
    virtualRouterName: str

class CreateMeshOutputTypeDef(BaseModel):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMeshOutputTypeDef(BaseModel):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMeshOutputTypeDef(BaseModel):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMeshOutputTypeDef(BaseModel):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTlsTypeDef(BaseModel):
    certificate: ListenerTlsCertificateTypeDef
    mode: ListenerTlsModeType
    validation: Optional[ListenerTlsValidationContextTypeDef] = None

class ClientPolicyTlsTypeDef(BaseModel):
    validation: TlsValidationContextTypeDef
    certificate: Optional[ClientTlsCertificateTypeDef] = None
    enforce: Optional[bool] = None
    ports: Optional[Sequence[int]] = None

class VirtualGatewayListenerTlsTypeDef(BaseModel):
    certificate: VirtualGatewayListenerTlsCertificateTypeDef
    mode: VirtualGatewayListenerTlsModeType
    validation: Optional[VirtualGatewayListenerTlsValidationContextTypeDef] = None

class VirtualGatewayClientPolicyTlsTypeDef(BaseModel):
    validation: VirtualGatewayTlsValidationContextTypeDef
    certificate: Optional[VirtualGatewayClientTlsCertificateTypeDef] = None
    enforce: Optional[bool] = None
    ports: Optional[Sequence[int]] = None

class CreateVirtualServiceInputRequestTypeDef(BaseModel):
    meshName: str
    spec: VirtualServiceSpecTypeDef
    virtualServiceName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class UpdateVirtualServiceInputRequestTypeDef(BaseModel):
    meshName: str
    spec: VirtualServiceSpecTypeDef
    virtualServiceName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class VirtualServiceDataTypeDef(BaseModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualServiceSpecTypeDef
    status: VirtualServiceStatusTypeDef
    virtualServiceName: str

class GrpcGatewayRouteTypeDef(BaseModel):
    action: GrpcGatewayRouteActionTypeDef
    match: GrpcGatewayRouteMatchTypeDef

class GrpcRouteTypeDef(BaseModel):
    action: GrpcRouteActionTypeDef
    match: GrpcRouteMatchTypeDef
    retryPolicy: Optional[GrpcRetryPolicyTypeDef] = None
    timeout: Optional[GrpcTimeoutTypeDef] = None

class HttpGatewayRouteTypeDef(BaseModel):
    action: HttpGatewayRouteActionTypeDef
    match: HttpGatewayRouteMatchTypeDef

class HttpRouteTypeDef(BaseModel):
    action: HttpRouteActionTypeDef
    match: HttpRouteMatchTypeDef
    retryPolicy: Optional[HttpRetryPolicyTypeDef] = None
    timeout: Optional[HttpTimeoutTypeDef] = None

class LoggingTypeDef(BaseModel):
    accessLog: Optional[AccessLogTypeDef] = None

class VirtualGatewayLoggingTypeDef(BaseModel):
    accessLog: Optional[VirtualGatewayAccessLogTypeDef] = None

class CreateVirtualRouterOutputTypeDef(BaseModel):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualRouterOutputTypeDef(BaseModel):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualRouterOutputTypeDef(BaseModel):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualRouterOutputTypeDef(BaseModel):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTypeDef(BaseModel):
    portMapping: PortMappingTypeDef
    connectionPool: Optional[VirtualNodeConnectionPoolTypeDef] = None
    healthCheck: Optional[HealthCheckPolicyTypeDef] = None
    outlierDetection: Optional[OutlierDetectionTypeDef] = None
    timeout: Optional[ListenerTimeoutTypeDef] = None
    tls: Optional[ListenerTlsTypeDef] = None

class ClientPolicyTypeDef(BaseModel):
    tls: Optional[ClientPolicyTlsTypeDef] = None

class VirtualGatewayListenerTypeDef(BaseModel):
    portMapping: VirtualGatewayPortMappingTypeDef
    connectionPool: Optional[VirtualGatewayConnectionPoolTypeDef] = None
    healthCheck: Optional[VirtualGatewayHealthCheckPolicyTypeDef] = None
    tls: Optional[VirtualGatewayListenerTlsTypeDef] = None

class VirtualGatewayClientPolicyTypeDef(BaseModel):
    tls: Optional[VirtualGatewayClientPolicyTlsTypeDef] = None

class CreateVirtualServiceOutputTypeDef(BaseModel):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualServiceOutputTypeDef(BaseModel):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualServiceOutputTypeDef(BaseModel):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualServiceOutputTypeDef(BaseModel):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayRouteSpecTypeDef(BaseModel):
    grpcRoute: Optional[GrpcGatewayRouteTypeDef] = None
    http2Route: Optional[HttpGatewayRouteTypeDef] = None
    httpRoute: Optional[HttpGatewayRouteTypeDef] = None
    priority: Optional[int] = None

class RouteSpecTypeDef(BaseModel):
    grpcRoute: Optional[GrpcRouteTypeDef] = None
    http2Route: Optional[HttpRouteTypeDef] = None
    httpRoute: Optional[HttpRouteTypeDef] = None
    priority: Optional[int] = None
    tcpRoute: Optional[TcpRouteTypeDef] = None

class BackendDefaultsTypeDef(BaseModel):
    clientPolicy: Optional[ClientPolicyTypeDef] = None

class VirtualServiceBackendTypeDef(BaseModel):
    virtualServiceName: str
    clientPolicy: Optional[ClientPolicyTypeDef] = None

class VirtualGatewayBackendDefaultsTypeDef(BaseModel):
    clientPolicy: Optional[VirtualGatewayClientPolicyTypeDef] = None

class CreateGatewayRouteInputRequestTypeDef(BaseModel):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class GatewayRouteDataTypeDef(BaseModel):
    gatewayRouteName: str
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: GatewayRouteSpecTypeDef
    status: GatewayRouteStatusTypeDef
    virtualGatewayName: str

class UpdateGatewayRouteInputRequestTypeDef(BaseModel):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class CreateRouteInputRequestTypeDef(BaseModel):
    meshName: str
    routeName: str
    spec: RouteSpecTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class RouteDataTypeDef(BaseModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    routeName: str
    spec: RouteSpecTypeDef
    status: RouteStatusTypeDef
    virtualRouterName: str

class UpdateRouteInputRequestTypeDef(BaseModel):
    meshName: str
    routeName: str
    spec: RouteSpecTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class BackendTypeDef(BaseModel):
    virtualService: Optional[VirtualServiceBackendTypeDef] = None

class VirtualGatewaySpecTypeDef(BaseModel):
    listeners: Sequence[VirtualGatewayListenerTypeDef]
    backendDefaults: Optional[VirtualGatewayBackendDefaultsTypeDef] = None
    logging: Optional[VirtualGatewayLoggingTypeDef] = None

class CreateGatewayRouteOutputTypeDef(BaseModel):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayRouteOutputTypeDef(BaseModel):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayRouteOutputTypeDef(BaseModel):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayRouteOutputTypeDef(BaseModel):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteOutputTypeDef(BaseModel):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRouteOutputTypeDef(BaseModel):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRouteOutputTypeDef(BaseModel):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouteOutputTypeDef(BaseModel):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualNodeSpecTypeDef(BaseModel):
    backendDefaults: Optional[BackendDefaultsTypeDef] = None
    backends: Optional[Sequence[BackendTypeDef]] = None
    listeners: Optional[Sequence[ListenerTypeDef]] = None
    logging: Optional[LoggingTypeDef] = None
    serviceDiscovery: Optional[ServiceDiscoveryTypeDef] = None

class CreateVirtualGatewayInputRequestTypeDef(BaseModel):
    meshName: str
    spec: VirtualGatewaySpecTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class UpdateVirtualGatewayInputRequestTypeDef(BaseModel):
    meshName: str
    spec: VirtualGatewaySpecTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class VirtualGatewayDataTypeDef(BaseModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualGatewaySpecTypeDef
    status: VirtualGatewayStatusTypeDef
    virtualGatewayName: str

class CreateVirtualNodeInputRequestTypeDef(BaseModel):
    meshName: str
    spec: VirtualNodeSpecTypeDef
    virtualNodeName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class UpdateVirtualNodeInputRequestTypeDef(BaseModel):
    meshName: str
    spec: VirtualNodeSpecTypeDef
    virtualNodeName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class VirtualNodeDataTypeDef(BaseModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualNodeSpecTypeDef
    status: VirtualNodeStatusTypeDef
    virtualNodeName: str

class CreateVirtualGatewayOutputTypeDef(BaseModel):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualGatewayOutputTypeDef(BaseModel):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualGatewayOutputTypeDef(BaseModel):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualGatewayOutputTypeDef(BaseModel):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualNodeOutputTypeDef(BaseModel):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualNodeOutputTypeDef(BaseModel):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualNodeOutputTypeDef(BaseModel):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualNodeOutputTypeDef(BaseModel):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

