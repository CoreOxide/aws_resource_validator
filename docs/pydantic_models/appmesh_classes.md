# appmesh_classes

# AccessLogTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.FileAccessLogTypeDef]


# AwsCloudMapInstanceAttributeTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# AwsCloudMapServiceDiscoveryTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapInstanceAttributeTypeDef]]

### ipPreference
- **Type**: typing.Optional[typing.Literal['IPv4_ONLY', 'IPv4_PREFERRED', 'IPv6_ONLY', 'IPv6_PREFERRED']]


# BackendDefaultsTypeDef

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyTypeDef]


# BackendTypeDef

### virtualService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceBackendTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientPolicyTlsTypeDef

### validation
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextTypeDef'>
- **Required**: Yes

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientTlsCertificateTypeDef]

### enforce
- **Type**: typing.Optional[bool]

### ports
- **Type**: typing.Optional[typing.Sequence[int]]


# ClientPolicyTypeDef

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyTlsTypeDef]


# ClientTlsCertificateTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsFileCertificateTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsSdsCertificateTypeDef]


# CreateGatewayRouteInputRequestTypeDef

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecTypeDef'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]]


# CreateGatewayRouteOutputTypeDef

### gatewayRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMeshInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MeshSpecTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]]


# CreateMeshOutputTypeDef

### mesh
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRouteInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecTypeDef'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]]


# CreateRouteOutputTypeDef

### route
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVirtualGatewayInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecTypeDef'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]]


# CreateVirtualGatewayOutputTypeDef

### virtualGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVirtualNodeInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecTypeDef'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]]


# CreateVirtualNodeOutputTypeDef

### virtualNode
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVirtualRouterInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecTypeDef'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]]


# CreateVirtualRouterOutputTypeDef

### virtualRouter
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVirtualServiceInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceSpecTypeDef'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]]


# CreateVirtualServiceOutputTypeDef

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGatewayRouteInputRequestTypeDef

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteGatewayRouteOutputTypeDef

### gatewayRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMeshInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMeshOutputTypeDef

### mesh
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRouteInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteRouteOutputTypeDef

### route
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVirtualGatewayInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteVirtualGatewayOutputTypeDef

### virtualGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVirtualNodeInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteVirtualNodeOutputTypeDef

### virtualNode
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVirtualRouterInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteVirtualRouterOutputTypeDef

### virtualRouter
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVirtualServiceInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteVirtualServiceOutputTypeDef

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGatewayRouteInputRequestTypeDef

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeGatewayRouteOutputTypeDef

### gatewayRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMeshInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeMeshOutputTypeDef

### mesh
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRouteInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeRouteOutputTypeDef

### route
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVirtualGatewayInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeVirtualGatewayOutputTypeDef

### virtualGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVirtualNodeInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeVirtualNodeOutputTypeDef

### virtualNode
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVirtualRouterInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeVirtualRouterOutputTypeDef

### virtualRouter
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVirtualServiceInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeVirtualServiceOutputTypeDef

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DnsServiceDiscoveryTypeDef

### hostname
- **Type**: <class 'str'>
- **Required**: Yes

### ipPreference
- **Type**: typing.Optional[typing.Literal['IPv4_ONLY', 'IPv4_PREFERRED', 'IPv6_ONLY', 'IPv6_PREFERRED']]

### responseType
- **Type**: typing.Optional[typing.Literal['ENDPOINTS', 'LOADBALANCER']]


# DurationTypeDef

### unit
- **Type**: typing.Optional[typing.Literal['ms', 's']]

### value
- **Type**: typing.Optional[int]


# EgressFilterTypeDef

### type
- **Type**: typing.Literal['ALLOW_ALL', 'DROP_ALL']
- **Required**: Yes


# FileAccessLogTypeDef

### path
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.LoggingFormatTypeDef]


# GatewayRouteDataTypeDef

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadataTypeDef'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteStatusTypeDef'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# GatewayRouteHostnameMatchTypeDef

### exact
- **Type**: typing.Optional[str]

### suffix
- **Type**: typing.Optional[str]


# GatewayRouteHostnameRewriteTypeDef

### defaultTargetHostname
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GatewayRouteRefTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# GatewayRouteSpecTypeDef

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteTypeDef]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteTypeDef]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteTypeDef]

