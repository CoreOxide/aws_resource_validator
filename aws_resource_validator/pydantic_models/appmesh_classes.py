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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteGatewayRouteInputTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None


class DeleteMeshInputTypeDef(BaseValidatorModel):
    meshName: str


class DeleteRouteInputTypeDef(BaseValidatorModel):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None


class DeleteVirtualGatewayInputTypeDef(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None


class DeleteVirtualNodeInputTypeDef(BaseValidatorModel):
    meshName: str
    virtualNodeName: str
    meshOwner: Optional[str] = None


class DeleteVirtualRouterInputTypeDef(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None


class DeleteVirtualServiceInputTypeDef(BaseValidatorModel):
    meshName: str
    virtualServiceName: str
    meshOwner: Optional[str] = None


class DescribeGatewayRouteInputTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None


class DescribeMeshInputTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None


class DescribeRouteInputTypeDef(BaseValidatorModel):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None


class DescribeVirtualGatewayInputTypeDef(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None


class DescribeVirtualNodeInputTypeDef(BaseValidatorModel):
    meshName: str
    virtualNodeName: str
    meshOwner: Optional[str] = None


class DescribeVirtualRouterInputTypeDef(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None


class DescribeVirtualServiceInputTypeDef(BaseValidatorModel):
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


class ListGatewayRoutesInputTypeDef(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    limit: Optional[int] = None
    meshOwner: Optional[str] = None
    nextToken: Optional[str] = None


class ListMeshesInputTypeDef(BaseValidatorModel):
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


class ListRoutesInputTypeDef(BaseValidatorModel):
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


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    limit: Optional[int] = None
    nextToken: Optional[str] = None


class ListVirtualGatewaysInputTypeDef(BaseValidatorModel):
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


class ListVirtualNodesInputTypeDef(BaseValidatorModel):
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


class ListVirtualRoutersInputTypeDef(BaseValidatorModel):
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


class ListVirtualServicesInputTypeDef(BaseValidatorModel):
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


class PortMappingTypeDef(BaseValidatorModel):
    port: int
    protocol: PortProtocolType


class ListenerTlsAcmCertificateTypeDef(BaseValidatorModel):
    certificateArn: str


class TlsValidationContextFileTrustTypeDef(BaseValidatorModel):
    certificateChain: str


class TlsValidationContextSdsTrustTypeDef(BaseValidatorModel):
    secretName: str


class MeshStatusTypeDef(BaseValidatorModel):
    status: Optional[MeshStatusCodeType] = None


class MeshServiceDiscoveryTypeDef(BaseValidatorModel):
    ipPreference: Optional[IpPreferenceType] = None


class RouteStatusTypeDef(BaseValidatorModel):
    status: RouteStatusCodeType


class SubjectAlternativeNameMatchersOutputTypeDef(BaseValidatorModel):
    exact: List[str]


class SubjectAlternativeNameMatchersTypeDef(BaseValidatorModel):
    exact: Sequence[str]


class TcpRouteMatchTypeDef(BaseValidatorModel):
    port: Optional[int] = None


class TlsValidationContextAcmTrustOutputTypeDef(BaseValidatorModel):
    certificateAuthorityArns: List[str]


class TlsValidationContextAcmTrustTypeDef(BaseValidatorModel):
    certificateAuthorityArns: Sequence[str]


class UntagResourceInputTypeDef(BaseValidatorModel):
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


class VirtualGatewayPortMappingTypeDef(BaseValidatorModel):
    port: int
    protocol: VirtualGatewayPortProtocolType


class VirtualGatewayListenerTlsAcmCertificateTypeDef(BaseValidatorModel):
    certificateArn: str


class VirtualGatewayTlsValidationContextFileTrustTypeDef(BaseValidatorModel):
    certificateChain: str


class VirtualGatewayTlsValidationContextSdsTrustTypeDef(BaseValidatorModel):
    secretName: str


class VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef(BaseValidatorModel):
    certificateAuthorityArns: List[str]


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


class AwsCloudMapServiceDiscoveryOutputTypeDef(BaseValidatorModel):
    namespaceName: str
    serviceName: str
    attributes: Optional[List[AwsCloudMapInstanceAttributeTypeDef]] = None
    ipPreference: Optional[IpPreferenceType] = None


class AwsCloudMapServiceDiscoveryTypeDef(BaseValidatorModel):
    namespaceName: str
    serviceName: str
    attributes: Optional[Sequence[AwsCloudMapInstanceAttributeTypeDef]] = None
    ipPreference: Optional[IpPreferenceType] = None


class ClientTlsCertificateTypeDef(BaseValidatorModel):
    file: Optional[ListenerTlsFileCertificateTypeDef] = None
    sds: Optional[ListenerTlsSdsCertificateTypeDef] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagRefTypeDef]


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: List[TagRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GrpcRetryPolicyOutputTypeDef(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    grpcRetryEvents: Optional[List[GrpcRetryPolicyEventType]] = None
    httpRetryEvents: Optional[List[str]] = None
    tcpRetryEvents: Optional[List[Literal["connection-error"]]] = None


class GrpcRetryPolicyTypeDef(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    grpcRetryEvents: Optional[Sequence[GrpcRetryPolicyEventType]] = None
    httpRetryEvents: Optional[Sequence[str]] = None
    tcpRetryEvents: Optional[Sequence[Literal["connection-error"]]] = None


class GrpcTimeoutTypeDef(BaseValidatorModel):
    idle: Optional[DurationTypeDef] = None
    perRequest: Optional[DurationTypeDef] = None


class HttpRetryPolicyOutputTypeDef(BaseValidatorModel):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    httpRetryEvents: Optional[List[str]] = None
    tcpRetryEvents: Optional[List[Literal["connection-error"]]] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GatewayRouteTargetTypeDef(BaseValidatorModel):
    virtualService: GatewayRouteVirtualServiceTypeDef
    port: Optional[int] = None


class GrpcRouteActionOutputTypeDef(BaseValidatorModel):
    weightedTargets: List[WeightedTargetTypeDef]


class GrpcRouteActionTypeDef(BaseValidatorModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]


class HttpRouteActionOutputTypeDef(BaseValidatorModel):
    weightedTargets: List[WeightedTargetTypeDef]


class HttpRouteActionTypeDef(BaseValidatorModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]


class TcpRouteActionOutputTypeDef(BaseValidatorModel):
    weightedTargets: List[WeightedTargetTypeDef]


class TcpRouteActionTypeDef(BaseValidatorModel):
    weightedTargets: Sequence[WeightedTargetTypeDef]


class HttpGatewayRouteRewriteTypeDef(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameRewriteTypeDef] = None
    path: Optional[HttpGatewayRoutePathRewriteTypeDef] = None
    prefix: Optional[HttpGatewayRoutePrefixRewriteTypeDef] = None


class HttpQueryParameterTypeDef(BaseValidatorModel):
    name: str
    match: Optional[QueryParameterMatchTypeDef] = None


class LoggingFormatOutputTypeDef(BaseValidatorModel):
    json: Optional[List[JsonFormatRefTypeDef]] = None
    text: Optional[str] = None


class LoggingFormatTypeDef(BaseValidatorModel):
    json: Optional[Sequence[JsonFormatRefTypeDef]] = None
    text: Optional[str] = None


class ListGatewayRoutesInputPaginateTypeDef(BaseValidatorModel):
    meshName: str
    virtualGatewayName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMeshesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRoutesInputPaginateTypeDef(BaseValidatorModel):
    meshName: str
    virtualRouterName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceInputPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVirtualGatewaysInputPaginateTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVirtualNodesInputPaginateTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVirtualRoutersInputPaginateTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVirtualServicesInputPaginateTypeDef(BaseValidatorModel):
    meshName: str
    meshOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMeshesOutputTypeDef(BaseValidatorModel):
    meshes: List[MeshRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRoutesOutputTypeDef(BaseValidatorModel):
    routes: List[RouteRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListVirtualGatewaysOutputTypeDef(BaseValidatorModel):
    virtualGateways: List[VirtualGatewayRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListVirtualNodesOutputTypeDef(BaseValidatorModel):
    virtualNodes: List[VirtualNodeRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListVirtualRoutersOutputTypeDef(BaseValidatorModel):
    virtualRouters: List[VirtualRouterRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListVirtualServicesOutputTypeDef(BaseValidatorModel):
    virtualServices: List[VirtualServiceRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class VirtualRouterListenerTypeDef(BaseValidatorModel):
    portMapping: PortMappingTypeDef


class ListenerTlsCertificateTypeDef(BaseValidatorModel):
    acm: Optional[ListenerTlsAcmCertificateTypeDef] = None
    file: Optional[ListenerTlsFileCertificateTypeDef] = None
    sds: Optional[ListenerTlsSdsCertificateTypeDef] = None


class ListenerTlsValidationContextTrustTypeDef(BaseValidatorModel):
    file: Optional[TlsValidationContextFileTrustTypeDef] = None
    sds: Optional[TlsValidationContextSdsTrustTypeDef] = None


class EgressFilterTypeDef(BaseValidatorModel):
    pass


class MeshSpecTypeDef(BaseValidatorModel):
    egressFilter: Optional[EgressFilterTypeDef] = None
    serviceDiscovery: Optional[MeshServiceDiscoveryTypeDef] = None


class SubjectAlternativeNamesOutputTypeDef(BaseValidatorModel):
    match: SubjectAlternativeNameMatchersOutputTypeDef


class SubjectAlternativeNamesTypeDef(BaseValidatorModel):
    match: SubjectAlternativeNameMatchersTypeDef


class TlsValidationContextTrustOutputTypeDef(BaseValidatorModel):
    acm: Optional[TlsValidationContextAcmTrustOutputTypeDef] = None
    file: Optional[TlsValidationContextFileTrustTypeDef] = None
    sds: Optional[TlsValidationContextSdsTrustTypeDef] = None


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


class VirtualGatewayTlsValidationContextTrustOutputTypeDef(BaseValidatorModel):
    acm: Optional[VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef] = None
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


class ServiceDiscoveryOutputTypeDef(BaseValidatorModel):
    awsCloudMap: Optional[AwsCloudMapServiceDiscoveryOutputTypeDef] = None
    dns: Optional[DnsServiceDiscoveryTypeDef] = None


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


class GrpcMetadataMatchMethodTypeDef(BaseValidatorModel):
    pass


class GrpcGatewayRouteMetadataTypeDef(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[GrpcMetadataMatchMethodTypeDef] = None


class GrpcRouteMetadataMatchMethodTypeDef(BaseValidatorModel):
    pass


class GrpcRouteMetadataTypeDef(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[GrpcRouteMetadataMatchMethodTypeDef] = None


class HeaderMatchMethodTypeDef(BaseValidatorModel):
    pass


class HttpGatewayRouteHeaderTypeDef(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[HeaderMatchMethodTypeDef] = None


class HttpRouteHeaderTypeDef(BaseValidatorModel):
    name: str
    invert: Optional[bool] = None
    match: Optional[HeaderMatchMethodTypeDef] = None


class TcpRouteOutputTypeDef(BaseValidatorModel):
    action: TcpRouteActionOutputTypeDef
    match: Optional[TcpRouteMatchTypeDef] = None
    timeout: Optional[TcpTimeoutTypeDef] = None


class TcpRouteTypeDef(BaseValidatorModel):
    action: TcpRouteActionTypeDef
    match: Optional[TcpRouteMatchTypeDef] = None
    timeout: Optional[TcpTimeoutTypeDef] = None


class HttpGatewayRouteActionTypeDef(BaseValidatorModel):
    target: GatewayRouteTargetTypeDef
    rewrite: Optional[HttpGatewayRouteRewriteTypeDef] = None


class VirtualRouterSpecOutputTypeDef(BaseValidatorModel):
    listeners: Optional[List[VirtualRouterListenerTypeDef]] = None


class VirtualRouterSpecTypeDef(BaseValidatorModel):
    listeners: Optional[Sequence[VirtualRouterListenerTypeDef]] = None


class CreateMeshInputTypeDef(BaseValidatorModel):
    meshName: str
    clientToken: Optional[str] = None
    spec: Optional[MeshSpecTypeDef] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None


class MeshDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: MeshSpecTypeDef
    status: MeshStatusTypeDef


class UpdateMeshInputTypeDef(BaseValidatorModel):
    meshName: str
    clientToken: Optional[str] = None
    spec: Optional[MeshSpecTypeDef] = None


class ListenerTlsValidationContextOutputTypeDef(BaseValidatorModel):
    trust: ListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesOutputTypeDef] = None


class ListenerTlsValidationContextTypeDef(BaseValidatorModel):
    trust: ListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None


class TlsValidationContextOutputTypeDef(BaseValidatorModel):
    trust: TlsValidationContextTrustOutputTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesOutputTypeDef] = None


class TlsValidationContextTypeDef(BaseValidatorModel):
    trust: TlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None


class VirtualGatewayListenerTlsValidationContextOutputTypeDef(BaseValidatorModel):
    trust: VirtualGatewayListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesOutputTypeDef] = None


class VirtualGatewayListenerTlsValidationContextTypeDef(BaseValidatorModel):
    trust: VirtualGatewayListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None


class VirtualGatewayTlsValidationContextOutputTypeDef(BaseValidatorModel):
    trust: VirtualGatewayTlsValidationContextTrustOutputTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesOutputTypeDef] = None


class VirtualGatewayTlsValidationContextTypeDef(BaseValidatorModel):
    trust: VirtualGatewayTlsValidationContextTrustTypeDef
    subjectAlternativeNames: Optional[SubjectAlternativeNamesTypeDef] = None


class VirtualServiceSpecTypeDef(BaseValidatorModel):
    provider: Optional[VirtualServiceProviderTypeDef] = None


class GrpcGatewayRouteMatchOutputTypeDef(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameMatchTypeDef] = None
    metadata: Optional[List[GrpcGatewayRouteMetadataTypeDef]] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None


class GrpcGatewayRouteMatchTypeDef(BaseValidatorModel):
    hostname: Optional[GatewayRouteHostnameMatchTypeDef] = None
    metadata: Optional[Sequence[GrpcGatewayRouteMetadataTypeDef]] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None


class GrpcRouteMatchOutputTypeDef(BaseValidatorModel):
    metadata: Optional[List[GrpcRouteMetadataTypeDef]] = None
    methodName: Optional[str] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None


class GrpcRouteMatchTypeDef(BaseValidatorModel):
    metadata: Optional[Sequence[GrpcRouteMetadataTypeDef]] = None
    methodName: Optional[str] = None
    port: Optional[int] = None
    serviceName: Optional[str] = None


class HttpGatewayRouteMatchOutputTypeDef(BaseValidatorModel):
    headers: Optional[List[HttpGatewayRouteHeaderTypeDef]] = None
    hostname: Optional[GatewayRouteHostnameMatchTypeDef] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatchTypeDef] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[List[HttpQueryParameterTypeDef]] = None


class HttpGatewayRouteMatchTypeDef(BaseValidatorModel):
    headers: Optional[Sequence[HttpGatewayRouteHeaderTypeDef]] = None
    hostname: Optional[GatewayRouteHostnameMatchTypeDef] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatchTypeDef] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[Sequence[HttpQueryParameterTypeDef]] = None


class HttpRouteMatchOutputTypeDef(BaseValidatorModel):
    headers: Optional[List[HttpRouteHeaderTypeDef]] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatchTypeDef] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[List[HttpQueryParameterTypeDef]] = None
    scheme: Optional[HttpSchemeType] = None


class HttpRouteMatchTypeDef(BaseValidatorModel):
    headers: Optional[Sequence[HttpRouteHeaderTypeDef]] = None
    method: Optional[HttpMethodType] = None
    path: Optional[HttpPathMatchTypeDef] = None
    port: Optional[int] = None
    prefix: Optional[str] = None
    queryParameters: Optional[Sequence[HttpQueryParameterTypeDef]] = None
    scheme: Optional[HttpSchemeType] = None


class FileAccessLogOutputTypeDef(BaseValidatorModel):
    pass


class AccessLogOutputTypeDef(BaseValidatorModel):
    file: Optional[FileAccessLogOutputTypeDef] = None


class VirtualGatewayFileAccessLogOutputTypeDef(BaseValidatorModel):
    pass


class VirtualGatewayAccessLogOutputTypeDef(BaseValidatorModel):
    file: Optional[VirtualGatewayFileAccessLogOutputTypeDef] = None


class FileAccessLogTypeDef(BaseValidatorModel):
    pass


class AccessLogTypeDef(BaseValidatorModel):
    file: Optional[FileAccessLogTypeDef] = None


class VirtualGatewayFileAccessLogTypeDef(BaseValidatorModel):
    pass


class VirtualGatewayAccessLogTypeDef(BaseValidatorModel):
    file: Optional[VirtualGatewayFileAccessLogTypeDef] = None


class VirtualRouterDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualRouterSpecOutputTypeDef
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


class ListenerTlsOutputTypeDef(BaseValidatorModel):
    certificate: ListenerTlsCertificateTypeDef
    mode: ListenerTlsModeType
    validation: Optional[ListenerTlsValidationContextOutputTypeDef] = None


class ListenerTlsTypeDef(BaseValidatorModel):
    certificate: ListenerTlsCertificateTypeDef
    mode: ListenerTlsModeType
    validation: Optional[ListenerTlsValidationContextTypeDef] = None


class ClientPolicyTlsOutputTypeDef(BaseValidatorModel):
    validation: TlsValidationContextOutputTypeDef
    certificate: Optional[ClientTlsCertificateTypeDef] = None
    enforce: Optional[bool] = None
    ports: Optional[List[int]] = None


class ClientPolicyTlsTypeDef(BaseValidatorModel):
    validation: TlsValidationContextTypeDef
    certificate: Optional[ClientTlsCertificateTypeDef] = None
    enforce: Optional[bool] = None
    ports: Optional[Sequence[int]] = None


class VirtualGatewayListenerTlsOutputTypeDef(BaseValidatorModel):
    certificate: VirtualGatewayListenerTlsCertificateTypeDef
    mode: VirtualGatewayListenerTlsModeType
    validation: Optional[VirtualGatewayListenerTlsValidationContextOutputTypeDef] = None


class VirtualGatewayListenerTlsTypeDef(BaseValidatorModel):
    certificate: VirtualGatewayListenerTlsCertificateTypeDef
    mode: VirtualGatewayListenerTlsModeType
    validation: Optional[VirtualGatewayListenerTlsValidationContextTypeDef] = None


class VirtualGatewayClientPolicyTlsOutputTypeDef(BaseValidatorModel):
    validation: VirtualGatewayTlsValidationContextOutputTypeDef
    certificate: Optional[VirtualGatewayClientTlsCertificateTypeDef] = None
    enforce: Optional[bool] = None
    ports: Optional[List[int]] = None


class VirtualGatewayClientPolicyTlsTypeDef(BaseValidatorModel):
    validation: VirtualGatewayTlsValidationContextTypeDef
    certificate: Optional[VirtualGatewayClientTlsCertificateTypeDef] = None
    enforce: Optional[bool] = None
    ports: Optional[Sequence[int]] = None


class CreateVirtualServiceInputTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualServiceSpecTypeDef
    virtualServiceName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None


class UpdateVirtualServiceInputTypeDef(BaseValidatorModel):
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


class GrpcGatewayRouteOutputTypeDef(BaseValidatorModel):
    action: GrpcGatewayRouteActionTypeDef
    match: GrpcGatewayRouteMatchOutputTypeDef


class GrpcGatewayRouteTypeDef(BaseValidatorModel):
    action: GrpcGatewayRouteActionTypeDef
    match: GrpcGatewayRouteMatchTypeDef


class GrpcRouteOutputTypeDef(BaseValidatorModel):
    action: GrpcRouteActionOutputTypeDef
    match: GrpcRouteMatchOutputTypeDef
    retryPolicy: Optional[GrpcRetryPolicyOutputTypeDef] = None
    timeout: Optional[GrpcTimeoutTypeDef] = None


class GrpcRouteTypeDef(BaseValidatorModel):
    action: GrpcRouteActionTypeDef
    match: GrpcRouteMatchTypeDef
    retryPolicy: Optional[GrpcRetryPolicyTypeDef] = None
    timeout: Optional[GrpcTimeoutTypeDef] = None


class HttpGatewayRouteOutputTypeDef(BaseValidatorModel):
    action: HttpGatewayRouteActionTypeDef
    match: HttpGatewayRouteMatchOutputTypeDef


class HttpGatewayRouteTypeDef(BaseValidatorModel):
    action: HttpGatewayRouteActionTypeDef
    match: HttpGatewayRouteMatchTypeDef


class HttpRouteOutputTypeDef(BaseValidatorModel):
    action: HttpRouteActionOutputTypeDef
    match: HttpRouteMatchOutputTypeDef
    retryPolicy: Optional[HttpRetryPolicyOutputTypeDef] = None
    timeout: Optional[HttpTimeoutTypeDef] = None


class HttpRouteTypeDef(BaseValidatorModel):
    action: HttpRouteActionTypeDef
    match: HttpRouteMatchTypeDef
    retryPolicy: Optional[HttpRetryPolicyTypeDef] = None
    timeout: Optional[HttpTimeoutTypeDef] = None


class LoggingOutputTypeDef(BaseValidatorModel):
    accessLog: Optional[AccessLogOutputTypeDef] = None


class VirtualGatewayLoggingOutputTypeDef(BaseValidatorModel):
    accessLog: Optional[VirtualGatewayAccessLogOutputTypeDef] = None


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


class VirtualRouterSpecUnionTypeDef(BaseValidatorModel):
    pass


class CreateVirtualRouterInputTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualRouterSpecUnionTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None


class UpdateVirtualRouterInputTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualRouterSpecUnionTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


class ListenerOutputTypeDef(BaseValidatorModel):
    portMapping: PortMappingTypeDef
    connectionPool: Optional[VirtualNodeConnectionPoolTypeDef] = None
    healthCheck: Optional[HealthCheckPolicyTypeDef] = None
    outlierDetection: Optional[OutlierDetectionTypeDef] = None
    timeout: Optional[ListenerTimeoutTypeDef] = None
    tls: Optional[ListenerTlsOutputTypeDef] = None


class ListenerTypeDef(BaseValidatorModel):
    portMapping: PortMappingTypeDef
    connectionPool: Optional[VirtualNodeConnectionPoolTypeDef] = None
    healthCheck: Optional[HealthCheckPolicyTypeDef] = None
    outlierDetection: Optional[OutlierDetectionTypeDef] = None
    timeout: Optional[ListenerTimeoutTypeDef] = None
    tls: Optional[ListenerTlsTypeDef] = None


class ClientPolicyOutputTypeDef(BaseValidatorModel):
    tls: Optional[ClientPolicyTlsOutputTypeDef] = None


class ClientPolicyTypeDef(BaseValidatorModel):
    tls: Optional[ClientPolicyTlsTypeDef] = None


class VirtualGatewayListenerOutputTypeDef(BaseValidatorModel):
    portMapping: VirtualGatewayPortMappingTypeDef
    connectionPool: Optional[VirtualGatewayConnectionPoolTypeDef] = None
    healthCheck: Optional[VirtualGatewayHealthCheckPolicyTypeDef] = None
    tls: Optional[VirtualGatewayListenerTlsOutputTypeDef] = None


class VirtualGatewayListenerTypeDef(BaseValidatorModel):
    portMapping: VirtualGatewayPortMappingTypeDef
    connectionPool: Optional[VirtualGatewayConnectionPoolTypeDef] = None
    healthCheck: Optional[VirtualGatewayHealthCheckPolicyTypeDef] = None
    tls: Optional[VirtualGatewayListenerTlsTypeDef] = None


class VirtualGatewayClientPolicyOutputTypeDef(BaseValidatorModel):
    tls: Optional[VirtualGatewayClientPolicyTlsOutputTypeDef] = None


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


class GatewayRouteSpecOutputTypeDef(BaseValidatorModel):
    grpcRoute: Optional[GrpcGatewayRouteOutputTypeDef] = None
    http2Route: Optional[HttpGatewayRouteOutputTypeDef] = None
    httpRoute: Optional[HttpGatewayRouteOutputTypeDef] = None
    priority: Optional[int] = None


class GatewayRouteSpecTypeDef(BaseValidatorModel):
    grpcRoute: Optional[GrpcGatewayRouteTypeDef] = None
    http2Route: Optional[HttpGatewayRouteTypeDef] = None
    httpRoute: Optional[HttpGatewayRouteTypeDef] = None
    priority: Optional[int] = None


class RouteSpecOutputTypeDef(BaseValidatorModel):
    grpcRoute: Optional[GrpcRouteOutputTypeDef] = None
    http2Route: Optional[HttpRouteOutputTypeDef] = None
    httpRoute: Optional[HttpRouteOutputTypeDef] = None
    priority: Optional[int] = None
    tcpRoute: Optional[TcpRouteOutputTypeDef] = None


class RouteSpecTypeDef(BaseValidatorModel):
    grpcRoute: Optional[GrpcRouteTypeDef] = None
    http2Route: Optional[HttpRouteTypeDef] = None
    httpRoute: Optional[HttpRouteTypeDef] = None
    priority: Optional[int] = None
    tcpRoute: Optional[TcpRouteTypeDef] = None


class BackendDefaultsOutputTypeDef(BaseValidatorModel):
    clientPolicy: Optional[ClientPolicyOutputTypeDef] = None


class VirtualServiceBackendOutputTypeDef(BaseValidatorModel):
    virtualServiceName: str
    clientPolicy: Optional[ClientPolicyOutputTypeDef] = None


class BackendDefaultsTypeDef(BaseValidatorModel):
    clientPolicy: Optional[ClientPolicyTypeDef] = None


class VirtualServiceBackendTypeDef(BaseValidatorModel):
    virtualServiceName: str
    clientPolicy: Optional[ClientPolicyTypeDef] = None


class VirtualGatewayBackendDefaultsOutputTypeDef(BaseValidatorModel):
    clientPolicy: Optional[VirtualGatewayClientPolicyOutputTypeDef] = None


class VirtualGatewayBackendDefaultsTypeDef(BaseValidatorModel):
    clientPolicy: Optional[VirtualGatewayClientPolicyTypeDef] = None


class GatewayRouteDataTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: GatewayRouteSpecOutputTypeDef
    status: GatewayRouteStatusTypeDef
    virtualGatewayName: str


class RouteDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    routeName: str
    spec: RouteSpecOutputTypeDef
    status: RouteStatusTypeDef
    virtualRouterName: str


class BackendOutputTypeDef(BaseValidatorModel):
    virtualService: Optional[VirtualServiceBackendOutputTypeDef] = None


class BackendTypeDef(BaseValidatorModel):
    virtualService: Optional[VirtualServiceBackendTypeDef] = None


class VirtualGatewaySpecOutputTypeDef(BaseValidatorModel):
    listeners: List[VirtualGatewayListenerOutputTypeDef]
    backendDefaults: Optional[VirtualGatewayBackendDefaultsOutputTypeDef] = None
    logging: Optional[VirtualGatewayLoggingOutputTypeDef] = None


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


class GatewayRouteSpecUnionTypeDef(BaseValidatorModel):
    pass


class CreateGatewayRouteInputTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecUnionTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None


class UpdateGatewayRouteInputTypeDef(BaseValidatorModel):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecUnionTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


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


class RouteSpecUnionTypeDef(BaseValidatorModel):
    pass


class CreateRouteInputTypeDef(BaseValidatorModel):
    meshName: str
    routeName: str
    spec: RouteSpecUnionTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None


class UpdateRouteInputTypeDef(BaseValidatorModel):
    meshName: str
    routeName: str
    spec: RouteSpecUnionTypeDef
    virtualRouterName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


class VirtualNodeSpecOutputTypeDef(BaseValidatorModel):
    backendDefaults: Optional[BackendDefaultsOutputTypeDef] = None
    backends: Optional[List[BackendOutputTypeDef]] = None
    listeners: Optional[List[ListenerOutputTypeDef]] = None
    logging: Optional[LoggingOutputTypeDef] = None
    serviceDiscovery: Optional[ServiceDiscoveryOutputTypeDef] = None


class VirtualNodeSpecTypeDef(BaseValidatorModel):
    backendDefaults: Optional[BackendDefaultsTypeDef] = None
    backends: Optional[Sequence[BackendTypeDef]] = None
    listeners: Optional[Sequence[ListenerTypeDef]] = None
    logging: Optional[LoggingTypeDef] = None
    serviceDiscovery: Optional[ServiceDiscoveryTypeDef] = None


class VirtualGatewayDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualGatewaySpecOutputTypeDef
    status: VirtualGatewayStatusTypeDef
    virtualGatewayName: str


class VirtualNodeDataTypeDef(BaseValidatorModel):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualNodeSpecOutputTypeDef
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


class VirtualGatewaySpecUnionTypeDef(BaseValidatorModel):
    pass


class CreateVirtualGatewayInputTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualGatewaySpecUnionTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None


class UpdateVirtualGatewayInputTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualGatewaySpecUnionTypeDef
    virtualGatewayName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


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


class VirtualNodeSpecUnionTypeDef(BaseValidatorModel):
    pass


class CreateVirtualNodeInputTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualNodeSpecUnionTypeDef
    virtualNodeName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None
    tags: Optional[Sequence[TagRefTypeDef]] = None


class UpdateVirtualNodeInputTypeDef(BaseValidatorModel):
    meshName: str
    spec: VirtualNodeSpecUnionTypeDef
    virtualNodeName: str
    clientToken: Optional[str] = None
    meshOwner: Optional[str] = None


