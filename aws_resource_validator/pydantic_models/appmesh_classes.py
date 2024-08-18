from datetime import datetime
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
from aws_resource_validator.pydantic_models.appmesh_constants import *

class AwsCloudMapInstanceAttributeTypeDef(BaseValidatorModel):
    key: str
    value: str

class ListenerTlsFileCertificateTypeDef(BaseValidatorModel):
    certificateChain: str
    privateKey: str

class ListenerTlsSdsCertificateTypeDef(BaseValidatorModel):
    secretName: str

class TagRefTypeDef(BaseValidatorModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteGatewayRouteInputRequestTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None

class DeleteMeshInputRequestTypeDef(BaseValidatorModel):
    meshName: str

class DeleteRouteInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None

class DeleteVirtualGatewayInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None

class DeleteVirtualNodeInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualNodeName: str
    meshOwner: Optional[str] = None

class DeleteVirtualRouterInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None

class DeleteVirtualServiceInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualServiceName: str
    meshOwner: Optional[str] = None

class DescribeGatewayRouteInputRequestTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None

class DescribeMeshInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None

class DescribeRouteInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None

class DescribeVirtualGatewayInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None

class DescribeVirtualNodeInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualNodeName: str
    meshOwner: Optional[str] = None

class DescribeVirtualRouterInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None

class DescribeVirtualServiceInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualServiceName: str
    meshOwner: Optional[str] = None

class DnsServiceDiscoveryTypeDef(BaseValidatorModel):
    hostname: str
    ipPreference: Optional[IpPreferenceType] = None
    responseType: Optional[DnsResponseTypeType] = None

class DurationTypeDef(BaseValidatorModel):
    unit: Optional[DurationUnitType] = None
    value: Optional[int] = None

class EgressFilterTypeDef(BaseValidatorModel):
    type: EgressFilterTypeType

class GatewayRouteStatusTypeDef(BaseValidatorModel):
    status: GatewayRouteStatusCodeType

class ResourceMetadataTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshOwner: str
    resourceOwner: str
    uid: str
    version: int

class GatewayRouteHostnameMatchTypeDef(BaseValidatorModel):
    exact: Optional[str] = None
    suffix: Optional[str] = None

class GatewayRouteHostnameRewriteTypeDef(BaseValidatorModel):
    defaultTargetHostname: Optional[DefaultGatewayRouteRewriteType] = None

class GatewayRouteRefTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    gatewayRouteName: str
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str

class GatewayRouteVirtualServiceTypeDef(BaseValidatorModel):
    virtualServiceName: str

class MatchRangeTypeDef(BaseValidatorModel):
    end: int
    start: int

class WeightedTargetTypeDef(BaseValidatorModel):
    virtualNode: str
    weight: int
    port: Optional[int] = None

class HealthCheckPolicyTypeDef(BaseValidatorModel):
    healthyThreshold: int
    intervalMillis: int
    protocol: PortProtocolType
    timeoutMillis: int
    unhealthyThreshold: int
    path: Optional[str] = None
    port: Optional[int] = None

class HttpPathMatchTypeDef(BaseValidatorModel):
    exact: Optional[str] = None
    regex: Optional[str] = None

class HttpGatewayRoutePathRewriteTypeDef(BaseValidatorModel):
    exact: Optional[str] = None

class HttpGatewayRoutePrefixRewriteTypeDef(BaseValidatorModel):
    defaultPrefix: Optional[DefaultGatewayRouteRewriteType] = None
    value: Optional[str] = None

class QueryParameterMatchTypeDef(BaseValidatorModel):
    exact: Optional[str] = None

class JsonFormatRefTypeDef(BaseValidatorModel):
    key: str
    value: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListGatewayRoutesInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class ListMeshesInputRequestTypeDef(BaseValidatorModel):
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class MeshRefTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int

class ListRoutesInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class RouteRefTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    routeName: str
    version: int
    virtualRouterName: str

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class ListVirtualGatewaysInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class VirtualGatewayRefTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str

class ListVirtualNodesInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class VirtualNodeRefTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualNodeName: str

class ListVirtualRoutersInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class VirtualRouterRefTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualRouterName: str

class ListVirtualServicesInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None

class VirtualServiceRefTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualServiceName: str

class ListenerTlsAcmCertificateTypeDef(BaseValidatorModel):
    certificateArn: str

class TlsValidationContextFileTrustTypeDef(BaseValidatorModel):
    certificateChain: str

class TlsValidationContextSdsTrustTypeDef(BaseValidatorModel):
    secretName: str

class PortMappingTypeDef(BaseValidatorModel):
    port: int
    protocol: PortProtocolType

class MeshStatusTypeDef(BaseValidatorModel):
    status: Optional[MeshStatusCodeType] = None

class MeshServiceDiscoveryTypeDef(BaseValidatorModel):
    ipPreference: Optional[IpPreferenceType] = None

class RouteStatusTypeDef(BaseValidatorModel):
    status: RouteStatusCodeType

class SubjectAlternativeNameMatchersTypeDef(BaseValidatorModel):
    exact: Sequence[str]

class TcpRouteMatchTypeDef(BaseValidatorModel):
    port: Optional[int] = None

class TlsValidationContextAcmTrustTypeDef(BaseValidatorModel):
    certificateAuthorityArns: Sequence[str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class VirtualGatewayListenerTlsFileCertificateTypeDef(BaseValidatorModel):
    certificateChain: str
    privateKey: str

class VirtualGatewayListenerTlsSdsCertificateTypeDef(BaseValidatorModel):
    secretName: str

class VirtualGatewayGrpcConnectionPoolTypeDef(BaseValidatorModel):
    maxRequests: int

class VirtualGatewayHttp2ConnectionPoolTypeDef(BaseValidatorModel):
    maxRequests: int

class VirtualGatewayHttpConnectionPoolTypeDef(BaseValidatorModel):
    maxConnections: int
    maxPendingRequests: Optional[int] = None

class VirtualGatewayStatusTypeDef(BaseValidatorModel):
    status: VirtualGatewayStatusCodeType

class VirtualGatewayHealthCheckPolicyTypeDef(BaseValidatorModel):
    healthyThreshold: int
    intervalMillis: int
    protocol: VirtualGatewayPortProtocolType
    timeoutMillis: int
    unhealthyThreshold: int
    path: Optional[str] = None
    port: Optional[int] = None

class VirtualGatewayListenerTlsAcmCertificateTypeDef(BaseValidatorModel):
    certificateArn: str

class VirtualGatewayTlsValidationContextFileTrustTypeDef(BaseValidatorModel):
    certificateChain: str

class VirtualGatewayTlsValidationContextSdsTrustTypeDef(BaseValidatorModel):
    secretName: str

class VirtualGatewayPortMappingTypeDef(BaseValidatorModel):
    port: int
    protocol: VirtualGatewayPortProtocolType

class VirtualGatewayTlsValidationContextAcmTrustTypeDef(BaseValidatorModel):
    certificateAuthorityArns: Sequence[str]

class VirtualNodeGrpcConnectionPoolTypeDef(BaseValidatorModel):
    maxRequests: int

class VirtualNodeHttp2ConnectionPoolTypeDef(BaseValidatorModel):
    maxRequests: int

class VirtualNodeHttpConnectionPoolTypeDef(BaseValidatorModel):
    maxConnections: int
    maxPendingRequests: Optional[int] = None

class VirtualNodeTcpConnectionPoolTypeDef(BaseValidatorModel):
    maxConnections: int

class VirtualNodeStatusTypeDef(BaseValidatorModel):
    status: VirtualNodeStatusCodeType

class VirtualNodeServiceProviderTypeDef(BaseValidatorModel):
    virtualNodeName: str

class VirtualRouterStatusTypeDef(BaseValidatorModel):
    status: VirtualRouterStatusCodeType

class VirtualRouterServiceProviderTypeDef(BaseValidatorModel):
    virtualRouterName: str

class VirtualServiceStatusTypeDef(BaseValidatorModel):
    status: VirtualServiceStatusCodeType

class AwsCloudMapServiceDiscoveryTypeDef(BaseValidatorModel):
    namespaceName: str
    serviceName: str
    attributes: Optional[Sequence[AwsCloudMapInstanceAttributeTypeDef]] = None
    ipPreference: Optional[IpPreferenceType] = None

class ClientTlsCertificateTypeDef(BaseValidatorModel):
    file: Optional[ListenerTlsFileCertificateTypeDef] = None
    sds: Optional[ListenerTlsSdsCertificateTypeDef] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagRefTypeDef]

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    nextToken: str
    tags: List[TagRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GrpcRetryPolicyTypeDef(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    grpcRetryEvents: Optional[Sequence[GrpcRetryPolicyEventType]] = None
    httpRetryEvents: Optional[Sequence[str]] = None
    tcpRetryEvents: Optional[Sequence[Literal["connection-error"]]] = None

class GrpcTimeoutTypeDef(BaseValidatorModel):
    idle: Optional[DurationTypeDef] = None
    perRequest: Optional[DurationTypeDef] = None

class HttpRetryPolicyTypeDef(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    httpRetryEvents: Optional[Sequence[str]] = None
    tcpRetryEvents: Optional[Sequence[Literal["connection-error"]]] = None

class HttpTimeoutTypeDef(BaseValidatorModel):
    idle: Optional[DurationTypeDef] = None
    perRequest: Optional[DurationTypeDef] = None

class OutlierDetectionTypeDef(BaseValidatorModel):
    baseEjectionDuration: DurationTypeDef
    interval: DurationTypeDef
    maxEjectionPercent: int
    maxServerErrors: int

class TcpTimeoutTypeDef(BaseValidatorModel):
    idle: Optional[DurationTypeDef] = None

class GrpcGatewayRouteRewriteTypeDef(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameRewriteTypeDef] = None

class ListGatewayRoutesOutputTypeDef(BaseValidatorModel):
    gatewayRoutes: List[GatewayRouteRefTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayRouteTargetTypeDef(BaseValidatorModel):
    virtualService: GatewayRouteVirtualServiceTypeDef
    port: Optional[int] = None

class GrpcMetadataMatchMethodTypeDef(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRangeTypeDef] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None

class GrpcRouteMetadataMatchMethodTypeDef(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRangeTypeDef] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None

class HeaderMatchMethodTypeDef(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None
    range: Optional[MatchRangeTypeDef] = None
    regex: Optional[str] = None
    suffix: Optional[str] = None

class GrpcRouteActionTypeDef(BaseValidatorModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class HttpRouteActionTypeDef(BaseValidatorModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class TcpRouteActionTypeDef(BaseValidatorModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class HttpGatewayRouteRewriteTypeDef(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameRewriteTypeDef] = None
    path: Optional[HttpGatewayRoutePathRewriteTypeDef] = None
    prefix: Optional[HttpGatewayRoutePrefixRewriteTypeDef] = None

class HttpQueryParameterTypeDef(BaseValidatorModel):
    name: str
    match: Optional[QueryParameterMatchTypeDef] = None

class LoggingFormatTypeDef(BaseValidatorModel):
    json: Optional[Sequence[JsonFormatRefTypeDef]] = None
    text: Optional[str] = None

class ListGatewayRoutesInputListGatewayRoutesPaginateTypeDef(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMeshesInputListMeshesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutesInputListRoutesPaginateTypeDef(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualNodesInputListVirtualNodesPaginateTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualRoutersInputListVirtualRoutersPaginateTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVirtualServicesInputListVirtualServicesPaginateTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMeshesOutputTypeDef(BaseValidatorModel):
    meshes: List[MeshRefTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoutesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    routes: List[RouteRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualGatewaysOutputTypeDef(BaseValidatorModel):
    nextToken: str
    virtualGateways: List[VirtualGatewayRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualNodesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    virtualNodes: List[VirtualNodeRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualRoutersOutputTypeDef(BaseValidatorModel):
    nextToken: str
    virtualRouters: List[VirtualRouterRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualServicesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    virtualServices: List[VirtualServiceRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTlsCertificateTypeDef(BaseValidatorModel):
    acm: Optional[ListenerTlsAcmCertificateTypeDef] = None
    file: Optional[ListenerTlsFileCertificateTypeDef] = None
    sds: Optional[ListenerTlsSdsCertificateTypeDef] = None

class ListenerTlsValidationContextTrustTypeDef(BaseValidatorModel):
    file: Optional[TlsValidationContextFileTrustTypeDef] = None
    sds: Optional[TlsValidationContextSdsTrustTypeDef] = None

class VirtualRouterListenerTypeDef(BaseValidatorModel):
    portMapping: PortMappingTypeDef

class MeshSpecTypeDef(BaseValidatorModel):
    egressFilter: Optional[EgressFilterTypeDef] = None
    serviceDiscovery: Optional[MeshServiceDiscoveryTypeDef] = None

class SubjectAlternativeNamesTypeDef(BaseValidatorModel):
    match: SubjectAlternativeNameMatchersTypeDef

class TlsValidationContextTrustTypeDef(BaseValidatorModel):
    acm: Optional[TlsValidationContextAcmTrustTypeDef] = None
    file: Optional[TlsValidationContextFileTrustTypeDef] = None
    sds: Optional[TlsValidationContextSdsTrustTypeDef] = None

class VirtualGatewayClientTlsCertificateTypeDef(BaseValidatorModel):
    file: Optional[VirtualGatewayListenerTlsFileCertificateTypeDef] = None
    sds: Optional[VirtualGatewayListenerTlsSdsCertificateTypeDef] = None

class VirtualGatewayConnectionPoolTypeDef(BaseValidatorModel):
    grpc: Optional[VirtualGatewayGrpcConnectionPoolTypeDef] = None
    http: Optional[VirtualGatewayHttpConnectionPoolTypeDef] = None
    http2: Optional[VirtualGatewayHttp2ConnectionPoolTypeDef] = None

class VirtualGatewayListenerTlsCertificateTypeDef(BaseValidatorModel):
    acm: Optional[VirtualGatewayListenerTlsAcmCertificateTypeDef] = None
    file: Optional[VirtualGatewayListenerTlsFileCertificateTypeDef] = None
    sds: Optional[VirtualGatewayListenerTlsSdsCertificateTypeDef] = None

class VirtualGatewayListenerTlsValidationContextTrustTypeDef(BaseValidatorModel):
    file: Optional[VirtualGatewayTlsValidationContextFileTrustTypeDef] = None
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrustTypeDef] = None

class VirtualGatewayTlsValidationContextTrustTypeDef(BaseValidatorModel):
    acm: Optional[VirtualGatewayTlsValidationContextAcmTrustTypeDef] = None
    file: Optional[VirtualGatewayTlsValidationContextFileTrustTypeDef] = None
    sds: Optional[VirtualGatewayTlsValidationContextSdsTrustTypeDef] = None

class VirtualNodeConnectionPoolTypeDef(BaseValidatorModel):
    grpc: Optional[VirtualNodeGrpcConnectionPoolTypeDef] = None
    http: Optional[VirtualNodeHttpConnectionPoolTypeDef] = None
    http2: Optional[VirtualNodeHttp2ConnectionPoolTypeDef] = None
    tcp: Optional[VirtualNodeTcpConnectionPoolTypeDef] = None

class VirtualServiceProviderTypeDef(BaseValidatorModel):
    virtualNode: Optional[VirtualNodeServiceProviderTypeDef] = None
    virtualRouter: Optional[VirtualRouterServiceProviderTypeDef] = None

class ServiceDiscoveryTypeDef(BaseValidatorModel):
    awsCloudMap: Optional[AwsCloudMapServiceDiscoveryTypeDef] = None
    dns: Optional[DnsServiceDiscoveryTypeDef] = None

class ListenerTimeoutTypeDef(BaseValidatorModel):
    grpc: Optional[GrpcTimeoutTypeDef] = None
    http: Optional[HttpTimeoutTypeDef] = None
    http2: Optional[HttpTimeoutTypeDef] = None
    tcp: Optional[TcpTimeoutTypeDef] = None

class GrpcGatewayRouteActionTypeDef(BaseValidatorModel):
    target: GatewayRouteTargetTypeDef
    rewrite: Optional[GrpcGatewayRouteRewriteTypeDef] = None

class GrpcGatewayRouteMetadataTypeDef(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[GrpcMetadataMatchMethodTypeDef] = None

class GrpcRouteMetadataTypeDef(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[GrpcRouteMetadataMatchMethodTypeDef] = None

class HttpGatewayRouteHeaderTypeDef(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[HeaderMatchMethodTypeDef] = None

class HttpRouteHeaderTypeDef(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[HeaderMatchMethodTypeDef] = None

class TcpRouteTypeDef(BaseValidatorModel):
    action: TcpRouteActionTypeDef
    match: Optional[TcpRouteMatchTypeDef] = None
    timeout: Optional[TcpTimeoutTypeDef] = None

class HttpGatewayRouteActionTypeDef(BaseValidatorModel):
    target: GatewayRouteTargetTypeDef
    rewrite: Optional[HttpGatewayRouteRewriteTypeDef] = None

class FileAccessLogTypeDef(BaseValidatorModel):
    path: str
    format: Optional[LoggingFormatTypeDef] = None

class VirtualGatewayFileAccessLogTypeDef(BaseValidatorModel):
    path: str
    format: Optional[LoggingFormatTypeDef] = None

class VirtualRouterSpecTypeDef(BaseValidatorModel):
    listeners: Optional[Sequence[VirtualRouterListenerTypeDef]] = None

class CreateMeshInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    clientToken: Optional[str] = None
    spec: Optional[MeshSpecTypeDef] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class MeshDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: MeshSpecTypeDef
    status: MeshStatusTypeDef

class UpdateMeshInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    clientToken: Optional[str] = None
    spec: Optional[MeshSpecTypeDef] = None

class ListenerTlsValidationContextTypeDef(BaseValidatorModel):
    trust: ListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None

class TlsValidationContextTypeDef(BaseValidatorModel):
    trust: TlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None

class VirtualGatewayListenerTlsValidationContextTypeDef(BaseValidatorModel):
    trust: VirtualGatewayListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None

class VirtualGatewayTlsValidationContextTypeDef(BaseValidatorModel):
    trust: VirtualGatewayTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None

class VirtualServiceSpecTypeDef(BaseValidatorModel):
    provider: Optional[VirtualServiceProviderTypeDef] = None

class GrpcGatewayRouteMatchTypeDef(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameMatchTypeDef] = None
    metadata: Optional[Sequence[GrpcGatewayRouteMetadataTypeDef]] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None

class GrpcRouteMatchTypeDef(BaseValidatorModel):
    metadata: Optional[Sequence[GrpcRouteMetadataTypeDef]] = None
    methodName: Optional[str] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None

class HttpGatewayRouteMatchTypeDef(BaseValidatorModel):
    headers: Optional[Sequence[HttpGatewayRouteHeaderTypeDef]] = None
    hostname: Optional[GatewayRouteHostnameMatchTypeDef] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatchTypeDef] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[Sequence[HttpQueryParameterTypeDef]] = None

class HttpRouteMatchTypeDef(BaseValidatorModel):
    headers: Optional[Sequence[HttpRouteHeaderTypeDef]] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatchTypeDef] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[Sequence[HttpQueryParameterTypeDef]] = None
    scheme: Optional[HttpSchemeType] = None

class AccessLogTypeDef(BaseValidatorModel):
    file: Optional[FileAccessLogTypeDef] = None

class VirtualGatewayAccessLogTypeDef(BaseValidatorModel):
    file: Optional[VirtualGatewayFileAccessLogTypeDef] = None

class CreateVirtualRouterInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualRouterSpecTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class UpdateVirtualRouterInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualRouterSpecTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class VirtualRouterDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualRouterSpecTypeDef
    status: VirtualRouterStatusTypeDef
    virtualRouterName: str

class CreateMeshOutputTypeDef(BaseValidatorModel):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMeshOutputTypeDef(BaseValidatorModel):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMeshOutputTypeDef(BaseValidatorModel):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMeshOutputTypeDef(BaseValidatorModel):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTlsTypeDef(BaseValidatorModel):
    certificate: ListenerTlsCertificateTypeDef
    mode: ListenerTlsModeType
    validation: Optional[ListenerTlsValidationContextTypeDef] = None

class ClientPolicyTlsTypeDef(BaseValidatorModel):
    validation: TlsValidationContextTypeDef
    certificate: Optional[ClientTlsCertificateTypeDef] = None
    enforce: Optional[bool] = None
    ports: Optional[Sequence[int]] = None

class VirtualGatewayListenerTlsTypeDef(BaseValidatorModel):
    certificate: VirtualGatewayListenerTlsCertificateTypeDef
    mode: VirtualGatewayListenerTlsModeType
    validation: Optional[VirtualGatewayListenerTlsValidationContextTypeDef] = None

class VirtualGatewayClientPolicyTlsTypeDef(BaseValidatorModel):
    validation: VirtualGatewayTlsValidationContextTypeDef
    certificate: Optional[VirtualGatewayClientTlsCertificateTypeDef] = None
    enforce: Optional[bool] = None
    ports: Optional[Sequence[int]] = None

class CreateVirtualServiceInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualServiceSpecTypeDef
    virtualServiceName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class UpdateVirtualServiceInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualServiceSpecTypeDef
    virtualServiceName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class VirtualServiceDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualServiceSpecTypeDef
    status: VirtualServiceStatusTypeDef
    virtualServiceName: str

class GrpcGatewayRouteTypeDef(BaseValidatorModel):
    action: GrpcGatewayRouteActionTypeDef
    match: GrpcGatewayRouteMatchTypeDef

class GrpcRouteTypeDef(BaseValidatorModel):
    action: GrpcRouteActionTypeDef
    match: GrpcRouteMatchTypeDef
    retryPolicy: Optional[GrpcRetryPolicyTypeDef] = None
    timeout: Optional[GrpcTimeoutTypeDef] = None

class HttpGatewayRouteTypeDef(BaseValidatorModel):
    action: HttpGatewayRouteActionTypeDef
    match: HttpGatewayRouteMatchTypeDef

class HttpRouteTypeDef(BaseValidatorModel):
    action: HttpRouteActionTypeDef
    match: HttpRouteMatchTypeDef
    retryPolicy: Optional[HttpRetryPolicyTypeDef] = None
    timeout: Optional[HttpTimeoutTypeDef] = None

class LoggingTypeDef(BaseValidatorModel):
    accessLog: Optional[AccessLogTypeDef] = None

class VirtualGatewayLoggingTypeDef(BaseValidatorModel):
    accessLog: Optional[VirtualGatewayAccessLogTypeDef] = None

class CreateVirtualRouterOutputTypeDef(BaseValidatorModel):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualRouterOutputTypeDef(BaseValidatorModel):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualRouterOutputTypeDef(BaseValidatorModel):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualRouterOutputTypeDef(BaseValidatorModel):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTypeDef(BaseValidatorModel):
    portMapping: PortMappingTypeDef
    connectionPool: Optional[VirtualNodeConnectionPoolTypeDef] = None
    healthCheck: Optional[HealthCheckPolicyTypeDef] = None
    outlierDetection: Optional[OutlierDetectionTypeDef] = None
    timeout: Optional[ListenerTimeoutTypeDef] = None
    tls: Optional[ListenerTlsTypeDef] = None

class ClientPolicyTypeDef(BaseValidatorModel):
    tls: Optional[ClientPolicyTlsTypeDef] = None

class VirtualGatewayListenerTypeDef(BaseValidatorModel):
    portMapping: VirtualGatewayPortMappingTypeDef
    connectionPool: Optional[VirtualGatewayConnectionPoolTypeDef] = None
    healthCheck: Optional[VirtualGatewayHealthCheckPolicyTypeDef] = None
    tls: Optional[VirtualGatewayListenerTlsTypeDef] = None

class VirtualGatewayClientPolicyTypeDef(BaseValidatorModel):
    tls: Optional[VirtualGatewayClientPolicyTlsTypeDef] = None

class CreateVirtualServiceOutputTypeDef(BaseValidatorModel):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualServiceOutputTypeDef(BaseValidatorModel):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualServiceOutputTypeDef(BaseValidatorModel):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualServiceOutputTypeDef(BaseValidatorModel):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayRouteSpecTypeDef(BaseValidatorModel):
    grpcRoute: Optional[GrpcGatewayRouteTypeDef] = None
    http2Route: Optional[HttpGatewayRouteTypeDef] = None
    httpRoute: Optional[HttpGatewayRouteTypeDef] = None
    priority: Optional[int] = None

class RouteSpecTypeDef(BaseValidatorModel):
    grpcRoute: Optional[GrpcRouteTypeDef] = None
    http2Route: Optional[HttpRouteTypeDef] = None
    httpRoute: Optional[HttpRouteTypeDef] = None
    priority: Optional[int] = None
    tcpRoute: Optional[TcpRouteTypeDef] = None

class BackendDefaultsTypeDef(BaseValidatorModel):
    clientPolicy: Optional[ClientPolicyTypeDef] = None

class VirtualServiceBackendTypeDef(BaseValidatorModel):
    virtualServiceName: str
    clientPolicy: Optional[ClientPolicyTypeDef] = None

class VirtualGatewayBackendDefaultsTypeDef(BaseValidatorModel):
    clientPolicy: Optional[VirtualGatewayClientPolicyTypeDef] = None

class CreateGatewayRouteInputRequestTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class GatewayRouteDataTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: GatewayRouteSpecTypeDef
    status: GatewayRouteStatusTypeDef
    virtualGatewayName: str

class UpdateGatewayRouteInputRequestTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class CreateRouteInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    routeName: str
    spec: RouteSpecTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class RouteDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    routeName: str
    spec: RouteSpecTypeDef
    status: RouteStatusTypeDef
    virtualRouterName: str

class UpdateRouteInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    routeName: str
    spec: RouteSpecTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class BackendTypeDef(BaseValidatorModel):
    virtualService: Optional[VirtualServiceBackendTypeDef] = None

class VirtualGatewaySpecTypeDef(BaseValidatorModel):
    listeners: Sequence[VirtualGatewayListenerTypeDef]
    backendDefaults: Optional[VirtualGatewayBackendDefaultsTypeDef] = None
    logging: Optional[VirtualGatewayLoggingTypeDef] = None

class CreateGatewayRouteOutputTypeDef(BaseValidatorModel):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayRouteOutputTypeDef(BaseValidatorModel):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayRouteOutputTypeDef(BaseValidatorModel):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayRouteOutputTypeDef(BaseValidatorModel):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteOutputTypeDef(BaseValidatorModel):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRouteOutputTypeDef(BaseValidatorModel):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRouteOutputTypeDef(BaseValidatorModel):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouteOutputTypeDef(BaseValidatorModel):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualNodeSpecTypeDef(BaseValidatorModel):
    backendDefaults: Optional[BackendDefaultsTypeDef] = None
    backends: Optional[Sequence[BackendTypeDef]] = None
    listeners: Optional[Sequence[ListenerTypeDef]] = None
    logging: Optional[LoggingTypeDef] = None
    serviceDiscovery: Optional[ServiceDiscoveryTypeDef] = None

class CreateVirtualGatewayInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualGatewaySpecTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class UpdateVirtualGatewayInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualGatewaySpecTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class VirtualGatewayDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualGatewaySpecTypeDef
    status: VirtualGatewayStatusTypeDef
    virtualGatewayName: str

class CreateVirtualNodeInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualNodeSpecTypeDef
    virtualNodeName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None

class UpdateVirtualNodeInputRequestTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualNodeSpecTypeDef
    virtualNodeName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None

class VirtualNodeDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualNodeSpecTypeDef
    status: VirtualNodeStatusTypeDef
    virtualNodeName: str

class CreateVirtualGatewayOutputTypeDef(BaseValidatorModel):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualGatewayOutputTypeDef(BaseValidatorModel):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualGatewayOutputTypeDef(BaseValidatorModel):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualGatewayOutputTypeDef(BaseValidatorModel):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualNodeOutputTypeDef(BaseValidatorModel):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualNodeOutputTypeDef(BaseValidatorModel):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualNodeOutputTypeDef(BaseValidatorModel):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualNodeOutputTypeDef(BaseValidatorModel):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