### priority
- **Type**: typing.Optional[int]


# GatewayRouteStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# GatewayRouteTargetTypeDef

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteVirtualServiceTypeDef'>
- **Required**: Yes

### port
- **Type**: typing.Optional[int]


# GatewayRouteVirtualServiceTypeDef

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# GrpcGatewayRouteActionTypeDef

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteTargetTypeDef'>
- **Required**: Yes

### rewrite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteRewriteTypeDef]


# GrpcGatewayRouteMatchTypeDef

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameMatchTypeDef]

### metadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteMetadataTypeDef]]

### port
- **Type**: typing.Optional[int]

### serviceName
- **Type**: typing.Optional[str]


# GrpcGatewayRouteMetadataTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcMetadataMatchMethodTypeDef]


# GrpcGatewayRouteRewriteTypeDef

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameRewriteTypeDef]


# GrpcGatewayRouteTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteActionTypeDef'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteMatchTypeDef'>
- **Required**: Yes


# GrpcMetadataMatchMethodTypeDef

### exact
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MatchRangeTypeDef]

### regex
- **Type**: typing.Optional[str]

### suffix
- **Type**: typing.Optional[str]


# GrpcRetryPolicyTypeDef

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### perRetryTimeout
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef'>
- **Required**: Yes

### grpcRetryEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['cancelled', 'deadline-exceeded', 'internal', 'resource-exhausted', 'unavailable']]]

### httpRetryEvents
- **Type**: typing.Optional[typing.Sequence[str]]

### tcpRetryEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['connection-error']]]


# GrpcRouteActionTypeDef

### weightedTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTargetTypeDef]
- **Required**: Yes


# GrpcRouteMatchTypeDef

### metadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMetadataTypeDef]]

### methodName
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### serviceName
- **Type**: typing.Optional[str]


# GrpcRouteMetadataMatchMethodTypeDef

### exact
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MatchRangeTypeDef]

### regex
- **Type**: typing.Optional[str]

### suffix
- **Type**: typing.Optional[str]


# GrpcRouteMetadataTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMetadataMatchMethodTypeDef]


# GrpcRouteTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteActionTypeDef'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMatchTypeDef'>
- **Required**: Yes

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRetryPolicyTypeDef]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcTimeoutTypeDef]


# GrpcTimeoutTypeDef

### idle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef]

### perRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef]


# HeaderMatchMethodTypeDef

### exact
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MatchRangeTypeDef]

### regex
- **Type**: typing.Optional[str]

### suffix
- **Type**: typing.Optional[str]


# HealthCheckPolicyTypeDef

### healthyThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### intervalMillis
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['grpc', 'http', 'http2', 'tcp']
- **Required**: Yes

### timeoutMillis
- **Type**: <class 'int'>
- **Required**: Yes

### unhealthyThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### path
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]


# HttpGatewayRouteActionTypeDef

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteTargetTypeDef'>
- **Required**: Yes

### rewrite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteRewriteTypeDef]


# HttpGatewayRouteHeaderTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HeaderMatchMethodTypeDef]


# HttpGatewayRouteMatchTypeDef

### headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteHeaderTypeDef]]

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameMatchTypeDef]

### method
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE']]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpPathMatchTypeDef]

### port
- **Type**: typing.Optional[int]

### prefix
- **Type**: typing.Optional[str]

### queryParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.HttpQueryParameterTypeDef]]


# HttpGatewayRoutePathRewriteTypeDef

### exact
- **Type**: typing.Optional[str]


# HttpGatewayRoutePrefixRewriteTypeDef

### defaultPrefix
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### value
- **Type**: typing.Optional[str]


# HttpGatewayRouteRewriteTypeDef

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameRewriteTypeDef]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRoutePathRewriteTypeDef]

### prefix
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRoutePrefixRewriteTypeDef]


# HttpGatewayRouteTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteActionTypeDef'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteMatchTypeDef'>
- **Required**: Yes


# HttpPathMatchTypeDef

### exact
- **Type**: typing.Optional[str]

### regex
- **Type**: typing.Optional[str]


# HttpQueryParameterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.QueryParameterMatchTypeDef]


# HttpRetryPolicyTypeDef

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### perRetryTimeout
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef'>
- **Required**: Yes

### httpRetryEvents
- **Type**: typing.Optional[typing.Sequence[str]]

### tcpRetryEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['connection-error']]]


# HttpRouteActionTypeDef

### weightedTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTargetTypeDef]
- **Required**: Yes


# HttpRouteHeaderTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HeaderMatchMethodTypeDef]


# HttpRouteMatchTypeDef

### headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteHeaderTypeDef]]

### method
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE']]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpPathMatchTypeDef]

### port
- **Type**: typing.Optional[int]

### prefix
- **Type**: typing.Optional[str]

### queryParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.HttpQueryParameterTypeDef]]

### scheme
- **Type**: typing.Optional[typing.Literal['http', 'https']]


# HttpRouteTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteActionTypeDef'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteMatchTypeDef'>
- **Required**: Yes

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRetryPolicyTypeDef]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpTimeoutTypeDef]


# HttpTimeoutTypeDef

### idle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef]

### perRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef]


# JsonFormatRefTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ListGatewayRoutesInputListGatewayRoutesPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListGatewayRoutesInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListGatewayRoutesOutputTypeDef

### gatewayRoutes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteRefTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMeshesInputListMeshesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListMeshesInputRequestTypeDef

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMeshesOutputTypeDef

### meshes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.MeshRefTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoutesInputListRoutesPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListRoutesInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListRoutesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.RouteRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputListTagsForResourcePaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualGatewaysInputListVirtualGatewaysPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListVirtualGatewaysInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualGatewaysOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualNodesInputListVirtualNodesPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListVirtualNodesInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualNodesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### virtualNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualRoutersInputListVirtualRoutersPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListVirtualRoutersInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualRoutersOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouters
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualServicesInputListVirtualServicesPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListVirtualServicesInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualServicesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### virtualServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListenerTimeoutTypeDef

### grpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcTimeoutTypeDef]

### http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpTimeoutTypeDef]

### http2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpTimeoutTypeDef]

### tcp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpTimeoutTypeDef]


# ListenerTlsAcmCertificateTypeDef

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListenerTlsCertificateTypeDef

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsAcmCertificateTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsFileCertificateTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsSdsCertificateTypeDef]


# ListenerTlsFileCertificateTypeDef

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### privateKey
- **Type**: <class 'str'>
- **Required**: Yes


# ListenerTlsSdsCertificateTypeDef

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# ListenerTlsTypeDef

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsCertificateTypeDef'>
- **Required**: Yes

### mode
- **Type**: typing.Literal['DISABLED', 'PERMISSIVE', 'STRICT']
- **Required**: Yes

### validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsValidationContextTypeDef]


# ListenerTlsValidationContextTrustTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextFileTrustTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextSdsTrustTypeDef]


# ListenerTlsValidationContextTypeDef

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsValidationContextTrustTypeDef'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesTypeDef]


# ListenerTypeDef

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.PortMappingTypeDef'>
- **Required**: Yes

### connectionPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeConnectionPoolTypeDef]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HealthCheckPolicyTypeDef]

### outlierDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.OutlierDetectionTypeDef]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTimeoutTypeDef]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsTypeDef]


# LoggingFormatTypeDef

### json
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.JsonFormatRefTypeDef]]

### text
- **Type**: typing.Optional[str]


# LoggingTypeDef

### accessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AccessLogTypeDef]


# MatchRangeTypeDef

### end
- **Type**: <class 'int'>
- **Required**: Yes

### start
- **Type**: <class 'int'>
- **Required**: Yes


# MeshDataTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadataTypeDef'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshSpecTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshStatusTypeDef'>
- **Required**: Yes


# MeshRefTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes


# MeshServiceDiscoveryTypeDef

### ipPreference
- **Type**: typing.Optional[typing.Literal['IPv4_ONLY', 'IPv4_PREFERRED', 'IPv6_ONLY', 'IPv6_PREFERRED']]


# MeshSpecTypeDef

### egressFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.EgressFilterTypeDef]

### serviceDiscovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MeshServiceDiscoveryTypeDef]


# MeshStatusTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']]


# OutlierDetectionTypeDef

### baseEjectionDuration
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef'>
- **Required**: Yes

### interval
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef'>
- **Required**: Yes

### maxEjectionPercent
- **Type**: <class 'int'>
- **Required**: Yes

### maxServerErrors
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortMappingTypeDef

### port
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['grpc', 'http', 'http2', 'tcp']
- **Required**: Yes


# QueryParameterMatchTypeDef

### exact
- **Type**: typing.Optional[str]


# ResourceMetadataTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### meshOwner
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### uid
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# RouteDataTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadataTypeDef'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteStatusTypeDef'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes


# RouteRefTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes


# RouteSpecTypeDef

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteTypeDef]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteTypeDef]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteTypeDef]

### priority
- **Type**: typing.Optional[int]

### tcpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteTypeDef]


# RouteStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# ServiceDiscoveryTypeDef

### awsCloudMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapServiceDiscoveryTypeDef]

### dns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DnsServiceDiscoveryTypeDef]


# SubjectAlternativeNameMatchersTypeDef

### exact
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SubjectAlternativeNamesTypeDef

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNameMatchersTypeDef'>
- **Required**: Yes


# TagRefTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]
- **Required**: Yes


# TcpRouteActionTypeDef

### weightedTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTargetTypeDef]
- **Required**: Yes


# TcpRouteMatchTypeDef

### port
- **Type**: typing.Optional[int]


# TcpRouteTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteActionTypeDef'>
- **Required**: Yes

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteMatchTypeDef]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpTimeoutTypeDef]


# TcpTimeoutTypeDef

### idle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef]


# TlsValidationContextAcmTrustTypeDef

### certificateAuthorityArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TlsValidationContextFileTrustTypeDef

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes


# TlsValidationContextSdsTrustTypeDef

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# TlsValidationContextTrustTypeDef

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextAcmTrustTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextFileTrustTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextSdsTrustTypeDef]


# TlsValidationContextTypeDef

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextTrustTypeDef'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesTypeDef]


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGatewayRouteInputRequestTypeDef

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecTypeDef'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateGatewayRouteOutputTypeDef

### gatewayRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMeshInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MeshSpecTypeDef]


# UpdateMeshOutputTypeDef

### mesh
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRouteInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecTypeDef'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateRouteOutputTypeDef

### route
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVirtualGatewayInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecTypeDef'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateVirtualGatewayOutputTypeDef

### virtualGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVirtualNodeInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecTypeDef'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateVirtualNodeOutputTypeDef

### virtualNode
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVirtualRouterInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecTypeDef'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateVirtualRouterOutputTypeDef

### virtualRouter
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVirtualServiceInputRequestTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceSpecTypeDef'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateVirtualServiceOutputTypeDef

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VirtualGatewayAccessLogTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayFileAccessLogTypeDef]


# VirtualGatewayBackendDefaultsTypeDef

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicyTypeDef]


# VirtualGatewayClientPolicyTlsTypeDef

### validation
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextTypeDef'>
- **Required**: Yes

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientTlsCertificateTypeDef]

### enforce
- **Type**: typing.Optional[bool]

### ports
- **Type**: typing.Optional[typing.Sequence[int]]


# VirtualGatewayClientPolicyTypeDef

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicyTlsTypeDef]


# VirtualGatewayClientTlsCertificateTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsFileCertificateTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsSdsCertificateTypeDef]


# VirtualGatewayConnectionPoolTypeDef

### grpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayGrpcConnectionPoolTypeDef]

### http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayHttpConnectionPoolTypeDef]

### http2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayHttp2ConnectionPoolTypeDef]


# VirtualGatewayDataTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadataTypeDef'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayStatusTypeDef'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayFileAccessLogTypeDef

### path
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.LoggingFormatTypeDef]


# VirtualGatewayGrpcConnectionPoolTypeDef

### maxRequests
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualGatewayHealthCheckPolicyTypeDef

### healthyThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### intervalMillis
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['grpc', 'http', 'http2']
- **Required**: Yes

### timeoutMillis
- **Type**: <class 'int'>
- **Required**: Yes

### unhealthyThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### path
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]


# VirtualGatewayHttp2ConnectionPoolTypeDef

### maxRequests
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualGatewayHttpConnectionPoolTypeDef

### maxConnections
- **Type**: <class 'int'>
- **Required**: Yes

### maxPendingRequests
- **Type**: typing.Optional[int]


# VirtualGatewayListenerTlsAcmCertificateTypeDef

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayListenerTlsCertificateTypeDef

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsAcmCertificateTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsFileCertificateTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsSdsCertificateTypeDef]


# VirtualGatewayListenerTlsFileCertificateTypeDef

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### privateKey
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayListenerTlsSdsCertificateTypeDef

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayListenerTlsTypeDef

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsCertificateTypeDef'>
- **Required**: Yes

### mode
- **Type**: typing.Literal['DISABLED', 'PERMISSIVE', 'STRICT']
- **Required**: Yes

### validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsValidationContextTypeDef]


# VirtualGatewayListenerTlsValidationContextTrustTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextFileTrustTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextSdsTrustTypeDef]


# VirtualGatewayListenerTlsValidationContextTypeDef

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsValidationContextTrustTypeDef'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesTypeDef]


# VirtualGatewayListenerTypeDef

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayPortMappingTypeDef'>
- **Required**: Yes

### connectionPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayConnectionPoolTypeDef]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayHealthCheckPolicyTypeDef]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsTypeDef]


# VirtualGatewayLoggingTypeDef

### accessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayAccessLogTypeDef]


# VirtualGatewayPortMappingTypeDef

### port
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['grpc', 'http', 'http2']
- **Required**: Yes


# VirtualGatewayRefTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewaySpecTypeDef

### listeners
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTypeDef]
- **Required**: Yes

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayBackendDefaultsTypeDef]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayLoggingTypeDef]


# VirtualGatewayStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# VirtualGatewayTlsValidationContextAcmTrustTypeDef

### certificateAuthorityArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VirtualGatewayTlsValidationContextFileTrustTypeDef

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayTlsValidationContextSdsTrustTypeDef

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayTlsValidationContextTrustTypeDef

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextAcmTrustTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextFileTrustTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextSdsTrustTypeDef]


# VirtualGatewayTlsValidationContextTypeDef

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextTrustTypeDef'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesTypeDef]


# VirtualNodeConnectionPoolTypeDef

### grpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeGrpcConnectionPoolTypeDef]

### http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeHttpConnectionPoolTypeDef]

### http2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeHttp2ConnectionPoolTypeDef]

### tcp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeTcpConnectionPoolTypeDef]


# VirtualNodeDataTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadataTypeDef'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeStatusTypeDef'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualNodeGrpcConnectionPoolTypeDef

### maxRequests
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualNodeHttp2ConnectionPoolTypeDef

### maxRequests
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualNodeHttpConnectionPoolTypeDef

### maxConnections
- **Type**: <class 'int'>
- **Required**: Yes

### maxPendingRequests
- **Type**: typing.Optional[int]


# VirtualNodeRefTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualNodeServiceProviderTypeDef

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualNodeSpecTypeDef

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.BackendDefaultsTypeDef]

### backends
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.BackendTypeDef]]

### listeners
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTypeDef]]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.LoggingTypeDef]

### serviceDiscovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ServiceDiscoveryTypeDef]


# VirtualNodeStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# VirtualNodeTcpConnectionPoolTypeDef

### maxConnections
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualRouterDataTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadataTypeDef'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterStatusTypeDef'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualRouterListenerTypeDef

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.PortMappingTypeDef'>
- **Required**: Yes


# VirtualRouterRefTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualRouterServiceProviderTypeDef

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualRouterSpecTypeDef

### listeners
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterListenerTypeDef]]


# VirtualRouterStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# VirtualServiceBackendTypeDef

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyTypeDef]


# VirtualServiceDataTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadataTypeDef'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceSpecTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceStatusTypeDef'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualServiceProviderTypeDef

### virtualNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeServiceProviderTypeDef]

### virtualRouter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterServiceProviderTypeDef]


# VirtualServiceRefTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: <class 'str'>
- **Required**: Yes

### resourceOwner
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'int'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualServiceSpecTypeDef

### provider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceProviderTypeDef]


# VirtualServiceStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# WeightedTargetTypeDef

### virtualNode
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: <class 'int'>
- **Required**: Yes

### port
- **Type**: typing.Optional[int]


